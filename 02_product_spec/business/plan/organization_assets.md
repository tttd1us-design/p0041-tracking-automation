# 10조 스튜디오 조직·자산 실측 (v1.0)

작성: 10조 수석 / 2026-10-03
목적: 사업계획서 v4.0의 조직 편성 근거
원칙: **실제 설치·확인된 것만 기재. 미설치는 미설치로 표기.**

---

## 1. 전체 구조 (실측)

```
                    [대표 — sang wan lee]
                   의사결정 · 승인 · 법적 책임
                   (사람 1명 — 유일한 인간)
                              │
                ┌─────────────┴─────────────┐
                │   [수석 — Hermes Agent]    │
                │   v0.21.3 (2026.9.14)     │
                │   총괄 기획·지휘·집행      │
                │   위임 한도: 동시 10개     │
                └─────────────┬─────────────┘
                              │
        ┌──────────┬──────────┼──────────┬──────────┐
        │          │          │          │          │
    [발굴팀]   [기획팀]   [개발팀]   [배포팀]  [보고팀]
        │          │          │          │          │
   하위에이전트  하위에이전트  AI CLI   하위에이전트  하위에이전트
```

**총 인원: 사람 1명 + AI 에이전트 체계 1식**

---

## 2. AI 자산 목록 (실측)

### 2.1. 지휘 계층

| 역할 | 시스템 | 버전 | 확인 |
|---|---|---|---|
| **수석 (총괄)** | Hermes Agent | v0.21.3 (2026.9.14) | ✅ |
| 위임 능력 | delegate_task | 동시 10개 | ✅ |
| 모델 | gemini-3.8-flash | provider: gemini | ✅ |
| 플랫폼 | Telegram DM | chat_id 8547129098 | ✅ |

### 2.2. 개발 계층 (AI CLI)

| 도구 | 버전 | 용도 | 상태 |
|---|---|---|---|
| **Claude Code** | 2.1.210 | 주력 개발 (spec.md → 코드) | ✅ 설치 |
| **Codex CLI** | 0.154.0 | 보조 개발·코드 리뷰 | ✅ 설치 |
| **Gemini CLI** | 0.47.0 | 조사·분석 | ✅ 설치 |
| **Antigravity** | GUI (246MB) | 대표 직접 개발 (GUI 선호) | ✅ 설치 |
| OpenCode | — | 스킬만 존재, CLI 미설치 | ❌ 미설치 |
| Aider | — | — | ❌ 미설치 |

**주의:** opencode 스킬은 있으나 CLI가 없다. 필요 시 설치 승인 요청.

### 2.3. 자동화 계층 (크론)

| 작업명 | 주기 | 사용 스킬 | 상태 |
|---|---|---|---|
| 사업아이템 데일리 브리프 | 월~금 09:30 | naver-news-search, google-trends | ✅ active |
| 정기 불편 발굴 | 월/수/금 10:00 | 10jo-pain-mining | ✅ active |
| 무료 모델 감시 | 매일 08:40 | — | ✅ active |

### 2.4. 외부 연동

| 서비스 | 상태 | 계정 |
|---|---|---|
| Google Drive | ✅ 인증 | tttd1us@gmail.com |
| 백업 폴더 | ✅ | `10jo_Studio_Backup` (ID: 1JKujfoEKU…) |
| MCP 서버 | ❌ 없음 | — |
| Claude 계정 | ✅ Pro | tttd1us@gmail.com |

---

## 3. 스킬 자산 (총 88개)

### 3.1. 10조 전용 스킬 7개

| 스킬 | 역할 | 상태 |
|---|---|---|
| `10jo-pain-mining` | 불편 발굴 → painpoints.json | ✅ |
| `10jo-product-spec` | 불편 → spec.md | ✅ |
| `10jo-build-mvp` | spec.md → Claude Code 개발 | ✅ |
| `10jo-deploy` | MVP → 무료 배포 | ✅ |
| `10jo-status-report` | 경영 현황 보고 | ✅ |
| `10jo-business-plan` | 사업계획서 (조사 프로토콜 포함) | ✅ |
| `10jo-pdf-report` | 마크다운 → 한글 A4 PDF | ✅ |

### 3.2. 카테고리별 스킬 분포 (88개 실측)

| 카테고리 | 개수 | 대표 스킬 |
|---|---|---|
| productivity | 14 | xlsx, pdf, docx, powerpoint, notion, google-workspace |
| software-development | 14 | github, systematic-debugging, test-driven-development, grill-me, spike |
| creative | 13 | creative-ideation, baoyu-infographic, popular-web-designs, humanizer |
| **카테고리 없음 (허브 설치)** | **14** | find-skills, agent-browser, copywriting, seo, the-mom-test, webapp-testing, cold-email-outreach, customer-feedback, marketing-psychology, user-research, web-quality-audit, Kanban, Stripe Payments |
| **10jo-studio** | **7** | 위 3.1 참조 |
| research | 6 | grounded-citations, arxiv, competitor-news-monitor, rss-feeds, duckduckgo-search, llm-wiki |
| autonomous-ai-agents | 6 | claude-code, codex, opencode, computer-use, hermes-agent, agent-merge-conflict-arbiter |
| korean | 3 | naver-blog-research, naver-news-search, korean-law-search |
| media | 3 | youtube-content, gif-search, songsee |
| web-development | 3 | publish-site, cloudflare-temporary-deploy, scrollcraft |
| email | 2 | himalaya, email-inbox-triage |
| web | 1 | blocked-page-recovery |
| note-taking | 1 | obsidian |
| social-media | 1 | reddit-reading |
| **합계** | **88** | |

출처별: hub-installed 23 · builtin 51 · local 14

### 3.3. 부서별 투입 스킬 매핑

| 부서 | 주력 스킬 | 보조 스킬 |
|---|---|---|
| **불편 발굴팀** | 10jo-pain-mining | youtube-content, reddit-reading, naver-blog-research, naver-news-search, google-trends, rss-feeds, duckduckgo-search |
| **기획팀** | 10jo-product-spec | creative-ideation, grill-me, the-mom-test, korean-law-search, user-research |
| **사업기획팀** | 10jo-business-plan | grounded-citations, competitor-news-monitor, marketing-psychology, copywriting |
| **개발팀** | 10jo-build-mvp | claude-code, codex, test-driven-development, systematic-debugging, requesting-code-review, simplify-code, webapp-testing |
| **배포팀** | 10jo-deploy | publish-site, cloudflare-temporary-deploy, github |
| **마케팅팀** | (신설 예정) | seo, copywriting, marketing-psychology, cold-email-outreach, social-media-content-calendar |
| **보고팀** | 10jo-status-report | 10jo-pdf-report, pdf, docx, xlsx, powerpoint |
| **고객지원팀** | (신설 예정) | customer-feedback, user-research |

---

## 4. 부서 편성 (6개 부서)

### 4.1. 부서별 상세

| # | 부서 | 책임자 | 실행 주체 | 주간 산출물 |
|---|---|---|---|---|
| 1 | **불편 발굴팀** | 수석 | 하위 에이전트 (병렬) | 불편 5건 |
| 2 | **기획팀** | 수석 | 수석 + 하위 에이전트 | spec.md 1건 |
| 3 | **개발팀** | 수석 | Claude Code / Antigravity | 작동 코드 |
| 4 | **배포팀** | 수석 | 수석 + 하위 에이전트 | 라이브 URL |
| 5 | **마케팅팀** | 수석 | 수석 + 하위 에이전트 | SEO 콘텐츠 2건 |
| 6 | **보고팀** | 수석 | 수석 | 주간 보고서 |

### 4.2. 각 부서의 실제 작업 흐름

**1. 불편 발굴팀**
```
크론 (월/수/금 10:00) 자동 실행
  → 유튜브 자막 수집 (yt-dlp)
  → 레딧·네이버·커뮤니티 검색
  → 후보 추출 → 점수화 → painpoints.json 누적
  → 상위 5건 보고
```

**2. 기획팀**
```
대표가 P-번호 승인
  → 경쟁·대체재 조사 (web_search)
  → 법적 리스크 확인 (korean-law-search)
  → 해법 3안 (creative-ideation)
  → 자기 공격 (grill-me)
  → spec.md 작성 → 대표 승인
```

**3. 개발팀**
```
대표가 개발 착수 승인
  → Claude Code에 spec.md 투입 (claude -p)
  → 코드 생성 → npm run build 검증
  → DEV_NOTES.md 작성
  → 수석이 직접 검증 (자기보고 불신)
```
※ 대표가 직접 할 경우: Antigravity GUI 사용

**4. 배포팀**
```
대표가 배포 승인
  → GitHub Pages / Cloudflare 배포
  → 라이브 URL 확인
  → DEPLOY_LOG.md 기록
```

**5. 마케팅팀 (신설)**
```
제품 출시 후
  → SEO 콘텐츠 (검색 수요 잡기)
  → 랜딩페이지 카피
  → 커뮤니티 게시
  → 무료 도구로 트래픽 → 유료 전환
```

**6. 보고팀**
```
매주 금요일
  → 불편·기획·개발·배포·매출 집계
  → 실제 파일과 대조 (보고 ≠ 실제 방지)
  → PDF 정식 보고서 → 대표 제출
```

---

## 5. 의사결정 권한 체계

### 5.1. 권한 매트릭스

| 결정 유형 | 수석 자율 | 대표 승인 | 대표 직접 |
|---|---|---|---|
| 폴더·문서·코드 구조 | ✅ | | |
| 스킬 수정·생성 | ✅ | | |
| 하위 에이전트 생성·지시 | ✅ | | |
| 작업 우선순위 | ✅ | | |
| 불편 항목 선정 | 제안 | ✅ | |
| 개발 착수 | | ✅ | |
| 외부 배포 | | ✅ | |
| **지출 (금액 무관)** | | ✅ | |
| **결제 연동** | | ✅ | |
| 사업자등록·통신판매업 | | | ✅ |
| 계약·세금 | | | ✅ |
| 사람 채용 | | | ✅ |

### 5.2. 승인 게이트 5개 (절대 우회 금지)

```
[1] 아이템 확정   → 대표 승인 → spec.md
[2] 개발 착수     → 대표 승인 → 코드
[3] 외부 배포     → 대표 승인 → 라이브
[4] 결제 연동     → 대표 승인 → 과금
[5] 지출 발생     → 대표 승인 → 금액 무관
```

---

## 6. 주간 운영 리듬

| 요일 | 업무 | 실행 |
|---|---|---|
| 월 09:30 | 데일리 브리프 (자동) | 크론 |
| 월 10:00 | 정기 불편 발굴 (자동) | 크론 |
| 월 | 주간 계획 수립 | 수석 |
| 화 | 제품 개발 | Claude Code |
| 수 10:00 | 불편 발굴 (자동) + 고객 인터뷰 | 크론 + 수석 |
| 목 | 개발 + 마케팅 콘텐츠 | Claude Code + 수석 |
| 금 10:00 | 불편 발굴 (자동) | 크론 |
| 금 | 주간 보고 + 승인 요청 | 수석 |
| 토 | 실험 (새 고통 검증) | 수석 |
| 일 | 휴무 | — |

---

## 7. 정직한 한계 (계획서에 반드시 포함)

| 한계 | 내용 | 대응 |
|---|---|---|
| **사람 1명** | 대표가 아프면 회사가 멈춘다 | 모든 결정·코드를 파일로 남겨 재개 가능하게 |
| **세션 단절** | 수석의 기억은 컨텍스트 압축·게이트웨이 중단으로 잘린다 | 모든 결정을 파일로 기록 |
| **AI 오류** | 그럴듯한 거짓을 자신 있게 말한다 | 모든 산출물 실측 검증 |
| **법적 인격 없음** | 계약·등록·세금 불가 | 대표가 직접 수행 |
| **고객 접촉 불가** | 전화·미팅·신뢰 형성 불가 | 이메일·메시지로 대체 |
| **동시 작업 한도** | 하위 에이전트 10개 | 조사는 7개씩 분할 |
| **유료 도구 불가** | 무료 자원만 | 무료 티어 우회 설계 |
| **사람 채용 불가** | 수석은 AI 팀장 | 사람 필요 시 대표가 직접 |

---

## 8. 확장 계획 (필요 시 승인 요청)

| 시점 | 추가 필요 | 이유 | 비용 |
|---|---|---|---|
| 즉시 | 없음 | 현재 체계로 착수 가능 | 0원 |
| 제품 3개 이상 | OpenCode CLI | 개발 병렬화 | 0원 |
| 유료고객 100명 | 모니터링 도구 | 장애 감지 | 검토 필요 |
| 유료고객 500명 | 전용 서버 | 트래픽 대응 | 승인 필요 |
| 매출 발생 | 세무 도구 | 신고 | 승인 필요 |

---

*이 문서는 실측 기반이며, 자산이 바뀌면 갱신한다.*
