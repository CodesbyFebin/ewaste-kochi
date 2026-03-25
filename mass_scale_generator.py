import os
import datetime
import xml.etree.ElementTree as ET
from urllib.parse import quote

base_dir = "/media/hp-ml10/Projects/EwasteKochi.com"
locations_dir = os.path.join(base_dir, "locations")
blog_dir = os.path.join(base_dir, "blog")

os.makedirs(locations_dir, exist_ok=True)
os.makedirs(blog_dir, exist_ok=True)

# ── 1. The 50-Node Location Matrix (Ernakulam District Domination) ──
kochi_locations = [
    "Aluva", "Angamaly", "Edappally", "Kakkanad", "Kaloor", "Kalamassery", 
    "Marine Drive", "Palarivattom", "Panampilly Nagar", "Thrippunithura", "Vyttila", 
    "Fort Kochi", "Mattancherry", "Willingdon Island", "Thoppumpady", "Palluruthy", 
    "Kacheripady", "Ravipuram", "Elamkulam", "Kadavanthra", "Thammanam", "Vennala",
    "Chottanikkara", "Nettoor", "Kundanoor", "Maradu", "Kizhakkambalam", "Perumbavoor",
    "Muvattupuzha", "Kothamangalam", "Kolenchery", "Potta", "Nedumbassery", 'Athani',
    "Cheranallur", "Eloor", "Muttom", "Choornikkara", "Keezhmad", "Chengamanad",
    "Kumbalam", "Chellanam", "Mulavukad", "Njarackal", "Vypeen", "Kuzhuppilly",
    "Paravur", "Chendamangalam", "Puthenvelikkara", "Varapuzha"
]

# ── 2. The 30-Node Traffic Explosion Blog Network ──
blog_slugs = [
    "where-to-sell-old-phone-kochi", "laptop-resale-value-kochi", 
    "is-olx-safe-in-kerala", "how-companies-dispose-it-assets-india",
    "ewaste-management-rules-2022-kerala", "dpdp-act-impact-on-startups-kochi",
    "why-not-to-throw-batteries-in-trash", "laptop-battery-disposal-ernakulam",
    "iphone-resale-value-drop-calc", "sell-macbook-pro-kochi-cash",
    "data-wiping-software-vs-shredding", "what-is-a-certificate-of-destruction",
    "pcb-authorized-ewaste-recyclers-list", "haritha-karma-sena-ewaste-fee",
    "bulk-computer-scrap-buyers-kerala", "office-shifting-it-clearance",
    "data-center-decommissioning-steps", "hard-drive-shredding-service-kochi",
    "how-to-recycle-broken-tv-kochi", "sell-dead-laptop-for-parts",
    "smartphone-recycling-precious-metals", "what-happens-to-recycled-ewaste",
    "corporate-social-responsibility-ewaste", "hospital-medical-equipment-disposal",
    "bank-it-asset-disposition-rbi", "schools-ewaste-collection-drive",
    "best-place-to-sell-used-electronics", "electronic-waste-hazards",
    "kochi-municipal-corporation-ewaste", "infopark-green-initiatives-2026"
]

# ── TEMPLATES (Injected with dynamic localized context + Trust Signals) ──

location_template = """<!DOCTYPE html>
<html lang="en-IN" dir="ltr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>E-Waste Recycling & ITAD in {location} | EWaste Kochi Sector</title>
<meta name="description" content="Free e-waste pickup and certified Corporate ITAD directly in {location}. We offer highest cash value for old laptops & mobile phones. DPDP Act compliant.">
<link rel="stylesheet" href="../assets/css/style.css">
</head>
<body style="background:var(--ow);">
<header class="header" id="nav" style="background:var(--n);border-bottom:1px solid rgba(255,255,255,.05);"><div class="wrap nav-container"><a href="../index.html" class="logo" style="color:var(--w);"><div class="logo-icon">♻️</div>EWaste<em>Kochi</em></a><nav class="nav-links"><a href="../book-free-pickup-kochi.html" class="btn btn-wa btn-sm">Book Pickup in {location}</a></nav></div></header>

<section style="padding:100px 0;text-align:center;">
  <div class="wrap">
    <div class="ey">Location Domination Silo</div>
    <h1 style="margin:20px 0;">Certified E-Waste Disposal in {location}</h1>
    
    <div style="background:#E5F7F2; padding:20px; border-radius:8px; display:inline-block; margin-bottom:40px; border:1px solid var(--g);">
      <strong>⚡ Local Dispatch Alert:</strong> Fleet currently operating near {location}. Book now for prioritizing today's routing schedule.
    </div>

    <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(250px, 1fr));gap:20px;text-align:left;">
      <div style="background:var(--w);padding:30px;border-radius:12px;box-shadow:var(--sh-md);">
        <h3 style="color:var(--g);">Sell Devices Locally</h3>
        <p>Highest fixed market prices for old iPhones, Samsung, and laptops in {location}. Better than Cashify.</p>
        <a href="../buyback/sell-old-phone-kochi.html" style="font-weight:700;color:var(--nb);">Check Price Estimator →</a>
      </div>
      <div style="background:var(--w);padding:30px;border-radius:12px;box-shadow:var(--sh-md);">
        <h3 style="color:var(--gd);">Corporate ITAD</h3>
        <p>Strict DPDP Act 2023 compliance and physical hard drive shredding for {location} businesses.</p>
        <a href="../itad-kochi.html" style="font-weight:700;color:var(--nb);">View Business Protocol →</a>
      </div>
      <div style="background:var(--nb);color:var(--w);padding:30px;border-radius:12px;box-shadow:var(--sh-md);">
        <h3 style="color:#fff;">Residential Cleanup</h3>
        <p style="color:rgba(255,255,255,.7);">Clear out dead TVs, appliances, and e-waste safely from your {location} home.</p>
        <a href="../book-free-pickup-kochi.html" class="btn btn-primary" style="margin-top:10px;">Schedule Free Pickup</a>
      </div>
    </div>
  </div>
</section>
</body>
</html>"""

blog_template = """<!DOCTYPE html>
<html lang="en-IN" dir="ltr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title} | EWaste Kochi Traffic Engine</title>
<link rel="stylesheet" href="../assets/css/style.css">
</head>
<body style="background:var(--ow);">
<header class="header" id="nav" style="background:var(--n);border-bottom:1px solid rgba(255,255,255,.05);"><div class="wrap nav-container"><a href="../index.html" class="logo" style="color:var(--w);"><div class="logo-icon">♻️</div>EWaste<em>Kochi</em></a></div></header>

<section style="padding:100px 0;">
  <div class="wrap" style="max-width:800px;background:var(--w);padding:60px;border-radius:12px;box-shadow:var(--sh-md);">
    <div class="breadcrumb" style="margin-bottom:20px;"><a href="../index.html">Home</a><span>›</span><span>Blog</span></div>
    <div style="text-transform:uppercase;font-family:var(--fm);color:var(--tm);font-size:.85rem;margin-bottom:16px;">Traffic Explosion Engine • March 2026</div>
    <h1 style="font-size:2.5rem;line-height:1.2;margin-bottom:30px;">{title}</h1>
    
    <div style="font-size:1.1rem;line-height:1.8;color:var(--nb);">
      <p>This is a high-ROI traffic asset generated to capture top-of-funnel (TOFU) search queries across Kerala. Content deployment is queued for this specific semantic cluster.</p>
      
      <div style="background:#f4f9ff;border-left:4px solid var(--g);padding:20px;margin:40px 0;">
        <h4 style="margin-bottom:10px;">Semantic Mesh Routing</h4>
        <ul style="list-style:none;padding:0;">
          <li style="margin-bottom:8px;">↳ Primary Objective: Informational Authority</li>
          <li style="margin-bottom:8px;">↳ Targeted Action: <a href="../book-free-pickup-kochi.html" style="color:var(--g);font-weight:700;">Convert to Lead Pipeline</a></li>
          <li>↳ Internal Hop: <a href="../itad-kochi.html" style="color:var(--g);font-weight:700;">Pass Link Juice to ITAD Hub</a></li>
        </ul>
      </div>
    </div>
  </div>
</section>
</body>
</html>"""

# ── 3. File Generation ──
sitemap_urls = []
date_str = datetime.datetime.now().strftime("%Y-%m-%d")

print("Initiating Mass Scale Generation Engine...")

# Render 50 Location Pages
for loc in kochi_locations:
    slug = f"ewaste-recycling-{loc.lower()[:15].replace(' ', '-')}.html"
    filepath = os.path.join(locations_dir, slug)
    
    with open(filepath, "w") as f:
        f.write(location_template.format(location=loc))
    sitemap_urls.append(f"https://ewastekochi.com/locations/{slug}")

print(f"✅ Generated {len(kochi_locations)} Location Silo nodes.")

# Render 30 Blog Pages
for slug in blog_slugs:
    filepath = os.path.join(blog_dir, f"{slug}.html")
    title = slug.replace("-", " ").title()
    
    with open(filepath, "w") as f:
        f.write(blog_template.format(title=title))
    sitemap_urls.append(f"https://ewastekochi.com/blog/{slug}.html")

print(f"✅ Generated {len(blog_slugs)} Blog Traffic nodes.")

# ── 4. Sitemap XML Auto-Updater ──
sitemap_path = os.path.join(base_dir, "sitemap.xml")
if os.path.exists(sitemap_path):
    print("Updating sitemap.xml...")
    # Very basic append for the generated URLs
    with open(sitemap_path, "r") as f:
        sitemap_content = f.read()
    
    # Remove the closing tag
    new_sitemap = sitemap_content.replace('</urlset>', '')
    
    for url in sitemap_urls:
        priority = "0.7" if "locations" in url else "0.6"
        new_sitemap += f"  <url><loc>{url}</loc><lastmod>{date_str}</lastmod><changefreq>weekly</changefreq><priority>{priority}</priority></url>\n"
    
    new_sitemap += "</urlset>"
    
    with open(sitemap_path, "w") as f:
        f.write(new_sitemap)
    print(f"✅ Sitemap updated with {len(sitemap_urls)} new semantic URLs.")
else:
    print("Warning: sitemap.xml not found at root.")

print("\n🚀 PHASE 2 TRAFFIC EXPLOSION COMPLETE!")
