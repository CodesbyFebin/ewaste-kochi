#!/usr/bin/env python3
"""
EWasteKochi.in — Internal Link Weaver
Adds contextual internal links to all HTML pages.
Smart: Only links first occurrence per page, never links inside existing <a> tags.
Run: python3 internal_link_weaver.py (from project root)
"""

import os
import re

SITE_URL = "https://ewastekochi.in"

# (keyword_pattern, target_url, link_text, max_per_page)
# Lower max_per_page for high-volume terms to avoid over-linking
LINK_RULES = [
    # PRIMARY COMMERCIAL
    (r'\bDPDP Act 2023\b',                 "/compliance/dpdp-act-2023-penalties.html",   "DPDP Act 2023",           2),
    (r'\bDPDP Act\b',                       "/compliance/dpdp-act-2023-penalties.html",   "DPDP Act",                1),
    (r'\bNIST 800-88\b',                    "/compliance/nist-800-88-explained.html",      "NIST 800-88",             2),
    (r'\bNIST SP 800-88\b',                 "/compliance/nist-800-88-explained.html",      "NIST SP 800-88",          1),
    (r'\bDoD 5220\.22-M\b',                 "/compliance/dod-5220-22m-guide.html",         "DoD 5220.22-M",           1),
    (r'\bCertificate of Destruction\b',     "/certificate-of-destruction.html",            "Certificate of Destruction", 2),
    (r'\bchain of custody\b',               "/compliance/chain-of-custody.html",           "chain of custody",        1),
    # SERVICES
    (r'\bCorporate ITAD\b',                 "/itad-kochi.html",                            "Corporate ITAD",          2),
    (r'\bIT asset disposal\b',              "/itad-kochi.html",                            "IT asset disposal",       1),
    (r'\bITAD\b',                           "/itad-kochi.html",                            "ITAD",                    1),
    (r'\bdata destruction\b',               "/data-destruction-kochi.html",                "data destruction",        2),
    (r'\bhard drive shredding\b',           "/hard-drive-shredding-kochi.html",            "hard drive shredding",    2),
    (r'\bsell (?:your |old )?phone\b',      "/sell-old-phone-kochi.html",                  "sell your phone",         1),
    (r'\blaptop buyback\b',                 "/sell-old-laptop-kochi.html",                 "laptop buyback",          2),
    (r'\bsell (?:your |old )?laptop\b',     "/sell-old-laptop-kochi.html",                 "sell your laptop",        1),
    (r'\bfree (?:e-waste )?pickup\b',       "/book-free-pickup-kochi.html",                "free pickup",             1),
    (r'\bbook (?:a )?pickup\b',             "/book-free-pickup-kochi.html",                "book a pickup",           1),
    (r'\boffice clearance\b',               "/office-clearance-kochi.html",                "office clearance",        1),
    # COMPLIANCE PAGES
    (r'\bKSPCB\b',                          "/compliance/kerala-pcb-authorization.html",   "KSPCB",                   2),
    (r'\bKerala PCB\b',                     "/compliance/kerala-pcb-authorization.html",   "Kerala PCB",              1),
    (r'\bverify (?:your |a )?certificate\b',"/compliance/certificate-verification.html",   "verify your certificate", 1),
    # LOCATION PAGES
    (r'\bKakkanad\b',                       "/locations/ewaste-kakkanad.html",             "Kakkanad",                1),
    (r'\bInforpark\b',                      "/locations/ewaste-infopark.html",             "Infopark",                1),
    (r'\bEdappally\b',                      "/locations/ewaste-edappally.html",            "Edappally",               1),
    (r'\bThrippunithura\b',                 "/locations/ewaste-thrippunithura.html",       "Thrippunithura",          1),
    (r'\bVyttila\b',                        "/locations/ewaste-vyttila.html",              "Vyttila",                 1),
]

SKIP_ELEMENTS = ['<a', '<script', '<style', '<head', '<title', '<meta', '<link', 'class="logo"', 'class="nav']

def is_inside_tag(text, pos):
    """Check if position is inside an HTML tag or existing anchor."""
    # Look backwards for unclosed tag
    before = text[:pos]
    last_lt = before.rfind('<')
    last_gt = before.rfind('>')
    return last_lt > last_gt

def add_links_to_html(content, source_path):
    """Apply link rules to HTML content, skipping <head>, <script>, <style>, existing <a> tags."""
    changes = 0
    # Extract body content only (don't touch head)
    body_match = re.search(r'(<body[^>]*>)(.*?)(</body>)', content, re.DOTALL | re.IGNORECASE)
    if not body_match:
        return content, changes

    body_start, body_content, body_end = body_match.groups()
    original_body = body_content

    for pattern, url, link_text, max_count in LINK_RULES:
        # Skip if current page IS the target (don't self-link)
        if source_path.replace("\\", "/").replace("./", "") in url.lstrip("/"):
            continue

        count = 0
        def replace_link(m):
            nonlocal count
            if count >= max_count:
                return m.group(0)
            # Check the surrounding context — don't link inside existing <a> or <script>/<style>
            start = m.start()
            before_snippet = body_content[max(0, start-200):start]
            # Skip if inside <a ...>, <script>, <style>, nav, header
            skip_contexts = ['<a ', '<script', '<style', 'class="logo', 'class="nav', 'class="footer', '<head']
            if any(ctx in before_snippet.split('>')[-1] or ctx in before_snippet for ctx in ['<a ']):
                # More careful check: is there an unclosed <a> before this?
                a_opens = before_snippet.count('<a ')
                a_closes = before_snippet.count('</a>')
                if a_opens > a_closes:
                    return m.group(0)
            count += 1
            return f'<a href="{url}">{m.group(0)}</a>'

        # Apply replacement to body only
        new_body = re.sub(pattern, replace_link, body_content, flags=re.IGNORECASE)
        if new_body != body_content:
            changes += count
        body_content = new_body

    if changes > 0:
        content = content.replace(body_match.group(0), body_start + body_content + body_end)

    return content, changes

SKIP_FILES = ["portal-login", "404", "scripts/"]

def process_all():
    print(f"\n{'='*60}")
    print(f"  EWasteKochi.in — Internal Link Weaver")
    print(f"{'='*60}\n")

    total_files  = 0
    total_links  = 0
    updated_files = 0

    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
        for file in sorted(files):
            if not file.endswith(".html"):
                continue
            path = os.path.join(root, file)
            rel  = path.replace("\\", "/")
            if any(skip in rel for skip in SKIP_FILES):
                continue

            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

            new_content, n_links = add_links_to_html(content, rel)
            total_files += 1

            if n_links > 0:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"  ✓ {rel} — {n_links} link(s) added")
                updated_files += 1
                total_links += n_links

    print(f"\n{'='*60}")
    print(f"✅ DONE")
    print(f"   Files scanned:  {total_files}")
    print(f"   Files updated:  {updated_files}")
    print(f"   Links inserted: {total_links}")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    process_all()
