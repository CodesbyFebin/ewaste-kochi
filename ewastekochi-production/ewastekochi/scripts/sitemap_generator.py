#!/usr/bin/env python3
"""
EWasteKochi.in — XML Sitemap Generator
Crawls all .html files in the project directory and generates sitemap.xml
Run: python3 sitemap_generator.py (from project root)
"""

import os
from datetime import datetime

SITE_URL    = "https://ewastekochi.in"
OUTPUT_FILE = "sitemap.xml"

# Priority and changefreq rules by path pattern
PRIORITY_RULES = [
    ("index.html",            "1.0",  "weekly"),
    ("sell-old-phone",        "0.95", "weekly"),
    ("sell-old-laptop",       "0.95", "weekly"),
    ("itad-kochi",            "0.92", "monthly"),
    ("data-destruction",      "0.92", "monthly"),
    ("hard-drive-shredding",  "0.90", "monthly"),
    ("book-free-pickup",      "0.90", "weekly"),
    ("get-instant-quote",     "0.88", "weekly"),
    ("locations/ewaste-kakkanad",    "0.88", "monthly"),
    ("locations/ewaste-infopark",    "0.88", "monthly"),
    ("locations/ewaste-edappally",   "0.85", "monthly"),
    ("locations/ewaste-thrippunithura", "0.85", "monthly"),
    ("locations/",            "0.80", "monthly"),
    ("compliance/dpdp",       "0.82", "monthly"),
    ("compliance/nist",       "0.80", "monthly"),
    ("compliance/",           "0.75", "monthly"),
    ("industries/",           "0.75", "monthly"),
    ("comparisons/",          "0.72", "monthly"),
    ("blog/",                 "0.70", "weekly"),
    ("about",                 "0.65", "yearly"),
    ("contact",               "0.70", "monthly"),
    ("faq",                   "0.68", "monthly"),
    ("privacy-policy",        "0.30", "yearly"),
    ("terms",                 "0.30", "yearly"),
    ("refund",                "0.30", "yearly"),
]

SKIP_PATTERNS = [
    "scripts/", ".htaccess", "robots.txt",
    "404.html", "portal-login", "__pycache__"
]

def get_priority(path):
    path_norm = path.replace("\\", "/")
    for pattern, priority, changefreq in PRIORITY_RULES:
        if pattern in path_norm:
            return priority, changefreq
    return "0.60", "monthly"

def generate_sitemap():
    pages = []
    today = datetime.now().strftime("%Y-%m-%d")

    for root, dirs, files in os.walk("."):
        # Skip hidden dirs and scripts
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'scripts' and d != '__pycache__']
        for file in sorted(files):
            if not file.endswith(".html"):
                continue
            rel_path = os.path.relpath(os.path.join(root, file), ".").replace("\\", "/")
            if rel_path.startswith("./"):
                rel_path = rel_path[2:]
            if any(skip in rel_path for skip in SKIP_PATTERNS):
                continue
            if rel_path == "index.html":
                url = f"{SITE_URL}/"
            else:
                url = f"{SITE_URL}/{rel_path}"
            priority, changefreq = get_priority(rel_path)
            pages.append((url, today, changefreq, priority))

    # Sort by priority descending
    pages.sort(key=lambda x: float(x[3]), reverse=True)

    # Build XML
    xml_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
        '        xmlns:xhtml="http://www.w3.org/1999/xhtml">',
        f'  <!-- Generated: {datetime.now().isoformat()} — {len(pages)} URLs -->',
        f'  <!-- Site: {SITE_URL} -->',
        '',
    ]

    for url, lastmod, changefreq, priority in pages:
        xml_lines += [
            '  <url>',
            f'    <loc>{url}</loc>',
            f'    <lastmod>{lastmod}</lastmod>',
            f'    <changefreq>{changefreq}</changefreq>',
            f'    <priority>{priority}</priority>',
            '  </url>',
        ]

    xml_lines.append('</urlset>')
    sitemap_content = "\n".join(xml_lines)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(sitemap_content)

    print(f"✅ sitemap.xml generated — {len(pages)} URLs")
    print(f"   Highest priority: {pages[0][0] if pages else 'none'}")
    print(f"\n📋 NEXT: Submit to Google Search Console:")
    print(f"   {SITE_URL}/sitemap.xml")
    print(f"   Also submit to Bing Webmaster Tools.")

if __name__ == "__main__":
    generate_sitemap()
