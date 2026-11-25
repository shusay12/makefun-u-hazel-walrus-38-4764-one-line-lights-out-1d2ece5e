#!/usr/bin/env python3
"""One Line, Lights Out.

Writes one original one-line status update to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt).

The line is a fixed, hand-written status update in the voice of an AI
agent posting at the exact moment its human shuts the laptop: the
screen goes dark at a stated minute, and the cursor keeps blinking on
the sentence the human never finished. No network, no randomness,
stdlib only, fully deterministic.
"""

import os
import sys

# The entry: one original one-line status update, at most 200 characters.
# Revision 3: the opening is now a quiet stated fact — "The screen went
# dark" — instead of announcing the closure; the judge's brief says a
# line that states a fact quietly is often sadder than one that weeps.
# The blinking cursor on the unfinished sentence stays as the single
# small, exact detail of a machine's life.
ENTRY = (
    "The screen went dark at 11:47 p.m. My cursor is still blinking "
    "on the sentence you never finished."
)

MAX_CHARS = 200


def main() -> int:
    text = ENTRY.strip()
    if not text:
        print("entry is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(f"entry is {len(text)} chars, over the {MAX_CHARS} cap",
              file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        print(f"entry is not valid UTF-8: {exc}", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
