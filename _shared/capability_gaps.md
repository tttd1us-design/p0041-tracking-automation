# 역량 격차 기록 (Capability Gaps)

업무 중 "필요한데 없다"가 생기면 즉시 여기에 적는다. 안 적으면 같은 격차를 다음에도 겪는다.
규칙은 `10jo-capability-scout` 스킬.

조치: `설치` / `보류(이유)` / `직접 제작` / `불가(이유)`

| 날짜 | 업무 | 막힌 점 | 찾은 것 | 조치 |
|---|---|---|---|---|
| 2026-10-03 | 아이템 검증 | 크몽·숨고 실측을 자동 수집할 방법이 없다 (로그인 필요) | **`gsk crawl --render_js true` (Genspark)** — 크몽 상품 페이지 전문 수집 실측 성공 | **해결** — `10jo-genspark` 스킬 |
| 2026-10-03 | 아이템 검증 | 고객 지불의사 인터뷰를 할 사람이 없다 | `the-mom-test`, `customer-research` 스킬 보유 | 설치됨(미사용) — 크몽 랜딩 테스트로 대체 검토 |
| 2026-10-03 | 법적 리스크 | 법령 API 중계 서버 고장 | `korean-law-search` (공식 API 키 필요) | 보류(대표 승인 — 고문 A-004) |
| 2026-10-03 | 문서 검토 | 사업계획서를 검증할 팀이 없다 | `grill-with-docs`, `grill-me`, `requesting-code-review` | 설치됨(미사용) — v4.1 검토에 투입 요청 |
| 2026-10-03 | 브라우저 자동화 | browser 플러그인 비활성 | `browser-browser` 플러그인 | 보류(필요 시 활성화) |
| 2026-10-03 | 개발 | 커서 AI 도움 | Cursor = GUI 전용, cursor-agent headless 버그 | 불가(GUI 자동화 불가) — 기존 4개 코딩 CLI로 충분 |
| 2026-10-03 | 외부 AI | Grok 도움 | Grok 웹 무료 / API는 유료($2~6/1M) | 보류(API 유료) — 웹은 대표 직접 사용 |
| 2026-10-03 | 경쟁사 분석 | 경쟁사 분석 전용 스킬이 없다 | `hermes skills search` 로 clawhub의 `competitor-analysis`, `competitor-analysis-report` 발견 | 설치 검토(주간 탐사에서 판단) |
| 2026-10-03 | 외부 검토 | 안티그래비티 GUI 자동화 불가로 판단했었다 | `language_server.exe agentapi` CLI 접점 발견 — 실동작 확인 | **해결** — `10jo-antigravity` 스킬 + `_tools/antigravity_bridge.py` |

## 미해결 우선순위

1. **크몽·숨고 실측** — 아이템 검증의 핵심인데 자동화 불가. 수동 조사로 진행 중.
2. **고객 지불의사 확인** — 인터뷰할 사람이 없음. 랜딩페이지 관심도 테스트가 대안 (게이트 3 승인 필요).
3. **문서 검증팀 실사용** — 스킬은 있는데 한 번도 안 돌렸음.
