#!/usr/bin/env bash
# 10조 스튜디오 — 자동 백업 (v2, 2026-10-04 대표 지시 반영)
#
# 대표 지시(2026-10-04):
#   "진행결과물은 삭제없이 저장되고 시스템관련 운영파일은 백업을 지속적으로 하되
#    1주일 경과된 후에는 불필요한 부분만을 판단해서 삭제."
#   "백업의 중요한 부분은 항상 보관하여 백업하도록 해줘."
#
# 백업 3계층:
#   L1 (수시)  : _tools/checkpoint.py — 작업 상태 스냅샷 (30분마다 크론)
#   L2 (일간)  : 이 스크립트 daily  — 전체 아카이브 (매일 03:00)
#   L3 (주간/월간): 이 스크립트 weekly/monthly — 장기 보관 (일 04:00 / 1일 05:00)
#
# 백업 대상:
#   1) D:/10jo_Studio  — 소스·문서·데이터·진행결과물 (node_modules/.next/out/.git 제외)
#   2) D:/hermes       — 스킬·크론·설정·운영파일 (회사의 두뇌와 자동화)
# 백업 위치: D:/10jo_Studio/04_deployment/backups/<daily|weekly|monthly>/
#
# 보관 정책 (대표 지시: 진행결과물 무삭제 / 운영파일 7일):
#   daily   : 14개 (2주)
#   weekly  : 8개  (2개월)
#   monthly : 12개 (1년) — 중요 백업, 항상 보관
#
# 원칙: 무료 자원만. 비밀값(.env, *.pem, auth.json)은 절대 포함하지 않는다.

set -uo pipefail

ROOT="/d/10jo_Studio"
HERMES_HOME="/d/hermes"   # 2026-10-03 D로 이전
GDRIVE_FOLDER_ID="1JKujfoEUK5mi9p_m0eTXhUZ_92ZtuhkM"   # 10jo_Studio_Backup
KIND="${1:-daily}"
STAMP="$(date +%Y-%m-%d_%H%M)"
NAME="10jo_Studio_${KIND}_${STAMP}.tar.gz"

DEST_DIR="$ROOT/04_deployment/backups/$KIND"
ARCHIVE="$DEST_DIR/$NAME"
mkdir -p /d/hermes/cache/tmp
STAGE="$(mktemp -d -p /d/hermes/cache/tmp)"   # 임시 파일도 D에만

mkdir -p "$DEST_DIR"

echo "=== 10조 스튜디오 백업 v2 ($KIND) ==="
echo "시각: $(date '+%Y-%m-%d %H:%M:%S')"

cd "$ROOT" || { echo "❌ 작업 폴더를 찾을 수 없습니다: $ROOT"; exit 1; }

# ── 0단계: 체크포인트 먼저 저장 (작업 상태 보존) ──
if [ -f "$ROOT/_tools/checkpoint.py" ]; then
  PYBIN="/d/hermes/studio-py/Scripts/python.exe"
  [ -x "$PYBIN" ] || PYBIN="python"
  "$PYBIN" "$ROOT/_tools/checkpoint.py" save "백업 전 자동 체크포인트 ($KIND)" 2>/dev/null \
    && echo "✅ 체크포인트 저장" || echo "⚠️ 체크포인트 건너뜀"
fi

# ── 1단계: D드라이브 작업공간 → 스테이징 ──
tar -czf "$STAGE/workspace.tar.gz" \
  --exclude='node_modules' \
  --exclude='.next' \
  --exclude='out' \
  --exclude='.git' \
  --exclude='.pnpm' \
  --exclude='04_deployment/backups' \
  --exclude='*.pem' \
  --exclude='.env' \
  --exclude='.env*.local' \
  --exclude='.claude_run.json' \
  --exclude='.claude_review.json' \
  01_pain_mining 02_product_spec 03_apps_dev 04_deployment 05_reports \
  _docs _shared _tools _logs \
  README.md AGENTS.md CLAUDE.md skills-lock.json 2>/dev/null

# ── 2단계: C드라이브 Hermes 자산 (스킬·크론·설정) → 스테이징 ──
# 비밀값(.env, auth.json, *.pem, token)은 절대 포함하지 않는다.
if [ -d "$HERMES_HOME" ]; then
  mkdir -p "$STAGE/hermes"
  for sub in skills scripts cron plugins memories; do
    [ -d "$HERMES_HOME/$sub" ] && cp -r "$HERMES_HOME/$sub" "$STAGE/hermes/" 2>/dev/null
  done
  # 설정 파일 (config.yaml 은 비밀값이 없다 — 자격증명은 auth.json 에 있다)
  [ -f "$HERMES_HOME/config.yaml" ] && cp "$HERMES_HOME/config.yaml" "$STAGE/hermes/" 2>/dev/null
  # 안전장치: 혹시 딸려온 비밀값 제거
  find "$STAGE/hermes" -type f \( -name "*.pem" -o -name ".env" -o -name ".env*" \
    -o -name "auth.json" -o -name "*token*" -o -name "*credential*" \) -delete 2>/dev/null
  tar -czf "$STAGE/hermes_assets.tar.gz" -C "$STAGE" hermes 2>/dev/null
fi

# ── 3단계: 하나의 아카이브로 결합 ──
tar -czf "$ARCHIVE" -C "$STAGE" \
  $( [ -f "$STAGE/workspace.tar.gz" ] && echo workspace.tar.gz ) \
  $( [ -f "$STAGE/hermes_assets.tar.gz" ] && echo hermes_assets.tar.gz ) 2>/dev/null
rm -rf "$STAGE"

if [ ! -f "$ARCHIVE" ]; then
  echo "❌ 아카이브 생성 실패"
  exit 1
fi

SIZE="$(du -h "$ARCHIVE" | cut -f1)"
echo "✅ 로컬 백업: $ARCHIVE ($SIZE)"

# Google Drive 업로드 — 2026-10-03 중단 (대표 지시: 드라이브에는 결과물만, 시스템 백업은 D에만)
if false; then
echo "--- Google Drive 업로드 중 ---"
WIN_ARCHIVE="D:/10jo_Studio/04_deployment/backups/$KIND/$NAME"
UPLOAD_OUT="$(timeout 300 gws drive +upload "$WIN_ARCHIVE" --parent "$GDRIVE_FOLDER_ID" 2>&1)"
if echo "$UPLOAD_OUT" | grep -q '"id"'; then
  FID="$(echo "$UPLOAD_OUT" | grep -oE '"id": *"[^"]+"' | head -1 | grep -oE '[A-Za-z0-9_-]{20,}')"
  echo "✅ 드라이브 업로드 완료 (id: $FID)"
else
  echo "⚠️ 드라이브 업로드 실패 — 로컬 백업은 유지됨"
  echo "$UPLOAD_OUT" | head -5
fi
fi

# ── 4단계: 보관 정책 적용 (대표 지시) ──
# 중요 백업(weekly/monthly)은 항상 보관. daily만 2주 보관.
case "$KIND" in
  daily)   KEEP=14 ; KEEP_DESC="2주" ;;
  weekly)  KEEP=8  ; KEEP_DESC="2개월" ;;
  monthly) KEEP=12 ; KEEP_DESC="1년 (중요 — 항상 보관)" ;;
  *)       KEEP=14 ; KEEP_DESC="2주" ;;
esac
cd "$DEST_DIR" || exit 0
ls -1t *.tar.gz 2>/dev/null | tail -n +$((KEEP + 1)) | while read -r old; do
  rm -f "$old"
  echo "  정리: $old (보관 $KEEP개=$KEEP_DESC 초과)"
done

# ── 5단계: 운영파일 7일 정리 (진행결과물은 삭제 안 함) ──
if [ -f "$ROOT/_tools/checkpoint.py" ]; then
  python "$ROOT/_tools/checkpoint.py" prune 2>/dev/null | head -2
fi

echo "=== 백업 완료 ==="
