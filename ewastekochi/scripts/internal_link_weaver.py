#!/usr/bin/env python3
"""Adds contextual internal links across all HTML pages. Run from ewastekochi/ root."""
import re, os

LINK_RULES = {
    "DPDP Act 2023": "/compliance/dpdp-act-2023-penalties.html",
    "DPDP Act": "/compliance/dpdp-act-2023-penalties.html",
    "NIST 800-88": "/compliance/nist-800-88-explained.html",
    "DoD 5220.22-M": "/compliance/dod-5220-22m-guide.html",
    "Certificate of Destruction": "/certificate-of-destruction.html",
    "sell phone": "/sell-old-phone-kochi.html",
    "sell your phone": "/sell-old-phone-kochi.html",
    "laptop buyback": "/sell-old-laptop-kochi.html",
    "sell laptop": "/sell-old-laptop-kochi.html",
    "free pickup": "/book-free-pickup.html",
    "hard drive shredding": "/hard-drive-shredding-kochi.html",
    "data destruction": "/data-destruction-kochi.html",
    "ITAD": "/itad-kochi.html",
    "chain of custody": "/compliance/chain-of-custody.html",
}

def add_links(content, current_file):
    for keyword, url in LINK_RULES.items():
        if url in current_file: continue  # Don't self-link
        count = [0]
        def replacer(m):
            if count[0] > 0: return m.group(0)
            count[0] += 1
            return f'<a href="{url}">{m.group(0)}</a>'
        pattern = re.compile(rf'(?<!["'/])\b{re.escape(keyword)}\b(?!["'])(?![^<]*>)', re.IGNORECASE)
        content = pattern.sub(replacer, content)
    return content

def process_all():
    updated = 0
    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d not in ["scripts","css","js","images","__pycache__"]]
        for f in files:
            if not f.endswith(".html"): continue
            path = os.path.join(root, f)
            with open(path,"r",encoding="utf-8") as fh: content = fh.read()
            new = add_links(content, path)
            if new != content:
                with open(path,"w",encoding="utf-8") as fh: fh.write(new)
                print(f"  Linked: {path}")
                updated += 1
    print(f"Updated {updated} files with internal links.")

process_all()
