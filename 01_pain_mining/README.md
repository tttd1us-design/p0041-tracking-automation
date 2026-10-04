# 01_pain_mining — 불편 발굴팀

## 역할
유튜브 자막·레딧·커뮤니티에서 돈 낼 만한 불편을 수집해 `data/processed/painpoints.json`에 누적한다.

## 폴더 구조

```
01_pain_mining/
├── data/
│   ├── processed/      # 가공된 데이터 (painpoints.json)
│   └── raw/            # 원시 데이터 (CSV, JSON)
├── raw/
│   └── YYYY-MM-DD/     # 날짜별 원시 자막, 크롤링 결과
├── reports/
│   ├── weekly/         # 주간 리포트
│   └── monthly/        # 월간 리포트
└── scripts/
    ├── mining/         # 수집 스크립트 (yt-dlp, 크롤링)
    ├── analysis/       # 분석 스크립트 (필터링, 점수화)
    └── export/         # 내보내기 스크립트 (JSON, CSV)
```

## 작업 절차

1. **수집:** `scripts/mining/`의 스크립트로 유튜브·레딧·커뮤니티 데이터 수집
2. **필터:** `scripts/analysis/prefilter.py`로 1차 필터링
3. **분석:** 후보를 읽고 불편 항목으로 정리
4. **저장:** `data/processed/painpoints.json`에 안전하게 저장
5. **리포트:** `reports/weekly/YYYY-MM-DD.md`에 작성

## 스킬
`10jo-pain-mining` 스킬을 참고한다.
