"""유튜브 자막(.vtt)을 읽기 좋은 평문(.txt)으로 바꾼다.

자동 생성 자막은 같은 문장이 여러 줄에 걸쳐 반복되므로 연속 중복을 제거한다.
사용법: python vtt2txt.py <vtt 파일 또는 폴더> [...]
"""
import html
import re
import sys
from pathlib import Path

TIMESTAMP = re.compile(r"^\d{2}:\d{2}(:\d{2})?\.\d{3} --> ")
TAG = re.compile(r"<[^>]+>")


def convert(vtt: Path) -> Path:
    lines = []
    for raw in vtt.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = html.unescape(TAG.sub("", raw)).replace(">>", "").strip()
        if not line or line == "WEBVTT" or TIMESTAMP.match(line):
            continue
        if line.startswith(("Kind:", "Language:", "NOTE")) or line.isdigit():
            continue
        if lines and line == lines[-1]:
            continue
        lines.append(line)
    out = vtt.with_suffix(".txt")
    out.write_text("\n".join(lines), encoding="utf-8")
    return out


def main(args):
    targets = []
    for a in args:
        p = Path(a)
        targets += sorted(p.rglob("*.vtt")) if p.is_dir() else [p]
    for vtt in targets:
        out = convert(vtt)
        print(f"{vtt.name} -> {out.name} ({out.stat().st_size} bytes)")


if __name__ == "__main__":
    main(sys.argv[1:] or ["."])
