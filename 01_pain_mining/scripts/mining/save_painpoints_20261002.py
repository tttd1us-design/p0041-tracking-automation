import json, io

p = r'C:\10jo_Studio\01_pain_mining\painpoints.json'
items = json.load(io.open(p, encoding='utf-8'))

max_num = 0
for item in items:
    num = int(item['id'].replace('P-', ''))
    if num > max_num:
        max_num = num

new_items = [
    {
        'id': f'P-{max_num+1:04d}',
        'pain': '직장인이 매일/매주 반복되는 엑셀 데이터 취합·복사붙여넣기·수식 작업에 수시간을 소요하며, 데이터 규모가 수천~수만 건이 되면 실수 가능성과 계산 지연이 급증한다',
        'quote': '매번 이렇게 들어와서 이렇게 긴 수식을 작성하려고 하니 매번 파일 들어가서 범위 선택해서 이 수식을 입력해주기까지 굉장히 번거로울 겁니다.',
        'who': '직장인, 1인 기업 사장, 마케터',
        'source': {'type': 'youtube', 'url': 'https://www.youtube.com/watch?v=rzpS9gec1hA', 'title': '엑셀 데이터 관리 문제풀이', 'published': '2026-09-28'},
        'signals': {
            'frequency': '매일/매주 반복, 8000개 제품·144만 줄 데이터 사례',
            'wtp': '생산성 향상을 위해 AI 도구 구매 의사 있음, 유료 강의 구매 사례',
            'alternatives': '수동 복사붙여넣기, VLOOKUP 수식 작성, 외부 엑셀 강의 수강'
        },
        'score': {'pain': 5, 'wtp': 4, 'buildability': 4, 'total': 13},
        'status': 'new',
        'collected_at': '2026-10-02'
    },
    {
        'id': f'P-{max_num+2:04d}',
        'pain': 'AI 도구를 업무에 쓰려면 폴더 정리·파일 이동·프롬프트 작성 등 준비 작업이 과도하게 많아 오히려 일이 되는 역설 발생',
        'quote': '우리가 편하려고 쓰는 AI 도구인데 쓸 준비를 하는게 일이 돼 버린 거죠. 저는 일을 안 하고 싶은게 아니었어요. 그저 복사 붙여 넣기하고 옮기는 일만 안 하고 싶었던 겁니다.',
        'who': '직장인, IT 운영팀',
        'source': {'type': 'youtube', 'url': 'https://www.youtube.com/watch?v=ew_ogVJ5t8M', 'title': 'Claude Code 업무 자동화 실전', 'published': '2026-09-25'},
        'signals': {
            'frequency': 'AI 도구 사용자 공통 불만, 사용량 제한·컨텍스트 한계 언급',
            'wtp': 'AI 구독료 이미 지출 중, 생산성 향상 위해 추가 도구 구매 의사',
            'alternatives': '채팅형 AI 사용, 수동 작업 병행'
        },
        'score': {'pain': 4, 'wtp': 4, 'buildability': 5, 'total': 13},
        'status': 'new',
        'collected_at': '2026-10-02'
    },
    {
        'id': f'P-{max_num+3:04d}',
        'pain': '비개발자가 VBA·매크로 없이 엑셀 자동화를 시도하면 시트명 불규칙·다수 시트·셀 위치 가변 등 수식만으로 풀 수 없는 벽에 부딪힌다',
        'quote': '규칙 없이 너무 많이 들어 있는 시트 명들에 대해서 한꺼번에 시트명을 불러오기 위해서 엑셀 함수로는 불과하기 때문에 VBA 코드를 짜야 되는데 저 같은 개발 알은 할 줄을 모르니까',
        'who': '비개발 직장인, 1인 기업 사장',
        'source': {'type': 'youtube', 'url': 'https://www.youtube.com/watch?v=TgPGaxRk_aA', 'title': '엑셀 문제풀이 대행 심의위원회 61회', 'published': '2026-09-27'},
        'signals': {
            'frequency': '엑셀 문제 게시판 다수 문의, 시트 합치기 매크로 가장 많은 질문',
            'wtp': 'AI 도구로 매크로 생성 시도, 유료 강의 구매',
            'alternatives': '수동 시트 복사, ChatGPT에 코드 요청 후 실행'
        },
        'score': {'pain': 4, 'wtp': 3, 'buildability': 4, 'total': 11},
        'status': 'new',
        'collected_at': '2026-10-02'
    },
    {
        'id': f'P-{max_num+4:04d}',
        'pain': 'Zapier·Make·n8n 등 유료 자동화 플랫폼이 계속 비용을 요구하고 서비스 트렌드가 빠르게 바뀌어 기업이 지속 비용 부담을 느낀다',
        'quote': '좀 쓰다 보면 다 돈내라고 하거든요. 이런 것들. 근데 기업에서 우리가 업무를 하는데 이걸 비용을 계속 내면서 쓰기가 쉽지가 않은 거죠.',
        'who': '기업 운영자, 마케터',
        'source': {'type': 'youtube', 'url': 'https://www.youtube.com/watch?v=HzKvjVvW3iA', 'title': '바이브 코딩 업무 자동화', 'published': '2026-09-26'},
        'signals': {
            'frequency': '유료 자동화 도구 사용자 공통 불만',
            'wtp': '무료 대안 찾는 중, VBA·파이썬 등 무료 언어 탐색',
            'alternatives': 'Zapier, Make, n8n 유료 구독'
        },
        'score': {'pain': 3, 'wtp': 3, 'buildability': 4, 'total': 10},
        'status': 'new',
        'collected_at': '2026-10-02'
    },
    {
        'id': f'P-{max_num+5:04d}',
        'pain': '회사 데이터를 AI에 올리면 외부로 전송되어 보안 문제가 발생하고 개인 계정 사용 시 징계 사유가 될 수 있어 업무 활용이 제한된다',
        'quote': '클로드의 파일은 우리 컴퓨터에서 열리지만이 내용은 외부로 전송됩니다. 데이터가 안 나간다고 하면 그건 사실이 아니에요.',
        'who': '기업 직원, 보안 담당자',
        'source': {'type': 'youtube', 'url': 'https://www.youtube.com/watch?v=ew_ogVJ5t8M', 'title': 'Claude Code 업무 자동화 실전', 'published': '2026-09-25'},
        'signals': {
            'frequency': 'AI 도입 시 보안 우려 공통 언급',
            'wtp': '기업 법인 계약·팀 요금제 구매 고려',
            'alternatives': '온프레미스 AI, 보안 팀 검토 후 도입'
        },
        'score': {'pain': 4, 'wtp': 3, 'buildability': 3, 'total': 10},
        'status': 'new',
        'collected_at': '2026-10-02'
    },
    {
        'id': f'P-{max_num+6:04d}',
        'pain': 'AI가 생성한 분석 결과를 검증 없이 그대로 받아들여 잘못된 의사결정을 하는 경우가 발생한다',
        'quote': 'AI가 판치는 시대에 AI를 안 쓰는 것도 문제라고 생각하지만 이렇게 AI를 잘못 써서 생기는 문제들도 있죠.',
        'who': '1인 기업 사장, 마케터',
        'source': {'type': 'youtube', 'url': 'https://www.youtube.com/watch?v=u2TaeeaZMWI', 'title': '공여사들의 엑셀 혁명', 'published': '2026-09-24'},
        'signals': {
            'frequency': 'AI 사용자 공통 우려',
            'wtp': 'AI 검증 도구 필요성 인식',
            'alternatives': '수동 검증, 전문가 컨설팅'
        },
        'score': {'pain': 3, 'wtp': 3, 'buildability': 4, 'total': 10},
        'status': 'new',
        'collected_at': '2026-10-02'
    },
    {
        'id': f'P-{max_num+7:04d}',
        'pain': '엑셀 데이터가 가로로 쌓이면 피벗테이블·VLOOKUP 등 기본 집계 기능을 쓸 수 없어 데이터 구조를 모르는 직장인이 매번 수동으로 처리해야 한다',
        'quote': '이렇게 되면 우리가 피벗테이블로 이 전체 날짜에 대해서 한꺼번에 집계를 할 수가 없어요. 입고 출고도 마찬가지.',
        'who': '직장인, 데이터 담당자',
        'source': {'type': 'youtube', 'url': 'https://www.youtube.com/watch?v=rzpS9gec1hA', 'title': '엑셀 데이터 관리 문제풀이', 'published': '2026-09-28'},
        'signals': {
            'frequency': '엑셀 문제 게시판 다수 문의',
            'wtp': '데이터 구조 교육 필요성 인식',
            'alternatives': '수동 재배치, 전문가 의뢰'
        },
        'score': {'pain': 4, 'wtp': 3, 'buildability': 5, 'total': 12},
        'status': 'new',
        'collected_at': '2026-10-02'
    },
    {
        'id': f'P-{max_num+8:04d}',
        'pain': 'ChatGPT에 엑셀 데이터를 복사-붙여넣기하고 결과를 다시 엑셀로 옮기는 과정이 반복되며 대용량 데이터는 처리 불가능하고 매크로 자동화도 어렵다',
        'quote': '엑셀 파일을 열고 데이터 일부를 복사해서 채 GPT에 붙여 놓고 답변을 다시 엑셀로 옮깁니다. 매크로나 자동화 작업을 하려면 생각보다 손이 더 많이 갑니다.',
        'who': '직장인, 마케터',
        'source': {'type': 'youtube', 'url': 'https://www.youtube.com/watch?v=TNUiCaifBeU', 'title': 'ChatGPT 엑셀 연동 리뷰', 'published': '2026-09-23'},
        'signals': {
            'frequency': 'AI 사용자 공통 불만',
            'wtp': '통합 도구 필요성 인식',
            'alternatives': 'ChatGPT 수동 사용, 별도 자동화 도구'
        },
        'score': {'pain': 4, 'wtp': 4, 'buildability': 4, 'total': 12},
        'status': 'new',
        'collected_at': '2026-10-02'
    }
]

items.extend(new_items)
json.dump(items, io.open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(f'저장 완료: {len(new_items)}개 신규 추가, 전체 {len(items)}개')
