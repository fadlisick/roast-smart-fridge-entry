#!/usr/bin/env python3
"""Roast the Smart Fridge — one line, best laugh wins.

The entry is a single roast line for the smart fridge. The line picks
an angle nobody else will: the fridge is not a helpful appliance, it
is a dairy snitch — a 3 AM text about expired milk, Wi-Fi included,
with abandonment issues. Funny first, original angle second.

Deterministic: no randomness, no network, no clock. The same line is
written on every run.
"""

import os
import sys

ROAST = (
    "My smart fridge texts me at 3 AM to say the milk expired, "
    "like I hired a dairy snitch with Wi-Fi and abandonment issues."
)


def main() -> int:
    # Gate guard: the sealed scorer requires 1 to 160 characters,
    # not only white space. Refuse to write anything out of range
    # rather than submit a line the gate would score 0.
    stripped = ROAST.strip()
    if not 1 <= len(stripped) <= 160:
        raise ValueError("roast line outside the 1-160 character gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(ROAST)
    return 0


if __name__ == "__main__":
    sys.exit(main())
