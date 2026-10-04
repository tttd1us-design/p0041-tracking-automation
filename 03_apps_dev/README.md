# 03_apps_dev — 소프트웨어 개발팀

## 역할
승인된 spec.md를 Claude Code(claude -p)에 넘겨 프로젝트 폴더에 코드를 생성한다.

## 폴더 구조

```
03_apps_dev/
├── projects/
│   ├── app1_excel_merge/        # 엑셀 데이터 취합 자동화 도구
│   ├── app2_market_analysis/    # 시장 조사·상권 분석 도구
│   └── app3_behavior_tracker/   # 행동 변화 트래커
├── shared/
│   ├── components/              # 공유 UI 컴포넌트
│   ├── utils/                   # 공유 유틸리티
│   └── styles/                  # 공유 스타일
└── docs/
    ├── api/                     # API 문서
    ├── design/                  # 디자인 문서
    └── requirements/            # 요구사항 문서
```

## 작업 절차

1. **명세서 확인:** `02_product_spec/specs/approved/spec.md` 읽기
2. **프로젝트 생성:** `projects/appN_이름/` 폴더 생성
3. **개발:** Claude Code로 코딩
   ```bash
   claude -p "spec.md에 적힌 요구사항대로 웹앱을 완성해라." --allowedTools "Read,Write,Bash"
   ```
4. **테스트:** 로컬에서 테스트 실행
5. **문서화:** `docs/`에 API, 디자인, 요구사항 문서 작성

## 스킬
`10jo-build-mvp` 스킬을 참고한다.
