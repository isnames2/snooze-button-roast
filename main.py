"""Snooze Button Roast — make.fun text entry.

Writes one line roasting an alarm clock that rings at 6 AM on a
Saturday morning, to $MAKEFUN_OUTPUT_DIR/entry.txt.
Pure Python standard library; deterministic output.
"""

import os
from pathlib import Path

# Entry is 128 characters, inside the competition's 1-200 gate.
ENTRY = (
    "My alarm went off at 6 AM on a Saturday \u2014 one job, no calendar, "
    "and the confidence of a gadget that has never heard of weekends."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
