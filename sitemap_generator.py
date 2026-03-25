import os
from pathlib import Path
from datetime import datetime

BASE_URL = "https://ewastekochi.com"
ROOT_DIR = Path("/media/hp-ml10/Projects/EwasteKochi.com")
SITEMAP_PATH = ROOT_DIR / "sitemap.xml"

# Directories to crawl for SEO pages
CONTENT_DIRS = [
    "services",
    "itad",
    "security",
    "locations/v2",
    "blog",
    "ml", # Malayalam Cluster
    "buyback",
    "locations" # Legacy cluster
]

# Core pages to always include
CORE_PAGES = [
    "index.html",
    "about.html",
    "contact.html",
    "media-kit.html",
    "marketplace.html",
    "faq.html",
    "pickup-certificate.html",
    "certificate-of-destruction.html"
]

def generate_sitemap():
    print("🛰️  Generating Master Sitemap for EWaste Kochi...")
    
    url_nodes = []
    today = datetime.now().strftime("%Y-%m-%d")

    # 1. Add Core Pages
    for page in CORE_PAGES:
        if (ROOT_DIR / page).exists():
            url_nodes.append(f"""  <url>
    <loc>{BASE_URL}/{page}</loc>
    <lastmod>{today}</lastmod>
    <priority>1.0</priority>
  </url>""")

    # 2. Add Content Pages from High-Intent Clusters
    for folder in CONTENT_DIRS:
        folder_path = ROOT_DIR / folder
        if folder_path.exists():
            # Check for blog output specifically if it exists in 'output/blog'
            if folder == "blog" and (ROOT_DIR / "output" / "blog").exists():
                search_path = ROOT_DIR / "output" / "blog"
                prefix = "blog"
            else:
                search_path = folder_path
                prefix = folder

            for file in search_path.glob("**/*.html"):
                # Avoid duplicates of core pages if any
                if file.name in CORE_PAGES: continue
                
                # Calculate relative path from root
                rel_path = file.relative_to(ROOT_DIR if folder != "blog" else (ROOT_DIR / "output"))
                
                priority = "0.8" if "v2" in str(rel_path) or "services" in str(rel_path) else "0.6"
                
                url_nodes.append(f"""  <url>
    <loc>{BASE_URL}/{rel_path}</loc>
    <lastmod>{today}</lastmod>
    <priority>{priority}</priority>
  </url>""")

    # 3. Write Sitemap
    sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{"".join(url_nodes)}
</urlset>
"""

    with open(SITEMAP_PATH, "w") as f:
        f.write(sitemap_content)
    
    print(f"✅ Master Sitemap generated with {len(url_nodes)} URLs!")

if __name__ == "__main__":
    generate_sitemap()
