import os
from datetime import date

BASE = "/media/hp-ml10/Projects/ewastekochi-production/ewastekochi"
SITE = "https://ewastekochi.com"
TODAY = date.today().isoformat()

TEN_PAGES = [
    ("guides","r2v3-certification-guide-india","R2v3 Certification Guide India | Responsible Recycling 2026","Complete R2v3 responsible recycling certification guide for Indian e-waste recyclers. Requirements, audit process, benefits."),
    ("guides","ewaste-audit-checklist-kerala-2026","E-Waste Audit Checklist Kerala 2026 | KSPCB Compliance","Complete e-waste compliance audit checklist for Kerala businesses. KSPCB, DPDP Act 2023, EPR validation framework."),
    ("compliance","gdpr-ewaste-india-export","GDPR E-Waste Compliance for India IT Exporters | Kerala Guide","GDPR-compliant e-waste disposal guide for Kerala IT exporters handling EU customer data. CoD requirements, legal obligations."),
    ("compliance","sebi-brsr-ewaste-kochi","SEBI BRSR E-Waste Reporting Kochi | Listed Company Guide","SEBI mandatory BRSR e-waste disclosure guidance for Kochi-based listed companies. GRI-aligned metrics and EPR data."),
    ("industries","pharma-ewaste-kochi","Pharma Industry E-Waste Kochi | Lab Equipment Recycling","Pharmaceutical lab equipment recycling Kochi. Analytical instruments, HVAC controllers, cleanroom electronics."),
    ("industries","fintech-data-destruction-kochi","Fintech & NBFC Data Destruction Kochi | RBI Compliant ITAD","Data destruction for Kochi fintech and NBFCs. RBI IT Framework-aligned, secure ITAD, Certificate of Destruction issued."),
    ("recycling","wearable-device-recycling-kochi","Wearable Device Recycling Kochi | Smartwatch Fitness Tracker","Smartwatch, fitness tracker and wearable recycling Kochi. Lithium battery extraction, data wipe, eco disposal."),
    ("collection","bulk-ac-disposal-kochi","Bulk AC Unit Disposal Kochi | Refrigerant-Safe Recycling","AC unit disposal Kochi. Refrigerant recovery, compressor recycling, KSPCB certified. Free pickup for 3+ units."),
    ("trading","sell-old-cisco-networking-kochi","Sell Old Cisco Networking Equipment Kochi | Best Price 2026","Sell old Cisco routers, switches and firewalls in Kochi. Instant valuation, data wipe, free pickup for 5+ units."),
    ("data-security","magnetic-media-degaussing-kochi","Magnetic Media Degaussing Kochi | HDD Tape Floppy Certified","NIST-compliant degaussing for HDDs, magnetic tapes and floppy disks in Kochi. Degaussing certificate issued per unit."),
]

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{h1} | EWaste Kochi</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large">
<meta name="geo.region" content="IN-KL"><meta name="geo.placename" content="Kochi, Kerala, India">
<meta name="date" content="{today}">
<meta property="og:title" content="{h1}"><meta property="og:url" content="{canon}"><meta property="og:type" content="article">
<link rel="alternate" hreflang="en-in" href="{canon}">
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Outfit:wght@400;700;800&display=swap" rel="stylesheet">
<style>
:root{{--bg:#0A0F0C;--bg2:#111A14;--green:#00E664;--white:#E8F2EA;--text:#9BB8A2;--muted:#5A7A62;--border:rgba(0,230,100,.13);--r:14px;}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Outfit',sans-serif;background:var(--bg);color:var(--text);line-height:1.8;overflow-x:hidden}}
a{{color:inherit;text-decoration:none}} .wrap{{max-width:1240px;margin:0 auto;padding:0 24px}}
.section{{padding:70px 0;border-bottom:1px solid var(--border)}}
h1,h2{{font-family:'Bebas Neue',cursive;text-transform:uppercase}}
h1{{font-size:clamp(2.2rem,5vw,4rem);color:var(--white);margin-bottom:16px}}
h2{{font-size:clamp(1.6rem,3vw,2.4rem);color:var(--white);margin-bottom:16px}}
h3{{font-size:1.1rem;color:var(--green);margin:18px 0 8px}} p{{margin-bottom:14px}}
.hero{{min-height:50vh;display:flex;align-items:center;background:radial-gradient(ellipse at 20% 50%,rgba(0,230,100,.08),transparent 60%);border-bottom:1px solid var(--border)}}
.badge{{display:inline-block;background:rgba(0,230,100,.12);border:1px solid rgba(0,230,100,.3);color:var(--green);padding:5px 14px;border-radius:50px;font-size:.75rem;font-weight:700;margin-bottom:16px}}
.btn{{display:inline-flex;align-items:center;gap:8px;font-weight:800;padding:12px 24px;border-radius:10px;font-size:.9rem;margin-top:18px;margin-right:10px}}
.btn-wa{{background:#25D366;color:#fff}} .btn-out{{border:2px solid var(--green);color:var(--green)}}
.faq-item{{background:var(--bg2);border:1px solid var(--border);border-radius:10px;margin-bottom:10px}}
.faq-q{{padding:16px 20px;cursor:pointer;font-weight:700;color:var(--white);display:flex;justify-content:space-between}}
.faq-q::after{{content:"＋";color:var(--green)}} .faq-a{{padding:0 20px 16px;line-height:1.8}}
.nav{{background:rgba(7,16,10,.96);backdrop-filter:blur(20px);border-bottom:1px solid var(--border);position:sticky;top:0;z-index:100}}
.nav-in{{max-width:1240px;margin:0 auto;padding:0 24px;height:60px;display:flex;align-items:center;justify-content:space-between}}
.brand{{font-family:'Bebas Neue';font-size:1.4rem;color:var(--white)}}
.nav-cta{{background:var(--green);color:var(--bg);padding:7px 16px;border-radius:8px;font-weight:800;font-size:.82rem}}
.card{{background:var(--bg2);border:1px solid var(--border);border-radius:var(--r);padding:24px;margin-bottom:18px}}
.silo{{display:flex;flex-wrap:wrap;gap:10px;margin-top:18px}}
.silo a{{background:var(--bg2);border:1px solid var(--border);color:var(--green);padding:8px 14px;border-radius:8px;font-size:.82rem;font-weight:700}}
</style>
<script type="application/ld+json">
{{"@context":"https://schema.org","@graph":[
{{"@type":"LocalBusiness","name":"EWaste Kochi","telephone":"+91-7500555454","aggregateRating":{{"@type":"AggregateRating","ratingValue":"4.9","reviewCount":"312"}},"address":{{"@type":"PostalAddress","addressLocality":"Kochi","addressRegion":"Kerala","addressCountry":"IN"}}}},
{{"@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"Home","item":"{site}"}},{{"@type":"ListItem","position":2,"name":"{folder_label}","item":"{site}/{folder}"}},{{"@type":"ListItem","position":3,"name":"{slug_label}","item":"{canon}"}}]}}
]}}
</script>
</head>
<body>
<nav class="nav"><div class="nav-in"><a class="brand" href="/">♻️ EWaste Kochi</a><a class="nav-cta" href="https://wa.me/917500555454">WhatsApp →</a></div></nav>
<section class="section hero"><div class="wrap">
<span class="badge">✅ KSPCB Authorised · NIST 800-88 · DPDP 2023</span>
<h1>{h1}</h1>
<p style="max-width:680px;font-size:1.05rem;color:var(--white);opacity:.85">{desc}</p>
<a class="btn btn-wa" href="https://wa.me/917500555454">💬 WhatsApp Instant Quote</a>
<a class="btn btn-out" href="/">See All Services →</a>
</div></section>
<section class="section"><div class="wrap">
<h2>Complete Guide: {h1}</h2>
<div class="card"><h3>🔒 Why Certification Matters</h3><p>KSPCB authorisation under E-Waste Management Rules 2022 is mandatory for all recyclers in Kerala. EWaste Kochi is fully authorised, ensuring {slug_label} services comply with all regulatory requirements, including data protection under DPDP Act 2023 and environmental obligations under EPR rules.</p></div>
<div class="card"><h3>📋 DPDP Act 2023 Compliance</h3><p>Every storage device processed receives NIST 800-88-level sanitisation with a Certificate of Destruction listing serial numbers, destruction method, and technician credentials. This CoD is accepted by statutory auditors as evidence of DPDP Act compliance, protecting your organisation from regulatory penalties up to ₹250 crore.</p></div>
<div class="card"><h3>🚚 Our Collection Process</h3><p>Book via WhatsApp → GPS-tracked vehicle to your location → tamper-evident sealing on-site → NIST destruction at our KSPCB facility → digital Certificate of Destruction within 24 hours → ESG weight report issued. Free for 10+ devices in Ernakulam district.</p></div>
<div class="card"><h3>🌍 Environmental Impact</h3><p>Every tonne recycled through EWaste Kochi prevents 4.2 tonnes CO₂ equivalent, recovers 300–400g gold, 2–4kg silver, and 150–200kg copper per tonne of PCBs. Materials flow into India's circular manufacturing chain, supporting Kerala's Haritham initiative and national resource efficiency targets.</p></div>
<div class="card"><h3>💰 Transparent Pricing</h3><p>1–25 devices: ₹299 logistics + ₹80/device · 26–100 devices: Free pickup + ₹60/device · 101–500: ₹45/device all-inclusive · 500+: Custom enterprise rate. Schools, NGOs, government: 100% free. All prices include GST invoice and digital CoD.</p></div>
</div></section>
<section class="section"><div class="wrap">
<h2>Expert FAQs — {slug_label}</h2>
<details class="faq-item"><summary class="faq-q">Is EWaste Kochi KSPCB authorised?</summary><p class="faq-a">Yes. EWaste Kochi is authorised by Kerala State Pollution Control Board under E-Waste Management Rules 2022 and registered with CPCB as dismantler and recycler for all 21 notified categories. Our authorisation is renewable annually and available on request.</p></details>
<details class="faq-item"><summary class="faq-q">Do you provide a Certificate of Destruction?</summary><p class="faq-a">Yes — every job. The CoD includes device serial numbers, NIST 800-88 method, technician ID, KSPCB authorisation reference, and date. Digitally signed, accepted by auditors for DPDP, RBI IT Framework, and SEBI cybersecurity compliance.</p></details>
<details class="faq-item"><summary class="faq-q">How fast can you pick up from our Kochi office?</summary><p class="faq-a">Same-day pickup for bookings before 12 PM, Ernakulam district. 24–48 hours for bulk volume. Emergency 7-day service available. WhatsApp +91 75005 55454 for instant booking.</p></details>
<details class="faq-item"><summary class="faq-q">What is the minimum for free pickup?</summary><p class="faq-a">10+ devices of any type within Ernakulam district. Under 10 devices: ₹299 logistics fee. Schools, NGOs, government bodies: always free regardless of quantity.</p></details>
<details class="faq-item"><summary class="faq-q">Do you issue EPR compliance credits?</summary><p class="faq-a">Yes. We are CPCB-registered, empanelled with multiple PROs. Weight certificates uploaded to CPCB EPMS portal, EPR credit certificates issued within 5 business days. Avoids ₹70/kg penalty for EPR shortfalls.</p></details>
<details class="faq-item"><summary class="faq-q">Can you do on-site data destruction?</summary><p class="faq-a">Yes. Mobile degaussing unit (60+ drives/hour) and portable shredder available at Infopark, SmartCity, KINFRA and any Kochi premises. Drives never leave with data intact. Starts at ₹150/drive for HDD shredding.</p></details>
<details class="faq-item"><summary class="faq-q">Do you provide ESG reporting data?</summary><p class="faq-a">Yes. Every corporate client receives Materials & Impact Report with CO₂ avoided, weight by category, and hazardous material diverted. Structured for GRI, SEBI BRSR, CDP and MSCI ESG questionnaires.</p></details>
<details class="faq-item"><summary class="faq-q">How do you handle SSD destruction?</summary><p class="faq-a">NAND flash-aware protocol: cryptographic erase if supported, then firmware ATA Enhanced Secure Erase, then physical shredding to ≤1mm for NIST Destroy-level. Individual serial certificates issued per SSD.</p></details>
<details class="faq-item"><summary class="faq-q">Can schools and colleges use your service free?</summary><p class="faq-a">Yes, 100% free for educational institutions: free bulk pickup, NIST data destruction, consolidated CoD for records, Green School Certificate for 500kg+ annual volume, plus awareness materials for classes.</p></details>
<details class="faq-item"><summary class="faq-q">What penalties exist for improper e-waste disposal in Kerala?</summary><p class="faq-a">EPR shortfall: ₹70/kg from CPCB. DPDP data breach: up to ₹250 crore. IT Act 43A: corporate liability for breaches from discarded hardware. KSPCB can issue closure orders for illegal dumping. Using EWaste Kochi with CoD documentation is the complete defence against all risks.</p></details>
</div></section>
<section style="background:var(--bg2);padding:50px 0;border-top:1px solid var(--border);">
<div class="wrap"><h2>Related Services</h2>
<div class="silo">
<a href="/">🏠 Home</a>
<a href="/data-destruction-kochi">🔒 Data Destruction</a>
<a href="/data-security/itad-kochi">🏢 ITAD</a>
<a href="/recycling/battery-recycling-kochi">🔋 Battery Recycling</a>
<a href="/collection/ewaste-pickup-kochi">🚚 Free Pickup</a>
<a href="/trading/sell-old-electronics-near-me">💰 Sell Electronics</a>
<a href="/locations/">📍 Kochi Locations</a>
<a href="/data-security/hard-drive-shredding-kochi">💾 HDD Shredding</a>
</div>
<p style="margin-top:24px;font-size:.8rem;color:var(--muted);">♻️ EWaste Kochi — Kerala's #1 KSPCB Authorised E-Waste Hub · <a href="tel:+91-7500555454" style="color:var(--green)">+91 75005 55454</a> · <a href="https://wa.me/917500555454" style="color:#25D366">WhatsApp</a></p>
</div></section>
</body></html>"""

created = 0
for folder, slug, h1, desc in TEN_PAGES:
    out_dir = os.path.join(BASE, folder)
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"{slug}.html")
    if os.path.exists(out_path):
        print(f"  SKIP: {folder}/{slug}.html")
        continue
    canon = f"{SITE}/{folder}/{slug}"
    folder_label = folder.replace("-"," ").title()
    slug_label = slug.replace("-"," ").title()
    html = TEMPLATE.format(h1=h1,desc=desc,canon=canon,today=TODAY,site=SITE,
                           folder=folder,folder_label=folder_label,slug_label=slug_label,slug=slug)
    with open(out_path,"w",encoding="utf-8") as f:
        f.write(html)
    print(f"  ✓ {folder}/{slug}.html")
    created += 1

print(f"\nCreated {created} new pages")

# Quick sitemap rebuild
import glob, re
from pathlib import Path
EXCLUDE = {"__pycache__","gitlab_repo","ewastekochi-production", "node_modules"}
PRIORITY = {"_root":"1.0","locations":"0.9","data-security":"0.9","itad":"0.9","recycling":"0.8","collection":"0.8","disposal":"0.8","trading":"0.8","buyback":"0.8","services":"0.8","industries":"0.7","comparisons":"0.7","compliance":"0.7","guides":"0.7","blog":"0.7","general-waste":"0.6","proof":"0.6"}
FREQ = {"_root":"daily","blog":"weekly"}
files=[]
for root,dirs,fs in os.walk(BASE):
    dirs[:] = [d for d in dirs if d not in EXCLUDE]
    for name in fs:
        if name.endswith(".html"):
            files.append(os.path.join(root,name))
urls=[]
seen=set()
for fp in sorted(files):
    rel = Path(fp).relative_to(BASE)
    parts = list(rel.parts)
    cat = parts[0] if len(parts)>1 else "_root"
    clean = str(rel).replace(".html","")
    url = f"{SITE}/" if clean=="index" else f"{SITE}/{clean}"
    if url in seen: continue
    seen.add(url)
    urls.append((url,PRIORITY.get(cat,"0.6"),FREQ.get(cat,"weekly")))
urls.sort(key=lambda x:(-float(x[1]),x[0]))
lines=['<?xml version="1.0" encoding="UTF-8"?>','<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for url,pri,freq in urls:
    lines+=["  <url>",f"    <loc>{url}</loc>",f"    <lastmod>{TODAY}</lastmod>",f"    <changefreq>{freq}</changefreq>",f"    <priority>{pri}</priority>","  </url>"]
lines.append("</urlset>")
sm = os.path.join(BASE,"sitemap.xml")
with open(sm,"w",encoding="utf-8") as f:
    f.write("\n".join(lines))
print(f"\n✅ sitemap.xml rebuilt — {len(urls)} URLs")
