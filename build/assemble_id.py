#!/usr/bin/env python3
"""Optional assembler: rebuild Indonesia playground build.py from the Japan shell.

The checked-in `build.py` is the source of truth. Run this only if you need to
re-import layout/CSS from the Japan playground, then re-apply Indonesia content
via `python build/patch_build.py`.
"""
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent
JP = Path(r"C:\Users\91638\Downloads\JP-Playground\JP-Playground\build\build.py")

if not JP.exists():
    raise SystemExit(f"Japan build.py not found: {JP}")

shutil.copyfile(JP, ROOT / "build.py")
print(f"copied {JP} -> {ROOT / 'build.py'}")
print("Next: python build/patch_build.py && python build/build.py")
