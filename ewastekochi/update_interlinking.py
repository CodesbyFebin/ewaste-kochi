import os
import random
import re

BASE = "/media/hp-ml10/Projects/ewastekochi-production/ewastekochi"
LIST_PATH = os.path.join(BASE, "html_files_list.txt")

with open(LIST_PATH, "r", encoding="utf-8") as f:
    files = [line.strip() for line in f if line.strip()]

# Total pool for random selection
all_urls = ["/" + f.replace(".html", "") for f in files]
if "/index" in all_urls: all_urls.remove("/index")
all_urls.append("/")

def process_file(rel_path):
    abs_path = os.path.join(BASE, rel_path)
    if not os.path.exists(abs_path): return
    
    with open(abs_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check if we already have the interlinking footer
    if 'id="master-interlinking"' in content:
        return
    
    # Select 10 random links for "Explore More Services"
    random_links = random.sample(all_urls, min(10, len(all_urls)))
    links_html = " ".join([f'<a href="{url}" class="silo-link">{url.split("/")[-1].replace("-", " ").title() if url != "/" else "Home"}</a>' for url in random_links])
    
    interlink_html = f"""
<section class="section" style="background:var(--bg2); border-top:1px solid var(--border);" id="master-interlinking">
  <div class="wrap">
    <h2 style="font-family:\'Bebas Neue\', cursive; font-size: 2.2rem; color: var(--white); margin-bottom: 20px;">Explore More Services</h2>
    <div style="display:flex; flex-wrap:wrap; gap:10px; margin-top:20px;">
      <a href="/" class="silo-link">🏠 Home</a>
      {links_html}
    </div>
    <div style="margin-top:40px; padding-top:20px; border-top:1px solid var(--border); font-size:0.85rem; color:var(--muted);">
      <p>© 2026 EWaste Kochi - Kerala\'s #1 Certified ITAD & E-Waste Recycler. Authorized by KSPCB. NIST 800-88 Compliant. DPDP Act 2023 Validated.</p>
    </div>
  </div>
</section>
"""
    
    # Insert before </body>
    new_content = re.sub(r'(</body>)', interlink_html + r'\1', content, flags=re.IGNORECASE)
    
    if new_content == content:
        # If no </body> tag (malformed HTML), just append
        new_content = content + "\n" + interlink_html
        
    with open(abs_path, "w", encoding="utf-8") as f:
        f.write(new_content)

print(f"Starting interlinking update for {len(files)} files...")
count = 0
for f in files:
    try:
        process_file(f)
        count += 1
        if count % 100 == 0:
            print(f"Processed {count}/{len(files)} files...")
    except Exception as e:
        print(f"Error processing {f}: {e}")

print(f"✅ Successfully updated interlinking for {count} files.")
