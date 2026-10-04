#!/usr/bin/env python3
"""HTML to PDF via Chrome headless."""
import subprocess
import sys
from pathlib import Path

html_path = Path("05_reports/2026-10-04_대표이사_보고서_v2.html")
pdf_path = Path("05_reports/2026-10-04_대표이사_보고서_v2.pdf")

chrome_paths = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]

chrome = None
for p in chrome_paths:
    if Path(p).exists():
        chrome = p
        break

if not chrome:
    print("ERROR: Chrome/Edge not found")
    sys.exit(1)

print(f"Using: {chrome}")
result = subprocess.run(
    [
        chrome,
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        "--print-to-pdf=" + str(pdf_path.absolute()),
        "--print-to-pdf-no-header",
        str(html_path.absolute()),
    ],
    capture_output=True,
    text=True,
    timeout=60,
)

print(f"exit_code: {result.returncode}")
if result.stdout:
    print(f"stdout: {result.stdout[:500]}")
if result.stderr:
    print(f"stderr: {result.stderr[:500]}")

if pdf_path.exists():
    size = pdf_path.stat().st_size
    print(f"PDF created: {pdf_path.absolute()} ({size:,} bytes)")
else:
    print("ERROR: PDF not created")
    sys.exit(1)
