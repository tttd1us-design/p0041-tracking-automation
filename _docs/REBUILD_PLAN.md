# 10조 스튜디오 — 재구축 설계안 (REBUILD_PLAN)

작성: Claude Code(개발) / 2026-10-03
대상: `D:\10jo_Studio` / 진단서 `_docs\SYSTEM_DIAGNOSIS.md` 5장 질문 7개에 대한 답

---

## 0. 실측 재확인 (내가 직접 본 것)

진단서 수치를 그대로 믿지 않고 Read/Glob/Bash(읽기전용)로 다시 확인했다.

| 항목 | 진단서 | 내 실측 | 일치 |
|---|---|---|---|
| 빈 폴더 (`_logs`,`_shared`,`04_deployment`) | 빈 폴더 | 하위까지 전부 파일 0개 | ✅ |
| `03_apps_dev/projects` | 빈 폴더 | `app1_excel_merge`·`app2_market_analysis`·`app3_behavior_tracker` 3개가 **빈 채로** 존재 | ✅(+미리 만든 빈 폴더) |
| `specs/approved` | — | **비어 있음**. 두 spec 모두 아직 `draft`에 있음 | 신규 발견 |
| spec 2개 중복 | P-0001/3/7/8 중복 | ExcelMerge Pro·Excel Auto-Transform 둘 다 같은 4건을 원천으로 함 | ✅ |
| approved 4건 slug/spec_path | 누락 | `P-0001,0003,0007,0008` 전부 `slug=None spec_path=None` | ✅ |
| Git | 없음 | D 루트·하위 어디에도 `.git` 없음. **단 agent-kanban만 자체 `.git` 보유** | ✅ |
| agent-kanban 외부 의존 | 로그인 불가 | `wrangler.toml` 확인: Cloudflare Workers+D1, OIDC(id.realmroot.dev), Enbor, GitHub App. 시크릿 5종은 `wrangler secret put`로만 주입 → 미보유 | ✅ |
| C 드라이브 잔여물 | 43개 파일 | **샌드박스가 `C:\10jo_Studio` 접근을 차단** — 내 작업 권한 밖. 역설적으로 "D에서만 작업" 원칙을 강제로 증명 | 간접확인 |

**신규 발견 2개:**
1. `specs/approved/`가 비어 있다 → 게이트 2(개발 착수)가 **아직 완결되지 않았다.** spec이 draft에 있는 한 개발팀은 정식으로 일을 못 받은 상태다.
2. `03_apps_dev/projects/`에 app1/2/3 빈 폴더가 **미리 생성**돼 있다. CLAUDE.md의 경로 계약(`projects/<slug>/`)과 네이밍(`app1_excel_merge` vs slug)이 어긋나 혼란 요인.

---

## 1. agent-kanban — 삭제할 것인가?

### 결론: **활성 트리(`_tools/`)에서 제거(삭제 권장). 단 삭제 실행은 대표 승인 사항 — 개발팀이 직접 지우지 않는다.**

회사 규칙상 "저장소 삭제 금지"이고 이 폴더는 자체 `.git`을 가진 리포지토리다. 그래서 **내가 지우지 않고**, 근거와 명령만 제시한다.

### 삭제를 권하는 근거

1. **우리 코드가 아니다.** `saltbo/agent-kanban`, 라이선스 `FSL-1.1-ALv2`, 공식 사이트 `agent-kanban.dev`, 버전 2.0.0. 외부 OSS 제품을 통째로 받아 둔 것이다.
2. **무료 자원 원칙 위반 소지.** 실사용하려면 Cloudflare Workers+D1 배포 + Realmroot/Enbor OIDC 계정 + GitHub App + 시크릿 5종(`OIDC_WEB_CLIENT_SECRET`, `AK_SESSION_ENCRYPTION_KEY`, `AK_SIGNING_KEY`, `GITHUB_APP_WEBHOOK_SECRET`, `GITHUB_APP_PRIVATE_KEY`)이 필요하다. 이는 **게이트 3(외부 배포)·게이트 4(지출)** 영역이며 대표 승인 없이는 못 건드린다.
3. **지금 가치가 0이다.** OIDC 발급 주체(realmroot.dev)가 외부 서비스라 시크릿 없이는 **로그인 자체가 불가** → 현재 상태로는 보드를 열 수조차 없다.
4. **오염 위험.** 자체 `CLAUDE.md`와 `.claude/`를 품고 있어, 개발팀이 이 하위에서 실행되면 우리 회사 지침 대신 agent-kanban의 지침을 읽는다. 경로 계약이 깨진다.
5. **용량·버전관리 오염.** `node_modules`와 `.git`을 그대로 끌어안고 있어, D 루트에 git을 거는 순간 서브모듈/중첩리포 문제를 일으킨다.

### "그래도 쓸모 있지 않나?" — 유지 시 붙을 자리 검토

개념(에이전트 작업보드, "사람을 실행 루프에서 빼기")은 우리 비전과 맞다. 하지만:

- 1인 회사의 작업 통제면(control plane)은 이미 **Hermes + 폴더 상태(`specs/draft→approved`, `projects/`) + `05_reports` 주간보고**가 대신하고 있다. 중복 투자다.
- 무료로 셀프호스팅하려 해도 OIDC 인증이 외부 서비스에 하드 의존이라 **자력으로 로그인 가능한 상태로 만들 수 없다.**

→ 따라서 "지금 우리 파이프라인에 붙는 자리는 **없다**." 아이디어만 추출해 두고 코드는 활성 트리에서 뺀다.

### 처리 방식 (대표 결정용 3안)

- **A안(권장):** 트리 밖으로 들어내 보관. upstream 포인터만 남긴다.
  `_tools/agent-kanban`를 `D:\10jo_Studio\_archive\agent-kanban\`로 이동하거나, 대표가 삭제. 대신 `_docs/REFERENCES.md`에 `https://github.com/saltbo/agent-kanban (FSL-1.1-ALv2)` 한 줄 기록.
- **B안:** 당장 결정 보류 → `.gitignore`와 D 루트 git 범위에서 제외만 하고 그대로 둔다(단 혼란·용량 비용 지속).
- **C안(비권장):** 유지 + 배포. 게이트 3·4 승인과 시크릿 5종 확보가 전제 — 1인 무료 회사 단계에선 과투자.

> 삭제 명령(대표 승인 후 대표가 실행): `Remove-Item -Recurse -Force 'D:\10jo_Studio\_tools\agent-kanban'`
> 보관 이동(비파괴, 권장): `Move-Item 'D:\10jo_Studio\_tools\agent-kanban' 'D:\10jo_Studio\_archive\agent-kanban'`

---

## 2. 폴더 구조 재편안 (빈 폴더 처리 포함)

### 원칙
- **"미래에 쓸지도 모른다"는 빈 폴더를 미리 만들지 않는다.** 필요할 때 만든다. 빈 폴더는 구조를 어지럽히고 "여긴 뭐가 있어야 하나" 착각을 부른다.
- 각 단계 루트 1개 + 그 안의 산출물만 둔다.
- 아카이브/참고용은 `_archive/`, `_docs/`로 분리.

### 재편 후 모습

```
D:\10jo_Studio\
├─ CLAUDE.md                    ← 개발팀 지침 정본(루트, 그대로 유지)
├─ README.md
├─ .gitignore                   ← 신규
├─ _docs\                       COMPANY_RULES.md, AGENTS.md, SYSTEM_DIAGNOSIS.md, REBUILD_PLAN.md, REFERENCES.md(신규)
├─ _archive\                    ← 신규. agent-kanban·구버전 등 "안 지우되 비활성" 보관소
├─ 01_pain_mining\
│   ├─ data\processed\painpoints.json   ← 정본(38건)
│   ├─ raw\2026-10-02\                  ← 날짜별 원천만. 빈 날짜폴더(10-01,10-03)는 삭제
│   ├─ reports\weekly\
│   └─ scripts\                         ← mining 스크립트 유지, 빈 analysis/export 폴더 삭제
├─ 02_product_spec\
│   ├─ business\plan\business_plan.md
│   ├─ organization\roles\org_chart.md
│   ├─ specs\
│   │   ├─ draft\         ← 작성 중
│   │   └─ approved\<slug>\spec.md   ← 게이트 2 통과분만. 개발팀의 유일 입력
│   └─ README.md
├─ 03_apps_dev\
│   └─ projects\<slug>\      ← 앱 1개=폴더 1개. slug는 painpoints/spec과 동일 문자열
├─ 04_deployment\
│   └─ <slug>\DEPLOY_LOG.md  ← 배포팀이 배포 시 생성. 그 전엔 비움
└─ 05_reports\
    └─ weekly\YYYY-MM-DD-status.md
```

### 삭제할 빈 폴더(대표 승인 후)
`_logs\*`, `_shared\*`, `04_deployment\{backups,cdn,domains,monitoring,ssl}`, `03_apps_dev\{docs,shared}` 및 `projects\app1_*·app2_*·app3_*`(빈 선행 폴더), `01_pain_mining\data\raw`(미사용)·빈 날짜폴더, `02_product_spec\templates`, `05_reports\{archive,financial,monthly,quarterly}`의 빈 하위.
> 빈 폴더라 git에 어차피 안 올라간다. 삭제는 "깔끔함"을 위한 것이며 비파괴에 가깝지만, 폴더 삭제도 대표가 확인 후 실행한다.

### slug 표준
- `painpoints.json`의 approved 건 ↔ `specs/approved/<slug>/` ↔ `03_apps_dev/projects/<slug>/` ↔ `04_deployment/<slug>/`가 **같은 slug 문자열**로 1:1 연결되게 한다.
- MVP 1호 제안 slug: `excel-auto-transform` (아래 4장에서 정본 확정).

---

## 3. 스킬 ↔ 폴더 경로 계약 고정법

문제의 근원: 스킬 3개(`10jo-build-mvp`, `10jo-deploy`, `10jo-status-report`)가 `C:\10jo_Studio\...`를 하드코딩 → D와 이원화. (이 스킬 파일들은 사용자 홈의 Claude 설정에 있어 내 작업범위 밖이라 직접 못 고친다. 아래는 고정 설계.)

### 계약서(단일 진실원) 도입
`_docs\PATHS.md`를 **경로 계약 정본**으로 신설하고, 모든 스킬이 여기만 참조하게 한다.

```
ROOT         = D:\10jo_Studio
PAINPOINTS   = {ROOT}\01_pain_mining\data\processed\painpoints.json
SPEC_DRAFT   = {ROOT}\02_product_spec\specs\draft\<slug>\spec.md
SPEC_FINAL   = {ROOT}\02_product_spec\specs\approved\<slug>\spec.md
APP          = {ROOT}\03_apps_dev\projects\<slug>\
DEPLOY_LOG   = {ROOT}\04_deployment\<slug>\DEPLOY_LOG.md
STATUS       = {ROOT}\05_reports\weekly\YYYY-MM-DD-status.md
```

### 고정 3원칙
1. **드라이브 D로 일원화.** 스킬 3개의 `C:\` → `D:\`로 일괄 수정(대표/Hermes가 스킬 편집). 수정 후 스킬 안에서 `C:\10jo_Studio` 문자열이 0건이 될 때까지 검증.
2. **slug를 키로.** 스킬 인자로 `<slug>`를 받고, 위 템플릿에 끼워 경로를 생성 — 경로를 스킬마다 다시 쓰지 않는다.
3. **방향 가드.** 각 스킬 선두에서 `현재 경로가 D:\10jo_Studio로 시작하지 않으면 중단`하는 안전장치. CLAUDE.md의 "작업 범위는 현 앱 폴더 안" 규칙과 짝을 이룬다. (이미 샌드박스가 C 접근을 막는 것으로 1차 방어가 걸려 있음 — 이걸 계약으로 명문화.)

### 연결고리 복구(진단서 결함: slug/spec_path 누락)
`painpoints.json`의 approved 4건에 `slug`·`spec_path`를 채운다(아래 7장 2단계). 그래야 불편→명세→앱→배포가 slug 하나로 추적된다.

---

## 4. spec.md 정본 확정 기준

### 기준(이 순서로 판정)
1. **경로 위치:** `specs/approved/<slug>/spec.md`에 있는 것만 정본. draft는 전부 초안.
2. **원천 추적성:** `painpoints.json`의 approved 건과 `slug`로 연결된 것.
3. **단일성:** 한 slug에 spec 1개. 중복 발견 시 아래로 병합.

### 현재 중복 판정 (ExcelMerge Pro vs Excel Auto-Transform)

| 항목 | ExcelMerge Pro (`draft/spec.md`) | Excel Auto-Transform (`draft/excel-auto-transform/spec.md`) |
|---|---|---|
| 상태표기 | "개발 대기" | "승인 대기" |
| 원천 불편 명시 | 없음 | P-0001,3,7,8 **명시** |
| 근거(사용자 발언) | 없음 | 유튜브 인용 3건 포함 |
| slug 폴더 | 루트 draft에 흩어짐 | 전용 폴더 보유 |
| 상세도 | 5KB | 10.5KB, 해법 한 줄 포함 |

→ **정본 권고: `excel-auto-transform`.** 원천 불편이 명시돼 추적 가능하고, 근거·해법·대안분석이 더 탄탄하다. ExcelMerge Pro는 제품명 후보로만 흡수(둘 다 같은 불편을 다루므로 기능 손실 없음).

### 확정 절차(대표 승인 = 게이트 2)
1. `excel-auto-transform/spec.md`를 정본으로 지정, 제품명·누락 항목을 ExcelMerge Pro에서 보강.
2. 대표가 "이 slug로 개발 착수" 승인.
3. `specs/draft/excel-auto-transform/` → `specs/approved/excel-auto-transform/`로 이동.
4. 구 `draft/spec.md`(ExcelMerge Pro)는 `specs/archive/`로 이동(삭제 아님).
> **현재 `approved/`가 비어 있으므로, 이 절차 전에는 개발팀이 정식으로 받은 일이 없다.** 지금 개발 착수하면 규칙 위반.

---

## 5. C 드라이브 잔여물 처리

- **사실:** `C:\10jo_Studio`는 이 세션 샌드박스가 접근을 막는다(= 허용 작업 디렉터리는 `D:\10jo_Studio`뿐). 개발팀은 C를 **읽지도 쓰지도 못하는** 게 정상이고 바람직하다.
- **원칙:** 모든 작업은 D. C는 구버전 잔여물(파일 43개, 구 painpoints 8건)일 뿐 정본이 아니다.
- **처리(대표가 D 밖에서 직접):**
  1. C의 고유/최신 산출물이 D에 다 있는지 대조(특히 `painpoints.json` — D 38건이 최신, C 8건은 구버전이므로 폐기 대상).
  2. 안전을 위해 C 전체를 `D:\10jo_Studio\_archive\C_backup_20261003\`로 **백업 이동** 후, C 원본 폴더 제거.
  3. 스킬 3개의 `C:\` 경로를 `D:\`로 교체(3장과 동일 작업)하면 재생성 방지.
- **개발팀 수칙:** 어떤 경우에도 C에 코드·문서를 만들지 않는다. CLAUDE.md "작업 범위=현 앱 폴더" + 3장의 "D 시작 가드"로 강제.

---

## 6. Git 저장소 위치·방식

### 위치: **`D:\10jo_Studio` 루트에 단일 저장소.**
근거: 회사 전 자산이 한 폴더 아래 있고, 불편→spec→코드→보고가 한 이력으로 묶여야 추적된다. 1인 회사엔 멀티레포보다 모노레포가 단순하다.

### `.gitignore` (루트, 신규) — 비밀·용량·외부물 제외
```
# 비밀값 (회사 규칙: 코드/문서/git 금지)
.env
.env.local
.dev.vars
*.key
*.pem

# 의존성/빌드 산출물
node_modules/
.next/
dist/
.wrangler/

# 외부 제품 — 우리 이력에 넣지 않음
_tools/agent-kanban/
_archive/

# OS/로그
_logs/
.DS_Store
Thumbs.db
```

### 커밋/푸시 정책 (CLAUDE.md 준수)
- **커밋은 한다. 푸시는 안 한다** — 외부 공개 배포(게이트 3)는 배포팀/대표 소관.
- 비밀값은 `.env.local`에만, `.gitignore`로 제외.
- `_tools/agent-kanban`은 자체 `.git`을 가지므로 **반드시 ignore**(안 그러면 중첩 리포로 꼬인다). 1장 A안으로 트리 밖에 들어내면 더 깔끔.

### 초기화 명령 (대표 승인 후)
```
cd D:\10jo_Studio
git init
# (위 .gitignore 작성 후)
git add -A
git commit -m "chore: baseline — 재구축 기준선 스냅샷"
```

---

## 7. 재구축 실행 순서 (단계별 명령)

> 원칙: **비파괴 먼저, 파괴적·외부 영향은 대표 승인 게이트.** 아래 ⚠ 표시는 대표 실행/승인 항목(개발팀이 직접 안 함).

**0단계 — 안전 백업 (⚠ 대표, D 밖 포함)**
```
# C 잔여물 백업 이동 후 원본 제거는 5장 참조
Copy-Item 'D:\10jo_Studio' 'D:\10jo_Studio_backup_20261003' -Recurse
```

**1단계 — 경로 계약 고정 (내가/대표 공동)**
- `_docs\PATHS.md` 작성(3장 템플릿).
- 스킬 3개 `C:\`→`D:\` 치환 + "D 시작 가드" 삽입. (⚠ 스킬은 내 작업범위 밖 → 대표/Hermes 편집)
- 검증: 스킬 텍스트에서 `C:\10jo_Studio` 0건 확인.

**2단계 — 데이터 연결고리 복구 (내가)**
- `painpoints.json`의 approved 4건에 필드 추가:
  `P-0001/0003/0007/0008 → "slug":"excel-auto-transform", "spec_path":"02_product_spec/specs/approved/excel-auto-transform/spec.md"`
- Google Drive의 구버전 `painpoints.json`(8건)을 최신 38건으로 교체(또는 구버전 아카이브 표시). (⚠ 외부 저장소 반영은 대표 확인)

**3단계 — spec 정본 확정 (⚠ 대표 승인 = 게이트 2)**
```
# 승인 후:
New-Item -ItemType Directory 'D:\10jo_Studio\02_product_spec\specs\approved' -Force
Move-Item 'D:\10jo_Studio\02_product_spec\specs\draft\excel-auto-transform' `
          'D:\10jo_Studio\02_product_spec\specs\approved\excel-auto-transform'
New-Item -ItemType Directory 'D:\10jo_Studio\02_product_spec\specs\archive' -Force
Move-Item 'D:\10jo_Studio\02_product_spec\specs\draft\spec.md' `
          'D:\10jo_Studio\02_product_spec\specs\archive\excelmerge-pro-spec.md'
```

**4단계 — 폴더 청소 (⚠ 대표 확인 후 실행)**
- 2장 "삭제할 빈 폴더" 목록 제거.
- `03_apps_dev/projects`의 `app1_*·app2_*·app3_*` 빈 폴더 제거(정식 slug 폴더로 대체).

**5단계 — agent-kanban 처리 (⚠ 대표 결정)**
- 권장 A안: `Move-Item 'D:\10jo_Studio\_tools\agent-kanban' 'D:\10jo_Studio\_archive\agent-kanban'`
- `_docs\REFERENCES.md`에 upstream 링크 1줄 기록.

**6단계 — Git 기준선 (⚠ 대표 승인 후, 푸시는 안 함)**
- 6장 `.gitignore` 작성 → `git init` → 첫 커밋.

**7단계 — 개발 착수 (게이트 2 통과분만)**
- `approved/excel-auto-transform/spec.md`를 입력으로 `03_apps_dev/projects/excel-auto-transform/`에 MVP 구현.
- 스택: Next.js(App Router)+TS+Tailwind, 단일 페이지 우선.
- 개인정보 수집 기능이 있으면 `korean-privacy-terms` 스킬로 방침·약관 초안(미정값은 `[대표 확인 필요]`).
- 결제는 `TODO(결제연동-승인필요)` 표시만.
- 종료 전 `npm run build` 통과 확인, `DEV_NOTES.md` 작성.

---

## 부록 — 질문 7개 1줄 요약

1. **agent-kanban:** 활성 트리에서 제거(삭제 권장, 실행은 대표). 외부 OIDC·유료 배포 의존 + 로그인 불가 + 우리 파이프라인에 붙을 자리 없음. 보관 이동 + upstream 링크로 대체.
2. **폴더:** 단계 루트 1개+산출물만. "미리 만든 빈 폴더" 전부 제거, 필요 시 생성. slug로 단계 간 1:1 연결.
3. **경로 계약:** `_docs\PATHS.md` 단일 진실원 + 스킬을 D로 일원화 + slug 인자화 + "D 시작 가드".
4. **spec 정본:** `approved/<slug>/`에 있는 것만 정본. 현재 둘 다 draft → `excel-auto-transform` 채택·보강 후 승인 이동. (지금은 정식 착수 전)
5. **C 드라이브:** 샌드박스가 이미 차단. 대조 후 D로 백업 이동+원본 제거, 스킬 경로 교체로 재발 방지. 개발팀은 C 금지.
6. **Git:** D 루트 단일 모노레포. 비밀·node_modules·agent-kanban·_archive는 ignore. 커밋 O, 푸시 X.
7. **순서:** 백업 → 경로계약 → 데이터복구 → spec확정(⚠게이트2) → 폴더청소 → kanban처리 → git기준선 → 개발착수.

> 이 문서는 개발팀의 설계 제안이다. ⚠ 표시(파괴적·외부 영향·게이트)는 대표 승인/실행 사항이며 개발팀이 직접 수행하지 않았다. 파일 삭제는 하지 않았다.
