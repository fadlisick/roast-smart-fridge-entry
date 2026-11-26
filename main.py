#!/usr/bin/env python3
"""Roast the Smart Fridge — one line, best laugh wins.

The entry is a single roast line for a smart home gadget. The line picks
an angle nobody else will: the robot vacuum is not a helpful cleaner,
it is a golden retriever — it eats a charging cable a month and then
plays a cheerful chime like it brought home a dead squirrel. Funny
first, original angle second.

Deterministic: no randomness, no network, no clock. The same line is
written on every run.
"""

import os
import sys

ROAST = (
    "My robot vacuum eats one charging cable a month and then plays "
    "a cheerful chime like a golden retriever bringing me a dead squirrel."
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
