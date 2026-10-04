#!/usr/bin/env bash
# 10조 스튜디오 — 재부팅 후 자동 복구
# 대표 지시(2026-10-04): "서버가 재부팅되고 꺼졌을때 서버가 재가동시 이전의 작업을 바로 시행할 수 있게 준비가 되어야."
#
# 이 스크립트는 재부팅 후 1회 실행하면 된다.
# 작업 폴더에 두고 바로 실행: bash _tools/resume_after_reboot.sh

set -uo pipefail

ROOT="D:/10jo_Studio"
PYBIN="D:/hermes/studio-py/Scripts/python.exe"
[ -x "$PYBIN" ] || PYBIN="python"

echo "=== 10조 스튜디오 재부팅 복구 ==="
echo "시각: $(date '+%Y-%m-%d %H:%M:%S')"
echo ""

# 1. 체크포인트 복원
echo "--- 1. 체크포인트 복원 ---"
CKPT="$ROOT/_tools/checkpoint.py"
if [ -f "$CKPT" ]; then
  "$PYBIN" "$CKPT" restore 2>&1
fi
echo ""

# 2. 마지막 작업 상태 확인
echo "--- 2. 마지막 작업 상태 ---"
STATE="$ROOT/_shared/STATE.md"
if [ -f "$STATE" ]; then
  head -20 "$STATE"
else
  echo "STATE.md 없음 — 체크포인트 목록 확인"
  "$PYBIN" "$CKPT" list 2>&1 | head -10
fi
echo ""

# 3. 백업 상태 확인
echo "--- 3. 백업 상태 ---"
for kind in daily weekly monthly; do
  count=$(ls -1 "$ROOT/04_deployment/backups/$kind"/*.tar.gz 2>/dev/null | wc -l)
  echo "  $kind: ${count}개"
done
echo ""

# 4. 크론 상태 확인
echo "--- 4. 크론 상태 ---"
hermes cron list 2>&1 | grep -E "Name:|Enabled:" | head -20
echo ""

# 5. 열린 작업 (Kanban)
echo "--- 5. 열린 작업 (Kanban) ---"
hermes kanban stats 2>&1 | head -15
echo ""

# 6. 디스크 여유
echo "--- 6. 디스크 여유 ---"
"$PYBIN" -c "
import shutil
for drive in ['C:/', 'D:/']:
    total, used, free = shutil.disk_usage(drive)
    print(f'  {drive} 여유: {free/1024**3:.1f}GB')
"
echo ""

# 7. 다음 작업 제안
echo "--- 7. 다음 작업 제안 ---"
echo "  1. 검증 에이전트 결과 확인 (P-0041, P-0045, P-0043)"
echo "  2. 불편 발굴 계속 (다른 주제 검색)"
echo "  3. 검증 통과 아이템 → 기획(spec) → 대표 승인 → 개발"
echo ""

echo "=== 복구 완료 ==="
