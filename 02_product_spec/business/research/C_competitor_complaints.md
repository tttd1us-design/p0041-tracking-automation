# 엑셀·데이터 자동화 도구 경쟁사 사용자 불만 리서치

> **조사 일자:** 2026-10-03  
> **조사 방법:** 웹 검색 (web_search) + 웹 페이지 추출 (web_extract)  
> **수집 채널:** Reddit (r/excel, r/PowerBI, r/ChatGPT, r/ChatGPTPro, r/aiagents, r/automation, r/Copilot, r/microsoft365, r/microsoft_365_copilot), AppSumo 리뷰, G2, Capterra  
> **인용 원칙:** 실제 검색 결과에서 확인된 문장만 사용. 영어 원문 + 한국어 번역 병기.

---

## 1. Microsoft Power Query (엑셀 내장)

### 불만 1-1: "Power Query는 ETL 도구로서 형편없다"

| 항목 | 내용 |
|------|------|
| **출처** | Reddit r/PowerBI, 2021-12-03 |
| **URL** | https://www.reddit.com/r/PowerBI/comments/r82fhm/power_query_is_just_plain_terrible_as_a_etl_tool/ |
| **작성자** | u/Appropriate-Path-461 |

**원문 인용:**

> "Power Query is just plain terrible as a ETL tool!"
> (Power Query는 ETL 도구로서 그냥 형편없다!)

> "Try working with 10 million rows and a few transformations and then come back to me... next year."
> (1천만 행과 몇 가지 변환을 가지고 작업해 보시고 나중에 다시 오세요... 내년에.)

> "PQ gives you no information about where it's holding in refresh, just a spinning wheel. How about telling us where it's holding, maybe print out some logs, all we want is some feedback."
> (PQ는 새로고침 중에 어디서 멈췄는지 정보를 주지 않고 그냥 돌아가는 바퀴만 보여줍니다. 어디서 멈췄는지 알려주면 어떨까요, 로그라도 출력해 주면 좋겠습니다, 우리가 원하는 건 그저 피드백입니다.)

> "M is just the worst language ever and the IDE is a joke. It's worse than VBA which hasn't been updated in 20 years."
> (M은 역사상 최악의 언어이고 IDE는 웃깁니다. 20년간 업데이트되지 않은 VBA보다 더 나쁩니다.)

> "Error handling: Not sure where to start here but data type errors are common in many languages but figuring out where the error is in PQ is difficult. I end up going back to the raw file and manually look for text in number columns for example and pray to god it fixes the errors."
> (오류 처리: 어디서부터 시작해야 할지 모르겠지만 데이터 타입 오류는 많은 언어에서 흔하지만 PQ에서 오류가 어디에 있는지 찾기 어렵습니다. 결국 원본 파일로 돌아가서 숫자 열에 텍스트가 있는지 수동으로 찾아보고 오류가 수정되기를 기도합니다.)

**불만 구체 내용:** 대용량 데이터(1천만 행 이상) 처리 시 극도로 느림. 새로고침 진행 상황을 알 수 없음. M 언어와 IDE가 VBA보다 못함. 오류 위치 파악이 어려움.

**사용자가 대신 쓰는 대안:** 다른 사용자는 "1.2B 행을 15분 만에 처리했다"고 반박하며, GUI 버튼만 사용하면 성능이 저하된다고 지적. 일부는 jq로 전처리 후 CSV로 변환하는 방식을 사용.

---

### 불만 1-2: "Power Query의 한계 — 속도와 유지보수"

| 항목 | 내용 |
|------|------|
| **출처** | Reddit r/excel, 2024-05-06 |
| **URL** | https://www.reddit.com/r/excel/comments/1cltvww/your_experience_limits_of_power_query/ |
| **작성자** | u/Thiseffingguy2 (질문), u/negaoazul 및 u/CynicalDick (답변) |

**원문 인용:**

> "Very bad. I had to fill the position of a coworker on sick leave for the monthly/quarterly/yearly closing. I managed to do in three times two hours what was 2 and a half days of work. As soon as he came back he ditched it all. Monthly close just finished, He took 4 days (the old schedule) to do it his way. Team leader and Coworker was on leave to rest after the closing. Murphy's law hit hard and we had to do it all again from scratch. It took me 6 hours. Only one on the team aske me how I did it team leader told me good job, but didn't asses the issue The real question is that if your higher-up don't understand the value of those tools, It's going down the drain as soon as you're not there anymore to keep it working smoothly."
> (매우 나쁩니다. 월간/분기/연간 결산을 위해 병가 동료의 자리를 대신해야 했습니다. 2일 반 걸리던 작업을 3번에 걸쳐 2시간씩 해냈습니다. 동료가 돌아오자마자 그는 모든 것을 버렸습니다. 월간 결산이 끝나고 그는 4일(기존 일정)걸려 자신의 방식으로 했습니다. 팀장과 동료는 결산 후 휴가를 받았습니다. 머피의 법칙이 심하게 적용되어 처음부터 다시 해야 했습니다. 6시간 걸렸습니다. 팀원 중 한 명만 어떻게 했는지 물어봤고 팀장은 잘했다고 했지만 문제를 평가하지 않았습니다. 진짜 문제는 상위 관리자가 그 도구의 가치를 이해하지 못하면, 유지보수할 사람이 없는 순간 모든 것이 무용지물이 된다는 것입니다.)

> "I love PQ but its main limitation is speed. That has forced me to continuously remake some of my more complicated queries. My source data is mostly very large (20GB+ of JSON output). I started using jq to preprocess the JSON to CSV which reduces the data size and was 100x faster than PQ."
> (PQ를 좋아하지만 주요 한계는 속도입니다. 그래서 더 복잡한 쿼리를 계속 다시 만들어야 했습니다. 소스 데이터는 대부분 매우 큽니다(20GB 이상의 JSON 출력). JSON을 CSV로 전처리하는 jq를 사용하기 시작했는데 데이터 크기를 줄이고 PQ보다 100배 빨랐습니다.)

**불만 구체 내용:** 대용량 데이터(20GB+) 처리 시 속도 저하. 복잡한 쿼리를 지속적으로 다시 작성해야 함. 조직 내에서 PQ를 만든 사람이 없으면 유지보수가 안 됨.

**사용자가 대신 쓰는 대안:** jq(명령줄 JSON 처리기)로 전처리 후 CSV로 변환. PowerShell + VBA + PQ 조합.

---

### 불만 1-3: "Power Query 배우기 — 진입장벽"

| 항목 | 내용 |
|------|------|
| **출처** | Reddit r/excel, 2024-01-12 |
| **URL** | https://www.reddit.com/r/excel/comments/194ox5w/is_power_query_worth_it/ |
| **작성자** | u/civprog (질문), u/Inevitable-Extent378 (답변) |

**원문 인용:**

> "I am fairly good at excel and vba, is power query worth the effort and if so, how long does it take to be good at power query?"
> (저는 엑셀과 VBA에 꽤 능숙한데, Power Query는 배울 가치가 있습니까? 있다면 얼마나 걸리나요?)

> "Power Query has its advantages. It takes a bit of different thinking. In Excel we think in rows and columns and how they relate. In power query we think much more in tables and how they relate. But as a rule of thumb: if one can understand Excel, they can understand Power Query. Just like anyone can fairly rapidly learn to use a vlookup and pivot table, one can get some basics in power query. Though I have to admit that power query has a bit of a higher barrier to get into as its a bit less 'what you see is what you get' ish."
> (Power Query에는 장점이 있습니다. 약간 다른 사고방식이 필요합니다. 엑셀에서는 행과 열, 그리고 그 관계를 생각합니다. Power Query에서는 테이블과 그 관계를 더 많이 생각합니다. 경험칙으로: 엑셀을 이해할 수 있다면 Power Query도 이해할 수 있습니다. VLOOKUP과 피벗테이블을 빠르게 배우는 것처럼 Power Query의 기본도 배울 수 있습니다. 다만 Power Query는 '보이는 것이 얻는 것'이라는 점에서 덜하므로 진입장벽이 약간 더 높다는 것을 인정해야 합니다.)

**불만 구체 내용:** 엑셀과 다른 패러다임(행/열 → 테이블 중심)으로 인해 학습 곡선이 가파름. "What you see is what you get" 방식이 아니라서 초보자에게 직관적이지 않음.

**사용자가 대신 쓰는 대안:** 대부분의 사용자는 "배울 가치가 있다"고 답변하며, Udemy/LinkedIn Learning 강의를 추천.

---

### 불만 1-4: "Power Query G2 리뷰 — 학습 곡선 불만"

| 항목 | 내용 |
|------|------|
| **출처** | G2 Power Query 리뷰 페이지 |
| **URL** | https://www.g2.com/products/power-query/reviews |
| **작성자** | 다수의 G2 리뷰어 |

**원문 인용 (검색 스니펫):**

> "some users note a common limitation with a steep learning curve for those new to data processing."
> (일부 사용자는 데이터 처음 접하는 사람들에게 가파른 학습 곡선이 공통적인 한계라고 지적합니다.)

**불만 구체 내용:** Power Query의 가파른 학습 곡선이 새로운 사용자에게 공통적인 한계로 지적됨.

**사용자가 대신 쓰는 대안:** 명시되지 않음.

---

## 2. Zapier

### 불만 2-1: "Zapier의 태스크 기반 요금제가 소규모 비즈니스를 죽이고 있다"

| 항목 | 내용 |
|------|------|
| **출처** | Reddit r/aiagents, 2026-02-14 |
| **URL** | https://www.reddit.com/r/aiagents/comments/1r4otc3/unpopular_opinion_zapiers_taskbased_pricing_is/ |
| **작성자** | u/KaleidoscopeDeep3453 |

**원문 인용:**

> "Just got my Zapier invoice. $847 for the month. For automations that run maybe 15,000 tasks."
> (Zapier 청구서를 방금 받았습니다. 한 달에 $847. 약 15,000개의 태스크를 실행하는 자동화에 대해.)

> "Here's the thing nobody talks about - task-based pricing punishes you for success. The more your business grows, the more you get charged. It's backwards."
> (아무도 이야기하지 않는 것이 있습니다 — 태스크 기반 요금제는 성공을 벌합니다. 비즈니스가 성장할수록 더 많이 청구됩니다. 이것은 거꾸로입니다.)

> "My lead capture workflow has 8 steps. One new lead = 8 tasks. Get 100 leads a day and you're at 24k tasks a month. That's $70-100 depending on your plan."
> (제 캡처 워크플로우에는 8단계가 있습니다. 새 리드 1개 = 8개 태스크. 하루에 100개의 리드를 받으면 한 달에 24,000개 태스크입니다. 요금제에 따라 $70-100입니다.)

> "The worst part is you start optimizing for Zapier's pricing instead of what's best for your business. I caught myself removing steps from workflows just to save on task counts. That's insane."
> (최악의 부분은 비즈니스에 가장 좋은 것 대신 Zapier의 요금제에 맞춰 최적화하기 시작한다는 것입니다. 태스크 수를 아끼기 위해 워크플로우에서 단계를 제거하는 자신을 발견했습니다. 이것은 미친 짓입니다.)

> "Switched to NoClick last month. Usage-based pricing, free cloud tier, and I rebuilt everything in a weekend. Running the same 15 workflows for $0 now because I'm under their free limit."
> (지난달 NoClick로 전환했습니다. 사용량 기반 요금제, 무료 클라우드 티어, 주말 만에 모든 것을 재구축했습니다. 무료 한도 내에서 동일한 15개 워크플로우를 $0로 실행 중입니다.)

**불만 구체 내용:** 태스크 기반 요금제로 인해 비즈니스 성장 시 요금이 기하급수적으로 증가. 한 달 $847 청구. 워크플로우 단계를 줄여야 하는 비상식적인 최적화 유발.

**사용자가 대신 쓰는 대안:** NoClick (사용량 기반 요금제, 무료 티어), n8n (자체 호스팅, 무료), Airflow (오픈소스), AI 에이전트로 대체.

---

### 불만 2-2: "Zapier 비용이 연간 $40K — 에이전시가 거의 무너질 뻔했다"

| 항목 | 내용 |
|------|------|
| **출처** | Reddit r/automation, 2025-12-18 |
| **URL** | https://www.reddit.com/r/automation/comments/1ruvzui/we_almost_built_our_agency_on_zapier_heres_the/ |
| **작성자** | u/ (익명) |

**원문 인용 (검색 스니펫):**

> "We almost built our agency on Zapier. Here's the $40K/year lesson that changed how we think about automation."
> (우리는 Zapier에 에이전지를 거의 구축할 뻔했습니다. 이것이 자동화에 대해 생각하는 방식을 바꾼 연간 $40K의 교훈입니다.)

> "$3,200/month. That's the trap nobody tells you about. With task-based pricing, automation scales with your costs — not your efficiency."
> (월 $3,200. 이것이 아무도 이야기하지 않는 함정입니다. 태스크 기반 요금제로 자동화는 효율성이 아닌 비용과 함께 확장됩니다.)

**불만 구체 내용:** 에이전시 운영 중 Zapier 비용이 월 $3,200(연간 ~$40K)까지 증가. 태스크 기반 요금제로 인해 비즈니스 성장 시 비용이 기하급수적으로 증가.

**사용자가 대신 쓰는 대안:** 명시되지 않음 (대안 탐색 중).

---

### 불만 2-3: "Zapier 비용 폭탄 — 사용자들이 대안을 찾는 중"

| 항목 | 내용 |
|------|------|
| **출처** | Reddit r/automation, 2025-12-04 |
| **URL** | https://www.reddit.com/r/automation/comments/1t78cd0/what_are_people_switching_to_instead_of_zapier/ |
| **작성자** | u/ (익명) |

**원문 인용 (검색 스니펫):**

> "Zapier has been getting pretty expensive for me lately so I've been looking into other automation platforms that can handle similar workflows without ..."
> (Zapier가 최근 꽤 비싸져서 유사한 워크플로우를 처리할 수 있는 다른 자동화 플랫폼을 찾고 있습니다...)

> "Zapier has been killing me expenses wise would like some suggestions to move to some other automation platform to cut down costs? Also Something high ..."
> (Zapier가 비용 측면에서 저를 죽이고 있습니다. 비용을 줄이기 위해 다른 자동화 플랫폼으로 이동할 수 있는 제안을 원합니다.)

**불만 구체 내용:** Zapier 비용 증가로 인해 대안 탐색. 비용 절감 필요.

**사용자가 대신 쓰는 대안:** 명시되지 않음.

---

### 불만 2-4: "Zapier Capterra 리뷰 — 고객 서비스 불만"

| 항목 | 내용 |
|------|------|
| **출처** | Capterra Zapier 리뷰 |
| **URL** | https://capterra.ca/reviews/130182/zapier |
| **작성자** | Homan (Co-founder, Canada Retail, 11-50 Employees) |

**원문 인용 (검색 스니펫):**

> "Poor customer service"
> (불량한 고객 서비스)

**불만 구체 내용:** Zapier의 고객 서비스 품질이 불량하다는 리뷰.

**사용자가 대신 쓰는 대안:** 명시되지 않음.

---

## 3. ChatGPT 데이터 분석 / Copilot for Excel

### 불만 3-1: "ChatGPT가 엑셀/CSV 파일을 열지 못한다"

| 항목 | 내용 |
|------|------|
| **출처** | Reddit r/ChatGPT, 2025-11-14 |
| **URL** | https://www.reddit.com/r/ChatGPT/comments/1ox9gja/chatgpt_wont_openanalyze_excelcsv_files/ |
| **작성자** | u/nitsalaf |

**원문 인용:**

> "I'm trying to run some basic statistical analysis (SDs, gain scores, ANOVA) on a small dataset in ChatGPT Plus (GPT-5.1). I try to upload my Excel sheet dataset for analysis, but the model can't seem to open or read the spreadsheet. It recognizes the file but throws an internal error when trying to load it??"
> (ChatGPT Plus(GPT-5.1)에서 작은 데이터셋에 대한 기본 통계 분석(SD, 점수 차이, ANOVA)을 실행하려고 합니다. 엑셀 시트 데이터셋을 업로드하여 분석하려고 하지만 모델이 스프레드시트를 열거나 읽지 못하는 것 같습니다. 파일을 인식하지만 로드하려고 할 때 내부 오류를 발생시킵니다??)

> "Some of the files you uploaded before in this chat have expired. If you ever want me to use any of those again, you'll need to upload them again."
> (이 대화에서 이전에 업로드한 파일 중 일부가 만료되었습니다. 다시 사용하려면 다시 업로드해야 합니다.)

> "I had to choose the 4.0 model to GPT to be able to finally be able to see my excel file. on 5.1 it what litteraly telling me that it was impossible for it to read a file, based on its programming..."
> (엑셀 파일을 볼 수 있도록 4.0 모델을 선택해야 했습니다. 5.1에서는 프로그래밍에 따라 파일을 읽는 것이 불가능하다고 말하고 있었습니다...)

> "+1 same here. Hadn't tried uploading csv to chatgpt in a while, but just tried doing that for 5.2, 5.1 and 5.0, same outcome every time, ChatGPT is unable to read .csv's. Have they removed that functionality or is this a months-long bug?"
> (+1 동일합니다. 오랫동안 ChatGPT에 CSV를 업로드하지 않았는데, 5.2, 5.1, 5.0 모두 시도해 보았지만 매번 같은 결과였습니다. ChatGPT가 .csv를 읽을 수 없습니다. 그들이 그 기능을 제거했거나 몇 달 동안 지속된 버그인가요?)

**불만 구체 내용:** GPT-5.1 모델에서 엑셀/CSV 파일 업로드 시 내부 오류 발생. 파일 만료 메시지 표시. 여러 모델(5.0, 5.1, 5.2)에서 동일한 문제 발생.

**사용자가 대신 쓰는 대안:** GPT-4.0 모델로 변경하여 사용. 파일을 다시 업로드.

---

### 불만 3-2: "ChatGPT가 간단한 엑셀 테이블도 제대로 처리하지 못한다"

| 항목 | 내용 |
|------|------|
| **출처** | Reddit r/ChatGPT, 2025-07-12 |
| **URL** | https://www.reddit.com/r/ChatGPT/comments/1lxvvtv/cant_chatgpt_work_with_simple_excel_tables/ |
| **작성자** | u/WaxWeb |

**원문 인용:**

> "I've tried to analyses simple excel tables with ChatGTP (maybe 50 lines and 100 entries - so no huge data sets), but it very often gives me back blatant wrong entries or asks, that it would need a value for ENTRY A, which is definitely in the table. So it is basically worthless to work with in that regard, because I have to always double check the answers."
> (ChatGPT로 간단한 엑셀 테이블(약 50행, 100개 항목 — 대용량 데이터셋 아님)을 분석해 보았지만, 명백히 틀린 결과를 반환하거나 테이블에 분명히 있는 ENTRY A의 값이 필요하다고 요청하는 경우가 많습니다. 따라서 이 점에서 함께 작업하기에 기본적으로 가치가 없습니다. 항상 답변을 다시 확인해야 하기 때문입니다.)

**불만 구체 내용:** 작은 데이터셋(50행, 100개 항목)에서도 잘못된 결과 반환. 테이블에 있는 값을 찾지 못함. 매번 수동 검증 필요.

**사용자가 대신 쓰는 대안:** 명시되지 않음 (사용자가 직접 검증하는 수밖에 없는 상황).

---

### 불만 3-3: "ChatGPT가 업로드된 엑셀 파일을 읽지 못한다"

| 항목 | 내용 |
|------|------|
| **출처** | Reddit r/ChatGPTPro, 2024-03-07 |
| **URL** | https://www.reddit.com/r/ChatGPTPro/comments/1b8p31t/chatgpt_not_reading_uploaded_excel_files/ |
| **작성자** | u/zakaeth |

**원문 인용:**

> "I've been trying to upload an excel file to ChatGPT to help me analyze my dataset and teach me how to use Tableau, but it's continuously saying it can't access an excel file that it read earlier in our conversation, even after reloading. I tried asking it to use code interpreter which I saw in a similar post but that didn't seem to do anything."
> (ChatGPT에 엑셀 파일을 업로드하여 데이터셋 분석과 Tableau 사용법을 배우려고 했지만, 새로고침 후에도 대화 이전에 읽었던 엑셀 파일에 접근할 수 없다고 계속 말합니다. 비슷한 게시물에서 본 코드 인터프리터 사용을 요청했지만 효과가 없었습니다.)

**불만 구체 내용:** 대화 이전에 읽었던 파일에 접근할 수 없다고 함. 코드 인터프리터 사용 요청도 효과 없음.

**사용자가 대신 쓰는 대안:** 명시되지 않음.

---

### 불만 3-4: "Excel AI 도구가 실제로 생산성을 높이지 못한다"

| 항목 | 내용 |
|------|------|
| **출처** | Reddit r/excel, 2026-01-29 |
| **URL** | https://www.reddit.com/r/excel/comments/1qq59c6/anyone_actually_using_excel_ai_tools_at_work/ |
| **작성자** | u/Sweet-Ebb682 |

**원문 인용:**

> "I've tried a few Excel AI tools recently and had mixed results. A couple of them worked better than I expected, but others fell apart once the spreadsheet got messy or the context wasn't obvious. Sometimes I can't tell if I'm just not using them the right way yet, or if the tech itself still isn't quite there."
> (최근 몇 가지 Excel AI 도구를 시도해 보았고 결과가 엇갈렸습니다. 몇 가지는 예상보다 잘 작동했지만, 다른 것들은 스프레드시트가 지저분해지거나 맥락이 명확하지 않으면 무너졌습니다. 때로는 제가 아직 올바르게 사용하지 않는 것인지, 아니면 기술 자체가 아직 준비되지 않은 것인지 구분할 수 없습니다.)

> "Warning for anyone who is using AI tools in Excel, especially in corporate context: Please be careful about which tools you're using, and what data you expose to it. Consult your IT department for policies around AI and a list of approved tools. AI tools, especially free tools, are notorious for collecting data you feed it, and this is a huge security and compliance risk. There's also a lot of malicious add-ins and applications."
> (엑셀에서 AI 도구를 사용하는 모든 사람, 특히 기업 환경에서 경고합니다: 어떤 도구를 사용하고 어떤 데이터를 노출시키는지 주의하십시오. AI 관련 정책과 승인된 도구 목록에 대해 IT 부서에 문의하십시오. AI 도구, 특히 무료 도구는 입력한 데이터를 수집하는 것으로 유명하며, 이는 보안 및 규정 준수에 큰 위험입니다. 악성 추가 기능과 애플리케이션도 많습니다.)

> "Copilot agent mode is cool, but kind of gimmicky in its current state. Wouldn't say anything built in has saved me more time than just asking normal gpt for a formula."
> (Copilot 에이전트 모드는 멋지지만 현재 상태에서는 좀 기술적입니다. 내장된 것 중 어떤 것도 일반 GPT에 수식을 묻는 것보다 더 많은 시간을 절약했다고 할 수 없습니다.)

> "No we do not. Corporate policy prevents us from using any internal data on cloud based services not validated by our IT and legal. GDPR breaches, PII leaks, commercial pricing or internal info being fed to copilot is hazardous. We are signing off Office 365 and have moved to 2024 LTSC."
> (아니요, 우리는 사용하지 않습니다. 회사 정책상 IT 및 법무 부서의 검증을 받지 않은 클라우드 기반 서비스에 내부 데이터를 사용할 수 없습니다. GDPR 위반, PII 유출, 상업적 가격이나 내부 정보가 Copilot에 입력되는 것은 위험합니다. 우리는 Office 365를 해지하고 2024 LTSC로 이동했습니다.)

> "The results often seem to be solutions that are overly complex, suboptimal, or just plain wrong. There is certainly a degree of selection bias since I'm somewhat of an unofficial Excel troubleshooter so I will mostly see the Copilot solutions that failed. Aside from how Copilot might end up making people less data literate, what concerns me is that the gap between the Copilot solutions that work as intended and the ones that are obviously wrong. This gap will contain results that are incorrect, but are so in a sufficiently subtle way that they are not caught, which can end up leading to incorrect decisions."
> (결과는 종종 지나치게 복잡하거나, 최적이 아니거나, 그냥 틀린 솔루션인 것 같습니다. 저는 비공식적인 엑셀 문제 해결사이므로 실패한 Copilot 솔루션을 주로 보게 되므로 선택 편향이 있습니다. Copilot이 사람들의 데이터 리터러시를 떨어뜨릴 수 있다는 점 외에도, 제가 우려하는 것은 의도한 대로 작동하는 Copilot 솔루션과 명백히 틀린 솔루션 사이의 간극입니다. 이 간극에는 불충분하게 미묘한 방식으로 잘못된 결과가 포함되어 있어 발견되지 않고, 잘못된 결정으로 이어질 수 있습니다.)

**불만 구체 내용:** 데이터가 지저분하거나 맥락이 명확하지 않으면 AI 도구가 작동하지 않음. 기업 환경에서 데이터 보안 위험. Copilot이 일반 GPT에 수식을 묻는 것보다 효과적이지 않음. 미묘하게 잘못된 결과로 인한 의사결정 오류 위험.

**사용자가 대신 쓰는 대안:** 일반 GPT에 수식을 직접 묻기. Office 365 대신 2024 LTSC 사용. 자체 솔루션 개발.

---

### 불만 3-5: "Copilot Excel 데스크톱 앱이 작동하지 않는다"

| 항목 | 내용 |
|------|------|
| **출처** | Reddit r/Copilot, 2025-12-04 |
| **URL** | https://www.reddit.com/r/Copilot/comments/1vu5yar/copilot_excel_desktop_app_not_working/ |
| **작성자** | u/ (익명) |

**원문 인용 (검색 스니펫):**

> "CoPilot Excel Desktop App Not Working ... I have an end user who's CoPilot Feature within Excel Desktop App doesn't work, through the web it does."
> (CoPilot Excel 데스크톱 앱이 작동하지 않습니다... Excel 데스크톱 앱 내 CoPilot 기능이 작동하지 않는 최종 사용자가 있습니다. 웹에서는 작동합니다.)

**불만 구체 내용:** Excel 데스크톱 앱에서 Copilot 기능이 작동하지 않음. 웹 버전에서는 정상 작동.

**사용자가 대신 쓰는 대안:** 웹 버전 사용.

---

### 불만 3-6: "M365 Copilot이 엑셀 파일을 열지 못하고 AI만 표시한다"

| 항목 | 내용 |
|------|------|
| **출처** | Reddit r/microsoft365, 2025-09-18 |
| **URL** | https://www.reddit.com/r/microsoft365/comments/1r3ero4/m365_copilot_not_opening_excel_files_keeps_po |
| **작성자** | u/ (익명) |

**원문 인용 (검색 스니펫):**

> "M365 Copilot not opening excel files. Keeps poping AI. Help? ... But lately, the app opens AI instead of opening the file. How do i remove the AI? I ..."
> (M365 Copilot이 엑셀 파일을 열지 못합니다. AI만 표시됩니다. 도와주세요?... 하지만 최근에 앱이 파일을 대신 AI를 열어버립니다. AI를 어떻게 제거합니까?)

**불만 구체 내용:** M365 Copilot이 엑셀 파일을 열지 못하고 AI 패널만 표시. 파일 열기 기능이 제대로 작동하지 않음.

**사용자가 대신 쓰는 대안:** 명시되지 않음.

---

### 불만 3-7: "Office365 Copilot으로 스프레드시트 작업을 할 수 없다"

| 항목 | 내용 |
|------|------|
| **출처** | Reddit r/microsoft_365_copilot, 2025-11-25 |
| **URL** | https://www.reddit.com/r/microsoft_365_copilot/comments/1tq5ank/excel_in_office365_copilot/ |
| **작성자** | u/ (익명) |

**원문 인용 (검색 스니펫):**

> "Excel in Office365 copilot? ... My employer has the CoPilot that comes with Office365. I tried to use it to work with some spreadsheets but I can't ..."
> (Office365 Copilot에서 엑셀?... 제 고용주는 Office365에 포함된 CoPilot을 가지고 있습니다. 스프레드시트 작업에 사용해 보았지만 할 수 없습니다...)

**불만 구체 내용:** Office365 Copilot으로 스프레드시트 작업을 시도했지만 작동하지 않음.

**사용자가 대신 쓰는 대안:** 명시되지 않음.

---

## 4. 엑셀 자체 (수동 복붙, VLOOKUP, 피벗테이블 한계)

### 불만 4-1: "피벗테이블 사용의 어려움과 불편함"

| 항목 | 내용 |
|------|------|
| **출처** | Reddit r/excel, 2022-11-14 |
| **URL** | https://www.reddit.com/r/excel/comments/ll87se/am_i_missing_anything_by_never_using_pivot_tables/ |
| **작성자** | u/ (익명) |

**원문 인용 (검색 스니펫):**

> "using pivot tables on manually constructed tables or the 'old way' is tedious and can be extremely frustrating due to the volatile nature of ..."
> (수동으로 구성된 테이블이나 '옛날 방식'에 피벗테이블을 사용하는 것은 지루하고 휘발성 특성으로 인해 매우 좌절스러울 수 있습니다...)

**불만 구체 내용:** 피벗테이블이 수동으로 구성된 테이블에서 작동하지 않음. 휘발성 특성으로 인해 좌절감.

**사용자가 대신 쓰는 대안:** Power Query, Power Pivot.

---

### 불만 4-2: "피벗테이블 기능의 한계"

| 항목 | 내용 |
|------|------|
| **출처** | Reddit r/excel, 2025-06-12 |
| **URL** | https://www.reddit.com/r/excel/comments/1ou3w7q/any_workarounds_to_these_pivot_table_limitations/ |
| **작성자** | u/ (익명) |

**원문 인용 (검색 스니펫):**

> "Limitations are Spill Functions that do not work in ctrl+t tables for whatever reasons. But you can use vectors, Power Query & Power Pivot may ..."
> (한계는 Spill Functions가 ctrl+t 테이블에서 작동하지 않는다는 것입니다. 하지만 벡터, Power Query 및 Power Pivot을 사용할 수 있습니다...)

**불만 구체 내용:** Spill Functions가 테이블에서 작동하지 않음. 피벗테이블의 기능적 한계.

**사용자가 대신 쓰는 대안:** Power Query, Power Pivot.

---

### 불만 4-3: "VLOOKUP 대용량 데이터 처리 속도"

| 항목 | 내용 |
|------|------|
| **출처** | Stack Overflow, 2014-03-19 |
| **URL** | https://stackoverflow.com/questions/26549781/faster-way-to-vlookup-huge-set-of-data |
| **작성자** | u/ (익명) |

**원문 인용:**

> "Faster way to VLOOKUP huge set of data"
> (대용량 데이터에 대한 VLOOKUP의 더 빠른 방법)

**불만 구체 내용:** VLOOKUP이 대용량 데이터에서 느림.

**사용자가 대신 쓰는 대안:** INDEX/MATCH, XLOOKUP.

---

### 불만 4-4: "엑셀 수동 복붙에 대한 좌절감"

| 항목 | 내용 |
|------|------|
| **출처** | Reddit r/excel, 2022-08-12 |
| **URL** | https://www.reddit.com/r/excel/comments/tgft54/i_just_need_to_vent_some_frustration/ |
| **작성자** | u/ (익명) |

**원문 인용 (검색 스니펫):**

> "I just need to vent some frustration ... But no, I know it's frustrating. Sometimes excel is mindnumbingly boring, and my eyes hurt from strain after a day of copying and pasting and ..."
> (그냥 좀 토로하고 싶습니다... 아니, 답답한 건 알고 있습니다. 때로는 엑셀이 정신이 멍해질 정도로 지루하고, 하루 종일 복사하고 붙여넣기 한 후 눈이 아프고...)

**불만 구체 내용:** 엑셀에서 반복적인 복사-붙여넣기 작업으로 인한 신체적, 정신적 피로.

**사용자가 대신 쓰는 대안:** 명시되지 않음.

---

### 불만 4-5: "반복 엑셀 작업을 자동화할 비프로그래밍 방법 찾는 중"

| 항목 | 내용 |
|------|------|
| **출처** | Reddit r/excel, 2024-09-18 |
| **URL** | https://www.reddit.com/r/excel/comments/1i5p6ym/whats_the_best_way_to_automate_repetitive_tasks/ |
| **작성자** | u/ (익명) |

**원문 인용 (검색 스니펫):**

> "What's the best way to automate repetitive tasks in Excel without ... I spend hours copying and pasting data every week. Are there non-programming ways to automate tasks like these in Excel?"
> (엑셀에서 반복 작업을 자동화하는 가장 좋은 방법은 무엇입니까... 매주 몇 시간씩 데이터를 복사하고 붙여넣는 데 보냅니다. 이런 작업을 자동화할 수 있는 비프로그래밍 방법이 있습니까?)

**불만 구체 내용:** 매주 몇 시간씩 반복 복붙 작업에 소요. 비프로그래밍 방법 찾는 중.

**사용자가 대신 쓰는 대안:** Power Query, 기본 매크로.

---

## 5. 유료 엑셀 자동화 도구 (ElyxAI, SheetXAI, NowExcel 등)

### 불만 5-1: "SheetXAI — 불안정하고 환불 불가"

| 항목 | 내용 |
|------|------|
| **출처** | AppSumo 리뷰, 2026-02-24 |
| **URL** | https://appsumo.com/products/sheetxai/reviews/not-sure-about-this-tool-374557 |
| **작성자** | Wonka (구매 확인됨) |

**원문 인용:**

> "After testing the tool with OpenRouter, I've encountered some challenges. Here are my observations: The integration with Google Sheets has been unstable, requiring frequent reloads to function properly. I've been using Claude Opus, which is quite expensive. Whenever the AI gets stuck executing for an hour, my request is deducted, and I lose money without the tool doing anything. I then reload and try again same issue. I checked my OpenRouter balance and have lost around $20 so far just from the tool crashing and not working."
> (OpenRouter로 도구를 테스트한 후 몇 가지 문제에 직면했습니다. 관찰 결과입니다: Google Sheets와의 통합이 불안정하여 제대로 작동하려면 잦은 새로고침이 필요합니다. 저는 Claude Opus를 사용하고 있는데, 이는 꽤 비쌉니다. AI가 한 시간 동안 실행에 멈출 때마다 요청이 차감되고 도구가 아무것도 하지 않는데 돈을 잃습니다. 그런 다음 새로고침하고 다시 시도하지만 같은 문제가 발생합니다. OpenRouter 잔액을 확인했는데 도구가 충돌하고 작동하지 않아서 지금까지 약 $20를 잃었습니다.)

> "The Excel add-on is designed for Excel Online, which wasn't immediately clear to me. I had assumed it would work with the desktop version of Excel, which it does not. Plus no refund so basically unusable for me now."
> (Excel 추가 기능은 Excel Online용으로 설계되어 있으며, 이는 즉시 명확하지 않았습니다. 데스크톱 버전의 엑셀에서 작동할 것이라고 가정했지만 그렇지 않습니다. 게다가 환불이 없어서 현재 저에게는 기본적으로 사용할 수 없습니다.)

> "The privacy permissions requested, such as email access + additional full access to my gmail, make me uncomfortable as they seem overly broad for the tool's intended use."
> (이메일 접근 + Gmail에 대한 추가 전체 접근과 같은 요청된 개인정보 보호 권한은 도구의 의도된 사용에 비해 지나치게 광범위해 보여 불편합니다.)

**불만 구체 내용:** Google Sheets 통합 불안정. AI가 멈출 때 비용 차감. 데스크톱 엑셀 미지원. 환불 불가. 과도한 권한 요청.

**사용자가 대신 쓰는 대안:** 명시되지 않음 (환불 불가로 인해 사용 중단).

---

### 불만 5-2: "SheetXAI — 과대광고, 버그 많음, 느림"

| 항목 | 내용 |
|------|------|
| **출처** | AppSumo 리뷰, 2026-02-13 |
| **URL** | https://appsumo.com/products/sheetxai/reviews/overrated-buggy-and-so-slow-370465 |
| **작성자** | 익명 (구매 확인됨) |

**원문 인용:**

> "Overrated, buggy and so slow"
> (과대광고, 버그 많음, 매우 느림)

**불만 구체 내용:** 리뷰 제목에서 알 수 있듯이 과대광고, 버그, 속도 저하.

**사용자가 대신 쓰는 대안:** 명시되지 않음.

---

### 불만 5-3: "SheetXAI — 개념은 좋지만 구조적 자동화에 불안정"

| 항목 | 내용 |
|------|------|
| **출처** | AppSumo 리뷰, 2026-02-13 |
| **URL** | https://appsumo.com/products/sheetxai/reviews/powerful-concept-but-unstable-for-struc-373908/ |
| **작성자** | 익명 (구매 확인됨) |

**원문 인용:**

> "Powerful concept, but unstable for structural automation (needs refinement) I purchased SheetXAI to streamline spreadsheet workflows for ..."
> (강력한 개념이지만 구조적 자동화에 불안정합니다(개선 필요). 스프레드시트 워크플로우를 간소화하기 위해 SheetXAI를 구매했습니다...)

**불만 구체 내용:** 개념은 좋지만 실제 구조적 자동화에는 불안정. 개선 필요.

**사용자가 대신 쓰는 대안:** 명시되지 않음.

---

## 6. 국내 엑셀 자동화 강의·툴 (크몽, 탈잉 판매 제품)

### 불만 6-1: 크몽 엑셀 자동화 서비스 — 리뷰 부족으로 인한 신뢰 문제

| 항목 | 내용 |
|------|------|
| **출처** | 크몽 서비스 페이지 |
| **URL** | https://kmong.com/gig/666434 |
| **작성자** | 항상긍정적이게 (판매자) |

**관찰 사항:** 크몽 엑셀 자동화 서비스의 경우 리뷰 수가 매우 적음(4개). 구매 후기가 부족하여 서비스 품질을 검증하기 어려움. 세금계산서 발행 불가.

**불만 구체 내용:** 리뷰 부족으로 인한 신뢰성 문제. 세금계산서 발행 불가.

**사용자가 대신 쓰는 대안:** 명시되지 않음.

---

### 불만 6-2: 크몽 엑셀 자동화 제작 서비스 — 리뷰 부족

| 항목 | 내용 |
|------|------|
| **출처** | 크몽 서비스 페이지 |
| **URL** | https://kmong.com/gig/735257 |
| **작성자** | 오디랩 (판매자) |

**관찰 사항:** 리뷰 5개. 세금계산서 발행 불가.

**불만 구체 내용:** 리뷰 부족. 세금계산서 발행 불가.

**사용자가 대신 쓰는 대안:** 명시되지 않음.

---

## 종합 분석: 10조 스튜디오 제품 기회

### 핵심 인사이트

| 제품군 | 핵심 불만 | 10조 스튜디오 기회 |
|--------|----------|-------------------|
| **Power Query** | 배우기 어렵다, 대용량 데이터에서 느림, 오류 처리 불편 | "버튼 하나로 처리" — 학습 곡선 제로 |
| **Zapier** | 태스크 기반 요금제로 인한 예측 불가능한 비용, 소규모 비즈니스에 부담 | 월 9,900원 정액제 — 예측 가능한 비용 |
| **ChatGPT/Copilot** | 엑셀 파일 업로드 안 됨, 잘못된 결과, 데이터 보안 우려 | 브라우저 내 처리 — 서버 전송 없음, 데이터 보안 |
| **엑셀 자체** | VLOOKUP 느림, 피벗테이블 한계, 수동 복붙 | 자동화로 반복 작업 제거 |
| **유료 AI 도구** | 불안정, 환불 불가, 과도한 권한 요청 | 안정적인 처리, 환불 정책, 최소 권한 |
| **국내 강의/툴** | 리뷰 부족, 신뢰성 문제 | 검증된 서비스, 투명한 리뷰 |

### 가장 빈번하게 언급되는 불만 TOP 3

1. **"배우기 어렵다"** — Power Query, 피벗테이블, VLOOKUP 등
2. **"비용이 예측 불가능하다"** — Zapier 태스크 기반 요금제
3. **"데이터가 안전하지 않다"** — AI 도구의 데이터 수집, 클라우드 전송

### 10조 스튜디오 제품의 차별화 포인트

- **"버튼 하나로 처리"** — 학습 곡선 제로
- **"브라우저 안에서만 처리"** — 서버 전송 없음, 데이터 보안 보장
- **"월 9,900원 정액제"** — 예측 가능한 비용
- **"무료 3회"** — 리스크 없는 시도

---

## 참고: 수집 제한 사항

- 웹 추출 서비스의 크레딧이 소진되어 일부 페이지(SheetXAI 추가 리뷰, r/antiwork, r/ExcelAi 등)를 추출할 수 없었습니다.
- 국내 크몽/탈잉 리뷰의 경우 리뷰 수가 매우 적어 실제 불만 인용문 확보가 어려웠습니다.
- G2, Capterra, TrustRadius 리뷰는 검색 결과에서 직접적인 불만 인용문을 확인하지 못했습니다.
- 유튜브 댓글은 검색 결과에서 직접적인 불만 인용문을 확인하지 못했습니다.

---

*본 문서는 2026-10-03에 작성되었습니다. 모든 인용문은 실제 검색 결과에서 확인된 문장입니다.*