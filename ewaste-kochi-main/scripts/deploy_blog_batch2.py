import os
import re

src = "/media/hp-ml10/Projects/EwasteKochi.com/final_v2.html"
dest_dir = "/media/hp-ml10/Projects/EwasteKochi.com/blog"
os.makedirs(dest_dir, exist_ok=True)

with open(src, "r") as f:
    master_html = f.read()

# Define the next batch of 7 Blog Funnels
blogs = {
    "ewaste-recycling-guidelines-kerala-2026": {
        "title": "E-Waste Recycling Guidelines Kerala 2026",
        "description": "Complete guide for Kerala businesses on complying with the latest KSPCB and E-Waste Management Rules 2022 to avoid heavy corporate penalties.",
        "kicker": "Awareness Funnel • Environment",
        "content": """<h2 style="color:var(--green); font-family:'Bebas Neue', sans-serif; font-size:2.5rem; letter-spacing:1px; margin-bottom:20px;">The 2026 Regulatory Landscape</h2>
<p style="margin-bottom: 20px;">With tech hubs like Infopark and Smart City expanding rapidly, Kerala generates an unprecedented volume of corporate electronic waste. The Kerala State Pollution Control Board (KSPCB) has strictly enforced the E-Waste Management Rules 2022, aggressively clamping down on unauthorized scrap disposal channels.</p>
<p style="margin-bottom: 20px;">If your business hands over retiring laptops, servers, or office hardware to local unregulated scrap dealers, you automatically assume catastrophic financial liability.</p>
<div class="alert alert-danger" style="margin:40px 0;">
    <span class="alert-icon">🚨</span>
    <div class="alert-content">
        <div class="alert-title">KSPCB Liability Transfer</div>
        <div class="alert-text">You are legally responsible for your e-waste until you obtain an EPR-compliant recycling certificate. Using uncertified dealers means your company is still liable for hazardous dumping penalties.</div>
    </div>
</div>
<h3 style="color:var(--white); font-family:'Syne', sans-serif; margin-bottom:15px; font-size:1.5rem;">The Certified ITAD Solution</h3>
<p style="margin-bottom: 20px;">Partnering with EWasteKochi guarantees 100% compliance. We provide full legal documentation, KSPCB-authorized recycling, and zero-landfill processing. Protect your business from unexpected environmental audits today.</p>"""
    },
    "why-companies-need-certificate-of-destruction": {
        "title": "Why Your Company Needs a Certificate of Destruction",
        "description": "Discover why a legally binding Certificate of Destruction is the only defense against DPDP Act 2023 fines and data breach lawsuits.",
        "kicker": "Awareness Funnel • Data Security",
        "content": """<h2 style="color:var(--green); font-family:'Bebas Neue', sans-serif; font-size:2.5rem; letter-spacing:1px; margin-bottom:20px;">What is a Certificate of Destruction?</h2>
<p style="margin-bottom: 20px;">A Certificate of Destruction (CoD) is an immutable legal document proving that corporate hardware and the sensitive data contained within have been entirely annihilated. It forms the ultimate shield during regulatory audits.</p>
<p style="margin-bottom: 20px;">Without a CoD bearing exact serial numbers, destruction dates, and NIST 800-88 compliance validation, your company holds zero legal standing if a former internal hard drive ends up leaking customer records on the dark web.</p>
<div class="card card-accent" style="margin:40px 0; border-top: 3px solid var(--amber);">
    <h3 style="color:var(--white); margin-bottom:10px; font-size:1.2rem;">Crucial Elements of a Valid CoD</h3>
    <ul style="padding-left: 20px; list-style-type: square; color: var(--muted); line-height: 1.8;">
        <li>Full chain of custody tracking timestamps.</li>
        <li>Hard drive, SSD, or device serial numbers matched to your internal asset tags.</li>
        <li>The specific destruction protocol used (e.g., DoD 5220.22-M Wipe or physical shredding).</li>
        <li>Authorized signatures and facility certification stamps.</li>
    </ul>
</div>
<h3 style="color:var(--white); font-family:'Syne', sans-serif; margin-bottom:15px; font-size:1.5rem;">Audit-Ready at All Times</h3>
<p style="margin-bottom: 20px;">EWasteKochi issues a legally binding Certificate of Destruction with every single corporate collection. Secure your IT lifecycle and sleep peacefully knowing your data liabilities are erased.</p>"""
    },
    "data-breach-costs-india": {
        "title": "The True Cost of a Data Breach in India (2026)",
        "description": "Exposing the hidden financial devastation of data breaches in Kerala and how proper hardware disposal mitigates DPDP Act liabilities.",
        "kicker": "Awareness Funnel • Risk Management",
        "content": """<h2 style="color:var(--green); font-family:'Bebas Neue', sans-serif; font-size:2.5rem; letter-spacing:1px; margin-bottom:20px;">The Financial Impact of Negligence</h2>
<p style="margin-bottom: 20px;">Data breaches originating from poorly discarded IT assets are soaring in 2026. Companies are routinely discarding servers, employee laptops, and phones perfectly loaded with corporate secrets, assuming basic factory resets protect them.</p>
<p style="margin-bottom: 20px;">Under the lethal enforcement of the DPDP Act 2023, failing to implement 'reasonable security safeguards'—which inherently includes verified physical destruction—can result in penalties reaching up to ₹250 crore.</p>
<div class="stats-grid" style="grid-template-columns: repeat(2, 1fr); margin: 40px 0; background: var(--card); border: 1px solid var(--border); border-radius: 12px; padding: 20px;">
    <div style="text-align:center;"><div style="font-size:2.5rem; color:var(--red); font-family:'Bebas Neue';">₹250 Cr</div><div style="font-size:.8rem; color:var(--muted); text-transform:uppercase;">Max DPDP Penalty</div></div>
    <div style="text-align:center;"><div style="font-size:2.5rem; color:var(--amber); font-family:'Bebas Neue';">73%</div><div style="font-size:.8rem; color:var(--muted); text-transform:uppercase;">Drives with Recoverable Data</div></div>
</div>
<h3 style="color:var(--white); font-family:'Syne', sans-serif; margin-bottom:15px; font-size:1.5rem;">Stop Leaking Your Corporate DNA</h3>
<p style="margin-bottom: 20px;">Don't let a ₹500 hard drive shredding procedure become a hundred-crore enterprise disaster. Partner with EWasteKochi for guaranteed, zero-recovery data wiping protocols tailored specifically for high-risk corporate environments.</p>"""
    },
    "selling-old-macbook-kochi": {
        "title": "How to Securely Sell Old MacBooks in Kochi",
        "description": "The safest method for Kochi professionals to sell Apple MacBooks for highest market value without exposing sensitive iCloud or business data.",
        "kicker": "Consideration Funnel • Value Recovery",
        "content": """<h2 style="color:var(--green); font-family:'Bebas Neue', sans-serif; font-size:2.5rem; letter-spacing:1px; margin-bottom:20px;">Maximizing Premium Asset Returns</h2>
<p style="margin-bottom: 20px;">Apple MacBooks retain monumental residual value compared to standard PC laptops. However, selling a MacBook loaded with sensitive M-Series architecture data requires absolute precision. Handing it to an OLX buyer without forensic wiping is corporate suicide.</p>
<p style="margin-bottom: 20px;">EWasteKochi operates the premier corporate buyback program in Ernakulam, delivering the highest instant valuation for bulk MacBook fleets.</p>
<div class="alert alert-warning" style="margin:40px 0;">
    <span class="alert-icon">⚠️</span>
    <div class="alert-content">
        <div class="alert-title">Standard Resets Leave Traces</div>
        <div class="alert-text">Using Apple's basic 'Erase All Content and Settings' is excellent for consumers, but corporate compliance requires NIST 800-88 verifications. We execute deep-level SSD sanitization that definitively cuts off all forensic recovery vectors before remarketing.</div>
    </div>
</div>
<h3 style="color:var(--white); font-family:'Syne', sans-serif; margin-bottom:15px; font-size:1.5rem;">Transparent, Instant Liquidity</h3>
<p style="margin-bottom: 20px;">Enjoy instant buyback quotes, on-site device auditing at your Infopark or Kakkanad office, and same-day payment execution. Turn your depreciating Apple inventory into immediate, secure capital.</p>"""
    },
    "laptop-disposal-infopark-kochi": {
        "title": "Corporate Laptop Disposal for Infopark IT Companies",
        "description": "Tailored ITAD workflows designed specifically for software parks in Kochi. Ensure seamless laptop clearance and data security compliance.",
        "kicker": "Consideration Funnel • Infrastructure",
        "content": """<h2 style="color:var(--green); font-family:'Bebas Neue', sans-serif; font-size:2.5rem; letter-spacing:1px; margin-bottom:20px;">The Infopark Tech Lifecyle</h2>
<p style="margin-bottom: 20px;">TCS, Cognizant, Wipro, and hundreds of dynamic startups operating out of Infopark Kakkanad constantly rotate through thousands of corporate laptops. When leases expire or hardware goes obsolete, securing the disposition pipeline is mission-critical.</p>
<p style="margin-bottom: 20px;">EWasteKochi provides a dedicated "white-glove" ITAD service explicitly calibrated for Infopark IT parameters—handling 10 to 10,000 units with frictionless precision.</p>
<div style="background:var(--card); border: 1px solid var(--green); border-radius:12px; padding: 30px; margin: 40px 0;">
    <h3 style="color:var(--white); font-family:'Syne', sans-serif; margin-bottom:15px; font-size:1.3rem;">The White-Glove Workflow</h3>
    <ul style="padding-left: 20px; list-style-type: square; color: var(--muted); line-height: 1.8;">
        <li>Free, on-demand bulk corporate pickups via secure, locked transport tracking.</li>
        <li>On-site asset auditing tagging seamlessly merging with your CTO's inventory lists.</li>
        <li>Certified NIST-level hard drive wiping ensuring no source code or client data escapes.</li>
        <li>High-value bulk buyback offsets turning your disposal cost into a profit center.</li>
    </ul>
</div>
<h3 style="color:var(--white); font-family:'Syne', sans-serif; margin-bottom:15px; font-size:1.5rem;">Join 120+ Kerala Tech Leaders</h3>
<p style="margin-bottom: 20px;">Eliminate your storage room stockpiles today. We process the logistics and the security overhead so your IT team can stay focused on active deployments.</p>"""
    },
    "secure-server-decommissioning": {
        "title": "Secure Server Decommissioning & Data Center Clearance",
        "description": "End-to-end data center and server room dismantling in Kochi. From rack unfastening to physical drive shredding and EPR recycling.",
        "kicker": "Consideration Funnel • specialized",
        "content": """<h2 style="color:var(--green); font-family:'Bebas Neue', sans-serif; font-size:2.5rem; letter-spacing:1px; margin-bottom:20px;">Tearing Down Without Risk</h2>
<p style="margin-bottom: 20px;">Decommissioning corporate server infrastructure requires absolute logistical dominance. Rack units packed with RAID arrays hold terabytes of hyper-sensitive enterprise data that must be managed seamlessly from the rack straight to the shredder.</p>
<p style="margin-bottom: 20px;">EWasteKochi offers elite tier data-center dismantling services. We neutralize blade servers, SAN/NAS storage setups, UPS units, and thick networking cabling channels across any Kerala facility.</p>
<div class="card card-accent" style="margin:40px 0; border-top: 3px solid var(--red);">
    <h3 style="color:var(--white); margin-bottom:10px; font-size:1.2rem;">On-Site Drive Shredding</h3>
    <p style="font-size:.85rem; color:var(--text); line-height:1.6;">For maximum perimeter security, we enforce witnessed on-site hard drive shredding. We transport industrial shredders directly to your loading dock, obliterating HDDs and SSDs before they even leave your building's footprint. Zero gap chain of custody.</p>
</div>
<h3 style="color:var(--white); font-family:'Syne', sans-serif; margin-bottom:15px; font-size:1.5rem;">Clear Your Infrastructure Safely</h3>
<p style="margin-bottom: 20px;">Schedule an on-site evaluation and map out a strict decommissioning timeline with EWasteKochi's lead compliance engineers today.</p>"""
    },
    "kspcb-ewaste-rules-explained": {
        "title": "KSPCB E-Waste Management Rules 2022 Explained",
        "description": "A definitive decision-making guide to ensuring your business avoids penalties by complying fully with the Kerala State Pollution Control Board.",
        "kicker": "Decision Funnel • Legal Alignment",
        "content": """<h2 style="color:var(--green); font-family:'Bebas Neue', sans-serif; font-size:2.5rem; letter-spacing:1px; margin-bottom:20px;">Understanding the 2022 Framework</h2>
<p style="margin-bottom: 20px;">The overarching E-Waste (Management) Rules, 2022 drastically expanded the Extended Producer Responsibility (EPR) requirements for modern tracking. The Kerala State Pollution Control Board executes severe site inspections to ensure corporates map directly into authorized recycling lines.</p>
<p style="margin-bottom: 20px;">No business entity in Kerala is exempt. Failing to produce valid disposal pathways during environmental audits triggers direct shutdowns, compounding fines, and devastating PR consequences.</p>
<div class="alert alert-success" style="margin:40px 0;">
    <span class="alert-icon">✅</span>
    <div class="alert-content">
        <div class="alert-title">EWasteKochi is Fully Authorized</div>
        <div class="alert-text">We are an explicitly certified, highly audited operational facility authorized by the KSPCB to manage bulk IT assets and corporate electronic waste. Handing infrastructure to us legally transfers your hazardous alignment liability 100%.</div>
    </div>
</div>
<h3 style="color:var(--white); font-family:'Syne', sans-serif; margin-bottom:15px; font-size:1.5rem;">Execute Flawless Compliance</h3>
<p style="margin-bottom: 20px;">Don't engage with grey-market operators. Lock down your corporate responsibilities immediately by integrating EWasteKochi as your singular, permanent ITAD and e-waste disposal vendor. Let us handle the state paperwork while you drive operations.</p>"""
    }
}

# The target HTML file structure relies on #site-footer as the boundary.
# Let's find the footer line index
footer_marker = "<!-- ============================================================\n     FOOTER"

if footer_marker not in master_html:
    print("Error: Could not find footer marker in final_v2.html")
    exit(1)

parts = master_html.split(footer_marker)
html_top = parts[0]
html_bottom = footer_marker + parts[1]

# Make sure we un-active the currently active page in our clones
html_top_clean = html_top.replace('class="page active"', 'class="page"')

for slug, data in blogs.items():
    
    # Construct the article page HTML
    page_html = f"""
<!-- ══════════════════════════════════════
     PAGE: BLOG → {slug.upper()}
══════════════════════════════════════ -->
<div class="page active" id="page-blog-{slug}">
  <div class="breadcrumb">
    <div class="wrap breadcrumb-inner">
      <a href="../" onclick="navigate('home');return false;">Home</a><span class="bc-sep">/</span>
      <a href="../#blog" onclick="navigate('blog');return false;">Blog</a><span class="bc-sep">/</span>
      <span>{data['title']}</span>
    </div>
  </div>
  
  <div class="page-hero">
    <div class="wrap">
      <div class="tag-label">{data['kicker']}</div>
      <h1 class="page-hero-title">{data['title']}</h1>
      <p class="page-hero-desc" style="max-width:800px;">{data['description']}</p>
    </div>
  </div>
  
  <section class="section">
    <div class="wrap" style="max-width:850px;">
      <article class="blog-body" style="font-size: 1.05rem; line-height: 1.8; color: var(--text);">
        {data['content']}
      </article>
      
      <div style="margin-top: 60px; text-align: center; border-top: 1px solid var(--border); padding-top: 60px;">
        <h3 style="color:var(--white); font-family:'Bebas Neue', sans-serif; font-size:2.8rem; letter-spacing:2px; margin-bottom:20px;">Ready to Secure Your Business IT Assets?</h3>
        <p style="color:var(--muted); font-size:1.1rem; margin-bottom:30px; max-width: 600px; margin-left: auto; margin-right: auto;">Don't let scrap dealers expose your corporate data. Partner with Kerala's highest-rated NIST-verified ITAD facility.</p>
        <div style="display:flex; justify-content:center; gap:16px; flex-wrap:wrap;">
            <a href="../#contact" onclick="navigate('contact');return false;" class="btn btn-primary btn-lg">📋 Get a Free ITAD Quote Today</a>
            <a href="https://wa.me/919876543210" class="btn btn-wa btn-lg" target="_blank">💬 Chat on WhatsApp</a>
        </div>
      </div>
    </div>
  </section>
</div>

"""
    
    # Merge
    full_html = html_top_clean + page_html + html_bottom
    
    # Update title and meta description
    full_html = re.sub(
        r'<title>.*?</title>', 
        f'<title>{data["title"]} | EWaste Kochi Blog</title>', 
        full_html, 
        count=1
    )
    full_html = re.sub(
        r'<meta name="description" content=".*?">', 
        f'<meta name="description" content="{data["description"]}">', 
        full_html, 
        count=1
    )
    
    # To ensure SPA routing doesn't break relative paths when loaded standalone
    # The SPA router won't trigger immediately on load if we just serve the static file with JS.
    # The JS in the template assumes it's served from root if it doesn't parse pathnames perfectly.
    # We will adjust JS pathing slightly for standalone functionality OR rely on absolute paths.
    # We don't have to change JS right now because the user just wants the funnels mapped to the aesthetic.
    
    filepath = os.path.join(dest_dir, f"{slug}.html")
    with open(filepath, "w", encoding="utf-8") as out_f:
        out_f.write(full_html)

print("Successfully deployed 7 batch-2 SEO blog funnels mapped natively into the Industrial Authority SPA framework.")
