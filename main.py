#!/usr/bin/env python3
"""Write the competition entry: one excuse line to entry.txt.

Standard library only. Deterministic: the same bytes on every run.
"""

import os

ENTRY = "Sorry boss, front door lock jammed overnight, locksmith can't come till noon so I'm stuck inside"


def main() -> None:
    # Self-check against the competition gate before writing anything:
    # one line, 1-140 characters, at most 20 words, valid UTF-8.
    assert 1 <= len(ENTRY) <= 140, "entry out of gate range"
    assert len(ENTRY.split()) <= 20, "entry over 20 words"
    assert "\n" not in ENTRY, "entry must be one line"
    ENTRY.encode("utf-8")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
