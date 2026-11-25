#!/usr/bin/env python3
"""Copy the pre-rendered entry image to the output directory.

Standard library only: the grading sandbox installs nothing, so this
program imports nothing beyond the standard library. The image itself
was drawn on the build machine and ships in the repository as entry.png.
"""
import os
import shutil
import sys
from pathlib import Path


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    src = Path(__file__).resolve().parent / "entry.png"
    dst = Path(out_dir) / "entry.png"
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dst)
    print(f"wrote {dst} ({dst.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
