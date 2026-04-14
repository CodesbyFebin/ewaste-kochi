import os
import shutil
import glob
import re

base_dir = "/media/hp-ml10/Projects/ewastekochi-production/ewastekochi"
sitemap_path = os.path.join(base_dir, "sitemap.xml")

categories = {
    "data-security": ["destruction", "shredding", "wiping", "itad", "data", "gdpr", "dpdp", "secure", "security", "decommissioning"],
    "trading": ["sell", "buy", "buyers", "cashify", "alternative", "scrap", "aakri", "dealers", "dealer"],
    "disposal": ["disposal", "dispose", "taking", "bin", "box", "plasma", "bed"],
    "collection": ["collection", "pickup", "management"],
    "recycling": ["recycle", "recycling", "re", "cd", "ac", "battery", "batteries"],
}

# files to ignore moving
ignore_files = [
    "index.html", 
    "data-destruction-kochi.html",
    "404.html",
    "contact.html",
    "about.html",
    "services.html"
]

def get_category(filename):
    name_lower = filename.lower()
    for cat, keywords in categories.items():
        if any(kw in name_lower for kw in keywords):
            return cat
    return "general-waste"

def main():
    # 1. Gather all html files in the root dir
    html_files = [f for f in os.listdir(base_dir) if f.endswith(".html") and os.path.isfile(os.path.join(base_dir, f))]
    
    moved_urls = []
    
    for file in html_files:
        if file in ignore_files or file.startswith("sitemap"):
            continue
            
        # some generated files might match existing templates, we only move files that were recently generated
        # or we just move all of them except ignore_files.
        cat = get_category(file)
        cat_dir = os.path.join(base_dir, cat)
        
        if not os.path.exists(cat_dir):
            os.makedirs(cat_dir)
            
        old_path = os.path.join(base_dir, file)
        new_path = os.path.join(cat_dir, file)
        
        # rename/move
        shutil.move(old_path, new_path)
        
        # update canonical URL inside the file
        slug = file.replace('.html', '')
        with open(new_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        # replace old canonicals
        content = content.replace(f"https://ewastekochi.com/{slug}.html", f"https://ewastekochi.com/{cat}/{slug}.html")
        content = content.replace(f"https://ewastekochi.com/{slug}", f"https://ewastekochi.com/{cat}/{slug}")
        
        # ensure interlinking to home page is prominent (adding a breadcrumb or making sure the nav works)
        # We already have <a class="nav-brand" href="/"> in the template, which acts as home interlink.
        
        with open(new_path, "w", encoding="utf-8") as f:
            f.write(content)
            
        # track for sitemap update
        moved_urls.append((slug, cat))
        print(f"Moved {file} -> {cat}/{file}")

    # 2. Update sitemap.xml
    if os.path.exists(sitemap_path):
        with open(sitemap_path, "r", encoding="utf-8") as f:
            sitemap_content = f.read()
            
        for slug, cat in moved_urls:
            # Our sitemap update script added them as <loc>https://ewastekochi.com/{slug}</loc>
            old_loc = f"<loc>https://ewastekochi.com/{slug}</loc>"
            new_loc = f"<loc>https://ewastekochi.com/{cat}/{slug}</loc>"
            
            # Also might have added them as <loc>https://ewastekochi.com/{slug}.html</loc>
            old_loc_html = f"<loc>https://ewastekochi.com/{slug}.html</loc>"
            new_loc_html = f"<loc>https://ewastekochi.com/{cat}/{slug}.html</loc>"
            
            sitemap_content = sitemap_content.replace(old_loc, new_loc)
            sitemap_content = sitemap_content.replace(old_loc_html, new_loc_html)
            
        with open(sitemap_path, "w", encoding="utf-8") as f:
            f.write(sitemap_content)
        print("Updated sitemap.xml with the new category paths.")

if __name__ == "__main__":
    main()
