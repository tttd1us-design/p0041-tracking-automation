import sys, os
sys.path.insert(0, 'D:/hermes/cache/scratch/pylibs')
os.chdir('D:/10jo_Studio')

import markdown
from pathlib import Path

md_path = Path('05_reports/2026-10-03_대표이사_보고서.md')
html_path = Path('05_reports/2026-10-03_대표이사_보고서.html')
css = Path('_shared/templates/ceo_report_v2.css').read_text(encoding='utf-8')
md_text = md_path.read_text(encoding='utf-8')

md = markdown.Markdown(extensions=['fenced_code','tables','meta'])
body = md.convert(md_text)
meta = md.Meta

cover = {}
if 'cover' in meta:
    for line in meta['cover']:
        if line.startswith('theme:'): cover['theme'] = line[6:].strip()
        elif line.startswith('kpi:'): cover['kpi'] = line[4:].strip()
        elif line.startswith('highlight:'): cover['highlight'] = line[10:].strip()

title = '10조 스튜디오 대표이사 보고서'
subtitle = '2026-10-03 18:46 (KST) · 17:46~18:46 1시간'
docno = '10JO-CEO-20261003-02'
period = '2026-10-03 17:46~18:46'

theme_lines = cover.get('theme','').split('|')
kpi_str = cover.get('kpi','')
highlight_lines = cover.get('highlight','').split('|')

kpi_items = []
if kpi_str:
    for item in kpi_str.split(';'):
        parts = [p.strip() for p in item.split('|')]
        if len(parts) >= 4: kpi_items.append(parts)

html = f'''<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<title>{title}</title>
<style>{css}</style>
</head>
<body>
<div class="cover">
  <div class="brand-band">
    <svg class="brand-logo" width="52" height="52" viewBox="0 0 52 52" xmlns="http://www.w3.org/2000/svg">
      <rect width="52" height="52" rx="9" fill="#1565c0"/>
      <g fill="#ffffff">
        <circle cx="15" cy="15" r="2.6"/><circle cx="26" cy="15" r="2.6"/><circle cx="37" cy="15" r="2.6"/>
        <circle cx="15" cy="26" r="2.6"/><circle cx="37" cy="26" r="2.6"/>
        <circle cx="15" cy="37" r="2.6"/><circle cx="26" cy="37" r="2.6"/><circle cx="37" cy="37" r="2.6"/>
      </g>
      <rect x="23.4" y="21" width="5.2" height="10" rx="1.4" fill="#ffffff"/>
    </svg>
    <div><div class="brand-name">10조 스튜디오</div><div class="brand-sub">10조 Studio · CEO Report</div></div>
    <span class="badge badge-report">대표이사 보고</span>
  </div>
  <div class="meta-row">보고서 · {docno} · {period} · CONFIDENTIAL</div>
  <h1>{title}</h1>
  <div class="subtitle">{subtitle}</div>
  <div class="theme-line"><div class="theme-bar"></div><div class="theme-text">{theme_lines[0] if len(theme_lines)>0 else ''}<br>{theme_lines[1] if len(theme_lines)>1 else ''}</div></div>
  <div class="kpi-row">'''
for ki in kpi_items:
    html += f'<div class="kpi"><strong>{ki[0]}</strong><span>{ki[1]}</span><small>{ki[2]}</small></div>'
html += '''</div>
  <div class="highlight-box"><div class="highlight-title">핵심 판단</div><div class="highlight-text">'''
html += highlight_lines[0] if len(highlight_lines)>0 else ''
if len(highlight_lines)>1: html += '<br>' + highlight_lines[1]
html += '''</div></div>
  <table class="docinfo">
    <tr><td>문서번호</td><td>''' + docno + '''</td><td>보고일</td><td>2026-10-03 18:46</td></tr>
    <tr><td>보고자</td><td>10조 수석</td><td>보고기간</td><td>17:46~18:46</td></tr>
    <tr><td>수신</td><td>대표이사</td><td>분류</td><td>CONFIDENTIAL</td></tr>
    <tr><td>검토</td><td>Claude Code 기술 고문 / Antigravity</td><td>상태</td><td>배포 승인 대기</td></tr>
  </table>
  <div class="signatures">
    <div class="sig"><span>작성</span><b>10조 수석</b></div><div class="sig"><span>검토</span><b>Claude Code 고문</b></div><div class="sig"><span>승인</span><b>대표이사</b></div>
  </div>
  <div class="security">무단 복제·배포 금지 · 10조 스튜디오 CONFIDENTIAL</div>
</div>
''' + body + '''
</body>
</html>'''

html_path.write_text(html, encoding='utf-8')
print('HTML 생성:', html_path)
