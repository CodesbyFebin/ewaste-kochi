"""
Blog Subdomain Builder — blog.ewastekochi.com
- Creates /blog-subdomain/ folder (deploy this as blog.ewastekochi.com webroot)
- Copies all blog HTML files, rewrites canonical + internal links to blog.ewastekochi.com
- Generates a full blog index page with card grid
- Generates sitemap for the subdomain
"""
import os, re, shutil
from datetime import datetime

SRC  = "/media/hp-ml10/Projects/ewastekochi-production/ewastekochi/blog/"
DEST = "/media/hp-ml10/Projects/ewastekochi-production/blog-subdomain/"
MAIN = "https://ewastekochi.com"
BLOG = "https://blog.ewastekochi.com"

os.makedirs(DEST, exist_ok=True)

# ── Collect all blog posts (skip index.html — we'll regenerate it) ────────────
posts = sorted([f for f in os.listdir(SRC) if f.endswith(".html") and f != "index.html"])

# ── Rewrite each post ─────────────────────────────────────────────────────────
def rewrite(html, slug):
    # Fix canonical
    html = re.sub(
        r'<link rel="canonical"[^>]*>',
        f'<link rel="canonical" href="{BLOG}/{slug}">',
        html
    )
    # If no canonical exists, inject one after <head>
    if '<link rel="canonical"' not in html:
        html = html.replace("<head>", f'<head>\n<link rel="canonical" href="{BLOG}/{slug}">')

    # Add/replace base href so relative assets resolve to main domain
    if "<base " not in html:
        html = html.replace("<head>", f'<head>\n<base href="{MAIN}/">')

    # Update og:url
    html = re.sub(r'<meta property="og:url"[^>]*>', f'<meta property="og:url" content="{BLOG}/{slug}">', html)

    # Inject subdomain nav bar if missing
    if "blog-subnav" not in html:
        subnav = f"""
<div id="blog-subnav" style="background:#0A0F0C;border-bottom:1px solid rgba(0,230,100,.15);padding:10px 24px;display:flex;align-items:center;justify-content:space-between;font-family:'Outfit',sans-serif;font-size:.85rem">
  <div style="display:flex;align-items:center;gap:20px">
    <a href="{BLOG}/" style="font-weight:800;color:#00E664;text-decoration:none">📝 Blog.EwasteKochi</a>
    <a href="{BLOG}/" style="color:#9BB8A2;text-decoration:none">All Posts</a>
    <a href="{MAIN}/itad-kochi.html" style="color:#9BB8A2;text-decoration:none">ITAD Guide</a>
    <a href="{MAIN}/data-destruction-kochi.html" style="color:#9BB8A2;text-decoration:none">Data Destruction</a>
    <a href="{MAIN}/ewaste-compliance-kerala.html" style="color:#9BB8A2;text-decoration:none">Compliance</a>
  </div>
  <a href="{MAIN}/" style="color:#5A7A62;text-decoration:none">← Main Site</a>
</div>"""
        html = html.replace("<body>", f"<body>\n{subnav}")

    return html

print(f"Processing {len(posts)} blog posts → {DEST}")
for fname in posts:
    src_path  = os.path.join(SRC, fname)
    dest_path = os.path.join(DEST, fname)
    with open(src_path, "r", encoding="utf-8", errors="ignore") as f:
        html = f.read()
    html = rewrite(html, fname)
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  ✓ {fname}")

# ── Blog Index Page ───────────────────────────────────────────────────────────
def slug_to_title(slug):
    return slug.replace(".html","").replace("-"," ").title()

cards = ""
for fname in posts:
    title = slug_to_title(fname)
    cards += f"""
    <a href="{BLOG}/{fname}" class="card">
      <div class="card-tag">EWaste Kochi</div>
      <h2>{title}</h2>
      <span class="card-cta">Read Full Guide →</span>
    </a>"""

index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Blog | EWaste Kochi — ITAD, Data Security & E-Waste Kerala</title>
<meta name="description" content="Expert guides on ITAD, data destruction, e-waste rules, laptop buyback, and DPDP Act compliance in Kochi, Kerala. {len(posts)} in-depth articles.">
<link rel="canonical" href="{BLOG}/">
<meta property="og:title" content="EWaste Kochi Blog — Kerala ITAD & E-Waste Authority">
<meta property="og:url" content="{BLOG}/">
<meta property="og:type" content="website">
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Outfit:wght@400;600;700;800&display=swap" rel="stylesheet">
<style>
:root{{--bg:#0A0F0C;--bg2:#111A14;--green:#00E664;--white:#E8F2EA;--text:#9BB8A2;--muted:#5A7A62;--border:rgba(0,230,100,.13)}}
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Outfit',sans-serif;background:var(--bg);color:var(--text);min-height:100vh}}
a{{text-decoration:none;color:inherit}}
/* top nav */
.top-nav{{background:rgba(7,16,10,.97);border-bottom:1px solid var(--border);padding:0 24px;height:62px;display:flex;align-items:center;justify-content:space-between;position:sticky;top:0;z-index:100;backdrop-filter:blur(20px)}}
.nav-brand{{font-family:'Bebas Neue';font-size:1.5rem;color:var(--white);display:flex;align-items:center;gap:8px}}
.nav-links{{display:flex;gap:20px;font-size:.83rem;color:var(--muted);font-weight:600}}
.nav-links a:hover{{color:var(--green)}}
.nav-cta{{background:var(--green);color:var(--bg);padding:8px 18px;border-radius:8px;font-weight:800;font-size:.83rem}}
/* hero */
.hero{{padding:80px 24px 60px;text-align:center;border-bottom:1px solid var(--border);background:radial-gradient(ellipse at 50% 0%,rgba(0,230,100,.06),transparent 60%)}}
.hero h1{{font-family:'Bebas Neue';font-size:clamp(2.6rem,7vw,5rem);color:var(--white);line-height:1.05;margin-bottom:16px}}
.hero h1 span{{color:var(--green)}}
.hero p{{color:var(--muted);max-width:580px;margin:0 auto 32px;line-height:1.8}}
.hero-stats{{display:inline-flex;gap:32px;background:var(--bg2);border:1px solid var(--border);border-radius:12px;padding:16px 32px;font-size:.85rem}}
.hero-stats b{{color:var(--green);font-size:1.3rem;display:block;font-family:'Bebas Neue'}}
/* search */
.search-bar{{max-width:900px;margin:40px auto 0;padding:0 24px}}
.search-bar input{{width:100%;background:var(--bg2);border:1px solid var(--border);border-radius:10px;padding:14px 20px;color:var(--white);font-size:1rem;outline:none;transition:border-color .2s}}
.search-bar input:focus{{border-color:var(--green)}}
/* grid */
.wrap{{max-width:1240px;margin:0 auto;padding:0 24px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:20px;padding:40px 0 80px}}
.card{{background:var(--bg2);border:1px solid var(--border);border-radius:14px;padding:28px;display:flex;flex-direction:column;gap:12px;transition:border-color .2s,transform .2s;cursor:pointer}}
.card:hover{{border-color:var(--green);transform:translateY(-3px)}}
.card-tag{{font-size:.7rem;font-weight:700;text-transform:uppercase;letter-spacing:1px;color:var(--muted)}}
.card h2{{font-size:1.05rem;color:var(--white);font-weight:700;line-height:1.4;flex:1}}
.card-cta{{font-size:.82rem;font-weight:800;color:var(--green)}}
/* footer */
.footer{{background:#050806;border-top:1px solid var(--border);padding:40px 24px;text-align:center;font-size:.82rem;color:var(--muted)}}
.footer a{{color:var(--green);margin:0 8px}}
@media(max-width:600px){{.nav-links{{display:none}}.hero h1{{font-size:2.4rem}}.hero-stats{{flex-direction:column;gap:16px;text-align:center}}}}
</style>
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Blog","name":"EWaste Kochi Blog","url":"{BLOG}/","description":"Expert guides on ITAD, data destruction, e-waste compliance and laptop buyback in Kochi Kerala.","publisher":{{"@type":"Organization","name":"EWaste Kochi","url":"{MAIN}/"}}}}
</script>
</head>
<body>

<nav class="top-nav">
  <div class="nav-brand">📝 Blog.EwasteKochi</div>
  <div class="nav-links">
    <a href="{BLOG}/">All Posts</a>
    <a href="{MAIN}/itad-kochi.html">ITAD Guide</a>
    <a href="{MAIN}/data-destruction-kochi.html">Data Destruction</a>
    <a href="{MAIN}/ewaste-compliance-kerala.html">Compliance</a>
  </div>
  <a class="nav-cta" href="{MAIN}/">Main Site →</a>
</nav>

<div class="hero">
  <h1>Kochi's #1 <span>E-Waste & ITAD</span><br>Knowledge Hub</h1>
  <p>{len(posts)} expert guides on data destruction, ITAD, DPDP Act compliance, laptop buyback, and e-waste rules — all focused on Kochi &amp; Kerala.</p>
  <div class="hero-stats">
    <div><b>{len(posts)}</b>In-Depth Articles</div>
    <div><b>10</b>Topic Categories</div>
    <div><b>2,000+</b>FAQs Covered</div>
  </div>
</div>

<div class="search-bar">
  <input type="text" id="search" placeholder="🔍  Search guides… e.g. DPDP Act, laptop buyback, data destruction" oninput="filterCards(this.value)">
</div>

<div class="wrap">
  <div class="grid" id="grid">{cards}</div>
</div>

<footer class="footer">
  <p>© 2026 EWaste Kochi Blog — KSPCB Authorised ITAD Authority, Kochi Kerala</p>
  <p style="margin-top:10px">
    <a href="{MAIN}/">Main Site</a>
    <a href="{MAIN}/itad-kochi.html">ITAD</a>
    <a href="{MAIN}/data-destruction-kochi.html">Data Destruction</a>
    <a href="{MAIN}/computer-scrap-kochi.html">Computer Scrap</a>
    <a href="{MAIN}/ewaste-compliance-kerala.html">Compliance</a>
  </p>
</footer>

<script>
function filterCards(q) {{
  q = q.toLowerCase();
  document.querySelectorAll('#grid .card').forEach(c => {{
    const t = c.querySelector('h2').textContent.toLowerCase();
    c.style.display = t.includes(q) ? '' : 'none';
  }});
}}
</script>
</body>
</html>"""

with open(os.path.join(DEST, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_html)
print(f"\n  ✓ index.html (blog homepage with {len(posts)} post cards)")

# ── Subdomain Sitemap ─────────────────────────────────────────────────────────
now = datetime.now().strftime("%Y-%m-%d")
sm  = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
sm += f'  <url><loc>{BLOG}/</loc><lastmod>{now}</lastmod><priority>1.0</priority></url>\n'
for fname in posts:
    sm += f'  <url><loc>{BLOG}/{fname}</loc><lastmod>{now}</lastmod><priority>0.8</priority></url>\n'
sm += "</urlset>"

with open(os.path.join(DEST, "sitemap.xml"), "w") as f:
    f.write(sm)

# ── robots.txt ────────────────────────────────────────────────────────────────
with open(os.path.join(DEST, "robots.txt"), "w") as f:
    f.write(f"User-agent: *\nAllow: /\nSitemap: {BLOG}/sitemap.xml\n")

print(f"  ✓ sitemap.xml ({len(posts)+1} URLs)")
print(f"  ✓ robots.txt")
print(f"\n═══════════════════════════════════════════")
print(f"  ✅  blog-subdomain/ READY TO DEPLOY")
print(f"  📁  {len(posts)+1} HTML files (index + {len(posts)} posts)")
print(f"  🌐  Point blog.ewastekochi.com → {DEST}")
print(f"  🗺️   Sitemap: {BLOG}/sitemap.xml")
print(f"═══════════════════════════════════════════")
