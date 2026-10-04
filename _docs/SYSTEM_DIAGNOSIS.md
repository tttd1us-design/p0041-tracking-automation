# 10조 스튜디오 — 시스템 진단서 (Claude Code 검토 요청)

작성: Hermes 총괄 / 2026-10-03 00:10 KST

## 0. 검토 요청 사항

1인 가상 AI 소프트웨어 회사 "10조 스튜디오"의 작업 환경이 **작동은 하지만 구조적 결함 3개**를
안고 있다. 아래 실측 결과를 보고, **재구축 설계안**을 제시하라.

특히 판단해 달라:
- `D:\10jo_Studio\_tools\agent-kanban` (Node/React/Cloudflare D1 기반 웹앱)을 **삭제할지 유지할지**
- 폴더 구조를 어떻게 재편할지
- Hermes 스킬 ↔ 작업 폴더 ↔ Claude Code 간 경로 계약을 어떻게 고정할지

---

## 1. 회사 정의

- 이름: 10조 스튜디오 (10jo Studio)
- 사명: 불편 발굴 → 해법 도출 → 소프트웨어 개발 → 글로벌 서비스화
- 목표: 30개 고통을 소프트웨어로 해결, 장기 나스닥 상장
- 인력: 대표 1인 + Hermes(총괄) + Claude Code(개발) + 하위 에이전트
- 예산: 무료 자원만 사용. 유료는 대표 승인 필수

## 2. 작업 파이프라인 (설계 의도)

```
[대표] → [Hermes 총괄]
            ├─ 01_pain_mining   (불편 발굴)   → painpoints.json
            ├─ 02_product_spec  (기획)        → spec.md
            ├─ 03_apps_dev      (개발)        → 소스코드
            ├─ 04_deployment    (배포)        → 라이브 URL
            └─ 05_reports       (보고)        → 현황
승인 게이트: 아이템 확정 / 개발 착수 / 외부 배포 / 지출 / 결제연동
```

## 3. 실측 현재 상태

### 3.1. 폴더 구조 (D:\10jo_Studio)

```
D:\10jo_Studio\
├─ README.md
├─ _docs\        COMPANY_RULES.md, AGENTS.md, CLAUDE.md
├─ _logs\        agents\, errors\, system\   ← 전부 빈 폴더
├─ _shared\      assets\, guides\, templates\ ← 전부 빈 폴더
├─ _tools\       agent-kanban\  ← 외부 웹앱 (대량 용량 점유)
├─ 01_pain_mining\
│   ├─ data\processed\painpoints.json   ← 38건, 32KB
│   ├─ data\raw\                        ← 빈 폴더 (미사용)
│   ├─ raw\2026-10-01\ (0개), 2026-10-02\ (28개), 2026-10-03\ (0개)
│   ├─ reports\weekly\2026-10-02.md
│   └─ scripts\mining\  app_reviews.py, prefilter.py, vtt2txt.py, save_painpoints_20261002.py
├─ 02_product_spec\
│   ├─ business\plan\business_plan.md   (15.5KB)
│   ├─ organization\roles\org_chart.md  (9.7KB)
│   ├─ specs\draft\spec.md                          ← ExcelMerge Pro (5KB)
│   ├─ specs\draft\excel-auto-transform\spec.md     ← Excel Auto-Transform (10.5KB)
│   ├─ templates\   ← 빈 폴더
│   └─ README.md
├─ 03_apps_dev\  docs\, projects\, shared\  ← 전부 빈 폴더 (파일 0개)
├─ 04_deployment\ backups\, cdn\, domains\, monitoring\, ssl\ ← 전부 빈 폴더 (파일 0개)
└─ 05_reports\   archive\, financial\, monthly\, quarterly\, weekly\
    └─ weekly\2026-10-02-status.md
```

### 3.2. 데이터 상태 (painpoints.json)

- 총 38건, ID P-0001~P-0038, 결번 0, 중복 0
- 필수 필드 누락 0, score 구조 정상
- status: approved 4건(P-0001, P-0003, P-0007, P-0008), new 34건
- **문제: approved 4건에 `slug`·`spec_path` 필드가 없음 → 불편↔명세 연결고리 끊김**
- 점수 분포: 9~15점, 평균 10.2

### 3.3. 발견된 결함

**결함 1 — 작업 공간 이원화 (치명적)**
- `C:\10jo_Studio\` 에 구버전 잔여 43개 파일 방치 (painpoints.json 8건 구버전 포함)
- Hermes 스킬 3개가 아직 C: 경로를 가리킴:
  - `10jo-build-mvp`: `C:\10jo_Studio\CLAUDE.md`
  - `10jo-deploy`: `C:\10jo_Studio\04_deployment\<slug>\DEPLOY_LOG.md`
  - `10jo-status-report`: `C:\10jo_Studio\05_reports\YYYY-MM-DD-status.md`
- 위험: 개발팀 실행 시 C 드라이브에 코드 생성 → D 드라이브 구조 무력화

**결함 2 — spec.md 정본 부재 (치명적)**
- 같은 불편(P-0001/P-0003/P-0007/P-0008)을 다루는 spec이 2개, 제품명·상세도가 다름
- 개발팀에 어느 것을 넘길지 미결정

**결함 3 — 보고·백업 불일치**
- 05_reports 주간보고: "불편 8건" (실제 38건)
- Google Drive: painpoints.json(24KB, 8건) + painpoints_2026-10-02.json(32KB, 38건) 공존

**기타**
- Git 저장소 없음 (버전 관리 부재)
- `03_apps_dev` / `04_deployment` 파일 0개 (개발·배포 미착수)
- 빈 폴더 다수 (`_logs`, `_shared`, `data/raw`, `templates`, `docs`, `projects`, `shared` 등)
- `_tools\agent-kanban`: Node 24 + pnpm + Cloudflare D1 + Realmroot/Enbor OIDC 인증 의존
  → 로그인하려면 외부 서비스 시크릿 4종 필요. 현재 미보유로 **실사용 불가 상태**

### 3.4. 정상 작동 항목

- 도구 체인: node v24.15.0, npm 11.12.1, pnpm 10.33.0, python 3.11.16, yt-dlp 2026.08.19, claude 2.1.210, git 2.54.0
- Google Drive 인증: tttd1us@gmail.com, token_valid true
- Hermes 스킬 76개 활성 (10jo 5개 + builtin 51 + hub 16 + local 등)

## 4. 제약 조건

- 무료 자원만. 유료 도구·서비스 가입은 대표 승인 필요
- 비밀값은 코드·문서·git에 넣지 않음
- 승인 없이: 아이템 확정 / 개발 착수 / 외부 배포 / 지출 / 결제연동 금지
- 대표는 안티그래비티(GUI) 또는 Claude Code로 개발하기를 원함
- 모든 작업은 D 드라이브에서

## 5. 질문

1. agent-kanban을 삭제해야 하는가? 유지한다면 우리 파이프라인 어디에 붙는가?
2. 폴더 구조 재편안을 제시하라 (빈 폴더 처리 포함)
3. 스킬↔폴더 경로 계약을 깨지지 않게 고정하는 방법은?
4. spec.md 정본 확정 기준은?
5. C 드라이브 잔여물 처리 방법은?
6. Git 저장소를 어디에 어떻게 둘 것인가?
7. 위 6가지를 반영한 **재구축 실행 순서**를 단계별 명령과 함께 제시하라.
