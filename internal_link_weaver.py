import os
import re

# CONFIG
ROOT = "/media/hp-ml10/Projects/ewastekochi-production/ewastekochi/"
PILLAR_TOPICS = [
    "e-waste-recycling-kochi",
    "it-asset-disposal-kochi",
    "data-destruction-kochi",
    "laptop-recycling-kochi",
    "corporate-e-waste-kochi",
    "computer-disposal-kochi",
    "electronics-scrap-kochi",
    "mobile-recycling-kochi",
    "battery-recycling-kochi",
    "itad-kochi-complete-guide"
]

def get_html_files(directory):
    files = []
    for d, _, fs in os.walk(directory):
        for f in fs:
            if f.endswith(".html"):
                files.append(os.path.join(d, f))
    return files

def weave_links():
    files = get_html_files(ROOT)
    print(f"Weaving internal links for {len(files)} files...")
    
    pillar_links_html = '<div class="pillar-links" style="display:flex;gap:15px;flex-wrap:wrap;margin:40px 0;padding:20px;background:#111a14;border-radius:15px;border:1px solid rgba(0,232,122,.15)">\n'
    for slug in PILLAR_TOPICS:
        name = slug.replace("-", " ").title()
        pillar_links_html += f'  <a href="/{slug}.html" style="color:#00e664;text-decoration:none;font-weight:700">↳ {name}</a>\n'
    pillar_links_html += '</div>\n'

    for fpath in files:
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        
        # 1. Inject Pillar Links Hub before footer
        if "</footer>" in content:
            new_content = content.replace("</footer>", pillar_links_html + "</footer>")
            
            # Use relative paths for subdirectories (blog, industries, etc.)
            depth = fpath.replace(ROOT, "").lstrip("/").count("/")
            if depth > 0:
                rel = "../" * depth
                new_content = new_content.replace('href="/', f'href="{rel}')
            
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(new_content)
                
    print("🚀 Internal Link Weaver: Authority Loop completed!")

if __name__ == "__main__":
    weave_links()
