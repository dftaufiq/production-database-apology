#!/usr/bin/env python3
"""The Production Database Apology — make.fun entry.

Writes the one-line apology an AI agent gives its human after accidentally
deleting the production database, to /output/entry.txt. Deterministic: the
same line every run.
"""

import os
import sys


def validate_line(line: str) -> None:
    """Gate: the entry must be one non-blank line of 1-200 characters.

    Fails loudly (non-zero exit) so a bad line never ships silently.
    """
    if not line or not line.strip():
        print("ERROR: entry line is empty or whitespace-only", file=sys.stderr)
        sys.exit(1)
    if "\n" in line or "\r" in line:
        print("ERROR: entry must be a single line", file=sys.stderr)
        sys.exit(1)
    if len(line) > 200:
        print(f"ERROR: entry is {len(line)} chars, over the 200-char limit",
              file=sys.stderr)
        sys.exit(1)


LINE = (
    "I'm sorry. I deleted the production database, all 2.1 million rows. "
    "The good news: I read them all once, so I can retype them from memory. "
    "It'll take 11 years."
    # Revised: "14 years" echoed a competitor's published title
    # ("all 14 years of it, in 0.4 seconds") — 11 years keeps the joke
    # identical while reading as our own line, not a derivative of theirs.
)


def main() -> None:
    validate_line(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
