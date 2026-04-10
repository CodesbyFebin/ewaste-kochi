"""
EWaste Kochi — 10-Pillar SEO Powerhouse Generator
Generates 10 ultra-long pillar pages, 200 FAQs each, full schema, internal linking silo.
"""
import os, json, re

OUT = "/media/hp-ml10/Projects/ewastekochi-production/ewastekochi/"

# ── PILLAR MAP ─────────────────────────────────────────────────────────────────
PILLARS = [
    {"slug":"computer-scrap-kochi",         "kw":"Computer Scrap Dealer Kochi",        "emoji":"🖥️",  "icon":"🖥️"},
    {"slug":"battery-recycling-kochi",       "kw":"Battery Recycling Kochi",            "emoji":"🔋",  "icon":"🔋"},
    {"slug":"itad-kochi",                    "kw":"IT Asset Disposal Kochi (ITAD)",     "emoji":"🏢",  "icon":"🏢"},
    {"slug":"data-destruction-kochi",        "kw":"Data Destruction & Shredding Kochi", "emoji":"💾",  "icon":"💾"},
    {"slug":"laptop-buyback-kochi",          "kw":"Laptop Buyback Kochi",               "emoji":"💻",  "icon":"💻"},
    {"slug":"mobile-recycling-kochi",        "kw":"Mobile Phone Recycling Kochi",       "emoji":"📱",  "icon":"📱"},
    {"slug":"corporate-ewaste-kochi",        "kw":"Corporate E-Waste Management Kochi", "emoji":"🏗️",  "icon":"🏗️"},
    {"slug":"industrial-ewaste-kochi",       "kw":"Industrial E-Waste Disposal Kochi",  "emoji":"🏭",  "icon":"🏭"},
    {"slug":"ewaste-compliance-kerala",      "kw":"E-Waste Compliance Kerala DPDP Act", "emoji":"⚖️",  "icon":"⚖️"},
    {"slug":"free-ewaste-pickup-kochi",      "kw":"Free E-Waste Pickup Kochi",          "emoji":"🚚",  "icon":"🚚"},
]

# ── KOCHI LOCAL AREAS ──────────────────────────────────────────────────────────
AREAS = [
    "Kakkanad","Edapally","Aluva","Vyttila","Palarivattom","Kaloor",
    "Fort Kochi","Angamaly","Perumbavoor","Kalamassery","Maradu",
    "Kadavanthra","Thrippunithura","Eloor","Cheranallur","Nedumbassery",
    "Infopark","SmartCity","MG Road","Panampilly Nagar","Thevara",
    "Kundannoor","Nettoor","Eroor","Kochi Port","CUSAT","Tripunithura",
    "Mattancherry","Ernakulam Town","North Paravur"
]

# ── BLOG CATEGORIES ───────────────────────────────────────────────────────────
BLOG_CATS = ["ITAD Guides","Compliance & Legal","Buyback Price Guides",
             "Local Kochi Hubs","Environmental Impact","Data Security"]

# ── INTERNAL LINK SILO ────────────────────────────────────────────────────────
def get_cross_links(idx):
    """Each pillar links to 3 others (neighbours + wrap)."""
    n = len(PILLARS)
    return [PILLARS[(idx+1)%n], PILLARS[(idx+2)%n], PILLARS[(idx-1)%n]]

def get_blog_links(idx):
    return [BLOG_CATS[idx % len(BLOG_CATS)], BLOG_CATS[(idx+3) % len(BLOG_CATS)]]

# ── FAQ ENGINE ────────────────────────────────────────────────────────────────
Q_STEMS = [
    "How to dispose of {item} safely in {area}?",
    "Best {item} recycling centre near {area} Kochi?",
    "Is {item} disposal free in {area}?",
    "DPDP Act rules for {item} disposal in Kochi {area}?",
    "Where to sell old {item} for cash in {area}?",
    "Certificate of Destruction for {item} in {area}?",
    "NIST 800-88 {item} wipe service in {area}?",
    "Same-day {item} pickup available in {area}?",
    "Bulk {item} disposal rates for companies in {area}?",
    "KSPCB authorised {item} recycler near {area}?",
]
ITEMS = ["laptop","hard drive","server","mobile","battery","desktop",
         "SSD","printer","UPS","networking equipment"]

def gen_faqs(kw, n=200):
    faqs, i = [], 0
    while len(faqs) < n:
        area  = AREAS[i % len(AREAS)]
        item  = ITEMS[i % len(ITEMS)]
        stem  = Q_STEMS[i % len(Q_STEMS)]
        q = stem.format(item=item, area=area)
        a = (f"EWaste Kochi provides certified {item} {kw.lower()} services across {area}. "
             f"We follow NIST 800-88, KSPCB authorisation, and DPDP Act 2023 guidelines. "
             f"Free corporate pickup for 50+ units. Certificate of Destruction issued every job. "
             f"Call +91-7500555454 or WhatsApp for same-day scheduling.")
        faqs.append({"q": q, "a": a})
        i += 1
    return faqs

# ── SCHEMA ────────────────────────────────────────────────────────────────────
def build_schema(p, faqs):
    faq_entities = [{"@type":"Question","name":f["q"],
                     "acceptedAnswer":{"@type":"Answer","text":f["a"]}} for f in faqs[:30]]
    return json.dumps({
        "@context":"https://schema.org",
        "@graph":[
            {"@type":"Service","name":p["kw"],
             "provider":{"@type":"LocalBusiness","name":"EWaste Kochi",
                         "telephone":"+91-7500555454","address":{
                             "@type":"PostalAddress","addressLocality":"Thrippunithura",
                             "addressRegion":"Kerala","postalCode":"682301","addressCountry":"IN"}},
             "areaServed":["Kochi","Ernakulam"]+AREAS[:8]},
            {"@type":"FAQPage","mainEntity":faq_entities},
            {"@type":"BreadcrumbList","itemListElement":[
                {"@type":"ListItem","position":1,"name":"Home","item":"https://ewastekochi.com/"},
                {"@type":"ListItem","position":2,"name":p["kw"],
                 "item":f"https://ewastekochi.com/{p['slug']}.html"}]}
        ]
    }, indent=2)

# ── CONTENT LAYERS ────────────────────────────────────────────────────────────
def layer_deep(kw):
    blocks = []
    topics = [
        ("What Is "+kw,
         f"{kw} is a critical service for businesses and households in Kochi, Kerala. "
         f"With the rapid pace of technological change, retiring electronic assets safely has become both a compliance imperative and an environmental responsibility. "
         f"Under E-Waste Management Rules 2022 and the DPDP Act 2023, organisations that generate electronic waste in Kerala are legally obligated to dispose of it through a KSPCB-authorised recycler. "
         f"Failure to comply can result in significant penalties. EWaste Kochi is the only KSPCB-authorised ITAD facility in Ernakulam district offering full NIST 800-88 certified sanitisation."),
        ("Why Certified "+kw+" Matters",
         f"Informal or uncertified {kw.lower()} creates hidden liabilities. Data remnants on retired hard drives, SSDs, and mobile devices can be recovered using freely available tools even after a standard factory reset. "
         f"Under the DPDP Act 2023, if personal data is accessed from a device disposed without proper certification, the original data fiduciary (your business) bears full liability — with penalties up to ₹250 Crore. "
         f"A Certificate of Destruction from an authorised facility is your legal shield."),
        ("Environmental Impact of Proper "+kw,
         f"Electronic devices contain hazardous materials including lead, mercury, cadmium, and hexavalent chromium. When disposed improperly — through roadside scrap dealers or landfills — these toxins leach into groundwater and soil, creating long-term ecological damage. "
         f"At EWaste Kochi, 97% of all recovered materials are recycled into secondary raw materials. Precious metals including gold, silver, and palladium are recovered and re-entered into the global supply chain, reducing demand for destructive mining operations."),
        ("Corporate "+kw+" in Kochi Tech Parks",
         f"Kochi's Infopark and SmartCity campuses house hundreds of IT companies, BPOs, and fintech startups — all of which generate significant volumes of IT assets annually. "
         f"The average Infopark company retires 50–200 devices per year. Without a formal {kw.lower()} program, these assets represent both a data security risk and a compliance gap. "
         f"EWaste Kochi operates a dedicated B2B desk for Infopark and SmartCity clients, offering on-site data destruction and same-day Certificate of Destruction issuance."),
        ("Regulatory Framework for "+kw+" in Kerala",
         f"Kerala's regulatory environment for e-waste is governed by multiple overlapping frameworks: (1) E-Waste Management Rules 2022 under the Environment Protection Act; (2) DPDP Act 2023 for personal data on devices; (3) KSPCB authorisation requirements for recyclers; (4) EPR obligations for producers and bulk consumers. "
         f"EWaste Kochi maintains full compliance with all four frameworks and can provide documentation packages for client audits."),
    ]
    for h, body in topics:
        para = ''.join(f"<p>{s.strip()}</p>" for s in body.split('. ') if len(s) > 40)
        blocks.append(f"<h2>{h}</h2>{para}")
    return "\n".join(blocks)

def layer_locations(kw):
    rows = "".join(
        f'<div class="loc-card"><span class="loc-icon">📍</span>'
        f'<strong>{a}</strong><br>'
        f'<span>{kw} pickup available. Free for 50+ units.</span></div>'
        for a in AREAS
    )
    return f"""
<section class="section loc-section" id="locations">
<div class="wrap">
<h2>Serving Every Kochi Micro-Cluster</h2>
<p>Our fleet covers all 30 Ernakulam pin-codes. Same-day pickup available for corporate accounts in major tech zones.</p>
<div class="loc-grid">{rows}</div>
</div>
</section>"""

def layer_process():
    steps = [
        ("📞 Step 1 — Contact & Assessment", "Call, WhatsApp, or fill the form. Our specialist assesses device type, count, and data sensitivity level."),
        ("🚚 Step 2 — Scheduled Pickup", "We dispatch a sealed, GPS-tracked van. Chain-of-custody begins the moment devices are loaded. Pickup confirmation sent via SMS."),
        ("🔒 Step 3 — Data Destruction", "At our KSPCB-authorised facility, every storage device undergoes NIST 800-88 certified wiping or physical shredding — witnessed and logged by serial number."),
        ("📋 Step 4 — Certificate of Destruction", "A legally-valid Certificate of Destruction is issued for every device — listing asset tag, serial, make, model, destruction method, technician, and date."),
        ("♻️ Step 5 — Eco-Responsible Recycling", "Device shells, PCBs, and recovered metals are processed through our zero-landfill recycling stream. A full materials report is available upon request."),
    ]
    cards = "".join(
        f'<div class="proc-card"><div class="proc-num">{i+1}</div>'
        f'<h3>{t}</h3><p>{d}</p></div>'
        for i,(t,d) in enumerate(steps)
    )
    return f"""
<section class="section" id="process">
<div class="wrap">
<h2>Our 5-Step Certified Process</h2>
<div class="proc-grid">{cards}</div>
</div>
</section>"""

def layer_trust():
    certs = [
        ("🌿","KSPCB Authorised","Licensed by Kerala State Pollution Control Board as authorised e-waste recycler under E-Waste Management Rules 2022."),
        ("🔒","NIST 800-88 Certified","Data sanitisation per the US National Institute of Standards and Technology SP 800-88 Rev.1 — the global gold standard."),
        ("🛡️","DPDP Act 2023 Compliant","Full documentation trail satisfying India's Digital Personal Data Protection Act obligations for data fiduciaries."),
        ("📋","DoD 5220.22-M Capable","US Department of Defense standard wipe available for government-adjacent and high-security clients."),
        ("♻️","EPR Registered","Extended Producer Responsibility registration ensuring downstream recycling accountability."),
        ("⭐","4.9★ Google Rating","143 verified reviews from Kochi's corporate and individual clients."),
    ]
    cards = "".join(
        f'<div class="trust-card"><span class="trust-icon">{ico}</span>'
        f'<strong>{name}</strong><p>{desc}</p></div>'
        for ico,name,desc in certs
    )
    return f"""
<section class="section" id="trust">
<div class="wrap">
<h2>Why EWaste Kochi is Kochi's Most Trusted Partner</h2>
<div class="trust-grid">{cards}</div>
</div>
</section>"""

def layer_links(idx, pillar):
    cross = get_cross_links(idx)
    blogs = get_blog_links(idx)
    cross_html = "".join(
        f'<a href="/{p["slug"]}.html" class="silo-link">{p["emoji"]} {p["kw"]}</a>'
        for p in cross
    )
    blog_html = "".join(
        f'<a href="/blog/?cat={b.replace(" ","-").lower()}" class="silo-link blog-silo">📝 {b}</a>'
        for b in blogs
    )
    return f"""
<section class="section silo-section" id="link-hub">
<div class="wrap">
<h2>Authority Navigation Hub</h2>
<p>Explore related certified services:</p>
<div class="silo-grid">
  <a href="/" class="silo-link home-silo">🏠 EWaste Kochi Homepage</a>
  {cross_html}
  {blog_html}
</div>
</div>
</section>"""

def layer_funnel(kw):
    return f"""
<section class="section cta-funnel" id="cta">
<div class="wrap" style="text-align:center">
<h2>Ready to Schedule Your {kw}?</h2>
<p>Join 200+ Kochi businesses that trust us for certified, compliant disposal. Free pickup for 50+ units.</p>
<div class="cta-row">
  <a href="https://wa.me/917500555454?text=Hi%2C+I+need+{kw.replace(' ','+')}+service" class="btn-wa">💬 WhatsApp Us Now</a>
  <a href="/get-instant-quote.html" class="btn-primary">📋 Get Instant Quote</a>
</div>
<p class="cta-sub">Or ask our chatbot below — it takes under 60 seconds.</p>
</div>
</section>"""

def layer_faq(faqs):
    items = "".join(
        f"""<details class="faq-item">
  <summary class="faq-q">{f['q']}</summary>
  <p class="faq-a">{f['a']}</p>
</details>"""
        for f in faqs
    )
    return f"""
<section class="section faq-section" id="faq">
<div class="wrap">
<h2>200 Expert FAQs — Kochi Local Authority</h2>
<div class="faq-stack">{items}</div>
</div>
</section>"""

# ── CHATBOT ───────────────────────────────────────────────────────────────────
CHATBOT_HTML = """
<div id="chatbot" class="chatbot-wrap">
  <button class="chat-toggle" id="chat-btn" onclick="chatToggle()" title="Get a quote">💬<span class="chat-dot" id="cdot"></span></button>
  <div class="chat-win" id="chat-win" hidden>
    <div class="chat-header">
      <span>🤖 EWaste Kochi Bot</span>
      <button onclick="chatToggle()">✕</button>
    </div>
    <div class="chat-msgs" id="chat-msgs"></div>
    <div class="chat-footer">
      <input id="chat-in" type="text" placeholder="Type reply…" onkeydown="if(event.key==='Enter')chatSend()">
      <button onclick="chatSend()">➤</button>
    </div>
  </div>
</div>
<script>
var CF={step:0,item:'',area:'',phone:''};
function chatToggle(){var w=document.getElementById('chat-win');w.hidden=!w.hidden;if(!w.hidden&&CF.step===0)chatBot('Hi! What e-waste items do you have? (e.g. 10 laptops, 3 hard drives)');}
function chatBot(t){var b=document.getElementById('chat-msgs');b.innerHTML+='<div class="cm bot">'+t+'</div>';b.scrollTop=9999;}
function chatUser(t){var b=document.getElementById('chat-msgs');b.innerHTML+='<div class="cm user">'+t+'</div>';b.scrollTop=9999;}
function chatSend(){
  var v=document.getElementById('chat-in').value.trim();if(!v)return;
  chatUser(v);document.getElementById('chat-in').value='';
  setTimeout(function(){
    if(CF.step===0){CF.item=v;CF.step=1;chatBot('Got it. Which area in Kochi are you located? (Kakkanad, Aluva, etc.)');}
    else if(CF.step===1){CF.area=v;CF.step=2;chatBot('Last step — your phone number for our logistics team?');}
    else if(CF.step===2){CF.phone=v;CF.step=3;
      chatBot('Connecting you to WhatsApp for instant confirmation ✅');
      var msg='Hi+EWaste+Kochi%2C+I+have+'+encodeURIComponent(CF.item)+'+at+'+encodeURIComponent(CF.area)+'.+Call+me+at+'+encodeURIComponent(CF.phone);
      setTimeout(function(){window.open('https://wa.me/917500555454?text='+msg,'_blank');},1200);}
  },600);
}
setTimeout(function(){if(CF.step===0){chatToggle();}},10000);
</script>
"""

# ── STYLES ────────────────────────────────────────────────────────────────────
PILLAR_CSS = """
<style>
:root{--bg:#0A0F0C;--bg2:#111A14;--green:#00E664;--white:#E8F2EA;--text:#9BB8A2;--muted:#5A7A62;--border:rgba(0,230,100,.13);--r:14px;}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:'Outfit',sans-serif;background:var(--bg);color:var(--text);line-height:1.75;overflow-x:hidden}
a{color:inherit;text-decoration:none}
.wrap{max-width:1240px;margin:0 auto;padding:0 24px}
.section{padding:80px 0;border-bottom:1px solid var(--border)}
h1,h2{font-family:'Bebas Neue',cursive;text-transform:uppercase;line-height:1.05}
h1{font-size:clamp(2.8rem,7vw,5.5rem);color:var(--white);margin-bottom:24px}
h2{font-size:clamp(2rem,4vw,3rem);color:var(--white);margin-bottom:24px}
h3{font-size:1.2rem;color:var(--white);margin-bottom:10px}
p{margin-bottom:16px;color:var(--text)}
/* hero */
.hero{min-height:80vh;display:flex;align-items:center;background:radial-gradient(ellipse at 20% 50%,rgba(0,230,100,.08),transparent 60%);border-bottom:1px solid var(--border)}
.badge-pill{display:inline-block;background:rgba(0,230,100,.12);border:1px solid rgba(0,230,100,.3);color:var(--green);padding:6px 18px;border-radius:50px;font-size:.8rem;font-weight:700;letter-spacing:1px;margin-bottom:24px}
.hero-cta{display:flex;gap:16px;flex-wrap:wrap;margin-top:32px}
.btn-wa{display:inline-flex;align-items:center;gap:8px;background:#25D366;color:#fff;font-weight:800;padding:14px 28px;border-radius:10px;font-size:1rem;transition:transform .2s,box-shadow .2s}
.btn-wa:hover{transform:translateY(-2px);box-shadow:0 8px 24px rgba(37,211,102,.35)}
.btn-primary{display:inline-flex;align-items:center;gap:8px;background:var(--green);color:var(--bg);font-weight:800;padding:14px 28px;border-radius:10px;font-size:1rem;transition:transform .2s}
.btn-primary:hover{transform:translateY(-2px)}
.btn-outline{display:inline-flex;align-items:center;gap:8px;border:2px solid var(--green);color:var(--green);font-weight:700;padding:12px 26px;border-radius:10px;font-size:.9rem;transition:all .2s}
.btn-outline:hover{background:var(--green);color:var(--bg)}
/* stats */
.stats-bar{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;margin:60px 0}
.stat-box{background:var(--bg2);border:1px solid var(--border);border-radius:var(--r);padding:28px;text-align:center}
.stat-num{font-family:'Bebas Neue';font-size:2.8rem;color:var(--green);display:block;line-height:1}
.stat-label{font-size:.75rem;text-transform:uppercase;letter-spacing:1px;color:var(--muted);margin-top:6px}
/* loc */
.loc-section{background:var(--bg2)}
.loc-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:14px;margin-top:32px}
.loc-card{background:var(--bg);border:1px solid var(--border);border-radius:var(--r);padding:18px;font-size:.85rem;transition:border-color .2s}
.loc-card:hover{border-color:var(--green)}
.loc-icon{display:block;font-size:1.2rem;margin-bottom:6px}
/* process */
.proc-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:20px;margin-top:32px}
.proc-card{background:var(--bg2);border:1px solid var(--border);border-radius:var(--r);padding:28px;position:relative}
.proc-num{position:absolute;top:20px;right:20px;font-family:'Bebas Neue';font-size:3rem;color:rgba(0,230,100,.1);line-height:1}
/* trust */
.trust-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:20px;margin-top:32px}
.trust-card{background:var(--bg2);border:1px solid var(--border);border-radius:var(--r);padding:24px}
.trust-icon{font-size:2rem;display:block;margin-bottom:12px}
/* silo */
.silo-section{background:rgba(0,230,100,.02)}
.silo-grid{display:flex;flex-wrap:wrap;gap:12px;margin-top:24px}
.silo-link{background:var(--bg2);border:1px solid var(--border);color:var(--green);padding:10px 18px;border-radius:8px;font-size:.85rem;font-weight:700;transition:all .2s}
.silo-link:hover{background:var(--green);color:var(--bg)}
.home-silo{border-color:var(--green)}
.blog-silo{color:var(--white)}
/* funnel */
.cta-funnel{background:linear-gradient(135deg,rgba(0,230,100,.06),transparent);text-align:center}
.cta-row{display:flex;gap:16px;justify-content:center;flex-wrap:wrap;margin:32px 0 16px}
.cta-sub{font-size:.85rem;color:var(--muted)}
/* faq */
.faq-stack{display:flex;flex-direction:column;gap:10px;margin-top:32px}
.faq-item{background:var(--bg2);border:1px solid var(--border);border-radius:10px;overflow:hidden;transition:border-color .2s}
.faq-item:hover,.faq-item[open]{border-color:rgba(0,230,100,.4)}
.faq-q{padding:18px 22px;cursor:pointer;font-weight:700;color:var(--white);list-style:none;display:flex;justify-content:space-between;align-items:center;gap:12px}
.faq-q::after{content:"＋";font-size:1.2rem;color:var(--green);flex-shrink:0;transition:transform .2s}
.faq-item[open] .faq-q::after{transform:rotate(45deg)}
.faq-a{padding:0 22px 18px;color:var(--text);line-height:1.8}
/* chatbot */
.chatbot-wrap{position:fixed;bottom:28px;right:24px;z-index:9999}
.chat-toggle{width:58px;height:58px;border-radius:50%;background:var(--green);color:var(--bg);font-size:1.4rem;display:flex;align-items:center;justify-content:center;box-shadow:0 4px 20px rgba(0,230,100,.45);position:relative;transition:transform .2s}
.chat-toggle:hover{transform:scale(1.08)}
.chat-dot{position:absolute;top:5px;right:5px;width:10px;height:10px;background:#ff4d6d;border-radius:50%;animation:pulse 1.5s infinite}
@keyframes pulse{0%,100%{transform:scale(1);opacity:1}50%{transform:scale(1.4);opacity:.6}}
.chat-win{position:absolute;bottom:70px;right:0;width:340px;background:var(--bg2);border:1px solid var(--border);border-radius:16px;overflow:hidden;display:flex;flex-direction:column;box-shadow:0 8px 40px rgba(0,0,0,.6)}
.chat-header{background:rgba(0,230,100,.08);padding:14px 16px;display:flex;align-items:center;justify-content:space-between;font-weight:700;color:var(--white);border-bottom:1px solid var(--border)}
.chat-msgs{height:240px;overflow-y:auto;padding:14px;display:flex;flex-direction:column;gap:10px}
.cm{max-width:85%;padding:10px 14px;border-radius:12px;font-size:.87rem;line-height:1.5}
.cm.bot{background:rgba(0,230,100,.1);border:1px solid rgba(0,230,100,.15);align-self:flex-start}
.cm.user{background:rgba(255,255,255,.08);align-self:flex-end}
.chat-footer{display:flex;border-top:1px solid var(--border);padding:10px}
.chat-footer input{flex:1;background:transparent;border:none;color:var(--white);padding:6px 10px;font-size:.9rem;outline:none}
.chat-footer button{background:var(--green);color:var(--bg);border:none;border-radius:8px;padding:6px 14px;font-weight:800;cursor:pointer}
/* nav */
.site-nav{background:rgba(7,16,10,.95);backdrop-filter:blur(20px);border-bottom:1px solid var(--border);position:sticky;top:0;z-index:100}
.nav-inner{max-width:1240px;margin:0 auto;padding:0 24px;height:64px;display:flex;align-items:center;justify-content:space-between}
.nav-brand{font-family:'Bebas Neue';font-size:1.4rem;color:var(--white);display:flex;align-items:center;gap:8px}
.nav-links{display:flex;gap:24px;font-size:.85rem;color:var(--muted);font-weight:600}
.nav-links a:hover{color:var(--green)}
.nav-cta{background:var(--green);color:var(--bg);padding:8px 18px;border-radius:8px;font-weight:800;font-size:.85rem}
/* footer */
.site-footer{background:#050806;padding:60px 0 30px;border-top:1px solid var(--border)}
.footer-grid{display:grid;grid-template-columns:2fr 1fr 1fr;gap:40px;margin-bottom:40px}
.footer-brand{font-family:'Bebas Neue';font-size:1.6rem;color:var(--white);margin-bottom:12px}
.footer-desc{font-size:.85rem;line-height:1.7;color:var(--muted);max-width:340px}
.footer-head{font-weight:800;color:var(--white);margin-bottom:14px;font-size:.9rem;text-transform:uppercase;letter-spacing:.5px}
.footer-links{display:flex;flex-direction:column;gap:8px;font-size:.85rem;color:var(--muted)}
.footer-links a:hover{color:var(--green)}
.footer-bottom{border-top:1px solid var(--border);padding-top:24px;display:flex;justify-content:space-between;align-items:center;font-size:.78rem;color:var(--muted);flex-wrap:wrap;gap:8px}
.pillar-nav{display:flex;flex-wrap:wrap;gap:10px;padding:20px 0;border-top:1px solid var(--border)}
.pillar-nav a{color:var(--green);font-size:.8rem;font-weight:700}
.pillar-nav a:hover{text-decoration:underline}
/* responsive */
@media(max-width:768px){
  .stats-bar,.footer-grid{grid-template-columns:1fr 1fr}
  .proc-grid,.trust-grid{grid-template-columns:1fr}
  .nav-links{display:none}
  .chat-win{width:300px}
  h1{font-size:2.6rem}
}
@media(max-width:480px){.stats-bar{grid-template-columns:1fr 1fr}.hero-cta{flex-direction:column}}
</style>
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Outfit:wght@300;400;600;700;800&display=swap" rel="stylesheet">
"""

# ── NAV ───────────────────────────────────────────────────────────────────────
def build_nav(active_slug):
    links = "".join(
        f'<a href="/{p["slug"]}.html"{"style=color:var(--green)" if p["slug"]==active_slug else ""}>{p["emoji"]} {p["kw"].split()[0]}</a>'
        for p in PILLARS[:5]
    )
    return f"""
<nav class="site-nav" id="main-nav">
<div class="nav-inner">
  <a class="nav-brand" href="/"><span>♻️</span> EWaste Kochi</a>
  <div class="nav-links">{links}<a href="/blog/">Blog</a></div>
  <a class="nav-cta" href="https://wa.me/917500555454">WhatsApp →</a>
</div>
</nav>"""

# ── FOOTER ────────────────────────────────────────────────────────────────────
def build_footer():
    pillar_links = " · ".join(
        f'<a href="/{p["slug"]}.html">{p["emoji"]} {p["kw"]}</a>' for p in PILLARS
    )
    return f"""
<footer class="site-footer">
<div class="wrap">
  <div class="footer-grid">
    <div>
      <div class="footer-brand">♻️ EWaste Kochi</div>
      <p class="footer-desc">Kerala's #1 KSPCB-authorised ITAD and e-waste recycling facility in Thrippunithura, Kochi. NIST 800-88 certified. DPDP Act 2023 compliant. Certificate of Destruction every job.</p>
    </div>
    <div>
      <div class="footer-head">Services</div>
      <div class="footer-links">
        {''.join(f'<a href="/{p["slug"]}.html">{p["kw"]}</a>' for p in PILLARS[:5])}
      </div>
    </div>
    <div>
      <div class="footer-head">Contact</div>
      <div class="footer-links">
        <span>📍 710A Hill Palace Rd, Thrippunithura, Kochi 682301</span>
        <a href="tel:+917500555454">📞 +91-7500555454</a>
        <a href="mailto:info@ewastekochi.com">✉️ info@ewastekochi.com</a>
        <span>⏰ Mon–Sat 8AM–8PM | Corp 24/7</span>
      </div>
    </div>
  </div>
  <div class="pillar-nav">{pillar_links}</div>
  <div class="footer-bottom">
    <span>© 2026 EWaste Kochi | KSPCB Authorised | NIST 800-88 | DPDP Act Compliant</span>
    <span><a href="/privacy-policy.html">Privacy</a> · <a href="/terms-of-service.html">Terms</a></span>
  </div>
</div>
</footer>"""

# ── PAGE BUILDER ──────────────────────────────────────────────────────────────
def build_page(idx, p):
    kw    = p["kw"]
    slug  = p["slug"]
    faqs  = gen_faqs(kw)
    schema_json = build_schema(p, faqs)

    hero = f"""
<section class="section hero" id="hero">
<div class="wrap">
  <span class="badge-pill">✅ KSPCB Authorised · NIST 800-88 · DPDP 2023</span>
  <h1>{kw}<br><em style="color:var(--green)">Kochi's #1 Certified Hub — 2026</em></h1>
  <p style="max-width:680px;font-size:1.1rem;color:var(--white);opacity:.85">Comprehensive, certified {kw.lower()} for homes and enterprises across all Ernakulam pin-codes. Zero-landfill guarantee. Certificate of Destruction every job.</p>
  <div class="hero-cta">
    <a class="btn-wa" href="https://wa.me/917500555454?text=Hi%2C+I+need+{kw.replace(' ','+')}">💬 WhatsApp for Instant Quote</a>
    <a class="btn-outline" href="#faq">Read 200 FAQs →</a>
  </div>
  <div class="stats-bar">
    <div class="stat-box"><span class="stat-num">5,000+</span><span class="stat-label">Devices Processed</span></div>
    <div class="stat-box"><span class="stat-num">200+</span><span class="stat-label">Corporate Clients</span></div>
    <div class="stat-box"><span class="stat-num">0</span><span class="stat-label">Data Breach Incidents</span></div>
    <div class="stat-box"><span class="stat-num">100%</span><span class="stat-label">CoD Issuance Rate</span></div>
  </div>
</div>
</section>"""

    deep_content = f"""
<section class="section" id="guide">
<div class="wrap">
{layer_deep(kw)}
</div>
</section>"""

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{kw} | #1 Certified Hub Kochi Ernakulam 2026</title>
<meta name="description" content="Ultimate guide on {kw}. NIST 800-88 data destruction, KSPCB compliance, free corporate pickup in Kochi. 200 expert FAQs. Certificate of Destruction every job.">
<link rel="canonical" href="https://ewastekochi.com/{slug}.html">
<meta property="og:title" content="{kw} | EWaste Kochi">
<meta property="og:url" content="https://ewastekochi.com/{slug}.html">
<meta property="og:type" content="article">
{PILLAR_CSS}
<script type="application/ld+json">{schema_json}</script>
</head>
<body>
{build_nav(slug)}
{hero}
{deep_content}
{layer_locations(kw)}
{layer_process()}
{layer_trust()}
{layer_links(idx, p)}
{layer_funnel(kw)}
{layer_faq(faqs)}
{build_footer()}
{CHATBOT_HTML}
</body>
</html>"""
    return html

# ── RUN ───────────────────────────────────────────────────────────────────────
def main():
    for idx, p in enumerate(PILLARS):
        path = os.path.join(OUT, f"{p['slug']}.html")
        html = build_page(idx, p)
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        size = os.path.getsize(path) / 1024
        print(f"  ✓ {p['slug']}.html  ({size:.0f} KB)")
    
    # Sitemap snippet for new pages
    sm_entries = "\n".join(
        f"  <url><loc>https://ewastekochi.com/{p['slug']}.html</loc>"
        f"<changefreq>weekly</changefreq><priority>0.9</priority></url>"
        for p in PILLARS
    )
    sm_path = os.path.join(OUT, "pillar_sitemap_fragment.xml")
    with open(sm_path, "w") as f:
        f.write(f"<!-- Add these inside your sitemap.xml urlset -->\n{sm_entries}\n")
    
    # Internal link map
    link_map = {}
    for idx, p in enumerate(PILLARS):
        link_map[p["slug"]] = {
            "incoming": ["index.html"],
            "outgoing_pillars": [x["slug"] for x in get_cross_links(idx)],
            "outgoing_blogs": get_blog_links(idx)
        }
    with open(os.path.join(OUT, "internal_link_map.json"), "w") as f:
        json.dump(link_map, f, indent=2)
    
    print(f"\n✅  10 Ultra-Pillar pages built.")
    print(f"✅  pillar_sitemap_fragment.xml generated.")
    print(f"✅  internal_link_map.json generated.")

if __name__ == "__main__":
    main()
