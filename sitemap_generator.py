import os
from datetime import datetime

ROOT = "/media/hp-ml10/Projects/ewastekochi-production/ewastekochi/"
BASE_URL = "https://ewastekochi.com"

def generate_sitemap_xml():
    files = []
    for d, _, fs in os.walk(ROOT):
        for f in fs:
            if f.endswith(".html"):
                full_path = os.path.join(d, f)
                rel_path = full_path.replace(ROOT, "").replace("\\", "/")
                files.append(rel_path)

    now = datetime.now().strftime("%Y-%m-%d")
    
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    for f in files:
        url = f"{BASE_URL}/{f}"
        if f == "index.html":
            url = BASE_URL + "/"
        xml += f'  <url>\n    <loc>{url}</loc>\n    <lastmod>{now}</lastmod>\n    <changefreq>daily</changefreq>\n    <priority>{"1.0" if f == "index.html" else "0.8"}</priority>\n  </url>\n'
    
    xml += "</urlset>"
    
    with open(os.path.join(ROOT, "sitemap.xml"), "w") as f:
        f.write(xml)
    print(f"✅ Sitemap: {len(files)} URLs added to sitemap.xml")

if __name__ == "__main__":
    generate_sitemap_xml()
