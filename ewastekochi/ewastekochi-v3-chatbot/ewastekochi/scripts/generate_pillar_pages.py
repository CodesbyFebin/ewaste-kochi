#!/usr/bin/env python3
"""
EWasteKochi.in — 10 Pillar Pages + AI Chatbot Generator
Generates all 10 pillar pages with the AI chatbot system embedded.

Run from project root:
    python3 scripts/generate_pillar_pages.py
"""

import os
from datetime import datetime

SITE_URL = "https://ewastekochi.in"
PHONE    = "+91-XXXXXXXXXX"
WA_NUM   = "91XXXXXXXXXX"
EMAIL    = "info@ewastekochi.in"
YEAR     = datetime.now().year

# ── CHATBOT EMBED ────────────────────────────────────────────
# The full chatbot CSS + HTML + JS extracted from chatbot-embed.html
# In production: <link rel="stylesheet" href="/assets/chatbot.css">
#                <script src="/assets/chatbot.js"></script>
# For now, we reference the embed file inline via include pattern.
# The generator reads the embed and extracts the style/script blocks.

def read_chatbot_assets():
    """Read chatbot-embed.html and extract embeddable CSS + JS."""
    try:
        with open("chatbot-embed.html", "r", encoding="utf-8") as f:
            content = f.read()

        import re
        # Extract style block (id="ew-chat-styles")
        style_match = re.search(r'<style id="ew-chat-styles">(.*?)</style>', content, re.DOTALL)
        # Extract script block (the IIFE)
        script_match = re.search(r'<script>\s*\(function\(\).*?</script>', content, re.DOTALL)
        # Extract root div
        div_match = re.search(r'(<div id="ew-chat-root"></div>)', content)

        style = f'<style id="ew-chat-styles">{style_match.group(1)}</style>' if style_match else ''
        script = script_match.group(0) if script_match else ''
        div = div_match.group(1) if div_match else '<div id="ew-chat-root"></div>'

        return style, div, script
    except FileNotFoundError:
        print("  ⚠️  chatbot-embed.html not found — embedding placeholder")
        return (
            '<style>/* chatbot styles here */</style>',
            '<div id="ew-chat-root"></div>',
            '<script>/* chatbot script here */</script>'
        )

CHAT_STYLE, CHAT_DIV, CHAT_SCRIPT = read_chatbot_assets()

# ── SHARED PAGE COMPONENTS ───────────────────────────────────
SHARED_FONTS = """<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" href="https://fonts.googleapis.com/css2?family=Syne:wght@700;800;900&family=DM+Sans:wght@300;400;500;600&family=IBM+Plex+Mono:wght@400;600&display=swap" as="style" onload="this.onload=null;this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Syne:wght@700;800;900&family=DM+Sans:wght@300;400;500;600&family=IBM+Plex+Mono:wght@400;600&display=swap"></noscript>"""

SHARED_CSS = """<style>
:root{--bg:#07100A;--bg2:#0B170E;--surf:#152018;--surf2:#1C2B1F;--b:rgba(0,232,122,.12);--b2:rgba(0,232,122,.22);--g:#00E87A;--g2:#00C463;--lime:#B4FF5C;--amber:#F5A827;--red:#FF4D6D;--white:#F0F7F2;--text:#A8C4AE;--muted:#5A7A62;}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
html{scroll-behavior:smooth;font-size:16px;}
body{font-family:'DM Sans',system-ui,sans-serif;background:var(--bg);color:var(--text);line-height:1.65;overflow-x:hidden;-webkit-font-smoothing:antialiased;}
body::before{content:'';position:fixed;inset:0;background-image:linear-gradient(rgba(0,232,122,.02) 1px,transparent 1px),linear-gradient(90deg,rgba(0,232,122,.02) 1px,transparent 1px);background-size:48px 48px;pointer-events:none;z-index:0;}
a{color:inherit;text-decoration:none;}
::selection{background:var(--g);color:var(--bg);}
::-webkit-scrollbar{width:5px;}::-webkit-scrollbar-track{background:var(--bg);}::-webkit-scrollbar-thumb{background:var(--g2);border-radius:3px;}
.wrap{max-width:1200px;margin:0 auto;padding:0 2rem;position:relative;z-index:1;}
.g{color:var(--g);}
/* topbar */
.topbar{background:var(--g);color:var(--bg);font-family:'IBM Plex Mono',monospace;font-size:.7rem;font-weight:700;padding:7px 0;text-align:center;letter-spacing:.5px;overflow:hidden;white-space:nowrap;position:relative;z-index:200;}
.topbar-inner{display:inline-flex;animation:ticker 40s linear infinite;}
.ti{padding:0 3rem;}
@keyframes ticker{from{transform:translateX(0);}to{transform:translateX(-50%);}}
/* nav */
.nav{position:sticky;top:0;background:rgba(7,16,10,.96);border-bottom:1px solid var(--b);z-index:100;backdrop-filter:blur(8px);}
.nav-inner{max-width:1200px;margin:0 auto;padding:0 2rem;height:66px;display:flex;align-items:center;justify-content:space-between;}
.logo{font-family:'Syne',sans-serif;font-size:1.3rem;font-weight:900;color:var(--white);}
.logo span{color:var(--g);}
.nb{font-size:.58rem;background:var(--g);color:var(--bg);padding:2px 7px;border-radius:3px;margin-left:.4rem;}
.nav-cta{display:flex;gap:.6rem;}
.btn,.btn-out{display:inline-flex;align-items:center;gap:.4rem;padding:.65rem 1.4rem;border-radius:6px;font-weight:700;font-size:.88rem;cursor:pointer;transition:all .2s;text-decoration:none;}
.btn{background:var(--g);color:var(--bg);}
.btn:hover{background:var(--lime);transform:translateY(-1px);}
.btn-out{border:1.5px solid var(--b2);color:var(--text);}
.btn-out:hover{border-color:var(--g);color:var(--g);}
.btn-wa{background:#25D366;color:#fff;border:none;}
.btn-wa:hover{background:#1db954;}
/* hero */
.hero{padding:72px 0 56px;position:relative;overflow:hidden;}
.hero::after{content:'';position:absolute;top:-30%;right:-10%;width:600px;height:600px;border-radius:50%;background:radial-gradient(circle,rgba(0,232,122,.06) 0%,transparent 65%);pointer-events:none;}
.pill{display:inline-flex;align-items:center;gap:.3rem;font-family:'IBM Plex Mono',monospace;font-size:.67rem;letter-spacing:1.5px;text-transform:uppercase;padding:.3rem .85rem;border-radius:3px;margin:.2rem;}
.pill-g{background:rgba(0,232,122,.1);border:1px solid rgba(0,232,122,.3);color:var(--g);}
.pill-a{background:rgba(245,168,39,.08);border:1px solid rgba(245,168,39,.25);color:var(--amber);}
.pill-r{background:rgba(255,77,109,.08);border:1px solid rgba(255,77,109,.22);color:var(--red);}
h1{font-family:'Syne',sans-serif;font-size:clamp(2.2rem,5vw,3.8rem);font-weight:900;color:var(--white);line-height:1.04;letter-spacing:-1.5px;margin-bottom:1.25rem;}
h1 em{font-style:normal;color:var(--g);}
h2{font-family:'Syne',sans-serif;font-size:clamp(1.6rem,3.5vw,2.4rem);font-weight:800;color:var(--white);line-height:1.08;letter-spacing:-0.5px;margin-bottom:1rem;}
h3{font-family:'Syne',sans-serif;font-size:1.15rem;font-weight:800;color:var(--white);margin-bottom:.65rem;}
.lead{font-size:1.05rem;color:var(--text);line-height:1.8;max-width:660px;margin-bottom:2rem;}
.tag{font-family:'IBM Plex Mono',monospace;font-size:.68rem;letter-spacing:2.5px;text-transform:uppercase;color:var(--g);display:flex;align-items:center;gap:.5rem;margin-bottom:1rem;}
.tag::before{content:'';width:16px;height:2px;background:var(--g);}
.tag.amber{color:var(--amber);}.tag.amber::before{background:var(--amber);}
/* sections */
.section{padding:72px 0;}.section-alt{background:var(--bg2);}.section-dark{background:rgba(0,0,0,.2);}
.badge{display:inline-flex;align-items:center;gap:.3rem;font-family:'IBM Plex Mono',monospace;font-size:.67rem;letter-spacing:1px;text-transform:uppercase;padding:.3rem .8rem;border-radius:4px;border:1px solid var(--b2);color:var(--g);background:rgba(0,232,122,.06);margin:.2rem;}
.badge.amber{border-color:rgba(245,168,39,.3);color:var(--amber);background:rgba(245,168,39,.06);}
.badge.red{border-color:rgba(255,77,109,.3);color:var(--red);background:rgba(255,77,109,.06);}
.card{background:var(--surf);border:1px solid var(--b);border-radius:12px;padding:1.75rem;transition:all .25s;}
.card:hover{border-color:var(--b2);transform:translateY(-2px);box-shadow:0 12px 32px rgba(0,0,0,.4);}
.grid-2{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:1.5rem;}
.grid-3{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:1.25rem;}
.alert{background:rgba(255,77,109,.07);border-left:4px solid var(--red);padding:1.1rem 1.4rem;border-radius:0 8px 8px 0;margin:1.5rem 0;font-size:.93rem;line-height:1.65;}
.alert strong{color:var(--amber);}
.cta-box{background:linear-gradient(135deg,var(--surf),rgba(0,232,122,.04));border:1px solid var(--b);border-radius:14px;padding:2rem 2.25rem;display:flex;align-items:center;justify-content:space-between;gap:2rem;flex-wrap:wrap;margin:3rem 0;}
.cta-box h3{font-size:1.3rem;color:var(--white);margin-bottom:.3rem;}
.cta-box p{font-size:.88rem;color:var(--muted);}
.cta-btns{display:flex;gap:.65rem;flex-wrap:wrap;}
.check-list{list-style:none;display:flex;flex-direction:column;gap:.6rem;}
.check-list li{display:flex;align-items:flex-start;gap:.65rem;font-size:.92rem;color:var(--text);line-height:1.65;}
.check-list li::before{content:'✓';color:var(--g);font-weight:700;flex-shrink:0;margin-top:1px;}
.stat-row{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:1rem;}
.stat{background:var(--surf);border:1px solid var(--b);border-radius:10px;padding:1.5rem;text-align:center;}
.stat .n{font-family:'Syne',sans-serif;font-size:2.2rem;font-weight:900;color:var(--g);line-height:1;}
.stat .l{font-size:.78rem;color:var(--muted);margin-top:.4rem;}
.breadcrumb{font-size:.8rem;color:var(--muted);padding:.5rem 0 1rem;}
.breadcrumb a{color:var(--g);}
.breadcrumb span{margin:0 .35rem;}
/* trust bar */
.trust-bar{display:flex;gap:1.5rem;flex-wrap:wrap;padding:1.25rem 1.75rem;background:rgba(0,232,122,.04);border:1px solid var(--b);border-radius:10px;margin-top:2rem;}
.trust-item{font-size:.85rem;color:var(--text);font-weight:500;display:flex;align-items:center;gap:.4rem;}
.live-dot{width:7px;height:7px;border-radius:50%;background:var(--g);box-shadow:0 0 6px var(--g);animation:pulse 2s infinite;flex-shrink:0;}
@keyframes pulse{0%,100%{opacity:1;}50%{opacity:.3;}}
/* footer */
.footer{background:var(--bg2);border-top:1px solid var(--b);padding:48px 0 28px;}
.footer-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:2rem;margin-bottom:2rem;}
.footer-grid h4{font-family:'IBM Plex Mono',monospace;font-size:.68rem;text-transform:uppercase;letter-spacing:2px;color:var(--g);margin-bottom:1rem;}
.footer-grid a{display:block;font-size:.84rem;color:var(--muted);margin-bottom:.5rem;transition:color .2s;}
.footer-grid a:hover{color:var(--white);}
.footer-grid p{font-size:.84rem;color:var(--muted);line-height:1.65;margin-bottom:.6rem;}
.fl{font-family:'Syne',sans-serif;font-size:1.2rem;font-weight:900;color:var(--white);display:block;margin-bottom:.6rem;}
.fl span{color:var(--g);}
.footer-bottom{border-top:1px solid var(--b);padding-top:1.25rem;font-size:.76rem;color:var(--muted);display:flex;justify-content:space-between;flex-wrap:wrap;gap:.5rem;}
.footer-bottom a{color:var(--muted);transition:color .2s;}.footer-bottom a:hover{color:var(--g);}
@media(max-width:768px){.section{padding:48px 0;}.wrap{padding:0 1.25rem;}.nav-cta .btn-out{display:none;}.cta-box{flex-direction:column;}.grid-2,.grid-3{grid-template-columns:1fr;}.stat-row{grid-template-columns:repeat(2,1fr);}}
</style>"""

def nav_html():
    ticks = ["⚡ FREE Pickup 50+ Units · Ernakulam","🔒 NIST 800-88 · Certificate of Destruction Every Job","💰 MacBooks up to ₹65,000 · iPhones up to ₹75,000","✓ KSPCB Authorized · DPDP Act 2023 Compliant"]
    ticks_html = "".join([f'<span class="ti">{t}</span>' for t in ticks*2])
    return f"""<div class="topbar" aria-hidden="true"><div class="topbar-inner">{ticks_html}</div></div>
<nav class="nav"><div class="nav-inner">
  <a href="/" class="logo"><span>EWaste</span>Kochi<span class="nb">KSPCB CERT.</span></a>
  <div class="nav-cta">
    <a href="tel:{PHONE}" class="btn-out">📞 Call</a>
    <a href="/book-free-pickup-kochi.html" class="btn">Book Pickup →</a>
  </div>
</div></nav>"""

def footer_html():
    return f"""<footer class="footer"><div class="wrap">
  <div class="footer-grid">
    <div>
      <span class="fl"><span>EWaste</span>Kochi</span>
      <p>Kerala's #1 certified ITAD & e-waste recycling facility. KSPCB Authorized. NIST 800-88. DPDP Act 2023 compliant.</p>
      <p>📍 710A Hill Palace Rd, Thrippunithura, Kochi 682301</p>
      <p>📞 <a href="tel:{PHONE}">{PHONE}</a> · ✉️ <a href="mailto:{EMAIL}">{EMAIL}</a></p>
    </div>
    <div><h4>Services</h4>
      <a href="/services/corporate-itad-kochi.html">Corporate ITAD</a>
      <a href="/services/data-destruction-kochi.html">Data Destruction</a>
      <a href="/services/hard-drive-shredding-kochi.html">Hard Drive Shredding</a>
      <a href="/services/laptop-buyback-kochi.html">Laptop Buyback</a>
      <a href="/services/phone-buyback-kochi.html">Phone Buyback</a>
    </div>
    <div><h4>Compliance</h4>
      <a href="/compliance/dpdp-act-2023-penalties.html">DPDP Act 2023</a>
      <a href="/compliance/nist-800-88-explained.html">NIST 800-88</a>
      <a href="/compliance/certificate-of-destruction.html">Certificate of Destruction</a>
      <a href="/compliance/kspcb-authorization.html">KSPCB Authorization</a>
    </div>
    <div><h4>Company</h4>
      <a href="/about.html">About Us</a>
      <a href="/blog/">Blog</a>
      <a href="/faq.html">FAQ</a>
      <a href="/contact.html">Contact</a>
    </div>
  </div>
  <div class="footer-bottom">
    <span>© {YEAR} EWasteKochi. KSPCB Authorized Recycler.</span>
    <span><a href="/privacy-policy.html">Privacy</a> · <a href="/terms-of-service.html">Terms</a> · <a href="/refund-policy.html">Refund</a></span>
  </div>
</div></footer>"""

def cta_box(h="Ready to Get Started?", p="Free pickup · Certificate of Destruction · 2-hour response."):
    return f"""<div class="cta-box"><div><h3>{h}</h3><p>{p}</p></div>
<div class="cta-btns">
  <a href="/book-free-pickup-kochi.html" class="btn">🚚 Book Free Pickup →</a>
  <a href="https://wa.me/{WA_NUM}?text=Hi%2C%20I%20need%20a%20quote%20for%20e-waste%20services%20in%20Kochi" class="btn-wa" target="_blank" rel="noopener">💬 WhatsApp</a>
  <a href="tel:{PHONE}" class="btn-out">📞 Call</a>
</div></div>"""

def page_wrap(pillar_key, title, meta, canonical, hero_section, main_content):
    """Wrap a pillar page with all shared elements + chatbot embed."""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{meta}">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{meta}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE_URL}/images/og-ewastekochi.webp">
<meta name="twitter:card" content="summary_large_image">
<meta name="robots" content="index, follow">
<!-- GTM — replace GTM-XXXXXXX -->
<script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);}})(window,document,'script','dataLayer','GTM-XXXXXXX');</script>
{SHARED_FONTS}
{SHARED_CSS}
{CHAT_STYLE}
</head>
<body data-page="{pillar_key}">
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-XXXXXXX" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
{nav_html()}
<main>
{hero_section}
{main_content}
</main>
{footer_html()}
{CHAT_DIV}
{CHAT_SCRIPT}
</body>
</html>"""

# ════════════════════════════════════════════════════════════
# 10 PILLAR PAGES
# ════════════════════════════════════════════════════════════

PILLAR_PAGES = [

  # ── 1. COLLECTION ────────────────────────────────────────
  {
    "key": "collection",
    "slug": "pillars/ewaste-collection-kochi.html",
    "title": "E-Waste Collection Kochi | Free Same-Day Pickup | KSPCB Authorized",
    "meta": "Free e-waste collection in Kochi. Same-day or next-day pickup for 50+ units across Ernakulam. KSPCB authorized. Certificate of Destruction. Book via WhatsApp in 30 seconds.",
    "canonical": f"{SITE_URL}/pillars/ewaste-collection-kochi.html",
    "hero": """<section class="hero">
  <div class="wrap">
    <div style="display:flex;gap:.4rem;flex-wrap:wrap;margin-bottom:1.5rem;">
      <span class="pill pill-g">✓ KSPCB Authorized</span>
      <span class="pill pill-a">⚡ Same-Day Available</span>
      <span class="pill pill-g">🚛 Free for 50+ Units</span>
    </div>
    <div class="tag">E-Waste Collection · Kochi</div>
    <h1>Free E-Waste Collection<br>in <em>Kochi</em> —<br>Book in 30 Seconds</h1>
    <p class="lead">Same-day or next-day pickup across all of Ernakulam district. Free for 50+ units. Walk-in at Thrippunithura Mon–Sat 8AM–8PM. Chain-of-custody manifest at your door.</p>
    <div style="display:flex;gap:1rem;flex-wrap:wrap;margin-bottom:2rem;">
      <a href="/book-free-pickup-kochi.html" class="btn">🚛 Book Today's Slot →</a>
      <a href="https://wa.me/91XXXXXXXXXX?text=Hi%2C+I+want+to+book+a+free+e-waste+pickup+in+Kochi+today" class="btn-wa" target="_blank" rel="noopener">💬 WhatsApp to Book</a>
    </div>
    <div class="trust-bar">
      <span class="trust-item"><span class="live-dot"></span>Live: 5,200+ Devices Collected</span>
      <span class="trust-item">⭐ 4.9 · 243 Google Reviews</span>
      <span class="trust-item">🚛 Same-day in Kakkanad, Edappally, Vyttila</span>
      <span class="trust-item">🔒 Chain-of-custody from your door</span>
    </div>
  </div>
</section>""",
    "body": f"""<section class="section section-alt">
  <div class="wrap">
    <div class="grid-2">
      <div class="card">
        <h3 style="margin-bottom:1rem;">How Collection Works</h3>
        <ol style="padding-left:1.25rem;display:flex;flex-direction:column;gap:.7rem;font-size:.92rem;color:var(--text);">
          <li><strong style="color:var(--white);">WhatsApp by 12PM</strong> — We confirm your slot within 1 hour.</li>
          <li><strong style="color:var(--white);">We arrive at your location</strong> — Our team brings packaging and chain-of-custody forms.</li>
          <li><strong style="color:var(--white);">Everything is logged</strong> — Every item inventoried by serial number on-site.</li>
          <li><strong style="color:var(--white);">Certificate issued</strong> — Certificate of Destruction within 48 hours by email.</li>
        </ol>
      </div>
      <div class="card">
        <h3 style="margin-bottom:1rem;">Free Pickup Coverage</h3>
        <ul class="check-list">
          <li>Kakkanad / Infopark — same-day, priority zone</li>
          <li>Edappally / Vyttila / Palarivattom</li>
          <li>Thrippunithura / Maradu</li>
          <li>Ernakulam South / MG Road</li>
          <li>Aluva / Perumbavoor / Angamaly</li>
          <li>Fort Kochi / Kalamassery</li>
          <li>+ 40 more Ernakulam pincodes</li>
        </ul>
      </div>
    </div>
    <div class="alert" style="margin-top:2rem;">⚠️ <strong>DPDP Act 2023:</strong> Collection by an unauthorized vendor exposes your business to penalties up to <strong>₹250 Crore</strong>. Only KSPCB-authorized collectors like EWasteKochi satisfy the legal requirement.</div>
    {cta_box("Book Your Free Collection", "Same-day slots fill fast. WhatsApp by 12PM.")}
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="tag">What We Collect</div>
    <h2>Every Type of E-Waste Accepted</h2>
    <div class="grid-3">
      {''.join([f'<div class="card" style="text-align:center;"><div style="font-size:2rem;margin-bottom:.75rem;">{icon}</div><h3 style="font-size:1rem;">{name}</h3><p style="font-size:.84rem;color:var(--muted);margin-top:.3rem;">{desc}</p></div>' for icon, name, desc in [
        ("💻","Laptops & MacBooks","All brands, all conditions"),
        ("📱","Smartphones & Tablets","iPhone, Samsung, all brands"),
        ("🖥️","Desktops & Monitors","CRT, LCD, all sizes"),
        ("🖨️","Printers & Peripherals","Keyboards, mice, scanners"),
        ("🔌","Servers & Network Gear","Racks, switches, routers"),
        ("🔋","Batteries & UPS","Li-ion, lead-acid, NiMH"),
        ("📺","TVs & Displays","All screen types"),
        ("🎮","Gaming Consoles","All brands and generations"),
        ("🔧","Industrial Electronics","PLC, CNC terminals, OT"),
      ]])}
    </div>
  </div>
</section>""",
  },

  # ── 2. RECYCLING ─────────────────────────────────────────
  {
    "key": "recycling",
    "slug": "pillars/ewaste-recycling-kochi.html",
    "title": "E-Waste Recycling Kochi | KSPCB Certified | 100% Responsible Processing",
    "meta": "Certified e-waste recycling in Kochi. KSPCB authorized. Zero landfill. Precious metal recovery. DPDP Act 2023 compliant. CSR-eligible documentation. Certificate of Responsible Recycling.",
    "canonical": f"{SITE_URL}/pillars/ewaste-recycling-kochi.html",
    "hero": """<section class="hero">
  <div class="wrap">
    <div style="display:flex;gap:.4rem;flex-wrap:wrap;margin-bottom:1.5rem;">
      <span class="pill pill-g">✓ KSPCB Authorized</span>
      <span class="pill pill-g">🌿 Zero Landfill</span>
      <span class="pill pill-a">📋 CSR Eligible</span>
    </div>
    <div class="tag">Eco-Certified Recycling · Kerala</div>
    <h1>E-Waste Recycling in<br><em>Kochi</em> Done Right —<br>Zero Landfill, 100%<br>Certified</h1>
    <p class="lead">Kerala's KSPCB-authorized facility. Nothing we collect ends in a landfill. Precious metals recovered responsibly. Hazardous components channelled through certified streams. CSR-eligible documentation for your sustainability reports.</p>
    <div style="display:flex;gap:1rem;flex-wrap:wrap;margin-bottom:2rem;">
      <a href="/book-free-pickup-kochi.html" class="btn">♻️ Schedule Collection →</a>
      <a href="https://wa.me/91XXXXXXXXXX?text=Hi%2C+I+want+to+recycle+e-waste+responsibly+in+Kochi" class="btn-wa" target="_blank" rel="noopener">💬 Ask About CSR Drives</a>
    </div>
    <div class="trust-bar">
      <span class="trust-item">🌱 100% responsible — zero landfill</span>
      <span class="trust-item">✓ KSPCB Authorization — only legal recycler</span>
      <span class="trust-item">📋 CSR + EPR compliance docs available</span>
      <span class="trust-item">🌿 Haritha Karma Sena partner</span>
    </div>
  </div>
</section>""",
    "body": f"""<section class="section section-alt">
  <div class="wrap">
    <div class="tag">What Actually Happens</div>
    <h2>What Happens to Your Device<br>After We Collect It</h2>
    <p class="lead">Most recyclers don't tell you this. We do — because transparency is how trust is built.</p>
    <div class="grid-3">
      {''.join([f'<div class="card"><div style="font-size:1.8rem;margin-bottom:.75rem;">{icon}</div><h3>{title}</h3><p style="font-size:.88rem;color:var(--text);line-height:1.7;margin-top:.4rem;">{body}</p></div>' for icon, title, body in [
        ("📋","1. Intake & Inventory","Every device is logged by serial number. Chain-of-custody manifest is created and shared with you."),
        ("🔒","2. Data Sanitisation","All storage media receives NIST 800-88 Purge. Your data is gone before any device is touched for disassembly."),
        ("🔬","3. Grading & Assessment","Devices are graded for refurbishment potential. Working devices go to refurbishment, not landfill."),
        ("⚗️","4. Component Recovery","Non-refurbishable devices are disassembled. Gold, silver, copper, aluminium, and rare earth magnets are extracted."),
        ("☢️","5. Hazmat Processing","Batteries, CRT glass, and capacitors go to designated hazardous material recycling streams — KSPCB compliant."),
        ("📜","6. Certificate Issued","Certificate of Responsible Recycling issued per batch. CSR-eligible PDF for your sustainability reports."),
      ]])}
    </div>
    {cta_box("Schedule Your Collection", "Free pickup · Zero landfill · CSR documentation included.")}
  </div>
</section>""",
  },

  # ── 3. LAPTOP DISPOSAL ───────────────────────────────────
  {
    "key": "laptop",
    "slug": "pillars/laptop-disposal-kochi.html",
    "title": "Sell Old Laptop Kochi | Up to ₹65,000 | Data Secure | 15–20% Above Cashify",
    "meta": "Sell your old laptop in Kochi and get maximum value. MacBook Pro up to ₹65,000. ThinkPad, Dell, HP business laptops up to ₹35,000. NIST 800-88 data wipe. Certificate of Destruction. Same-day UPI payment.",
    "canonical": f"{SITE_URL}/pillars/laptop-disposal-kochi.html",
    "hero": """<section class="hero">
  <div class="wrap">
    <div style="display:flex;gap:.4rem;flex-wrap:wrap;margin-bottom:1.5rem;">
      <span class="pill pill-a">💰 15–20% Above Cashify</span>
      <span class="pill pill-g">🔒 NIST 800-88 Data Wipe</span>
      <span class="pill pill-g">⚡ Same-Day Payment</span>
    </div>
    <div class="tag">Laptop Buyback · Kochi</div>
    <h1>Sell Your Old Laptop<br>in Kochi.<br><em>Get More.</em><br>Data 100% Secure.</h1>
    <p class="lead">We pay more than Cashify — consistently — because our refurbishment channels unlock higher value. Every sale includes a NIST 800-88 data wipe and Certificate of Destruction. Same-day UPI payment.</p>
    <div style="display:flex;gap:.75rem;flex-wrap:wrap;margin-bottom:1.5rem;">
      <div style="background:var(--surf);border:1px solid var(--b2);border-radius:8px;padding:1rem 1.25rem;text-align:center;">
        <div style="font-family:'Syne',sans-serif;font-size:2rem;font-weight:900;color:var(--g);line-height:1;">₹65K</div>
        <div style="font-size:.78rem;color:var(--muted);margin-top:.2rem;">MacBook Pro M3</div>
      </div>
      <div style="background:var(--surf);border:1px solid var(--b2);border-radius:8px;padding:1rem 1.25rem;text-align:center;">
        <div style="font-family:'Syne',sans-serif;font-size:2rem;font-weight:900;color:var(--amber);line-height:1;">₹35K</div>
        <div style="font-size:.78rem;color:var(--muted);margin-top:.2rem;">ThinkPad X1 Carbon</div>
      </div>
      <div style="background:var(--surf);border:1px solid var(--b2);border-radius:8px;padding:1rem 1.25rem;text-align:center;">
        <div style="font-family:'Syne',sans-serif;font-size:2rem;font-weight:900;color:var(--g);line-height:1;">₹32K</div>
        <div style="font-size:.78rem;color:var(--muted);margin-top:.2rem;">Dell Latitude 7430</div>
      </div>
    </div>
    <div style="display:flex;gap:1rem;flex-wrap:wrap;margin-bottom:2rem;">
      <a href="/book-free-pickup-kochi.html" class="btn">📋 Get Free Valuation →</a>
      <a href="https://wa.me/91XXXXXXXXXX?text=Hi%2C+I+want+to+sell+my+laptop+in+Kochi.+Model%3A+" class="btn-wa" target="_blank" rel="noopener">💬 WhatsApp for Price</a>
    </div>
    <div class="trust-bar">
      <span class="trust-item">💰 15–20% above Cashify on business laptops</span>
      <span class="trust-item">🔒 NIST 800-88 data wipe — legally certified</span>
      <span class="trust-item">⚡ Same-day UPI / cash payment</span>
      <span class="trust-item">📋 Certificate of Destruction emailed</span>
    </div>
  </div>
</section>""",
    "body": f"""<section class="section section-alt">
  <div class="wrap">
    <div class="tag">Current Prices · March {YEAR}</div>
    <h2>What We Pay vs. Cashify</h2>
    <div style="background:var(--surf);border:1px solid var(--b2);border-radius:10px;overflow:hidden;margin-bottom:2rem;">
      <table style="width:100%;border-collapse:collapse;">
        <thead><tr style="background:var(--surf2);">
          <th style="padding:.85rem 1.25rem;text-align:left;font-size:.68rem;letter-spacing:2px;text-transform:uppercase;color:var(--muted);">Model</th>
          <th style="padding:.85rem 1.25rem;text-align:right;font-size:.68rem;letter-spacing:2px;text-transform:uppercase;color:var(--g);">EWasteKochi</th>
          <th style="padding:.85rem 1.25rem;text-align:right;font-size:.68rem;letter-spacing:2px;text-transform:uppercase;color:var(--muted);">Cashify</th>
          <th style="padding:.85rem 1.25rem;text-align:right;font-size:.68rem;letter-spacing:2px;text-transform:uppercase;color:var(--amber);">You Gain</th>
        </tr></thead>
        <tbody>
          {''.join([f'<tr style="border-bottom:1px solid var(--b);"><td style="padding:.85rem 1.25rem;color:var(--white);font-weight:500;">{m}</td><td style="padding:.85rem 1.25rem;text-align:right;color:var(--g);font-weight:700;">{ew}</td><td style="padding:.85rem 1.25rem;text-align:right;color:var(--muted);">{cs}</td><td style="padding:.85rem 1.25rem;text-align:right;color:var(--amber);font-family:monospace;font-size:.85rem;">{gain}</td></tr>' for m,ew,cs,gain in [
            ("MacBook Pro M3 Pro 14\"","₹62–65,000","~₹52,000","+₹13,000"),
            ("MacBook Air M2","₹42–46,000","~₹36,000","+₹10,000"),
            ("MacBook Pro M1 14\"","₹48–52,000","~₹40,000","+₹12,000"),
            ("ThinkPad X1 Carbon Gen 9+","₹30–35,000","~₹24,000","+₹11,000"),
            ("Dell Latitude 7430/7440","₹28–32,000","~₹22,000","+₹10,000"),
            ("HP EliteBook 840/850 G8+","₹22–26,000","~₹17,000","+₹9,000"),
          ]])}
        </tbody>
      </table>
    </div>
    {cta_box("Get Your Laptop's Price Now", "Confirmed within 2 hours. We honour our quote. No inspection surprises.")}
  </div>
</section>""",
  },

  # ── 4. MOBILE RECYCLING ──────────────────────────────────
  {
    "key": "mobile",
    "slug": "pillars/mobile-recycling-kochi.html",
    "title": "Sell Old Phone Kochi | iPhone up to ₹75,000 | Instant Payment | No OLX Risk",
    "meta": "Sell your old phone in Kochi instantly. iPhone 15 Pro Max up to ₹75,000. Samsung Galaxy S24 Ultra up to ₹55,000. Instant UPI payment. Certificate of Data Destruction. No OLX risk.",
    "canonical": f"{SITE_URL}/pillars/mobile-recycling-kochi.html",
    "hero": """<section class="hero">
  <div class="wrap">
    <div style="display:flex;gap:.4rem;flex-wrap:wrap;margin-bottom:1.5rem;">
      <span class="pill pill-a">💰 iPhone up to ₹75,000</span>
      <span class="pill pill-g">⚡ Instant Payment</span>
      <span class="pill pill-r">🚫 No OLX Risk</span>
    </div>
    <div class="tag">Phone Buyback · Kochi</div>
    <h1>Sell Your Old Phone<br>in Kochi.<br><em>₹75,000.</em><br>2 Minutes. Done.</h1>
    <p class="lead">No OLX. No fake buyers. No data exposure. We pay top market rate with same-day UPI transfer and include a Certificate of Data Destruction confirming your personal data is permanently wiped.</p>
    <div style="display:flex;gap:1rem;flex-wrap:wrap;margin-bottom:2rem;">
      <a href="/book-free-pickup-kochi.html" class="btn">📱 Get Instant Price →</a>
      <a href="https://wa.me/91XXXXXXXXXX?text=Hi%2C+I+want+to+sell+my+phone+in+Kochi.+Model%3A+" class="btn-wa" target="_blank" rel="noopener">💬 WhatsApp for Price</a>
    </div>
    <div class="trust-bar">
      <span class="trust-item">⚡ Takes less than 2 minutes to schedule</span>
      <span class="trust-item">💰 Better than OLX, Cashify, local shops</span>
      <span class="trust-item">🔒 Your data permanently destroyed</span>
      <span class="trust-item">⭐ 4.9★ · 243 Google Reviews</span>
    </div>
  </div>
</section>""",
    "body": f"""<section class="section section-alt">
  <div class="wrap">
    <div class="tag">Current Phone Prices · {YEAR}</div>
    <h2>What Your Phone Is Worth</h2>
    <div class="grid-2" style="margin-bottom:2rem;">
      <div class="card">
        <h3 style="margin-bottom:1rem;">🍎 iPhone Buyback Prices</h3>
        <ul style="list-style:none;display:flex;flex-direction:column;gap:.55rem;">
          {''.join([f'<li style="display:flex;justify-content:space-between;padding:.55rem 0;border-bottom:1px solid var(--b);font-size:.9rem;"><span style="color:var(--text);">{m}</span><span style="color:var(--g);font-weight:700;">{p}</span></li>' for m,p in [
            ("iPhone 15 Pro Max","up to ₹75,000"),
            ("iPhone 15 Pro","up to ₹65,000"),
            ("iPhone 14 Pro Max","up to ₹56,000"),
            ("iPhone 14 Pro","up to ₹48,000"),
            ("iPhone 13 Pro","up to ₹40,000"),
            ("iPhone 13","up to ₹32,000"),
          ]])}
        </ul>
      </div>
      <div class="card">
        <h3 style="margin-bottom:1rem;">📱 Samsung & Others</h3>
        <ul style="list-style:none;display:flex;flex-direction:column;gap:.55rem;">
          {''.join([f'<li style="display:flex;justify-content:space-between;padding:.55rem 0;border-bottom:1px solid var(--b);font-size:.9rem;"><span style="color:var(--text);">{m}</span><span style="color:var(--g);font-weight:700;">{p}</span></li>' for m,p in [
            ("Samsung Galaxy S24 Ultra","up to ₹55,000"),
            ("Samsung Galaxy S23 Ultra","up to ₹46,000"),
            ("OnePlus 12","up to ₹32,000"),
            ("Google Pixel 8 Pro","up to ₹36,000"),
            ("Damaged / Non-working","price on inspection"),
            ("Any other brand","WhatsApp us"),
          ]])}
        </ul>
      </div>
    </div>
    {cta_box("Get Your Phone's Price Now", "Instant quote · Same-day payment · Data destruction certificate.")}
  </div>
</section>""",
  },

  # ── 5. CORPORATE ITAD ────────────────────────────────────
  {
    "key": "corporate",
    "slug": "pillars/corporate-itad-kochi.html",
    "title": "Corporate ITAD Kochi | NIST 800-88 + DPDP Act 2023 | Infopark Trusted",
    "meta": "Corporate ITAD in Kochi for IT companies, banks, and enterprises. NIST 800-88 certified. DPDP Act 2023 compliant. Certificate of Destruction per device. Free pickup 50+ units. Annual contracts. Infopark trusted.",
    "canonical": f"{SITE_URL}/pillars/corporate-itad-kochi.html",
    "hero": """<section class="hero">
  <div class="wrap">
    <div style="display:flex;gap:.4rem;flex-wrap:wrap;margin-bottom:1.5rem;">
      <span class="pill pill-g">✓ NIST 800-88 Certified</span>
      <span class="pill pill-g">✓ DPDP Act 2023 Compliant</span>
      <span class="pill pill-a">🏢 Infopark Trusted</span>
    </div>
    <div class="tag">Corporate ITAD · Kochi</div>
    <h1>Certified ITAD for<br><em>Kochi Businesses</em> —<br>Compliance-First,<br>Value-Maximised</h1>
    <p class="lead">End-to-end IT asset disposition for Infopark, Smart City, and Ernakulam corporates. NIST 800-88 data destruction, Certificate of Destruction per device, DPDP Act 2023 audit-ready documentation. Asset recovery offsets disposal costs.</p>
    <div style="display:flex;gap:1rem;flex-wrap:wrap;margin-bottom:2rem;">
      <a href="/book-free-pickup-kochi.html" class="btn">🏢 Get Corporate Quote →</a>
      <a href="https://wa.me/91XXXXXXXXXX?text=Hi%2C+I+need+a+corporate+ITAD+quote+for+our+company+in+Kochi.+Volume%3A+" class="btn-wa" target="_blank" rel="noopener">💬 WhatsApp Our Team</a>
    </div>
    <div class="trust-bar">
      <span class="trust-item">🏢 Trusted by Infopark IT companies</span>
      <span class="trust-item">⚖️ DPDP Act 2023 audit-ready docs</span>
      <span class="trust-item">💰 Asset recovery: typical 100-unit batch = ₹8–15L</span>
      <span class="trust-item">📋 Annual ITAD contracts available</span>
    </div>
  </div>
</section>""",
    "body": f"""<section class="section section-alt">
  <div class="wrap">
    <div class="grid-2">
      <div class="card">
        <h3 style="margin-bottom:1rem;">What's Included — Every Job</h3>
        <ul class="check-list">
          <li>NIST 800-88 Purge — cryptographically verified overwriting</li>
          <li>Certificate of Destruction per device with serial number</li>
          <li>Chain-of-custody manifest from pickup through destruction</li>
          <li>DPDP Act 2023 audit-ready PDF documentation package</li>
          <li>Asset recovery payout for devices with residual value</li>
          <li>KSPCB authorization reference for your compliance records</li>
          <li>Consolidated invoice for single-PO accounting</li>
        </ul>
      </div>
      <div class="card">
        <h3 style="margin-bottom:1rem;">The Financial Case</h3>
        <p style="font-size:.9rem;color:var(--text);line-height:1.75;margin-bottom:1rem;">A batch of 100 three-year-old business laptops typically yields <strong style="color:var(--g);">₹8–15 lakh</strong> in asset recovery — converting a disposal cost centre into a budget recovery line item.</p>
        <p style="font-size:.9rem;color:var(--text);line-height:1.75;margin-bottom:1rem;">The Certificate of Destruction required for DPDP compliance, which we include as standard, would cost <strong style="color:var(--white);">₹50,000–₹1.5 lakh</strong> from a standalone compliance consultancy.</p>
        <p style="font-size:.9rem;color:var(--g);font-weight:600;">Net result: you get paid, and you get compliant.</p>
      </div>
    </div>
    <div class="alert" style="margin-top:2rem;">⚠️ <strong>DPDP Act 2023 Enforcement:</strong> The Data Protection Board of India is actively conducting audits. Without a Certificate of Destruction, your organisation has no documented due diligence if a data breach surfaces from a disposed device. Penalties reach <strong>₹250 Crore</strong>.</div>
    {cta_box("Book Your ITAD Consultation", "Free assessment · No commitment · DPDP Act compliance from day one.")}
  </div>
</section>""",
  },

  # ── 6. FREE PICKUP ───────────────────────────────────────
  {
    "key": "pickup",
    "slug": "pillars/free-pickup-kochi.html",
    "title": "Free E-Waste Pickup Kochi | Same-Day Slots | 50+ Units Free | Book Now",
    "meta": "Free e-waste pickup in Kochi. Same-day or next-day for 50+ units across Ernakulam. WhatsApp to book in 30 seconds. Walk-in Thrippunithura Mon–Sat 8AM–8PM. KSPCB Authorized.",
    "canonical": f"{SITE_URL}/pillars/free-pickup-kochi.html",
    "hero": """<section class="hero">
  <div class="wrap">
    <div style="display:flex;gap:.4rem;flex-wrap:wrap;margin-bottom:1.5rem;">
      <span class="pill pill-g">🚛 FREE for 50+ Units</span>
      <span class="pill pill-a">⚡ Same-Day Available</span>
      <span class="pill pill-g">✓ No Hidden Charges</span>
    </div>
    <div class="tag">Free Pickup · All Ernakulam</div>
    <h1>Free E-Waste Pickup<br>in <em>Kochi</em> —<br>100% Free.<br>Zero Catch.</h1>
    <p class="lead">Free same-day or next-day pickup anywhere in Ernakulam district for 50+ units. WhatsApp by 12PM on weekdays for same-day service. Walk-in at Thrippunithura always free.</p>
    <div style="display:flex;gap:1rem;flex-wrap:wrap;margin-bottom:2rem;">
      <a href="/book-free-pickup-kochi.html" class="btn">🚛 Book Now — 30 Seconds →</a>
      <a href="https://wa.me/91XXXXXXXXXX?text=Hi%2C+I+want+to+book+a+free+e-waste+pickup+in+Kochi.+My+location+is%3A+" class="btn-wa" target="_blank" rel="noopener">💬 WhatsApp to Book</a>
    </div>
    <div class="trust-bar">
      <span class="trust-item"><span class="live-dot"></span>Last pickup: 35 min ago · Kakkanad</span>
      <span class="trust-item">🚛 FREE for 50+ units — no catch</span>
      <span class="trust-item">⚡ Same-day if WhatsApp by 12PM</span>
      <span class="trust-item">📍 All 50+ Ernakulam pincodes</span>
    </div>
  </div>
</section>""",
    "body": f"""<section class="section section-alt">
  <div class="wrap">
    <div class="grid-2">
      <div class="card">
        <h3 style="margin-bottom:1rem;">Pickup Pricing — Transparent</h3>
        <ul style="list-style:none;display:flex;flex-direction:column;gap:.7rem;font-size:.9rem;">
          {''.join([f'<li style="display:flex;justify-content:space-between;align-items:center;padding:.65rem 0;border-bottom:1px solid var(--b);"><span style="color:var(--text);">{item}</span><span style="color:var(--g);font-weight:700;font-size:.88rem;">{price}</span></li>' for item, price in [
            ("50+ units · Ernakulam district","FREE · Same-day"),
            ("10–49 units · Ernakulam","Nominal fee confirmed on booking"),
            ("1–9 units · Individual pickup","Fixed fee per location"),
            ("Walk-in · Thrippunithura facility","Always FREE"),
            ("On-site data destruction","Quote on request"),
          ]])}
        </ul>
        <p style="font-size:.76rem;color:var(--muted);margin-top:.75rem;">Individual pickup fee is almost always offset by our higher prices vs. any competitor.</p>
      </div>
      <div class="card">
        <h3 style="margin-bottom:1rem;">Coverage Areas</h3>
        <div style="display:flex;flex-wrap:wrap;gap:.4rem;">
          {''.join([f'<span style="font-size:.8rem;padding:.3rem .75rem;background:var(--bg2);border:1px solid {"var(--b2)" if hot else "var(--b)"};border-radius:4px;color:{"var(--g)" if hot else "var(--text)"};">{area}</span>' for area, hot in [
            ("Kakkanad ⭐", True),("Infopark ⭐", True),("Edappally ⭐", True),("Vyttila", False),
            ("Thrippunithura ⭐", True),("Palarivattom", False),("Kaloor", False),("MG Road", False),
            ("Aluva", False),("Perumbavoor", False),("Angamaly", False),("Fort Kochi", False),
            ("Kalamassery", False),("Maradu", False),("+ 38 more", False),
          ]])}
        </div>
      </div>
    </div>
    {cta_box("Book Your Free Pickup", "Same-day slots fill fast. WhatsApp by 12PM to guarantee today's slot.")}
  </div>
</section>""",
  },

  # ── 7. ITAD ──────────────────────────────────────────────
  {
    "key": "itad",
    "slug": "pillars/it-asset-disposal-kochi.html",
    "title": "IT Asset Disposal Kochi | NIST 800-88 | DPDP Act 2023 | Certificate of Destruction",
    "meta": "Certified IT asset disposal in Kochi. NIST 800-88 data destruction. Certificate of Destruction per device. DPDP Act 2023 compliant. KSPCB Authorized. On-site shredding available. Free audit-ready documentation.",
    "canonical": f"{SITE_URL}/pillars/it-asset-disposal-kochi.html",
    "hero": """<section class="hero">
  <div class="wrap">
    <div style="display:flex;gap:.4rem;flex-wrap:wrap;margin-bottom:1.5rem;">
      <span class="pill pill-g">✓ NIST 800-88 Certified</span>
      <span class="pill pill-g">✓ DPDP Act 2023</span>
      <span class="pill pill-a">📋 Certificate Every Device</span>
    </div>
    <div class="tag">IT Asset Disposal · Kerala</div>
    <h1>Certified IT Asset<br><em>Disposal</em> in Kochi —<br>NIST 800-88.<br>Audit-Ready.</h1>
    <p class="lead">The only KSPCB-authorized ITAD provider in Kochi offering NIST 800-88 Purge and Destroy level data destruction with a Certificate of Destruction per device and full DPDP Act 2023 audit documentation.</p>
    <div style="display:flex;gap:1rem;flex-wrap:wrap;margin-bottom:2rem;">
      <a href="/book-free-pickup-kochi.html" class="btn">🔐 Get ITAD Quote →</a>
      <a href="https://wa.me/91XXXXXXXXXX?text=Hi%2C+I+need+NIST+800-88+IT+asset+disposal+in+Kochi.+Scope%3A+" class="btn-wa" target="_blank" rel="noopener">💬 Discuss Your Requirement</a>
    </div>
    <div class="trust-bar">
      <span class="trust-item">🔒 NIST 800-88 Purge + Destroy available</span>
      <span class="trust-item">📋 Certificate of Destruction every device</span>
      <span class="trust-item">⚖️ DPDP Act 2023 audit-ready package</span>
      <span class="trust-item">🏛️ DoD 5220.22-M for government clients</span>
    </div>
  </div>
</section>""",
    "body": f"""<section class="section section-alt">
  <div class="wrap">
    <div class="grid-2">
      <div class="card">
        <h3 style="margin-bottom:1rem;">NIST 800-88 Levels We Offer</h3>
        <ul style="list-style:none;display:flex;flex-direction:column;gap:.85rem;">
          {''.join([f'<li style="padding:.85rem;background:var(--bg2);border:1px solid var(--b);border-radius:8px;"><div style="font-family:monospace;font-size:.78rem;color:var(--amber);margin-bottom:.3rem;letter-spacing:1px;">{level}</div><div style="font-size:.9rem;color:var(--white);font-weight:600;margin-bottom:.3rem;">{name}</div><div style="font-size:.84rem;color:var(--muted);">{desc}</div></li>' for level, name, desc in [
            ("NIST 800-88 — CLEAR","Software Overwrite","Standard OS commands. For devices reused internally."),
            ("NIST 800-88 — PURGE","Firmware-level Sanitisation","Cryptographic Erase or ATA Secure Erase. Irrecoverable by all known lab methods. Our standard."),
            ("NIST 800-88 — DESTROY","Physical Destruction","Industrial shredding to 2mm. Absolute certainty. On-site available."),
            ("DoD 5220.22-M","7-Pass Overwrite","For government and classified environments on request."),
          ]])}
        </ul>
      </div>
      <div class="card">
        <h3 style="margin-bottom:1rem;">Why Certification Matters</h3>
        <div class="alert" style="margin-bottom:1rem;"><strong>A factory reset is not enough.</strong> Free tools recover files from reset devices in under 10 minutes. 78% of secondhand devices in a 2024 study contained recoverable personal data.</div>
        <ul class="check-list">
          <li>NIST 800-88 Purge renders data irrecoverable by any known forensic method</li>
          <li>Certificate of Destruction = your legal evidence of due diligence under DPDP Act</li>
          <li>Serial-number tracking means every device is individually accounted for</li>
          <li>Chain-of-custody proves your data was never exposed between pickup and destruction</li>
        </ul>
      </div>
    </div>
    {cta_box("Book Your ITAD Assessment", "Free · No commitment · DPDP Act compliant from day one.")}
  </div>
</section>""",
  },

  # ── 8. BATTERY RECYCLING ─────────────────────────────────
  {
    "key": "battery",
    "slug": "pillars/battery-recycling-kochi.html",
    "title": "Battery Recycling Kochi | Safe Lithium & UPS Disposal | KSPCB Authorized",
    "meta": "Safe battery recycling in Kochi. Lithium-ion, lead-acid, UPS, laptop, phone batteries. KSPCB authorized hazardous waste processing. Certified safe disposal. Free pickup for bulk volumes.",
    "canonical": f"{SITE_URL}/pillars/battery-recycling-kochi.html",
    "hero": """<section class="hero">
  <div class="wrap">
    <div style="display:flex;gap:.4rem;flex-wrap:wrap;margin-bottom:1.5rem;">
      <span class="pill pill-r">⚠️ Classified Hazardous Waste</span>
      <span class="pill pill-g">✓ KSPCB Authorized</span>
      <span class="pill pill-g">🔋 All Battery Types</span>
    </div>
    <div class="tag">Battery Recycling · Kerala</div>
    <h1>Safe Battery<br><em>Recycling</em> in Kochi —<br>Certified. Legal.<br>Hazard-Free.</h1>
    <p class="lead">Lithium batteries are classified hazardous waste under E-Waste Management Rules 2022. Improper disposal risks fire, toxic contamination, and legal liability. EWasteKochi handles all battery types through certified KSPCB-compliant channels.</p>
    <div style="display:flex;gap:1rem;flex-wrap:wrap;margin-bottom:2rem;">
      <a href="/book-free-pickup-kochi.html" class="btn">🔋 Schedule Battery Collection →</a>
      <a href="https://wa.me/91XXXXXXXXXX?text=Hi%2C+I+need+to+recycle+batteries+safely+in+Kochi.+Type%3A+" class="btn-wa" target="_blank" rel="noopener">💬 WhatsApp for Details</a>
    </div>
    <div class="trust-bar">
      <span class="trust-item">⚠️ Lithium = hazardous waste — certified disposal required</span>
      <span class="trust-item">✓ KSPCB compliant battery processing chain</span>
      <span class="trust-item">🔋 All types: Li-ion, lead-acid, NiMH, NiCd</span>
      <span class="trust-item">🏭 Industrial and EV batteries by arrangement</span>
    </div>
  </div>
</section>""",
    "body": f"""<section class="section section-alt">
  <div class="wrap">
    <div class="alert">⚠️ <strong>Legal Warning:</strong> Under E-Waste Management Rules 2022, batteries are classified as hazardous waste. Disposal through unauthorized channels — including informal scrap dealers — is a regulatory violation that exposes both the recycler AND the originating business to legal liability.</div>
    <div class="grid-2" style="margin-top:2rem;">
      <div class="card">
        <h3 style="margin-bottom:1rem;">Battery Types We Accept</h3>
        <ul class="check-list">
          <li>Smartphone lithium-ion batteries (loose or in device)</li>
          <li>Laptop battery packs (all brands)</li>
          <li>UPS and inverter batteries (lead-acid)</li>
          <li>Server rack UPS batteries</li>
          <li>Tablet and wearable batteries</li>
          <li>Industrial NiCd / NiMH battery packs</li>
          <li>EV battery modules (by prior arrangement)</li>
          <li>Drone and RC lithium polymer batteries</li>
        </ul>
      </div>
      <div class="card">
        <h3 style="margin-bottom:1rem;">Why Certified Processing Matters</h3>
        <ul class="check-list">
          <li>Lithium battery puncture causes thermal runaway — fire and toxic fume risk</li>
          <li>Lead-acid batteries contain sulfuric acid and lead — soil and water contamination</li>
          <li>Informal scrap dealers crack batteries open — health hazard for workers</li>
          <li>KSPCB-certified processing uses sealed, temperature-monitored handling</li>
          <li>Battery materials (cobalt, lithium, lead) are recovered and re-entered into supply chain</li>
        </ul>
      </div>
    </div>
    {cta_box("Schedule Safe Battery Collection", "All types accepted · KSPCB compliant · Safe for your team and environment.")}
  </div>
</section>""",
  },

  # ── 9. SCRAP ELECTRONICS ─────────────────────────────────
  {
    "key": "scrap",
    "slug": "pillars/scrap-electronics-kochi.html",
    "title": "Sell Scrap Electronics Kochi | Best Price | Servers, Laptops, Bulk Buy",
    "meta": "Best prices for scrap electronics in Kochi. Servers, laptops, desktops, phones, bulk e-waste. 30–60% above local scrap dealers. Free pickup for large volumes. Same-day UPI payment.",
    "canonical": f"{SITE_URL}/pillars/scrap-electronics-kochi.html",
    "hero": """<section class="hero">
  <div class="wrap">
    <div style="display:flex;gap:.4rem;flex-wrap:wrap;margin-bottom:1.5rem;">
      <span class="pill pill-a">💰 30–60% Above Scrap Dealers</span>
      <span class="pill pill-g">📦 All Bulk Volumes</span>
      <span class="pill pill-g">⚡ Same-Day Payment</span>
    </div>
    <div class="tag">Scrap Electronics · Kochi</div>
    <h1>Get <em>Paid</em> for<br>Scrap Electronics<br>in Kochi —<br>More Than Anyone.</h1>
    <p class="lead">We access enterprise refurbishment and export markets — unlocking 30–60% more value than local scrap dealers for the same hardware. Same-day UPI payment. Free pickup for large volumes. DPDP-compliant disposal.</p>
    <div style="display:flex;gap:1rem;flex-wrap:wrap;margin-bottom:2rem;">
      <a href="/book-free-pickup-kochi.html" class="btn">💰 Get Bulk Quote →</a>
      <a href="https://wa.me/91XXXXXXXXXX?text=Hi%2C+I+have+scrap+electronics+to+sell+in+Kochi.+I+have%3A+" class="btn-wa" target="_blank" rel="noopener">💬 WhatsApp Inventory</a>
    </div>
    <div class="trust-bar">
      <span class="trust-item">💰 30–60% above local scrap rate</span>
      <span class="trust-item">📦 Any volume — no minimum</span>
      <span class="trust-item">⚡ Same-day UPI or cash payment</span>
      <span class="trust-item">🔒 DPDP-compliant data destruction</span>
    </div>
  </div>
</section>""",
    "body": f"""<section class="section section-alt">
  <div class="wrap">
    <div class="tag">Bulk Pricing Guide</div>
    <h2>What We Pay for Scrap Electronics</h2>
    <div class="grid-3" style="margin-bottom:2rem;">
      {''.join([f'<div class="card" style="text-align:center;"><div style="font-size:1.8rem;margin-bottom:.75rem;">{icon}</div><h3 style="font-size:1rem;margin-bottom:.4rem;">{cat}</h3><div style="font-family:monospace;font-size:1.1rem;color:var(--g);font-weight:700;">{price}</div><p style="font-size:.78rem;color:var(--muted);margin-top:.3rem;">{note}</p></div>' for icon, cat, price, note in [
        ("💻","Business Laptops (2019+)","₹8K–₹35K/unit","Model-dependent"),
        ("🖥️","Servers (rack, recent)","₹15K–₹50K/unit","Config-dependent"),
        ("📱","Smartphones (working)","₹3K–₹75K/unit","Model-dependent"),
        ("🖥️","Desktops & Towers","₹2K–₹8K/unit","Spec-dependent"),
        ("🌐","Managed Switches","₹2K–₹15K/unit","Brand-dependent"),
        ("📦","Mixed E-Waste Bulk","Aggregate quote","Send inventory"),
      ]])}
    </div>
    <div class="card" style="margin-bottom:2rem;">
      <h3 style="margin-bottom:.75rem;">Why We Pay More Than Local Scrap Dealers</h3>
      <p style="font-size:.93rem;color:var(--text);line-height:1.75;max-width:700px;">Local scrap dealers price for their local consumer resale market — which undervalues enterprise hardware significantly. A ThinkPad X1 Carbon a scrap dealer pays ₹8,000 for, we pay ₹28,000–₹32,000 for — because we sell it into the enterprise refurbishment market, not to a local buyer. That difference is what we pass on to you.</p>
    </div>
    {cta_box("Get Your Bulk Scrap Quote", "Send your inventory via WhatsApp — we reply with full valuation within 2 hours.")}
  </div>
</section>""",
  },

  # ── 10. COMPLIANCE ───────────────────────────────────────
  {
    "key": "compliance",
    "slug": "pillars/compliance-kochi.html",
    "title": "E-Waste Compliance Kochi | Kerala PCB Approved | DPDP Act 2023 | ITAD Audit",
    "meta": "Government-approved e-waste compliance in Kochi. KSPCB Authorization. DPDP Act 2023 penalty protection. Certificate of Destruction. Audit-ready chain of custody. EPR and E-Waste Rules 2022.",
    "canonical": f"{SITE_URL}/pillars/compliance-kochi.html",
    "hero": """<section class="hero">
  <div class="wrap">
    <div style="display:flex;gap:.4rem;flex-wrap:wrap;margin-bottom:1.5rem;">
      <span class="pill pill-g">♻️ Kerala PCB Approved</span>
      <span class="pill pill-g">⚖️ DPDP Act 2023</span>
      <span class="pill pill-a">📋 Audit-Ready Docs</span>
    </div>
    <div class="tag">Regulatory Compliance · Kerala</div>
    <h1>Government-Approved<br><em>E-Waste Compliance</em><br>in Kochi —<br>Every Standard Met.</h1>
    <p class="lead">EWasteKochi holds KSPCB authorization under E-Waste Management Rules 2022 and provides full DPDP Act 2023 compliance documentation. Every disposal is legally protected, audit-ready, and documented to withstand scrutiny from the Data Protection Board of India.</p>
    <div style="display:flex;gap:1rem;flex-wrap:wrap;margin-bottom:2rem;">
      <a href="/book-free-pickup-kochi.html" class="btn">⚖️ Get Compliant Today →</a>
      <a href="https://wa.me/91XXXXXXXXXX?text=Hi%2C+I+need+DPDP+Act+2023+compliant+IT+disposal+documentation+for+our+organisation.+" class="btn-wa" target="_blank" rel="noopener">💬 Discuss Compliance Needs</a>
    </div>
    <div class="trust-bar">
      <span class="trust-item">♻️ KSPCB Authorization — legally required</span>
      <span class="trust-item">⚖️ DPDP Act 2023 — ₹250Cr penalty protection</span>
      <span class="trust-item">📋 Certificate of Destruction — audit evidence</span>
      <span class="trust-item">📊 EPR + GFR documentation available</span>
    </div>
  </div>
</section>""",
    "body": f"""<section class="section section-alt">
  <div class="wrap">
    <div class="tag">Compliance Framework</div>
    <h2>Every Regulation — Covered</h2>
    <div class="grid-2">
      {''.join([f'<div class="card"><div class="tag" style="margin-bottom:.5rem;">{tag}</div><h3 style="margin-bottom:.5rem;">{title}</h3><p style="font-size:.88rem;color:var(--text);line-height:1.7;">{body}</p></div>' for tag, title, body in [
        ("amber · DPDP Act 2023","₹250 Crore Penalty Protection","The Digital Personal Data Protection Act 2023 requires data fiduciaries to permanently destroy personal data on decommissioned devices. Our Certificate of Destruction is your documented evidence of compliance."),
        ("","KSPCB Authorization","E-Waste Management Rules 2022 mandate that bulk consumers use only KSPCB-authorized recyclers. Using us automatically satisfies this requirement — using anyone else is a regulatory violation."),
        ("","E-Waste Management Rules 2022","Bulk consumers must register, maintain disposal records, and submit annual returns. Our documentation package provides everything needed for your annual EPR compliance submission."),
        ("","GFR Capital Asset Disposal","Government departments disposing of IT assets require formal valuation certificates and destruction documentation under General Financial Rules. We provide GFR-formatted certificates on request."),
        ("","RBI IT Governance (Banks)","Financial institutions require comprehensive storage media destruction documentation per RBI IT governance guidelines. Our process is specifically documented to satisfy RBI audit requirements."),
        ("","NABH Accreditation (Hospitals)","Hospital accreditation increasingly includes IT governance review. Our Certificate of Destruction package has passed NABH audits at multiple Kochi hospitals without follow-up questions."),
      ]])}
    </div>
    {cta_box("Get Full Compliance Coverage", "Free compliance assessment · Certificate of Destruction · Audit-ready documentation.")}
  </div>
</section>""",
  },
]

# ════════════════════════════════════════════════════════════
# MAIN EXECUTION
# ════════════════════════════════════════════════════════════
def generate_all():
    print(f"\n{'═'*65}")
    print(f"  EWasteKochi.in — 10 Pillar Pages + AI Chatbot Generator")
    print(f"  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'═'*65}\n")

    os.makedirs("pillars", exist_ok=True)

    for i, page in enumerate(PILLAR_PAGES, 1):
        html = page_wrap(
            pillar_key = page["key"],
            title      = page["title"],
            meta       = page["meta"],
            canonical  = page["canonical"],
            hero_section = page["hero"],
            main_content = page["body"],
        )
        with open(page["slug"], "w", encoding="utf-8") as f:
            f.write(html)

        char_kb = len(html) // 1024
        print(f"  ✅ [{i:02d}] /{page['slug']} ({char_kb}KB) — chatbot: data-page=\"{page['key']}\"")

    print(f"\n{'═'*65}")
    print(f"✅ DONE — {len(PILLAR_PAGES)} pillar pages generated in /pillars/")
    print(f"\n📋 Each page has:")
    print(f"   • data-page attribute matching Claude AI pillar personality")
    print(f"   • 3-second auto-popup + scroll depth trigger")
    print(f"   • Page-specific greeting + quick replies")
    print(f"   • Smart WhatsApp CTA with context pre-fill")
    print(f"   • Lead capture form after 3 exchanges")
    print(f"\n⚠️  Pre-deploy:")
    print(f"   1. Replace XXXXXXXXXX with real phone in chatbot-embed.html")
    print(f"   2. Replace YOUR_FORM_ID in ewSubmitLead()")
    print(f"   3. Replace GTM-XXXXXXX with your container ID")
    print(f"{'═'*65}\n")

if __name__ == "__main__":
    generate_all()
