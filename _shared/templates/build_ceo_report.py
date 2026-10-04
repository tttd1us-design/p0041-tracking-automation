#!/usr/bin/env python3
"""10조 스튜디오 — 대표이사 보고서 HTML 빌더 (공식 양식 v1.0)

마크다운 + 공식 표지(문서정보·결재란) + 밝은 톤 CSS → 단일 HTML (PDF 인쇄용)

사용:
  python build_ceo_report.py <입력.md> <출력.html> <제목> <부제> [문서번호] [보고기간]

표지 구성 (한국 공식 업무보고서 관행 + CEO/Board Report 국제 표준):
  - 회사명 / 문서 분류 띠
  - 문서 유형 · 제목 · 부제
  - 문서 정보표 (문서번호·보고일·보고자·보고기간·수신·분류)
  - 결재란 (작성 / 검토 / 승인)
"""
import sys
import re
import subprocess
import html as html_mod
from datetime import datetime
from pathlib import Path

CSS_PATH = Path("D:/10jo_Studio/_shared/templates/ceo_report.css")


def build(md_path, out_path, title, subtitle, doc_num=None, period=None):
    md = Path(md_path).read_text(encoding="utf-8")
    css = CSS_PATH.read_text(encoding="utf-8")

    # 1) 마크다운 → HTML 본문 (pandoc GFM)
    proc = subprocess.run(
        ["pandoc", "-f", "gfm", "-t", "html5", "--no-highlight"],
        input=md.encode("utf-8"),
        capture_output=True,
    )
    if proc.returncode != 0:
        raise SystemExit(f"pandoc 실패: {proc.stderr.decode('utf-8', 'replace')}")
    body = proc.stdout.decode("utf-8")

    # 2) 문서 메타
    today = datetime.now()
    today_kr = today.strftime("%Y년 %m월 %d일")
    if not doc_num:
        doc_num = f"10JO-CEO-{today.strftime('%Y%m%d')}-01"
    if not period:
        period = today_kr

    # 3) 공식 표지
    cover = f"""
<div class="cover">
  <div class="cover-brand">
    <div class="cover-brand-name">10조 스튜디오</div>
    <div class="cover-brand-sub">10JO STUDIO · AI SOFTWARE COMPANY</div>
  </div>
  <div class="cover-band">대 표 이 사 보 고</div>

  <div class="cover-titleblock">
    <div class="cover-doc-type">CEO REPORT</div>
    <div class="cover-title">{html_mod.escape(title)}</div>
    <div class="cover-subtitle">{html_mod.escape(subtitle)}</div>
    <div class="cover-rule"></div>
  </div>

  <table class="cover-info">
    <tr>
      <th>문서번호</th><td>{html_mod.escape(doc_num)}</td>
      <th>보고일</th><td>{today_kr}</td>
    </tr>
    <tr>
      <th>보고자</th><td>10조 수석 (총괄 기획·지휘 본부)</td>
      <th>보고기간</th><td>{html_mod.escape(period)}</td>
    </tr>
    <tr>
      <th>수신</th><td>대표이사 이상완</td>
      <th>분류</th><td>경영진 보고용 · CONFIDENTIAL</td>
    </tr>
    <tr>
      <th>검토</th><td>10조 수석 (Hermes Agent)</td>
      <th>상태</th><td>대표 승인 대기</td>
    </tr>
  </table>

  <table class="cover-approval">
    <tr>
      <th>작 성</th><th>검 토</th><th>승 인</th>
    </tr>
    <tr>
      <td>10조 수석</td>
      <td>10조 수석</td>
      <td>대표이사</td>
    </tr>
  </table>

  <div class="cover-foot">
    10조 스튜디오 · 본 문서는 대표이사 보고용으로 무단 복제·배포를 금합니다.
  </div>
</div>
"""

    # 4) 목차 — 계층형 (h1 대분류 + h2 중분류)
    toc_html = ""
    h1s = re.findall(r"<h1[^>]*>(.*?)</h1>", body, re.DOTALL)
    h2s = re.findall(r"<h2[^>]*>(.*?)</h2>", body, re.DOTALL)
    if len(h1s) >= 4:
        def clean(t):
            return html_mod.escape(re.sub(r"<[^>]+>", "", t).strip())

        items = []
        # h1/h2 등장 순서를 유지하며 계층 구성
        for m in re.finditer(r"<h([12])[^>]*>(.*?)</h\1>", body, re.DOTALL):
            lvl, txt = m.group(1), clean(m.group(2))
            if not txt:
                continue
            if lvl == "1":
                items.append(
                    f'<li style="font-weight:700;color:#0d2a4d;'
                    f'margin-top:3.5mm;padding-bottom:1.2mm;'
                    f'border-bottom:1px solid #cfd8dc">{txt}</li>'
                )
            else:
                items.append(
                    f'<li style="list-style:none;padding-left:6mm;'
                    f'color:#37474f;font-size:9.5pt;margin-bottom:1.2mm">'
                    f'— {txt}</li>'
                )
        toc_html = (
            '<div style="page-break-after:always">'
            '<h1 style="margin-top:0;border-bottom:2px solid #1a3a6b">목차</h1>'
            '<ul style="list-style:none;padding-left:0;margin-top:4mm">'
            + "".join(items) +
            "</ul></div>"
        )

    # 5) 조립
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
    if len(sys.argv) < 5:
        raise SystemExit(__doc__)
    build(
        sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4],
        sys.argv[5] if len(sys.argv) > 5 else None,
        sys.argv[6] if len(sys.argv) > 6 else None,
    )
