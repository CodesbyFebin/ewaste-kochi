import json
import os
import re
from datetime import datetime

# CONFIG
BASE_URL = "https://ewastekochi.com"
PUBLIC_DIR = "public"

def get_urls():
    urls = ["/", "/recycling/", "/itad/", "/ewaste/", "/about/", "/contact/", "/blog/"]
    
    # Locations
    with open('src/data/locations.js', 'r') as f:
        loc_js = f.read()
    loc_slugs = re.findall(r'"slug":\s*"([^"]+)"', loc_js)
    print(f"Found {len(loc_slugs)} locations.")
        
    # Services
    with open('src/data/services.js', 'r') as f:
        svc_js = f.read()
    svc_slugs = re.findall(r"['\"]?slug['\"]?:\s*['\"]([^'\"]+)['\"]", svc_js)
    print(f"Found {len(svc_slugs)} services.")
        
    for l in loc_slugs:
        urls.append(f"/locations/{l}/")
        for s in svc_slugs:
            urls.append(f"/locations/{l}/{s}/")
            
    for s in svc_slugs:
        urls.append(f"/services/{s}/")
        
    # Blogs
    blog_count = 0
    for i in range(1, 11): # Now 10 parts
        try:
            with open(f'src/data/blogPosts_part{i}.json', 'r') as f:
                blogs = json.load(f)
                for b in blogs:
                    urls.append(f"/blog/{b['slug']}/")
                    blog_count += 1
        except: pass
    print(f"Found {blog_count} blogs.")
                
    return sorted(list(set(urls)))

def generate_xml(urls):
    now = datetime.now().strftime("%Y-%m-%d")
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for url in urls:
        xml += f'  <url>\n    <loc>{BASE_URL}{url}</loc>\n    <lastmod>{now}</lastmod>\n    <changefreq>daily</changefreq>\n    <priority>0.8</priority>\n  </url>\n'
    xml += "</urlset>"
    with open(os.path.join(PUBLIC_DIR, "sitemap-authority.xml"), "w") as f:
        f.write(xml)
    print(f"Generated sitemap-authority.xml with {len(urls)} URLs.")

if __name__ == "__main__":
    urls = get_urls()
    generate_xml(urls)
