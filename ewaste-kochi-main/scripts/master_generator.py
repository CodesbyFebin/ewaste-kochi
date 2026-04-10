#!/usr/bin/env python3
"""
scripts/master_generator.py

Wrapper to run the legacy master_generator (from the ewastekochi folder)
and then ensure JS data modules exist (by invoking master_generator_write_js.py).

This avoids modifying the legacy generator while producing the required
src/data/*.js modules that the Astro project consumes.

Run: python3 scripts/master_generator.py
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEGACY = ROOT.parent / "ewastekochi" / "master_generator.py"
WRITER = ROOT / "master_generator_write_js.py"

# If legacy generator exists, run it in its directory so any relative
# file outputs still land where they expect.
if LEGACY.exists():
    print(f"Running legacy generator: {LEGACY}")
    try:
        subprocess.run([sys.executable, str(LEGACY)], check=True)
    except subprocess.CalledProcessError as e:
        print("Legacy generator returned non-zero exit code:", e)
        # continue to attempt JS writer anyway
else:
    print("Legacy generator not found at:", LEGACY)

# Run the JS writer to convert or emit src/data/*.js
if WRITER.exists():
    print(f"Running JS writer: {WRITER}")
    try:
        subprocess.run([sys.executable, str(WRITER)], check=True)
    except subprocess.CalledProcessError as e:
        print("JS writer returned non-zero exit code:", e)
        sys.exit(e.returncode)
else:
    print("JS writer not found at:", WRITER)
    sys.exit(1)

print("Done. src/data/*.js should now be present or updated.")
