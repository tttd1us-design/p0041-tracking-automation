#!/usr/bin/env python3
"""10조 스튜디오 — 체크포인트 (수시 저장).

대표 지시(2026-10-04): "작업중인 내용을 수시로 저장해서 컴퓨터 서버가 다운되어도
재부팅 후 원활하게 업무가 진행될 수 있도록 해줘."

설계:
  - 작업 상태를 JSON 한 파일에 스냅샷한다 (원자적 쓰기 — 다운 중에도 안 깨짐).
  - 진행결과물(05_reports, 01_pain_mining/data 등)은 절대 삭제하지 않는다.
  - 시스템 운영파일(로그·임시·캐시)만 7일 경과 후 정리한다.
  - 체크포인트 자체는 최근 50개만 보관한다.

사용:
  python checkpoint.py save "메모"        # 현재 상태 스냅샷
  python checkpoint.py list               # 최근 체크포인트 목록
  python checkpoint.py restore            # 최신 체크포인트를 STATE.md 로 복원
  python checkpoint.py prune              # 7일 경과 운영파일 정리

저장 위치: D:/10jo_Studio/_shared/checkpoints/
"""
from __future__ import annotations

import json
import os
import shutil
import sys
import tempfile
from datetime import datetime, timedelta
from pathlib import Path

ROOT = Path("D:/10jo_Studio")
CKPT_DIR = ROOT / "_shared" / "checkpoints"
STATE_MD = ROOT / "_shared" / "STATE.md"
LATEST = CKPT_DIR / "LATEST.json"
KEEP_CKPT = 50          # 체크포인트 보관 개수
PRUNE_DAYS = 7          # 운영파일 정리 기준 (대표 지시)

# 진행결과물 — 절대 삭제 금지
NEVER_DELETE = [
    "05_reports", "01_pain_mining/data", "01_pain_mining/reports",
    "02_product_spec", "03_apps_dev/projects", "04_deployment",
    "_docs", "_shared", "_tools",
]

# 7일 경과 후 정리 가능한 운영파일 패턴 (상대경로 glob)
PRUNABLE = [
    "_logs/*.log",
    "_logs/*.txt",
    "01_pain_mining/raw/*/*.vtt",
    "01_pain_mining/raw/*/*.webm",
    "01_pain_mining/raw/*/*.mp4",
    "_shared/tmp/*",
    "05_reports/*.png",           # 스크린샷 (보고서 PDF는 보존)
    "05_reports/*.html",          # 중간 산출물 (PDF는 보존)
    "03_apps_dev/projects/*/.next/**",
    "03_apps_dev/projects/*/out/**",
]


def _atomic_write(path: Path, text: str) -> None:
    """원자적 쓰기 — 서버가 쓰는 중에 죽어도 파일이 깨지지 않는다."""
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=str(path.parent), suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(text)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, path)   # 원자적 교체
    except Exception:
        if os.path.exists(tmp):
            os.unlink(tmp)
        raise


def _scan_workspace() -> dict:
    """작업공간 핵심 상태를 수집한다."""
    state: dict = {"generated_at": datetime.now().isoformat(timespec="seconds")}

    # 1) 불편 데이터
    pp = ROOT / "01_pain_mining/data/processed/painpoints.json"
    if pp.exists():
        try:
            items = json.loads(pp.read_text(encoding="utf-8"))
            if isinstance(items, dict):
                items = items.get("painpoints", [])
            state["painpoints_count"] = len(items)
            state["painpoints_last_id"] = items[-1].get("id") if items else None
        except Exception as e:
            state["painpoints_error"] = str(e)

    # 2) 보고서
    rep = ROOT / "05_reports"
    if rep.exists():
        pdfs = sorted(rep.glob("*.pdf"), key=lambda p: p.stat().st_mtime, reverse=True)
        state["reports_count"] = len(pdfs)
        state["reports_latest"] = [p.name for p in pdfs[:5]]

    # 3) 스펙
    specs = ROOT / "02_product_spec"
    if specs.exists():
        state["specs"] = [str(p.relative_to(ROOT)) for p in specs.rglob("*.md")][:20]

    # 4) 프로젝트
    proj = ROOT / "03_apps_dev/projects"
    if proj.exists():
        state["projects"] = [p.name for p in proj.iterdir() if p.is_dir()]

    # 5) 백업
    bk = ROOT / "04_deployment/backups"
    if bk.exists():
        state["backups"] = {
            kind: len(list((bk / kind).glob("*.tar.gz")))
            for kind in ("daily", "weekly", "monthly") if (bk / kind).exists()
        }

    # 6) 열린 작업 (Kanban)
    try:
        import subprocess
        out = subprocess.run(["hermes", "kanban", "stats"],
                             capture_output=True, text=True, encoding="utf-8",
                             errors="replace", timeout=30, shell=True)
        state["kanban_raw"] = (out.stdout or "")[:600]
    except Exception as e:
        state["kanban_error"] = str(e)

    return state


def cmd_save(note: str = "") -> int:
    CKPT_DIR.mkdir(parents=True, exist_ok=True)
    state = _scan_workspace()
    state["note"] = note
    stamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")

    # 개별 체크포인트
    _atomic_write(CKPT_DIR / f"ckpt_{stamp}.json",
                  json.dumps(state, ensure_ascii=False, indent=2))
    # 최신 포인터 (원자적)
    _atomic_write(LATEST, json.dumps(state, ensure_ascii=False, indent=2))

    # 사람이 읽는 STATE.md (재부팅 후 이걸 보면 된다)
    md = [f"# 10조 스튜디오 작업 상태 (체크포인트)", "",
          f"**저장 시각:** {state['generated_at']}",
          f"**메모:** {note or '(없음)'}", "", "---", ""]
    md.append(f"- 불편 데이터: **{state.get('painpoints_count', '?')}건** "
              f"(마지막 {state.get('painpoints_last_id', '?')})")
    md.append(f"- 보고서 PDF: **{state.get('reports_count', '?')}건**")
    if state.get("reports_latest"):
        md.append("  - 최근: " + ", ".join(state["reports_latest"][:3]))
    md.append(f"- 프로젝트: {', '.join(state.get('projects', [])) or '(없음)'}")
    if state.get("backups"):
        md.append(f"- 백업: " + ", ".join(f"{k} {v}개" for k, v in state["backups"].items()))
    md += ["", "## 열린 작업 (Kanban)", "", "```", state.get("kanban_raw", "(조회 실패)"), "```", ""]
    _atomic_write(STATE_MD, "\n".join(md))

    # 오래된 체크포인트 정리
    ckpts = sorted(CKPT_DIR.glob("ckpt_*.json"))
    for old in ckpts[:-KEEP_CKPT]:
        old.unlink(missing_ok=True)

    print(f"✅ 체크포인트 저장: {stamp} — 불편 {state.get('painpoints_count','?')}건, "
          f"보고서 {state.get('reports_count','?')}건")
    return 0


def cmd_list() -> int:
    ckpts = sorted(CKPT_DIR.glob("ckpt_*.json"), reverse=True)
    print(f"체크포인트 {len(ckpts)}개 (최근 15개)")
    for c in ckpts[:15]:
        try:
            d = json.loads(c.read_text(encoding="utf-8"))
            print(f"  {d.get('generated_at','?')} | 불편 {d.get('painpoints_count','?')} | "
                  f"보고서 {d.get('reports_count','?')} | {d.get('note','')[:30]}")
        except Exception:
            print(f"  {c.name} (읽기 실패)")
    return 0


def cmd_restore() -> int:
    if not LATEST.exists():
        print("❌ 체크포인트가 없습니다.")
        return 1
    d = json.loads(LATEST.read_text(encoding="utf-8"))
    print(f"최신 체크포인트: {d.get('generated_at')}")
    print(f"  불편 데이터: {d.get('painpoints_count','?')}건")
    print(f"  보고서: {d.get('reports_count','?')}건")
    print(f"  프로젝트: {', '.join(d.get('projects', []))}")
    print(f"→ STATE.md 갱신됨: {STATE_MD}")
    cmd_save("restore")
    return 0


def cmd_prune() -> int:
    """7일 경과 운영파일만 정리. 진행결과물은 절대 건드리지 않는다."""
    cutoff = datetime.now() - timedelta(days=PRUNE_DAYS)
    removed, kept, freed = 0, 0, 0

    for pattern in PRUNABLE:
        for path in ROOT.glob(pattern):
            if not path.is_file():
                continue
            rel = str(path.relative_to(ROOT)).replace("\\", "/")
            # 안전장치: 진행결과물 경로면 건너뛴다
            if any(rel.startswith(nd) for nd in NEVER_DELETE if not nd.endswith("reports")):
                kept += 1
                continue
            mtime = datetime.fromtimestamp(path.stat().st_mtime)
            if mtime < cutoff:
                try:
                    size = path.stat().st_size
                    path.unlink()
                    removed += 1
                    freed += size
                except Exception:
                    kept += 1
            else:
                kept += 1

    print(f"✅ 정리 완료 — 삭제 {removed}개 ({freed/1024/1024:.1f}MB), 보존 {kept}개")
    print(f"   기준: {PRUNE_DAYS}일 경과 운영파일만. 진행결과물(보고서·불편데이터·스펙)은 삭제 안 함.")
    return 0


def main() -> int:
    cmd = sys.argv[1] if len(sys.argv) > 1 else "save"
    note = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else ""
    if cmd == "save":
        return cmd_save(note)
    if cmd == "list":
        return cmd_list()
    if cmd == "restore":
        return cmd_restore()
    if cmd == "prune":
        return cmd_prune()
    print(__doc__)
    return 1


if __name__ == "__main__":
    sys.exit(main())
