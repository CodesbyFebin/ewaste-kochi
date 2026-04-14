#!/usr/bin/env python3
"""Regenerate sitemap.xml from all live HTML files + write robots.txt."""
import os, re, glob
from pathlib import Path
from datetime import date

BASE = "/media/hp-ml10/Projects/ewastekochi-production/ewastekochi"
SITE = "https://ewastekochi.com"
TODAY = date.today().isoformat()

EXCLUDE = {"__pycache__", "gitlab_repo", "ewastekochi-production", "node_modules"}

# Priority rules by folder
PRIORITY_MAP = {
    "_root": "1.0",
    "locations": "0.9",
    "data-security": "0.9",
    "itad": "0.9",
    "recycling": "0.8",
    "collection": "0.8",
    "disposal": "0.8",
    "trading": "0.8",
    "buyback": "0.8",
    "services": "0.8",
    "industries": "0.7",
    "comparisons": "0.7",
    "compliance": "0.7",
    "guides": "0.7",
    "blog": "0.7",
    "general-waste": "0.6",
    "proof": "0.6",
}
CHANGEFREQ_MAP = {
    "_root": "daily",
    "blog": "weekly",
}

def get_meta(rel_parts):
    cat = rel_parts[0] if len(rel_parts) > 1 else "_root"
    return (
        PRIORITY_MAP.get(cat, "0.6"),
        CHANGEFREQ_MAP.get(cat, "weekly")
    )

def get_url(fp):
    rel = Path(fp).relative_to(BASE)
    # Remove .html extension for clean URLs
    clean = str(rel).replace(".html", "")
    # Root index.html → just /
    if clean == "index":
        return f"{SITE}/"
    return f"{SITE}/{clean}"

def main():
    # ── Gather all HTML pages ───────────────────────────────────────────────
    all_html = []
    for root, dirs, files in os.walk(BASE):
        dirs[:] = [d for d in dirs if d not in EXCLUDE]
        for name in files:
            if name.endswith(".html"):
                fp = os.path.join(root, name)
                all_html.append(fp)

    print(f"Found {len(all_html)} HTML files")

    # ── Build sitemap XML ───────────────────────────────────────────────────
    urls = []
    seen = set()
    for fp in sorted(all_html):
        url = get_url(fp)
        if url in seen:
            continue
        seen.add(url)
        rel = Path(fp).relative_to(BASE)
        parts = list(rel.parts)
        priority, changefreq = get_meta(parts)
        urls.append((url, priority, changefreq))

    # Sort: homepage first, then by priority desc, then alpha
    urls.sort(key=lambda x: (-float(x[1]), x[0]))

    xml_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
        '        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">',
    ]
    for url, priority, changefreq in urls:
        xml_lines += [
            "  <url>",
            f"    <loc>{url}</loc>",
            f"    <lastmod>{TODAY}</lastmod>",
            f"    <changefreq>{changefreq}</changefreq>",
            f"    <priority>{priority}</priority>",
            "  </url>",
        ]
    xml_lines.append("</urlset>")

    sitemap_path = os.path.join(BASE, "sitemap.xml")
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write("\n".join(xml_lines))
    print(f"✅ sitemap.xml written — {len(urls)} URLs")

    # ── Write robots.txt ────────────────────────────────────────────────────
    robots = f"""# ============================================================
# ROBOTS.TXT — EWaste Kochi | KSPCB Authorised Recycler
# Updated: {TODAY}
# ============================================================

User-agent: *
Allow: /
Disallow: /admin/
Disallow: /cgi-bin/
Disallow: /tmp/
Disallow: /backup/
Disallow: /private/
Disallow: /*.py$
Disallow: /*.log$
Disallow: /*.csv$
Disallow: /*.json$
Crawl-delay: 0.5

# ── Major Search Engines ──────────────────────────────────────

User-agent: Googlebot
Allow: /
Crawl-delay: 0.3

User-agent: Googlebot-Image
Allow: /images/
Allow: /assets/images/

User-agent: Googlebot-News
Allow: /blog/

User-agent: bingbot
Allow: /
Crawl-delay: 0.5

User-agent: Slurp
Allow: /
Crawl-delay: 1

User-agent: DuckDuckBot
Allow: /
Crawl-delay: 0.5

User-agent: Baiduspider
Allow: /
Crawl-delay: 1

User-agent: YandexBot
Allow: /
Crawl-delay: 1

# ── AI + LLM Crawlers (Full Access for Visibility) ───────────

User-agent: GPTBot
Allow: /
Crawl-delay: 0.5

User-agent: Google-Extended
Allow: /
Crawl-delay: 0.5

User-agent: anthropic-ai
Allow: /
Crawl-delay: 0.5

User-agent: Claude-Web
Allow: /
Crawl-delay: 0.5

User-agent: PerplexityBot
Allow: /
Crawl-delay: 0.5

User-agent: CCBot
Allow: /
Crawl-delay: 1

User-agent: Applebot
Allow: /
Crawl-delay: 1

User-agent: cohere-ai
Allow: /
Crawl-delay: 0.5

# ── Social Media Crawlers ─────────────────────────────────────

User-agent: facebookexternalhit
Allow: /

User-agent: LinkedInBot
Allow: /

User-agent: Twitterbot
Allow: /

User-agent: WhatsApp
Allow: /

# ── Sitemaps ──────────────────────────────────────────────────

Sitemap: {SITE}/sitemap.xml

# ── Host ──────────────────────────────────────────────────────

Host: {SITE}
"""
    robots_path = os.path.join(BASE, "robots.txt")
    with open(robots_path, "w", encoding="utf-8") as f:
        f.write(robots)
    print("✅ robots.txt written")

if __name__ == "__main__":
    main()
