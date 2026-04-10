#!/usr/bin/env python3
"""
scripts/master_generator_write_js.py

Wrapper utility to (1) optionally run your existing master_generator.py and
(2) emit canonical JS data modules under src/data/*.js for Astro.

Behavior:
- If scripts/master_generator.py exists, it will be executed first (so your
  existing generator can produce CSV/JSON artifacts it already creates).
- The script then looks for source data in these places (in order):
  - src/data/*.js (if already present, they will be re-exported as-is)
  - src/data/*.json or src/data/*.csv
  - ../ewastekochi/*.csv or ../ewastekochi/*.json (legacy source folder)
- It will create/update: src/data/locations.js, services.js, industries.js,
  compliance.js, trading.js (whichever it can derive). Missing silos are
  emitted as empty arrays so imports don't fail.

Run: python scripts/master_generator_write_js.py
"""

import subprocess
import json
from pathlib import Path
import csv
import sys
import re

ROOT = Path(__file__).resolve().parents[1]
SRC_DATA = ROOT / "src" / "data"
LEGACY_DIR = ROOT.parent / "ewastekochi"

SRC_DATA.mkdir(parents=True, exist_ok=True)

SILOS = ["locations", "services", "industries", "compliance", "trading"]


def run_master_generator_if_present():
    mg = Path(__file__).resolve().parents[1] / "scripts" / "master_generator.py"
    if mg.exists():
        print(f"Running existing generator: {mg}")
        try:
            subprocess.run([sys.executable, str(mg)], check=True)
        except subprocess.CalledProcessError as e:
            print("master_generator.py returned non-zero exit code:", e)
    else:
        print("No master_generator.py found; skipping run.")


def read_js_array(path: Path):
    # Very small parser: look for `export const NAME = [ ... ];` and eval the JSON-like content
    text = path.read_text(encoding='utf-8')
    m = re.search(r"export\s+const\s+([a-zA-Z0-9_]+)\s*=\s*(\[.*\])", text, flags=re.S)
    if not m:
        return None
    arr_text = m.group(2)
    # Replace single quotes with double quotes for JSON parsing, naive but practical
    json_like = arr_text.replace("'", '"')
    try:
        data = json.loads(json_like)
        return data
    except Exception:
        # fallback: try to safely convert using a regex to quote keys
        try:
            # naive: wrap unquoted keys (not perfect)
            fixed = re.sub(r"(\w+)\s*:", r'"\1":', arr_text)
            fixed = fixed.replace("'", '"')
            data = json.loads(fixed)
            return data
        except Exception as e:
            print(f"Failed to parse JS array at {path}: {e}")
            return None


def read_csv(path: Path):
    rows = []
    with path.open(newline='') as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append({k: v for k, v in r.items() if v is not None})
    return rows


def write_js(name: str, array):
    out = SRC_DATA / f"{name}.js"
    with out.open("w", encoding="utf-8") as f:
        f.write(f"export const {name} = [\n")
        for item in array:
            # dump ASCII-safe JSON (but keep unicode)
            js = json.dumps(item, ensure_ascii=False)
            f.write(f"  {js},\n")
        f.write("];\n")
    print(f"Wrote {out}")


def gather_from_src_js(name: str):
    p = SRC_DATA / f"{name}.js"
    if p.exists():
        data = read_js_array(p)
        if data is not None:
            return data
    return None


def gather_from_csv_or_json(name: str):
    # try: src/data/name.json, src/data/name.csv
    j = SRC_DATA / f"{name}.json"
    if j.exists():
        try:
            return json.loads(j.read_text(encoding='utf-8'))
        except Exception as e:
            print(f"Failed to parse {j}: {e}")
    c = SRC_DATA / f"{name}.csv"
    if c.exists():
        try:
            return read_csv(c)
        except Exception as e:
            print(f"Failed to read CSV {c}: {e}")
    # legacy dir
    j2 = LEGACY_DIR / f"{name}.json"
    if j2.exists():
        try:
            return json.loads(j2.read_text(encoding='utf-8'))
        except Exception as e:
            print(f"Failed to parse {j2}: {e}")
    c2 = LEGACY_DIR / f"{name}.csv"
    if c2.exists():
        try:
            return read_csv(c2)
        except Exception as e:
            print(f"Failed to read CSV {c2}: {e}")
    return None


def main():
    # Step 1: attempt to run existing master generator (optional)
    run_master_generator_if_present()

    # Step 2: for each silo, try to gather existing data and write a canonical JS file
    for silo in SILOS:
        data = gather_from_src_js(silo)
        if data is not None:
            print(f"Using existing src/data/{silo}.js")
            write_js(silo, data)
            continue

        data = gather_from_csv_or_json(silo)
        if data is not None:
            print(f"Converting {silo} from CSV/JSON to JS module")
            write_js(silo, data)
            continue

        # fallback: try to extract from other likely files (services.js exists in src/data)
        # If nothing found, emit an empty array
        print(f"No source found for {silo}; emitting empty array.")
        write_js(silo, [])

    print("Done. You can now run: npm run dev")


if __name__ == '__main__':
    main()
