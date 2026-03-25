#!/usr/bin/env python3
"""
Generate comprehensive sitemap.xml covering:
- All existing ewastekochi.com pages (from sitemap doc)
- All 1200+ newly generated pages
- Sitemap index for pages > 50,000 URLs
"""
import os
from datetime import date
from pathlib import Path

TODAY = date.today().isoformat()
SITE = "https://ewastekochi.com"
BASE = "/home/claude/ewaste-gen/output"

PRIORITY_MAP = {
    "/": "1.0",
    "/data-destruction-kochi": "1.0",
    "/contact": "0.9",
    "/about": "0.8",
    "/services": "0.9",
}

SECTION_PRIORITY = {
    "locations": "0.9",
    "data-security": "0.9",
    "itad": "0.9",
    "recycling": "0.85",
    "collection": "0.85",
    "disposal": "0.80",
    "trading": "0.80",
    "buyback": "0.80",
    "services": "0.85",
    "industries": "0.75",
    "comparisons": "0.70",
    "compliance": "0.80",
    "guides": "0.75",
    "proof": "0.70",
    "general-waste": "0.65",
}

FREQ_MAP = {
    "_root": "daily",
    "locations": "weekly",
    "data-security": "weekly",
    "collection": "weekly",
    "recycling": "weekly",
    "disposal": "weekly",
    "trading": "weekly",
    "buyback": "weekly",
    "services": "weekly",
    "industries": "monthly",
    "comparisons": "monthly",
    "compliance": "monthly",
    "guides": "monthly",
    "general-waste": "monthly",
    "itad": "weekly",
}

def get_priority(url):
    path = url.replace(SITE, "")
    if path in PRIORITY_MAP:
        return PRIORITY_MAP[path]
    parts = path.strip("/").split("/")
    sec = parts[0] if parts else ""
    return SECTION_PRIORITY.get(sec, "0.65")

def get_freq(url):
    path = url.replace(SITE, "")
    if path in ("", "/"):
        return "daily"
    parts = path.strip("/").split("/")
    sec = parts[0] if parts else ""
    return FREQ_MAP.get(sec, "monthly")

# Collect existing URLs from the sitemap doc (doc3)
EXISTING_URLS = """https://ewastekochi.com/
https://ewastekochi.com/data-destruction-kochi
https://ewastekochi.com/contact
https://ewastekochi.com/about
https://ewastekochi.com/services
https://ewastekochi.com/data-security/banks-data-destruction
https://ewastekochi.com/data-security/business-it-decommissioning-services
https://ewastekochi.com/data-security/certificate-of-destruction
https://ewastekochi.com/data-security/certified-it-asset-destruction
https://ewastekochi.com/data-security/corporate-data-policy-ewaste-kerala
https://ewastekochi.com/data-security/corporate-data-security-compliance-kochi
https://ewastekochi.com/data-security/corporate-itad-checklist
https://ewastekochi.com/data-security/corporate-itad-quote
https://ewastekochi.com/data-security/data-breach-costs-india
https://ewastekochi.com/data-security/data-breach-prevention-consulting
https://ewastekochi.com/data-security/data-center-decommissioning-kochi
https://ewastekochi.com/data-security/data-center-decommissioning-steps
https://ewastekochi.com/data-security/data-destruction-complete-guide
https://ewastekochi.com/data-security/data-destruction-compliance-audit
https://ewastekochi.com/data-security/data-destruction-degaussing-kochi
https://ewastekochi.com/data-security/data-secure-it-recycling
https://ewastekochi.com/data-security/data-wiping-software-vs-shredding
https://ewastekochi.com/data-security/data-wiping-vs-physical-destruction
https://ewastekochi.com/data-security/data-wiping-vs-shredding
https://ewastekochi.com/data-security/dpdp-act-2023-it-disposal-kerala
https://ewastekochi.com/data-security/dpdp-act-impact-on-startups-kochi
https://ewastekochi.com/data-security/dpdp-act-penalties-explained
https://ewastekochi.com/data-security/dpdp-compliance
https://ewastekochi.com/data-security/dpdp-vs-gdpr-data-destruction
https://ewastekochi.com/data-security/e-waste-destruction
https://ewastekochi.com/data-security/e-waste-security
https://ewastekochi.com/data-security/flash-drive-usb-destruction-kochi
https://ewastekochi.com/data-security/gdpr-dpdp-act-compliance-ewaste-kochi
https://ewastekochi.com/data-security/government-itad
https://ewastekochi.com/data-security/hard-disk-data-recovery-risk
https://ewastekochi.com/data-security/hard-drive-destruction-service
https://ewastekochi.com/data-security/hard-drive-shredding
https://ewastekochi.com/data-security/hard-drive-shredding-company
https://ewastekochi.com/data-security/hard-drive-shredding-cost-kochi
https://ewastekochi.com/data-security/hard-drive-shredding-destruction-kochi
https://ewastekochi.com/data-security/hard-drive-shredding-kerala
https://ewastekochi.com/data-security/hard-drive-shredding-kochi
https://ewastekochi.com/data-security/hard-drive-shredding-service-kochi
https://ewastekochi.com/data-security/hard-drive-shredding-vs-degaussing
https://ewastekochi.com/data-security/how-to-choose-itad-provider
https://ewastekochi.com/data-security/india-dpdp-act-data-privacy-act-data-protection-act-compliance
https://ewastekochi.com/data-security/is-formatting-enough-data-delete
https://ewastekochi.com/data-security/iso-27001-certified-data-sanitization-kochi
https://ewastekochi.com/data-security/itad
https://ewastekochi.com/data-security/itad-companies-in-india
https://ewastekochi.com/data-security/itad-complete-guide-kochi
https://ewastekochi.com/data-security/itad-kakkanad
https://ewastekochi.com/data-security/itad-kochi
https://ewastekochi.com/data-security/itad-kochi-complete-guide
https://ewastekochi.com/data-security/itad-service-kochi-2026
https://ewastekochi.com/data-security/itad-vs-ewaste-recycling
https://ewastekochi.com/data-security/magnetic-media-degaussing-kochi
https://ewastekochi.com/data-security/mobile-device-data-erasure-kochi
https://ewastekochi.com/data-security/nist-800-88-data-wiping
https://ewastekochi.com/data-security/nist-data-wipe-kerala
https://ewastekochi.com/data-security/on-site-data-destruction-infopark
https://ewastekochi.com/data-security/phone-data-recovery-risk
https://ewastekochi.com/data-security/r2-certified-recycling-kochi
https://ewastekochi.com/data-security/secure-chain-of-custody-documentation-kochi
https://ewastekochi.com/data-security/secure-computer-disposal
https://ewastekochi.com/data-security/secure-computer-recycling
https://ewastekochi.com/data-security/secure-data-destruction-methods
https://ewastekochi.com/data-security/secure-disposal-of-computers
https://ewastekochi.com/data-security/secure-e-waste-destruction
https://ewastekochi.com/data-security/secure-e-waste-recycling
https://ewastekochi.com/data-security/secure-electronic-disposal
https://ewastekochi.com/data-security/secure-laptop-disposal
https://ewastekochi.com/data-security/secure-phone-disposal
https://ewastekochi.com/data-security/secure-server-decommissioning
https://ewastekochi.com/data-security/secure-waste-disposal
https://ewastekochi.com/data-security/server-data-center-decommissioning
https://ewastekochi.com/data-security/ssd-destruction-kochi
https://ewastekochi.com/data-security/ssd-destruction-service
https://ewastekochi.com/data-security/ssd-erasure-vs-physical-destruction
https://ewastekochi.com/data-security/ssd-secure-erasure-kochi
https://ewastekochi.com/data-security/tape-media-destruction-kochi
https://ewastekochi.com/data-security/what-is-a-certificate-of-destruction
https://ewastekochi.com/data-security/what-is-itad
https://ewastekochi.com/data-security/why-companies-need-certificate-of-destruction
https://ewastekochi.com/itad/index
https://ewastekochi.com/itad/itad-asset_disposal-kochi
https://ewastekochi.com/itad/itad-certificate_of_destruction-kochi
https://ewastekochi.com/itad/itad-data_destruction-kochi
https://ewastekochi.com/itad/itad-hard_drive_shredding-kochi
https://ewastekochi.com/itad/itad-itad-kochi
https://ewastekochi.com/itad/itad-laptop_buyback-kochi
https://ewastekochi.com/itad/itad-server_decommissioning-kochi
https://ewastekochi.com/itad/services/sell-server-racks-kochi
https://ewastekochi.com/itad/services/sell-ups-batteries-kochi
https://ewastekochi.com/locations/aluva-ewaste-kochi
https://ewastekochi.com/locations/edappally-ewaste-kochi
https://ewastekochi.com/locations/ewaste-aluva
https://ewastekochi.com/locations/ewaste-angamaly
https://ewastekochi.com/locations/ewaste-aroor
https://ewastekochi.com/locations/ewaste-cherai
https://ewastekochi.com/locations/ewaste-edappally
https://ewastekochi.com/locations/ewaste-ernakulam
https://ewastekochi.com/locations/ewaste-fort-kochi
https://ewastekochi.com/locations/ewaste-infopark
https://ewastekochi.com/locations/ewaste-kakkanad
https://ewastekochi.com/locations/ewaste-kalamassery
https://ewastekochi.com/locations/ewaste-kaloor
https://ewastekochi.com/locations/ewaste-kochi
https://ewastekochi.com/locations/ewaste-kothamangalam
https://ewastekochi.com/locations/ewaste-marine-drive
https://ewastekochi.com/locations/ewaste-mattancherry
https://ewastekochi.com/locations/ewaste-mg-road
https://ewastekochi.com/locations/ewaste-moovattupuzha
https://ewastekochi.com/locations/ewaste-muvattupuzha
https://ewastekochi.com/locations/ewaste-north-paravur
https://ewastekochi.com/locations/ewaste-palarivattom
https://ewastekochi.com/locations/ewaste-panampilly-nagar
https://ewastekochi.com/locations/ewaste-perumbavoor
https://ewastekochi.com/locations/ewaste-piravom
https://ewastekochi.com/locations/ewaste-smart-city
https://ewastekochi.com/locations/ewaste-thevara
https://ewastekochi.com/locations/ewaste-thrippunithura
https://ewastekochi.com/locations/ewaste-tripunithura
https://ewastekochi.com/locations/ewaste-vyttila
https://ewastekochi.com/locations/index
https://ewastekochi.com/locations/infopark-ewaste-kochi
https://ewastekochi.com/locations/kakkanad-ewaste-kochi
https://ewastekochi.com/locations/marine-drive-ewaste-kochi
https://ewastekochi.com/locations/panampilly-nagar-ewaste-kochi
https://ewastekochi.com/locations/thrippunithura-ewaste-kochi
https://ewastekochi.com/locations/vyttila-ewaste-kochi
https://ewastekochi.com/buyback/bulk-laptop-buyback
https://ewastekochi.com/buyback/bulk-laptop-buyback-kochi
https://ewastekochi.com/buyback/laptops/sell-dell-xps-13-kochi
https://ewastekochi.com/buyback/laptops/sell-dell-xps-15-kochi
https://ewastekochi.com/buyback/laptops/sell-dell-xps-17-kochi
https://ewastekochi.com/buyback/laptops/sell-hp-spectre-x360-kochi
https://ewastekochi.com/buyback/laptops/sell-lenovo-thinkpad-x1-carbon-kochi
https://ewastekochi.com/buyback/laptops/sell-macbook-air-m1-kochi
https://ewastekochi.com/buyback/laptops/sell-macbook-air-m2-kochi
https://ewastekochi.com/buyback/laptops/sell-macbook-air-m3-kochi
https://ewastekochi.com/buyback/laptops/sell-macbook-air-m4-kochi
https://ewastekochi.com/buyback/laptops/sell-macbook-pro-13-kochi
https://ewastekochi.com/buyback/laptops/sell-macbook-pro-14-kochi
https://ewastekochi.com/buyback/laptops/sell-macbook-pro-15-kochi
https://ewastekochi.com/buyback/laptops/sell-macbook-pro-m2-kochi
https://ewastekochi.com/buyback/laptops/sell-macbook-pro-m3-kochi
https://ewastekochi.com/buyback/laptops/sell-macbook-pro-m3-max-kochi
https://ewastekochi.com/buyback/laptops/sell-macbook-pro-m3-pro-kochi
https://ewastekochi.com/buyback/laptops/sell-thinkpad-x1-carbon-gen-12-kochi
https://ewastekochi.com/buyback/office-it-clearance-kochi
https://ewastekochi.com/buyback/phones/sell-google-pixel-8-kochi
https://ewastekochi.com/buyback/phones/sell-google-pixel-8-pro-kochi
https://ewastekochi.com/buyback/phones/sell-google-pixel-9-pro-kochi
https://ewastekochi.com/buyback/phones/sell-iphone-14-kochi
https://ewastekochi.com/buyback/phones/sell-iphone-14-plus-kochi
https://ewastekochi.com/buyback/phones/sell-iphone-14-pro-kochi
https://ewastekochi.com/buyback/phones/sell-iphone-14-pro-max-kochi
https://ewastekochi.com/buyback/phones/sell-iphone-15-kochi
https://ewastekochi.com/buyback/phones/sell-iphone-15-pro-kochi
https://ewastekochi.com/buyback/phones/sell-iphone-15-pro-max-kochi
https://ewastekochi.com/buyback/phones/sell-samsung-s23-ultra-kochi
https://ewastekochi.com/buyback/phones/sell-samsung-s24+-kochi
https://ewastekochi.com/buyback/phones/sell-samsung-s24-kochi
https://ewastekochi.com/buyback/phones/sell-samsung-s24-ultra-kochi
https://ewastekochi.com/buyback/sell-broken-laptop-kochi
https://ewastekochi.com/buyback/sell-dead-iphone-kochi
https://ewastekochi.com/buyback/sell-iphone-kochi
https://ewastekochi.com/buyback/sell-macbook-kochi
https://ewastekochi.com/buyback/sell-old-desktop-kochi
https://ewastekochi.com/buyback/sell-old-laptop-kochi
https://ewastekochi.com/buyback/sell-samsung-galaxy-kochi
https://ewastekochi.com/buyback/sell-water-damaged-macbook-kochi
https://ewastekochi.com/collection/apartment-complex-ewaste-kochi
https://ewastekochi.com/collection/b2b-e-waste-collection-contracts
https://ewastekochi.com/collection/book-free-pickup
https://ewastekochi.com/collection/book-free-pickup-kochi
https://ewastekochi.com/collection/bulk-ac-disposal-kochi
https://ewastekochi.com/collection/corporate-e-waste-management-programs
https://ewastekochi.com/collection/e-waste-collection-aluva
https://ewastekochi.com/collection/e-waste-collection-kochi
https://ewastekochi.com/collection/e-waste-collection-near-me
https://ewastekochi.com/collection/e-waste-management-kochi-complete-guide
https://ewastekochi.com/collection/e-waste-management-rules-2022-guide
https://ewastekochi.com/collection/e-waste-pickup-infopark
https://ewastekochi.com/collection/e-waste-pickup-kakkanad
https://ewastekochi.com/collection/event-ewaste-management-kochi
https://ewastekochi.com/collection/ewaste-pickup
https://ewastekochi.com/collection/ewaste-pickup-kochi
https://ewastekochi.com/collection/free-e-waste-pickup-kochi
https://ewastekochi.com/collection/free-ewaste-pickup-kochi
https://ewastekochi.com/collection/mall-kiosk-ewaste-collection
https://ewastekochi.com/collection/medical-equipment-e-waste-management
https://ewastekochi.com/collection/office-ewaste-pickup
https://ewastekochi.com/collection/schools-ewaste-collection-drive
https://ewastekochi.com/disposal/banking-finance-sector-it-disposal
https://ewastekochi.com/disposal/computer-disposal-kochi
https://ewastekochi.com/disposal/e-waste-disposal-near-me
https://ewastekochi.com/disposal/electronic-waste-disposal-near-me
https://ewastekochi.com/disposal/ewaste-disposal
https://ewastekochi.com/disposal/hard-drive-disposal
https://ewastekochi.com/disposal/hospital-medical-equipment-disposal
https://ewastekochi.com/disposal/how-companies-dispose-it-assets-india
https://ewastekochi.com/disposal/it-asset-disposal-kochi
https://ewastekochi.com/disposal/it-disposal-services
https://ewastekochi.com/disposal/it-equipment-disposal
https://ewastekochi.com/disposal/laptop-disposal-kochi
https://ewastekochi.com/disposal/server-disposal-kochi
https://ewastekochi.com/disposal/ups-battery-disposal-services
https://ewastekochi.com/disposal/waste-disposal-kochi
https://ewastekochi.com/recycling/ac-recycle
https://ewastekochi.com/recycling/atm-machine-recycling-kochi
https://ewastekochi.com/recycling/battery-recycling
https://ewastekochi.com/recycling/battery-recycling-kochi
https://ewastekochi.com/recycling/bulk-electronics-recycling
https://ewastekochi.com/recycling/computer-laptop-recycling-guide
https://ewastekochi.com/recycling/corporate-electronics-recycling-program
https://ewastekochi.com/recycling/drone-recycling-kochi
https://ewastekochi.com/recycling/e-waste-recycling-centers
https://ewastekochi.com/recycling/e-waste-recycling-kochi
https://ewastekochi.com/recycling/e-waste-recycling-near-me
https://ewastekochi.com/recycling/electronics-recycling-near-me
https://ewastekochi.com/recycling/environmental-benefits-e-waste-recycling
https://ewastekochi.com/recycling/epr-extended-producer-responsibility-compliance
https://ewastekochi.com/recycling/esg-reporting-e-waste-metrics
https://ewastekochi.com/recycling/ewaste-recycling
https://ewastekochi.com/recycling/ewaste-recycling-ernakulam
https://ewastekochi.com/recycling/ewaste-recycling-guidelines-kerala-2026
https://ewastekochi.com/recycling/ewaste-recycling-kochi
https://ewastekochi.com/recycling/ewaste-recycling-near-me
https://ewastekochi.com/recycling/gaming-console-recycling-kochi
https://ewastekochi.com/recycling/how-ewaste-is-recycled
https://ewastekochi.com/recycling/how-to-recycle-electronics
https://ewastekochi.com/recycling/it-hardware-asset-recovery
https://ewastekochi.com/recycling/kerala-pollution-control-board-regulations
https://ewastekochi.com/recycling/laptop-recycling-kerala
https://ewastekochi.com/recycling/laptop-recycling-kochi
https://ewastekochi.com/recycling/led-bulb-recycling-kochi
https://ewastekochi.com/recycling/mobile-phone-smartphone-recycling
https://ewastekochi.com/recycling/mobile-recycling-kochi
https://ewastekochi.com/recycling/precious-metal-recovery-e-waste
https://ewastekochi.com/recycling/server-rack-removal-kochi
https://ewastekochi.com/recycling/server-recycling-kochi
https://ewastekochi.com/recycling/solar-panel-recycling-kerala
https://ewastekochi.com/recycling/telecom-equipment-recycling
https://ewastekochi.com/recycling/telecom-tower-equipment-recycling
https://ewastekochi.com/recycling/wearable-device-recycling-kochi
https://ewastekochi.com/recycling/what-happens-to-recycled-ewaste
https://ewastekochi.com/recycling/where-to-donate-electronics
https://ewastekochi.com/recycling/where-to-recycle-batteries
https://ewastekochi.com/recycling/where-to-recycle-old-electronics
https://ewastekochi.com/services/corporate-laptop-buyback-kochi
https://ewastekochi.com/services/data-breach-prevention-consulting
https://ewastekochi.com/services/data-center-decommissioning-kochi
https://ewastekochi.com/services/hard-drive-degaussing-kochi
https://ewastekochi.com/services/it-asset-buyback-kochi
https://ewastekochi.com/services/it-asset-inventory-audit
https://ewastekochi.com/services/server-recycling-kochi
https://ewastekochi.com/services/ssd-secure-erasure-kochi
https://ewastekochi.com/trading/authorized-recycler-vs-scrap-dealer-kochi
https://ewastekochi.com/trading/best-place-to-sell-used-electronics
https://ewastekochi.com/trading/bulk-computer-scrap-buyers-kerala
https://ewastekochi.com/trading/bulk-laptop-buyback
https://ewastekochi.com/trading/cashify-kochi-alternative
https://ewastekochi.com/trading/computer-scrap-kochi
https://ewastekochi.com/trading/corporate-it-buyback-program
https://ewastekochi.com/trading/corporate-laptop-buyback-kochi
https://ewastekochi.com/trading/corporate-monitor-buyback-kochi
https://ewastekochi.com/trading/e-waste-buyers-near-me
https://ewastekochi.com/trading/electronics-scrap-kochi
https://ewastekochi.com/trading/iphone-buyback-kochi
https://ewastekochi.com/trading/it-asset-buyback-kochi
https://ewastekochi.com/trading/laptop-buyback-kochi
https://ewastekochi.com/trading/macbook-buyback-kochi
https://ewastekochi.com/trading/old-server-buyer
https://ewastekochi.com/trading/olx-alternative-kochi
https://ewastekochi.com/trading/samsung-buyback-kochi
https://ewastekochi.com/trading/sell-broken-macbook-kochi
https://ewastekochi.com/trading/sell-dead-laptop-for-parts
https://ewastekochi.com/trading/sell-electronic-waste
https://ewastekochi.com/trading/sell-macbook-pro-kochi-cash
https://ewastekochi.com/trading/sell-old-cisco-networking-kochi
https://ewastekochi.com/trading/sell-old-desktop-kochi
https://ewastekochi.com/trading/sell-old-electronics-near-me
https://ewastekochi.com/trading/sell-old-ipad-kochi
https://ewastekochi.com/trading/sell-old-laptop-kochi
https://ewastekochi.com/trading/sell-old-phone-kochi
https://ewastekochi.com/trading/sell-old-server-rack-kochi
https://ewastekochi.com/trading/sell-used-servers-kochi
https://ewastekochi.com/trading/tablet-buyback-kochi
https://ewastekochi.com/trading/where-to-sell-electronics-locally
https://ewastekochi.com/trading/where-to-sell-old-phone-kochi
https://ewastekochi.com/comparisons/cashify-vs-ewastekochi
https://ewastekochi.com/comparisons/local-vs-certified-recycling
https://ewastekochi.com/comparisons/olx-vs-ewastekochi
https://ewastekochi.com/comparisons/scrap-dealers-vs-certified-recycling
https://ewastekochi.com/compliance/brsr-ewaste-disclosure-kochi
https://ewastekochi.com/compliance/certificate-verification
https://ewastekochi.com/compliance/chain-of-custody
https://ewastekochi.com/compliance/dpdp-act-2023-ewaste-penalties
https://ewastekochi.com/compliance/epr-framework-india
https://ewastekochi.com/compliance/how-to-get-itad-certificate
https://ewastekochi.com/compliance/iso-14001-ewaste-kochi
https://ewastekochi.com/compliance/iso-27001-compliance
https://ewastekochi.com/compliance/kerala-pcb-authorization
https://ewastekochi.com/compliance/nist-800-88-explained
https://ewastekochi.com/compliance/sebi-brsr-ewaste-kochi
https://ewastekochi.com/guides/dpdp-act-ewaste-compliance-checklist
https://ewastekochi.com/guides/ewaste-audit-checklist-kerala-2026
https://ewastekochi.com/guides/ewaste-carbon-footprint-calculator
https://ewastekochi.com/guides/ewaste-management-rules-2022-guide
https://ewastekochi.com/guides/how-to-choose-ewaste-recycler-kochi
https://ewastekochi.com/guides/r2v3-certification-guide-india
https://ewastekochi.com/industries/banks-financial-data-destruction
https://ewastekochi.com/industries/ca-firm-ewaste-kochi
https://ewastekochi.com/industries/fintech-data-destruction-kochi
https://ewastekochi.com/industries/government-itad-kochi
https://ewastekochi.com/industries/hospitality-ewaste-kochi
https://ewastekochi.com/industries/hospitals-medical-ewaste
https://ewastekochi.com/industries/it-companies-kochi
https://ewastekochi.com/industries/legal-firm-data-destruction-kochi
https://ewastekochi.com/industries/logistics-fleet-ewaste-kochi
https://ewastekochi.com/industries/manufacturing-ewaste
https://ewastekochi.com/industries/pharma-ewaste-kochi
https://ewastekochi.com/industries/schools-education-ewaste
https://ewastekochi.com/industries/startup-ewaste-programme-kochi
https://ewastekochi.com/industries/startups-itad-kochi
https://ewastekochi.com/proof/certificate-samples""".strip().split("\n")

# Collect new pages from generated output
new_urls = []
try:
    url_file = os.path.join(BASE, "_all_urls.txt")
    with open(url_file) as f:
        new_urls = [u.strip() for u in f.readlines() if u.strip()]
except:
    # Scan the directory
    for html_file in Path(BASE).rglob("*.html"):
        if html_file.name == "_all_urls.txt":
            continue
        rel = html_file.relative_to(BASE)
        parts = list(rel.parts)
        slug = str(rel).replace(".html", "")
        new_urls.append(f"{SITE}/{slug}")

# Combine all URLs, deduplicate
all_urls = list(dict.fromkeys(EXISTING_URLS + new_urls))
print(f"Total unique URLs: {len(all_urls)}")

# Sort by priority desc, then alphabetically
all_urls_sorted = sorted(all_urls, key=lambda u: (-float(get_priority(u)), u))

# Generate sitemap XML
header = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9
        http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd"
        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">"""

lines = [header]
for url in all_urls_sorted:
    p = get_priority(url)
    f = get_freq(url)
    lines += [
        "  <url>",
        f"    <loc>{url}</loc>",
        f"    <lastmod>{TODAY}</lastmod>",
        f"    <changefreq>{f}</changefreq>",
        f"    <priority>{p}</priority>",
        "  </url>",
    ]
lines.append("</urlset>")

sitemap_content = "\n".join(lines)
out_path = os.path.join(BASE, "sitemap.xml")
with open(out_path, "w") as f:
    f.write(sitemap_content)

print(f"✅ sitemap.xml written: {len(all_urls_sorted)} URLs")
print(f"   File size: {os.path.getsize(out_path)/1024:.1f} KB")

# Generate sitemap index
index_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <sitemap>
    <loc>{SITE}/sitemap.xml</loc>
    <lastmod>{TODAY}</lastmod>
  </sitemap>
  <sitemap>
    <loc>{SITE}/sitemap-images.xml</loc>
    <lastmod>{TODAY}</lastmod>
  </sitemap>
  <sitemap>
    <loc>{SITE}/sitemap-news.xml</loc>
    <lastmod>{TODAY}</lastmod>
  </sitemap>
</sitemapindex>"""

with open(os.path.join(BASE, "sitemap-index.xml"), "w") as f:
    f.write(index_xml)

print(f"✅ sitemap-index.xml written")

# Output URL list for deployment
with open(os.path.join(BASE, "all_pages_list.txt"), "w") as f:
    for url in all_urls_sorted:
        f.write(url + "\n")
print(f"✅ all_pages_list.txt written ({len(all_urls_sorted)} URLs)")
