#!/usr/bin/env python3
"""
legacy/master_generator_emit_js.py

Safely import the legacy master_generator.py as a module (without re-running
its heavy generation flow) and attempt to extract the in-memory lists
(LOCATIONS, SERVICES, INDUSTRIES, INTENT_PAGES, etc.) to produce
src/data/*.js files for Astro.

This is non-intrusive: it imports the legacy generator as a module and
reads top-level variables. If the legacy script executes heavy code at
import time, this may run that code — test carefully.

Run: python3 ewastekochi/master_generator_emit_js.py
"""
from pathlib import Path
import importlib.util
import sys
import json

LEGACY = Path(__file__).resolve().parents[1] / "master_generator.py"
ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "ewaste-kochi-main" / "src" / "data"
OUT.mkdir(parents=True, exist_ok=True)

if not LEGACY.exists():
    print("Legacy master_generator.py not found at", LEGACY)
    sys.exit(1)

spec = importlib.util.spec_from_file_location("legacy_master", str(LEGACY))
mod = importlib.util.module_from_spec(spec)
try:
    spec.loader.exec_module(mod)
except Exception as e:
    print("Importing legacy generator raised:", e)
    print("Proceeding may fail if generator executed heavy tasks on import.")

# Helper to write JS
def write_js(name, data):
    out = OUT / f"{name}.js"
    with out.open('w', encoding='utf-8') as f:
        f.write(f"export const {name} = ")
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write(";\n")
    print("Wrote", out)

# Try to extract lists by common names
mappings = {
    'locations': ['LOCATIONS', 'locations', 'Locations'],
    'services': ['SERVICES', 'services', 'Services'],
    'industries': ['INDUSTRIES', 'industries', 'Industries'],
    'compliance': ['COMPLIANCE', 'compliance'],
    'trading': ['TRADING', 'trading'],
}

for name, candidates in mappings.items():
    found = None
    for c in candidates:
        if hasattr(mod, c):
            found = getattr(mod, c)
            break
    if found is None:
        print(f"No variable found for silo {name}; emitting empty array.")
        write_js(name, [])
        continue
    # Normalize data: if LOCATIONS is tuples, convert to dicts
    sample = found[0] if isinstance(found, (list, tuple)) and len(found) > 0 else None
    if sample is None:
        write_js(name, [])
        continue
    # Heuristic conversions
    out_list = []
    if name == 'locations' and isinstance(sample, (list, tuple)):
        # LOCATIONS defined as list of tuples (slug, displayName, lat, lng)
        for item in found:
            try:
                slug = item[0]
                display = item[1] if len(item) > 1 else slug
                lat = item[2] if len(item) > 2 else None
                lng = item[3] if len(item) > 3 else None
                out_list.append({
                    'slug': slug,
                    'name': display,
                    'lat': lat,
                    'lng': lng
                })
            except Exception:
                continue
    elif name == 'services' and isinstance(sample, str):
        for s in found:
            out_list.append({'slug': s, 'name': s.replace('-', ' ').title()})
    elif isinstance(found, list) and isinstance(sample, (dict,)):
        out_list = found
    else:
        # fallback: attempt to coerce each item into a dict
        for item in found:
            if isinstance(item, dict):
                out_list.append(item)
            elif isinstance(item, (list, tuple)):
                # try first two elements
                if len(item) >= 2:
                    out_list.append({'slug': item[0], 'name': item[1]})
            else:
                out_list.append({'value': item})

    write_js(name, out_list)

print('Done writing JS modules.')
