#!/usr/bin/env python3
"""One Word, One Username, One Reward.

Writes a single username to entry.txt in the output directory.
The username is one word, 12 characters, with no spaces or padding.
The output is fully deterministic: every run writes identical bytes.
"""

import os

USERNAME = "TotallyHuman"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(USERNAME)


if __name__ == "__main__":
    main()
