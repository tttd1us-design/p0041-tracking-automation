"""구글 플레이에서 경쟁 앱의 낮은 별점 리뷰를 모은다 (불편의 직접 증거).

사용법:
  python app_reviews.py "가계부" --out raw/2026-10-02          # 검색어로 상위 앱 3개
  python app_reviews.py --app com.example.app --out raw/...      # 앱 ID 지정
옵션: --apps-per-query 3  --count 200  --max-score 2  --lang ko --country kr

앱마다 <out>/appreviews_<appId>.txt 를 만든다. 한 줄에 리뷰 하나:
  [날짜] ★점수 👍공감수 | 리뷰 본문
prefilter.py 를 거치지 않아도 될 만큼 이미 '불만' 위주라, 바로 분석에 쓴다.
"""
import argparse
import sys
from pathlib import Path

from google_play_scraper import Sort, app as app_info, reviews, search


def collect(app_id, args, out_dir):
    meta = app_info(app_id, lang=args.lang, country=args.country)
    rows, _ = reviews(app_id, lang=args.lang, country=args.country, sort=Sort.NEWEST, count=args.count)
    low = [r for r in rows if r["score"] <= args.max_score and r.get("content")]
    low.sort(key=lambda r: r.get("thumbsUpCount") or 0, reverse=True)
    path = out_dir / f"appreviews_{app_id}.txt"
    header = (
        f"# {meta.get('title')} ({app_id}) 평점 {meta.get('score')} 설치 {meta.get('installs')}\n"
        f"# https://play.google.com/store/apps/details?id={app_id}\n"
        f"# 최근 {len(rows)}개 중 별점 {args.max_score} 이하 {len(low)}개 (공감순)\n"
    )
    lines = [
        f"[{r['at'].date()}] ★{r['score']} 👍{r.get('thumbsUpCount') or 0} | {' '.join(r['content'].split())}"
        for r in low
    ]
    path.write_text(header + "\n".join(lines) + "\n", encoding="utf-8")
    print(f"{app_id}: {len(rows)} reviews, {len(low)} low-score -> {path.name}")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("query", nargs="?", help="검색어 (앱 ID를 모르면)")
    p.add_argument("--app", action="append", default=[], help="앱 ID (여러 번 지정 가능)")
    p.add_argument("--out", required=True, help="저장 폴더 (예: raw/YYYY-MM-DD)")
    p.add_argument("--apps-per-query", type=int, default=3)
    p.add_argument("--count", type=int, default=200)
    p.add_argument("--max-score", type=int, default=2)
    p.add_argument("--lang", default="ko")
    p.add_argument("--country", default="kr")
    args = p.parse_args()

    app_ids = list(args.app)
    if args.query:
        hits = search(args.query, lang=args.lang, country=args.country, n_hits=args.apps_per_query)
        app_ids += [h["appId"] for h in hits if h.get("appId")]
    if not app_ids:
        p.error("검색어나 --app 중 하나는 필요합니다")

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    for app_id in dict.fromkeys(app_ids):
        try:
            collect(app_id, args, out_dir)
        except Exception as e:  # 한 앱이 실패해도 나머지는 계속
            print(f"{app_id}: 실패 {type(e).__name__}: {e}", file=sys.stderr)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
