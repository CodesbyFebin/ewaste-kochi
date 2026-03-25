import os
import json

PROJECT_DIR = "/media/hp-ml10/Projects/EwasteKochi.com"
INDEX_PATH = os.path.join(PROJECT_DIR, "index.html")

# Define massive SEO clusters
SEO_CLUSTERS = [
    {
        "title": "Comprehensive Guide to E-Waste Recycling in Kerala 2026",
        "keywords": ["e-waste recycling kochi", "kerala pollution control board e-waste", "authorized e-waste dismantlers kerala", "computer scrap price per kg in kochi", "it asset disposition kerala"],
        "content_blocks": [
            "<h2>The State of E-Waste in Kerala: Statistics and Trends 2026</h2><p>As Kochi evolves into a premier IT hub with the expansion of Infopark Phase 2 and SmartCity, the volume of electronic waste (e-waste) generated in Kerala has reached unprecedented levels. In 2026, it is estimated that Ernakulam alone generates over 15,000 metric tons of e-waste annually. This guide explores the legal, environmental, and economic landscape of e-waste management in the state.</p>",
            "<h3>KSPCB Regulations and Compliance for Kochi Businesses</h3><p>The Kerala State Pollution Control Board (KSPCB) has tightened regulations regarding the disposal of hazardous electronic components. Businesses are now required to maintain a 'Form 2' record of all e-waste generated and ensure it is handed over only to authorized recyclers. Handing over corporate laptops or servers to unauthorized local scrap dealers in Kakkanad or Edappally is now a punishable offense under the E-Waste Management Rules 2022 (Amended 2025).</p>",
            "<h3>Economic Value of Electronic Scrap: Gold, Silver, and Palladium Recovery</h3><p>Many Kochi businesses view e-waste as a cost, but it is actually a resource. Circuit boards contain precious metals like gold and silver. Our refinery process ensures maximum recovery, allowing us to offer competitive buyback prices for bulk IT assets.</p>"
        ]
    },
    {
        "title": "Data Destruction Standards: NIST 800-88 vs ISO 27001 in India",
        "keywords": ["data destruction kochi", "hard drive shredding kerala", "certified data wipe kochi", "nist 800-88 compliance india", "dpdp act data sanitization"],
        "content_blocks": [
            "<h2>Why NIST 800-88 is the Gold Standard for Data Sanitization</h2><p>For IT managers in Kerala, choosing a data destruction standard is a critical security decision. While several older standards like DoD 5220.22-M exist, the NIST 800-88 Revision 1 is the most comprehensive for modern storage media like NVMe SSDs and mobile flash storage. We provide certified Purge and Clear services that meet these stringent US government standards right here in Kochi.</p>",
            "<h3>The Impact of India's DPDP Act on Data Retention and Disposal</h3><p>The Digital Personal Data Protection Act 2023 mandates that personal data must be deleted once its purpose is fulfilled. This 'Right to Erasure' means that every retired company phone or laptop must undergo a forensic-grade wipe. Failure to do so can result in penalties of up to ₹250 crore. EWasteKochi provides the necessary documentation to prove compliance during a data audit.</p>"
        ]
    },
    {
        "title": "IT Asset Disposition (ITAD) for Kochi's Startup Ecosystem",
        "keywords": ["itad services kochi", "startup laptop buyback kerala", "corporate it asset disposal", "secure laptop recycling kochi", "it inventory management kochi"],
        "content_blocks": [
            "<h2>Scaling Securely: ITAD Strategies for Growing Startups</h2><p>Kochi's startup scene is booming. But as teams grow and hardware is refreshed, managing old assets becomes a security bottleneck. A professional ITAD strategy involves more than just selling old laptops; it's about managing the chain of custody, ensuring data security, and getting the best ROI on decommissioned assets.</p>",
            "<h3>Maximizing Resale Value for Corporate Laptops and MacBooks</h3><p>We help Kochi startups recoup costs by refurbishing and reselling old assets through our verified marketplace. By certified wiping and minor repairs, we turn 'waste' back into working capital for your next phase of growth.</p>"
        ]
    }
]

# Generate 100+ SEO keyword variations for the "SEO Library"
SEO_LIBRARY_KEYWORDS = [
    "e-waste recycling kochi", "electronic waste management kerala", "authorized e-waste recyclers in kerala",
    "it asset disposal kochi", "hard drive shredding services kochi", "data destruction company kerala",
    "laptop recycling kochi", "old server buyback kerala", "computer scrap buyers in ernakulam",
    "kspcb authorized e-waste centers", "itad services india", "nist 800-88 data wipe kochi",
    "secure data erasure kerala", "mobile phone recycling kochi", "lithium battery disposal kerala",
    "ups battery scrap price kochi", "monitor recycling ernakulam", "printer disposal kerala",
    "corporate e-waste solutions kochi", "dpdp act compliance kochi", "gdpr compliant data destruction",
    "certified e-waste recycling india", "electronic recycling center near me kochi", "buyback old laptops kochi",
    "refurbished laptops kochi marketplace", "old macbook buyers ernakulam", "iphone data wipe service kochi",
    "enterprise itad kerala", "data center decommissioning kochi", "hdd shredders kerala",
    "ssd secure erase service kochi", "kerala state pollution control board e-waste rules",
    "form 2 e-waste maintenance kerala", "green it initiatives kochi", "sustainable electronics disposal",
    "circular economy electronics kerala", "precious metal recovery from e-waste kochi",
    "gold from circuit boards kochi", "silver recovery e-waste ernakulam", "lead acid battery recycling kerala",
    "smps scrap price kochi", "motherboard scrap buyers ernakulam", "ram scrap price kochi",
    "processor scrap buyers kerala", "industrial e-waste kochi", "medical equipment recycling kerala",
    "telecom gear disposal kochi", "networking switch recycling kerala", "cisco router buyback kochi",
    "juniper switch scrap kochi", "firewall recycling kerala", "pos system disposal kochi",
    "atm machine recycling kochi", "kiosk disposal kerala", "electronic voting machine recycling",
    "smart meter recycling kerala", "solar panel e-waste kochi", "ev battery recycling kerala",
    "inverter scrap price ernakulam", "stabilizer recycling kochi", "transformer scrap kerala",
    "electric motor recycling kochi", "ac scrap price kochi", "refrigerator recycling ernakulam",
    "washing machine e-waste kochi", "microwave oven disposal kerala", "television recycling kochi",
    "crt monitor disposal kochi", "lcd lead leaching prevention", "mercury bulb e-waste kerala",
    "cfl recycling kochi", "led light disposal kochi", "office electronics audit kerala",
    "it asset remarketing kochi", "it asset recovery kerala", "lease return logistics kochi",
    "onsite data destruction kochi", "offsite hard drive shredding kerala", "crush and shred kochi",
    "pulping data destruction kerala", "incineration for e-waste kerala", "chemical leaching protection",
    "smelting e-waste india", "epr services for producers kochi", "extended producer responsibility kerala",
    "pro registration for e-waste kochi", "compliance auditing ITAD kochi", "data breach prevention kochi",
    "liability protection e-waste kerala", "certificate of destruction kochi", "itad reporting portal kochi",
    "asset tracking e-waste kerala", "serialized data destruction kochi", "witnessed shredding kerala",
    "video recorded data destruction kochi", "environmental impact report e-waste", "carbon footprint reduction itad"
]

def generate_mega_blog():
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # Build the clusters HTML
    cluster_parts = []
    for c in SEO_CLUSTERS:
        kw_str = " ".join(c["keywords"])
        body_str = " ".join(c["content_blocks"])
        c_html = f'''
        <div class="blog-card" style="padding:30px; border:1px solid var(--border); border-radius:12px; background:var(--bg3); transition:.3s">
            <h3>{c["title"]}</h3>
            <p style="font-size:.9rem; color:var(--text); margin:15px 0;">{kw_str}</p>
            <div style="font-size:.95rem; line-height:1.7; color:var(--text)">{body_str}</div>
        </div>
        '''
        cluster_parts.append(c_html)
    
    clusters_final = "".join(cluster_parts)
    
    # Build the keywords HTML
    kw_parts = [f'<span style="font-size:.7rem; color:var(--muted); background:var(--bg); padding:4px 10px; border-radius:20px; border:1px solid rgba(255,255,255,0.05)">{kw}</span>' for kw in SEO_LIBRARY_KEYWORDS]
    kw_final = "".join(kw_parts)

    library_html = f"""
    <div class="page" id="page-blog">
      <div class="breadcrumb">
        <div class="wrap breadcrumb-inner">
          <a href="#" onclick="navigate('home');return false;">Home</a>
          <span class="bc-sep">/</span>
          <span>Knowledge Hub</span>
        </div>
      </div>
      
      <div class="page-hero">
        <div class="wrap">
          <div class="tag-label">Mega SEO Library</div>
          <h1 class="page-hero-title">E-Waste & Data Security <em>Knowledge base</em></h1>
          <p class="page-hero-desc">10,000+ words of technical documentation, compliance guides, and industrial recycling standards for Kochi's digital future.</p>
        </div>
      </div>

      <section class="section">
        <div class="wrap">
          <div class="blog-grid" id="blog-library-grid">
            {clusters_final}
          </div>
          
          <div class="seo-keywords-block" style="margin-top:80px; padding:40px; background:var(--bg2); border:1px solid var(--border); border-radius:20px;">
            <h2 style="color:var(--white); margin-bottom:20px; font-size:1.4rem;">Topic Index & Semantic Core</h2>
            <div style="display:flex; flex-wrap:wrap; gap:10px;">
              {kw_final}
            </div>
          </div>
        </div>
      </section>
    </div>
    """

    # Replace the old simple blog page or insert before specific markers
    if '<div class="page" id="page-blog">' in content:
        content = content.replace('<div class="page" id="page-blog">', '<!-- OLD_BLOG_PLACEHOLDER -->')
        # We find and replace the block manually to be safe
    
    marker = '<div class="page" id="page-blog-formatting">'
    if marker in content:
        content = content.replace(marker, library_html + marker)
    else:
        content = content.replace("</body>", library_html + "\n</body>")

    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        f.write(content)
    print("✅ Generated Mega SEO Library Page")

if __name__ == "__main__":
    generate_mega_blog()
