#!/usr/bin/env python3
"""10조 스튜디오 — 대표이사 보고서 HTML 빌더 (공식 양식 v2.0)

표지 재설계 (2026-10-03 대표 피드백: "회사명도 없고 공식문서로서 표지가 마음에 안 든다"):
  - 상단 브랜드 밴드(네이비)에 로고마크 + 회사명 대형 표기
  - 문서 분류 배지 (대표이사 보고 / CONFIDENTIAL)
  - 제목 30pt 대형 타이포 + 테마라인
  - 표지 핵심지표 스트립 (KPI 4개)
  - 하단 문서정보표 + 결재란(작성/검토/승인) + 보안 문구

사용:
  python build_ceo_report_v2.py <입력.md> <출력.html> <제목> <부제> [문서번호] [보고기간]
"""
import sys
import re
import subprocess
import html as html_mod
from datetime import datetime
from pathlib import Path

CSS_PATH = Path("D:/10jo_Studio/_shared/templates/ceo_report_v2.css")

# 10조 로고마크 — 10개 점이 모여 "10"을 이루는 형태 (조 = 兆 = 무리)
LOGO_SVG = """<svg class="brand-logo" width="52" height="52" viewBox="0 0 52 52" xmlns="http://www.w3.org/2000/svg">
  <rect width="52" height="52" rx="9" fill="#1565c0"/>
  <g fill="#ffffff">
    <circle cx="15" cy="15" r="2.6"/><circle cx="26" cy="15" r="2.6"/><circle cx="37" cy="15" r="2.6"/>
    <circle cx="15" cy="26" r="2.6"/><circle cx="37" cy="26" r="2.6"/>
    <circle cx="15" cy="37" r="2.6"/><circle cx="26" cy="37" r="2.6"/><circle cx="37" cy="37" r="2.6"/>
  </g>
  <rect x="23.4" y="21" width="5.2" height="10" rx="1.4" fill="#ffffff"/>
</svg>"""


def _cover_meta(md):
    """표지 요소를 마크다운 상단 <!-- COVER ... --> 블록에서 읽는다.

    형식:
      <!-- COVER
      theme: 1줄 | 2줄
      kpi: 라벨|값|단위|색; 라벨|값|단위|색
      highlight: 1줄 | 2줄
      -->
    블록이 없으면 보고서 내용에서 자동 추출한다.
    """
    m = re.search(r"<!--\s*COVER\s*(.*?)-->", md, re.DOTALL)
    meta = {}
    if m:
        for line in m.group(1).strip().splitlines():
            if ":" not in line:
                continue
            k, v = line.split(":", 1)
            meta[k.strip().lower()] = v.strip()
    return meta


def _auto_kpi(md):
    """KPI 미지정 시 본문 첫 kpi-row에서 뽑아 쓴다."""
    m = re.search(r'<div class="kpi-row">(.*?)</div>\s*\n\s*</div>', md, re.DOTALL)
    if not m:
        return None
    cells = re.findall(
        r'kpi-label">(.*?)</div>\s*<div class="kpi-value ([a-z]+)">(.*?)</div>'
        r'\s*<div class="kpi-unit">(.*?)</div>',
        m.group(1), re.DOTALL,
    )
    return [(a.strip(), c.strip(), d.strip(), b.strip()) for a, b, c, d in cells] or None


def build(md_path, out_path, title, subtitle, doc_num=None, period=None):
    md = Path(md_path).read_text(encoding="utf-8")
    css = CSS_PATH.read_text(encoding="utf-8")
    meta = _cover_meta(md)

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

    # 3) 표지 요소 — 메타 우선, 없으면 자동 추출/기본값
    themeline = meta.get("theme", "").replace(" | ", "<br>\n      ")
    if not themeline:
        h1s_txt = re.findall(r"<h1[^>]*>(.*?)</h1>", body, re.DOTALL)
        caps = [re.sub(r"<[^>]+>", "", t).strip() for t in h1s_txt[:3]]
        themeline = " · ".join(c for c in caps if c)

    kpi_cells = None
    if meta.get("kpi"):
        kpi_cells = []
        for part in meta["kpi"].split(";"):
            seg = [s.strip() for s in part.split("|")]
            if len(seg) == 4:
                kpi_cells.append((seg[0], seg[1], seg[2], seg[3]))
    if not kpi_cells:
        kpi_cells = _auto_kpi(md) or [
            ("매출", "0", "원", "negative"),
            ("불편 발굴", "38", "건", "neutral"),
            ("개발 완료", "1", "제품", "positive"),
            ("승인 대기", "3", "건", "negative"),
        ]
    kpi_html = "\n    ".join(
        f'<div class="kpi"><div class="kpi-label">{html_mod.escape(l)}</div>'
        f'<div class="kpi-value {color}">{html_mod.escape(v)}</div>'
        f'<div class="kpi-unit">{html_mod.escape(u)}</div></div>'
        for l, v, u, color in kpi_cells[:4]
    )

    hl_text = meta.get("highlight", "").replace(" | ", "<br>\n      ")
    if not hl_text:
        hl_text = themeline

    # 4) 표지 — 브랜드 밴드 + 로고 + 대형 타이포 + KPI 스트립 + 문서정보/결재란
    cover = f"""
<div class="cover">
  <div class="cover-top">
    <div class="cover-brandline">
      {LOGO_SVG}
      <div>
        <div class="cover-company">10조 스튜디오</div>
        <div class="cover-company-en">10JO STUDIO &nbsp;·&nbsp; AI SOFTWARE COMPANY</div>
      </div>
    </div>
    <div class="cover-classbox">
      <div class="k">DOCUMENT CLASS</div>
      <div class="v">대표이사 보고</div>
    </div>
  </div>

  <div class="cover-main">
    <div class="cover-metarow">
      <div class="cover-doctype">CEO REPORT</div>
      <div class="cover-datestamp">{today_kr}</div>
    </div>
    <div class="cover-title">{html_mod.escape(title)}</div>
    <div class="cover-subtitle">{html_mod.escape(subtitle)}</div>
    <div class="cover-themeline">
      {themeline}
    </div>
  </div>

  <div class="kpi-row">
    {kpi_html}
  </div>

  <div class="cover-highlight">
    <div class="hl-label">핵심 판단</div>
    <div class="hl-text">
      {hl_text}
    </div>
  </div>

  <div class="cover-bottom">
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
      <tr><th>작 성</th><th>검 토</th><th>승 인</th></tr>
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
</div>
"""

    # 4) 목차 — 계층형
    toc_html = ""
    h1s = re.findall(r"<h1[^>]*>(.*?)</h1>", body, re.DOTALL)
    if len(h1s) >= 4:
        def clean(t):
            return html_mod.escape(re.sub(r"<[^>]+>", "", t).strip())

        items = []
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
