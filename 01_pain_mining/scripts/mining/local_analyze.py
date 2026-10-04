#!/usr/bin/env python3
"""
10조 스튜디오 — 로컬 모델 기반 불편 분석 자동화
Ollama(llama3.2:1b)로 자막/리뷰에서 불편 포인트를 추출해 painpoints.json에 추가.

사용:
  python 01_pain_mining/scripts/mining/local_analyze.py
  python 01_pain_mining/scripts/mining/local_analyze.py --dry-run
"""
import json
import os
import re
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(r"D:\10jo_Studio")
OLLAMA_URL = "http://127.0.0.1:11434"
MODEL = "llama3.2:1b"
PAINPOINTS_JSON = ROOT / "01_pain_mining" / "data" / "processed" / "painpoints.json"
RAW_DIR = ROOT / "01_pain_mining" / "raw" / "2026-10-04"

SYSTEM_PROMPT = """너는 10조 스튜디오의 불편 분석가다.
주어진 텍스트(유튜브 자막, 앱 리뷰, 커뮤니티 글)에서 **사람들이 실제로 돈을 내고서라도 없애고 싶어 하는 불편**만 추출한다.

규칙:
1. 불편 1건당 아래 JSON 형식으로 출력한다.
2. "불편"이 아닌 것(일반 정보, 기능 소개, 광고, 감상)은 제외한다.
3. 이미 알려진 불편과 중복되면 새로 만들지 않는다.
4. 출력은 JSON 배열만. 설명·마크다운 불필요.

출력 형식:
[
  {
    "id": "P-00XX",
    "title": "불편 제목 (20자 이내)",
    "description": "구체적 상황과 고통 (2~3문장)",
    "source": "유튜브/앱리뷰/커뮤니티",
    "source_url": "URL 또는 파일명",
    "willingness": "높음/중간/낮음",
    "category": "카테고리",
    "evidence": "원문 인용 (1문장)"
  }
]

불편이 없으면 [] 만 출력한다.
"""


def call_ollama(prompt: str, max_tokens: int = 2048) -> str:
    """Ollama API 호출"""
    payload = json.dumps({
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
        "stream": False,
        "options": {"temperature": 0.3, "max_tokens": max_tokens},
    }).encode("utf-8")

    req = urllib.request.Request(
        f"{OLLAMA_URL}/api/chat",
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    return data["message"]["content"]


def parse_json_array(text: str) -> list:
    """LLM 출력에서 JSON 배열 추출"""
    # 코드 블록 제거
    text = re.sub(r"```json\s*", "", text)
    text = re.sub(r"```\s*", "", text)
    # JSON 배열 찾기
    match = re.search(r"\[.*\]", text, re.DOTALL)
    if not match:
        return []
    try:
        return json.loads(match.group())
    except json.JSONDecodeError:
        return []


# 프롬프트 템플릿 누출 탐지 패턴
TEMPLATE_LEAK_PATTERNS = [
    "20자 이내", "2~3문장", "구체적 상황과 고통", "URL 또는 파일명",
    "유튜브/앱리뷰/커뮤니티", "카테고리", "원문 인용",
    "불편 제목", "P-00XX", "높음/중간/낮음",
]


def is_quality_item(item: dict) -> tuple:
    """품질 게이트 — 부실 항목을 걸러낸다. (통과여부, 사유)"""
    title = (item.get("title") or "").strip()
    desc = (item.get("description") or "").strip()

    # 1. 필수 필드 존재
    if not title or not desc:
        return False, "제목 또는 설명 누락"

    # 2. 프롬프트 템플릿 누출
    for pat in TEMPLATE_LEAK_PATTERNS:
        if pat in title or pat in desc:
            return False, f"템플릿 누출: {pat}"

    # 3. 제목과 설명이 동일 (분석 없이 원문 복사)
    if title == desc:
        return False, "제목=설명 (분석 없음)"

    # 4. 제목이 너무 짧거나 원문 인용만
    if len(title) < 8:
        return False, f"제목 너무 짧음 ({len(title)}자)"

    # 5. 설명이 너무 짧음 (2~3문장 요구)
    if len(desc) < 40:
        return False, f"설명 너무 짧음 ({len(desc)}자)"

    # 6. 제목이 의문문/감탄문만 (불편 정의 아님)
    if title.endswith("?") and len(title) < 25:
        return False, "제목이 의문문"

    return True, "OK"


def load_existing() -> list:
    if PAINPOINTS_JSON.exists():
        with open(PAINPOINTS_JSON, encoding="utf-8") as f:
            return json.load(f)
    return []


def next_id(existing: list) -> str:
    max_num = 0
    for item in existing:
        m = re.match(r"P-(\d+)", item.get("id", ""))
        if m:
            max_num = max(max_num, int(m.group(1)))
    return f"P-{max_num + 1:04d}"


def read_raw_files() -> list:
    """raw 디렉토리의 텍스트 파일 읽기"""
    files = []
    if RAW_DIR.exists():
        for f in sorted(RAW_DIR.glob("*.txt")):
            if f.name == "index.txt":
                continue
            try:
                content = f.read_text(encoding="utf-8")
                files.append({"name": f.name, "content": content})
            except Exception as e:
                print(f"  ⚠ {f.name} 읽기 실패: {e}")
    return files


def main():
    dry_run = "--dry-run" in sys.argv

    print("=== 10조 스튜디오 — 로컬 모델 불편 분석 ===")
    print(f"모델: {MODEL} (Ollama)")
    print(f"모드: {'DRY-RUN' if dry_run else '실행'}")
    print()

    # 1. 기존 불편 로드
    existing = load_existing()
    print(f"기존 불편: {len(existing)}건")

    # 2. 원본 파일 로드
    files = read_raw_files()
    print(f"분석 대상: {len(files)}개 파일")
    if not files:
        print("분석할 파일이 없습니다.")
        return

    # 3. 기존 불편 제목 집합 (중복 방지)
    existing_titles = {item.get("title", "") for item in existing}

    # 4. 파일별 분석
    new_items = []
    for i, f in enumerate(files, 1):
        print(f"\n[{i}/{len(files)}] {f['name']} ({len(f['content'])} chars)")

        # 긴 파일은 앞부분만
        content = f["content"][:8000]
        prompt = f"다음은 {f['name']}의 내용이다. 불편 포인트를 추출하라.\n\n{content}"

        try:
            result = call_ollama(prompt)
            items = parse_json_array(result)
            print(f"  → {len(items)}건 추출")

            for item in items:
                # 품질 게이트 통과 확인
                ok, reason = is_quality_item(item)
                if not ok:
                    print(f"  ✗ 품질 미달 제외: {reason} — {(item.get('title') or '')[:30]}")
                    continue

                # ID 부여
                item["id"] = next_id(existing + new_items)
                # 중복 체크
                if item.get("title", "") in existing_titles:
                    print(f"  ⚠ 중복 제외: {item.get('title', '')[:40]}")
                    continue
                existing_titles.add(item.get("title", ""))
                new_items.append(item)
                print(f"  ✓ {item['id']}: {item.get('title', '')[:50]}")

        except Exception as e:
            print(f"  ✗ 분석 실패: {e}")

        # API 부하 방지
        if i < len(files):
            time.sleep(1)

    # 5. 결과 저장
    print(f"\n=== 분석 완료: {len(new_items)}건 신규 추출 ===")
    for item in new_items:
        print(f"  {item['id']}: {item.get('title', '')[:60]}")

    if dry_run:
        print("\n[DRY-RUN] 저장하지 않습니다.")
        return

    if new_items:
        all_items = existing + new_items
        with open(PAINPOINTS_JSON, "w", encoding="utf-8") as f:
            json.dump(all_items, f, ensure_ascii=False, indent=2)
        print(f"\n✅ {PAINPOINTS_JSON}에 저장 (총 {len(all_items)}건)")
    else:
        print("\n신규 불편 없음.")


if __name__ == "__main__":
    main()
