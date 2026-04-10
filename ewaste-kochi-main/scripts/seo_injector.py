import os

# Config
PROJECT_DIR = "/media/hp-ml10/Projects/EwasteKochi.com"
CORE_FILES = ["index.html", "services.html", "data-destruction-kochi.html", "itad-kochi.html", "buyback/bulk-laptop-buyback.html"]

# ── 1. COMPONENTS (Expanded for 8000+ keywords) ──
ACTIONS = ["Sell", "Recycle", "Dispose", "Buyback", "Pickup", "Discard", "Expert", "Authorized", "Certified", "Bulk", "Best Price", "Cash for", "Secure", "NIST", "KSPCB"]
DEVICES = ["Laptop", "MacBook", "iPhone", "Server", "Hard Drive", "SSD", "Computer Scrap", "E-Waste", "Monitor", "Printer", "IT Asset", "Motherboard", "Workstation", "UPS", "Battery", "Network Switch"]
LOCATIONS = [
    "Kochi", "Ernakulam", "Kakkanad", "Edappally", "Vyttila", "Aluva", "Angamaly", "Thrippunithura", "Palarivattom", "Kaloor", 
    "LULU", "Infopark", "SmartCity", "MG Road", "Marine Drive", "Fort Kochi", "Mattancherry", "Kalamassery", "Eloor", "North Paravur",
    "Perumbavoor", "Muvattupuzha", "Kothamangalam", "Kolenchery", "Maradu", "Nettoor", "Cheranallur", "Ambalamukku", "Ravipuram", "Panampilly Nagar"
]
PINCODES = [f"682{i:03}" for i in range(1, 101)] # 100 pincodes

def generate_keywords():
    keywords = []
    # Generation Matrix
    for a in ACTIONS:
        for d in DEVICES:
            for l in LOCATIONS:
                keywords.append(f"{a} {d} {l}")
    
    for d in DEVICES:
        for l in LOCATIONS:
            for p in PINCODES:
                keywords.append(f"{d} {l} {p}")
                
    NICHE = [
        "NIST 800-88 Data Shredding", "DoD 5220.22-M Wipe", "DPDP Act 2023 compliance", 
        "Certified ITAD Kerala", "KSPCB Authorized Recycler", "Forensic Data Sanitization",
        "Environmental Waste Audit", "Certificate of Destruction Kochi", "Asset Lifecycle Management",
        "Sustainable Corporate Recycling", "Bank IT asset disposal", "Hospital E-waste collection"
    ]
    for n in NICHE:
        for l in LOCATIONS:
            keywords.append(f"{n} {l}")
            
    unique_keywords = sorted(list(set(keywords)))
    return unique_keywords

def inject_to_file(filepath):
    if not os.path.exists(filepath):
        print(f"⚠️ File not found: {filepath}")
        return
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Remove old index if exists
    start_idx = content.find("<!-- SEO_INDEX_START -->")
    end_idx = content.find("<!-- SEO_INDEX_END -->")
    if start_idx != -1 and end_idx != -1:
        cleaned_content = content[:start_idx] + content[end_idx+len("<!-- SEO_INDEX_END -->"):]
    else:
        cleaned_content = content
    
    # Trim ending tags to append
    body_pos = cleaned_content.find("</body>")
    if body_pos != -1:
        base_content = cleaned_content[:body_pos]
    else:
        base_content = cleaned_content
        
    keywords = generate_keywords()
    
    seo_block = f"""
<!-- SEO_INDEX_START -->
<section style="background:#07100A;padding:40px 0;border-top:1px solid rgba(0,232,122,.15);opacity:0.8;font-size:9px">
  <div class="wrap" style="max-width:1200px;margin:0 auto;padding:0 24px;color:#A8C4AE;line-height:2.2;text-align:justify">
    <h6 style="color:#F0F7F2;font-family:monospace;font-size:10px;text-transform:uppercase;letter-spacing:1px;margin-bottom:12px">SEO POWERHOUSE: Search Engine Service & Coverage Index ({len(keywords):,} Semantic Clusters)</h6>
    <div style="max-height:150px;overflow-y:auto;border:1px solid rgba(0,232,122,.08);padding:10px;border-radius:10px;scrollbar-width:thin">
"""
    seo_block += ", ".join(keywords)
    seo_block += """
    </div>
    <div style="margin-top:12px;font-family:monospace;font-size:8px">Last updated: March 2026. Certified ITAD, Data Destruction, and E-Waste Recycling in Kerala. Powered by EWasteKochi.com SEO Engine.</div>
  </div>
</section>
<!-- SEO_INDEX_END -->
"""
    
    final_content = base_content + seo_block + "\n</body>\n</html>"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(final_content)
    print(f"✅ SEO Powerhouse injected into {os.path.basename(filepath)}")

if __name__ == "__main__":
    for f in CORE_FILES:
        inject_to_file(os.path.join(PROJECT_DIR, f))
