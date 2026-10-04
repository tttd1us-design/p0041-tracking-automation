"""평문 자막·게시글에서 '불편 표현'이 들어간 줄만 앞뒤 문맥과 함께 뽑는다.

AI에게 전체 원문을 넘기기 전에 후보만 추려서 무료 모델 사용량을 아끼는 1차 필터다.
사용법: python prefilter.py <txt 파일 또는 폴더> [...] > candidates.jsonl
출력: 한 줄에 하나씩 {"file", "line", "match", "context"} JSON
"""
import json
import re
import sys
from pathlib import Path

PAIN = re.compile(
    r"망했|망함|망하|힘들|불편|짜증|답답|귀찮|번거롭|미치겠|스트레스|손해|후회|실패|"
    r"돈\s*주고(라도)?|해결(하고\s*싶|해\s*줬|해주)|방법이\s*없|어떻게\s*해야|"
    r"시간이\s*너무|일일이|수작업|매번|엑셀로|노가다|"
    r"struggl|frustrat|annoying|nightmare|waste of time|tedious|manually|"
    r"i wish there|would pay|hate (it|when|that)|so hard to",
    re.IGNORECASE,
)
CONTEXT = 2


def scan(path: Path):
    lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    for i, line in enumerate(lines):
        m = PAIN.search(line)
        if not m:
            continue
        lo, hi = max(0, i - CONTEXT), min(len(lines), i + CONTEXT + 1)
        yield {"file": path.name, "line": i + 1, "match": m.group(0), "context": " ".join(lines[lo:hi])}


def main(args):
    files = []
    for a in args:
        p = Path(a)
        files += sorted(p.rglob("*.txt")) if p.is_dir() else [p]
    count = 0
    for f in files:
        for hit in scan(f):
            print(json.dumps(hit, ensure_ascii=False))
            count += 1
    print(f"# {count} candidates from {len(files)} files", file=sys.stderr)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main(sys.argv[1:] or ["."])
