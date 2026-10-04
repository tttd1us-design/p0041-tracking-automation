# 마이크로SaaS·1인 SaaS 실패 사례 조사

> **작성일**: 2026-10-03
> **목적**: 10조 스튜디오 운영 기준서의 "무엇을 하면 망하는가" 장의 근거 자료
> **방법**: 웹 검색 10회 + 원문 추출 4회, 실패 포스트모텀 15건 분석

---

## 1. 실패 사례 15건

### 사례 1: LooksMutable

| 항목 | 내용 |
|------|------|
| **서비스명** | LooksMutable |
| **창업자** | rameerez (Ramiro E. Ramez) |
| **국가** | 미국 (web3/NFT 커뮤니티) |
| **시작~종료** | 2022년 1~2월 (약 3주 개발) ~ 2022년 출시 후 사실상 중단 |
| **무엇을 만들었는가** | NFT의 온체인 불변성을 검증하고 변경 이력을 추적하는 도구. NFT 메타데이터가 실제로 블록체인에 저장되었는지 확인해주는 서비스. |
| **실패 원인** | ① 문제가 충분히 아프지 않음: "Most people don't give a s\*\*t about the immutability of NFTs" — 창업자 스스로 인정. NFT 구매자들은 단기 차익 목적이 강해 장기적 불변성에 관심 없음. ② 프로젝트 규모가 너무 작음: "afternoon project soul" — 오후 만들기 프로젝트로 시작해 가치 제한적. ③ 타겟 커뮤니티 불일치: web3 커뮤니티가 아닌 web2 포럼에 출시. ④ 시장 타이밍 늦음: NFT 불변성 이슈는 이미 몇 달 전에 핫했고, 출시 시점에는 시장이 이동한 뒤. |
| **종료 시점 상태** | Product Hunt ~150 upvotes, Hacker News ~5, Reddit ~10, Twitter ~20K impressions, 웹사이트 방문자 ~800명. 유료 전환 0. 매출 $0. |
| **창업자 교훈** | "Select a better problem to work on. LooksMutable was too much of a side-project." / "Build the audience first. I was not part of the NFT community prior to launching this." / "Speed is the utmost important thing, both in detecting a trend and in deploying a solution." |
| **출처** | https://rameerez.com/lessons-learned-from-a-failed-product-launch-looksmutable-postmortem/ |

---

### 사례 2: RecoverFlow

| 항목 | 내용 |
|------|------|
| **서비스명** | RecoverFlow |
| **창업자** | BuildWithChoi (최 모씨) |
| **국가** | 한국 |
| **시작~종료** | 2025년 (5일 만에 중단 결정) |
| **무엇을 만들었는가** | 소규모 SaaS 기업($1K~$30K MRR)을 위한 Stripe 결제 실패 자동 복구 도구. 실패 코드별 스마트 재시도 + 3단계 자동 dunning 이메일. 월 $29. |
| **실패 원인** | ① 제품 전에 고객 부재: "No audience before product" — 신규 Twitter 계정의 유기적 도달은 사실상 0. ② 과도한 계획, 과소 검증: 50페이지 PRD, 24태스크 실행 계획, 14일 프로모션 플레이북을 작성했지만 고객 대화 0건. ③ 채널 불일치: Twitter 유기적 도달은 기존 오디언스가 있을 때만 작동. Reddit(신규 계정), Indie Hackers(유료 플랜 필요), 직접 DM(10일 계획) 모두 실행 못 함. ④ 킬 기준 미실행: 14일 내 50명 미만이면 중단하기로 했지만, 단일 채널 5일 운영 후 0명으로 조기 중단. |
| **종료 시점 상태** | 5일간 0 signups (3개 랜딩 페이지 캡처 지점 모두 0). 매출 $0. 백엔드 코드 한 줄도 작성하지 않은 상태에서 중단. |
| **창업자 교훈** | "This isn't a product failure. The product never existed beyond a landing page. This is a distribution failure, and more specifically, it's a sequencing failure." / "Validation is a person handing you money, or at minimum, a person saying 'yes, this hurts, and yes, I'd pay to fix it.'" / "Talk to 10 founders before writing any documentation." |
| **출처** | https://www.indiehackers.com/post/5-days-0-signups-im-shutting-down-my-saas-before-writing-a-single-line-of-backend-code-8dca5b1e12 |

---

### 사례 3: MonitorIntent

| 항목 | 내용 |
|------|------|
| **서비스명** | MonitorIntent |
| **창업자** | Prabal (공동창업자 1명) |
| **국가** | 미국 |
| **시작~종료** | 약 10개월 (첫 코드 ~ 폐업), 최신 제품 기준 ~7개월 |
| **무엇을 만들었는가** | LinkedIn 등에서 리드 스크래핑 + AI 자격 판별 B2B 리드 생성 도구. 3,000+ 자격 리드 제공. |
| **실패 원인** | ① 지속 불가능한 경제성: 단위 경제성은 흑자였지만 고정비(스크래핑 인프라, API 구독, 아웃리치 도구)가 매출을 초과. ② 기술적 침해: 자체 스크래핑 기술이 BrightData 같은 회사가 범용 데이터를 판매하면서 경쟁력 상실. ③ 데이터 소스 차단: 소셜 미디어 플랫폼이 스크래핑 제공자 고소 + 크롤링 강화. ④ 고객 인센티브 불일치: 고객이 저품질 리드 10배 스팸 발송이 더 저렴. ⑤ 포화 시장: Websets, Extruct AI 등 자본 경쟁자가 더 저렴하게 상품화. |
| **종료 시점 상태** | 부트스트랩 (외부 투자 0). 월 버닷레이트 수천 달러. 유료 고객 7명 (거의 모두 스타트업 창업자). 이탈률 높음. 3,000+ 리드 제공했지만 지속 불가능. |
| **창업자 교훈** | "Speed matters. The window between your idea being novel and it being commoditized is shrinking every month. Especially in AI." / "Sell while you build. Or before." / "Never build without a co-founder." |
| **출처** | https://prabal.ca/posts/monitorintent-postmortem/ |

---

### 사례 4: Juttu

| 항목 | 내용 |
|------|------|
| **서비스명** | Juttu |
| **창업자** | 3명 (3개국 리모트) |
| **국가** | 다국가 리모트 |
| **시작~종료** | 2023년 5월 ~ 2024년 11월 (1.5년) |
| **무엇을 만들었는가** | B2B SaaS — 프로덕트 팀의 사용자 인터뷰 자동화 및 스케줄링 도구. 고객 인터뷰 모집·일정 조율·실행을 자동화. |
| **실패 원인** | ① PMF 미달: Rob Snyder의 PMF 레벨 기준 Level 2(고객 사례 있지만 재현 불가) 미달. 2명의 유료 고객은 좋아했지만 다른 고객에게 재현 불가. ② Calendly API 의존 실패: Calendly 오픈 API 사용 약관 변경으로 차단 → 자체 스케줄링 구축으로 범위 확대. ③ 세일즈 집약적 제품: 플러그 앤 플레이가 아니라 긴 대화·커스터마이징·핀드홀딩 필요. ④ 가격 문제: 월 $200/팀 = 조직당 $1,000/월. 대부분 팀에게 "사용자 인터뷰"가 그렇게 아프지 않음. ⑤ 시장 미성숙: 프로덕트 디스커버리 도구 시장 자체가 아직 초기. ⑥ 3개 잠재 고객이 내부 구조조정·해고·예산 동결로 이탈. |
| **종료 시점 상태** | 자체 조달 (투자 0). 유료 고객 2명. 매출 미상 (최소 수준). 3개 잠재 고객 이탈. |
| **창업자 교훈** | "We validated the problem but jumped to a solution that didn't stick." / "We built a nice-to-have (a vitamin) instead of a must-have (a painkiller)." / "The market wasn't ready. Product discovery tooling is still immature." |
| **출처** | https://www.nikonoll.com/p/post-mortem-lessons-from-a-15-year |

---

### 사례 5: Code Interactive

| 항목 | 내용 |
|------|------|
| **서비스명** | codeinteractive.dev |
| **창업자** | Roko Kovač |
| **국가** | 미국 (추정) |
| **시작~종료** | 2024년 ~ 2025년 4월 (약 1년) |
| **무엇을 만들었는가** | .NET 콘텐츠에 특화된 인터랙티브 학습 플랫폼. boot.dev와 유사하지만 .NET 버전. |
| **실패 원인** | ① 창업자-제품 적합성 상실: .NET 개발자였지만 프로젝트 중반에 Linux/Go/인프라로 전환. 더 이상 .NET에 관심 없어짐. ② 검증/PMF 부족: 경쟁 제품(boot.dev)이 이미 검증된 상태에서 새로운 콘텐츠 니치로 진입. ③ 금전적 검증 부재: 무료로만 운영, 유료 전환 시도 안 함. ④ 피드백 루프 부재: 코스 미완성으로 사용자 유지 실패, 피드백은 봇 스팸 수준. ⑤ 집중 실패: 가장 인기 없는 코스에 시간 낭비. ⑥ 비현실적 기대: 주 10시간 가용 시간을 고려하지 않음. |
| **종료 시점 상태** | 343시간 투입, $300 지출, 매출 $0. |
| **창업자 교훈** | "I lost the founder-product fit." / "Payments are the only true validation." / "Don't build anything that doesn't have users from day one." / "Do I see myself working on this 2 years from now? If the answer is no, this is not a project for me." |
| **출처** | https://medium.com/@kova98/why-my-saas-failed-78755fa5a883 |

---

### 사례 6: Ravah

| 항목 | 내용 |
|------|------|
| **서비스명** | Ravah |
| **창업자** | Usama Kashif |
| **국가** | 미국 (추정) |
| **시작~종료** | 미상 (수개월 ~ 1년 추정) |
| **무엇을 만들었는가** | 스타트업 창업자를 위한 피드백/검증 도구 (정확한 제품 설명은 공개 자료에 제한적). |
| **실패 원인** | ① 관심 검증과 반복 사용 검증 혼동: 약 100명 웨이트리스트 가입 + Reddit 긍정 반응이 PMF로 오인. ② 제품 확장 반복: "I validated interest, then kept expanding the product before I had validated repeated need." ③ 비즈니스 질문 회피: 제품 개선으로 비즈니스 문제 직면을 지연. ④ 공동창업자 역할 불분명. |
| **종료 시점 상태** | 약 100명 웨이트리스트, Reddit 긍정 반응. 반복 사용 패턴 없음. 유료 전환 없음. 매출 $0. |
| **창업자 교훈** | "A waitlist is a lead, not product-market fit." / "You cannot build your way out of every problem." / "When the next feature is easier to justify than the next customer conversation, it is time to reassess." |
| **출처** | https://www.usamakashif.me/blog/why-i-shut-down-my-startup/ |

---

### 사례 7: Zinc

| 항목 | 내용 |
|------|------|
| **서비스명** | Zinc |
| **창업자** | Jordan Gabriel (공동창업자 1명) |
| **국가** | 호주 (추정) |
| **시작~종료** | 약 5개월 |
| **무엇을 만들었는가** | 매니저-직원 간 대화를 기록·분석하는 AI 성과관리 도구. |
| **실패 원인** | ① 법적·규제 장벽: 법무팀은 소송 발견 가능성 우려, HR은 "creepy factor" 지적, 기업 고객은 SOC 2 요구. ② 구매자 부재: 서명 권한자는 있지만 문제를 직접 겪지 않음. ③ 코어 기능이 단기 가치보다 리스크가 큼. ④ 검증 부족: 무료 파일로 2개월 진행 → 유료 파일로 전환 시 반대 급증. ⑤ 제품 포지셔닝 실패: "obviously better performance management system" — 기존 시스템과 직접 경쟁. |
| **종료 시점 상태** | 5개월간 개발. 유료 고객 0. 가장 가까운 거래가 보안 팀에 의해 무산. |
| **창업자 교훈** | "You need far less than you think to test real interest." / "Compliments don't cost anything. When we started asking for paid pilots, everything changed." / "If you're being compared to existing software, you're probably not ambitious enough." |
| **출처** | https://jordangabriels.substack.com/p/failing-to-make-something-people |

---

### 사례 8: Flowscriipt Components

| 항목 | 내용 |
|------|------|
| **서비스명** | Flowscriipt Components |
| **창업자** | 이름 미상 |
| **국가** | 미상 |
| **시작~종료** | 미상 (Product Hunt 출시 후 즉시 실패) |
| **무엇을 만들었는가** | Webflow 개발자를 위한 코드 없이 복사-붙여넣기 가능한 기능적 커스텀 컴포넌트. |
| **실패 원인** | ① 마케팅 노력 부족: 제품 구축에 시간 쓰고 마케팅 시간 없음. ② 개발 시간 과다: "I spent way too much time building this in my room than people knowing about it." ③ 촉박한 마감: 3일 만에 완성 → 마케팅 시간 없음. ④ 문제 깊이 부족: Webflow 개발자에게 컴포넌트가 급한 문제가 아닐 가능성. |
| **종료 시점 상태** | Product Hunt 17 upvotes, 100 방문자, 1 가입, 0 매출. |
| **창업자 교훈** | "Building a great product is only part of the equation; getting it in front of the right audience is more important." / "Ensure that the problem you're solving is genuinely important to your target audience." |
| **출처** | https://www.indiehackers.com/post/i-launched-a-product-on-product-hunt-and-it-failed-here-are-the-lessons-i-learned-905bd660bd |

---

### 사례 9: Cadence (익명)

| 항목 | 내용 |
|------|------|
| **서비스명** | Cadence (가명) |
| **창업자** | 2인 창업자 (익명 요청) |
| **국가** | 미국 (추정) |
| **시작~종료** | 2024년 초 ~ 2025년 가을 (약 1.5년) |
| **무엇을 만들었는가** | B2B 스케줄링 도구. 소규모 에이전시 타겟. |
| **실패 원인** | ① 성장은 있었지만 이탈률 숨김: 월 8% 성장했지만 월 6% gross churn + 확장 수익 거의 없음. ② $12.4K MRR은 2인 창업자에게 생활 불가: 서버 비용 제하고도 실질적 급여 지급 불가. ③ 고객 선택 실패: 에이전시(높은 이탈) vs 개인 사용자(낮은 이탈) — 개인 사용자 물결에 편승. ④ 대시보드가 성장만 추적: "Every metric on the dashboard was green. The only red number was the one we weren't tracking." (NRR/이탈률 미추적). ⑤ Product Hunt 스파이크를 시장으로 오인. |
| **종료 시점 상태** | $12,400 MRR, 140 유료 계정, 월 8% 성장. 2025년 가을 자발적 폐업. |
| **창업자 교훈** | "Zero is clarifying. Fifty grand is a business. Twelve grand is a guilt machine." / "Track retention before you track growth." / "A Product Hunt spike is not a market. It's a sugar high with a support cost." / "The metrics you choose are a confession." |
| **출처** | https://www.operatorbook.dev/stories/why-we-killed-our-saas-at-12k-mrr |

---

### 사례 10: Workstream.io

| 항목 | 내용 |
|------|------|
| **서비스명** | Workstream.io |
| **창업자** | Nicholas Freund (공동창업자 David) |
| **국가** | 미국 |
| **시작~종료** | 2020년 ~ 2025년 4월 (5년) |
| **무엇을 만들었는가** | B2B SaaS (정확한 제품 카테고리는 공개 자료에 제한적). $7M+ 자본 조달. |
| **실패 원인** | ① "Must-have" 제품 아님: "we were ultimately a nice-to-have product. We were not a mission-critical, must-have solution." ② 불공정한 우위 부재: 린 스타트업, 피벗, 창업자-시장 적합성은 테이블 스테이크일 뿐 진우위 아님. ③ 디자인 파트너 가스라이팅: 관심 보이다가 온보딩/구매 시점에 사라짐. ④ 초기 고객 유지 실패. |
| **종료 시점 상태** | $7M+ 조달. 5년간 운영. 2025년 4월 폐업. |
| **창업자 교훈** | "Build a Must-Have Product or Die." / "Nothing can compensate for a product that isn't solving a top-priority problem for customers." / "Founders must treat design partners like real customers from day zero." |
| **출처** | https://notanotherceo.substack.com/p/what-i-learned-as-ceo-of-a-failed |

---

### 사례 11: Toplyne

| 항목 | 내용 |
|------|------|
| **서비스명** | Toplyne |
| **창업자** | Rishen Kapoor, Ruchin Kulkarni, Rohit Khanna |
| **국가** | 인도 |
| **시작~종료** | 2021년 ~ 2025년 (3.5년) |
| **무엇을 만들었는가** | PLG 기업을 위한 AI 기반 영업 자동화 플랫폼. Salesforce, HubSpot 연동. 무료 사용자를 유료 고객으로 전환 (광고, 인앱 푸시, 이메일). |
| **실패 원인** | ① PMF 미달: "Despite our best efforts, we couldn't reach the scale or product-market fit we aimed for." — CEO 공식 성명. ② 자본 효과 없음: $17.5M 조달했지만 생존 불가. |
| **종료 시점 상태** | $15M Series A (Tiger Global, Peak XV 등) + $2.5M 시드 = 총 $17.5M 조달. 3.5년 운영. 투자자에게 자본 반환. |
| **창업자 교훈** | "We've learned a lot—mistakes included—and will hopefully share those takeaways soon." (구체적 교훈은 아직 공개되지 않음) |
| **출처** | https://indianstartupnews.com/news/saas-startup-toplyne-shuts-down-returns-capital-to-investors-7312106 |

---

### 사례 12: Slight

| 항목 | 내용 |
|------|------|
| **서비스명** | Slight |
| **창업자** | Colman Humphrey + Raiden (공동창업자) |
| **국가** | 미국 (추정) |
| **시작~종료** | 2020년 말 ~ 약 2.5년 |
| **무엇을 만들었는가** | 데이터 스타트업 (BI 도구 유사). 조직 내 데이터 공유/분석 플랫폼. |
| **실패 원인** | ① 유치 실패: pre-seed 조달했지만 seed 유치 실패. ② 고객 부족: "They saw value, but not enough to justify the internal friction." ③ 이상적 고객 타겟 불분명: "fast-growing Series B company" — 체계적 발견 불가. ④ 유통 전략 부재: "how will your product go from 'cool software' to actually being in people's hands?" ⑤ 시장 둔화: 기업 SaaS 지출 삭감 + 도구 통합. ⑥ 오픈소스 고려했지만 시기 늦음. |
| **종료 시점 상태** | Pre-seed 조달. 일부 고객 있었지만 seed 유치 실패로 폐업. |
| **창업자 교훈** | "Blaming the market is cope. Yes, it was tough, but we just didn't have enough customers. Everything else is context." / "If you don't know how your product will be adopted, how would your customers know?" |
| **출처** | https://www.colmanhumphrey.com/posts/why-slight-failed |

---

### 사례 13: IdeaBench

| 항목 | 내용 |
|------|------|
| **서비스명** | IdeaBench |
| **창업자** | VulcanWM |
| **국가** | 미상 |
| **시작~종료** | 미상 |
| **무엇을 만들었는가** | 아이디어 검증 도구 (구체적 설명 제한적). |
| **실패 원인** | 대안 제품 존재: "Better Alternatives Exist" — SaaS Heaven 등록 정보에 따르면 더 나은 대안이 이미 존재. |
| **종료 시점 상태** | 최대 MRR $0. |
| **창업자 교훈** | 링크 없음 (SaaS Heaven 등록 정보만 확인 가능). |
| **출처** | https://www.saasheaven.space/ |

---

### 사례 14: Loamly

| 항목 | 내용 |
|------|------|
| **서비스명** | Loamly |
| **창업자** | 이름 미상 (1인) |
| **국가** | 미상 |
| **시작~종료** | 2025년 12월 31일 Product Hunt 출시 (4.5개월 개발) |
| **무엇을 만들었는가** | B2B 마케팅 팀을 위한 도구 (정확한 기능은 제한적). |
| **실패 원인** | ① Product Hunt 부적합: B2B SaaS인데 Product Hunt 오디언스는 소비자 중심. ② 커뮤니티 참여 부재: 출시 전 PH 커뮤니티 활동 0. ③ 유통 채널 부재: 이메일 리스트, Twitter 팔로워, 네트워크 모두 0. ④ 출시일 선택 실패: 12월 31일 (연말 휴가 시즌). |
| **종료 시점 상태** | Product Hunt 2 upvotes (본인 것 포함), 0 comments, 0 signups from PH, 순위 #847/약 50개. Hacker News 2 free signups. |
| **창업자 교훈** | "Product Hunt rewards community engagement, not just product quality." / "B2B SaaS doesn't perform well on Product Hunt." / "Launch day doesn't matter if you don't have distribution." |
| **출처** | https://loamly.ai/blog/lessons-launching-hacker-news-product-hunt-b2b-saas |

---

### 사례 15: MakerPulse

| 항목 | 내용 |
|------|------|
| **서비스명** | MakerPulse |
| **창업자** | ykiki |
| **국가** | 미상 |
| **시작~종료** | 미상 (4주 개발) |
| **무엇을 만들었는가** | 5개 탭을 확인하는 대신 하나의 대시보드에서 지표를 볼 수 있는 통합 대시보드. 월 $19. |
| **실패 원인** | ① 오디언스 미구축: "The launch had no audience pre-built. I shipped quietly for 4 weeks and then waved at the launch day crowd." ② 훅이 너무 이성적: "Stop checking 5 tabs, see your metrics in one place" — 진실이지만 기억에 남지 않음. ③ 스크린샷 과다 폴리싱: 출시 전날까지 스크린샷 다듬느라 마케팅 시간 0. ④ AI 래퍼 포화: "The AI wrapper space is saturated." |
| **종료 시점 상태** | Product Hunt 3 upvotes (1개 본인 것), 0 comments, 가입 한 자릿수, 매출 $0. |
| **창업자 교훈** | "Ranking amplifies whatever is already true. Broken onboarding plus a spike equals a louder complaint inbox." / "Wrong customers at a low price is worse than no customers." / "Dogfooding. I am the first user of MakerPulse and the harshest reviewer of it." |
| **출처** | https://forem.com/ykiki/4-weeks-1-saas-3-upvotes-an-honest-product-hunt-postmortem-53h6 |

---

## 2. 마이크로SaaS 실패의 구조적 원인

15개 사례에서 확인된 실패 원인을 분류하고, 각 원인이 실제로 확인된 사례 수를 집계한다.

| 실패 원인 | 확인된 사례 수 | 해당 사례 |
|-----------|:---:|------|
| **유통 채널 부재 / 오디언스 미구축** | 12 | LooksMutable, RecoverFlow, MonitorIntent, Juttu, Code Interactive, Ravah, Flowscriipt, Cadence, Slight, Loamly, MakerPulse, IdeaBench |
| **문제가 충분히 아프지 않음 (Vitamin ≠ Painkiller)** | 10 | LooksMutable, MonitorIntent, Juttu, Code Interactive, Ravah, Zinc, Cadence, Workstream, Slight, MakerPulse |
| **PMF 미달 (검증 부족)** | 9 | RecoverFlow, Juttu, Code Interactive, Ravah, Zinc, Cadence, Workstream, Toplyne, Slight |
| **무료 대안 / 경쟁 대안 존재** | 7 | LooksMutable, MonitorIntent, Code Interactive, Zinc, Cadence, IdeaBench, MakerPulse |
| **이탈률 높음 / 유지 실패** | 5 | MonitorIntent, Juttu, Cadence, Workstream, Ravah |
| **개발에만 집중 (Build Trap)** | 5 | RecoverFlow, Flowscriipt, Code Interactive, MakerPulse, Loamly |
| **가격/단위경제성 문제** | 4 | Juttu, Cadence, Code Interactive, Toplyne |
| **기술적 침해 / 모트 소실** | 3 | MonitorIntent, Zinc, IdeaBench |
| **시장 타이밍 부적절** | 3 | LooksMutable, Slight, Toplyne |
| **창업자-제품 적합성 상실** | 2 | Code Interactive, Workstream |
| **과도한 계획 / 문서화 (Over-planned, under-validated)** | 2 | RecoverFlow, Slight |
| **채널 불일치 (잘못된 플랫폼 선택)** | 2 | RecoverFlow, Loamly |
| **공동창업자 부재 / 팀 문제** | 2 | MonitorIntent, Ravah |
| **시장 미성숙** | 2 | Juttu, Slight |
| **자본 효과 없음 (조달해도 생존 불가)** | 2 | Toplyne, Workstream |

### 핵심 패턴

1. **유통 채널 부재가 1위 (12/15)**: 제품을 만들어도 아무도 모른다. "Build it and they will come"은 거짓.
2. **문제의 심각도 부재가 2위 (10/15)**: "좋은 아이디어"는 아프지 않다. 고객이 돈을 낼 만큼 아프지 않으면 의미 없다.
3. **PMF 미달이 3위 (9/15)**: 검증 없이 개발하고, 출시하고, 그 후에 발견한다.
4. **무료 대안 존재 (7/15)**: 스프레드시트, 기존 도구, 무료 플랜으로 충분한 문제를 해결하려 하면 실패.

---

## 3. 통계로 본 실패율

### 3.1 CB Insights 스타트업 실패 원인 조사

**2024년 업데이트** (431개 VC 지원 스타트업 폐업 분석, 2023년 이후 폐업 기업):

| 실패 원인 | 비고 | 유형 |
|-----------|------|------|
| 자본 고갈 (Ran out of capital) | 70% | 증상 (최종 원인) |
| 제품-시장 적합성 부족 (Poor PMF) | 43% | 근본 원인 |
| 타이밍/거시 경제 불량 (Bad timing) | 29% | 근본 원인 |
| 지속 불가능한 단위경제성 | 19% | 근본 원인 |
| 팀 문제 (Wrong team) | 23% | 실행 |
| 경쟁 패배 (Outcompeted) | 19% | 시장 |
| 가격/비용 문제 | 18% | 재무 |
| 제품 미흡 | 17% | 제품 |
| 비즈니스 모델 부재 | 17% | 전략 |
| 마케팅 부실 | 14% | GTM |

- **자본 고갈은 증상이지 원인이 아니다**: CB Insights는 70%의 폐업 기업이 자본 고갈을 언급하지만, 이는 "최종 원인"이지 "근본 원인"이 아님을 명시.
- **431개 기업이 폐업 전 총 $17.5B 조달**: 중앙값 $11M. 돈이 생존을 보장하지 않음.
- **마지막 조달부터 폐업까지 중앙값 22개월**: 4분의 1은 3년 이상 "워킹 데드" 상태로 존속.

**출처**: https://www.cbinsights.com/research/report/startup-failure-reasons-top/

### 3.2 마이크로SaaS / 인디해커 성공 확률

| 데이터 포인트 | 수치 | 출처 |
|-------------|------|------|
| SaaS 스타트업 3년 내 실패율 | 92% | Rocking Web (1,000+ 사례 분석) |
| 마이크로SaaS 18개월 내 실패율 | 92% | Rocking Web |
| 마이크로SaaS 월 $1,000 MRR 미달 | 70% | Rocking Web (1,000개 제품 분석) |
| 마이크로SaaS $1K~$5K MRR (생존 가능 구간) | 18% | Rocking Web |
| 마이크로SaaS $100K MRR 초과 | 1~2% | Rocking Web |
| 마이크로SaaS 월 $50K+ | 1~2% | Rocking Web |
| 마이크로SaaS 손익분기 달성 (12개월 내) | 95% | Rocking Web |
| 마이크로SaaS 월 매출 중앙값 | ~$4,200 (약 $50K/년) | Rocking Web / Freemius |
| 마이크로SaaS 월 매출 평균 (상위 포함) | ~$500 (일반적) | Rocking Web / Freemius / IndieLaunches |
| Product Hunt SaaS 출시 후 $1K MRR 미달 | 97.4% (487/500) | FunnelKeeper (2024년 상반기 500개 분석) |
| Product Hunt 출시 후 활성 사용자 100명 미만 | 91.2% | FunnelKeeper |
| Product Hunt 출시 후 제품 업데이트 없음 | 84.6% | FunnelKeeper |
| Product Hunt 출시 후 생존 (급여 가능 수준) | 2.6% (13/500) | FunnelKeeper |
| Indie Hackers 커뮤니티 10K+ MRR 달성 | 0.07% (12/17,000명) | saasapp.hashnode.dev |
| 1인 창업자 $5K MRR 돌파 | 24% | SaaSOpp (312개 분석) |
| 1인 창업자 $10K MRR 돌파 | 11% | SaaSOpp |
| 1인 창업자 $20K MRR 돌파 | 4% | SaaSOpp |
| 1인 창업자 $50K MRR 돌파 | <1% | SaaSOpp |
| 월 이탈률 <3% → $10K MRR 돌파 | 52% | SaaSOpp |
| 월 이탈률 3~7% → $10K MRR 돌파 | 18% | SaaSOpp |
| 월 이탈률 >7% → $10K MRR 돌파 | 3% | SaaSOpp |
| 첫 유료 고객까지 걸리는 시간 (일반) | 3개월 | Rocking Web / Freemius |
| $1K MRR 달성 시간 (일반) | 12~18개월 | Rocking Web / Freemius |
| $1K MRR 달성 시간 (상위 18%) | 4~8개월 | Rocking Web / Freemius |
| $5K MRR 달성 (일반) | 82%는 달성 못함 | Rocking Web / Freemius |
| $10K MRR 달성 (일반) | 93%는 달성 못함 | Rocking Web / Freemius |

**출처**:
- https://www.rockingweb.com.au/18-month-rule-micro-saas-startup-failure-analysis
- https://www.rockingweb.com.au/micro-saas-revenue-analysis-2025/
- https://freemius.com/blog/state-of-micro-saas-2025/
- https://funnelkeeper.com/blog/product-hunt-guide
- https://saasopportunities.com/blog/what-312-micro-saas-businesses-reveal-about-what-actually-works-data-brutal
- https://saasapp.hashnode.dev/why-most-micro-saas-projects-fail-lessons-from-the-other-90
- https://indielaunches.com/indie-maker-analytics-2024-2025-projects/

### 3.3 생존자 편향 경고

- **성공 사례는 극히 일부**: 마이크로SaaS 성공 스토리의 대부분은 상위 1~2%의 결과물. 일반적인 결과는 월 $500 수준.
- **매출 분포는 멱법칙**: 상위 2%가 전체 마이크로SaaS 매출의 약 60%를 차지.
- **Product Hunt 출시 ≠ 성공**: 97.4%가 $1K MRR 미달. Product Hunt은 "신호"이지 "유통 채널"이 아님.
- **95%가 12개월 내 손익분기**: 이것은 긍정적이지만, 손익분기 수준이 월 $500~수천 달러에 불과.

---

## 4. "이 신호가 보이면 중단하라" 체크리스트

15개 실패 사례에서 공통적으로 나타난 중단 신호 10개:

### 🔴 즉시 중단 신호

1. **유료 의사 결정 없이 3개월 이상 경과** — 웨이트리스트, 무료 가입, "좋아요"만 있고 실제 카드 입력이 0건이면 중단. (Ravah, RecoverFlow, Code Interactive)

2. **단일 채널에 의존한 출시 후 2주 내 유의미한 트래픽 없음** — Product Hunt, Twitter, Reddit 중 하나만 사용하고 결과가 없으면 채널 전략 자체가 잘못된 것. (RecoverFlow, Loamly, MakerPulse)

3. **월 이탈률 5% 초과 + 확장 수익 없음** — 이탈률이 높은데 기존 고객의 추가 구매가 없으면 성장은 환상. (Cadence, MonitorIntent)

4. **고객이 "좋아는 하지만" 사지 않음** — 무료 파일로는 열광하고 유료 파일로 전환하면 조용해지면 문제가 충분히 아프지 않은 것. (Zinc, Juttu)

5. **경쟁 대안이 이미 무료로 존재** — 스프레드시트, 기존 도구, 무료 플랜으로 충분히 해결되는 문제를 유료로 팔려 하면 실패. (Code Interactive, IdeaBench, MakerPulse)

### 🟡 재평가 신호

6. **제품 개발 시간 > 고객 대화 시간** — 코드 작성 시간이 고객 인터뷰 시간보다 많으면 Build Trap. (RecoverFlow, Flowscriipt, Code Interactive)

7. **창업자가 제품을 2년 후에도 하고 싶은지 확신 없음** — 창업자-제품 적합성이 없으면 지속 불가. (Code Interactive, Workstream)

8. **매출이 있지만 창업자 생활비를 못 버팀** — $12K MRR이어도 2인 이상이면 생활 불가. "Zero is clarifying. Fifty grand is a business. Twelve grand is a guilt machine." (Cadence)

9. **타겟 고객 도달 경로가 없음** — "어떻게 고객을 찾을 것인가"에 답이 없으면 유통 전략 부재. (Slight, RecoverFlow, Loamly)

10. **매달 새로운 기능을 추가하지만 코어 가치는 개선되지 않음** — "10 times zero is still zero." 코어 제품이 안 팔리면 기능 추가는 의미 없음. (MakerPulse, Flowscriipt, Code Interactive)

---

## 5. 10조 스튜디오에 대한 시사점

1. **"제품 30개 만들어 1개 성공" 전략의 위험**: 성공률 1~2% 기준으로는 30개로도 부족할 수 있음. 그러나 각 제품의 개발 기간이 짧고(2~4주), 유료 검증을 우선한다면 시행착오 비용이 낮아짐.

2. **유통 채널이 성공의 열쇠**: 12/15 사례에서 유통 부재가 원인. 제품 만들기 전에 오디언스 구축이 선행되어야 함.

3. **"아픈 문제" 선택이 생존을 좌우함**: 10/15 사례에서 문제의 심각도 부재가 원인. "Vitamin"이 아닌 "Painkiller"를 찾아야 함.

4. **이탈률이 성장보다 중요**: 이탈률 5% 이상이면 신규 고객 유치는 의미 없음. 이탈률 3% 미만이어야 $10K MRR 돌파 가능성 52%.

5. **Product Hunt에 의존하지 말 것**: 97.4%가 $1K MRR 미달. Product Hunt은 보조 채널이지 주 채널이 될 수 없음.

6. **1인 천장은 $10K~$20K MRR**: 1인 창업자의 24%만 $5K MRR 돌파, 11%만 $10K MRR 돌파. 현실적인 목표 설정 필요.

---

## 6. 이 문서의 한계

- **표본 편향**: 15개 사례는 공개적으로 포스트모텀을 작성한 창업자에 한정. 실제 실패 사례의 대부분은 조용히 사라짐.
- **자기 보고 편향**: 모든 데이터는 창업자 스스로 작성한 포스트모텀 기반. 객관적 검증 불가.
- **시장 변화**: 2024~2026년 AI 도구 급변으로 인해 과거 사례의 교훈이 현재와 다를 수 있음.
- **매출 데이터 공개 제한**: 대부분의 사례에서 정확한 매출·고객 수·부채 데이터가 공개되지 않음.
- **국가별 차이**: 한국 사례(RecoverFlow)가 1건뿐이라 한국 시장 특성 반영 제한적.

---

## 7. 출처 목록

1. https://rameerez.com/lessons-learned-from-a-failed-product-launch-looksmutable-postmortem/
2. https://www.indiehackers.com/post/5-days-0-signups-im-shutting-down-my-saas-before-writing-a-single-line-of-backend-code-8dca5b1e12
3. https://prabal.ca/posts/monitorintent-postmortem/
4. https://www.nikonoll.com/p/post-mortem-lessons-from-a-15-year
5. https://medium.com/@kova98/why-my-saas-failed-78755fa5a883
6. https://www.usamakashif.me/blog/why-i-shut-down-my-startup/
7. https://jordangabriels.substack.com/p/failing-to-make-something-people
8. https://www.indiehackers.com/post/i-launched-a-product-on-product-hunt-and-it-failed-here-are-the-lessons-i-learned-905bd660bd
9. https://www.operatorbook.dev/stories/why-we-killed-our-saas-at-12k-mrr
10. https://notanotherceo.substack.com/p/what-i-learned-as-ceo-of-a-failed
11. https://indianstartupnews.com/news/saas-startup-toplyne-shuts-down-returns-capital-to-investors-7312106
12. https://www.colmanhumphrey.com/posts/why-slight-failed
13. https://www.saasheaven.space/
14. https://loamly.ai/blog/lessons-launching-hacker-news-product-hunt-b2b-saas
15. https://forem.com/ykiki/4-weeks-1-saas-3-upvotes-an-honest-product-hunt-postmortem-53h6
16. https://www.cbinsights.com/research/report/startup-failure-reasons-top/
17. https://www.rockingweb.com.au/18-month-rule-micro-saas-startup-failure-analysis
18. https://www.rockingweb.com.au/micro-saas-revenue-analysis-2025/
19. https://freemius.com/blog/state-of-micro-saas-2025/
20. https://funnelkeeper.com/blog/product-hunt-guide
21. https://saasopportunities.com/blog/what-312-micro-saas-businesses-reveal-about-what-actually-works-data-brutal
22. https://saasapp.hashnode.dev/why-most-micro-saas-projects-fail-lessons-from-the-other-90
23. https://indielaunches.com/indie-maker-analytics-2024-2025-projects/
24. https://shubhq.com/saas/research/saas-failure-postmortem
25. https://spaces.collab365.com/posts/indie-saas-post-mortems-point-to-no-buyers-not-bad-code-utt3f3m2
