import sys
import re
import os

blog_dir = "/media/hp-ml10/Projects/ewastekochi-production/ewastekochi/blog/"
sample_file = os.path.join(blog_dir, "dpdp-act-impact-startups.html")
index_file = os.path.join(blog_dir, "index.html")

with open(sample_file, "r") as f:
    sample_html = f.read()

# 1. Extract standard Header and Footer bounds
# We split before <div class="wrap"><div class="breadcrumb">
split_1 = '<div class="wrap"><div class="breadcrumb">'
parts = sample_html.split(split_1)
head_nav = parts[0]

# Extract footer: split right after <div class="section"> ... reviews section and CTA section?
# Actually, the quickest way to get the universal footer is splitting at the first client reviews block.
# Wait, the sample file has a reviews block, a CTA block, then footer.
# Let's split before: <div class="section">\n  <div class="wrap">\n    <div class="section-tag">Client Reviews</div>
split_2 = '<div class="section">\n  <div class="wrap">\n    <div class="section-tag">Client Reviews</div>'
if split_2 not in sample_html:
    split_2 = '<div class="section-tag">Client Reviews</div>'
    
footer_full = '<div class="section">\n  <div class="wrap">\n    <div class="section-tag">Client Reviews</div>' + sample_html.split('<div class="section-tag">Client Reviews</div>')[1]

def build_blog(filename, title, tag_emoji, tag_label, desc, badge_color, badge_text, time_min, body_html):
    html = head_nav
    html = html.replace("<title>DPDP Act 2023 — What Kerala Startups Must Do Now — EWaste Kochi</title>", f"<title>{title} — EWaste Kochi</title>")
    html = html.replace('content="India\'s Digital Personal Data Protection Act 2023 creates new ITAD obligations for startups. Penalties up to ₹250 Crore. Here\'s what Kochi startups must do now."', f'content="{desc}"')
    html = html.replace('href="https://ewastekochi.com/blog/dpdp-act-impact-startups.html"', f'href="https://ewastekochi.com/blog/{filename}"')
    html = html.replace('content="DPDP Act 2023 — What Kerala Startups Must Do Now — EWaste Kochi"', f'content="{title} — EWaste Kochi"')
    
    html += f"""<div class="wrap"><div class="breadcrumb"><a href="/">Home</a><span class="breadcrumb-sep">/</span><a href="/blog/">Blog</a><span class="breadcrumb-sep">/</span><span style="color:var(--white)">{title}</span></div></div>

<div class="page-hero">
  <div class="wrap">
    <div class="page-hero-tag">{tag_emoji} {tag_label}</div>
    <h1 class="page-hero-title">{title}</h1>
    <p class="page-hero-desc">{desc}</p>
    <div style="display:flex;gap:10px;flex-wrap:wrap;margin-top:4px">
      <span class="badge badge-{badge_color}">{badge_text}</span>
      <span style="font-size:.75rem;color:var(--muted);display:flex;align-items:center;gap:4px">📅 Updated March 2026</span>
    </div>
  </div>
</div>
<div class="section">
  <div class="wrap" style="max-width:800px;margin:0 auto">
{body_html}
  </div>
</div>

"""
    html += footer_full
    
    with open(os.path.join(blog_dir, filename), "w") as f:
        f.write(html)
        
    return f"""<a href="/blog/{filename}" class="card" style="display:block;text-decoration:none">
  <div style="display:inline-flex;align-items:center;gap:6px;background:rgba(0,232,122,.08);border:1px solid rgba(0,232,122,.15);border-radius:6px;padding:3px 10px;margin-bottom:12px;font-size:.7rem;font-weight:700;color:var(--green);font-family:var(--font-m)">{tag_emoji} {tag_label}</div>
  <div class="card-title">{title}</div>
  <div style="display:flex;gap:8px;align-items:center;margin-top:10px">
    <span class="badge badge-{badge_color}">{badge_text}</span>
    <span style="font-size:.72rem;color:var(--muted)">📖 {time_min} min read</span>
  </div>
</a>
"""

cards_html = ""

# Blog 1
b1_body = """
<p style="color:var(--text);line-height:1.8;margin-bottom:20px">When it's time to upgrade your company's IT infrastructure, getting the highest possible value for your old laptops is a priority. Cashify is the default platform for consumers, but does it make sense for business-grade hardware? We analyzed the payout structures for enterprise laptops in Kochi.</p>

<h2 style="font-size:1.4rem;color:var(--white);margin:32px 0 16px">The Assessment: Why Cashify Underprices Enterprise Laptops</h2>
<p style="color:var(--text);line-height:1.8;margin-bottom:20px">Cashify’s algorithm is built around fast-moving consumer laptops—entry-level HP Pavilions, Dell Inspirons, and low-spec MacBooks. When assessing enterprise hardware like Lenovo ThinkPads, Dell Latitudes, or high-spec MacBook Pro M2s, their automated deductor often slashes value aggressively for minor cosmetic wear, ignoring the underlying enterprise components.</p>

<div class="comp-table-wrap" style="margin:28px 0">
  <table class="comp-table">
    <thead><tr><th>Device Model</th><th>Cashify Offer</th><th>EWaste Kochi Offer</th></tr></thead>
    <tbody>
      <tr><td><strong style="color:var(--white)">MacBook Pro M2 (16GB/512GB)</strong></td><td>~₹52,000</td><td><strong style="color:var(--green)">Up to ₹68,000 ✓</strong></td></tr>
      <tr><td><strong style="color:var(--white)">Lenovo ThinkPad T14 Gen 2</strong></td><td>~₹18,000</td><td><strong style="color:var(--green)">Up to ₹28,000 ✓</strong></td></tr>
      <tr><td><strong style="color:var(--white)">Dell Latitude 5000 Series (Core i7)</strong></td><td>~₹14,500</td><td><strong style="color:var(--green)">Up to ₹22,000 ✓</strong></td></tr>
    </tbody>
  </table>
</div>

<h2 style="font-size:1.4rem;color:var(--white);margin:32px 0 16px">Beyond Price: The Compliance Risk</h2>
<p style="color:var(--text);line-height:1.8;margin-bottom:20px">Selling to Cashify means selling to a consumer pipeline. The device is wiped via standard factory reset. If any corporate data remains (emails, cached credentials, client records), you violate the DPDP Act 2023. EWaste Kochi issues a <strong>Certificate of Destruction</strong> alongside a 15–20% higher payout.</p>

<a href="/sell-old-laptop-kochi.html" class="btn btn-primary" style="margin-top:10px">💻 Check Your Laptop's Value Now</a>
"""
cards_html += build_blog("cashify-vs-ewaste-kochi-laptop-buyback.html", "Cashify vs EWaste Kochi — Which Gives Better Resale Value?", "🏆", "Comparison", "Why corporate laptops get 20% more value at EWaste Kochi compared to Cashify in 2026.", "green", "Buyback", 5, b1_body)

# Blog 2
b2_body = """
<p style="color:var(--text);line-height:1.8;margin-bottom:20px">Infopark Kakkanad is the beating heart of Kerala's tech ecosystem. With thousands of IT companies cycling through hardware every 3-4 years, secure and compliant E-Waste disposal is a massive logistical challenge. Here is the operational guide for tech park compliance.</p>

<h2 style="font-size:1.4rem;color:var(--white);margin:32px 0 16px">Infopark E-Waste Logistics</h2>
<p style="color:var(--text);line-height:1.8;margin-bottom:20px">Extracting 50+ laptops, servers, and monitors from Phase 1 or SmartCity requires SEZ clearance passes and gate passes. As an authorized vendor, EWaste Kochi coordinates directly with Infopark administration to ensure frictionless hardware extraction without disrupting your daily operations.</p>

<div style="display:flex;flex-direction:column;gap:12px;margin:28px 0">
  <div class="card"><strong style="color:var(--white)">1. Zero-Cost Logistics</strong><p style="font-size:.84rem;color:var(--text);margin-top:6px;line-height:1.65">For lots over 50 units, box packing, loading, and secure transit from Infopark to our Thrippunithura facility is entirely free.</p></div>
  <div class="card"><strong style="color:var(--white)">2. Server Rack Dismantling</strong><p style="font-size:.84rem;color:var(--text);margin-top:6px;line-height:1.65">We provide specialized dismantling teams for end-of-life cloud server racks, network switches, and UPS systems right from your server room.</p></div>
</div>

<p style="color:var(--text);line-height:1.8;margin-bottom:20px">Furthermore, all hardware from Infopark tech companies undergoes mandatory NIST 800-88 data destruction to protect sensitive source code and client IP.</p>

<a href="/itad-kochi.html" class="btn btn-primary" style="margin-top:10px">🏢 Book Corporate ITAD Pickup</a>
"""
cards_html += build_blog("how-to-dispose-e-waste-in-infopark-kakkanad.html", "Complete Guide to E-Waste Disposal in Infopark Kochi", "📍", "Local Guide", "The 2026 logistical guide to clearing out servers and laptops from Infopark Kakkanad.", "blue", "Logistics", 4, b2_body)

# Blog 3
b3_body = """
<p style="color:var(--text);line-height:1.8;margin-bottom:20px">If your business generates E-Waste, the law states you cannot simply throw it away or give it to a scrap dealer. The E-Waste Management Rules 2022 strictly mandate that bulk consumers channel their e-waste only to facilities authorized by the Kerala State Pollution Control Board (KSPCB).</p>

<h2 style="font-size:1.4rem;color:var(--white);margin:32px 0 16px">The Dangers of Unauthorized Scrappers</h2>
<p style="color:var(--text);line-height:1.8;margin-bottom:20px">Local scrap dealers pay by weight and typically extract valuable metals using crude, highly toxic methods (like acid baths or open burning). If your hardware is traced back to these illegal operations, your company faces massive environmental fines and reputational destruction.</p>

<h2 style="font-size:1.4rem;color:var(--white);margin:32px 0 16px">The Verification Requirement</h2>
<p style="color:var(--text);line-height:1.8;margin-bottom:20px">To remain compliant during your annual audits (ISO 14001 or KSPCB filing), you must prove your ITAD partner is KSPCB authorized. EWaste Kochi provides full authorization documentation transparently upfront with every corporate contract.</p>

<a href="/get-instant-quote.html" class="btn btn-primary" style="margin-top:10px">⚖️ Work With Authorized Experts</a>
"""
cards_html += build_blog("what-is-kspcb-authorization-for-e-waste.html", "Why KSPCB Authorized Recyclers are Mandatory in Kerala", "🧾", "Legal", "Why using local scrap dealers in Kerala exposes you to massive environmental fines.", "amber", "Compliance", 6, b3_body)

# Blog 4
b4_body = """
<p style="color:var(--text);line-height:1.8;margin-bottom:20px">A quick Google search for 'how to wipe a laptop' yields hundreds of free software tools. However, for a Kochi business disposing of corporate laptops, comparing a free tool like DBAN to a certified NIST 800-88 process is a dangerous miscalculation.</p>

<h2 style="font-size:1.4rem;color:var(--white);margin:32px 0 16px">The Hidden SSD Flaw</h2>
<p style="color:var(--text);line-height:1.8;margin-bottom:20px">Free wiping software was designed for old spinning hard drives (HDDs). Modern NVMe solid-state drives (SSDs) use 'wear leveling' — constantly moving data around. A free software wipe cannot access the reserved sectors of an SSD, meaning <strong style="color:var(--red)">significant corporate data remains intact and fully recoverable</strong>.</p>

<div class="card" style="margin:28px 0"><strong style="color:var(--white)">NIST 800-88 Compliance</strong><p style="font-size:.84rem;color:var(--text);margin-top:6px;line-height:1.65">NIST SP 800-88 protocols issue specialized cryptographic firm-ware commands directly to the SSD controller, forcing a total flash-cell purge. This is the only method to guarantee data is mathematically impossible to recover.</p></div>

<p style="color:var(--text);line-height:1.8;margin-bottom:20px">Furthermore, a free tool does not generate a legally sound, third-party <strong>Certificate of Destruction</strong>, leaving you completely exposed under the DPDP Act 2023.</p>

<a href="/data-destruction-kochi.html" class="btn btn-primary" style="margin-top:10px">🔒 Secure Your Data Now</a>
"""
cards_html += build_blog("laptop-data-wiping-software-vs-nist.html", "Free Data Wiping Software vs NIST 800-88", "🛡️", "Technical", "Why free software like DBAN fails to wipe modern SSDs and exposes corporate data.", "red", "Security", 8, b4_body)

# Blog 5
b5_body = """
<p style="color:var(--text);line-height:1.8;margin-bottom:20px">Under the DPDP Act 2023, Kochi organizations must formally document how they handle data sanitization at the end of an IT asset’s lifecycle. Without a formalized Corporate E-Waste Policy, ISO auditors and government regulators will flag your operations.</p>

<h2 style="font-size:1.4rem;color:var(--white);margin:32px 0 16px">What Must Be Included?</h2>
<ul style="color:var(--text);line-height:1.8;margin-bottom:20px;padding-left:20px">
  <li style="margin-bottom:10px"><strong>Data Sanitization Standard:</strong> Explicitly naming NIST 800-88 or DoD 5220.22-M as your required standard.</li>
  <li style="margin-bottom:10px"><strong>Chain of Custody Tracking:</strong> How assets are securely transported from your premises to the recycling facility.</li>
  <li style="margin-bottom:10px"><strong>Vendor Selection:</strong> Mandating the vendor must be KSPCB authorized.</li>
  <li style="margin-bottom:10px"><strong>Documentation:</strong> Mandating the strict retention of Certificates of Destruction for all serial numbers.</li>
</ul>

<div style="background:rgba(0,232,122,.08);border:1px solid rgba(0,232,122,.2);border-radius:12px;padding:24px;margin:32px 0;text-align:center">
  <h3 style="font-size:1.2rem;color:var(--white);margin-bottom:12px">Need a Ready-To-Use Policy Template?</h3>
  <p style="font-size:.9rem;color:var(--text);margin-bottom:16px">We have drafted a comprehensive, DPDP-aligned Corporate ITAD Policy framework tailored for Kerala businesses.</p>
  <a href="https://wa.me/919876543210?text=Hi%2C+Please+send+the+Corporate+ITAD+Policy+Template" class="btn btn-wa" target="_blank">💬 Request Template via WhatsApp</a>
</div>
"""
cards_html += build_blog("corporate-e-waste-policy-template-india.html", "Corporate E-Waste Policy Template for DPDP Compliance", "📄", "Template", "Download the exact ITAD policy framework required to pass DPDP Act and ISO 27001 audits.", "green", "Resource", 4, b5_body)


# Now append the new cards to index.html
with open(index_file, "r") as f:
    index_html = f.read()

# We look for <div class="grid-3">\n
# and inject our new cards into it!
grid_marker = '<div class="grid-3">'
if grid_marker in index_html:
    parts = index_html.split(grid_marker, 1)
    new_index = parts[0] + grid_marker + "\n" + cards_html + parts[1]
    with open(index_file, "w") as f:
        f.write(new_index)
        print("Successfully generated 5 new blog posts and updated index.html")
else:
    print("Could not find <div class='grid-3'> in index.html")

