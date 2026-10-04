# 10조 스튜디오 작업 공간

이 폴더는 1인 가상 AI 소프트웨어 회사 "10조 스튜디오"의 작업 공간이다.
**작업을 시작하기 전에 `_docs/COMPANY_RULES.md`를 읽고 따른다.**

## 폴더 구조

```
10jo_Studio/
├── _docs/              # 회사 규칙, 에이전트 지침, 가이드
├── _logs/              # 시스템, 에이전트, 오류 로그
├── _shared/            # 공유 템플릿, 가이드, 에셋
├── 01_pain_mining/     # 불편 발굴팀
│   ├── data/           # 가공된 데이터 (painpoints.json 등)
│   ├── raw/            # 원시 데이터 (자막, 크롤링 결과)
│   ├── reports/        # 분석 리포트 (weekly, monthly)
│   └── scripts/        # 수집·분석·내보내기 스크립트
├── 02_product_spec/    # 기획팀
│   ├── business/       # 사업 계획 (plan, financial, marketing)
│   ├── organization/   # 조직 구조 (roles, processes)
│   ├── specs/          # 제품 명세서 (approved, draft, archive)
│   └── templates/      # 문서 템플릿
├── 03_apps_dev/        # 개발팀
│   ├── projects/       # 프로젝트별 코드
│   ├── shared/         # 공유 컴포넌트, 유틸, 스타일
│   └── docs/           # API, 디자인, 요구사항 문서
├── 04_deployment/     # 배포팀
│   ├── domains/        # 도메인 설정
│   ├── ssl/            # SSL 인증서
│   ├── cdn/            # CDN 설정
│   ├── monitoring/     # 모니터링 설정
│   └── backups/        # 백업 (daily, weekly, monthly)
└── 05_reports/         # 경영 보고팀
    ├── weekly/         # 주간 보고서
    ├── monthly/        # 월간 보고서
    ├── quarterly/      # 분기 보고서
    ├── financial/      # 재무 보고서
    └── archive/        # 보관용 보고서
```

## 작업 시작 전 체크리스트

1. `_docs/COMPANY_RULES.md` 읽기
2. `_docs/AGENTS.md` 읽기 (에이전트 지침)
3. `_docs/CLAUDE.md` 읽기 (Claude Code 지침)
4. 오늘 날짜 확인: `date +%Y-%m-%d`
5. 작업 디렉토리로 이동: `cd /d/10jo_Studio/<부서폴더>`

## 부서별 업무 절차

부서별 업무 절차는 스킬에 있다:
- `10jo-pain-mining` — 불편 발굴
- `10jo-product-spec` — 제품 기획
- `10jo-build-mvp` — 개발
- `10jo-deploy` — 배포
- `10jo-status-report` — 경영 보고
