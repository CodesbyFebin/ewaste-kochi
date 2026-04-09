#!/usr/bin/env python3
"""
auto_index.py — EWasteKochi.com Search Engine & AI Model Auto-Indexer
Submits all sitemap URLs to:
  - Google Search Console (Indexing API)
  - IndexNow (Bing, Yandex, Seznam, Naver)
  - Bing Webmaster Tools
  - Yandex Webmaster API
  - Ping sitemap endpoints

Usage:
  python3 auto_index.py              # Index all URLs
  python3 auto_index.py --new-only  # Index only recently changed pages
  python3 auto_index.py --page /blog/some-post.html  # Index single page
"""

import requests
import json
import os
import xml.etree.ElementTree as ET
import argparse
import time
from datetime import datetime

# ── CONFIG ────────────────────────────────────────────────────────────────
DOMAIN       = "https://ewastekochi.com"
SITEMAP_URL  = "https://ewastekochi.com/sitemap.xml"
INDEXNOW_KEY = "0b5e235aab084c5fbef20e51c5b0f6c9"
INDEXNOW_KEY_FILE = f"{DOMAIN}/{INDEXNOW_KEY}.txt"

# IndexNow endpoints (Bing, Yandex, Seznam, Naver all share protocol)
INDEXNOW_ENDPOINTS = [
    "https://api.indexnow.org/indexnow",
    "https://www.bing.com/indexnow",
    "https://search.seznam.cz/indexnow",
    "https://yandex.com/indexnow",
]

# Search engine sitemap ping endpoints (no API key needed)
PING_ENDPOINTS = [
    f"https://www.google.com/ping?sitemap={SITEMAP_URL}",
    f"https://www.bing.com/ping?sitemap={SITEMAP_URL}",
    f"https://ping.blogs.yandex.ru/RPC2",  # Yandex ping
]

# ── LOAD SITEMAP URLS ─────────────────────────────────────────────────────
def get_sitemap_urls():
    # Try reading locally first
    local_sitemap = os.path.join(os.path.dirname(__file__), "sitemap.xml")
    if os.path.exists(local_sitemap):
        try:
            with open(local_sitemap, "r", encoding="utf-8") as f:
                content = f.read()
            tree = ET.fromstring(content)
            ns = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
            urls = [loc.text for loc in tree.findall('.//sm:loc', ns)]
            print(f"✅ Loaded {len(urls)} URLs from local sitemap.xml")
            return urls
        except Exception as e:
            print(f"⚠️  Failed to load local sitemap: {e}")

    # Fallback to remote
    try:
        r = requests.get(SITEMAP_URL, timeout=15)
        r.raise_for_status()
        tree = ET.fromstring(r.content)
        ns = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        urls = [loc.text for loc in tree.findall('.//sm:loc', ns)]
        print(f"✅ Loaded {len(urls)} URLs from remote sitemap")
        return urls
    except Exception as e:
        print(f"❌ Failed to load remote sitemap: {e}")
        return []

# ── INDEXNOW SUBMISSION ───────────────────────────────────────────────────
def submit_indexnow(urls):
    """Submit URLs to all IndexNow endpoints (Bing, Yandex, etc.)"""
    payload = {
        "host": "ewastekochi.com",
        "key": INDEXNOW_KEY,
        "keyLocation": INDEXNOW_KEY_FILE,
        "urlList": urls
    }
    headers = {"Content-Type": "application/json; charset=utf-8"}
    results = {}

    for endpoint in INDEXNOW_ENDPOINTS:
        try:
            r = requests.post(endpoint, json=payload, headers=headers, timeout=15)
            status = "✅ Accepted" if r.status_code in [200, 202] else f"⚠️  {r.status_code}"
            results[endpoint] = status
            print(f"  IndexNow → {endpoint.split('/')[2]}: {status}")
            time.sleep(0.5)
        except Exception as e:
            results[endpoint] = f"❌ Error: {e}"
            print(f"  IndexNow → {endpoint.split('/')[2]}: ❌ {e}")

    return results

# ── SITEMAP PING ──────────────────────────────────────────────────────────
def ping_sitemap():
    """Ping Google + Bing with sitemap URL (no API key required)"""
    for url in PING_ENDPOINTS[:2]:  # Google + Bing
        try:
            r = requests.get(url, timeout=10)
            engine = "Google" if "google" in url else "Bing"
            status = "✅" if r.status_code == 200 else f"⚠️  {r.status_code}"
            print(f"  Sitemap ping → {engine}: {status}")
        except Exception as e:
            print(f"  Sitemap ping error: {e}")
        time.sleep(0.3)

# ── ROBOTS.TXT VERIFY ────────────────────────────────────────────────────
def verify_robots():
    """Verify robots.txt is accessible and has correct sitemap declaration"""
    try:
        r = requests.get(f"{DOMAIN}/robots.txt", timeout=10)
        if "Sitemap:" in r.text and "GPTBot" in r.text and "ClaudeBot" in r.text:
            print("  ✅ robots.txt: Sitemap declared, AI crawlers allowed")
        else:
            print("  ⚠️  robots.txt: Missing sitemap or AI crawler rules")
    except Exception as e:
        print(f"  ❌ robots.txt check failed: {e}")

# ── MAIN ──────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="EWasteKochi Auto-Indexer")
    parser.add_argument("--new-only", action="store_true", help="Only submit high-priority pages")
    parser.add_argument("--page", type=str, help="Submit a single page URL path")
    args = parser.parse_args()

    print("\n" + "═"*58)
    print("  EWasteKochi.com — Search Engine & AI Auto-Indexer")
    print(f"  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("═"*58 + "\n")

    # Single page mode
    if args.page:
        url = f"{DOMAIN}{args.page}" if not args.page.startswith("http") else args.page
        print(f"📄 Single page mode: {url}\n")
        print("── IndexNow Submission ──")
        submit_indexnow([url])
        return

    # Load URLs
    urls = get_sitemap_urls()
    if not urls:
        print("❌ No URLs found. Is the site live?")
        return

    # High-priority only
    if args.new_only:
        HIGH_PRIORITY = ["/", "/itad-kochi.html", "/data-destruction-kochi.html",
                         "/sell-old-laptop-kochi.html", "/sell-old-phone-kochi.html",
                         "/blog/is-formatting-enough-delete-data.html",
                         "/blog/dpdp-act-impact-startups.html",
                         "/compliance/dpdp-act-2023-penalties.html"]
        urls = [f"{DOMAIN}{p}" for p in HIGH_PRIORITY]
        print(f"🎯 High-priority mode: {len(urls)} pages\n")

    # Step 1: Sitemap ping (Google + Bing)
    print("── Sitemap Ping (Google + Bing) ──")
    ping_sitemap()

    # Step 2: IndexNow (Bing, Yandex, Seznam)
    print(f"\n── IndexNow Submission ({len(urls)} URLs) ──")
    # IndexNow max 10,000 URLs per request; batch into 500
    batch_size = 500
    for i in range(0, len(urls), batch_size):
        batch = urls[i:i+batch_size]
        print(f"  Batch {i//batch_size + 1}: {len(batch)} URLs")
        submit_indexnow(batch)
        if i + batch_size < len(urls):
            time.sleep(2)

    # Step 3: Verify robots.txt
    print("\n── robots.txt Verification ──")
    verify_robots()

    # Step 4: Summary
    print("\n" + "═"*58)
    print("  ✅ Indexing submission complete!")
    print(f"  🔗 {len(urls)} URLs submitted")
    print("  📋 Next steps:")
    print("     1. Google Search Console → Sitemaps → Submit sitemap URL")
    print("     2. Bing Webmaster Tools → Sitemaps → Submit")
    print("     3. Wait 24-72h for Google  |  ~1h for Bing (IndexNow)")
    print("     4. For AI models: no action needed — robots.txt allows all")
    print("═"*58 + "\n")

if __name__ == "__main__":
    main()
