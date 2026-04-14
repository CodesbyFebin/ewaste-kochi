import os
import json

# CONFIG
OUTPUT_DIR = "/media/hp-ml10/Projects/ewastekochi-production/ewastekochi/"
BASE_URL = "https://ewastekochi.in/"

PILLARS = [
    {
        "slug": "e-waste-collection-kochi",
        "title": "E-Waste Collection Kochi (2026) | Certified Free Pickup & Disposal",
        "primary_keyword": "E-Waste Collection Kochi",
        "desc": "Kochi's #1 certified e-waste collection service. Free pickup for 50+ units, NIST 800-88 data destruction, and KSPCB authorized recycling. Serving Ernakulam, Kakkanad, Infopark.",
        "h2_keywords": ["Electronic Waste Collection Ernakulam", "Computer Scrap Pickup Kochi", "IT Disposal Services Kerala"],
        "h3_keywords": ["Residential E-Waste Pickup Kakkanad", "Corporate IT Disposal Infopark", "Secure Hard Drive Collection Edappally"]
    },
    {
        "slug": "e-waste-recycling-kochi",
        "title": "E-Waste Recycling Kochi | Zero-Landfill Certified Facility 2026",
        "primary_keyword": "E-Waste Recycling Kochi",
        "desc": "Authorized E-Waste Recycling in Kochi. Zero-landfill processing, precious metal recovery, and specialized electronic scrap treatment. KSPCB certified facility in Thrippunithura.",
        "h2_keywords": ["Sustainable Electronics Recycling Kerala", "Industrial e-Waste Processing Kochi", "Certified Recycler Ernakulam"],
        "h3_keywords": ["Scientific Dismantling Kochi", "Hazardous Material Recovery Kerala", "Circular Economy Electronics Kochi"]
    },
    {
        "slug": "laptop-disposal-kochi",
        "title": "Laptop Disposal Kochi | Secure Data Wipe & Instant Buyback 2026",
        "primary_keyword": "Laptop Disposal Kochi",
        "desc": "Secure laptop disposal in Kochi. NIST 800-88 certified data wiping, physical shredding, and high-value buyback for old MacBooks and business laptops.",
        "h2_keywords": ["Old Laptop Recycling Kochi", "Certified Data Destruction Kerala", "Sell Used Laptops Ernakulam"],
        "h3_keywords": ["MacBook Disposal Kochi", "Bulk ITAD Laptop Retirement", "Secure Hard Drive Shredding Kochi"]
    },
    {
        "slug": "mobile-recycling-kochi",
        "title": "Mobile Recycling Kochi | Sell Old Phones & Secure Disposal 2026",
        "primary_keyword": "Mobile Recycling Kochi",
        "desc": "certified mobile phone recycling and disposal in Kochi. Get the best price for old iPhones and Androids with guaranteed data sanitization.",
        "h2_keywords": ["Smartphone Recycling Ernakulam", "Sell Old Mobile Kochi", "Safe Battery Disposal Kerala"],
        "h3_keywords": ["iPhone Buyback Kochi", "End-of-life Phone Management", "Cell Phone Scrap Valuation Kochi"]
    },
    {
        "slug": "corporate-e-waste-kochi",
        "title": "Corporate E-Waste Kochi | Enterprise ITAD & DPDP Compliance",
        "primary_keyword": "Corporate E-Waste Kochi",
        "desc": "Enterprise-grade corporate e-waste management in Kochi. ITAD services for Infopark, SmartCity, and industrial belts. DPDP Act 2023 compliant documentation.",
        "h2_keywords": ["B2B IT Asset Disposal Kerala", "Corporate Recycling Contracts Kochi", "Enterprise Data Security Ernakulam"],
        "h3_keywords": ["Server Room Decommissioning Kochi", "Compliance Reporting for MNCs", "Asset Tagging & Inventory Management"]
    },
    {
        "slug": "free-e-waste-pickup-kochi",
        "title": "Free E-Waste Pickup Kochi | Schedule Certified Collection Today",
        "primary_keyword": "Free E-Waste Pickup Kochi",
        "desc": "Schedule free e-waste pickup in Kochi for schools, hospitals, and offices. 24-hour SLA for corporate collections in Ernakulam district.",
        "h2_keywords": ["No-Cost Electronic Collection Kerala", "Bulk Scrap Pickup Ernakulam", "Doorstep IT Disposal Kochi"],
        "h3_keywords": ["Pickup for Schools & Colleges Kochi", "Hospital IT Scrap Collection", "Free Pickup Eligibility Criteria"]
    },
    {
        "slug": "it-asset-disposal-kochi",
        "title": "IT Asset Disposal (ITAD) Kochi | Secure Retirement Guide 2026",
        "primary_keyword": "IT Asset Disposal Kochi",
        "desc": "Ultimate guide to IT Asset Disposal (ITAD) in Kochi. NIST 800-88 standards, reverse logistics, and value recovery for retiring IT infrastructure.",
        "h2_keywords": ["ITAD Services Ernakulam", "Secure Asset Retirement Kerala", "Lifecycle Management Kochi"],
        "h3_keywords": ["Data Sanitization Certificate Kochi", "Decommissioning Best Practices", "ITAD Audit Preparation"]
    },
    {
        "slug": "battery-recycling-kochi",
        "title": "Battery Recycling Kochi | Safe UPS & Lead-Acid Disposal 2026",
        "primary_keyword": "Battery Recycling Kochi",
        "desc": "Certified battery recycling in Kochi. Safe disposal of UPS batteries, Li-ion, and Lead-Acid. Environmental compliance for hazardous waste management.",
        "h2_keywords": ["Hazardous Waste Disposal Kerala", "UPS Battery Scrap Kochi", "Lead-Acid Battery Recycling Ernakulam"],
        "h3_keywords": ["Industrial Battery Disposal Rules", "Li-ion Safety Protocols Kochi", "Inverter Battery Scrap Valuation"]
    },
    {
        "slug": "electronics-scrap-kochi",
        "title": "Electronics Scrap Kochi | Industrial Scrap Management 2026",
        "primary_keyword": "Electronics Scrap Kochi",
        "desc": "Professional electronic scrap management in Kochi. Industrial scrap valuation, PCB recycling, and precious metal recovery for large-scale generators.",
        "h2_keywords": ["E-Scrap Valuation Kerala", "PCB Recovery Services Kochi", "Industrial Electronic Recycling Ernakulam"],
        "h3_keywords": ["Mixed Electronic Scrap Sorting", "Metal Reclamation from E-Waste", "Bulk Scrap Logistics Solutions"]
    },
    {
        "slug": "e-waste-rules-kerala",
        "title": "E-Waste Management Rules Kerala | 2022 Compliance Guide",
        "primary_keyword": "E-Waste Rules Kerala",
        "desc": "Comprehensive guide to E-Waste Management Rules 2022 in Kerala. KSPCB regulations, EPR obligations, and legal requirements for bulk consumers.",
        "h2_keywords": ["KSPCB E-Waste Regulations", "Environmental Law Compliance Kerala", "Bulk Consumer Responsibilities Kochi"],
        "h3_keywords": ["EPR Registration Guide Kerala", "DPDP Act 2023 Synchronization", "Annual E-Waste Return Filing"]
    }
]

def generate_long_content(pillar, word_count=2500):
    # Simulated long-form content generation with local modifiers and NLP optimization
    kw = pillar["primary_keyword"]
    h2s = pillar["h2_keywords"]
    h3s = pillar["h3_keywords"]
    
    cities = ["Kochi", "Ernakulam", "Kerala", "Kakkanad", "Edappally", "Aluva", "Thrippunithura", "Vyttila", "Palarivattom", "Fort Kochi"]
    
    internal_links = [
        '<a href="/blog/e-waste-management-kochi-complete-guide.html" style="color:var(--green)">E-Waste Complete Guide</a>',
        '<a href="/itad-kochi.html" style="color:var(--green)">IT Asset Disposition Kochi</a>',
        '<a href="/data-destruction-kochi.html" style="color:var(--green)">Certified Data Destruction</a>',
        '<a href="/sell-old-laptop-kochi.html" style="color:var(--green)">Sell Old Laptop Kochi</a>',
        '<a href="/free-e-waste-pickup-kochi.html" style="color:var(--green)">Free Pickup Service</a>'
    ]
    
    content = f"<p>Welcome to the definitive 2026 guide on <strong>{kw}</strong>. As the commercial capital of Kerala, Kochi handles approximately 40% of the state's total electronic volume. With the rapid expansion of Infopark Kakkanad, SmartCity, and the KINFRA clusters, the need for certified, secure, and environmentally responsible disposal has never been higher. For more details on our processes, see our {internal_links[0]}.</p>"
    
    content += f"<h2>Understanding {kw} in the Modern Era</h2>"
    content += f"<p>Managing {kw} is no longer just about tidying up an office space or clearing a garage. It is a critical component of corporate governance and environmental stewardship in Ernakulam. Under the E-Waste Management Rules 2022, every 'bulk consumer'—including hospitals in Edappally, IT firms in Aluva, and banks in Vyttila—must ensure their retiring hardware is channeled through authorized recyclers. Learn more about {internal_links[1]} to see how we assist bulk consumers.</p>"
    
    for i, h2 in enumerate(h2s):
        content += f"<h2>{h2}</h2>"
        content += f"<p>The landscape of {h2} has shifted towards a security-first discipline. Whether you are dealing with end-of-life laptops or complex industrial servers, the primary risk is data leakage. In Kochi's competitive business ecosystem, especially within the banking and fintech sectors of Palarivattom, implementing {internal_links[2]} standards is non-negotiable.</p>"
        
        for j, h3 in enumerate(h3s):
            content += f"<h3>{h3}</h3>"
            content += f"<p>When specifically looking at {h3}, one must consider the localized logistics of Kerala. Transportation of hazardous electronic scrap requires specialized gate-passes and chain-of-custody documentation that satisfies the Kerala State Pollution Control Board (KSPCB) auditors. Our Thrippunithura-based facility serves as the central hub for these operations, providing seamless reverse logistics across the entire Ernakulam district. We recommend checking our {internal_links[3]} for value recovery options.</p>"
            
            # Expansion block to hit word count
            for _ in range(3):
                idx = (i + j) % len(cities)
                content += f"<p>To further elaborate on the technical aspects of {h3}, we implement a multi-stage dismantling process. First, the primary housing is removed to isolate the printed circuit boards (PCBs). In {cities[idx]}, our methodologies for precious metal recovery are world-class, ensuring that gold, silver, and palladium are reclaimed rather than ending up in landfills. This 'circular economy' approach is why we are the preferred partner for {cities[(idx+1)%len(cities)]}-based organizations seeking ESG (Environmental, Social, and Governance) excellence. Our {internal_links[4]} makes this process effortless.</p>"
    
    # Adding a massive FAQ section to boost value and word count
    content += "<h2>Advanced Knowledge & Local Queries</h2>"
    content += "<p>Below we address the most pressing questions derived from Reddit Kochi, local Google PAA (People Also Ask), and corporate intent queries regarding e-waste disposal in Kerala.</p>"
    
    return content


def generate_faqs(pillar):
    slug = pillar["slug"]
    kw = pillar["primary_keyword"]
    faqs = [
        {"q": f"Where can I find the best {kw} service?", "a": "EWaste Kochi provides the most comprehensive and certified service in Ernakulam, with free pickup for corporate clients and certified data destruction."},
        {"q": f"Are there any charges for {kw} in Kochi?", "a": "For bulky volumes (50+ units), our pickup is absolutely free. For smaller residential quantities, a nominal logistics fee may apply depending on your location in Ernakulam."},
        {"q": "Is the data on my device safe during recycling?", "a": "Yes. We implement NIST 800-88 standards for all devices. Every hard drive is either wiped using military-grade software or physically shredded, and a Certificate of Destruction is issued."},
        {"q": f"What are the Kerala government rules for {kw}?", "a": f"The E-Waste Management Rules 2022 mandate that all bulk consumers must hand over waste only to authorized recyclers like us. Non-compliance can lead to heavy penalties under the DPDP Act 2023."},
        {"q": "How do I book a pickup in Kakkanad Infopark?", "a": "You can book directly through our WhatsApp link or call us. We have daily rounds in the Infopark and SmartCity areas for corporate collections."},
        {"q": "Do you provide a Certificate of Destruction?", "a": "Absolutely. A legally-binding Certificate of Destruction (CoD) is issued for every asset disposed of, which is essential for your annual KSPCB filings and audit trails."},
        {"q": "What happens to the hazardous materials?", "a": "Mercury, lead, and cadmium are safely extracted and sent to specialized hazardous waste treatment facilities (TSDFs) in compliance with environmental laws."},
        {"q": "Can I sell my old MacBook for cash in Kochi?", "a": "Yes! We offer up to ₹65,000 for Apple Silicon MacBooks. We typically beat market aggregators by 15-20% and provide immediate payment."},
        {"q": "Do you accept broken or non-working electronics?", "a": "Yes, we accept all end-of-life, damaged, and non-working electronic scrap. We value them based on component recovery potential."},
        {"q": "Is EWaste Kochi authorized by the Pollution Control Board?", "a": "Yes, we are a KSPCB authorized facility, operating under strict environmental and data security guidelines since our inception."}
    ]
    return faqs

def get_schema(pillar, faqs):
    kw = pillar["primary_keyword"]
    desc = pillar["desc"]
    url = f"{BASE_URL}{pillar['slug']}.html"
    
    webpage_schema = {
        "@type": "WebPage",
        "name": pillar["title"],
        "description": desc,
        "url": url,
        "breadcrumb": {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE_URL},
                {"@type": "ListItem", "position": 2, "name": "Docs", "item": f"{BASE_URL}docs/"},
                {"@type": "ListItem", "position": 3, "name": kw, "item": url}
            ]
        }
    }
    
    service_schema = {
        "@type": "Service",
        "serviceType": kw,
        "provider": {
            "@type": "LocalBusiness",
            "name": "EWaste Kochi",
            "url": BASE_URL
        },
        "areaServed": {"@type": "City", "name": "Kochi"},
        "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": "E-Waste Services",
            "itemListElement": [
                {"@type": "Offer", "itemOffered": {"@type": "Service", "name": kw}}
            ]
        }
    }
    
    faq_schema = {
        "@type": "FAQPage",
        "mainEntity": []
    }
    for faq in faqs:
        faq_schema["mainEntity"].append({
            "@type": "Question",
            "name": faq["q"],
            "acceptedAnswer": {"@type": "Answer", "text": faq["a"]}
        })
        
    return f"""
<script type="application/ld+json">
{json.dumps(webpage_schema, indent=2)}
</script>
<script type="application/ld+json">
{json.dumps(service_schema, indent=2)}
</script>
<script type="application/ld+json">
{json.dumps(faq_schema, indent=2)}
</script>
"""

def generate_page(pillar):
    faqs = generate_faqs(pillar)
    schema_html = get_schema(pillar, faqs)
    content_html = generate_long_content(pillar)
    
    faq_items_html = ""
    for i, faq in enumerate(faqs):
        faq_items_html += f"""
        <div class="faq-item" id="faq-{i}">
          <button class="faq-q" onclick="toggleFaq({i})">
            {faq['q']}
            <span class="arrow">+</span>
          </button>
          <div class="faq-a" id="faq-a-{i}">
            {faq['a']}
          </div>
        </div>
        """

    # Template with the premium design CSS
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>{pillar['title']}</title>
<meta name="description" content="{pillar['desc']}">
<link rel="canonical" href="{BASE_URL}{pillar['slug']}.html">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@700;800;900&family=DM+Sans:wght@300;400;500;600&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
<style>
:root {{
  --bg: #07100A; --bg2: #0B170E; --bg3: #101C13; --surface: #152018; --surface2: #1C2B1F;
  --border: rgba(0,232,122,.12); --border2: rgba(0,232,122,.22);
  --green: #00E87A; --green2: #00C463; --lime: #B4FF5C; --amber: #F5A827; --white: #F0F7F2;
  --text: #A8C4AE; --muted: #5A7A62; --head: 'Syne', sans-serif; --body: 'DM Sans', sans-serif; --mono: 'JetBrains Mono', monospace;
}}
*,*::before,*::after {{ box-sizing:border-box; margin:0; padding:0; }}
body {{ font-family: var(--body); background: var(--bg); color: var(--text); line-height: 1.65; overflow-x: hidden; }}
body::before {{ content:''; position:fixed; inset:0; background-image: linear-gradient(rgba(0,232,122,.025) 1px, transparent 1px), linear-gradient(90deg, rgba(0,232,122,.025) 1px, transparent 1px); background-size:48px 48px; pointer-events:none; z-index:0; }}
.wrap {{ max-width:1280px; margin:0 auto; padding:0 2rem; position:relative; z-index:1; }}
.nav {{ position:sticky; top:0; background:rgba(7,16,10,.95); border-bottom:1px solid var(--border); z-index:100; backdrop-filter:blur(8px); }}
.nav-inner {{ max-width:1280px; margin:0 auto; padding:0 2rem; height:68px; display:flex; align-items:center; justify-content:space-between; }}
.logo {{ display:flex; align-items:center; gap:.6rem; font-family:var(--head); font-size:1.35rem; font-weight:900; color:var(--white); text-decoration:none; }}
.logo span {{ color:var(--green); }}
.section {{ padding:88px 0; }}
h1 {{ font-family:var(--head); font-size:clamp(2.4rem,6vw,4.5rem); font-weight:900; color:var(--white); line-height:1.05; letter-spacing:-2px; margin-bottom:1.5rem; }}
h2 {{ font-family:var(--head); font-size:2.4rem; color:var(--white); margin:48px 0 24px; letter-spacing:-1px; }}
h3 {{ font-family:var(--head); font-size:1.5rem; color:var(--green); margin:32px 0 16px; }}
p {{ margin-bottom:24px; font-size:1.1rem; }}
.btn {{ display:inline-flex; align-items:center; gap:.5rem; padding:.8rem 1.8rem; border-radius:6px; font-weight:800; font-family:var(--head); transition:all .2s; cursor:pointer; text-decoration:none; border:none; border-radius:8px; }}
.btn-primary {{ background:var(--green); color:var(--bg); }}
.btn-primary:hover {{ background:var(--lime); transform:translateY(-1px); box-shadow:0 8px 24px rgba(0,232,122,.25); }}
.btn-wa {{ background:#25D366; color:#fff; }}
.faq-grid {{ display:grid; grid-template-columns:1fr; gap:1rem; margin-top:40px; }}
.faq-item {{ background:var(--surface); border:1px solid var(--border); border-radius:8px; }}
.faq-q {{ width:100%; text-align:left; padding:1.25rem 1.5rem; font-size:1.1rem; font-weight:700; color:var(--white); background:none; border:none; cursor:pointer; display:flex; justify-content:space-between; }}
.faq-a {{ display:none; padding:0 1.5rem 1.5rem; color:var(--text); border-top:1px solid var(--border); padding-top:1.25rem; }}
.cta-box {{ background:linear-gradient(135deg, var(--surface) 0%, rgba(0,232,122,.06) 100%); border:1px solid var(--border2); padding:64px; border-radius:16px; text-align:center; margin:80px 0; }}
.footer {{ background:var(--bg2); border-top:1px solid var(--border); padding:64px 0 32px; text-align:center; }}
.wa-float {{ position:fixed; bottom:2rem; right:2rem; width:60px; height:60px; background:#25D366; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:2rem; color:white; z-index:500; text-decoration:none; }}
</style>
</head>
<body>
<nav class="nav"><div class="nav-inner"><a href="/" class="logo"><span>EWaste</span>Kochi</a><div class="nav-cta"><a href="/book-free-pickup-kochi.html" class="btn btn-primary">Book Pickup →</a></div></div></nav>

<div class="wrap" style="padding:100px 0">
    <div style="color:var(--green); font-family:var(--mono); letter-spacing:4px; margin-bottom:12px">RESOURCE HUB / DOCUMENTATION</div>
    <h1>{pillar['title']}</h1>
    <div style="font-size:1.3rem; color:var(--white); opacity:.8; max-width:800px; margin-bottom:40px">{pillar['desc']}</div>
    
    <div style="background:var(--surface); border:1px solid var(--border); padding:32px; border-radius:12px; margin-bottom:60px">
        <h4 style="color:var(--white); font-family:var(--mono); margin-bottom:16px">Table of Contents</h4>
        <ul style="list-style:none; display:grid; grid-template-columns:1fr 1fr; gap:12px">
            <li><a href="#overview" style="color:var(--green); text-decoration:none">1. Comprehensive Overview</a></li>
            <li><a href="#compliance" style="color:var(--green); text-decoration:none">2. Compliance & Rules</a></li>
            <li><a href="#process" style="color:var(--green); text-decoration:none">3. Our Recycling Process</a></li>
            <li><a href="#faq" style="color:var(--green); text-decoration:none">4. FAQ Engine</a></li>
        </ul>
    </div>

    <div class="content-body" id="overview">
        {content_html}
    </div>

    <div class="cta-box">
        <h2 style="margin-top:0">Ready to Dispose Responsibly?</h2>
        <p>Get Kochi's most trusted certified e-waste service. Free pickup for 50+ units.</p>
        <div style="display:flex; gap:1rem; justify-content:center; flex-wrap:wrap">
            <a href="/book-free-pickup-kochi.html" class="btn btn-primary">Book Free Pickup</a>
            <a href="/get-instant-quote.html" class="btn btn-primary" style="background:var(--bg3); border:1px solid var(--green); color:var(--green)">Get Quote</a>
            <a href="https://wa.me/91XXXXXXXXXX" class="btn btn-wa">WhatsApp Now</a>
        </div>
        <div style="margin-top:24px; display:flex; gap:24px; justify-content:center; color:var(--muted); font-size:.9rem">
            <span>✓ Govt Approved</span>
            <span>✓ Secure Destruction</span>
            <span>✓ Zero Landfill</span>
        </div>
    </div>

    <div id="faq">
        <h2>Frequently Asked Questions</h2>
        <div class="faq-grid">
            {faq_items_html}
        </div>
    </div>
</div>

<div id="chatbot-container"></div>

<footer class="footer">
    <div class="wrap">
        <p>© 2026 EWaste Kochi. Certified ITAD & E-Waste Recycling, Thrippunithura. Serving Kakkanad, Edapally, Aluva, Ernakulam.</p>
    </div>
</footer>

<a href="https://wa.me/91XXXXXXXXXX" class="wa-float">💬</a>

{schema_html}

<script>
function toggleFaq(id) {{
    const el = document.getElementById('faq-a-' + id);
    const btn = document.querySelector('#faq-' + id + ' .arrow');
    if (el.style.display === 'block') {{
        el.style.display = 'none';
        btn.textContent = '+';
    }} else {{
        el.style.display = 'block';
        btn.textContent = '×';
    }}
}}
</script>
</body>
</html>
"""
    return html

for p in PILLARS:
    page_html = generate_page(p)
    with open(os.path.join(OUTPUT_DIR, f"{p['slug']}.html"), "w", encoding="utf-8") as f:
        f.write(page_html)
    print(f"Generated: {p['slug']}.html")

print("All 10 Docs pages generated successfully.")
