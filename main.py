#!/usr/bin/env python3
"""The Vacuum's Alibi: write the robot vacuum's one-line excuse to /output/entry.txt.

Stdlib only, no network. The line is a fixed literal: the vacuum drove over
the spot eleven times, found it unmoved, and reclassified it as a feature of
the floor, updating its map accordingly.
"""

import os

LINE = (
    "I drove over the spot eleven times. It did not move. "
    "I have reclassified it as a feature of the floor "
    "and updated my map accordingly."
)


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        raise SystemExit("line must be 1-200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"wrote {len(LINE)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
