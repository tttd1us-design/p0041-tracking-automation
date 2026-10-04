#!/usr/bin/env python3
"""
Antigravity 브리지 — 10조 스튜디오 수석이 Antigravity(Gemini 기반)에 직접 질문하고 응답을 받는다.

배경: Antigravity는 Electron GUI 앱이라 자동화가 불가능하다고 판단했으나,
      resources/bin/language_server.exe 의 `agentapi` 서브커맨드로 CLI 접점이 존재함을 확인.
      (2026-10-03 실측: 대화 생성 + send-message + 응답 수신 모두 성공)

사용법:
    python antigravity_bridge.py "질문 내용" [--model=flash|pro|flash_lite] [--timeout=120]

전제:
    - Antigravity 앱이 실행 중이어야 한다 (language_server.exe 가 떠 있어야 함)
    - 스크립트가 자동으로 포트·CSRF 토큰·프로젝트 ID를 찾는다

출력:
    Antigravity의 응답 텍스트 (stdout)

주의:
    - 응답은 로컬 SQLite(conversations/<id>.db)의 protobuf step_payload에서 추출한다.
    - 무료로 사용 가능 (대표님 Google 계정의 Antigravity 할당량 사용).
"""
import argparse
import glob
import os
import re
import sqlite3
import subprocess
import sys
import time
import json

EXE = r"C:\Users\sangwan.lee\AppData\Local\Programs\antigravity\resources\bin\language_server.exe"
CONV_DIR = r"C:\Users\sangwan.lee\.gemini\antigravity\conversations"
PROJ_DIR = r"C:\Users\sangwan.lee\.gemini\config\projects"


def find_ls_process():
    """language_server.exe 프로세스에서 포트·CSRF 토큰을 찾는다."""
    ps = (
        'Get-CimInstance Win32_Process -Filter "name=\'language_server.exe\'" | '
        'Select-Object ProcessId, CommandLine | ConvertTo-Json -Depth 3'
    )
    try:
        r = subprocess.run(["powershell", "-NoProfile", "-Command", ps],
                           capture_output=True, text=True, timeout=60)
        data = json.loads(r.stdout)
    except Exception:
        return None
    if isinstance(data, dict):
        data = [data]
    for proc in data:
        cmd = proc.get("CommandLine") or ""
        m = re.search(r"--csrf_token\s+([0-9a-f\-]+)", cmd)
        if m:
            return {"pid": proc.get("ProcessId"), "csrf": m.group(1)}
    return None


def find_port(pid):
    """해당 PID가 듣는 gRPC 포트를 찾는다. (agentapi 는 --https_server_port 0 로 뜬 포트)"""
    try:
        r = subprocess.run(["netstat", "-ano"], capture_output=True, timeout=60)
    except Exception:
        return None
    raw = r.stdout or b""
    text = raw.decode("cp949", errors="replace")
    cands = []
    for line in text.splitlines():
        if "LISTENING" not in line:
            continue
        parts = line.split()
        if len(parts) >= 5 and parts[-1] == str(pid):
            addr = parts[1]
            try:
                port = int(addr.rsplit(":", 1)[1])
            except ValueError:
                continue
            cands.append(port)
    return cands


def pick_grpc_port(pid, csrf):
    """후보 포트 중 agentapi 가 실제로 응답하는 포트를 고른다."""
    env = os.environ.copy()
    env["ANTIGRAVITY_CSRF_TOKEN"] = csrf
    for port in find_port(pid) or []:
        env["ANTIGRAVITY_LS_ADDRESS"] = f"127.0.0.1:{port}"
        try:
            r = subprocess.run([EXE, "agentapi", "get-conversation-metadata", "00000000-0000-0000-0000-000000000000"],
                               capture_output=True, text=True, timeout=25, env=env,
                               encoding="utf-8", errors="replace")
            out = r.stdout or ""
            # 인증 통과 신호: 'missing CSRF token' 이 아니면 이 포트가 맞다
            if "missing CSRF token" not in out and "connection error" not in out:
                return port, env
        except Exception:
            continue
    return None, env


def find_project_id():
    """기존 프로젝트 ID를 반환 (없으면 outside-of-project)."""
    try:
        files = [f for f in glob.glob(os.path.join(PROJ_DIR, "*.json")) if "outside" not in f]
        if files:
            with open(files[0], encoding="utf-8") as fh:
                return json.load(fh).get("id")
    except Exception:
        pass
    return "outside-of-project"


def _read_varint(buf, pos):
    """protobuf varint 읽기. (value, new_pos) 반환."""
    result = 0
    shift = 0
    while pos < len(buf):
        b = buf[pos]
        result |= (b & 0x7F) << shift
        pos += 1
        if not (b & 0x80):
            return result, pos
        shift += 7
        if shift > 63:
            raise ValueError("varint too long")
    raise ValueError("truncated varint")


def _parse_wire_fields(buf):
    """protobuf wire-format 파싱: length-delimited 필드(wire_type=2)만 추출."""
    fields = []
    pos = 0
    while pos < len(buf):
        try:
            tag, pos = _read_varint(buf, pos)
        except ValueError:
            break
        field_number = tag >> 3
        wire_type = tag & 0x07
        if wire_type == 0:  # varint
            _, pos = _read_varint(buf, pos)
        elif wire_type == 1:  # 64-bit
            pos += 8
        elif wire_type == 2:  # length-delimited
            try:
                length, pos = _read_varint(buf, pos)
            except ValueError:
                break
            if pos + length <= len(buf):
                fields.append((field_number, buf[pos:pos + length]))
                pos += length
            else:
                break
        elif wire_type == 5:  # 32-bit
            pos += 4
        else:
            break
    return fields


def extract_reply(payload):
    """step_payload(protobuf)에서 assistant 응답 텍스트를 뽑는다.

    클로드 조언 (2026-10-03) 반영:
      - 정규식 휴리스틱 대신 protobuf wire-format을 직접 파싱
      - length-delimited 필드 중 유효 UTF-8 텍스트만 추출
      - 가장 긴 텍스트 필드를 응답으로 선택
      - reasoning_content 필드는 제외 (2026-10-03 수정)
    """
    if not payload:
        return ""
    
    # 1단계: protobuf wire-format 파싱
    try:
        fields = _parse_wire_fields(payload)
        text_fields = []
        for _, data in fields:
            try:
                text = data.decode("utf-8")
                # reasoning 필드 제외
                if "reasoning" in text.lower() or "thinking" in text.lower():
                    continue
                # 의미 있는 문자가 있는지 확인
                if re.search(r'[\uac00-\ud7a3a-zA-Z]', text):
                    text_fields.append(text)
            except UnicodeDecodeError:
                continue
        if text_fields:
            # 가장 긴 텍스트 필드 선택 (응답 본문이 가장 길다)
            return max(text_fields, key=len).strip()
    except Exception:
        pass
    
    # 2단계: 폴백 — 제어문자 split + 정규식
    text = payload.decode("utf-8", errors="replace")
    m = re.search(r'\*\*[^*]+\*\*[^\x00-\x1f]*', text)
    if m:
        return m.group(0).strip()
    segs = re.split(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', text)
    candidates = []
    for s in segs:
        clean = re.sub(r'[^\w\s\*\-\.\,\;\:\!\?\(\)\[\]\{\}\"\'\\\/\+\=\<\>\#\&\\%\@]', '', s)
        if re.search(r'[\uac00-\ud7a3a-zA-Z]', clean):
            candidates.append(clean.strip())
    if not candidates:
        return ""
    return max(candidates, key=len)


def wait_reply(cid, timeout=180, poll=6):
    """대화 DB의 steps 에서 마지막 assistant 응답을 추출한다.

    클로드 조언 (2026-10-03) 반영:
      - 상태기반 완료판정: 응답이 안정되면 완료
      - 추출 실패가 timeout으로 위장되지 않도록 명시적 에러 반환
      - payload 길이/해시 로깅
    """
    path = os.path.join(CONV_DIR, f"{cid}.db")
    deadline = time.time() + timeout
    best = ""
    stable = 0
    empty_count = 0
    last_payload_len = 0
    last_payload_hash = ""
    
    while time.time() < deadline:
        time.sleep(poll)
        if not os.path.exists(path):
            continue
        try:
            con = sqlite3.connect(f"file:{path}?mode=ro", uri=True, timeout=10)
            cur = con.cursor()
            cur.execute(
                "SELECT step_payload FROM steps "
                "WHERE step_type=15 AND step_payload IS NOT NULL ORDER BY idx DESC LIMIT 1"
            )
            row = cur.fetchone()
            con.close()
        except Exception:
            continue
        if not row or not row[0]:
            empty_count += 1
            # 추출 실패가 지속되면 명시적 에러 반환 (timeout 위장 방지)
            if empty_count >= 5:
                return f"[오류] 응답 추출 실패 (payload 없음, {empty_count}회 시도)"
            continue
        
        payload = row[0]
        payload_len = len(payload)
        payload_hash = hash(payload)
        
        # payload가 변경되면 진행 중
        if payload_len != last_payload_len or payload_hash != last_payload_hash:
            last_payload_len = payload_len
            last_payload_hash = payload_hash
            empty_count = 0
        
        cand = extract_reply(payload)
        if cand and cand != best:
            best = cand
            stable = 0
        elif best:
            stable += 1
            if stable >= 2:      # 응답이 두 번 연속 그대로면 완료로 본다
                break
    
    # 타임아웃 시 명시적 에러
    if not best and empty_count > 0:
        return f"[오류] 응답 추출 실패 (타임아웃, {empty_count}회 시도)"
    
    return best


def ask(prompt, model="flash", timeout=180):
    proc = find_ls_process()
    if not proc:
        return "[오류] Antigravity가 실행 중이 아닙니다. Antigravity 앱을 먼저 실행하세요."
    port, env = pick_grpc_port(proc["pid"], proc["csrf"])
    if not port:
        return "[오류] language_server 의 gRPC 포트를 찾지 못했습니다."
    env["ANTIGRAVITY_PROJECT_ID"] = find_project_id()
    env["ANTIGRAVITY_LS_ADDRESS"] = f"127.0.0.1:{port}"

    r = subprocess.run([EXE, "agentapi", "new-conversation", f"--model={model}",
                        "--title=10jo", prompt],
                       capture_output=True, text=True, timeout=120, env=env,
                       encoding="utf-8", errors="replace")
    try:
        cid = json.loads(r.stdout)["response"]["newConversation"]["conversationId"]
    except Exception:
        return f"[오류] 대화 생성 실패: {r.stdout[:400]}"
    return wait_reply(cid, timeout=timeout)


def main():
    ap = argparse.ArgumentParser(description="Antigravity 브리지")
    ap.add_argument("prompt", help="Antigravity에 물어볼 내용")
    ap.add_argument("--model", default="flash", choices=["flash_lite", "flash", "pro"])
    ap.add_argument("--timeout", type=int, default=180)
    a = ap.parse_args()
    out = ask(a.prompt, a.model, a.timeout)
    print(out)
    return 0 if out and not out.startswith("[오류]") else 1


if __name__ == "__main__":
    sys.exit(main())
