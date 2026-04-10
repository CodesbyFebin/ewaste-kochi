import os
import re
from collections import defaultdict

BASE = "/media/hp-ml10/Projects/ewastekochi-production/ewastekochi"
INDEX_PATH = os.path.join(BASE, "index.html")
LIST_PATH = os.path.join(BASE, "html_files_list.txt")

with open(LIST_PATH, "r", encoding="utf-8") as f:
    files = [line.strip() for line in f if line.strip()]

categories = defaultdict(list)

for file in files:
    parts = file.split("/")
    if len(parts) == 1:
        cat = "Main Pages"
    else:
        cat = parts[0].replace("-", " ").title()
    
    url = "/" + file.replace(".html", "")
    if url == "/index": url = "/"
    
    name = parts[-1].replace(".html", "").replace("-", " ").replace("_", " ").title()
    if name == "Index": name = cat + " Overview"
    
    categories[cat].append((name, url))

# Build HTML Block
html_blocks = []
html_blocks.append('<section class="section" style="background:var(--bg2); border-top:1px solid var(--border);" id="sitemap-directory">')
html_blocks.append('  <div class="wrap">')
html_blocks.append('    <h2 style="text-align:center;">Comprehensive Services Directory</h2>')
html_blocks.append('    <p style="text-align:center; opacity:0.8; margin-bottom:40px;">Explore all 2,000+ of our certified e-waste, ITAD, and data destruction services across Kerala.</p>')
html_blocks.append('    <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px;">')

for cat in sorted(categories.keys()):
    items = sorted(categories[cat], key=lambda x: x[0])
    html_blocks.append(f'      <div style="background:var(--bg); border:1px solid var(--border); border-radius:10px; padding:20px;">')
    html_blocks.append(f'        <h3 style="margin-top:0; border-bottom:2px solid var(--green); padding-bottom:10px;">{cat} <span style="font-size:0.8rem; color:var(--muted); font-weight:normal;">({len(items)})</span></h3>')
    html_blocks.append(f'        <div style="max-height: 250px; overflow-y: auto; padding-right:10px; margin-top:15px;">')
    html_blocks.append(f'          <ul style="list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:8px;">')
    for name, url in items:
        html_blocks.append(f'            <li><a href="{url}" style="font-size:0.85rem; color:var(--text); transition:color 0.2s;" onmouseover="this.style.color=\'var(--green)\'" onmouseout="this.style.color=\'var(--text)\'">{name}</a></li>')
    html_blocks.append(f'          </ul>')
    html_blocks.append(f'        </div>')
    html_blocks.append(f'      </div>')

html_blocks.append('    </div>')
html_blocks.append('  </div>')
html_blocks.append('</section>')

sitemap_html = "\n".join(html_blocks)

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# Remove old section if exists (for idempotency)
import re
content = re.sub(r'<section class="section" style="background:var\(--bg2\); border-top:1px solid var\(--border\);" id="sitemap-directory">.*?</section>', '', content, flags=re.DOTALL)

# Insert before </body>
if "</body>" in content:
    content = content.replace("</body>", sitemap_html + "\n</body>")
else:
    # If no body closing tag, just append
    content += "\n" + sitemap_html

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print(f"✅ Injected 2000 links grouped into {len(categories)} categories into index.html")
