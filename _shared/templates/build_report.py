#!/usr/bin/env python3
"""10조 스튜디오 정식 보고서 HTML 빌더

마크다운 + 표지 + CSS → 단일 HTML (PDF 인쇄용)
사용: python build_report.py <입력.md> <출력.html> [제목] [부제]
"""
import sys
import subprocess
import html as html_mod
from pathlib import Path

CSS_PATH = Path("D:/10jo_Studio/_shared/templates/report.css")


def build(md_path: str, out_path: str, title: str, subtitle: str) -> None:
    md = Path(md_path).read_text(encoding="utf-8")
    css = CSS_PATH.read_text(encoding="utf-8")

    # 1) 마크다운 → HTML 본문 (pandoc, GFM)
    proc = subprocess.run(
        ["pandoc", "-f", "gfm", "-t", "html5", "--no-highlight"],
        input=md.encode("utf-8"),
        capture_output=True,
    )
    if proc.returncode != 0:
        raise SystemExit(f"pandoc 실패: {proc.stderr.decode('utf-8', 'replace')}")
    body = proc.stdout.decode("utf-8")

    # 2) 표지 HTML (대표이사 대시보드 스타일)
    from datetime import datetime
    today = datetime.now().strftime("%Y년 %m월 %d일")
    doc_num = f"10JO-RPT-{datetime.now().strftime('%Y-%m-%d')}-001"
    
    cover = f"""
<div class="cover">
  <div class="cover-header">
    <div class="cover-company">10조 스튜디오</div>
    <div class="cover-date">{today}</div>
  </div>
  <div class="cover-title">{html_mod.escape(title)}</div>
  <div class="cover-subtitle">{html_mod.escape(subtitle)}</div>
  
  <div class="cover-kpi">
    <div class="kpi-card">
      <div class="kpi-label">매출</div>
      <div class="kpi-value">0</div>
      <div class="kpi-unit">원</div>
    </div>
    <div class="kpi-card">
      <div class="kpi-label">불편 발굴</div>
      <div class="kpi-value">30</div>
      <div class="kpi-unit">건</div>
    </div>
    <div class="kpi-card">
      <div class="kpi-label">개발 완료</div>
      <div class="kpi-value">1</div>
      <div class="kpi-unit">제품</div>
    </div>
    <div class="kpi-card">
      <div class="kpi-label">승인 대기</div>
      <div class="kpi-value">3</div>
      <div class="kpi-unit">건</div>
    </div>
  </div>
  
  <div class="cover-progress">
    <div class="progress-item">
      <div class="progress-label"><span>Merge10 개발</span><span>100%</span></div>
      <div class="progress-bar"><div class="progress-fill" style="width:100%"></div></div>
    </div>
    <div class="progress-item">
      <div class="progress-label"><span>사업계획서</span><span>100%</span></div>
      <div class="progress-bar"><div class="progress-fill" style="width:100%"></div></div>
    </div>
    <div class="progress-item">
      <div class="progress-label"><span>외부 배포</span><span>0%</span></div>
      <div class="progress-bar"><div class="progress-fill" style="width:0%"></div></div>
    </div>
    <div class="progress-item">
      <div class="progress-label"><span>결제 연동</span><span>0%</span></div>
      <div class="progress-bar"><div class="progress-fill" style="width:0%"></div></div>
    </div>
  </div>
  
  <div class="cover-approval">
    <div class="cover-approval-title">🔔 대표 승인 요청</div>
    <div class="cover-approval-item">1. Merge10 외부 배포 — 라이브 URL 공개</div>
    <div class="cover-approval-item">2. 결제 연동 — 카드/계좌이체/카카오페이</div>
    <div class="cover-approval-item">3. 도메인 구매 — 15,000원/년</div>
  </div>
  
  <div class="cover-classification">문서번호 {doc_num} · 대표이사 전용 · CONFIDENTIAL</div>
</div>
"""

    # 3) 목차 생성 (10개 이상의 장이 있을 때)
    toc_html = ""
    h2_count = body.count("<h2")
    if h2_count >= 10:
        toc_html = '<div class="toc"><h2>목차</h2><ul>'
        # h2 태그에서 제목 추출
        import re
        h2_matches = re.findall(r'<h2[^>]*>(.*?)</h2>', body, re.DOTALL)
        for h2 in h2_matches:
            # HTML 태그 제거
            clean = re.sub(r'<[^>]+>', '', h2).strip()
            if clean:
                toc_html += f'<li>{html_mod.escape(clean)}</li>'
        toc_html += '</ul></div>'

    # 4) 최종 HTML 조립
    doc = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<title>{html_mod.escape(title)}</title>
<style>
{css}
</style>
</head>
<body>
{cover}
{toc_html}
{body}
</body>
</html>
"""
    Path(out_path).write_text(doc, encoding="utf-8")
    print(f"OK  {out_path}  ({len(doc):,} chars)")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise SystemExit(__doc__)
    t = sys.argv[3] if len(sys.argv) > 3 else "정식 사업계획서"
    s = sys.argv[4] if len(sys.argv) > 4 else ""
    build(sys.argv[1], sys.argv[2], t, s)
