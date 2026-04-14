import os
import shutil

base_dir = "/media/hp-ml10/Projects/EwasteKochi.com"

# 1. Clean old locations (prevent doorway penalty)
locations_dir = os.path.join(base_dir, "locations")
if os.path.exists(locations_dir):
    shutil.rmtree(locations_dir)
os.makedirs(locations_dir, exist_ok=True)

# 2. Build 8 Unique Location Nodes
locations = {
    "kakkanad": "IT Asset Disposal & Server Decommissioning for Infopark companies.",
    "infopark": "Enterprise-grade NIST 800-88 compliant electronics recycling inside Infopark Phase 1 & 2.",
    "edappally": "Highest B2C buyback rates for iPhones and MacBooks in the Edappally / Lulu Mall region.",
    "thrippunithura": "Our central headquarters. Direct drop-off e-waste facility & data destruction lab.",
    "vyttila": "Serving Vyttila Mobility Hub region with rapid 4-hour commercial IT clearance.",
    "panampilly-nagar": "Discrete, high-end IT asset disposal and premium buyback for South Kochi businesses.",
    "aluva": "Next-day bulk e-waste collection covering Aluva and Angamaly industrial zones.",
    "marine-drive": "Specialized banking and financial sector data destruction along Marine Drive."
}

loc_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"><title>Certified E-Waste Disposal in {name} | EWasteKochi</title>
    <link rel="stylesheet" href="../assets/css/style.css">
    <style>body{{background:#0a0e27;color:#fff;font-family:sans-serif;}} .wrap{{max-width:1200px;margin:0 auto;padding:40px 20px;}} .badge{{background:rgba(0,255,157,0.1);color:#00ff9d;padding:8px 16px;border-radius:20px;font-weight:bold;}}</style>
</head>
<body>
    <div class="wrap">
        <a href="../index.html" style="color:#00ff9d;text-decoration:none;">← Back to Home</a>
        <h1 style="font-size:3rem;margin-top:20px;">Certified E-Waste & ITAD in <span style="color:#00ff9d;">{name}</span></h1>
        <p style="font-size:1.2rem;line-height:1.6;color:#ccc;max-width:800px;">{desc}</p>
        
        <div style="margin:40px 0;padding:30px;background:rgba(255,255,255,0.05);border-radius:12px;border:1px solid rgba(0,255,157,0.2);">
            <h3 style="color:#00ff9d;">Local Service Context: {name}</h3>
            <p style="line-height:1.6;">EWasteKochi provides strictly compliant IT Asset Disposition in {name}, avoiding all gray-market scrap dealers. We follow E-Waste Rules 2022 guidelines and issue verified Certificates of Destruction protecting your firm against DPDP Act penalties (up to ₹250 crore).</p>
            <br>
            <a href="https://wa.me/917500555454" style="background:#00c47a;color:#000;padding:12px 24px;border-radius:30px;text-decoration:none;font-weight:bold;">Request {name} Pickup Track</a>
        </div>
    </div>
</body></html>
"""

for loc, desc in locations.items():
    with open(os.path.join(locations_dir, f"{loc}-ewaste-kochi.html"), "w") as f:
        name_formatted = loc.replace("-", " ").title()
        f.write(loc_template.format(name=name_formatted, desc=desc))


# 3. Build Sub-Buyback Pages
buyback_dir = os.path.join(base_dir, "buyback")
os.makedirs(buyback_dir, exist_ok=True)

bb_pages = [
    ("sell-iphone-kochi", "iPhone 16 to 13 Series", "₹30,000 – ₹1,20,000+"),
    ("sell-macbook-kochi", "MacBook M1/M2/M3", "₹45,000 – ₹95,000+"),
    ("sell-samsung-galaxy-kochi", "Galaxy S24 / Fold", "₹40,000 – ₹85,000"),
]

bb_template = """<!DOCTYPE html><html lang="en"><head><title>Sell {title} in Kochi</title><link rel="stylesheet" href="../assets/css/style.css"></head>
<body style="background:#0a0e27;color:#fff;font-family:sans-serif;">
    <div style="max-width:800px;margin:80px auto;padding:40px;background:rgba(255,255,255,0.05);border-radius:16px;">
        <a href="../sell-old-phone-kochi.html" style="color:#00ff9d;">← Back to Main Estimator</a>
        <h1 style="color:#00ff9d;margin:20px 0;">Premium Buyback: {title}</h1>
        <p>Highest fixed margins in Ernakulam for {title}. Live 2026 pricing range: <strong>{price}</strong> based on cycle count and physical grading.</p>
        <div style="margin-top:30px;padding:20px;border-left:4px solid #00ff9d;background:rgba(0,255,157,0.1);">All devices bypass middle-men apps and are NIST 800-88 wiped locally.</div>
    </div>
</body></html>"""

for slug, title, price in bb_pages:
    with open(os.path.join(buyback_dir, f"{slug}.html"), "w") as f:
        f.write(bb_template.format(title=title, price=price))


# 4. Build Proof Silo
proof_dir = os.path.join(base_dir, "proof")
os.makedirs(proof_dir, exist_ok=True)

proof_html = """<!DOCTYPE html><html lang="en"><head><title>Certificate of Destruction Audit Log | EWasteKochi</title><link rel="stylesheet" href="../assets/css/style.css"></head>
<body style="background:#0a0e27;color:#fff;font-family:sans-serif;">
    <div style="max-width:900px;margin:80px auto;padding:40px;">
        <h1 style="color:#00ff9d;">Audit-Ready Documentation</h1>
        <p>Preview our verified Certificate of Destruction (CoD) format, designed specifically to satisfy DPDP Act 2023 scrutiny, RBI IT audits, and ISO 27001 requirements.</p>
        <div style="margin-top:40px;padding:40px;background:#fff;border-radius:12px;color:#000;">
            <div style="border:12px solid #0a0e27;padding:40px;text-align:center;">
                <h2 style="font-family:serif;letter-spacing:4px;border-bottom:2px solid;padding-bottom:20px;">CERTIFICATE OF DATA DESTRUCTION</h2>
                <div style="text-align:left;margin-top:30px;font-family:mono;">
                    <strong>Certificate ID:</strong> EWK-2026-9042A<br>
                    <strong>Methodology:</strong> NIST SP 800-88 Rev.1 (Clear)<br>
                    <strong>Client Compliance:</strong> DPDP Act 2023 / Section 8<br>
                    <strong>Facility Code:</strong> KEIL / KSPCB Align<br><br>
                    <em>*Redacted Sample for Web View*</em>
                </div>
            </div>
        </div>
    </div>
</body></html>"""

with open(os.path.join(proof_dir, "certificate-samples.html"), "w") as f:
    f.write(proof_html)

print("Python execution complete: Replaced doorways with 8 high-tier Location pages, generated 3 Buyback sub-silos, and created Proof Hub.")
