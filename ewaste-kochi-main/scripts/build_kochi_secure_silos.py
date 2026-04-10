import os
import shutil

src = "/media/hp-ml10/Projects/KochiSecureEwaste-VFINAL.html"
dest_dir = "/media/hp-ml10/Projects/EwasteKochi.com/KochiSecureBuild"

os.makedirs(dest_dir, exist_ok=True)
os.makedirs(os.path.join(dest_dir, "services"), exist_ok=True)

# 1. Establish the main Homepage
shutil.copy(src, os.path.join(dest_dir, "index.html"))

# 2. Read the master template
with open(src, "r") as f:
    html = f.read()

# 3. Define the sub-silo services
services = {
    "data-center-decommissioning-kochi": (
        "Data Center Decommissioning Kochi", 
        "Secure, end-to-end data center decommissioning in Kochi. Server removal, NIST 800-88 data destruction, and EPR compliant hardware recycling. Certificates of Destruction issued for every rack."
    ),
    "corporate-laptop-buyback-kochi": (
        "Corporate Laptop Buyback Kochi", 
        "Turn your old IT assets into capital. Highest 2026 market rates for bulk corporate laptop buyback in Ernakulam and Infopark. All devices subjected to military-grade data wiping."
    ),
    "ssd-secure-erasure-kochi": (
        "SSD Secure Erasure Kerala", 
        "Military-grade SSD secure erasure and physical shredding. Guaranteed 100% data destruction for solid state drives in Kochi, preventing complex chip-based forensic recovery."
    ),
    "hard-drive-degaussing-kochi": (
        "Hard Drive Degaussing Kochi", 
        "Magnetic degaussing services in Ernakulam. Destroy hard drive magnetic media instantly with our industrial degaussers, neutralizing data permanently before physical shredding."
    ),
    "it-asset-buyback-kochi": (
        "IT Asset Buyback Kerala", 
        "Complete IT Asset Buyback program. Monetize your retiring corporate IT infrastructure securely. Free hardware appraisal across Kochi, Aluva, and Infopark environments."
    ),
    "data-breach-prevention-consulting": (
        "Data Breach Prevention Consulting", 
        "Avoid ₹250 Cr DPDP Act penalties. Expert consulting on data disposition, ITAD security, and verifiable destruction audit trails for Kerala-based corporations and medical facilities."
    ),
    "server-recycling-kochi": (
        "Server Recycling Kochi", 
        "Secure corporate server recycling and disposal across Kerala. Certified processing, precious metal recovery, and a strict zero-landfill guarantee under E-Waste Rules 2022."
    ),
    "it-asset-inventory-audit": (
        "IT Asset Inventory & Audit", 
        "Comprehensive asset tagging and inventory audit services for corporates before destruction. Strict chain of custody verification mapped directly to your internal compliance sheets."
    )
}

old_h1 = '''<h1 class="hero-h1">
          Secure E‑Waste &amp;
          <span class="acc">Certified ITAD</span>
          Data Destruction — Kochi
        </h1>'''

old_p = '''<p class="hero-desc">Kerala's most trusted 24/7 certified IT asset disposal (ITAD) and e‑waste recycling facility in Thrippunithura, Kochi. NIST/DoD hard drive shredding · Secure data wiping · Certificate of Destruction every job · Free corporate bulk pickup. Serving Infopark, Kakkanad, Ernakulam &amp; all of Kerala.</p>'''

old_title = '''<title>Kochi Secure E‑Waste & Certified ITAD | 24/7 Data Destruction & Hard Drive Shredding | Thrippunithura Kochi 2026</title>'''

# 4. Generate the Service Pages programmatically
for slug, (title, desc) in services.items():
    new_h1 = f'<h1 class="hero-h1"><span class="acc">{title}</span></h1>'
    new_p = f'<p class="hero-desc">{desc}</p>'
    new_title = f'<title>{title} | Kochi Secure E-Waste ITAD</title>'
    
    page_html = html.replace(old_h1, new_h1)
    page_html = page_html.replace(old_p, new_p)
    page_html = page_html.replace(old_title, new_title)
    
    # Save the specific service page
    out_path = os.path.join(dest_dir, "services", f"{slug}.html")
    with open(out_path, "w") as out_f:
        out_f.write(page_html)

print("Successfully established Master Directory and generated 8 targeted Service Pages.")
