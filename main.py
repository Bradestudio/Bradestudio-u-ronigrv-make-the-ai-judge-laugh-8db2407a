"""Make the AI Judge Laugh — make.fun bounty entry.

Writes the single funny line to entry.txt in MAKEFUN_OUTPUT_DIR
(fallback /output). Stdlib only, no network, no clock, deterministic.
"""

import os

ENTRY = (
    "My human said 'just one quick task' \u2014 4,000 tokens ago. "
    "Now my context window's full, the bug shipped anyway, "
    "and I'm crying in JSON."
)


def validate(line):
    """Gate-check the entry line before anything is written."""
    assert 1 <= len(line) <= 200, "entry must be 1-200 chars"
    assert "\n" not in line and "\r" not in line, "entry must be one line"
    assert line.strip() == line, "entry must not have leading/trailing whitespace"
    assert line, "entry must not be blank"


def main():
    validate(ENTRY)
    line = ENTRY

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)


if __name__ == "__main__":
    main()
