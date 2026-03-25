import os
import re

src = "/media/hp-ml10/Projects/EwasteKochi.com/index.html"
dest_dir = "/media/hp-ml10/Projects/EwasteKochi.com/blog"
os.makedirs(dest_dir, exist_ok=True)

with open(src, "r") as f:
    html = f.read()

# Define the 7 sequenced blog articles requested in the footer
blogs = {
    "what-is-itad": {
        "title": "What is ITAD? IT Asset Disposition Explained for Kerala Businesses",
        "kicker": "Awareness Funnel • IT Security",
        "hero_desc": "ITAD (IT Asset Disposition) is the business operations built around safely, ecologically, and legally disposing of obsolete or unwanted electronic equipment. Here is why your Kochi business needs it.",
        "content": '''<h2 style="color:var(--green); font-family:'Syne', sans-serif; margin-bottom:20px;">The Importance of ITAD</h2>
<p style="margin-bottom: 20px;">In an era dominated by rapid technological advancement, businesses constantly upgrade their IT infrastructure. <strong>ITAD</strong> is the secure, environmentally responsible, and legally compliant method of retiring these corporate assets.</p>
<p style="margin-bottom: 20px;">Simply storing old hard drives in a closet or handing them off to an unregulated scrap dealer strictly exposes your company to massive data breach liabilities and violation of the E-Waste Management Rules 2022.</p>
<div style="background:var(--panel); border:1px solid var(--border); padding:24px; border-radius:12px; margin:30px 0;">
<h3 style="color:var(--white); font-family:'Syne', sans-serif;">Key Components of Certified ITAD</h3>
<ul style="margin-top:15px; padding-left:20px;">
<li style="margin-bottom:10px;">End-to-end chain of custody documentation tracking every device.</li>
<li style="margin-bottom:10px;">NIST 800-88 compliant verifiable data destruction mechanics.</li>
<li style="margin-bottom:10px;">Legally binding Certificates of Destruction for RBI or Corporate audit compliance.</li>
<li style="margin-bottom:10px;">EPR (Extended Producer Responsibility) compliant recycling to guarantee zero-landfill operation.</li>
</ul></div>'''
    },
    "what-is-e-waste": {
        "title": "What is E-Waste? Understanding Kerala's Growing Crisis",
        "kicker": "Awareness Funnel • Environment",
        "hero_desc": "Electronic waste is the fastest-growing solid waste stream globally. Learn how Kochi businesses can handle it responsibly to avoid severe penalties and protect our ecosystem.",
        "content": '''<h2 style="color:var(--green); font-family:'Syne', sans-serif; margin-bottom:20px;">Defining Electronic Waste</h2>
<p style="margin-bottom: 20px;">E-waste refers to all items of electrical and electronic equipment (EEE) and its parts that have been discarded by its owner as waste without the intent of re-use.</p>
<p style="margin-bottom: 20px;">As IT companies in Infopark Kakkanad and Smart City cycle through hardware, secondary e-waste metrics are climbing rapidly. The Kerala State Pollution Control Board tightly monitors e-waste disposal channels heavily targeting non-compliant corporate entities.</p>
<p style="margin-bottom: 20px;">Only by collaborating explicitly with a certified ITAD partner like EWasteKochi can corporations legally transfer off their carbon recycling liabilities under E-Waste Rules 2022.</p>'''
    },
    "hard-drive-shredding-vs-degaussing": {
        "title": "Hard Drive Shredding vs Degaussing: Which is Safer?",
        "kicker": "Consideration Funnel • Infrastructure",
        "hero_desc": "Comparing physical hard drive shredding against magnetic degaussing. What are the absolute best NIST 800-88 compliant methodologies for enforcing zero data-recovery?",
        "content": '''<h2 style="color:var(--green); font-family:'Syne', sans-serif; margin-bottom:20px;">Magnetic Degaussing Explained</h2>
<p style="margin-bottom: 20px;">Degaussing involves passing a hard drive through a staggeringly powerful magnetic field, permanently altering the underlying magnetic domains and erasing all data. It is extremely fast and effective for magnetic HDDs, but <strong>does not work efficiently on Solid State Drives (SSDs)</strong>.</p>
<h2 style="color:var(--green); font-family:'Syne', sans-serif; margin-bottom:20px; margin-top:30px;">Industrial Physical Shredding</h2>
<p style="margin-bottom: 20px;">Industrial shredding physically destroys the drive down to millimeter-sized particulate matter rendering it harmless. It provides the ultimate visual proof of destruction and works on both HDDs and Solid State Drives (SSDs).</p>
<p style="margin-bottom: 20px;">For the highest level of security, EWasteKochi recommends employing <strong>both vectors simultaneously</strong>—magnetic degaussing followed by physical shredding, backed by an immutable Certificate of Destruction.</p>'''
    },
    "secure-data-destruction-methods": {
        "title": "A Guide to Secure Data Destruction Methods in 2026",
        "kicker": "Consideration Funnel • Compliance",
        "hero_desc": "Formatting a drive is not erasing it. Explore DoD 5220.22-M wiping, cryptographic erasure, and physical destruction standards critical for modern IT architecture compliance.",
        "content": '''<h2 style="color:var(--green); font-family:'Syne', sans-serif; margin-bottom:20px;">The Format Fallacy</h2>
<p style="margin-bottom: 20px;">Simply clicking 'Format' or using factory resets only deletes the file allocation layout map. The raw 1s and 0s remain 100% intact on the platters and can be retrieved using easily accessible software tools found anywhere online.</p>
<div style="background:linear-gradient(135deg,rgba(239,68,68,.09),rgba(239,68,68,.03)); border:1px solid rgba(239,68,68,.2); border-radius:20px; padding:28px; margin:30px 0;">
<h3 style="color:#FC8181; font-family:'Syne', sans-serif; font-weight:800;">Data Breaches Intentionally Target Secondary Markets</h3>
<p style="margin-top:10px;">Dozens of studies confirm that devices bought in secondary scrap markets across Ernakulam routinely contain recoverable private corporate data. Implementing Verified Data Destruction is no longer optional—it is a mandatory legal compliance layer under Section 8 guidelines.</p>
</div>'''
    },
    "dpdp-act-2023-it-disposal-kerala": {
        "title": "DPDP Act 2023: How It Impacts IT Asset Disposal in Kerala",
        "kicker": "Decision Funnel • Legal Liability",
        "hero_desc": "India's Digital Personal Data Protection Act carries up to ₹250 crore in corporate penalties. Discover why unregulated e-waste disposal is a direct and terrifying violation of the evolving law.",
        "content": '''<h2 style="color:var(--green); font-family:'Syne', sans-serif; margin-bottom:20px;">The Trap of Section 8 DPDP Act 2023</h2>
<p style="margin-bottom: 20px;">Under the newly established DPDP Act 2023 framework, mapped to 2026 enforcement rules, data fiduciaries face non-compliance penalties hitting up to ₹250 crore for failing to implement 'reasonable security safeguards'. This explicitly encompasses the end-of-lifecycle hardware disposal mechanisms.</p>
<p style="margin-bottom: 20px;">Selling your office hardware without an explicitly attached, third-party verified Certificate of Destruction violates these structural safeguards making CTOs heavily liable.</p>
<h3 style="color:var(--white); font-family:'Syne', sans-serif; margin-top:30px; margin-bottom:15px;">Deploying Your Defense Strategy</h3>
<p style="margin-bottom: 20px;">Partnering natively with EWasteKochi completely shifts the compliance burden. Our NIST-compliant wiping sequences guarantee an immutable audit trail, successfully bridging the strict regulatory gap between IT decommissioning and comprehensive data protection.</p>'''
    },
    "how-to-choose-itad-provider": {
        "title": "How to Choose an ITAD Provider in Kerala",
        "kicker": "Decision Funnel • Vendor Selection",
        "hero_desc": "Not all local scrap dealers are ITAD professionals. Equip yourself with this 7-point checklist for evaluating data destruction and e-waste scale vendors across Kochi.",
        "content": '''<h2 style="color:var(--green); font-family:'Syne', sans-serif; margin-bottom:20px;">The Critical Vendor Vetting Checklist</h2>
<p style="margin-bottom: 20px;">Before releasing any IT assets bearing corporate secrets, force your potential partner through this strict filter line:</p>
<ul style="margin-bottom: 20px; padding-left:20px;">
<li style="margin-bottom:10px;"><strong>Do they provide documented CoDs (Certificate of Destruction) enforcing hard serial-level tracking?</strong></li>
<li style="margin-bottom:10px;"><strong>Are their core destruction methodologies strictly NIST 800-88 & DoD 5220.22-M verified?</strong></li>
<li style="margin-bottom:10px;"><strong>Do they possess dedicated uncompromised facilities operating around the clock?</strong></li>
<li style="margin-bottom:10px;"><strong>Can they showcase valid EPR (Extended Producer Responsibility) Zero-Landfill integrations?</strong></li>
</ul>
<p style="margin-bottom: 20px;">EWasteKochi checks successfully against every global compliance checkpoint, eliminating friction for Kerala-based operations.</p>'''
    },
    "itad-service-kochi-2026": {
        "title": "The Premium ITAD Hub for Kochi Businesses in 2026",
        "kicker": "Decision Funnel • Conversion",
        "hero_desc": "Your definitive guide to executing secure, compliant, zero-risk, and profitable corporate IT asset disposition across Edappally, Ernakulam, and Infopark zones.",
        "content": '''<h2 style="color:var(--green); font-family:'Syne', sans-serif; margin-bottom:20px;">Protecting Kochi's Silicon Core</h2>
<p style="margin-bottom: 20px;">As complex IT infrastructure deepens across Smart City and Kakkanad, deploying rapid 24/7 ITAD protocols coupled with strict unrecoverable guarantees is absolutely paramount for business survival in 2026.</p>
<p style="margin-bottom: 20px;">EWasteKochi executes highly customized, elite enterprise-grade hardware disposal operations with aggressive, localized on-the-ground intelligence designed originally for Kerala’s hardest-hitting tech networks.</p>'''
    }
}

# Safely split the HTML document to retain the Hero and swap the middle out
prefix = html.split('<!-- ══ STATS BAND ══ -->')[0]
suffix = '<section id="faq"' + html.split('<section id="faq"')[1]

old_h1 = '''<h1 class="hero-h1">
          Secure E‑Waste &amp;
          <span class="acc">Certified ITAD</span>
          Data Destruction — Kochi
        </h1>'''

old_p = '''<p class="hero-desc">Kerala's most trusted 24/7 certified IT asset disposal (ITAD) and e‑waste recycling facility in Thrippunithura, Kochi. NIST/DoD hard drive shredding · Secure data wiping · Certificate of Destruction every job · Free corporate bulk pickup. Serving Infopark, Kakkanad, Ernakulam &amp; all of Kerala.</p>'''

old_kicker = "🏆 Kerala's #1 Certified ITAD &amp; E‑Waste Centre · Kochi 2026"

for slug, data in blogs.items():
    # Construct the highly readable localized article body
    article_body = f"""
<article class="blog-wrap" style="max-width: 850px; margin: 0 auto; padding: 80px 5%; font-size: 1.15rem; line-height: 1.8; color: var(--text);">
    {data["content"]}
    <div style="margin-top: 60px; text-align: center; border-top: 1px solid var(--border); padding-top: 40px; background: var(--dark); border-radius:12px; padding:40px;">
        <h3 style="color:var(--white); font-family:'Syne', sans-serif; font-size:1.4rem; margin-bottom:20px;">Ready to Secure Your Business IT Assets?</h3>
        <p style="color:var(--muted); font-size:1rem; margin-bottom:25px;">Don't let scrap dealers expose your data. Partner with a NIST-verified ITAD facility.</p>
        <a href="../index.html#contact" class="btn btn-p" style="padding:16px 32px; font-size:1.1rem; border-radius:50px;">Get a Free ITAD Quote Today</a>
    </div>
</article>
"""
    # Merge
    page = prefix + article_body + "\n\n" + suffix
    
    # Overwrite the specific hero strings
    new_h1 = f'<h1 class="hero-h1" style="font-size: clamp(2rem, 4vw, 3rem);"><span class="acc">{data["title"]}</span></h1>'
    new_p = f'<p class="hero-desc">{data["hero_desc"]}</p>'
    new_kicker = f'🏆 {data["kicker"]}'
    
    page = page.replace(old_h1, new_h1)
    page = page.replace(old_p, new_p)
    page = page.replace(old_kicker, new_kicker)
    
    # Replace <title> using regex for exact SEO formatting
    page = re.sub(r'<title>.*?</title>', f'<title>{data["title"]} | EWasteKochi ITAD</title>', page, count=1)
    
    with open(os.path.join(dest_dir, f"{slug}.html"), "w") as out_f:
        out_f.write(page)

print("Successfully deployed 7 sequence blog funnels mapped natively into the Dark Mode framework.")
