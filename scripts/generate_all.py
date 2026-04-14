#!/usr/bin/env python3
"""
EWasteKochi.com — Full Site Generator
Generates all 120+ pages using shared templates, CSS, and JS.
Run from the ewastekochi/ root directory:
    python scripts/generate_all.py
"""
import os, json, re
from datetime import datetime

# ── CONFIG ──────────────────────────────────────────────────────────────
BASE_URL = "https://ewastekochi.com"
PHONE = "+91-9876-543-210"
WA_NUM = "919876543210"
EMAIL = "info@ewastekochi.com"
ADDRESS = "710A Hill Palace Rd, East Fort Gate, Thrippunithura, Kochi 682301"
CSS_PATH = "/css/style.css"
JS_PATH = "/js/main.js"

# ── NAV + FOOTER SHARED HTML ────────────────────────────────────────────
NAV_HTML = """
<div class="topbar" aria-hidden="true">
  <div class="topbar-inner">
    <span>♻️ FREE CORPORATE PICKUP — 50+ UNITS ACROSS KOCHI</span>
    <span>🔒 NIST 800-88 CERTIFIED DATA DESTRUCTION</span>
    <span>📋 CERTIFICATE OF DESTRUCTION — EVERY DEVICE</span>
    <span>⚖️ DPDP ACT 2023 COMPLIANT ITAD</span>
    <span>📞 24/7 CORPORATE EMERGENCY: +91-9876-543-210</span>
    <span>♻️ FREE CORPORATE PICKUP — 50+ UNITS ACROSS KOCHI</span>
    <span>🔒 NIST 800-88 CERTIFIED DATA DESTRUCTION</span>
    <span>📋 CERTIFICATE OF DESTRUCTION — EVERY DEVICE</span>
    <span>⚖️ DPDP ACT 2023 COMPLIANT ITAD</span>
    <span>📞 24/7 CORPORATE EMERGENCY: +91-9876-543-210</span>
  </div>
</div>
<nav class="nav" id="main-nav">
  <div class="nav-inner">
    <a href="/" class="nav-logo"><div class="nav-logo-icon">♻️</div>EWaste Kochi</a>
    <div class="nav-links">
      <a href="/itad-kochi.html" class="nav-link">ITAD</a>
      <a href="/data-destruction-kochi.html" class="nav-link">Data Destruction</a>
      <a href="/sell-old-laptop-kochi.html" class="nav-link">Sell Laptop</a>
      <a href="/sell-old-phone-kochi.html" class="nav-link">Sell Phone</a>
      <a href="/compliance/dpdp-act-2023-penalties.html" class="nav-link">Compliance</a>
      <a href="/blog/" class="nav-link">Resources</a>
      <a href="/contact.html" class="nav-link">Contact</a>
    </div>
    <div style="display:flex;gap:10px;align-items:center">
      <a href="https://wa.me/919876543210?text=Hi%2C+I+need+a+quote" class="nav-wa btn" target="_blank">💬 WhatsApp</a>
      <a href="/get-instant-quote.html" class="nav-cta">📋 Free Quote</a>
    </div>
    <button class="hamburger" onclick="toggleMobileNav()" aria-label="Menu"><span></span><span></span><span></span></button>
  </div>
</nav>
<div class="nav-overlay" id="nav-overlay" onclick="closeMobileNav()"></div>
<div class="mobile-nav" id="mobile-nav">
  <button class="mobile-nav-close" onclick="closeMobileNav()">✕</button>
  <a href="/itad-kochi.html" class="mobile-nav-link" onclick="closeMobileNav()">Corporate ITAD <span>→</span></a>
  <a href="/data-destruction-kochi.html" class="mobile-nav-link" onclick="closeMobileNav()">Data Destruction <span>→</span></a>
  <a href="/sell-old-laptop-kochi.html" class="mobile-nav-link" onclick="closeMobileNav()">Sell Laptop <span>→</span></a>
  <a href="/sell-old-phone-kochi.html" class="mobile-nav-link" onclick="closeMobileNav()">Sell Phone <span>→</span></a>
  <a href="/compliance/dpdp-act-2023-penalties.html" class="mobile-nav-link" onclick="closeMobileNav()">Compliance <span>→</span></a>
  <a href="/faq.html" class="mobile-nav-link" onclick="closeMobileNav()">FAQs <span>→</span></a>
  <a href="/contact.html" class="mobile-nav-link" onclick="closeMobileNav()">Contact <span>→</span></a>
  <a href="/get-instant-quote.html" class="mobile-nav-cta" onclick="closeMobileNav()">📋 Get Free Quote</a>
</div>
"""

FOOTER_HTML = """
<footer>
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <div class="footer-brand"><div class="footer-brand-icon">♻️</div>EWaste Kochi</div>
        <div class="footer-desc">Kerala's most trusted certified ITAD and e-waste recycling facility. KSPCB authorization compliant. NIST 800-88 and DoD 5220.22-M methodology. Certificate of Destruction every device. Serving all Ernakulam district since 2019.</div>
        <div class="footer-badges">
          <span class="footer-badge">KSPCB Compliant</span>
          <span class="footer-badge">NIST 800-88</span>
          <span class="footer-badge">DoD 5220.22-M</span>
          <span class="footer-badge">DPDP Act</span>
          <span class="footer-badge">EPR Registered</span>
        </div>
      </div>
      <div>
        <div class="footer-heading">Services</div>
        <div class="footer-links">
          <a href="/itad-kochi.html" class="footer-link">Corporate ITAD</a>
          <a href="/data-destruction-kochi.html" class="footer-link">Data Destruction</a>
          <a href="/hard-drive-shredding-kochi.html" class="footer-link">Hard Drive Shredding</a>
          <a href="/sell-old-laptop-kochi.html" class="footer-link">Sell Old Laptop</a>
          <a href="/sell-old-phone-kochi.html" class="footer-link">Sell Old Phone</a>
          <a href="/office-clearance.html" class="footer-link">Office Clearance</a>
          <a href="/server-disposal-kochi.html" class="footer-link">Server Disposal</a>
        </div>
      </div>
      <div>
        <div class="footer-heading">Compliance</div>
        <div class="footer-links">
          <a href="/compliance/dpdp-act-2023-penalties.html" class="footer-link">DPDP Act 2023</a>
          <a href="/compliance/nist-800-88-explained.html" class="footer-link">NIST SP 800-88</a>
          <a href="/compliance/dod-5220-22m-guide.html" class="footer-link">DoD 5220.22-M</a>
          <a href="/compliance/certificate-verification.html" class="footer-link">Verify CoD</a>
          <a href="/compliance/chain-of-custody.html" class="footer-link">Chain of Custody</a>
          <a href="/blog/" class="footer-link">Knowledge Hub</a>
          <a href="/faq.html" class="footer-link">FAQs</a>
        </div>
      </div>
      <div>
        <div class="footer-heading">Contact</div>
        <div class="footer-contact-item"><span class="footer-contact-icon">📍</span><span>710A Hill Palace Rd, East Fort Gate, Thrippunithura, Kochi 682301</span></div>
        <div class="footer-contact-item"><span class="footer-contact-icon">📞</span><a href="tel:+919876543210" style="color:var(--muted)">+91-9876-543-210</a></div>
        <div class="footer-contact-item"><span class="footer-contact-icon">✉️</span><a href="mailto:info@ewastekochi.com" style="color:var(--muted)">info@ewastekochi.com</a></div>
        <div class="footer-contact-item"><span class="footer-contact-icon">⏰</span><span>Mon–Sat 8AM–8PM · Sun 10AM–4PM · Corporate 24/7</span></div>
      </div>
    </div>
    <div class="footer-bottom">
      <div class="footer-copy">© 2026 EWaste Kochi. All rights reserved. Certified ITAD & E-Waste Recycling, Kochi, Kerala.</div>
      <div class="footer-legal">
        <a href="/privacy-policy.html">Privacy Policy</a>
        <a href="/terms-of-service.html">Terms</a>
        <a href="/refund-policy.html">Refund Policy</a>
      </div>
    </div>
  </div>
</footer>
<div class="float-ctas">
  <a href="tel:+919876543210" class="float-btn float-call" title="Call">📞</a>
  <a href="https://wa.me/919876543210?text=Hi%2C+I+need+a+quote+for+e-waste+services" class="float-btn float-wa" title="WhatsApp" target="_blank">💬</a>
</div>
<div class="chatbot-wrap" id="chatbot">
  <button class="chat-toggle" onclick="toggleChat()" id="chat-toggle-btn" title="Chat with us">💬<span class="chat-badge" id="chat-badge" style="display:none">1</span></button>
  <div class="chat-window" id="chat-window">
    <div class="chat-header">
      <div class="chat-avatar">🤖</div>
      <div class="chat-header-info"><div class="chat-agent-name">EWaste Kochi Assistant</div><div class="chat-status"><span class="chat-status-dot"></span>Online · replies instantly</div></div>
      <button class="chat-close" onclick="toggleChat()">✕</button>
    </div>
    <div class="chat-messages" id="chat-messages"></div>
    <div class="chat-options" id="chat-options"></div>
    <div class="chat-input-row">
      <input type="text" class="chat-input" id="chat-input" placeholder="Type your question..." onkeydown="if(event.key==='Enter')sendChatMsg()">
      <button class="chat-send" onclick="sendChatMsg()">➤</button>
    </div>
  </div>
</div>
"""

LOCAL_SCHEMA = json.dumps({
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "name": "EWaste Kochi",
    "url": "https://ewastekochi.com/",
    "telephone": "+91-9876543210",
    "email": "info@ewastekochi.com",
    "address": {"@type": "PostalAddress", "streetAddress": "710A Hill Palace Rd, East Fort Gate, Kannankulangara", "addressLocality": "Thrippunithura", "addressRegion": "Kerala", "postalCode": "682301", "addressCountry": "IN"},
    "geo": {"@type": "GeoCoordinates", "latitude": 9.9390, "longitude": 76.3590},
    "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"], "opens": "08:00", "closes": "20:00"},{"@type": "OpeningHoursSpecification", "dayOfWeek": "Sunday", "opens": "10:00", "closes": "16:00"}],
    "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.9", "reviewCount": "143"},
    "areaServed": ["Kochi","Ernakulam","Kakkanad","Edapally","Thrippunithura","Aluva","Vyttila"]
}, indent=2)


def html_page(title, meta_desc, canonical, schema_extra=None, css_depth="/", js_depth="/", body_content="", breadcrumb=""):
    """Wrap content in the full page shell."""
    css = css_depth + "css/style.css"
    js = js_depth + "js/main.js"
    schema = LOCAL_SCHEMA
    if schema_extra:
        schema = schema_extra
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{meta_desc}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{BASE_URL}{canonical}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{meta_desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{BASE_URL}{canonical}">
<meta name="twitter:card" content="summary_large_image">
<link rel="dns-prefetch" href="//fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{css}">
<script type="application/ld+json">
{schema}
</script>
</head>
<body>
{NAV_HTML}
{breadcrumb}
{body_content}
{FOOTER_HTML}
<script src="{js}"></script>
</body>
</html>"""


def breadcrumb_html(crumbs):
    """crumbs = [("Home","/"), ("Blog","/blog/"), ("Article Title", None)]"""
    items = []
    for label, href in crumbs:
        if href:
            items.append(f'<a href="{href}">{label}</a>')
        else:
            items.append(f'<span style="color:var(--white)">{label}</span>')
    return f'<div class="wrap"><div class="breadcrumb">' + '<span class="breadcrumb-sep">/</span>'.join(items) + '</div></div>'


def write(path, content):
    os.makedirs(os.path.dirname(path) if os.path.dirname(path) else ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✓ {path}")


# ── LOCATION PAGE DATA ────────────────────────────────────────────────────
LOCATIONS = [
    ("Kakkanad", "kakkanad", "8 km", "Infopark, SmartCity, KSTP"),
    ("Infopark", "infopark", "8 km", "Phase 1, Phase 2, TCS, Wipro, UST campus"),
    ("Edapally", "edappally", "12 km", "Lulu Mall area, NH 66 corridor"),
    ("Vyttila", "vyttila", "5 km", "Vyttila Hub, mobility hub area"),
    ("Thrippunithura", "thrippunithura", "0 km — Main Facility", "Hill Palace, East Fort Gate"),
    ("Aluva", "aluva", "18 km", "CUSAT, KINFRA, SmartCity Aluva"),
    ("Palarivattom", "palarivattom", "10 km", "MG Road junction, Kadavanthra"),
    ("Kaloor", "kaloor", "7 km", "Jawaharlal Nehru Stadium area"),
    ("Marine Drive", "marine-drive", "6 km", "MG Road, Ernakulam South"),
    ("Fort Kochi", "fort-kochi", "14 km", "Mattancherry, Jew Town, Heritage zone"),
    ("Angamaly", "angamaly", "28 km", "NH 544, airport industrial zone"),
    ("Perumbavoor", "perumbavoor", "22 km", "Industrial estates, plywood hub"),
    ("Kalamassery", "kalamassery", "14 km", "KINFRA Hi-Tech Park, Eloor industrial"),
    ("Vytilla", "vytilla-hub", "5 km", "Water Metro hub, Kundannoor"),
    ("Maradu", "maradu", "8 km", "NH Bypass, Thammanam area"),
    ("Kadavanthra", "kadavanthra", "9 km", "Panampilly Nagar, Elamkulam"),
    ("Willingdon Island", "willingdon-island", "10 km", "Cochin Port, Bolgatty"),
    ("Cheranallur", "cheranallur", "7 km", "Airport Road, Nedumbassery"),
    ("Vaduthala", "vaduthala", "11 km", "Njarackal, Mulavukad area"),
    ("Alwaye", "alwaye", "18 km", "FACT, Travancore Cochin industrial"),
]

# Additional 32 pincode-based pages
ERNAKULAM_PINCODES = [
    ("682001", "Ernakulam North"), ("682002", "Ernakulam South"), ("682003", "Mattancherry"),
    ("682004", "Willingdon Island"), ("682005", "Fort Kochi"), ("682006", "Cherai"),
    ("682007", "Njarackal"), ("682008", "Mulavukad"), ("682009", "Thevara"),
    ("682010", "Kalamassery"), ("682011", "Edapally"), ("682012", "Kakkanad"),
    ("682013", "Maradu"), ("682014", "Vyttila"), ("682015", "Kaloor"),
    ("682016", "Palarivattom"), ("682017", "Vytilla Hub"), ("682018", "Kadavanthra"),
    ("682019", "Girinagar"), ("682020", "Panampilly Nagar"), ("682021", "Pachalam"),
    ("682022", "Cheranallur"), ("682023", "Vaduthala"), ("682024", "Elamkulam"),
    ("682025", "Tripunithura North"), ("682026", "Tripunithura South"), ("682027", "Piravom"),
    ("682028", "Mookkannoor"), ("682029", "North Paravur"), ("682030", "Aluva North"),
    ("682031", "Aluva South"), ("682032", "Perumbavoor East"),
]

# ── BLOG ARTICLES ────────────────────────────────────────────────────────
BLOG_ARTICLES = [
    ("is-formatting-enough-delete-data.html",
     "Is Formatting Your Hard Drive Enough to Delete Data?",
     "Is formatting a hard drive enough to permanently delete data? No — learn why NIST 800-88 certified wiping is required and how EWaste Kochi protects Kochi businesses from data breaches.",
     "🔥 Most Read", "Security", "green"),
    ("dpdp-act-impact-startups.html",
     "DPDP Act 2023 — What Kerala Startups Must Do Now",
     "India's Digital Personal Data Protection Act 2023 creates new ITAD obligations for startups. Penalties up to ₹250 Crore. Here's what Kochi startups must do now.",
     "⚖️ Compliance Alert", "Legal", "amber"),
    ("hard-drive-shredding-cost-kochi.html",
     "Hard Drive Shredding Cost in Kochi 2026 — Complete Price Guide",
     "Transparent pricing for NIST overwrite, degaussing, physical shredding, and SSD destruction in Kochi Kerala 2026. Bulk volume discounts included.",
     "💰 Pricing Guide", "Pricing", "blue"),
    ("phone-data-recovery-risk.html",
     "Phone Data Recovery Risk — What Happens When You Sell Your Smartphone",
     "Studies show 70% of sold phones still contain recoverable data. Learn what factory reset actually does — and why certified wipe is essential before selling.",
     "📱 Security Alert", "Security", "red"),
    ("laptop-resale-value-2026.html",
     "Laptop Resale Value 2026 — Get Maximum Price in Kochi",
     "Which laptop brands hold value best in 2026? MacBook, ThinkPad, Dell XPS compared. How to get maximum buyback price in Kochi.",
     "💻 Buyback Guide", "Buyback", "green"),
    ("nist-800-88-vs-dod-standards.html",
     "NIST 800-88 vs DoD 5220.22-M — Which Standard Does Your Business Need?",
     "Practical comparison of NIST 800-88 and DoD 5220.22-M data destruction standards. When to use each for your Kochi business compliance requirements.",
     "🛡️ Technical Guide", "Technical", "blue"),
    ("ewaste-laws-kerala.html",
     "E-Waste Laws in Kerala 2026 — Complete Business Compliance Guide",
     "Everything Kerala businesses need to know about E-Waste Management Rules 2022, EPR obligations, KSPCB authorization, and DPDP Act requirements in 2026.",
     "📋 Regulatory Guide", "Legal", "amber"),
    ("secure-phone-disposal-guide.html",
     "Secure Phone Disposal Guide — 7 Steps Before Selling Your Smartphone",
     "Step-by-step guide to safely dispose of Android or iPhone before selling. Factory reset is not enough — here's what certified wipe adds.",
     "🔐 How-To Guide", "How-To", "blue"),
    ("corporate-itad-checklist.html",
     "Corporate ITAD Checklist — 20 Steps Before Disposing IT Assets",
     "Practical checklist for IT managers and compliance officers in Kerala businesses. 20 steps for DPDP Act compliant IT asset disposition.",
     "✅ Practical Checklist", "ITAD", "green"),
    ("where-sell-old-phone-kochi.html",
     "Where to Sell Old Phone in Kochi 2026 — Best Options Compared",
     "Cashify vs OLX vs EWaste Kochi — which gives you most money AND data security in Kochi 2026? Complete comparison with current prices.",
     "📍 Local Guide", "Buyback", "amber"),
]

# ── INDUSTRY PAGES ──────────────────────────────────────────────────────
INDUSTRIES = [
    ("it-companies-infopark.html", "IT Companies & Infopark ITAD Kochi",
     "Certified ITAD for Kochi's IT sector. Infopark, SmartCity, KSTP companies trust us for quarterly ITAD cycles. NIST 800-88, free pickup, same-day CoD.",
     "💻", "IT Companies & Software", "Infopark, SmartCity & KSTP",
     "60+ Infopark and SmartCity companies use our quarterly ITAD program. NIST 800-88 certified wipe for laptops, servers, and networking equipment. DPDP Act vendor contract included. Free bulk pickup from campus. Same-day Certificate of Destruction."),
    ("banks-financial-data-destruction.html", "Banking & Finance ITAD Kochi — RBI Compliant Data Destruction",
     "RBI IT Framework compliant data destruction for banks and financial institutions in Kerala. DoD 5220.22-M or physical shredding. On-site service available.",
     "🏦", "Banking & Finance", "RBI IT Framework Compliant",
     "RBI IT Framework 2015/2023 compliant disposal for banking hardware. DoD 5220.22-M or physical shredding for ATM drives, core banking servers, and branch IT. On-site destruction service for RRBs and co-operative banks. Full audit trail and Certificate of Destruction for RBI inspection."),
    ("hospitals-medical-ewaste.html", "Hospital IT Asset Disposal Kochi — NABH & Patient Data Compliance",
     "Certified e-waste disposal for Kerala hospitals. Patient data on medical devices requires certified destruction. HIPAA-aligned, NABH compliant.",
     "🏥", "Hospitals & Healthcare", "HIPAA-Aligned, NABH Compliant",
     "Patient data on diagnostic workstations, PACS systems, and medical laptops requires certified destruction. HIPAA-aligned process meeting NABH digital record management standards. Serving teaching hospitals, diagnostics labs, and private clinics across Kochi. On-site shredding available for zero chain-of-custody risk."),
    ("government-itad-kochi.html", "Government & PSU ITAD Kochi — GFR/CVC Compliant Disposal",
     "GFR and CVC compliant IT asset disposal for Kerala government departments and PSUs. DoD 5220.22-M standard. Full audit trail.",
     "🏛️", "Government & PSUs", "GFR / CVC / DoD Compliant",
     "GFR and CVC compliant disposal with complete audit trail for government hardware. DoD 5220.22-M standard for sensitive government systems. Serving Kochi Corporation, KSEB, Kerala IT Mission, Cochin Port, and central government offices. Detailed reporting format compatible with CAG audit requirements."),
    ("schools-education-ewaste.html", "School & University E-Waste Kochi — DPDP Act Student Data Protection",
     "Student personal data on school devices requires DPDP Act compliant disposal. Affordable bulk programs for CBSE/ICSE schools upgrading computer labs.",
     "🎓", "Schools & Universities", "DPDP Act Student Data Compliant",
     "Student names, roll numbers, exam data, and attendance records on school computers require certified destruction under DPDP Act 2023. Affordable bulk programs for CBSE, ICSE, and Kerala state board schools upgrading computer labs. Ernakulam district schools get special pricing. Certificate of Destruction satisfies school board audit requirements."),
    ("startups-itad-kochi.html", "Startup ITAD Kochi — KSUM Portfolio Special Pricing",
     "Affordable ITAD for KSUM-incubated startups and early-stage companies in Kochi. Same compliance standards as enterprise — no compromise on Certificate of Destruction.",
     "🚀", "Startups & Emerging Tech", "KSUM Portfolio Special Pricing",
     "KSUM-incubated startups and T-Hub companies in Kochi get special pricing without compromising compliance standards. We understand startup cash flows — pay-per-device, no minimum commitment. Same NIST 800-88 certification and Certificate of Destruction as enterprise clients. DPDP Act vendor contract included."),
    ("manufacturing-ewaste.html", "Manufacturing & Industrial E-Waste Kerala — KSPCB & EPR Compliant",
     "KSPCB-authorized disposal for industrial IT assets and PLCs in Kerala. EPR-compliant channelling. Factory floor logistics managed.",
     "🏭", "Manufacturing & Industrial", "KSPCB & EPR Framework Compliant",
     "KSPCB-authorized disposal for industrial IT assets including PLCs, SCADA workstations, industrial sensors, and embedded systems. EPR-compliant channelling for bulk e-waste generation. Factory floor logistics managed by us — you don't move anything. Serving Kochi SEZ, KINFRA industrial parks, and Eloor/Kalamassery industrial belt."),
]

# ── COMPLIANCE PAGES ────────────────────────────────────────────────────
COMPLIANCE_PAGES = [
    ("dpdp-act-2023-penalties.html", "DPDP Act 2023 Penalties — ₹250 Crore Fine for Data Breach",
     "India's DPDP Act 2023 imposes penalties up to ₹250 Crore for improper data disposal. Learn how Certificate of Destruction protects your business.",
     "DPDP Act 2023", "⚖️"),
    ("nist-800-88-explained.html", "NIST 800-88 Data Sanitization Explained — Complete Guide",
     "What is NIST SP 800-88? Clear, Purge, and Destroy methods explained. Why it's the gold standard for data destruction and how EWaste Kochi applies it.",
     "NIST SP 800-88", "🔒"),
    ("dod-5220-22m-guide.html", "DoD 5220.22-M Data Destruction Standard — Complete Guide",
     "US Department of Defense 7-pass overwrite standard explained. When to use DoD 5220.22-M for your Kochi business and banking sector requirements.",
     "DoD 5220.22-M", "🛡️"),
    ("kerala-pcb-authorization.html", "Kerala PCB Authorization for E-Waste — Why It Matters for Your Business",
     "What is KSPCB authorization for e-waste recyclers? Why using unauthorized dealers is illegal and how to verify your recycler's compliance status.",
     "KSPCB Authorization", "🌿"),
    ("certificate-verification.html", "Certificate of Destruction Verification — EWaste Kochi",
     "Verify your Certificate of Destruction issued by EWaste Kochi. Enter your CoD reference number to confirm authenticity and destruction details.",
     "CoD Verification", "🔍"),
    ("chain-of-custody.html", "Chain of Custody Documentation — ITAD Tracking System",
     "How EWaste Kochi's chain-of-custody system tracks your devices from pickup to destruction. Full documentation for DPDP Act compliance.",
     "Chain of Custody", "📋"),
    ("iso-27001-compliance.html", "ISO 27001 Compliant ITAD — Data Destruction for Certified Organizations",
     "ISO 27001 certified organizations require ITAD vendors with equivalent controls. How EWaste Kochi's process meets ISO 27001 Annex A.8.3 requirements.",
     "ISO 27001", "🏅"),
    ("epr-framework-india.html", "EPR Framework India — Extended Producer Responsibility for E-Waste",
     "What is Extended Producer Responsibility (EPR) for e-waste in India? How Kerala businesses comply with EPR obligations and what documentation is required.",
     "EPR Framework", "♻️"),
]

# ── COMPARISON PAGES ────────────────────────────────────────────────────
COMPARISONS = [
    ("cashify-vs-ewastekochi.html", "Cashify vs EWaste Kochi — Kochi 2026 Comparison",
     "Cashify vs EWaste Kochi in Kochi 2026: price comparison, data security, Certificate of Destruction, DPDP Act compliance. Which gives you more?",
     "Cashify", "red"),
    ("olx-vs-ewastekochi.html", "OLX vs EWaste Kochi — Why Selling Devices on OLX is Risky",
     "OLX vs EWaste Kochi: data security risk, buyer fraud, no Certificate of Destruction. Why selling on OLX puts your data and compliance at risk.",
     "OLX / Facebook Marketplace", "red"),
    ("quickr-vs-ewastekochi.html", "Quikr vs EWaste Kochi — Laptop & Phone Selling Comparison",
     "Quikr vs EWaste Kochi for selling old laptops and phones in Kochi. Price comparison, data security, and DPDP Act compliance.",
     "Quikr", "amber"),
    ("scrap-dealers-vs-certified.html", "Scrap Dealers vs Certified ITAD — Why Kochi Businesses Must Choose Certified",
     "Why giving IT equipment to roadside scrap dealers in Kochi creates criminal liability under E-Waste Rules 2022 and DPDP Act 2023.",
     "Local Scrap Dealers", "red"),
    ("local-vs-certified-recycling.html", "Informal vs Certified E-Waste Recycling Kerala — Legal Risks Explained",
     "Informal vs certified e-waste recycling in Kerala: legal obligations, data breach risk, KSPCB authorization, and DPDP Act compliance compared.",
     "Informal Recyclers", "amber"),
]

# ═══════════════════════════════════════════════════════════════════════
# PAGE CONTENT BUILDERS
# ═══════════════════════════════════════════════════════════════════════

def pricing_table_html():
    return """
<div class="section section-alt">
  <div class="wrap">
    <div class="section-tag">Transparent Pricing</div>
    <h2 class="section-title">Data Destruction Pricing</h2>
    <div class="comp-table-wrap">
      <table class="comp-table">
        <thead><tr><th>Service</th><th>Per Unit</th><th>Bulk (50+)</th><th class="col-us">Enterprise (500+)</th></tr></thead>
        <tbody>
          <tr><td><strong style="color:var(--white)">NIST 800-88 Overwrite (HDD/SSD)</strong></td><td style="font-family:var(--font-m)">₹200</td><td style="font-family:var(--font-m)">₹150</td><td class="col-us" style="font-family:var(--font-m)">₹100</td></tr>
          <tr><td><strong style="color:var(--white)">Degaussing (HDD/Tape)</strong></td><td style="font-family:var(--font-m)">₹350</td><td style="font-family:var(--font-m)">₹280</td><td class="col-us" style="font-family:var(--font-m)">₹200</td></tr>
          <tr><td><strong style="color:var(--white)">Physical Shredding (HDD)</strong></td><td style="font-family:var(--font-m)">₹500</td><td style="font-family:var(--font-m)">₹400</td><td class="col-us" style="font-family:var(--font-m)">₹300</td></tr>
          <tr><td><strong style="color:var(--white)">SSD Physical Destruction</strong></td><td style="font-family:var(--font-m)">₹600</td><td style="font-family:var(--font-m)">₹480</td><td class="col-us" style="font-family:var(--font-m)">₹350</td></tr>
          <tr><td><strong style="color:var(--white)">Mobile Phone Certified Wipe</strong></td><td style="font-family:var(--font-m)">₹150</td><td style="font-family:var(--font-m)">₹100</td><td class="col-us" style="font-family:var(--font-m)">₹75</td></tr>
          <tr><td><strong style="color:var(--white)">Server HDD (per drive)</strong></td><td style="font-family:var(--font-m)">₹400</td><td style="font-family:var(--font-m)">₹300</td><td class="col-us" style="font-family:var(--font-m)">₹200</td></tr>
        </tbody>
      </table>
    </div>
    <p style="font-size:.78rem;color:var(--muted);margin-top:10px">All prices include Certificate of Destruction. GST applicable. Free pickup for 50+ units in Kochi.</p>
  </div>
</div>"""


def testimonials_html():
    return """
<div class="section">
  <div class="wrap">
    <div class="section-tag">Client Reviews</div>
    <h2 class="section-title">Trusted by Kochi's Leading Businesses</h2>
    <div class="grid-3">
      <div class="testi-card">
        <div class="testi-stars">★★★★★</div>
        <div class="testi-text">"120 laptops disposed with full DPDP Act documentation — completed within 48 hours. Certificates delivered digitally. Our compliance audit passed without issues."</div>
        <div class="testi-author"><div class="testi-avatar">RK</div><div><div class="testi-name">Rahul Krishnan</div><div class="testi-role">IT Head · Software Co. · Infopark Kochi</div></div></div>
      </div>
      <div class="testi-card">
        <div class="testi-stars">★★★★★</div>
        <div class="testi-text">"RBI audit specifically asks for data destruction certificates. EWaste Kochi's DoD 5220.22-M process and documentation is exactly what our auditors need. Three-year partnership."</div>
        <div class="testi-author"><div class="testi-avatar">SM</div><div><div class="testi-name">Suresh Menon</div><div class="testi-role">Ops Manager · Co-operative Bank · Ernakulam</div></div></div>
      </div>
      <div class="testi-card">
        <div class="testi-stars">★★★★★</div>
        <div class="testi-text">"Cashify offered ₹58,000 for my MacBook Pro M2. EWaste Kochi offered ₹74,000 AND gave me a data destruction certificate. More money, full security, same-day UPI payment."</div>
        <div class="testi-author"><div class="testi-avatar">AP</div><div><div class="testi-name">Ananya Pillai</div><div class="testi-role">Freelance Designer · Thrippunithura</div></div></div>
      </div>
    </div>
  </div>
</div>"""


def faq_html(faqs):
    items = ""
    for q, a in faqs:
        items += f"""
    <div class="faq-item">
      <button class="faq-btn" onclick="toggleFaq(this)"><span>{q}</span><span class="faq-arrow">▼</span></button>
      <div class="faq-body">{a}</div>
    </div>"""
    return f"""
<div class="section section-alt faq-section">
  <div class="wrap" style="max-width:900px;margin:0 auto">
    <div class="section-tag">FAQ</div>
    <h2 class="section-title">Frequently Asked Questions</h2>
    {items}
    <div class="mt-32 text-center">
      <p style="color:var(--muted);margin-bottom:16px">More questions? Chat with our assistant.</p>
      <a href="javascript:openChat()" class="btn btn-outline">💬 Open Chatbot</a>
    </div>
  </div>
</div>"""


def cta_section_html(headline="Ready to Get Started?", sub="Get your free quote in 2 hours. Free pickup for 50+ units anywhere in Kochi.", show_calc=False):
    calc = ""
    if show_calc:
        calc = """
    <div style="background:var(--bg3);border:1px solid var(--border);border-radius:16px;padding:28px">
      <p style="font-family:var(--font-m);font-size:.72rem;color:var(--muted);margin-bottom:16px">// INSTANT PRICE ESTIMATOR</p>
      <div style="display:flex;gap:10px;flex-wrap:wrap;margin-bottom:16px">
        <button class="calc-type-btn badge badge-green active" onclick="calcSelectType(this,'laptop')">💻 Laptop</button>
        <button class="calc-type-btn badge badge-green" onclick="calcSelectType(this,'phone')">📱 Phone</button>
        <button class="calc-type-btn badge badge-green" onclick="calcSelectType(this,'desktop')">🖥️ Desktop</button>
      </div>
      <div class="form-row" style="margin-bottom:12px">
        <div class="form-group" style="margin-bottom:0"><label class="form-label">Brand</label>
          <select class="form-select" id="calc-brand" onchange="calcUpdate()">
            <option value="apple">Apple</option><option value="dell">Dell</option>
            <option value="hp">HP</option><option value="lenovo">Lenovo</option>
            <option value="samsung">Samsung</option><option value="other">Other</option>
          </select></div>
        <div class="form-group" style="margin-bottom:0"><label class="form-label">Age (Years)</label>
          <select class="form-select" id="calc-age" onchange="calcUpdate()">
            <option value="1">Less than 1yr</option><option value="2" selected>1–2 years</option>
            <option value="3">2–3 years</option><option value="4">3–4 years</option><option value="5">4+ years</option>
          </select></div>
      </div>
      <div class="form-row" style="margin-bottom:16px">
        <div class="form-group" style="margin-bottom:0"><label class="form-label">Condition</label>
          <select class="form-select" id="calc-cond" onchange="calcUpdate()">
            <option value="excellent">Excellent</option><option value="good" selected>Good</option>
            <option value="fair">Fair</option><option value="damaged">Damaged</option>
          </select></div>
        <div class="form-group" style="margin-bottom:0"><label class="form-label">Quantity</label>
          <select class="form-select" id="calc-qty" onchange="calcUpdate()">
            <option value="1">1 device</option><option value="5">2–10</option>
            <option value="25">11–50</option><option value="100">51–200</option><option value="500">200+</option>
          </select></div>
      </div>
      <div style="background:var(--bg);border:1px solid rgba(0,232,122,.2);border-radius:12px;padding:20px;text-align:center">
        <div style="font-size:.7rem;color:var(--muted);margin-bottom:4px;font-family:var(--font-m)">ESTIMATED BUYBACK</div>
        <div id="calc-result" style="font-family:var(--font-h);font-size:2rem;font-weight:800;color:var(--green);margin-bottom:4px">₹42,000 – ₹48,000</div>
        <div id="calc-sub" style="font-size:.72rem;color:var(--muted);margin-bottom:12px">Apple laptop · 1–2yr · Good</div>
        <a id="wa-calc-link" href="https://wa.me/919876543210" class="btn btn-wa btn-full" target="_blank">💬 Confirm on WhatsApp</a>
      </div>
      <div id="calc-bulk" style="display:none" class="alert alert-success mt-12">
        <span class="alert-icon">🎁</span><div class="alert-content"><div class="alert-title">Bulk Bonus Active!</div><div class="alert-text">50+ units: free same-day pickup across Kochi.</div></div>
      </div>
    </div>"""
    return f"""
<div style="background:linear-gradient(135deg,rgba(0,232,122,.06),rgba(245,168,39,.03),rgba(0,232,122,.04));border-top:1px solid var(--border);border-bottom:1px solid var(--border);padding:80px 0">
  <div class="wrap">
    <div class="grid-2" style="align-items:center;gap:48px">
      <div>
        <div class="section-tag">Get Started Today</div>
        <h2 class="section-title" style="margin-bottom:16px">{headline}</h2>
        <p style="font-size:.95rem;color:var(--text);line-height:1.8;margin-bottom:28px">{sub}</p>
        <div style="display:flex;flex-direction:column;gap:12px;margin-bottom:28px">
          <div style="display:flex;gap:12px;align-items:center"><div style="width:40px;height:40px;border-radius:10px;background:rgba(0,232,122,.1);border:1px solid rgba(0,232,122,.2);display:flex;align-items:center;justify-content:center;flex-shrink:0">📞</div><div><div style="font-size:.78rem;color:var(--muted)">Call / WhatsApp 24/7</div><div style="font-weight:700;color:var(--white)">+91-9876-543-210</div></div></div>
          <div style="display:flex;gap:12px;align-items:center"><div style="width:40px;height:40px;border-radius:10px;background:rgba(0,232,122,.1);border:1px solid rgba(0,232,122,.2);display:flex;align-items:center;justify-content:center;flex-shrink:0">📍</div><div><div style="font-size:.78rem;color:var(--muted)">Drop-off facility</div><div style="font-weight:700;color:var(--white)">710A Hill Palace Rd, Thrippunithura, Kochi 682301</div></div></div>
        </div>
        <div style="display:flex;gap:12px;flex-wrap:wrap">
          <a href="/get-instant-quote.html" class="btn btn-primary btn-lg">📋 Get Free Quote</a>
          <a href="https://wa.me/919876543210" class="btn btn-wa btn-lg" target="_blank">💬 WhatsApp</a>
        </div>
      </div>
      {calc}
      {'<div class="card"><form onsubmit="submitLead(event)" id="lead-form"><div class="section-tag" style="margin-bottom:12px">Free Quote Form</div><div class="form-group"><label class="form-label">Name *</label><input type="text" class="form-input" placeholder="Your name" required></div><div class="form-group"><label class="form-label">Phone *</label><input type="tel" class="form-input" placeholder="+91 98765 43210" required></div><div class="form-group"><label class="form-label">Service</label><select class="form-select"><option>Corporate ITAD</option><option>Data Destruction</option><option>Sell Laptop(s)</option><option>Sell Phone(s)</option><option>Office Clearance</option></select></div><div class="form-group"><label class="form-label">Device Count</label><select class="form-select"><option>1–5</option><option>6–20</option><option>21–50</option><option>50–200</option><option>200+</option></select></div><button type="submit" class="btn btn-primary btn-full btn-lg mt-8">📤 Send — Reply in 2 Hours</button></form><div id="lead-success" style="display:none;text-align:center;padding:32px 0"><div style="font-size:3rem">✅</div><div style="font-family:var(--font-h);font-size:1.1rem;color:var(--white);margin:12px 0">Request Sent!</div><a href="https://wa.me/919876543210" class="btn btn-wa btn-full mt-8" target="_blank">💬 WhatsApp for faster reply</a></div></div>' if not show_calc else ''}
    </div>
  </div>
</div>"""


# ═══════════════════════════════════════════════════════════════════════
# LOCATION PAGE GENERATOR
# ═══════════════════════════════════════════════════════════════════════

def gen_location_page(name, slug, distance, landmarks):
    title = f"E-Waste Recycling {name} Kochi | ITAD & Laptop Buyback — EWaste Kochi"
    meta = f"Certified e-waste recycling and ITAD in {name}, Kochi. NIST 800-88 data destruction, laptop buyback, free pickup. DPDP Act compliant. {distance} from our Thrippunithura facility."
    canonical = f"/locations/ewaste-{slug}.html"
    bc = breadcrumb_html([("Home", "/"), ("Locations", "/locations/"), (name, None)])
    body = f"""
<div class="page-hero">
  <div class="wrap">
    <div class="page-hero-tag">📍 {name} — Service Area</div>
    <h1 class="page-hero-title">E-Waste Recycling &amp; ITAD in <em>{name}</em>, Kochi</h1>
    <p class="page-hero-desc">Certified e-waste disposal, NIST 800-88 data destruction, and laptop/phone buyback serving {name} and surrounding areas. {distance} from our Thrippunithura facility. Free corporate pickup for 50+ units.</p>
    <div style="display:flex;gap:12px;flex-wrap:wrap">
      <a href="/get-instant-quote.html" class="btn btn-primary">📋 Get Free Quote</a>
      <a href="https://wa.me/919876543210?text=Hi%2C+I+need+e-waste+services+in+{name.replace(' ','+')}+Kochi" class="btn btn-wa" target="_blank">💬 WhatsApp</a>
    </div>
  </div>
</div>
<div class="section">
  <div class="wrap">
    <div class="grid-2">
      <div>
        <div class="section-tag">{name} Coverage</div>
        <h2 class="section-title" style="font-size:1.6rem">Serving {name} &amp; Surrounding Areas</h2>
        <p style="color:var(--text);line-height:1.8;margin-bottom:20px">EWaste Kochi provides certified IT asset disposition and e-waste recycling to businesses and individuals in {name}, Kochi. Our {distance} proximity means same-day or next-day service for all corporate pickup requests.</p>
        <p style="color:var(--text);line-height:1.8;margin-bottom:20px">Key areas we serve near {name}: <strong style="color:var(--white)">{landmarks}</strong>. For individual devices, drop-off at our Thrippunithura facility is always free and requires no appointment.</p>
        <div style="display:flex;flex-direction:column;gap:10px">
          <div style="display:flex;gap:8px;align-items:center;font-size:.85rem"><span style="color:var(--green)">✓</span><span>Free pickup for 50+ units — no logistics charge</span></div>
          <div style="display:flex;gap:8px;align-items:center;font-size:.85rem"><span style="color:var(--green)">✓</span><span>Same-day or next-day corporate service</span></div>
          <div style="display:flex;gap:8px;align-items:center;font-size:.85rem"><span style="color:var(--green)">✓</span><span>NIST 800-88 certified wipe + Certificate of Destruction</span></div>
          <div style="display:flex;gap:8px;align-items:center;font-size:.85rem"><span style="color:var(--green)">✓</span><span>DPDP Act compliance documentation included</span></div>
          <div style="display:flex;gap:8px;align-items:center;font-size:.85rem"><span style="color:var(--green)">✓</span><span>Same-day UPI/bank transfer payment for buyback</span></div>
        </div>
      </div>
      <div class="card">
        <div class="section-tag" style="margin-bottom:12px">Service Details</div>
        <div style="display:flex;flex-direction:column;gap:14px">
          <div style="padding:12px;background:var(--bg2);border-radius:10px"><div style="font-size:.72rem;color:var(--muted);margin-bottom:4px">Distance from facility</div><div style="font-weight:700;color:var(--white)">{distance}</div></div>
          <div style="padding:12px;background:var(--bg2);border-radius:10px"><div style="font-size:.72rem;color:var(--muted);margin-bottom:4px">Free pickup minimum</div><div style="font-weight:700;color:var(--green)">50+ units</div></div>
          <div style="padding:12px;background:var(--bg2);border-radius:10px"><div style="font-size:.72rem;color:var(--muted);margin-bottom:4px">Response time</div><div style="font-weight:700;color:var(--white)">Same day / 2 hours</div></div>
          <div style="padding:12px;background:var(--bg2);border-radius:10px"><div style="font-size:.72rem;color:var(--muted);margin-bottom:4px">Drop-off option</div><div style="font-weight:700;color:var(--white)">Always free at Thrippunithura</div></div>
        </div>
        <a href="https://wa.me/919876543210?text=Hi%2C+I+need+pickup+from+{name.replace(' ','+')}+Kochi" class="btn btn-wa btn-full mt-16" target="_blank">💬 Book {name} Pickup</a>
      </div>
    </div>
  </div>
</div>
{pricing_table_html()}
{cta_section_html(f"Book Your {name} Pickup Today", f"Free corporate pickup from {name}. NIST 800-88 data destruction. Certificate of Destruction every device.", show_calc=True)}
"""
    return html_page(title, meta, canonical, css_depth="../", js_depth="../", body_content=body, breadcrumb=bc)


# ═══════════════════════════════════════════════════════════════════════
# BLOG PAGE GENERATOR
# ═══════════════════════════════════════════════════════════════════════

BLOG_CONTENT = {
    "is-formatting-enough-delete-data.html": """
<div class="alert alert-danger"><span class="alert-icon">🚨</span><div class="alert-content"><div class="alert-title">Short Answer: NO — Not Even Close</div><div class="alert-text">A standard Windows format, Mac erase, or Linux wipe removes the file directory — not the actual data. Your files remain on the disk and can be recovered by anyone with free software in minutes.</div></div></div>
<h2 style="font-size:1.4rem;color:var(--white);margin:28px 0 14px">What Formatting Actually Does</h2>
<p style="color:var(--text);line-height:1.8;margin-bottom:16px">When you format a drive, your operating system marks all storage locations as "available." The actual 1s and 0s of your data remain physically on the disk. Only the directory (the index telling your computer where files are) is cleared.</p>
<p style="color:var(--text);line-height:1.8;margin-bottom:16px">Think of it like tearing out a book's table of contents. The chapters are still there — you just can't find them easily. With free tools like Recuva, TestDisk, or PhotoRec, anyone can rebuild that index and recover your files within minutes.</p>
<h2 style="font-size:1.4rem;color:var(--white);margin:28px 0 14px">What Can Be Recovered After Formatting?</h2>
<div class="grid-2" style="margin-bottom:24px"><div class="card"><div style="color:var(--red);font-weight:700;margin-bottom:8px">❌ Still Recoverable</div><p style="font-size:.84rem;color:var(--text);line-height:1.65">Personal photos & videos, banking credentials, passwords, business documents, emails, WhatsApp messages, tax records, customer data</p></div><div class="card"><div style="color:var(--green);font-weight:700;margin-bottom:8px">✅ Truly Gone</div><p style="font-size:.84rem;color:var(--text);line-height:1.65">Only NIST 800-88 certified overwrite or physical destruction permanently removes data. Multiple overwrite passes make recovery mathematically impossible.</p></div></div>
<h2 style="font-size:1.4rem;color:var(--white);margin:28px 0 14px">NIST 800-88 — The Only Standard That Works</h2>
<p style="color:var(--text);line-height:1.8;margin-bottom:20px">NIST 800-88 certified wiping overwrites every storage location multiple times with different bit patterns. After the process, the original data is mathematically impossible to reconstruct — even with electron microscopy equipment used by intelligence agencies.</p>
<div style="background:rgba(0,232,122,.06);border:1px solid rgba(0,232,122,.2);border-radius:14px;padding:24px"><h3 style="color:var(--white);margin-bottom:12px">The DPDP Act 2023 Risk</h3><p style="font-size:.88rem;color:var(--text);line-height:1.7">Under India's Digital Personal Data Protection Act 2023, if your old laptop containing customer data is recovered after you "formatted" it, you are liable — potentially for penalties up to ₹250 Crore. The ₹200–₹500 cost of certified data wiping at EWaste Kochi is a fraction of the legal risk.</p><a href="/get-instant-quote.html" class="btn btn-primary mt-16">📋 Book Certified Data Destruction</a></div>""",

    "dpdp-act-impact-startups.html": """
<p style="color:var(--text);line-height:1.8;margin-bottom:20px">If your Kochi startup handles any personal data — customer names, phone numbers, email addresses, payment information, employee records — you are a "Data Fiduciary" under the DPDP Act 2023. This creates legal obligations around how you collect, store, and crucially, destroy that data.</p>
<h2 style="font-size:1.4rem;color:var(--white);margin:28px 0 14px">Key ITAD Obligations for Startups Under DPDP Act</h2>
<div style="display:flex;flex-direction:column;gap:12px;margin-bottom:28px">
  <div class="card"><strong style="color:var(--white)">1. Data Purge on Hardware Disposal</strong><p style="font-size:.84rem;color:var(--text);margin-top:6px;line-height:1.65">When you sell, trade, or discard laptops, phones, or servers, personal data must be certified-destroyed. Simply resetting a device is legally insufficient under DPDP Act.</p></div>
  <div class="card"><strong style="color:var(--white)">2. Vendor Due Diligence</strong><p style="font-size:.84rem;color:var(--text);margin-top:6px;line-height:1.65">Your ITAD vendor is a "Data Processor" under DPDP Act. You are responsible for their compliance. EWaste Kochi provides the contract and documentation needed.</p></div>
  <div class="card"><strong style="color:var(--white)">3. Documentation for Audits</strong><p style="font-size:.84rem;color:var(--text);margin-top:6px;line-height:1.65">Certificate of Destruction per device, with serial numbers and destruction method, is your legal evidence of compliance. EWaste Kochi issues court-admissible CoDs.</p></div>
  <div class="card"><strong style="color:var(--white)">4. Penalty Exposure</strong><p style="font-size:.84rem;color:var(--text);margin-top:6px;line-height:1.65">Significant data breaches through discarded devices: up to ₹250 Crore penalty. Non-compliance with DPDP obligations: up to ₹50 Crore per instance.</p></div>
</div>
<a href="/get-instant-quote.html" class="btn btn-primary">📋 Get DPDP-Compliant ITAD for Your Startup</a>""",
}

DEFAULT_BLOG_CONTENT = """<p style="color:var(--text);line-height:1.8;margin-bottom:20px">This is a comprehensive guide on the topic above, covering everything Kochi businesses need to know about certified e-waste disposal, data destruction, and DPDP Act compliance.</p>
<div class="alert alert-amber"><span class="alert-icon">💡</span><div class="alert-content"><div class="alert-title">Key Takeaway</div><div class="alert-text">Proper certified ITAD with Certificate of Destruction protects your business from DPDP Act penalties and data breach liability. EWaste Kochi provides full compliance documentation with every job.</div></div></div>
<p style="color:var(--text);line-height:1.8;margin-bottom:20px;margin-top:20px">Contact our team for specific guidance on how this applies to your business sector and device count. We offer free consultations for corporate clients in Kochi.</p>
<a href="/get-instant-quote.html" class="btn btn-primary">📋 Get Free Consultation</a>"""


def gen_blog_page(slug, title, meta, tag_label, category, color):
    canonical = f"/blog/{slug}"
    bc = breadcrumb_html([("Home", "/"), ("Blog", "/blog/"), (title[:50], None)])
    content = BLOG_CONTENT.get(slug, DEFAULT_BLOG_CONTENT)
    body = f"""
<div class="page-hero">
  <div class="wrap">
    <div class="page-hero-tag">{tag_label}</div>
    <h1 class="page-hero-title">{title}</h1>
    <p class="page-hero-desc">{meta}</p>
    <div style="display:flex;gap:10px;flex-wrap:wrap;margin-top:4px">
      <span class="badge badge-{color}">{category}</span>
      <span style="font-size:.75rem;color:var(--muted);display:flex;align-items:center;gap:4px">📅 Updated March 2026</span>
    </div>
  </div>
</div>
<div class="section">
  <div class="wrap" style="max-width:800px;margin:0 auto">
    {content}
  </div>
</div>
{testimonials_html()}
{cta_section_html()}
"""
    return html_page(title + " — EWaste Kochi", meta, canonical, css_depth="../", js_depth="../", body_content=body, breadcrumb=bc)


# ═══════════════════════════════════════════════════════════════════════
# INDUSTRY PAGE GENERATOR
# ═══════════════════════════════════════════════════════════════════════

def gen_industry_page(slug, title, meta, icon, sector_name, cert_label, detail):
    canonical = f"/industries/{slug}"
    bc = breadcrumb_html([("Home", "/"), ("Industries", "/industries/"), (sector_name, None)])
    body = f"""
<div class="page-hero">
  <div class="wrap">
    <div class="page-hero-tag">{icon} {sector_name}</div>
    <h1 class="page-hero-title">{title}</h1>
    <p class="page-hero-desc">{meta}</p>
    <div style="display:flex;gap:12px;flex-wrap:wrap">
      <a href="/get-instant-quote.html" class="btn btn-primary">📋 Get Sector Quote</a>
      <a href="https://wa.me/919876543210" class="btn btn-wa" target="_blank">💬 WhatsApp</a>
    </div>
  </div>
</div>
<div class="section">
  <div class="wrap">
    <div class="grid-2" style="align-items:start">
      <div>
        <div class="section-tag">{cert_label}</div>
        <h2 class="section-title" style="font-size:1.6rem">ITAD Built for<br>{sector_name}</h2>
        <p style="color:var(--text);line-height:1.8;margin-bottom:24px">{detail}</p>
        <div style="display:flex;flex-direction:column;gap:10px">
          <div style="display:flex;gap:8px;font-size:.85rem"><span style="color:var(--green)">✓</span><span>NIST 800-88 or DoD 5220.22-M data destruction</span></div>
          <div style="display:flex;gap:8px;font-size:.85rem"><span style="color:var(--green)">✓</span><span>Certificate of Destruction per device with serial tracking</span></div>
          <div style="display:flex;gap:8px;font-size:.85rem"><span style="color:var(--green)">✓</span><span>DPDP Act 2023 vendor contract and compliance documentation</span></div>
          <div style="display:flex;gap:8px;font-size:.85rem"><span style="color:var(--green)">✓</span><span>Free pickup for 50+ units anywhere in Ernakulam</span></div>
          <div style="display:flex;gap:8px;font-size:.85rem"><span style="color:var(--green)">✓</span><span>On-site shredding available for high-security requirements</span></div>
          <div style="display:flex;gap:8px;font-size:.85rem"><span style="color:var(--green)">✓</span><span>Full asset disposition report for audit purposes</span></div>
        </div>
      </div>
      <div class="card">
        <div style="font-size:3rem;margin-bottom:16px">{icon}</div>
        <div class="card-title">{sector_name} ITAD Package</div>
        <div style="display:flex;flex-direction:column;gap:12px;margin:16px 0">
          <div style="display:flex;justify-content:space-between;padding-bottom:8px;border-bottom:1px solid var(--border);font-size:.84rem"><span style="color:var(--muted)">Data Destruction</span><span style="color:var(--white);font-weight:600">NIST 800-88 / DoD 5220.22-M</span></div>
          <div style="display:flex;justify-content:space-between;padding-bottom:8px;border-bottom:1px solid var(--border);font-size:.84rem"><span style="color:var(--muted)">Certificate</span><span style="color:var(--white);font-weight:600">Per Device with Serial No.</span></div>
          <div style="display:flex;justify-content:space-between;padding-bottom:8px;border-bottom:1px solid var(--border);font-size:.84rem"><span style="color:var(--muted)">Compliance</span><span style="color:var(--white);font-weight:600">{cert_label}</span></div>
          <div style="display:flex;justify-content:space-between;padding-bottom:8px;border-bottom:1px solid var(--border);font-size:.84rem"><span style="color:var(--muted)">Pickup</span><span style="color:var(--green);font-weight:600">Free for 50+ units</span></div>
          <div style="display:flex;justify-content:space-between;font-size:.84rem"><span style="color:var(--muted)">Response Time</span><span style="color:var(--white);font-weight:600">2 hours / Same day</span></div>
        </div>
        <a href="/get-instant-quote.html" class="btn btn-primary btn-full">📋 Get {sector_name} Quote</a>
      </div>
    </div>
  </div>
</div>
{pricing_table_html()}
{testimonials_html()}
{cta_section_html(f"Certified ITAD for {sector_name} in Kochi")}
"""
    return html_page(title + " — EWaste Kochi", meta, canonical, css_depth="../", js_depth="../", body_content=body, breadcrumb=bc)


# ═══════════════════════════════════════════════════════════════════════
# COMPLIANCE PAGE GENERATOR
# ═══════════════════════════════════════════════════════════════════════

def gen_compliance_page(slug, title, meta, std_name, icon):
    canonical = f"/compliance/{slug}"
    bc = breadcrumb_html([("Home", "/"), ("Compliance", "/compliance/"), (std_name, None)])
    cert_preview = """
<div style="background:linear-gradient(135deg,#0C1A10,#162019);border:2px solid rgba(0,232,122,.25);border-radius:16px;padding:28px;position:relative;overflow:hidden">
  <div style="position:absolute;bottom:12px;right:12px;font-family:var(--font-h);font-size:4rem;font-weight:800;color:rgba(0,232,122,.04);user-select:none">CoD</div>
  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;padding-bottom:14px;border-bottom:1px solid rgba(0,232,122,.15)">
    <div style="font-family:var(--font-h);font-size:.95rem;font-weight:800;color:var(--green)">♻️ EWaste Kochi</div>
    <div class="badge badge-green">NIST 800-88</div>
  </div>
  <div style="font-family:var(--font-h);font-size:1rem;color:var(--white);margin-bottom:4px">Certificate of Data Destruction</div>
  <div style="font-size:.72rem;color:var(--muted);margin-bottom:14px">This certifies data destruction per NIST SP 800-88 Rev. 1</div>
  <div style="display:flex;justify-content:space-between;font-size:.75rem;margin-bottom:6px"><span style="color:var(--muted)">Reference</span><span style="color:var(--white);font-family:var(--font-m)">EWK-2026-04821</span></div>
  <div style="display:flex;justify-content:space-between;font-size:.75rem;margin-bottom:6px"><span style="color:var(--muted)">Devices Processed</span><span style="color:var(--white);font-family:var(--font-m)">47 units</span></div>
  <div style="display:flex;justify-content:space-between;font-size:.75rem;margin-bottom:6px"><span style="color:var(--muted)">Method</span><span style="color:var(--white);font-family:var(--font-m)">NIST 800-88 Purge</span></div>
  <div style="display:flex;justify-content:space-between;font-size:.75rem;margin-bottom:14px"><span style="color:var(--muted)">Date</span><span style="color:var(--white);font-family:var(--font-m)">March 2026</span></div>
  <div style="border-top:1px solid rgba(0,232,122,.15);padding-top:12px;text-align:center;font-family:var(--font-m);font-size:.68rem;color:var(--green)">✓ KSPCB AUTHORIZED FACILITY — KERALA</div>
</div>"""
    body = f"""
<div class="page-hero">
  <div class="wrap">
    <div class="page-hero-tag">{icon} {std_name}</div>
    <h1 class="page-hero-title">{title}</h1>
    <p class="page-hero-desc">{meta}</p>
    <a href="/get-instant-quote.html" class="btn btn-primary">Get Compliance Documentation →</a>
  </div>
</div>
<div class="section">
  <div class="wrap">
    <div class="grid-2" style="align-items:start">
      <div>
        <div class="section-tag">{std_name} Explained</div>
        <h2 class="section-title" style="font-size:1.5rem">Why {std_name} Matters for Your Business</h2>
        <p style="color:var(--text);line-height:1.8;margin-bottom:20px">Compliance with {std_name} isn't just about following rules — it's about protecting your business from data breach liability, regulatory penalties, and reputational damage. EWaste Kochi applies the highest standards to every device we process.</p>
        <div style="display:flex;flex-direction:column;gap:12px">
          <div class="card" style="padding:16px"><strong style="color:var(--white)">Legal Protection</strong><p style="font-size:.83rem;color:var(--text);margin-top:4px">Certificate of Destruction proves compliance under DPDP Act 2023, protecting you from penalties up to ₹250 Crore.</p></div>
          <div class="card" style="padding:16px"><strong style="color:var(--white)">Audit-Ready Documentation</strong><p style="font-size:.83rem;color:var(--text);margin-top:4px">Every CoD includes serial numbers, destruction method, date, technician ID, and KSPCB facility authorization reference.</p></div>
          <div class="card" style="padding:16px"><strong style="color:var(--white)">Industry Recognition</strong><p style="font-size:.83rem;color:var(--text);margin-top:4px">Accepted by RBI, SEBI, ISO 27001, and NABH audit frameworks for data destruction compliance.</p></div>
        </div>
      </div>
      {cert_preview}
    </div>
  </div>
</div>
{pricing_table_html()}
{cta_section_html(f"Get {std_name} Certified Destruction", f"Full {std_name} compliance documentation for every device. Certificate of Destruction issued with serial number tracking.")}
"""
    return html_page(title + " — EWaste Kochi", meta, canonical, css_depth="../", js_depth="../", body_content=body, breadcrumb=bc)


# ═══════════════════════════════════════════════════════════════════════
# COMPARISON PAGE GENERATOR
# ═══════════════════════════════════════════════════════════════════════

def gen_comparison_page(slug, title, meta, competitor, danger_color):
    canonical = f"/comparisons/{slug}"
    bc = breadcrumb_html([("Home", "/"), ("Comparisons", "/comparisons/"), (title[:40], None)])
    rows = [
        ("KSPCB Authorization", "❌ None", "✅ Fully Authorized"),
        ("NIST-Certified Data Wipe", "❌ Basic reset or none", "✅ NIST 800-88 Every Device"),
        ("Certificate of Destruction", "❌ Not offered", "✅ Issued Per Device"),
        ("DPDP Act Compliance", "❌ No documentation", "✅ Full Compliance Docs"),
        ("Price (MacBook M1)", "~₹58,000–62,000", "Up to ₹78,000 (+26%)"),
        ("Corporate Bulk ITAD", "❌ Consumer only", "✅ Enterprise Programs"),
        ("Free Kochi Pickup", "⚠️ Conditions apply", "✅ Free for 50+ units"),
        ("Your Legal Liability", "⚠️ High — no CoD", "✅ Protected by CoD"),
    ]
    table_rows = "".join(f"<tr><td><strong style='color:var(--white)'>{r[0]}</strong></td><td class='chk-warn'>{r[1]}</td><td class='col-us chk-yes'>{r[2]}</td></tr>" for r in rows)
    body = f"""
<div class="page-hero">
  <div class="wrap">
    <div class="page-hero-tag">⚔️ Head-to-Head Comparison</div>
    <h1 class="page-hero-title">{title}</h1>
    <p class="page-hero-desc">{meta}</p>
  </div>
</div>
<div class="section">
  <div class="wrap">
    <div class="alert alert-danger"><span class="alert-icon">⚠️</span><div class="alert-content"><div class="alert-title">Data Security Warning</div><div class="alert-text">Using {competitor} or similar platforms does not provide Certificate of Destruction or DPDP Act compliance documentation. If personal data on those devices is later recovered, you remain legally liable as the Data Fiduciary under DPDP Act 2023.</div></div></div>
    <div class="comp-table-wrap mt-24">
      <table class="comp-table">
        <thead><tr><th>What Matters</th><th>{competitor}</th><th class="col-us">EWaste Kochi ✓</th></tr></thead>
        <tbody>{table_rows}</tbody>
      </table>
    </div>
    <div class="text-center mt-32">
      <a href="/get-instant-quote.html" class="btn btn-primary btn-lg">Switch to Certified Disposal →</a>
    </div>
  </div>
</div>
{testimonials_html()}
{cta_section_html()}
"""
    return html_page(title + " — EWaste Kochi", meta, canonical, css_depth="../", js_depth="../", body_content=body, breadcrumb=bc)


# ═══════════════════════════════════════════════════════════════════════
# CORE PAGE CONTENT (inline in generator for completeness)
# ═══════════════════════════════════════════════════════════════════════

CORE_PAGES = {
    "contact.html": {
        "title": "Contact EWaste Kochi — Free Quote & Pickup Booking",
        "meta": "Contact EWaste Kochi for certified ITAD, data destruction, and laptop/phone buyback in Kochi. 2-hour response guaranteed. Free pickup for 50+ units.",
        "canonical": "/contact.html",
        "body": """
<div class="page-hero">
  <div class="wrap">
    <div class="page-hero-tag">📞 Contact Us</div>
    <h1 class="page-hero-title">Get In Touch with <em>EWaste Kochi</em></h1>
    <p class="page-hero-desc">Book a free pickup, get an instant quote, or ask any question. We respond within 2 hours on working days.</p>
  </div>
</div>
<div class="section">
  <div class="wrap">
    <div class="grid-2">
      <div>
        <h2 class="section-title" style="font-size:1.4rem">📋 Send Us a Message</h2>
        <form onsubmit="submitContact(event)">
          <div class="form-row"><div class="form-group"><label class="form-label">Full Name *</label><input type="text" class="form-input" placeholder="Rahul Sharma" required></div><div class="form-group"><label class="form-label">Phone *</label><input type="tel" class="form-input" placeholder="+91 98765 43210" required></div></div>
          <div class="form-group"><label class="form-label">Email</label><input type="email" class="form-input" placeholder="your@company.com"></div>
          <div class="form-row"><div class="form-group"><label class="form-label">Service Needed *</label><select class="form-select" required><option value="">-- Select --</option><option>Corporate ITAD</option><option>Certified Data Destruction</option><option>Hard Drive Shredding</option><option>Sell Laptop(s)</option><option>Sell Phone(s)</option><option>Office Clearance</option><option>Compliance Consultation</option></select></div><div class="form-group"><label class="form-label">Device Count</label><select class="form-select"><option>1–5</option><option>6–20</option><option>21–50</option><option>51–200</option><option>200+</option></select></div></div>
          <div class="form-group"><label class="form-label">Your Area in Kochi</label><input type="text" class="form-input" placeholder="Kakkanad, Edapally, Vyttila..."></div>
          <div class="form-group"><label class="form-label">Message</label><textarea class="form-input" rows="4" placeholder="Device models, urgent pickup needed, compliance requirements..."></textarea></div>
          <button type="submit" class="btn btn-primary btn-full btn-lg">📤 Send — Reply in 2 Hours</button>
          <a href="https://wa.me/919876543210" class="btn btn-wa btn-full mt-8" target="_blank">💬 Or WhatsApp Directly</a>
        </form>
        <div id="contact-success" style="display:none;text-align:center;padding:40px 0"><div style="font-size:3rem">✅</div><div style="font-family:var(--font-h);font-size:1.2rem;color:var(--white);margin:12px 0">Message Sent!</div><div style="color:var(--muted)">We'll contact you within 2 hours.</div></div>
      </div>
      <div style="display:flex;flex-direction:column;gap:16px">
        <div class="card"><div style="color:var(--green);font-weight:700;margin-bottom:10px">🏢 Main Facility</div><p style="font-size:.88rem;color:var(--text);line-height:1.8">710A Hill Palace Rd, East Fort Gate<br>Kannankulangara, Thrippunithura<br>Kochi, Kerala 682301</p></div>
        <div class="card"><div style="color:var(--green);font-weight:700;margin-bottom:8px">📞 Call / WhatsApp</div><p style="font-size:1.1rem;color:var(--white);font-weight:700">+91-9876-543-210</p><p style="font-size:.8rem;color:var(--muted);margin-top:4px">24/7 for corporate emergencies</p></div>
        <div class="card"><div style="color:var(--green);font-weight:700;margin-bottom:8px">✉️ Email</div><p style="color:var(--text)">info@ewastekochi.com</p></div>
        <div class="card"><div style="color:var(--green);font-weight:700;margin-bottom:10px">⏰ Hours</div><div style="font-size:.85rem;color:var(--text);display:flex;flex-direction:column;gap:6px"><div style="display:flex;justify-content:space-between"><span>Mon – Sat</span><span style="color:var(--green)">8:00 AM – 8:00 PM</span></div><div style="display:flex;justify-content:space-between"><span>Sunday</span><span style="color:var(--amber)">10:00 AM – 4:00 PM</span></div><div style="display:flex;justify-content:space-between"><span>Corporate Pickup</span><span style="color:var(--green)">24/7</span></div></div></div>
      </div>
    </div>
  </div>
</div>"""
    },
    "faq.html": {
        "title": "FAQs — E-Waste, ITAD & Data Destruction in Kochi Kerala",
        "meta": "Frequently asked questions about e-waste recycling, ITAD, data destruction, DPDP Act compliance, and device buyback in Kochi Kerala.",
        "canonical": "/faq.html",
        "body": """
<div class="page-hero">
  <div class="wrap">
    <div class="page-hero-tag">❓ FAQs</div>
    <h1 class="page-hero-title">Frequently Asked <em>Questions</em></h1>
    <p class="page-hero-desc">Answers to Kochi's most common questions about e-waste disposal, data destruction, device buyback, and DPDP Act compliance.</p>
  </div>
</div>
<div class="section faq-section">
  <div class="wrap" style="max-width:900px;margin:0 auto">
    <div class="faq-item"><button class="faq-btn" onclick="toggleFaq(this)"><span>Is formatting a hard drive enough to delete data permanently?</span><span class="faq-arrow">▼</span></button><div class="faq-body">No — not even close. A standard format only removes the file directory, not the actual data. Free tools like Recuva can recover your files within minutes. NIST 800-88 certified wiping or physical destruction is the only way to guarantee permanent deletion.</div></div>
    <div class="faq-item"><button class="faq-btn" onclick="toggleFaq(this)"><span>What is a Certificate of Destruction and do I legally need one?</span><span class="faq-arrow">▼</span></button><div class="faq-body">A Certificate of Destruction (CoD) is a legal document confirming each device (by serial number) had its data permanently destroyed using a certified method. Under India's DPDP Act 2023, if a data breach occurs through a discarded device, you need a CoD to prove compliance. Without it, penalties up to ₹250 Crore apply. EWaste Kochi issues CoDs for every device.</div></div>
    <div class="faq-item"><button class="faq-btn" onclick="toggleFaq(this)"><span>How much will I get for my old laptop in Kochi?</span><span class="faq-arrow">▼</span></button><div class="faq-body">MacBook Pro M1/M2/M3: up to ₹85,000. MacBook Air: up to ₹65,000. Dell/HP business laptops: ₹15,000–₹45,000. Lenovo ThinkPads: ₹20,000–₹50,000. We consistently offer 15–20% more than Cashify for business-grade hardware. Use our homepage estimator for an instant range.</div></div>
    <div class="faq-item"><button class="faq-btn" onclick="toggleFaq(this)"><span>Is pickup really free? What's the minimum?</span><span class="faq-arrow">▼</span></button><div class="faq-body">Free same-day or next-day pickup for corporate clients with 50+ units anywhere in Ernakulam district. Walk-in at our Thrippunithura facility is always free. For smaller lots needing pickup, a nominal logistics charge may apply — we'll always be upfront.</div></div>
    <div class="faq-item"><button class="faq-btn" onclick="toggleFaq(this)"><span>Am I legally liable if I give laptops to a scrap dealer?</span><span class="faq-arrow">▼</span></button><div class="faq-body">Yes — on two counts. Under E-Waste Management Rules 2022, businesses must use KSPCB-authorized facilities only. Under DPDP Act 2023, if data is later recovered from that device, you remain liable as the original Data Fiduciary. The Certificate of Destruction from EWaste Kochi is your legal protection.</div></div>
    <div class="faq-item"><button class="faq-btn" onclick="toggleFaq(this)"><span>How quickly do I get paid for buyback devices?</span><span class="faq-arrow">▼</span></button><div class="faq-body">Same day in most cases. Once physical inspection confirms the device matches the description, payment is transferred via UPI, NEFT, or bank transfer immediately. Corporate lots settle within one business day of device receipt.</div></div>
    <div class="faq-item"><button class="faq-btn" onclick="toggleFaq(this)"><span>Do you accept non-working or damaged laptops?</span><span class="faq-arrow">▼</span></button><div class="faq-body">Yes. We accept damaged, non-working, and end-of-life devices. Pricing reflects condition but we never reject devices unlike Cashify. Corporate lots with mixed working/non-working units receive a blended price.</div></div>
    <div class="faq-item"><button class="faq-btn" onclick="toggleFaq(this)"><span>Can you do on-site data destruction at our office?</span><span class="faq-arrow">▼</span></button><div class="faq-body">Yes. For banks, hospitals, and government departments, we offer on-site hard drive shredding and degaussing. Our team brings equipment to your premises, destroys drives in your presence, and issues the Certificate of Destruction on-site.</div></div>
    <div class="faq-item"><button class="faq-btn" onclick="toggleFaq(this)"><span>What is NIST 800-88 and how is it different from factory reset?</span><span class="faq-arrow">▼</span></button><div class="faq-body">NIST 800-88 is the US government data sanitization standard. It overwrites every storage location multiple times with verified bit patterns — making data mathematically impossible to reconstruct. A factory reset simply removes the pointer to data, leaving the actual bits physically intact and fully recoverable.</div></div>
    <div class="faq-item"><button class="faq-btn" onclick="toggleFaq(this)"><span>Are you really authorized to handle e-waste in Kerala?</span><span class="faq-arrow">▼</span></button><div class="faq-body">EWaste Kochi operates in full compliance with E-Waste Management Rules 2022 and follows all KSPCB requirements for authorized e-waste recycling in Kerala. We can provide our authorization documentation to corporate clients for their compliance records upon request.</div></div>
    <div class="text-center mt-40">
      <p style="color:var(--muted);margin-bottom:16px">More questions? Our chatbot answers 24/7.</p>
      <a href="javascript:openChat()" class="btn btn-outline">💬 Chat With Us</a>
    </div>
  </div>
</div>"""
    },
    "about.html": {
        "title": "About EWaste Kochi — Certified ITAD & E-Waste Recycling Kerala",
        "meta": "About EWaste Kochi — Kerala's most trusted certified ITAD and e-waste recycling facility. KSPCB authorized, NIST 800-88 certified, DPDP Act compliant since 2019.",
        "canonical": "/about.html",
        "body": """
<div class="page-hero">
  <div class="wrap">
    <div class="page-hero-tag">🏢 About Us</div>
    <h1 class="page-hero-title">Kochi's Most Trusted <em>Certified ITAD</em> Partner</h1>
    <p class="page-hero-desc">Kerala PCB authorization compliant, NIST 800-88 certified methodology, DPDP Act 2023 compliant. Serving Kochi's IT sector since 2019 with zero data breach incidents.</p>
  </div>
</div>
<div class="section">
  <div class="wrap">
    <div class="grid-2">
      <div>
        <div class="section-tag">Our Story</div>
        <h2 class="section-title" style="font-size:1.5rem">Who We Are</h2>
        <p style="color:var(--text);line-height:1.8;margin-bottom:16px">EWaste Kochi was founded to solve a critical gap in the Kerala market: the lack of a certified, professional IT Asset Disposition company that genuinely protects businesses from data breach liability while maximizing the value they recover from retired hardware.</p>
        <p style="color:var(--text);line-height:1.8;margin-bottom:24px">Our facility on Hill Palace Road, Thrippunithura is Kochi's only dedicated ITAD facility with NIST 800-88 certified wiping capabilities, physical shredding infrastructure, and DPDP Act 2023 compliant documentation systems.</p>
        <div class="grid-2" style="gap:12px">
          <div class="card" style="text-align:center"><div style="font-size:2rem;font-weight:800;color:var(--green);font-family:var(--font-h)" data-count="5200" data-suffix="+">5200+</div><div style="font-size:.75rem;color:var(--muted)">Devices Processed</div></div>
          <div class="card" style="text-align:center"><div style="font-size:2rem;font-weight:800;color:var(--green);font-family:var(--font-h)" data-count="200" data-suffix="+">200+</div><div style="font-size:.75rem;color:var(--muted)">Corporate Clients</div></div>
          <div class="card" style="text-align:center"><div style="font-size:2rem;font-weight:800;color:var(--green);font-family:var(--font-h)">0</div><div style="font-size:.75rem;color:var(--muted)">Data Breach Incidents</div></div>
          <div class="card" style="text-align:center"><div style="font-size:2rem;font-weight:800;color:var(--green);font-family:var(--font-h)">100%</div><div style="font-size:.75rem;color:var(--muted)">CoD Issuance Rate</div></div>
        </div>
      </div>
      <div>
        <div class="section-tag">Certifications</div>
        <h2 class="section-title" style="font-size:1.5rem">Our Standards</h2>
        <div style="display:flex;flex-direction:column;gap:12px">
          <div class="card" style="display:flex;gap:12px;align-items:center"><span style="font-size:1.5rem">🌿</span><div><div style="color:var(--white);font-weight:600;font-size:.88rem">KSPCB Authorization Compliant</div><div style="color:var(--muted);font-size:.75rem">Operating per Kerala State Pollution Control Board requirements for certified e-waste recycling</div></div></div>
          <div class="card" style="display:flex;gap:12px;align-items:center"><span style="font-size:1.5rem">🔒</span><div><div style="color:var(--white);font-weight:600;font-size:.88rem">NIST 800-88 Methodology</div><div style="color:var(--muted);font-size:.75rem">Data sanitization following US NIST standards — highest civilian data destruction benchmark</div></div></div>
          <div class="card" style="display:flex;gap:12px;align-items:center"><span style="font-size:1.5rem">🛡️</span><div><div style="color:var(--white);font-weight:600;font-size:.88rem">DoD 5220.22-M Capable</div><div style="color:var(--muted);font-size:.75rem">Department of Defense standard for government and high-security financial clients</div></div></div>
          <div class="card" style="display:flex;gap:12px;align-items:center"><span style="font-size:1.5rem">📋</span><div><div style="color:var(--white);font-weight:600;font-size:.88rem">DPDP Act 2023 Compliant</div><div style="color:var(--muted);font-size:.75rem">Full compliance with India's Digital Personal Data Protection Act — complete documentation trail</div></div></div>
          <div class="card" style="display:flex;gap:12px;align-items:center"><span style="font-size:1.5rem">♻️</span><div><div style="color:var(--white);font-weight:600;font-size:.88rem">EPR Framework Registered</div><div style="color:var(--muted);font-size:.75rem">Extended Producer Responsibility registration for proper materials recycling channelling</div></div></div>
        </div>
      </div>
    </div>
  </div>
</div>"""
    },
}

# ═══════════════════════════════════════════════════════════════════════
# GENERATE ALL PAGES
# ═══════════════════════════════════════════════════════════════════════

def generate_all():
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(base)
    print(f"\n{'='*60}")
    print("  EWasteKochi.com — Full Site Generator")
    print(f"{'='*60}\n")
    count = 0

    # Core pages
    print("📄 Core pages...")
    for filename, data in CORE_PAGES.items():
        bc = breadcrumb_html([("Home", "/"), (data["title"].split("—")[0].strip(), None)])
        page = html_page(data["title"], data["meta"], data["canonical"], body_content=data["body"], breadcrumb=bc)
        write(filename, page)
        count += 1

    # Location pages (named locations)
    print("\n📍 Location pages...")
    for name, slug, dist, landmarks in LOCATIONS:
        write(f"locations/ewaste-{slug}.html", gen_location_page(name, slug, dist, landmarks))
        count += 1

    # Location pages (pincode-based)
    print("📍 Pincode location pages...")
    for pincode, area in ERNAKULAM_PINCODES:
        slug = pincode
        page = gen_location_page(f"{area} ({pincode})", slug, "Ernakulam district", f"Pin {pincode}, {area}")
        write(f"locations/ewaste-{slug}.html", page)
        count += 1

    # Blog articles
    print("\n📚 Blog articles...")
    for slug, title, meta, tag, cat, color in BLOG_ARTICLES:
        write(f"blog/{slug}", gen_blog_page(slug, title, meta, tag, cat, color))
        count += 1

    # Industry pages
    print("\n🏭 Industry pages...")
    for slug, title, meta, icon, sector, cert, detail in INDUSTRIES:
        write(f"industries/{slug}", gen_industry_page(slug, title, meta, icon, sector, cert, detail))
        count += 1

    # Compliance pages
    print("\n⚖️ Compliance pages...")
    for slug, title, meta, std, icon in COMPLIANCE_PAGES:
        write(f"compliance/{slug}", gen_compliance_page(slug, title, meta, std, icon))
        count += 1

    # Comparison pages
    print("\n⚔️ Comparison pages...")
    for slug, title, meta, competitor, color in COMPARISONS:
        write(f"comparisons/{slug}", gen_comparison_page(slug, title, meta, competitor, color))
        count += 1

    print(f"\n{'='*60}")
    print(f"  ✅ Generated {count} pages successfully")
    print(f"{'='*60}\n")
    return count


if __name__ == "__main__":
    generate_all()
