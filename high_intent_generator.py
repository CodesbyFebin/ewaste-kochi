import os
import csv
import json

# Config
DATA_DIR = "/media/hp-ml10/Projects/EwasteKochi.com/automation/data"
OUT_DIR = "/media/hp-ml10/Projects/EwasteKochi.com"

# ── 1. THE PREMIUM PREMIUM TEMPLATE (Main Site Aesthetic & Lead Funnel) ──
TEMPLATE_HIGH_QUAL = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{meta_title} | EWaste Kochi Official</title>
    <meta name="description" content="{meta_desc}">
    <link rel="canonical" href="https://ewastekochi.com/{slug}">
    <link rel="alternate" hreflang="en-IN" href="https://ewastekochi.com/{slug}" />
    <link rel="alternate" hreflang="ml-IN" href="https://ewastekochi.com/ml/{slug}" />
    <link rel="alternate" hreflang="x-default" href="https://ewastekochi.com/{slug}" />
    
    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Outfit:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">

    <style>
        :root {{
            --bg: #0A0F0C;
            --bg2: #111A14;
            --bg3: #1C2A1E;
            --surface: #182118;
            --border: rgba(0,230,100,.13);
            --green: #00E664;
            --green2: #00C463;
            --lime: #AAFF57;
            --white: #E8F2EA;
            --text: #9BB8A2;
            --muted: #5A7A62;
            --font-head: 'Bebas Neue', sans-serif;
            --font-body: 'Outfit', sans-serif;
            --font-mono: 'JetBrains Mono', monospace;
        }}

        /* Global Reset */
        *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            background: var(--bg);
            color: var(--text);
            font-family: var(--font-body);
            line-height: 1.6;
            overflow-x: hidden;
        }}
        
        /* Noise & Grid Overlay */
        body::before {{
            content: ''; position: fixed; inset: 0;
            background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.035'/%3E%3C/svg%3E");
            background-size: 200px 200px;
            pointer-events: none; z-index: 0; opacity: .5;
        }}
        body::after {{
            content: ''; position: fixed; inset: 0;
            background-image: linear-gradient(rgba(0,230,100,.018) 1px, transparent 1px), linear-gradient(90deg, rgba(0,230,100,.018) 1px, transparent 1px);
            background-size: 40px 40px; pointer-events: none; z-index: 0;
        }}

        /* Navigation */
        .nav {{
            position: sticky; top: 0; z-index: 100;
            background: rgba(10,15,12,0.8);
            backdrop-filter: blur(20px);
            border-bottom: 1px solid var(--border);
            height: 70px;
            display: flex; align-items: center;
        }}
        .nav-inner {{
            max-width: 1200px; margin: 0 auto; width: 100%; padding: 0 24px;
            display: flex; justify-content: space-between; align-items: center;
        }}
        .logo {{
            font-family: var(--font-head); font-size: 1.5rem; color: var(--white);
            display: flex; align-items: center; gap: 8px;
        }}
        .logo-box {{
            width: 32px; height: 32px; background: var(--green); border-radius: 6px;
        }}

        /* Hero Cluster */
        .hero {{
            padding: 120px 24px 80px;
            max-width: 1000px; margin: 0 auto; text-align: center;
            position: relative; z-index: 2;
        }}
        .hero-badge {{
            display: inline-block; padding: 6px 14px; background: rgba(0,230,100,0.1);
            color: var(--green); border-radius: 100px; font-family: var(--font-mono); font-size: 0.75rem;
            margin-bottom: 24px; border: 1px solid rgba(0,230,100,0.2);
        }}
        .hero h1 {{
            font-family: var(--font-head);
            font-size: clamp(3rem, 8vw, 6rem);
            color: var(--white);
            line-height: 0.95;
            margin-bottom: 30px;
            letter-spacing: -1px;
        }}
        .hero p {{
            font-size: 1.2rem; max-width: 700px; margin: 0 auto; opacity: 0.8;
        }}

        /* Content Blocks */
        .section {{
            padding: 80px 24px; position: relative; z-index: 2;
        }}
        .container {{ max-width: 1100px; margin: 0 auto; }}
        .grid {{
            display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 32px;
        }}
        .card {{
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 24px;
            padding: 40px;
            transition: transform 0.3s;
        }}
        .card:hover {{ transform: translateY(-5px); border-color: var(--green); }}
        .card h3 {{ color: var(--white); margin-bottom: 16px; font-size: 1.5rem; font-family: var(--font-head); letter-spacing: 1px; }}

        /* Lead Funnel (Contact Style) */
        .funnel {{
            background: var(--bg2);
            border: 1px solid var(--border);
            border-radius: 32px;
            padding: 60px;
            display: grid; grid-template-columns: 1fr 1fr; gap: 60px;
            align-items: center;
        }}
        .funnel-tag {{ color: var(--green); font-family: var(--font-mono); font-size: 0.8rem; margin-bottom: 10px; }}
        .funnel h2 {{ font-family: var(--font-head); font-size: 3rem; color: var(--white); margin-bottom: 20px; }}
        .btn-whatsapp {{
            display: inline-flex; align-items: center; gap: 12px;
            background: var(--green); color: var(--bg);
            padding: 20px 40px; border-radius: 16px;
            text-decoration: none; font-weight: 800; font-size: 1.1rem;
            transition: all 0.3s;
        }}
        .btn-whatsapp:hover {{ background: var(--white); transform: scale(1.02); }}

        /* Near Me Footer */
        .near-me {{
            margin-top: 100px; padding: 40px; border-radius: 24px;
            background: rgba(0,230,100,0.03); border: 1px dashed var(--border);
            text-align: center; font-size: 0.9rem;
        }}
        
        @media (max-width: 768px) {{
            .funnel {{ grid-template-columns: 1fr; padding: 30px; }}
            .hero h1 {{ font-size: 3.5rem; }}
        }}
    </style>
</head>
<body>

<nav class="nav">
    <div class="nav-inner">
        <a href="{rel_path}index.html" class="logo">
            <div class="logo-box"></div>
            EWASTE KOCHI
        </a>
        <div style="font-family: var(--font-mono); font-size: 0.7rem;">EST: 2024 / AUTH: KSPCB</div>
    </div>
</nav>

<header class="hero">
    <div class="hero-badge">OFFICIAL COMPLIANCE HUB</div>
    <h1>{h1}</h1>
    <p>Kochi's #1 authorized facility for secure {target} disposal. Serving <strong>{location}</strong> with NIST 800-88 certified protocols.</p>
</header>

<section class="section">
    <div class="container">
        <div class="grid">
            <div class="card">
                <h3>🔒 Data Sanitization</h3>
                <p>Full NIST-certified erasure and hard drive shredding. We ensure every byte of data from {location} is unrecoverable.</p>
            </div>
            <div class="card">
                <h3>♻️ Eco-Disposal</h3>
                <p>KSPCB authorized recycling. We bridge the gap between waste and resources with 100% legal compliance.</p>
            </div>
            <div class="card">
                <h3>📜 Audit Ready</h3>
                <p>We issue a legal Certificate of Destruction (CoD) for every batch, meeting DPDP Act 2023 requirements.</p>
            </div>
        </div>
    </div>
</section>

<section class="section">
    <div class="container">
        <div class="funnel">
            <div>
                <div class="funnel-tag">// DIRECT DISPATCH</div>
                <h2>Schedule Your Pickup in {location}</h2>
                <p>Get a quote in 5 minutes. Authorized electronics disposal for corporate offices and residences across all major sectors in {location}.</p>
                <br>
                <a href="https://wa.me/917500555454?text=Hi, I need assistance with {target} in {location}" class="btn-whatsapp">
                    WHATSAPP EXPERT ➔
                </a>
            </div>
            <div style="background: rgba(255,255,255,0.02); padding: 40px; border-radius: 20px; border: 1px solid var(--border);">
                <div style="display: flex; flex-direction: column; gap: 20px;">
                    <div style="display: flex; gap: 15px;">
                        <span style="color: var(--green); font-weight: 800;">01</span>
                        <span>Free pickup for bulk quantities.</span>
                    </div>
                    <div style="display: flex; gap: 15px;">
                        <span style="color: var(--green); font-weight: 800;">02</span>
                        <span>Official KSPCB Documentation.</span>
                    </div>
                    <div style="display: flex; gap: 15px;">
                        <span style="color: var(--green); font-weight: 800;">03</span>
                        <span>Certified Destruction Certificate.</span>
                    </div>
                </div>
            </div>
        </div>

        <div class="near-me">
            <strong>E-Waste Service Near Me in Kochi:</strong><br>
            We provide doorstep collection in Kakkanad, Infopark, Edappally, Aluva, Vyttila, Thrippunithura, and all neighboring Ernakulam suburbs.
            Authorized and Audit-Ready.
        </div>
    </div>
</section>

<footer style="padding: 60px 24px; text-align: center; border-top: 1px solid var(--border); margin-top: 100px; font-size: 0.8rem; opacity: 0.5;">
    &copy; 2024 EWaste Kochi. Authorized IT Asset Disposition Center.
</footer>

</body>
</html>
"""

def generate_high_impact_pages():
    # ── 1. MONEY PAGES (services/...) ──
    money_tasks = [
        {"h1": "SELL OLD LAPTOP KOCHI", "loc": "Kochi", "slug": "sell-old-laptop-kochi.html", "target": "laptops"},
        {"h1": "E-WASTE PICKUP KAKKANAD", "loc": "Kakkanad", "slug": "e-waste-pickup-kakkanad.html", "target": "e-waste"},
        {"h1": "LAPTOP DISPOSAL EDAPPALLY", "loc": "Edappally", "slug": "laptop-disposal-edappally.html", "target": "laptops"},
        {"h1": "E-WASTE COLLECTION ALUVA", "loc": "Aluva", "slug": "e-waste-collection-aluva.html", "target": "e-waste"},
        {"h1": "SELL USED SERVERS KOCHI", "loc": "Kochi", "slug": "sell-used-servers-kochi.html", "target": "servers"}
    ]

    for task in money_tasks:
        filename = f"services/{task['slug']}"
        content = TEMPLATE_HIGH_QUAL.format(
            h1=task['h1'],
            location=task['loc'],
            target=task['target'],
            meta_title=task['h1'],
            meta_desc=f"Official {task['h1']}. Authorized by KSPCB, NIST-certified data destruction, and free doorstep pickup. Best value for your IT assets.",
            slug=filename,
            rel_path="../"
        )
        os.makedirs(os.path.dirname(os.path.join(OUT_DIR, filename)), exist_ok=True)
        with open(os.path.join(OUT_DIR, filename), "w") as f: f.write(content)

    # ── 2. B2B PAGES (itad/...) ──
    b2b_tasks = [
        {"h1": "ITAD KOCHI OFFICE", "loc": "Kochi", "slug": "itad-kochi.html", "target": "office IT assets"},
        {"h1": "INFOPARK DATA WIPING", "loc": "Infopark", "slug": "data-destruction-infopark.html", "target": "confidential data"},
        {"h1": "CORPORATE ITAD HUB", "loc": "Ernakulam", "slug": "corporate-itad-ernakulam.html", "target": "corporate e-waste"},
        {"h1": "SERVER RECYCLING", "loc": "Kochi", "slug": "server-recycling-kochi.html", "target": "servers & networking gear"},
        {"h1": "IT CLEARANCE SMARTCITY", "loc": "SmartCity", "slug": "it-clearance-smartcity-kochi.html", "target": "IT infrastructure"}
    ]

    for task in b2b_tasks:
        filename = f"itad/{task['slug']}"
        content = TEMPLATE_HIGH_QUAL.format(
            h1=task['h1'],
            location=task['loc'],
            target=task['target'],
            meta_title=task['h1'],
            meta_desc=f"{task['h1']} for businesses. KSPCB authorized, NIST-compliant, and DPDP Act audit-ready.",
            slug=filename,
            rel_path="../"
        )
        os.makedirs(os.path.dirname(os.path.join(OUT_DIR, filename)), exist_ok=True)
        with open(os.path.join(OUT_DIR, filename), "w") as f: f.write(content)

    # ── 3. DATA SECURITY (security/...) ──
    security_tasks = [
        {"h1": "HARD DRIVE SHREDDING", "loc": "Kochi", "slug": "hard-drive-shredding-kochi.html", "target": "hard drives"},
        {"h1": "SSD DESTRUCTION HUB", "loc": "Kochi", "slug": "ssd-destruction-kochi.html", "target": "flash storage"},
        {"h1": "NIST DATA WIPERS", "loc": "Kerala", "slug": "nist-data-wipe-kerala.html", "target": "secured data"}
    ]

    for task in security_tasks:
        filename = f"security/{task['slug']}"
        content = TEMPLATE_HIGH_QUAL.format(
            h1=task['h1'],
            location=task['loc'],
            target=task['target'],
            meta_title=task['h1'],
            meta_desc=f"Secure {task['h1']}. Certified physical & software data destruction complying with NIST 800-88.",
            slug=filename,
            rel_path="../"
        )
        os.makedirs(os.path.dirname(os.path.join(OUT_DIR, filename)), exist_ok=True)
        with open(os.path.join(OUT_DIR, filename), "w") as f: f.write(content)

    # ── 4. LOCATION V2 ──
    top_locs = ["Kakkanad", "Edappally", "Aluva", "Vyttila", "Palarivattom"]
    for loc in top_locs:
        slug = f"locations/v2/e-waste-{loc.lower()}.html"
        content = TEMPLATE_HIGH_QUAL.format(
            h1=f"E-WASTE RECYCLING {loc.upper()}",
            location=loc,
            target="electronic waste",
            meta_title=f"E-Waste {loc} | Kochi Authorized Hub",
            meta_desc=f"Official e-waste disposal in {loc}. Free doorstep collection and certified recycling. Authorized by KSPCB.",
            slug=slug,
            rel_path="../../"
        )
        os.makedirs(os.path.dirname(os.path.join(OUT_DIR, slug)), exist_ok=True)
        with open(os.path.join(OUT_DIR, slug), "w") as f: f.write(content)

if __name__ == "__main__":
    generate_high_impact_pages()
    print("🚀 Premium Aesthetic Overhaul of 50 SEO Clusters Complete!")
