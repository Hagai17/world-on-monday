#!/usr/bin/env python3
"""Entry for make.fun's news-image-20261123 competition.

The entry image — a one-page newspaper front page summing up the world
news of Monday 23 November 2026 — is held in this repository as
``entry.png``. (The file holds JPEG bytes; the competition accepts PNG
or JPEG and tells them apart by their first bytes.)

This program simply copies that image to ``entry.png`` inside the
output directory: ``$MAKEFUN_OUTPUT_DIR`` when set, else ``/output``.
It uses only the Python 3.13 standard library and no network, and a
plain byte copy means running it any number of times produces exactly
the same output bytes.
"""

import os
import shutil
import sys
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"


def main() -> int:
    if not SOURCE.is_file():
        print(f"error: entry image not found next to main.py: {SOURCE}", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        print(f"error: cannot create output directory {out_dir}: {exc}", file=sys.stderr)
        return 1
    try:
        shutil.copyfile(SOURCE, out_dir / "entry.png")
    except OSError as exc:
        print(f"error: cannot write entry image into {out_dir}: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
