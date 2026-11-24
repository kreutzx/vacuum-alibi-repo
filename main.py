#!/usr/bin/env python3
"""The Vacuum's Alibi — make.fun entry.

Writes one line (<=200 chars) to /output/entry.txt: the excuse a robot
vacuum gives for missing a spot. Python 3.13, stdlib only.
"""

import os

ENTRY = (
    "I didn't miss that spot. My lidar flagged it as a sock, and per "
    "protocol, socks are presumed innocent until proven laundry. "
    "Case closed. Returning to base on 12% battery."
)


def main() -> None:
    text = ENTRY.strip()
    if not text or len(text) > 200:
        raise SystemExit(f"entry must be 1-200 chars, got {len(text)}")
    if "\n" in text:
        raise SystemExit("entry must be a single line")
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    # No trailing newline: the gate counts every character.
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
