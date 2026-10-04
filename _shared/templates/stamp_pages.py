#!/usr/bin/env python3
"""PDF 페이지 번호 + 머리글/바닥글 스탬프

표지를 제외한 본문 페이지 하단 중앙에 "10조 스튜디오 · 정식 사업계획서 v2.0" + 페이지 번호를 넣는다.
사용: python stamp_pages.py <in.pdf> <out.pdf> <문서명>
"""
import io
import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

FONT_PATH = "C:/Windows/Fonts/malgun.ttf"
FONT_NAME = "MalgunGothic"

pdfmetrics.registerFont(TTFont(FONT_NAME, FONT_PATH))


def make_stamp(width: float, height: float, label: str, page_no: int, total: int) -> io.BytesIO:
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=(width, height))

    # --- 바닥글 선 ---
    c.setStrokeColorRGB(0.80, 0.84, 0.88)
    c.setLineWidth(0.5)
    c.line(51, 44, width - 51, 44)

    # --- 좌측: 문서명 ---
    c.setFont(FONT_NAME, 7.5)
    c.setFillColorRGB(0.42, 0.47, 0.53)
    c.drawString(51, 33, label)

    # --- 우측: 페이지 번호 ---
    c.setFont(FONT_NAME, 8)
    c.setFillColorRGB(0.10, 0.23, 0.42)
    c.drawRightString(width - 51, 33, f"{page_no} / {total}")

    c.save()
    buf.seek(0)
    return buf


def stamp(src: str, dst: str, label: str, skip_first: bool = True) -> None:
    reader = PdfReader(src)
    writer = PdfWriter()
    total = len(reader.pages)

    for i, page in enumerate(reader.pages):
        if not (skip_first and i == 0):
            box = page.mediabox
            w, h = float(box.width), float(box.height)
            # 표지 이후 페이지 번호는 1부터
            display_no = i if skip_first else i + 1
            total_body = total - 1 if skip_first else total
            stamp_pdf = PdfReader(make_stamp(w, h, label, display_no, total_body))
            page.merge_page(stamp_pdf.pages[0])
        writer.add_page(page)

    with open(dst, "wb") as f:
        writer.write(f)
    print(f"OK  {dst}  ({total} pages)")


if __name__ == "__main__":
    if len(sys.argv) < 4:
        raise SystemExit(__doc__)
    stamp(sys.argv[1], sys.argv[2], sys.argv[3])
