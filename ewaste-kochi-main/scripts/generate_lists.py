import os
from pathlib import Path
from xml.etree import ElementTree as ET

BASE = "/media/hp-ml10/Projects/ewastekochi-production/ewastekochi"
SITE = "https://ewastekochi.com"

def generate():
    sitemap_path = os.path.join(BASE, "sitemap.xml")
    if not os.path.exists(sitemap_path):
        print("sitemap.xml not found!")
        return

    # Parse sitemap to get URLs
    tree = ET.parse(sitemap_path)
    root = tree.getroot()
    # xml namespace handling is tricky with simple ET, so just find all strings that start with http
    urls = []
    with open(sitemap_path, 'r') as f:
        content = f.read()
        import re
        urls = re.findall(r'<loc>(.*?)</loc>', content)

    # 1. Generate URL List text file
    url_list_path = os.path.join(BASE, "url_list.txt")
    with open(url_list_path, "w", encoding="utf-8") as f:
        f.write("\n".join(urls))
    print(f"✅ Generated url_list.txt with {len(urls)} URLs")

    # 2. Get list of all physical HTML files
    EXCLUDE = {"__pycache__", "gitlab_repo", "ewastekochi-production", "node_modules"}
    html_files = []
    for r, dirs, fs in os.walk(BASE):
        dirs[:] = [d for d in dirs if d not in EXCLUDE]
        for name in fs:
            if name.endswith(".html"):
                fp = os.path.join(r, name)
                rel = Path(fp).relative_to(BASE)
                html_files.append(str(rel))

    html_files.sort()
    
    # Generate Physical Files list
    file_list_path = os.path.join(BASE, "html_files_list.txt")
    with open(file_list_path, "w", encoding="utf-8") as f:
        f.write("\n".join(html_files))
    print(f"✅ Generated html_files_list.txt with {len(html_files)} files")

if __name__ == "__main__":
    generate()
