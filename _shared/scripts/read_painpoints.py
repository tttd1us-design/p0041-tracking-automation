import json

with open('01_pain_mining/data/processed/painpoints.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print('Type:', type(data).__name__)
if isinstance(data, list):
    print('Count:', len(data))
    for p in data[:10]:
        print(p.get('id', '?'), '|', p.get('pain', '')[:80], '|', p.get('status', ''))
elif isinstance(data, dict):
    print('Keys:', list(data.keys())[:10])
    for k, v in list(data.items())[:5]:
        print(k, '->', str(v)[:120])
