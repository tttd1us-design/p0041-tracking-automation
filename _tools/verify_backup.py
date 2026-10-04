#!/usr/bin/env python3
"""10조 스튜디오 — 백업 검증 (아카이브가 실제로 쓸모 있는지 확인).

대표 지시(2026-10-04): "백업의 중요한 부분은 항상 보관하여 백업하도록 해줘."
→ 백업이 '있다'와 '복구 가능하다'는 다르다. 이 스크립트로 매번 확인한다.

검사 항목:
  1) 아카이브가 2중 구조인가 (workspace + hermes_assets)
  2) 진행결과물이 들어갔는가 (05_reports, painpoints.json, 스펙)
  3) 스킬·크론이 들어갔는가 (SKILL.md 개수)
  4) 비밀값이 새지 않았는가 (.pem/.env/auth.json/token) — 0건이어야 정상

사용:
  python verify_backup.py                # 최신 daily 검증
  python verify_backup.py weekly         # 종류 지정
  python verify_backup.py daily <경로>   # 특정 파일
"""
from __future__ import annotations

import subprocess
import sys
import tarfile
import tempfile
from pathlib import Path

ROOT = Path("D:/10jo_Studio")
BACKUP_DIR = ROOT / "04_deployment/backups"
SECRET_PATTERNS = (".pem", ".env", "auth.json", "token", "credential")

# MSYS tar는 "D:/..." 경로를 원격 호스트로 오해한다.
# → 파이썬 tarfile을 쓴다 (경로 문제 없음).


def _names(tf: tarfile.TarFile) -> list[str]:
    return [m.name for m in tf.getmembers() if m.isfile()]


def verify(kind: str = "daily", path: Path | None = None) -> int:
    if path is None:
        files = sorted((BACKUP_DIR / kind).glob("*.tar.gz"),
                       key=lambda p: p.stat().st_mtime, reverse=True)
        if not files:
            print(f"❌ {kind} 백업이 없습니다: {BACKUP_DIR / kind}")
            return 1
        path = files[0]

    print(f"=== 백업 검증: {path.name} ({path.stat().st_size/1024/1024:.1f}MB) ===")
    ok = True

    with tarfile.open(path, "r:gz") as outer:
        outer_names = _names(outer)
        print(f"1) 구조: {', '.join(outer_names)}")

        # 2중 구조 확인
        has_ws = "workspace.tar.gz" in outer_names
        has_hermes = "hermes_assets.tar.gz" in outer_names
        if not (has_ws and has_hermes):
            print(f"   ❌ 2중 구조 아님 (workspace={has_ws}, hermes={has_hermes})")
            ok = False
        else:
            print("   ✅ 2중 구조 정상")

        tmp = Path(tempfile.mkdtemp(prefix="bkverify_"))
        outer.extractall(tmp)

        # 작업공간 검사
        if has_ws:
            with tarfile.open(tmp / "workspace.tar.gz", "r:gz") as ws:
                ws_names = _names(ws)
            reports = sum(1 for n in ws_names if "05_reports" in n)
            pains = sum(1 for n in ws_names if "painpoints.json" in n)
            specs = sum(1 for n in ws_names if "02_product_spec" in n)
            print(f"2) 진행결과물: 보고서 {reports}개, 불편데이터 {pains}개, 스펙 {specs}개")
            if reports == 0 or pains == 0:
                print("   ❌ 진행결과물 누락 — 복구 불가")
                ok = False
            else:
                print("   ✅ 진행결과물 포함")

        # Hermes 자산 검사
        if has_hermes:
            with tarfile.open(tmp / "hermes_assets.tar.gz", "r:gz") as ha:
                ha_names = _names(ha)
            skills = sum(1 for n in ha_names if n.endswith("SKILL.md"))
            cron = sum(1 for n in ha_names if "/cron/" in n and n.endswith(".json"))
            print(f"3) 회사 두뇌: 스킬 {skills}개, 크론 {cron}개")
            if skills == 0:
                print("   ❌ 스킬 누락 — 자동화 복구 불가")
                ok = False
            else:
                print("   ✅ 스킬·크론 포함")

            # 비밀값 검사
            leaked = [n for n in ha_names
                      if any(p in n.lower() for p in SECRET_PATTERNS)]
            print(f"4) 비밀값: {len(leaked)}건")
            if leaked:
                print(f"   ❌ 비밀값 유출: {leaked[:5]}")
                ok = False
            else:
                print("   ✅ 비밀값 없음 (안전)")

        # 정리
        import shutil
        shutil.rmtree(tmp, ignore_errors=True)

    print()
    print("✅ 백업 검증 통과 — 복구 가능" if ok else "❌ 백업 검증 실패 — 즉시 조치 필요")
    return 0 if ok else 1


def main() -> int:
    kind = sys.argv[1] if len(sys.argv) > 1 else "daily"
    path = Path(sys.argv[2]) if len(sys.argv) > 2 else None
    return verify(kind, path)


if __name__ == "__main__":
    sys.exit(main())
