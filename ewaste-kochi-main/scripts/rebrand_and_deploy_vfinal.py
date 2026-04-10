import os
import shutil

src = "/media/hp-ml10/Projects/KochiSecureEwaste-VFINAL.html"
dest_dir = "/media/hp-ml10/Projects/EwasteKochi.com"

# Clean up the previous KochiSecureBuild mistake
old_build = os.path.join(dest_dir, "KochiSecureBuild")
if os.path.exists(old_build):
    shutil.rmtree(old_build)

os.makedirs(os.path.join(dest_dir, "services"), exist_ok=True)

# Read the Dark Mode master template
with open(src, "r") as f:
    html = f.read()

# PERFECT BRANDING REPLACEMENT -> Mapping back to EWasteKochi.com
replacements = {
    "Kochi Secure E‑Waste": "EWasteKochi",
    "Kochi Secure E-Waste": "EWasteKochi",
    "Kochi ITAD": "EWasteKochi ITAD",
    "kochisecureewaste.in": "ewastekochi.com",
    "+91-XXXXXXXXXX": "+91-7500555454",
    "+91 XXXXX XXXXX": "+91 75005 55454",
    "91XXXXXXXXXX": "917500555454",
    "info@kochisecureewaste.in": "info@ewastekochi.com",
    "Dr Shield ITAD Kerala": "EWasteKochi ITAD Kerala"
}

for old_str, new_str in replacements.items():
    html = html.replace(old_str, new_str)

# Write the new Master Homepage
with open(os.path.join(dest_dir, "index.html"), "w") as f:
    f.write(html)

# Sub-silos definitions
services = {
    "data-center-decommissioning-kochi": ("Data Center Decommissioning Kochi", "Secure, end-to-end data center decommissioning in Kochi. Server removal, NIST 800-88 data destruction, and EPR compliant hardware recycling."),
    "corporate-laptop-buyback-kochi": ("Corporate Laptop Buyback Kochi", "Turn your old IT assets into capital. Highest 2026 market rates for bulk corporate laptop buyback in Ernakulam and Infopark."),
    "ssd-secure-erasure-kochi": ("SSD Secure Erasure Kerala", "Military-grade SSD secure erasure and physical shredding. Guaranteed 100% data destruction for solid state drives in Kochi."),
    "hard-drive-degaussing-kochi": ("Hard Drive Degaussing Kochi", "Magnetic degaussing services in Ernakulam. Destroy hard drive magnetic media instantly with our industrial degaussers."),
    "it-asset-buyback-kochi": ("IT Asset Buyback Kerala", "Complete IT Asset Buyback program. Monetize your retiring corporate IT infrastructure securely with E-Waste Rules 2022 compliance."),
    "data-breach-prevention-consulting": ("Data Breach Prevention Consulting", "Avoid ₹250 Cr DPDP Act penalties. Expert consulting on data disposition, ITAD security, and verifiable destruction audit trails."),
    "server-recycling-kochi": ("Server Recycling Kochi", "Secure corporate server recycling and disposal across Kerala. Certified processing, precious metal recovery, and a strict zero-landfill guarantee."),
    "it-asset-inventory-audit": ("IT Asset Inventory & Audit", "Comprehensive asset tagging and inventory audit services for corporates before destruction. Chain of custody verification assured.")
}

# The base tags we are stripping from the template
old_h1 = '''<h1 class="hero-h1">
          Secure E‑Waste &amp;
          <span class="acc">Certified ITAD</span>
          Data Destruction — Kochi
        </h1>'''

old_p = '''<p class="hero-desc">Kerala's most trusted 24/7 certified IT asset disposal (ITAD) and e‑waste recycling facility in Thrippunithura, Kochi. NIST/DoD hard drive shredding · Secure data wiping · Certificate of Destruction every job · Free corporate bulk pickup. Serving Infopark, Kakkanad, Ernakulam &amp; all of Kerala.</p>'''

old_title = '''<title>EWasteKochi & Certified ITAD | 24/7 Data Destruction & Hard Drive Shredding | Thrippunithura Kochi 2026</title>'''

# Generate the 8 unique Service Pages with EWasteKochi branding
for slug, (title, desc) in services.items():
    new_h1 = f'<h1 class="hero-h1"><span class="acc">{title}</span></h1>'
    new_p = f'<p class="hero-desc">{desc}</p>'
    new_title = f'<title>{title} | EWasteKochi ITAD</title>'
    
    page_html = html.replace(old_h1, new_h1)
    page_html = page_html.replace(old_p, new_p)
    page_html = page_html.replace(old_title, new_title)
    
    with open(os.path.join(dest_dir, "services", f"{slug}.html"), "w") as out_f:
        out_f.write(page_html)

print("Successfully replaced branding with EWasteKochi.com and generated 1 Root + 8 Service Silos.")
