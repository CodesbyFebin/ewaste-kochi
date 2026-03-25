#!/usr/bin/env python3
"""
EWasteKochi.in — Schema Injector
Injects JSON-LD LocalBusiness + BreadcrumbList schema into pages that don't yet have it.
Smart: Detects existing schema, doesn't double-inject. Generates page-specific breadcrumbs.
Run: python3 schema_injector.py (from project root)
"""

import os
import json
import re

SITE_URL  = "https://ewastekochi.in"
SITE_NAME = "EWasteKochi"
PHONE     = "+91-XXXXXXXXXX"
EMAIL     = "info@ewastekochi.in"

BASE_SCHEMA = {
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "@id": f"{SITE_URL}/#business",
    "name": SITE_NAME,
    "description": "Kerala's #1 certified ITAD and e-waste recycling facility. NIST 800-88 data destruction, laptop buyback, free pickup. KSPCB Authorized. DPDP Act 2023 compliant.",
    "url": SITE_URL,
    "telephone": PHONE,
    "email": EMAIL,
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "710A Hill Palace Rd, East Fort Gate, Kannankulangara",
        "addressLocality": "Thrippunithura",
        "addressRegion": "Kerala",
        "postalCode": "682301",
        "addressCountry": "IN"
    },
    "geo": {
        "@type": "GeoCoordinates",
        "latitude": 9.9390,
        "longitude": 76.3590
    },
    "openingHoursSpecification": [
        {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"], "opens": "08:00", "closes": "20:00"},
        {"@type": "OpeningHoursSpecification", "dayOfWeek": "Sunday", "opens": "10:00", "closes": "16:00"}
    ],
    "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.9", "reviewCount": "243"},
    "priceRange": "₹",
    "areaServed": ["Kochi", "Ernakulam", "Kakkanad", "Thrippunithura", "Edappally", "Vyttila", "Aluva", "Kerala"]
}

def build_breadcrumb(rel_path):
    """Build BreadcrumbList schema from file path."""
    parts = rel_path.replace("\\", "/").split("/")
    items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE_URL}]
    pos = 2

    path_map = {
        "locations":   "Service Locations",
        "blog":        "Blog",
        "compliance":  "Compliance",
        "industries":  "Industries",
        "comparisons": "Comparisons",
    }

    # Add intermediate breadcrumbs for subdirectory pages
    if len(parts) > 1:
        folder = parts[0]
        if folder in path_map:
            items.append({
                "@type": "ListItem",
                "position": pos,
                "name": path_map[folder],
                "item": f"{SITE_URL}/{folder}/"
            })
            pos += 1

    # Add final page
    if rel_path != "index.html":
        # Try to derive a human name from the filename
        filename = parts[-1].replace(".html", "").replace("-", " ").title()
        items.append({
            "@type": "ListItem",
            "position": pos,
            "name": filename,
            "item": f"{SITE_URL}/{rel_path}"
        })

    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": items
    }

SKIP_FILES = ["portal-login", "scripts/", "__pycache__"]

def inject_schema(path, rel_path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Skip if LocalBusiness schema already present
    if '"@type": "LocalBusiness"' in content or '"@type":"LocalBusiness"' in content:
        return False, "already has LocalBusiness schema"

    # Skip if no </head> found
    if "</head>" not in content:
        return False, "no </head> found"

    schema_objects = [BASE_SCHEMA, build_breadcrumb(rel_path)]
    schema_tag = f'<script type="application/ld+json">\n{json.dumps(schema_objects, indent=2, ensure_ascii=False)}\n</script>'
    new_content = content.replace("</head>", f"{schema_tag}\n</head>", 1)

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)

    return True, "injected"

def process_all():
    print(f"\n{'='*60}")
    print(f"  EWasteKochi.in — Schema Injector")
    print(f"{'='*60}\n")

    injected  = 0
    skipped   = 0
    total     = 0

    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
        for file in sorted(files):
            if not file.endswith(".html"):
                continue
            path = os.path.join(root, file)
            rel  = os.path.relpath(path, ".").replace("\\", "/")
            if any(skip in rel for skip in SKIP_FILES):
                continue

            total += 1
            ok, reason = inject_schema(path, rel)
            if ok:
                print(f"  ✓ Schema injected → {rel}")
                injected += 1
            else:
                skipped += 1

    print(f"\n{'='*60}")
    print(f"✅ DONE")
    print(f"   Total files:   {total}")
    print(f"   Schema added:  {injected}")
    print(f"   Already had:   {skipped}")
    print(f"\n📋 Validate with: https://search.google.com/test/rich-results")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    process_all()
