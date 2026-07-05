"""
check_env.py — validate that required environment variables are present.
Reads the key names from .env.example and checks each against your .env.

Usage:
    python 07-scripts/core/check_env.py
"""

import os
import re
import sys
from pathlib import Path

try:
    from dotenv import load_dotenv
except ImportError:
    sys.exit("Install python-dotenv first:  pip install python-dotenv")

ROOT = Path(__file__).resolve().parents[2]
load_dotenv(dotenv_path=ROOT / ".env")

example = ROOT / ".env.example"
if not example.exists():
    sys.exit("No .env.example found at repo root.")

keys = re.findall(r"^([A-Z][A-Z0-9_]+)=", example.read_text(encoding="utf-8"), re.MULTILINE)

present, missing = [], []
for key in keys:
    (present if os.getenv(key) else missing).append(key)

print(f"Checked {len(keys)} keys from .env.example\n")
for k in present:
    print(f"  [set]     {k}")
for k in missing:
    print(f"  [missing] {k}")

print(f"\n{len(present)} set, {len(missing)} missing.")
if missing:
    print("Missing keys are only a problem if a workflow needs them today.")
