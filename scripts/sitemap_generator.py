#!/usr/bin/env python3
"""Run from ewastekochi/ root: python scripts/sitemap_generator.py"""
import os
from datetime import datetime

def generate_sitemap(base_url="https://ewastekochi.com"):
    pages = []
    PRIORITY = {
        "index.html": "1.0",
        "e-waste-management-kochi-complete-guide.html": "0.98",
        "itad-complete-guide-kochi.html": "0.98",
        "data-destruction-degaussing-kochi.html": "0.98",
        "iso-27001-certified-data-sanitization-kochi.html": "0.98",
        "corporate-data-security-compliance-kochi.html": "0.98",
        "hard-drive-shredding-destruction-kochi.html": "0.98",
        "gdpr-dpdp-act-compliance-ewaste-kochi.html": "0.98",
        "secure-chain-of-custody-documentation-kochi.html": "0.98",
        "itad-kochi.html": "0.95",
        "data-destruction-kochi.html": "0.95",
        "sell-old-laptop-kochi.html": "0.92",
        "sell-old-phone-kochi.html": "0.92",
        "get-instant-quote.html": "0.9"
    }
    for root, d_list, f_list in os.walk("."):
        d_list[:] = [d for d in d_list if d not in ["scripts", "css", "js", "images", "node_modules", ".git"]]
        for f in f_list:
            if f.endswith(".html"):
                path_raw = os.path.join(root, f)
                rel = os.path.relpath(path_raw, ".").replace("\\", "/")
                url = base_url + "/" + ("" if rel == "index.html" else rel)
                prio = PRIORITY.get(rel, "0.8" if "pillar" in rel or "complete-guide" in rel else ("0.55" if "locations" in rel else "0.75"))
                freq = "weekly" if float(prio) >= 0.9 else "monthly"
                pages.append((url, prio, freq))
    pages.sort(key=lambda x: float(x[1]), reverse=True)
    today = datetime.now().strftime("%Y-%m-%d")
    xml = '''<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'''
    for url, prio, freq in pages:
        xml += f"  <url><loc>{url}</loc><lastmod>{today}</lastmod><changefreq>{freq}</changefreq><priority>{prio}</priority></url>\n"
    xml += "</urlset>"
    with open("sitemap.xml","w") as f: f.write(xml)
    print(f"Generated sitemap.xml — {len(pages)} URLs")

generate_sitemap()
