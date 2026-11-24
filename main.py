#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse — entry program.

Reads the one-line entry from entry.txt next to this file, validates
the competition gate (exactly one line, 1-200 characters, not only
whitespace), and writes it byte-for-byte to
$MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os
import sys

MAX_CHARS = 200


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.txt")
    with open(src, "r", encoding="utf-8") as f:
        text = f.read()

    if "\n" in text or "\r" in text:
        print("error: entry must be exactly one line", file=sys.stderr)
        return 1
    if not 1 <= len(text) <= MAX_CHARS:
        print(
            "error: entry must be 1-%d characters, got %d"
            % (MAX_CHARS, len(text)),
            file=sys.stderr,
        )
        return 1
    if not text.strip():
        print("error: entry must not be only whitespace", file=sys.stderr)
        return 1
    if text != text.strip():
        print("error: entry must not start or end with whitespace",
              file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("error: MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Verify the write: read the output back and compare byte-for-byte.
    with open(out_path, "rb") as f:
        written = f.read()
    if written != text.encode("utf-8"):
        print("error: written output does not match entry.txt",
              file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
