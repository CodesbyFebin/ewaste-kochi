import os
import datetime
import xml.etree.ElementTree as ET
from xml.dom import minidom

# Config
DOMAIN = "https://ewastekochi.com"
PROJECT_DIR = "/media/hp-ml10/Projects/EwasteKochi.com"
SITEMAP_FILE = os.path.join(PROJECT_DIR, "sitemap.xml")

# Excluded files
EXCLUDE_FILES = ["404.html", "portal-login.html"]
EXCLUDE_DIRS = [".git", "node_modules", "assets", "venv", "tmp"]

def generate_sitemap():
    urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    
    # Homepage (Special)
    today = datetime.date.today().isoformat()
    url = ET.SubElement(urlset, "url")
    ET.SubElement(url, "loc").text = f"{DOMAIN}/"
    ET.SubElement(url, "lastmod").text = today
    ET.SubElement(url, "changefreq").text = "daily"
    ET.SubElement(url, "priority").text = "1.0"

    print(f"Scanning {PROJECT_DIR} for .html files...")
    
    for root, dirs, files in os.walk(PROJECT_DIR):
        # Exclude hidden and non-SEO dirs
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in EXCLUDE_DIRS]
        
        for f in files:
            if f.endswith(".html") and f not in EXCLUDE_FILES:
                rel_dir = os.path.relpath(root, PROJECT_DIR)
                rel_path = f if rel_dir == "." else os.path.join(rel_dir, f)
                
                # Use / for URL paths
                url_path = rel_path.replace(os.sep, "/")
                
                # Skip index.html since we added homepage /
                if url_path == "index.html":
                    continue
                
                full_url = f"{DOMAIN}/{url_path}"
                
                # Priority logic based on path
                priority = "0.7"
                if "blog" in url_path: priority = "0.75"
                if "compliance" in url_path: priority = "0.9"
                if "services" in url_path: priority = "0.85"
                if "itad" in url_path: priority = "0.9"
                if "industries" in url_path: priority = "0.8"
                if rel_dir == ".": priority = "0.95" # Top level pages
                
                url_elem = ET.SubElement(urlset, "url")
                ET.SubElement(url_elem, "loc").text = full_url
                ET.SubElement(url_elem, "lastmod").text = today
                ET.SubElement(url_elem, "changefreq").text = "weekly"
                ET.SubElement(url_elem, "priority").text = priority

    # Pretty print
    xmlstr = minidom.parseString(ET.tostring(urlset)).toprettyxml(indent="  ")
    
    with open(SITEMAP_FILE, "w", encoding="utf-8") as f:
        f.write(xmlstr)
    
    print(f"✅ Sitemap regenerated with {len(urlset)} URLs at {SITEMAP_FILE}")

if __name__ == "__main__":
    generate_sitemap()
