#!/usr/bin/env python3
"""
EWaste Kochi — Local SEO H1/H2 Upgrader
Updates h1 and h2 tags on all HTML pages with high local SEO headings.
"""

import os
import re
from pathlib import Path

BASE_DIR = "/media/hp-ml10/Projects/ewastekochi-production/ewastekochi"

# ── Local SEO suffix pools — rotated per category ──────────────────────────────
LOCATION_TAGS = [
    "Kochi", "Ernakulam", "Kakkanad", "Edappally", "Infopark Kochi",
    "Thrippunithura", "Vyttila", "Aluva Ernakulam", "Fort Kochi",
    "SmartCity Kochi", "Kalamassery", "Maradu", "Palarivattom",
]

# Category-aware H1/H2 templates
# Keys match the parent folder name
CATEGORY_H1 = {
    "data-security": [
        "Certified NIST Data Destruction {location} — #{rank} Rated 2026",
        "Secure IT Asset Disposal & Data Wiping {location} | DPDP Compliant",
        "Hard Drive Shredding & ITAD Services {location} | KSPCB Authorised",
        "100% Data-Safe E-Waste Destruction {location} | Certificate of Destruction",
    ],
    "recycling": [
        "Certified E-Waste Recycling {location} — Free Corporate Pickup 2026",
        "Zero-Landfill Electronics Recycling Hub {location} | KSPCB Approved",
        "Battery & Device Recycling Centre {location} | EPR Compliant 2026",
        "Professional E-Waste Recycling {location} — 5,000+ Pickups Completed",
    ],
    "collection": [
        "Free E-Waste Pickup {location} — Same-Day Corporate Collection 2026",
        "Scheduled E-Waste Collection {location} | GPS-Tracked Chain of Custody",
        "Bulk Electronics Pickup & Disposal {location} | KSPCB Authorised",
        "Corporate E-Waste Pickup {location} — Free for 10+ Devices",
    ],
    "disposal": [
        "Safe E-Waste Disposal {location} | KSPCB Zero-Landfill Certified",
        "Secure Electronic Waste Disposal Hub {location} — DPDP 2023 Compliant",
        "Hazardous E-Waste Disposal {location} — Mercury & Lead Safe Handling",
        "Certified Device Disposal & Data Sanitisation {location} | 2026",
    ],
    "trading": [
        "Sell Old Electronics {location} — Best Price Guaranteed 2026",
        "IT Asset Buyback & Resale Centre {location} | Instant Cash Offer",
        "Corporate Laptop & Device Buyback {location} — Secure & Certified",
        "Scrap Electronics Buyer {location} | KSPCB Authorised — Best Rates",
    ],
    "general-waste": [
        "E-Waste Management {location} — Certified Recycling Hub 2026",
        "Electronic Waste Solutions {location} | Free Pickup & Zero-Landfill",
        "Household & Corporate E-Waste Hub {location} | KSPCB Approved",
        "Sustainable Waste Disposal {location} — Data-Secure & Eco-Certified",
    ],
    "blog": [
        "E-Waste Insights: {topic} | Expert Guide {location} 2026",
        "{topic} — Complete Guide for {location} Businesses & Residents",
        "Professional Analysis: {topic} | EWaste Kochi {location}",
    ],
    "locations": [
        "E-Waste Recycling {location} — Doorstep Pickup Available",
        "Certified E-Waste Hub Serving {location} | KSPCB Authorised",
        "Free E-Waste Collection {location} — Book Online Today",
    ],
    "services": [
        "Professional {topic} Services {location} | KSPCB Certified 2026",
        "Enterprise {topic} {location} — Audit-Ready & DPDP Compliant",
        "Certified {topic} Provider {location} | Kerala's #1 ITAD Hub",
    ],
    "guides": [
        "Complete Guide: {topic} in {location} | Expert 2026 Edition",
        "How to {topic} in {location} — Step-by-Step Expert Guide",
        "The Definitive {topic} Playbook for {location} Enterprises",
    ],
    "buyback": [
        "Sell Your {topic} {location} — Instant Quote & Free Pickup",
        "Best Laptop Buyback Rates {location} | Certified & Secure",
        "{topic} Buyback Programme {location} | Same-Day Cash Payment",
    ],
    "itad": [
        "IT Asset Disposition (ITAD) {location} — ISO & NIST Certified",
        "Enterprise ITAD Services {location} | DPDP Act 2023 Compliant",
        "Certified ITAD Provider {location} — Certificate of Destruction Every Job",
    ],
    "industries": [
        "{topic} Industry E-Waste Solutions {location} | KSPCB Authorised",
        "Sector-Specific E-Waste Management {location} — Compliance Guaranteed",
        "Corporate IT Decommissioning for {topic} Sector {location}",
    ],
    "comparisons": [
        "{topic} Comparison Guide {location} | Expert Analysis 2026",
        "Certified vs Uncertified E-Waste Disposal {location} — Full Comparison",
    ],
    "compliance": [
        "E-Waste Compliance {location} | DPDP Act 2023 & KSPCB Rules",
        "{topic} Regulatory Compliance {location} — Expert Legal Guide 2026",
    ],
    "proof": [
        "Verified Certifications & Case Studies | EWaste Kochi {location}",
        "Proof of Compliance {location} | KSPCB, NIST & ISO Documentation",
    ],
    "_root": [
        "Certified E-Waste Recycling & Data Destruction {location} | 2026",
        "KSPCB Authorised E-Waste Hub {location} — Free Pickup & Data-Safe",
        "Kerala's #1 E-Waste Recycler {location} | NIST & DPDP Compliant",
    ],
}

CATEGORY_H2_SETS = {
    "data-security": [
        "Why Certified Data Destruction Matters in {location}",
        "NIST 800-88 Compliant Wiping: The Gold Standard for {location} Businesses",
        "DPDP Act 2023 Compliance Made Simple for {location} Enterprises",
        "How Our Hard Drive Shredding Facility in {location} Works",
        "Certificate of Destruction — Your Legal Shield in {location}",
    ],
    "recycling": [
        "How E-Waste Recycling Works at Our {location} Facility",
        "Zero-Landfill Promise: What It Means for {location}",
        "KSPCB-Authorised Recycling Chain in {location} Explained",
        "Precious Metal Recovery From Your Old Devices in {location}",
        "EPR Compliance Through Certified Recycling in {location}",
    ],
    "collection": [
        "How to Book a Free E-Waste Pickup in {location}",
        "Chain-of-Custody Documentation for {location} Corporate Clients",
        "GPS-Tracked Collection Vehicles in {location} — How It Works",
        "What Devices We Collect From {location} Households & Offices",
        "Same-Day Bulk Pickup Service for {location} IT Parks",
    ],
    "disposal": [
        "Hazardous Material Handling at Our {location} Facility",
        "KSPCB-Approved Disposal Methods for {location} Businesses",
        "Secure Chain-of-Custody From {location} to Disposal",
        "Why Landfill-Free Disposal Matters for {location}'s Environment",
        "Certificate of Safe Disposal — Issued for Every {location} Client",
    ],
    "trading": [
        "How We Calculate Buyback Prices for {location} Clients",
        "Devices We Buy From {location}: Full Category Breakdown",
        "Instant Cash Payment for IT Assets in {location}",
        "How Secure Is Selling Old Devices Through Us in {location}?",
        "Corporate Fleet Buyback Programme in {location} Explained",
    ],
    "general-waste": [
        "E-Waste Regulations You Must Know in {location}",
        "The Hidden Environmental Cost of Improper Disposal in {location}",
        "How Small Businesses in {location} Can Manage E-Waste",
        "Top 5 Most Recycled Electronics in {location} in 2026",
        "From Collection to Recycling: The Full Journey in {location}",
    ],
    "_default": [
        "Expert E-Waste Solutions Serving All of {location}",
        "Why {location} Trusts EWaste Kochi — 4.9★ Rating",
        "Our KSPCB-Authorised Process for {location} Clients",
        "Free Pickup & Data-Safe Recycling in {location}",
        "Schedule Your {location} E-Waste Collection Today",
    ],
}


def get_category(file_path: str) -> str:
    rel = Path(file_path).relative_to(BASE_DIR)
    if len(rel.parts) == 1:
        return "_root"
    return rel.parts[0]

def get_location(file_path: str, idx: int) -> str:
    return LOCATION_TAGS[idx % len(LOCATION_TAGS)]

def get_h1_templates(cat: str) -> list:
    return CATEGORY_H1.get(cat, CATEGORY_H1["_root"])

def get_h2_set(cat: str) -> list:
    return CATEGORY_H2_SETS.get(cat, CATEGORY_H2_SETS["_default"])

def extract_topic_from_path(file_path: str) -> str:
    stem = Path(file_path).stem
    return stem.replace("-", " ").replace("_", " ").title()

def build_h1(file_path: str, cat: str, idx: int) -> str:
    templates = get_h1_templates(cat)
    tpl = templates[idx % len(templates)]
    loc = get_location(file_path, idx)
    topic = extract_topic_from_path(file_path)
    return tpl.format(location=loc, topic=topic, rank=(idx % 3) + 1)

def build_h2s(file_path: str, cat: str, idx: int) -> list:
    h2_pool = get_h2_set(cat)
    loc = get_location(file_path, idx + 1)
    result = []
    for i, tpl in enumerate(h2_pool):
        result.append(tpl.format(location=loc, topic=extract_topic_from_path(file_path)))
    return result

def upgrade_headers(file_path: str, idx: int) -> bool:
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            html = f.read()
    except Exception:
        return False

    if len(html) < 500 or "<html" not in html.lower():
        return False

    cat = get_category(file_path)
    new_h1 = build_h1(file_path, cat, idx)
    new_h2s = build_h2s(file_path, cat, idx)

    # Replace first <h1>...</h1>
    h1_pattern = re.compile(r'(<h1[^>]*>)(.*?)(</h1>)', re.IGNORECASE | re.DOTALL)
    h1_match = h1_pattern.search(html)
    if h1_match:
        html = h1_pattern.sub(
            f'\\1{new_h1}\\3',
            html,
            count=1
        )
    else:
        # Inject after first <body> tag
        body_match = re.search(r'<body[^>]*>', html, re.IGNORECASE)
        if body_match:
            ins = body_match.end()
            html = html[:ins] + f'\n<h1 style="color:var(--white,#E8F2EA);font-family:\'Bebas Neue\',cursive;">{new_h1}</h1>\n' + html[ins:]

    # Replace ALL <h2>...</h2> tags with our SEO-rich set
    h2_pattern = re.compile(r'(<h2[^>]*>)(.*?)(</h2>)', re.IGNORECASE | re.DOTALL)
    h2_matches = list(h2_pattern.finditer(html))
    
    if h2_matches:
        # Cycle through our new h2s for each existing h2
        def h2_replacer(m):
            nonlocal h2_idx
            new_text = new_h2s[h2_idx % len(new_h2s)]
            h2_idx += 1
            return m.group(1) + new_text + m.group(3)
        h2_idx = 0
        html = h2_pattern.sub(h2_replacer, html)
    
    # Also update the <title> tag to include local SEO
    title_match = re.search(r'<title>(.*?)</title>', html, re.IGNORECASE)
    if title_match:
        old_title = title_match.group(1)
        # Only update if it doesn't already have a Kochi reference
        if "Kochi" not in old_title and "Ernakulam" not in old_title:
            loc = get_location(file_path, idx)
            new_title = f"{extract_topic_from_path(file_path)} {loc} | #1 Certified E-Waste Hub 2026"
            html = html.replace(title_match.group(0), f'<title>{new_title}</title>', 1)

    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html)
        return True
    except Exception:
        return False

def main():
    EXCLUDE = {"__pycache__", "gitlab_repo", "ewastekochi-production"}
    all_files = []
    for root, dirs, files in os.walk(BASE_DIR):
        dirs[:] = [d for d in dirs if d not in EXCLUDE]
        for name in files:
            if name.endswith(".html"):
                all_files.append(os.path.join(root, name))

    total = len(all_files)
    ok = 0
    print(f"🚀 Upgrading H1/H2 on {total} pages with local SEO...\n")

    for idx, fp in enumerate(sorted(all_files)):
        result = upgrade_headers(fp, idx)
        if result:
            ok += 1
            if ok % 100 == 0:
                print(f"  ✓ {ok}/{total} processed...")

    print(f"\n{'='*60}")
    print(f"✅ H1/H2 upgraded: {ok} / {total} pages")
    print("🏆 Local SEO H1/H2 injection complete!")

if __name__ == "__main__":
    main()
