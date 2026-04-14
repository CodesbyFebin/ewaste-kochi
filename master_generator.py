#!/usr/bin/env python3
"""
EWaste Kochi — 5000-Page SEO Domination Generator
Generates unique, AI-crawlable, schema-rich HTML pages for every keyword cluster
"""
import os, json, random
from pathlib import Path
from datetime import date, datetime

TODAY = date.today().isoformat()
SITE = "https://ewastekochi.com"
BASE = "/media/hp-ml10/Projects/ewastekochi-production/ewastekochi"

# ─── KEYWORD UNIVERSE ─────────────────────────────────────────
# High-traffic, low-competition keyword clusters with location combos

LOCATIONS = [
    ("kochi","Kochi","9.9312","76.2673"),
    ("ernakulam","Ernakulam","9.9816","76.2999"),
    ("kakkanad","Kakkanad","10.0159","76.3419"),
    ("edappally","Edappally","10.0200","76.3100"),
    ("vyttila","Vyttila","9.9630","76.3000"),
    ("aluva","Aluva","10.1004","76.3519"),
    ("kalamassery","Kalamassery","10.0574","76.3205"),
    ("thrippunithura","Thrippunithura","9.9290","76.3390"),
    ("palarivattom","Palarivattom","10.0007","76.3050"),
    ("infopark","Infopark Kakkanad","10.0159","76.3419"),
    ("smart-city","SmartCity Kochi","9.9580","76.3680"),
    ("fort-kochi","Fort Kochi","9.9658","76.2421"),
    ("marine-drive","Marine Drive Kochi","9.9641","76.2837"),
    ("mg-road","MG Road Ernakulam","9.9816","76.2999"),
    ("panampilly-nagar","Panampilly Nagar Kochi","9.9731","76.2890"),
    ("kaloor","Kaloor Kochi","10.0000","76.2967"),
    ("thevara","Thevara Kochi","9.9480","76.3000"),
    ("maradu","Maradu Kochi","9.9480","76.3400"),
    ("perumbavoor","Perumbavoor","10.1072","76.4680"),
    ("angamaly","Angamaly","10.1953","76.3839"),
    ("north-paravur","North Paravur","10.1415","76.2145"),
    ("moovattupuzha","Moovattupuzha","9.9862","76.5843"),
    ("kothamangalam","Kothamangalam","10.0598","76.6297"),
    ("piravom","Piravom","9.8667","76.5000"),
    ("alappuzha","Alappuzha","9.4981","76.3388"),
    ("thrissur","Thrissur","10.5276","76.2144"),
    ("muvattupuzha","Muvattupuzha","9.9862","76.5843"),
    ("thodupuzha","Thodupuzha","9.8967","76.7168"),
    ("kolenchery","Kolenchery","9.9833","76.4667"),
    ("tripunithura","Tripunithura","9.9433","76.3510"),
]

SERVICES = [
    "e-waste-recycling",
    "e-waste-pickup",
    "e-waste-collection",
    "e-waste-disposal",
    "ewaste-recycling",
    "ewaste-pickup",
    "battery-recycling",
    "laptop-recycling",
    "mobile-recycling",
    "computer-recycling",
    "data-destruction",
    "hard-drive-shredding",
    "itad",
    "it-asset-disposal",
    "server-recycling",
    "ssd-destruction",
    "electronics-recycling",
    "free-ewaste-pickup",
    "corporate-ewaste",
    "e-waste-management",
]

DEVICES = [
    ("laptop","laptop","laptops","Laptop"),
    ("desktop","desktop","desktops","Desktop Computer"),
    ("server","server","servers","Server"),
    ("printer","printer","printers","Printer"),
    ("monitor","monitor","monitors","Monitor"),
    ("phone","phone","smartphones","Smartphone"),
    ("tablet","tablet","tablets","Tablet"),
    ("macbook","MacBook","MacBooks","MacBook"),
    ("iphone","iPhone","iPhones","iPhone"),
    ("ipad","iPad","iPads","iPad"),
    ("router","router","routers","Router"),
    ("switch","network switch","network switches","Network Switch"),
    ("projector","projector","projectors","Projector"),
    ("keyboard","keyboard","keyboards","Keyboard"),
    ("mouse","mouse","mice","Mouse"),
    ("hard-drive","hard drive","hard drives","Hard Drive"),
    ("ssd","SSD","SSDs","SSD"),
    ("ram","RAM module","RAM modules","RAM"),
    ("ups","UPS","UPS units","UPS System"),
    ("battery","battery","batteries","Battery"),
    ("crt-monitor","CRT monitor","CRT monitors","CRT Monitor"),
    ("led-tv","LED TV","LED TVs","LED TV"),
    ("gaming-console","gaming console","gaming consoles","Gaming Console"),
    ("smartwatch","smartwatch","smartwatches","Smartwatch"),
    ("drone","drone","drones","Drone"),
    ("ac","air conditioner","air conditioners","Air Conditioner"),
    ("cctv","CCTV camera","CCTV cameras","CCTV Camera"),
    ("pos-system","POS system","POS systems","POS System"),
    ("atm","ATM machine","ATM machines","ATM Machine"),
    ("solar-panel","solar panel","solar panels","Solar Panel"),
]

BRANDS = [
    ("dell","Dell"),("hp","HP"),("lenovo","Lenovo"),("apple","Apple"),
    ("samsung","Samsung"),("sony","Sony"),("lg","LG"),("acer","Acer"),
    ("asus","Asus"),("toshiba","Toshiba"),("compaq","Compaq"),
    ("ibm","IBM"),("cisco","Cisco"),("netgear","Netgear"),
    ("motorola","Motorola"),("oneplus","OnePlus"),("xiaomi","Xiaomi"),
    ("realme","Realme"),("vivo","Vivo"),("oppo","Oppo"),
]

INDUSTRIES = [
    ("hospital","Hospital","hospitals","Healthcare"),
    ("bank","Bank","banks","Banking"),
    ("school","School","schools","Education"),
    ("college","College","colleges","Higher Education"),
    ("hotel","Hotel","hotels","Hospitality"),
    ("restaurant","Restaurant","restaurants","Food & Beverage"),
    ("startup","Startup","startups","Technology"),
    ("law-firm","Law Firm","law firms","Legal"),
    ("ca-firm","CA Firm","CA firms","Accounting"),
    ("pharmacy","Pharmacy","pharmacies","Pharmaceutical"),
    ("clinic","Clinic","clinics","Healthcare"),
    ("gym","Gym","gyms","Fitness"),
    ("mall","Shopping Mall","shopping malls","Retail"),
    ("logistics","Logistics Company","logistics companies","Logistics"),
    ("manufacturing","Manufacturing Plant","manufacturing plants","Manufacturing"),
    ("it-company","IT Company","IT companies","Information Technology"),
    ("telecom","Telecom Company","telecom companies","Telecommunications"),
    ("ngo","NGO","NGOs","Non-Profit"),
    ("government","Government Office","government offices","Government"),
    ("apartment","Apartment Complex","apartment complexes","Residential"),
]

INTENT_PAGES = [
    # Near Me / Local Intent
    ("where-to-recycle-batteries-near-me", "recycling", "Where to Recycle Batteries Near Me | Kochi 2026",
     "Find certified battery recycling near you in Kochi. All battery types accepted — lithium, lead-acid, NiMH. Free corporate collection.",
     "battery recycling near me"),
    ("where-to-recycle-old-electronics-near-me", "recycling", "Where to Recycle Old Electronics Near Me | Kochi",
     "Recycle old electronics near you in Kochi. Free certified collection, KSPCB authorised, all brands accepted.",
     "where to recycle old electronics"),
    ("where-to-donate-electronics-kochi", "collection", "Where to Donate Electronics Kochi | Free Device Donation",
     "Donate old electronics in Kochi. Schools, NGOs and refurbishers — we collect and redistribute working devices for free.",
     "where to donate electronics"),
    ("local-recycling-centers-kochi", "recycling", "Local E-Waste Recycling Centers Kochi | KSPCB Certified",
     "Local certified e-waste recycling centers in Kochi. Walk-in, drop-off, or free pickup. All electronics accepted.",
     "local recycling centers"),
    ("how-to-recycle-electronics-india", "guides", "How to Recycle Electronics India | Step-by-Step 2026",
     "Learn how to recycle electronics in India legally. KSPCB rules, EPR compliance, data destruction — complete guide.",
     "how to recycle electronics"),
    ("where-to-sell-electronics-locally-kochi", "trading", "Where to Sell Electronics Locally Kochi | Best Price 2026",
     "Best places to sell electronics locally in Kochi. Instant valuation, free pickup, same-day payment. All brands & conditions.",
     "where to sell electronics locally"),
    ("e-waste-collection-near-me-kochi", "collection", "E-Waste Collection Near Me | Free Kochi Pickup",
     "E-waste collection near you in Kochi. KSPCB certified, free corporate pickup, Certificate of Destruction issued.",
     "e waste collection near me"),
    ("cashify-kochi-alternative-2026", "trading", "Cashify Kochi Alternative 2026 | Better Price + Certified",
     "Better than Cashify in Kochi — higher prices, NIST data destruction, KSPCB certification. Sell any device safely.",
     "cashify kochi"),
    ("waste-management-kochi-guide", "general-waste", "Waste Management Kochi | E-Waste Complete Guide 2026",
     "Complete waste management guide for Kochi. E-waste rules, certified recyclers, free pickup — everything you need to know.",
     "waste management kochi"),
    ("waste-collection-near-me-kochi", "collection", "Waste Collection Near Me Kochi | Same-Day E-Waste Pickup",
     "Waste collection near you in Kochi. E-waste, batteries, IT equipment — free corporate pickup, same-day service available.",
     "waste collection near me"),
    ("ewaste-recycling-near-me-ernakulam", "recycling", "E-Waste Recycling Near Me | Ernakulam Free Collection",
     "Find e-waste recycling near you in Ernakulam. KSPCB certified, free pickup, data destruction, Certificate of Destruction.",
     "ewaste recycling near me"),
    ("e-waste-buyers-near-me-kochi", "trading", "E-Waste Buyers Near Me Kochi | Instant Quote 2026",
     "E-waste buyers near you in Kochi. Best prices for old electronics, IT assets, scrap laptops & phones. Free pickup.",
     "e waste buyers near me"),
    ("hard-drive-destruction-service-kochi", "data-security", "Hard Drive Destruction Service Kochi | NIST Certified",
     "Professional hard drive destruction service in Kochi. NIST 800-88 shredding, Certificate of Destruction, on-site available.",
     "hard drive destruction service"),
    ("secure-e-waste-destruction-kochi", "data-security", "Secure E-Waste Destruction Kochi | Data Safe Disposal",
     "Secure e-waste destruction in Kochi. NIST data wipe + physical shredding. DPDP Act 2023 compliant Certificate of Destruction.",
     "secure e waste destruction"),
    ("ewaste-disposal-near-me", "disposal", "E-Waste Disposal Near Me | Kochi Free Collection",
     "E-waste disposal near you in Kochi. Certified, free for corporates, KSPCB authorised. Book in 60 seconds via WhatsApp.",
     "e waste disposal near me"),
    ("recycle-device-kochi", "recycling", "Recycle Device Kochi | Any Brand Any Condition",
     "Recycle any device in Kochi. Laptops, phones, tablets, servers — all brands, working or broken. Free certified recycling.",
     "recycle device"),
    ("electronics-recycling-near-me-kochi", "recycling", "Electronics Recycling Near Me | Kochi KSPCB Certified",
     "Electronics recycling near you in Kochi. Free collection for 10+ devices. All electronics accepted. KSPCB authorised.",
     "electronics recycling near me"),
    ("sell-electronic-waste-kochi", "trading", "Sell Electronic Waste Kochi | Best Price Instant Payment",
     "Sell electronic waste in Kochi. Instant valuation, free pickup, same-day payment. KSPCB certified buyer. All conditions.",
     "sell electronic waste"),
    ("hard-drive-disposal-kochi", "data-security", "Hard Drive Disposal Kochi | Secure NIST 800-88 Method",
     "Secure hard drive disposal in Kochi. NIST 800-88 certified wiping and physical shredding. Certificate of Destruction issued.",
     "hard drive disposal"),
    ("hard-drive-shredding-kochi-2026", "data-security", "Hard Drive Shredding Kochi 2026 | On-Site Available",
     "Hard drive shredding in Kochi. On-site mobile shredding unit, NIST 800-88 certified, witnessed destruction. Book today.",
     "hard drive shredding"),
    ("itad-companies-india-kochi", "data-security", "ITAD Companies India | Kochi's Best ITAD Service 2026",
     "Top ITAD company in India serving Kochi. KSPCB certified, NIST compliant, EPR credits, Certificate of Destruction.",
     "itad companies in india"),
    ("secure-computer-recycling-kochi", "data-security", "Secure Computer Recycling Kochi | Data Destruction First",
     "Secure computer recycling in Kochi. NIST data wipe before recycling. KSPCB certified, Certificate of Destruction.",
     "secure computer recycling"),
    ("disposing-ewaste-guide-india", "guides", "Disposing E-Waste Legally India | Complete Guide 2026",
     "How to dispose e-waste legally in India. E-Waste Rules 2022, KSPCB authorisation, DPDP Act compliance — full guide.",
     "disposing e waste"),
    ("tv-ewaste-disposal-kochi", "disposal", "TV E-Waste Disposal Kochi | LED LCD CRT Recycling",
     "TV disposal in Kochi. LED, LCD, plasma and CRT TVs accepted. Certified recycling, free corporate collection.",
     "tv e waste near me"),
    ("aakri-shop-near-me-kochi", "trading", "Aakri Shop Near Me Kochi | Certified Alternative 2026",
     "Better than aakri shops in Kochi — certified e-waste recycling with data destruction, KSPCB certification and receipts.",
     "aakri shop near me"),
    ("e-waste-dealer-near-me-kochi", "trading", "E-Waste Dealer Near Me Kochi | Certified KSPCB Dealer",
     "Certified e-waste dealer near you in Kochi. KSPCB authorised, NIST data destruction, Certificate of Destruction issued.",
     "e waste dealer near me"),
    ("e-waste-scrap-buyers-near-me", "trading", "E-Waste Scrap Buyers Near Me | Kochi Instant Quote",
     "E-waste and electronics scrap buyers near you in Kochi. Best price for bulk IT scrap. Free pickup, same-day payment.",
     "e waste scrap buyers near me"),
    ("electronic-waste-disposal-near-me", "disposal", "Electronic Waste Disposal Near Me | Kochi Certified",
     "Certified electronic waste disposal near you in Kochi. KSPCB authorised, free corporate collection, data destruction.",
     "electronic waste disposal near me"),
    ("secure-waste-disposal-kochi", "data-security", "Secure Waste Disposal Kochi | IT Assets Data Destruction",
     "Secure IT waste disposal in Kochi. Hard drives wiped to NIST 800-88 standard. Certificate of Destruction. DPDP compliant.",
     "secure waste disposal"),
    ("ac-recycling-kochi", "recycling", "AC Recycling Kochi | Split Window Central AC Disposal",
     "Air conditioner recycling in Kochi. Split AC, window AC, central AC units — certified refrigerant recovery and recycling.",
     "ac recycle"),
    ("cd-dvd-recycling-kochi", "recycling", "CD DVD Recycling Kochi | Optical Media Destruction",
     "CD, DVD and optical media destruction in Kochi. Data-safe shredding, polycarbonate recovery. Certificate issued.",
     "cd recycling near me"),
    ("damaged-mobile-recycling-kochi", "recycling", "Damaged Mobile Phone Recycling Kochi | Any Condition",
     "Recycle damaged, broken or water-damaged mobile phones in Kochi. All brands, any condition. Free pickup for bulk.",
     "damaged mobile phone recycling"),
    ("old-phone-disposal-kochi", "disposal", "Old Phone Disposal Kochi | Secure Data Wipe + Recycling",
     "Dispose old phones in Kochi. Certified data wipe, physical recycling. Free pickup for 10+ devices. Certificate issued.",
     "old phone disposal near me"),
    ("waste-management-near-me-kochi", "general-waste", "Waste Management Near Me | Kochi E-Waste Specialists",
     "Waste management services near you in Kochi. E-waste, batteries, IT equipment — certified collection and recycling.",
     "waste management near me"),
    ("waste-management-companies-kochi", "collection", "Waste Management Companies Kochi | Top Certified 2026",
     "Best waste management companies in Kochi for e-waste. KSPCB certified, free pickup, data destruction, EPR credits.",
     "waste management companies in kochi"),
    ("it-disposal-services-kochi", "disposal", "IT Disposal Services Kochi | ITAD Certified 2026",
     "Professional IT disposal services in Kochi. NIST data destruction, EPR compliance, Certificate of Destruction. Free pickup.",
     "it disposal services"),
    ("mobile-recycling-kochi", "recycling", "Mobile Recycling Kochi | All Brands Any Condition",
     "Mobile phone recycling in Kochi. NIST data wipe, physical recycling. All brands accepted — Samsung, iPhone, OnePlus.",
     "mobile recycle"),
    ("business-it-decommissioning-kochi", "data-security", "Business IT Decommissioning Kochi | Complete ITAD Service",
     "IT decommissioning for Kochi businesses. Data destruction, asset recovery, EPR compliance, Certificate of Destruction.",
     "business it decommissioning services"),
    ("it-equipment-disposal-kochi", "disposal", "IT Equipment Disposal Kochi | Free Corporate Collection",
     "IT equipment disposal in Kochi. Servers, laptops, desktops, networking equipment — certified, free pickup for bulk.",
     "it equipment disposal"),
    ("plasma-tv-disposal-kochi", "disposal", "Plasma TV Disposal Kochi | Certified Recycling Service",
     "Plasma TV disposal in Kochi. Certified recycling of plasma panels, safe handling of hazardous phosphors. Free for bulk.",
     "plasma tv disposal"),
    ("sell-electronics-kochi", "trading", "Sell Electronics Kochi | Best Price Instant Payment 2026",
     "Sell any electronics in Kochi. Laptops, phones, servers, tablets — best price, free pickup, same-day payment.",
     "sell electronics"),
    ("ewaste-pickup-kochi-free", "collection", "Free E-Waste Pickup Kochi | Corporate & Residential",
     "Free e-waste pickup in Kochi for 10+ corporate devices. Same-day available. KSPCB certified. WhatsApp +91 75005 55454.",
     "ewaste pickup"),
    ("e-waste-laptop-recycling", "recycling", "E-Waste Laptop Recycling Kochi | All Brands Certified",
     "Laptop e-waste recycling in Kochi. NIST data wipe, certified recycling, buyback available. Dell, HP, Apple, Lenovo.",
     "e waste laptop"),
    ("e-waste-shop-near-me-kochi", "general-waste", "E-Waste Shop Near Me Kochi | Certified Collection Point",
     "E-waste collection shops near you in Kochi. Walk-in at our Thrippunithura facility or 6 kiosk locations across Ernakulam.",
     "e waste shop near me"),
    ("ewaste-scrap-buyers-kochi", "trading", "E-Waste Scrap Buyers Kochi | KSPCB Certified Buyer",
     "Certified e-waste scrap buyers in Kochi. Best price for IT scrap, electronics, and bulk hardware. Free corporate pickup.",
     "ewaste scrap"),
    ("itad-kochi-complete", "data-security", "ITAD Kochi | Complete IT Asset Disposition 2026",
     "Complete ITAD service in Kochi. Data destruction, asset recovery, EPR compliance, Certificate of Destruction. Book now.",
     "itad"),
    ("dpdp-act-india-ewaste", "compliance", "DPDP Act India E-Waste Compliance | Kerala Business Guide",
     "India's DPDP Act 2023 and e-waste disposal obligations for Kerala businesses. Compliance checklist and certified partners.",
     "india dpdp act data privacy"),
    ("e-waste-sale-kochi", "trading", "E-Waste Sale Kochi | Buy Certified Recycled Parts",
     "Buy certified recycled electronics parts in Kochi. Tested components from IT asset recovery. Best quality, best price.",
     "e waste sale"),
    ("gdpr-dpdp-compliance-kochi", "compliance", "GDPR & DPDP Compliance Kochi | Data Destruction Guide",
     "GDPR and DPDP Act 2023 compliant data destruction in Kochi. Certificate of Destruction accepted by international auditors.",
     "gdpr compliance in cochin"),
    ("hard-drive-shredding-company-kochi", "data-security", "Hard Drive Shredding Company Kochi | NIST Certified",
     "Kochi's leading hard drive shredding company. NIST 800-88 certified, on-site available, Certificate of Destruction.",
     "hard drive shredding company"),
    ("it-disposal-education-kochi", "industries", "IT Disposal for Education Kochi | Free School Service",
     "Free IT disposal for schools and colleges in Kochi. NIST data wipe, certified recycling, Green School Certificate.",
     "it disposal services for education"),
    ("secure-computer-disposal-kochi", "data-security", "Secure Computer Disposal Kochi | NIST DPDP Certified",
     "Secure computer disposal in Kochi. NIST 800-88 data wipe, physical shredding, Certificate of Destruction. Free pickup.",
     "secure computer disposal"),
    ("secure-laptop-disposal-kochi", "data-security", "Secure Laptop Disposal Kochi | Data Wipe + Recycling",
     "Secure laptop disposal in Kochi. NIST data destruction + certified recycling. Certificate of Destruction for compliance.",
     "secure laptop disposal"),
    ("device-recycling-kochi", "recycling", "Device Recycling Kochi | All Electronics Any Condition",
     "Recycle any device in Kochi. Phones, laptops, tablets, servers — certified recycling, data destruction, free pickup.",
     "device recycle"),
    ("plasma-tv-recycling-kochi", "recycling", "Plasma TV Recycling Kochi | Hazardous Phosphor Safe",
     "Plasma TV recycling in Kochi. Safe phosphor handling, panel dismantling, certified hazardous waste processing.",
     "plasma tv disposal"),
    ("sell-old-phone-kochi", "trading", "Sell Old Phone Kochi | Best Price Any Brand 2026",
     "Sell your old phone in Kochi. Any brand, any condition — iPhone, Samsung, OnePlus. Instant quote, same-day pickup.",
     "sell old phone"),
    ("ewaste-hub-kochi", "general-waste", "E-Waste Hub Kochi | Kerala's Certified Recycling Centre",
     "Kochi's e-waste hub. KSPCB certified facility at Thrippunithura. Walk-in, corporate, institutional — all served.",
     "ewaste hub"),
    ("e-waste-rules-kerala-2022", "guides", "E-Waste Rules Kerala 2022 | Complete Compliance Guide",
     "Complete guide to E-Waste Management Rules 2022 for Kerala. Producer, consumer, bulk consumer obligations explained.",
     "e waste rules kerala"),
    ("building-waste-disposal-kochi", "disposal", "Building Waste Kochi | Construction Electronics Disposal",
     "Electronic waste from construction and building sites in Kochi. Wiring, panels, HVAC controls — certified disposal.",
     "building waste near me"),
    ("ewaste-682207", "locations", "E-Waste Recycling 682207 | Kochi Pincode Service",
     "E-waste recycling service for pincode 682207 Kochi. Free pickup, data destruction, KSPCB certified.",
     "682207 ewaste"),
]

# ─── HTML TEMPLATE ─────────────────────────────────────────────
def make_page(folder, slug, h1, meta_desc, primary_kw, canonical_url, cat_label, 
               lat="9.9312", lng="76.2673", location="Kochi", page_type="service",
               device="", brand="", industry=""):

    slug_label = h1
    schema_type = "LocalBusiness" if "near me" in slug or any(l[0] in slug for l in LOCATIONS) else "WebPage"
    
    # Build content paragraphs based on slug context
    is_location = folder == "locations"
    is_data = folder == "data-security"
    is_trading = folder == "trading"
    is_recycling = folder == "recycling"
    is_collection = folder == "collection"
    is_guide = folder == "guides"
    
    content_blocks = generate_content(h1, meta_desc, primary_kw, location, slug, 
                                       is_data, is_trading, is_recycling, is_collection, is_guide, device, brand, industry)
    
    faqs = generate_faqs(h1, primary_kw, location, is_data, is_trading)
    
    html = f"""<!DOCTYPE html>
<html lang="en" prefix="og: https://ogp.me/ns#">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0,viewport-fit=cover">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<title>{h1} | EWaste Kochi — Kerala's #1 Certified Recycler</title>
<meta name="description" content="{meta_desc}">
<meta name="keywords" content="{primary_kw}, ewaste kochi, e-waste recycling kochi, KSPCB certified recycler, data destruction kochi, free ewaste pickup kochi, certified e waste recycler kerala, e waste near me, ewaste near me">
<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1">
<meta name="googlebot" content="index,follow,max-snippet:-1,max-image-preview:large">
<meta name="author" content="EWaste Kochi">
<meta name="revisit-after" content="7 days">
<meta name="geo.region" content="IN-KL">
<meta name="geo.placename" content="{location}, Kerala, India">
<meta name="geo.position" content="{lat};{lng}">
<meta name="ICBM" content="{lat}, {lng}">
<meta name="DC.language" content="en">
<meta name="DC.subject" content="E-Waste Recycling, Data Destruction, ITAD, {location}, Kerala">
<meta name="date" content="{TODAY}">
<link rel="canonical" href="{canonical_url}">
<link rel="alternate" hreflang="en-in" href="{canonical_url}">
<link rel="alternate" hreflang="x-default" href="{canonical_url}">
<meta property="og:site_name" content="EWaste Kochi">
<meta property="og:type" content="article">
<meta property="og:title" content="{h1} | EWaste Kochi">
<meta property="og:description" content="{meta_desc}">
<meta property="og:url" content="{canonical_url}">
<meta property="og:image" content="https://ewastekochi.com/assets/og-default.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="en_IN">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{h1} | EWaste Kochi">
<meta name="twitter:description" content="{meta_desc}">
<meta name="twitter:image" content="https://ewastekochi.com/assets/og-default.jpg">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon-32x32.png">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="manifest" href="/manifest.json">
<meta name="theme-color" content="#00E664">
<link rel="preconnect" href="https://fonts.googleapis.com" crossorigin>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Outfit:wght@300;400;600;700;800&display=swap" rel="stylesheet">
<script type="application/ld+json">
{{
  "@context":"https://schema.org",
  "@graph":[
    {{
      "@type":"Organization",
      "@id":"https://ewastekochi.com/#organization",
      "name":"EWaste Kochi",
      "url":"https://ewastekochi.com",
      "logo":"https://ewastekochi.com/assets/logo.png",
      "telephone":"+91-7500555454",
      "email":"info@ewastekochi.com",
      "address":{{"@type":"PostalAddress","addressLocality":"Kochi","addressRegion":"Kerala","postalCode":"682301","addressCountry":"IN"}},
      "geo":{{"@type":"GeoCoordinates","latitude":9.9312,"longitude":76.2673}},
      "aggregateRating":{{"@type":"AggregateRating","ratingValue":"4.9","reviewCount":"312","bestRating":"5"}},
      "sameAs":["https://www.linkedin.com/company/ewastekochi","https://twitter.com/EWasteKochi","https://www.facebook.com/ewastekochi"]
    }},
    {{
      "@type":"LocalBusiness",
      "@id":"https://ewastekochi.com/#localbusiness",
      "name":"EWaste Kochi",
      "telephone":"+91-7500555454",
      "priceRange":"₹₹",
      "address":{{"@type":"PostalAddress","streetAddress":"Near Thrippunithura","addressLocality":"{location}","addressRegion":"Kerala","postalCode":"682301","addressCountry":"IN"}},
      "geo":{{"@type":"GeoCoordinates","latitude":{lat},"longitude":{lng}}},
      "openingHoursSpecification":[{{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],"opens":"09:00","closes":"19:00"}}],
      "areaServed":"{location}, Kerala",
      "aggregateRating":{{"@type":"AggregateRating","ratingValue":"4.9","reviewCount":"312","bestRating":"5"}}
    }},
    {{
      "@type":"WebPage",
      "@id":"{canonical_url}#webpage",
      "url":"{canonical_url}",
      "name":"{h1}",
      "description":"{meta_desc}",
      "isPartOf":{{"@id":"https://ewastekochi.com/#website"}},
      "about":{{"@id":"https://ewastekochi.com/#organization"}},
      "datePublished":"{TODAY}",
      "dateModified":"{TODAY}",
      "inLanguage":"en-IN",
      "breadcrumb":{{"@id":"{canonical_url}#breadcrumb"}}
    }},
    {{
      "@type":"BreadcrumbList",
      "@id":"{canonical_url}#breadcrumb",
      "itemListElement":[
        {{"@type":"ListItem","position":1,"name":"Home","item":"https://ewastekochi.com/"}},
        {{"@type":"ListItem","position":2,"name":"{cat_label}","item":"https://ewastekochi.com/{folder}/"}},
        {{"@type":"ListItem","position":3,"name":"{h1}","item":"{canonical_url}"}}
      ]
    }},
    {{
      "@type":"FAQPage",
      "@id":"{canonical_url}#faq",
      "mainEntity":[
        {{"@type":"Question","name":"Is EWaste Kochi KSPCB authorised?","acceptedAnswer":{{"@type":"Answer","text":"Yes. EWaste Kochi holds current KSPCB authorisation under E-Waste Management Rules 2022, reference KSPCB/EW/2022/EK-047. We are CPCB-registered as both dismantler and recycler for all 21 e-waste categories."}}}},
        {{"@type":"Question","name":"Do you provide a Certificate of Destruction?","acceptedAnswer":{{"@type":"Answer","text":"Yes. Every job receives a legally-valid Certificate of Destruction listing serial numbers, NIST 800-88 destruction method, technician ID, and date. Accepted by statutory auditors for DPDP Act 2023 and RBI compliance."}}}},
        {{"@type":"Question","name":"How do I book a free e-waste pickup in {location}?","acceptedAnswer":{{"@type":"Answer","text":"WhatsApp +91 75005 55454 or visit ewastekochi.com/collection/book-free-pickup-kochi. Free pickup for 10+ devices in Ernakulam district. Same-day service available for bookings before 12 PM weekdays."}}}}
      ]
    }},
    {{
      "@type":"Service",
      "name":"{h1}",
      "provider":{{"@id":"https://ewastekochi.com/#organization"}},
      "areaServed":"{location}, Kerala",
      "description":"{meta_desc}",
      "url":"{canonical_url}",
      "serviceType":"E-Waste Recycling & Data Destruction"
    }}
  ]
}}
</script>
<style>
:root{{--bg:#0A0F0C;--bg2:#0F1912;--bg3:#141F16;--green:#00E664;--green2:#00C853;--white:#E8F2EA;--text:#9BB8A2;--muted:#5A7A62;--border:rgba(0,230,100,.13);--border2:rgba(0,230,100,.06);--r:12px;--r2:20px;}}
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
html{{scroll-behavior:smooth;-webkit-font-smoothing:antialiased}}
body{{font-family:'Outfit',sans-serif;background:var(--bg);color:var(--text);line-height:1.75;overflow-x:hidden}}
a{{color:inherit;text-decoration:none}}
img{{max-width:100%;height:auto}}
.wrap{{max-width:1200px;margin:0 auto;padding:0 20px}}
h1,h2,h3{{font-family:'Bebas Neue',cursive;text-transform:uppercase;line-height:1.05;letter-spacing:.02em}}
h1{{font-size:clamp(2.2rem,5.5vw,4.2rem);color:var(--white);margin-bottom:16px}}
h2{{font-size:clamp(1.6rem,3vw,2.6rem);color:var(--white);margin-bottom:18px}}
h3{{font-size:1.1rem;color:var(--green);margin:16px 0 8px;letter-spacing:.05em;text-transform:uppercase}}
h4{{font-size:.95rem;color:var(--white);margin:12px 0 6px;font-weight:700}}
p{{margin-bottom:14px;font-size:.95rem;line-height:1.8}}
strong{{color:var(--white);font-weight:700}}
ul{{padding-left:1.2rem;margin-bottom:14px}}
li{{margin-bottom:6px;font-size:.92rem}}
.section{{padding:64px 0;border-bottom:1px solid var(--border2)}}
.section:last-child{{border-bottom:none}}

/* NAV */
.nav{{background:rgba(7,16,10,.97);backdrop-filter:blur(24px);-webkit-backdrop-filter:blur(24px);border-bottom:1px solid var(--border);position:sticky;top:0;z-index:100;height:60px;display:flex;align-items:center}}
.nav-in{{max-width:1200px;margin:0 auto;padding:0 20px;width:100%;display:flex;align-items:center;justify-content:space-between;gap:16px}}
.brand{{font-family:'Bebas Neue';font-size:1.4rem;color:var(--white);display:flex;align-items:center;gap:8px;white-space:nowrap}}
.nav-links{{display:flex;gap:16px;font-size:.78rem;font-weight:600;color:var(--muted)}}
.nav-links a:hover{{color:var(--green)}}
.nav-cta{{background:var(--green);color:var(--bg);padding:7px 16px;border-radius:8px;font-weight:800;font-size:.78rem;white-space:nowrap;flex-shrink:0;transition:opacity .2s}}
.nav-cta:hover{{opacity:.88}}

/* BREADCRUMB */
.bc{{padding:9px 0;font-size:.78rem;color:var(--muted);border-bottom:1px solid var(--border2)}}
.bc a{{color:var(--green);transition:opacity .2s}}
.bc a:hover{{opacity:.75}}
.bc span{{margin:0 6px}}

/* HERO */
.hero{{min-height:52vh;display:flex;align-items:center;position:relative;overflow:hidden;border-bottom:1px solid var(--border)}}
.hero::before{{content:'';position:absolute;inset:0;background:radial-gradient(ellipse 70% 60% at 10% 50%,rgba(0,230,100,.09) 0%,transparent 70%);pointer-events:none}}
.hero::after{{content:'';position:absolute;top:-40%;right:-10%;width:600px;height:600px;background:radial-gradient(circle,rgba(0,230,100,.04) 0%,transparent 60%);pointer-events:none}}
.hero-inner{{position:relative;z-index:1;padding:60px 0}}
.badge-row{{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:18px}}
.badge{{display:inline-flex;align-items:center;gap:5px;background:rgba(0,230,100,.1);border:1px solid rgba(0,230,100,.25);color:var(--green);padding:4px 12px;border-radius:50px;font-size:.72rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase}}
.hero-desc{{max-width:680px;font-size:1.05rem;color:rgba(232,242,234,.82);margin-bottom:24px;line-height:1.7}}
.btn-row{{display:flex;flex-wrap:wrap;gap:10px;margin-bottom:32px}}
.btn{{display:inline-flex;align-items:center;gap:8px;font-weight:800;padding:12px 22px;border-radius:10px;font-size:.88rem;transition:all .2s;cursor:pointer;border:none}}
.btn-wa{{background:#25D366;color:#fff}}
.btn-wa:hover{{background:#22c55e}}
.btn-call{{background:rgba(255,255,255,.08);color:var(--white);border:1px solid rgba(255,255,255,.15)}}
.btn-call:hover{{background:rgba(255,255,255,.13)}}
.btn-outline{{border:2px solid var(--green);color:var(--green);background:transparent}}
.btn-outline:hover{{background:var(--green);color:var(--bg)}}

/* STATS GRID */
.stats{{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin:28px 0 0}}
.stat{{background:var(--bg2);border:1px solid var(--border);border-radius:var(--r);padding:20px 16px;text-align:center}}
.sn{{font-family:'Bebas Neue';font-size:2.2rem;color:var(--green);display:block;line-height:1}}
.sl{{font-size:.68rem;text-transform:uppercase;letter-spacing:.1em;color:var(--muted);margin-top:4px;display:block}}

/* CARDS */
.card{{background:var(--bg2);border:1px solid var(--border);border-radius:var(--r2);padding:24px;margin-bottom:16px;transition:border-color .2s}}
.card:hover{{border-color:rgba(0,230,100,.3)}}
.card-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:16px;margin:24px 0}}
.icon-card{{background:var(--bg2);border:1px solid var(--border);border-radius:var(--r2);padding:24px;display:flex;flex-direction:column;gap:10px;transition:transform .2s,border-color .2s}}
.icon-card:hover{{transform:translateY(-2px);border-color:rgba(0,230,100,.3)}}
.icon-card .icon{{font-size:1.8rem}}
.icon-card h4{{color:var(--white);font-size:.95rem;font-weight:800;margin:0}}
.icon-card p{{font-size:.82rem;color:var(--muted);margin:0;line-height:1.6}}

/* PROCESS STEPS */
.steps{{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:16px;margin:24px 0;counter-reset:step}}
.step{{background:var(--bg3);border:1px solid var(--border2);border-radius:var(--r);padding:20px;position:relative;counter-increment:step}}
.step::before{{content:counter(step);position:absolute;top:-10px;left:16px;background:var(--green);color:var(--bg);width:22px;height:22px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:900;font-family:'Outfit',sans-serif}}
.step h4{{color:var(--white);font-size:.88rem;margin-bottom:6px}}
.step p{{font-size:.8rem;margin:0;line-height:1.6}}

/* FAQ */
.faq-item{{background:var(--bg2);border:1px solid var(--border);border-radius:var(--r);margin-bottom:8px;overflow:hidden}}
.faq-q{{padding:16px 20px;cursor:pointer;font-weight:700;color:var(--white);display:flex;justify-content:space-between;align-items:center;font-size:.9rem;user-select:none;list-style:none}}
.faq-q::after{{content:"＋";color:var(--green);font-size:1.2rem;flex-shrink:0;margin-left:12px}}
details[open] .faq-q::after{{content:"－"}}
.faq-a{{padding:0 20px 16px;font-size:.88rem;line-height:1.8;border-top:1px solid var(--border2)}}

/* SILO LINKS */
.silo{{display:flex;flex-wrap:wrap;gap:8px;margin:20px 0}}
.silo a{{background:var(--bg2);border:1px solid var(--border);color:var(--green);padding:7px 14px;border-radius:8px;font-size:.78rem;font-weight:700;transition:all .2s}}
.silo a:hover{{background:var(--green);color:var(--bg)}}

/* PRICING TABLE */
.pricing{{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:12px;margin:20px 0}}
.price-card{{background:var(--bg3);border:1px solid var(--border);border-radius:var(--r);padding:20px;text-align:center}}
.price-card.featured{{border-color:var(--green);background:rgba(0,230,100,.05)}}
.price{{font-family:'Bebas Neue';font-size:2rem;color:var(--green);display:block}}
.price-label{{font-size:.72rem;color:var(--muted);text-transform:uppercase;letter-spacing:.08em}}

/* TRUST BADGES */
.trust-row{{display:flex;flex-wrap:wrap;gap:12px;margin:24px 0;padding:20px;background:var(--bg2);border:1px solid var(--border);border-radius:var(--r2);align-items:center}}
.trust-item{{display:flex;align-items:center;gap:8px;font-size:.78rem;font-weight:700;color:var(--white)}}
.trust-item span{{font-size:1.1rem}}

/* CTA SECTION */
.cta-section{{background:linear-gradient(135deg,rgba(0,230,100,.08) 0%,rgba(0,200,83,.04) 100%);border:1px solid rgba(0,230,100,.2);border-radius:var(--r2);padding:48px 32px;text-align:center;margin:40px 0}}
.cta-section h2{{margin-bottom:12px}}
.cta-section p{{max-width:560px;margin:0 auto 24px;color:rgba(232,242,234,.75)}}

/* TABLE */
table{{width:100%;border-collapse:collapse;margin:16px 0;font-size:.85rem}}
th{{background:rgba(0,230,100,.1);color:var(--green);padding:10px 14px;text-align:left;font-weight:700;font-size:.78rem;text-transform:uppercase;letter-spacing:.06em;border:1px solid var(--border)}}
td{{padding:10px 14px;border:1px solid var(--border2);color:var(--text);vertical-align:top}}
tr:nth-child(even) td{{background:rgba(255,255,255,.02)}}
.check{{color:var(--green)}}
.cross{{color:#ef4444}}

/* FOOTER */
.footer{{background:var(--bg2);border-top:1px solid var(--border);padding:40px 0;margin-top:80px}}
.footer-inner{{display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:32px}}
.footer-brand{{font-family:'Bebas Neue';font-size:1.3rem;color:var(--white);margin-bottom:8px}}
.footer-desc{{font-size:.78rem;color:var(--muted);line-height:1.6;margin-bottom:12px}}
.footer-col h4{{font-size:.72rem;text-transform:uppercase;letter-spacing:.1em;color:var(--muted);margin-bottom:10px;font-weight:700}}
.footer-col a{{display:block;font-size:.8rem;color:var(--muted);padding:3px 0;transition:color .2s}}
.footer-col a:hover{{color:var(--green)}}
.footer-bottom{{border-top:1px solid var(--border2);padding-top:16px;margin-top:24px;font-size:.72rem;color:var(--muted);display:flex;justify-content:space-between;flex-wrap:wrap;gap:8px}}

@media(max-width:900px){{.stats{{grid-template-columns:1fr 1fr}}.footer-inner{{grid-template-columns:1fr 1fr}}.nav-links{{display:none}}}}
@media(max-width:600px){{.stats{{grid-template-columns:1fr 1fr}}.footer-inner{{grid-template-columns:1fr}}.btn-row{{flex-direction:column}}.trust-row{{flex-direction:column}}}}
</style>
</head>
<body>

<!-- NAV -->
<nav class="nav">
  <div class="nav-in">
    <a class="brand" href="/">♻️ EWaste Kochi</a>
    <div class="nav-links">
      <a href="/data-destruction-kochi">Data Destruction</a>
      <a href="/recycling/battery-recycling-kochi">Battery Recycling</a>
      <a href="/collection/ewaste-pickup-kochi">Pickup</a>
      <a href="/trading/sell-old-electronics-near-me">Sell</a>
      <a href="/data-security/itad-kochi">ITAD</a>
    </div>
    <a class="nav-cta" href="https://wa.me/917500555454">WhatsApp →</a>
  </div>
</nav>

<!-- BREADCRUMB -->
<div class="wrap bc">
  <a href="/">Home</a><span>›</span>
  <a href="/{folder}/">{cat_label}</a><span>›</span>
  {h1}
</div>

<!-- HERO -->
<section class="section hero">
  <div class="wrap hero-inner">
    <div class="badge-row">
      <span class="badge">✅ KSPCB Authorised</span>
      <span class="badge">🔒 NIST 800-88</span>
      <span class="badge">📋 DPDP 2023 Compliant</span>
      <span class="badge">🌱 Zero Landfill</span>
    </div>
    <h1>{h1}</h1>
    <p class="hero-desc">{meta_desc}</p>
    <div class="btn-row">
      <a class="btn btn-wa" href="https://wa.me/917500555454?text=Hi%2C+I+need+{slug}">💬 WhatsApp Free Quote</a>
      <a class="btn btn-call" href="tel:+917500555454">📞 +91 75005 55454</a>
      <a class="btn btn-outline" href="/collection/book-free-pickup-kochi">Schedule Pickup →</a>
    </div>
    <div class="stats">
      <div class="stat"><span class="sn">5,000+</span><span class="sl">Jobs Done</span></div>
      <div class="stat"><span class="sn">100%</span><span class="sl">Zero Landfill</span></div>
      <div class="stat"><span class="sn">4.9 ★</span><span class="sl">Client Rating</span></div>
      <div class="stat"><span class="sn">24 / 7</span><span class="sl">WhatsApp</span></div>
    </div>
  </div>
</section>

<!-- TRUST -->
<div class="wrap" style="padding:20px 20px 0">
  <div class="trust-row">
    <div class="trust-item"><span>🏛️</span> KSPCB Authorised Recycler</div>
    <div class="trust-item"><span>🔐</span> NIST 800-88 Data Destruction</div>
    <div class="trust-item"><span>📄</span> Certificate of Destruction</div>
    <div class="trust-item"><span>♻️</span> CPCB Registered</div>
    <div class="trust-item"><span>⚡</span> Same-Day Service Available</div>
    <div class="trust-item"><span>🆓</span> Free for 10+ Corporate Devices</div>
  </div>
</div>

<!-- MAIN CONTENT -->
<section class="section">
  <div class="wrap">
    {content_blocks}
  </div>
</section>

<!-- HOW IT WORKS -->
<section class="section">
  <div class="wrap">
    <h2>How Our {primary_kw.title()} Service Works</h2>
    <p>Booking certified {primary_kw} in {location} takes under 60 seconds. Here's our streamlined 5-step process:</p>
    <div class="steps">
      <div class="step">
        <h4>Book Online or WhatsApp</h4>
        <p>Send a WhatsApp message to +91 75005 55454 or fill our booking form. Instant confirmation guaranteed.</p>
      </div>
      <div class="step">
        <h4>Inventory & Dispatch</h4>
        <p>We log your devices, assign a job number, and dispatch a GPS-tracked vehicle to your {location} location.</p>
      </div>
      <div class="step">
        <h4>Secure Collection</h4>
        <p>Assets are inventoried on-site and sealed in tamper-evident packaging. A pickup receipt is issued immediately.</p>
      </div>
      <div class="step">
        <h4>Data Destruction</h4>
        <p>All storage media is processed using NIST 800-88 methods (Clear, Purge, or Destroy). Process is video-recorded.</p>
      </div>
      <div class="step">
        <h4>Certificate Issued</h4>
        <p>Your digital Certificate of Destruction is emailed within 24 hours. Accepted by statutory auditors for DPDP Act 2023 compliance.</p>
      </div>
    </div>
  </div>
</section>

<!-- PRICING -->
<section class="section">
  <div class="wrap">
    <h2>Transparent Pricing — {primary_kw.title()} in {location}</h2>
    <p>All prices are GST-inclusive with no hidden fees. Free service for schools, NGOs and government offices regardless of volume.</p>
    <div class="pricing">
      <div class="price-card">
        <span class="price">₹299</span>
        <span class="price-label">1–9 Devices</span>
        <p style="font-size:.8rem;margin-top:10px;color:var(--muted)">Logistics fee + ₹80/device data destruction</p>
      </div>
      <div class="price-card featured">
        <span class="price">FREE</span>
        <span class="price-label">10–100 Devices</span>
        <p style="font-size:.8rem;margin-top:10px;color:var(--muted)">Free pickup + ₹60/device all-inclusive</p>
      </div>
      <div class="price-card">
        <span class="price">₹45</span>
        <span class="price-label">101–500 Devices</span>
        <p style="font-size:.8rem;margin-top:10px;color:var(--muted)">Free pickup + dedicated project manager</p>
      </div>
      <div class="price-card featured">
        <span class="price">CUSTOM</span>
        <span class="price-label">500+ Devices</span>
        <p style="font-size:.8rem;margin-top:10px;color:var(--muted)">Enterprise pricing — WhatsApp for same-day quote</p>
      </div>
    </div>
  </div>
</section>

<!-- FAQ -->
<section class="section">
  <div class="wrap">
    <h2>Frequently Asked Questions — {primary_kw.title()} {location}</h2>
    {faqs}
  </div>
</section>

<!-- CTA -->
<div class="wrap">
  <div class="cta-section">
    <h2>Ready to Recycle? Book Free Pickup in {location}</h2>
    <p>Join 5,000+ satisfied clients across Kochi and Ernakulam. KSPCB certified, NIST 800-88 compliant, zero landfill.</p>
    <div class="btn-row" style="justify-content:center">
      <a class="btn btn-wa" href="https://wa.me/917500555454?text=Book+{slug}">💬 WhatsApp Instant Quote</a>
      <a class="btn btn-outline" href="/collection/book-free-pickup-kochi">Book Free Pickup →</a>
    </div>
  </div>
</div>

<!-- SILO LINKS -->
<section class="section">
  <div class="wrap">
    <h2>Related Services — EWaste Kochi</h2>
    <div class="silo">
      <a href="/">🏠 Home</a>
      <a href="/data-destruction-kochi">🔒 Data Destruction</a>
      <a href="/data-security/itad-kochi">🏢 ITAD Kochi</a>
      <a href="/recycling/battery-recycling-kochi">🔋 Battery Recycling</a>
      <a href="/collection/ewaste-pickup-kochi">🚚 Free Pickup</a>
      <a href="/trading/sell-old-electronics-near-me">💰 Sell Electronics</a>
      <a href="/data-security/hard-drive-shredding-kochi">💾 Hard Drive Shredding</a>
      <a href="/recycling/laptop-recycling-kochi">💻 Laptop Recycling</a>
      <a href="/recycling/mobile-recycling-kochi">📱 Mobile Recycling</a>
      <a href="/locations/ewaste-kochi">📍 Locations</a>
      <a href="/data-security/certificate-of-destruction">📄 Certificate</a>
      <a href="/compliance/nist-800-88-explained">📋 NIST 800-88</a>
      <a href="/guides/ewaste-management-rules-2022-guide">📖 E-Waste Rules</a>
      <a href="/compliance/dpdp-act-2023-ewaste-penalties">⚖️ DPDP Act</a>
    </div>
  </div>
</section>

<!-- FOOTER -->
<footer class="footer">
  <div class="wrap">
    <div class="footer-inner">
      <div>
        <div class="footer-brand">♻️ EWaste Kochi</div>
        <p class="footer-desc">Kerala's #1 KSPCB authorised e-waste recycling & data destruction hub. NIST 800-88 · DPDP Act 2023 · EPR Certified · Zero Landfill.</p>
        <div style="font-size:.8rem;color:var(--muted)">
          📞 <a href="tel:+917500555454" style="color:var(--green)">+91 75005 55454</a><br>
          💬 <a href="https://wa.me/917500555454" style="color:#25D366">WhatsApp Us</a><br>
          📧 <a href="mailto:info@ewastekochi.com" style="color:var(--green)">info@ewastekochi.com</a>
        </div>
      </div>
      <div class="footer-col">
        <h4>Services</h4>
        <a href="/recycling/ewaste-recycling-kochi">E-Waste Recycling</a>
        <a href="/data-destruction-kochi">Data Destruction</a>
        <a href="/data-security/itad-kochi">ITAD</a>
        <a href="/recycling/battery-recycling-kochi">Battery Recycling</a>
        <a href="/collection/ewaste-pickup-kochi">Free Pickup</a>
      </div>
      <div class="footer-col">
        <h4>Locations</h4>
        <a href="/locations/ewaste-kochi">Kochi</a>
        <a href="/locations/ewaste-kakkanad">Kakkanad</a>
        <a href="/locations/ewaste-edappally">Edappally</a>
        <a href="/locations/ewaste-aluva">Aluva</a>
        <a href="/locations/ewaste-ernakulam">Ernakulam</a>
      </div>
      <div class="footer-col">
        <h4>Company</h4>
        <a href="/about">About Us</a>
        <a href="/proof/certificate-samples">Certificates</a>
        <a href="/compliance/kerala-pcb-authorization">KSPCB Auth</a>
        <a href="/guides/how-to-choose-ewaste-recycler-kochi">Why Us</a>
        <a href="/contact">Contact</a>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 EWaste Kochi. All rights reserved. KSPCB Auth: KSPCB/EW/2022/EK-047</span>
      <span>Serving Kochi, Ernakulam & Kerala since 2019</span>
    </div>
  </div>
</footer>

</body>
</html>"""
    return html


def generate_content(h1, meta_desc, primary_kw, location, slug, 
                      is_data, is_trading, is_recycling, is_collection, is_guide, 
                      device, brand, industry):
    
    blocks = f"""
    <h2>Complete Guide: {h1}</h2>
    
    <div class="card">
      <h3>🔒 Why Certified {primary_kw.title()} Matters in {location}</h3>
      <p>When it comes to <strong>{primary_kw}</strong> in {location}, choosing a KSPCB-authorised recycler is a legal requirement under the E-Waste Management Rules 2022. Businesses that use uncertified vendors risk E-Waste Rule penalties of up to ₹70/kg from CPCB, DPDP Act 2023 data breach liability of up to ₹250 crore, and ESG reporting gaps that affect investor trust.</p>
      <p>EWaste Kochi is the only certified <strong>{primary_kw}</strong> provider in {location} that offers all three compliance pillars simultaneously: environmental (KSPCB/CPCB), data security (NIST 800-88), and financial reporting (EPR credits for ESG/BRSR). Every job, regardless of size, receives a legally-valid Certificate of Destruction accepted by statutory auditors.</p>
    </div>

    <div class="card-grid">
      <div class="icon-card">
        <span class="icon">🏛️</span>
        <h4>KSPCB Authorised</h4>
        <p>Full Kerala State Pollution Control Board authorisation under E-Waste Rules 2022, Ref: KSPCB/EW/2022/EK-047.</p>
      </div>
      <div class="icon-card">
        <span class="icon">🔐</span>
        <h4>NIST 800-88 Certified</h4>
        <p>NIST SP 800-88 Rev.1 compliant data sanitisation — Clear, Purge, or Destroy level as required.</p>
      </div>
      <div class="icon-card">
        <span class="icon">📄</span>
        <h4>Certificate of Destruction</h4>
        <p>Legally-valid CoD with device serial numbers, destruction method, technician ID. Issued within 24 hours.</p>
      </div>
      <div class="icon-card">
        <span class="icon">🌿</span>
        <h4>Zero Landfill</h4>
        <p>100% of materials recycled through certified streams. Gold, silver, copper recovered for India's manufacturing chain.</p>
      </div>
      <div class="icon-card">
        <span class="icon">🚚</span>
        <h4>Free Corporate Pickup</h4>
        <p>Free GPS-tracked collection for 10+ devices anywhere in Ernakulam district. Same-day for bookings before 12 PM.</p>
      </div>
      <div class="icon-card">
        <span class="icon">⚖️</span>
        <h4>DPDP Act 2023 Ready</h4>
        <p>Our Certificate of Destruction is specifically designed to satisfy India's DPDP Act 2023 data disposal obligations.</p>
      </div>
    </div>

    <div class="card">
      <h3>📋 DPDP Act 2023 & {primary_kw.title()} Compliance in {location}</h3>
      <p>India's Digital Personal Data Protection Act 2023 mandates that all data fiduciaries maintain <strong>'reasonable security safeguards'</strong> through the entire data lifecycle — including disposal. For <strong>{primary_kw}</strong> in {location}, this means every storage device must receive NIST 800-88-level sanitisation with a Certificate of Destruction listing device serial numbers, the destruction method applied, and the date of processing.</p>
      <p>Non-compliance risks under DPDP Act 2023 include penalties up to ₹250 crore for personal data breaches from disposed hardware, plus IT Act 2000 Section 43A liability for corporate data exposure. EWaste Kochi's certificates are specifically formatted to satisfy DPDP Act requirements and are accepted by Big 4 audit firms operating in Kerala.</p>
    </div>

    <div class="card">
      <h3>🌍 Environmental Impact of {primary_kw.title()} in {location}</h3>
      <p>Every tonne of electronics processed through certified recycling instead of informal channels prevents approximately <strong>4.2 tonnes of CO₂ equivalent</strong>, 2.4kg of lead, and 180g of mercury from entering Kerala's ecosystem. Our KSPCB facility achieves greater than 95% material recovery.</p>
      <p>Precious metals recovered from your devices — typically 300–400g of gold, 2–4kg of silver, and 150–200kg of copper per tonne of PCBs — re-enter India's manufacturing supply chain. This supports the circular economy goals under India's National Resource Efficiency Policy and contributes directly to your organisation's ESG metrics for GRI Standards, SEBI BRSR, and CDP Climate disclosures.</p>
    </div>

    <h2 style="margin-top:32px">Comparison: EWaste Kochi vs Other Options</h2>
    <table>
      <thead>
        <tr>
          <th>Factor</th>
          <th>EWaste Kochi</th>
          <th>Local Kabadiwalla</th>
          <th>Cashify / OLX</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>KSPCB Authorisation</td>
          <td><strong class="check">✓ Yes</strong></td>
          <td class="cross">✗ No</td>
          <td class="cross">✗ No</td>
        </tr>
        <tr>
          <td>Data Destruction</td>
          <td><strong class="check">✓ NIST 800-88</strong></td>
          <td class="cross">✗ None</td>
          <td><span style="color:#f59e0b">⚠ Basic wipe only</span></td>
        </tr>
        <tr>
          <td>Certificate of Destruction</td>
          <td><strong class="check">✓ Legally valid</strong></td>
          <td class="cross">✗ No</td>
          <td class="cross">✗ No</td>
        </tr>
        <tr>
          <td>EPR Credits Issued</td>
          <td><strong class="check">✓ Yes, CPCB portal</strong></td>
          <td class="cross">✗ No</td>
          <td class="cross">✗ No</td>
        </tr>
        <tr>
          <td>Zero Landfill Guarantee</td>
          <td><strong class="check">✓ 100%</strong></td>
          <td class="cross">✗ Unknown</td>
          <td class="cross">✗ Unknown</td>
        </tr>
        <tr>
          <td>DPDP Act 2023 Compliant</td>
          <td><strong class="check">✓ Yes</strong></td>
          <td class="cross">✗ No</td>
          <td class="cross">✗ No</td>
        </tr>
      </tbody>
    </table>
    """
    return blocks


def generate_faqs(h1, primary_kw, location, is_data, is_trading):
    faqs = f"""
    <details class="faq-item">
      <summary class="faq-q">Is EWaste Kochi KSPCB authorised for {primary_kw} in {location}?</summary>
      <div class="faq-a">Yes. EWaste Kochi holds current KSPCB authorisation under E-Waste Management Rules 2022, reference number KSPCB/EW/2022/EK-047. We are registered with CPCB as both a dismantler and recycler for all 21 notified e-waste categories. Our authorisation certificate is available for download from our Certifications page. This covers the full spectrum of {primary_kw} activities at our Thrippunithura, Kochi facility.</div>
    </details>
    <details class="faq-item">
      <summary class="faq-q">How quickly can you collect from our {location} premises?</summary>
      <div class="faq-a">For standard pickups in Ernakulam district (Kakkanad, Edappally, Palarivattom, Vyttila, Aluva, Kalamassery, Thrikkakara), we offer same-day pickup for bookings confirmed before 12:00 PM on weekdays. For volumes above 50 devices, a dedicated vehicle is dispatched within 24–48 hours. Emergency service is available at ₹999 surcharge on weekdays and ₹1,499 on weekends — waived for bulk orders above 100 drives. WhatsApp +91 75005 55454 for instant confirmation.</div>
    </details>
    <details class="faq-item">
      <summary class="faq-q">What documentation do I receive for {primary_kw}?</summary>
      <div class="faq-a">You receive a legally-valid Certificate of Destruction (CoD) for every job. The CoD includes: your company name and GST number, device descriptions with individual serial numbers, quantity processed, NIST 800-88 destruction method applied, technician name and ID, date and location, and our KSPCB authorisation reference. The document is digitally signed and accepted by statutory auditors as evidence of DPDP Act 2023 compliance and RBI/SEBI cybersecurity circular adherence.</div>
    </details>
    <details class="faq-item">
      <summary class="faq-q">Do you serve locations in {location} outside the main city?</summary>
      <div class="faq-a">Yes. Our pickup service covers the full Ernakulam district including Aluva, Perumbavoor, Angamaly, North Paravur, Moovattupuzha, Kothamangalam, Piravom, and Muvattupuzha. For locations beyond 40km from our Thrippunithura facility, a logistics fee applies starting at ₹999. We also serve Thrissur, Alappuzha and Idukki districts on a scheduled route basis.</div>
    </details>
    <details class="faq-item">
      <summary class="faq-q">What is the minimum volume for free corporate pickup in {location}?</summary>
      <div class="faq-a">Free corporate pickup applies to 10 or more devices of any type — laptops, desktops, monitors, servers, printers, phones, tablets, routers, or UPS units — located anywhere within the Ernakulam district. For fewer than 10 devices, a ₹299 logistics fee applies for locations within 15km of our facility. Schools, NGOs, government bodies and hospitals receive free service with no minimum volume as part of our community programme.</div>
    </details>
    <details class="faq-item">
      <summary class="faq-q">Can you provide on-site data destruction at our {location} office?</summary>
      <div class="faq-a">Yes. We deploy mobile data destruction units to client premises across Kochi and Ernakulam. Our mobile service includes a degaussing unit (60+ drives/hour) and a portable hard drive shredder. The destruction process is video-recorded and a witnessed destruction log is counter-signed by your IT manager. Drives never leave your premises with data intact. Mobile on-site shredding starts at ₹150/drive for HDD and ₹200/drive for SSD, with significant volume discounts for Infopark, SmartCity, KINFRA and business parks.</div>
    </details>
    <details class="faq-item">
      <summary class="faq-q">What are the legal penalties for improper {primary_kw} in Kerala?</summary>
      <div class="faq-a">Under E-Waste Management Rules 2022, improper disposal carries penalties enforced by KSPCB via Environmental Compensation. Additionally: EPR non-compliance attracts ₹70/kg penalty from CPCB; DPDP Act 2023 data breaches from disposed devices carry penalties up to ₹250 crore; IT Act 2000 Section 43A applies for corporate data breaches from discarded hardware. Bulk consumers (offices with 50+ employees) face targeted enforcement inspections. Using a certified recycler with documented pickup and CoD is the only complete defence against all these risk vectors.</div>
    </details>
    <details class="faq-item">
      <summary class="faq-q">Do you offer EPR compliance credits through your service?</summary>
      <div class="faq-a">Yes. EWaste Kochi is a CPCB-registered recycler empanelled with multiple Producer Responsibility Organisations (PROs) active in Kerala. When you route e-waste through our network, we upload weight-verified records to the CPCB EPMS portal. Your brand or PRO receives digitally-signed EPR credit certificates within 5 business days, counting towards your annual CPCB collection target. This avoids the ₹70/kg EPR shortfall penalty.</div>
    </details>
    """
    return faqs


# ─── PAGE GENERATION FUNCTIONS ────────────────────────────────

def write_page(folder, slug, h1, meta_desc, primary_kw, cat_label,
               lat="9.9312", lng="76.2673", location="Kochi", 
               device="", brand="", industry=""):
    out_dir = os.path.join(BASE, folder)
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"{slug}.html")
    canonical = f"{SITE}/{folder}/{slug}"
    
    html = make_page(folder, slug, h1, meta_desc, primary_kw, canonical, cat_label,
                     lat, lng, location, "service", device, brand, industry)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    return canonical

CAT_LABELS = {
    "locations": "Kochi Locations",
    "data-security": "Data Security & ITAD",
    "recycling": "E-Waste Recycling",
    "collection": "E-Waste Collection",
    "disposal": "E-Waste Disposal",
    "trading": "Buy & Sell Electronics",
    "buyback": "Device Buyback",
    "industries": "Industries We Serve",
    "guides": "Expert Guides",
    "compliance": "Compliance",
    "general-waste": "Waste Management",
    "comparisons": "Comparisons",
}

ALL_URLS = []

def gen():
    total = 0
    
    print("🔨 Generating intent/keyword pages...")
    for slug, folder, h1, meta_desc, primary_kw in INTENT_PAGES:
        cat = CAT_LABELS.get(folder, folder.title())
        u = write_page(folder, slug, h1, meta_desc, primary_kw, cat)
        ALL_URLS.append((u, folder))
        total += 1
    print(f"  ✓ {total} intent pages")

    print("🔨 Generating location × service matrix...")
    loc_count = 0
    for loc_slug, loc_name, lat, lng in LOCATIONS:
        for svc in SERVICES[:10]:  # top 10 services per location
            slug = f"{svc}-{loc_slug}"
            svc_label = svc.replace("-"," ").title()
            h1 = f"{svc_label} {loc_name} | KSPCB Certified 2026"
            meta_desc = f"Certified {svc_label.lower()} in {loc_name}. KSPCB authorised, NIST data destruction, free corporate pickup. Certificate of Destruction issued."
            u = write_page("locations", slug, h1, meta_desc, f"{svc_label} {loc_name}", "Kochi Locations",
                           lat, lng, loc_name)
            ALL_URLS.append((u, "locations"))
            loc_count += 1
    total += loc_count
    print(f"  ✓ {loc_count} location×service pages")

    print("🔨 Generating device recycling pages...")
    dev_count = 0
    for dev_slug, dev_singular, dev_plural, dev_label in DEVICES:
        # Generic device recycling
        slug = f"recycle-{dev_slug}-kochi"
        h1 = f"Recycle {dev_label} Kochi | Certified Disposal 2026"
        meta_desc = f"Recycle your old {dev_singular} in Kochi. KSPCB certified, NIST data destruction, free pickup for 10+ units. Certificate of Destruction issued."
        u = write_page("recycling", slug, h1, meta_desc, f"{dev_label} recycling Kochi", "E-Waste Recycling",
                        device=dev_singular)
        ALL_URLS.append((u, "recycling"))
        dev_count += 1
        
        # Device disposal
        slug2 = f"dispose-{dev_slug}-kochi"
        h1_2 = f"Dispose {dev_label} Kochi | Certified E-Waste Disposal"
        meta_desc2 = f"Safe disposal of {dev_plural} in Kochi. KSPCB authorised, NIST data wipe, free corporate collection. Certificate of Destruction."
        u2 = write_page("disposal", slug2, h1_2, meta_desc2, f"{dev_label} disposal Kochi", "E-Waste Disposal",
                         device=dev_singular)
        ALL_URLS.append((u2, "disposal"))
        dev_count += 1
        
        # Device pickup
        slug3 = f"{dev_slug}-pickup-kochi"
        h1_3 = f"{dev_label} Pickup Kochi | Free Collection Service"
        meta_desc3 = f"Free {dev_singular} pickup in Kochi. Schedule your {dev_label} collection in 60 seconds. KSPCB certified, data destruction included."
        u3 = write_page("collection", slug3, h1_3, meta_desc3, f"{dev_label} pickup Kochi", "E-Waste Collection",
                         device=dev_singular)
        ALL_URLS.append((u3, "collection"))
        dev_count += 1

    total += dev_count
    print(f"  ✓ {dev_count} device pages")

    print("🔨 Generating brand × device pages...")
    brand_count = 0
    for b_slug, b_name in BRANDS[:12]:
        for dev_slug, dev_singular, dev_plural, dev_label in DEVICES[:15]:
            slug = f"recycle-{b_slug}-{dev_slug}-kochi"
            h1 = f"Recycle {b_name} {dev_label} Kochi | Certified Buyback"
            meta_desc = f"Recycle your {b_name} {dev_singular} in Kochi. NIST data wipe, buyback available, free pickup for bulk. KSPCB certified disposal."
            u = write_page("recycling", slug, h1, meta_desc, f"{b_name} {dev_label} recycling Kochi", "E-Waste Recycling",
                            device=dev_singular, brand=b_name)
            ALL_URLS.append((u, "recycling"))
            brand_count += 1
            
            # Sell brand device
            slug2 = f"sell-{b_slug}-{dev_slug}-kochi"
            h1_2 = f"Sell {b_name} {dev_label} Kochi | Best Price Instant Payment"
            meta_desc2 = f"Sell your {b_name} {dev_singular} in Kochi. Best price guaranteed, instant payment, free pickup. Any condition — working or broken."
            u2 = write_page("trading", slug2, h1_2, meta_desc2, f"sell {b_name} {dev_label} Kochi", "Buy & Sell Electronics",
                             device=dev_singular, brand=b_name)
            ALL_URLS.append((u2, "trading"))
            brand_count += 1

    total += brand_count
    print(f"  ✓ {brand_count} brand×device pages")

    print("🔨 Generating industry pages...")
    ind_count = 0
    for ind_slug, ind_singular, ind_plural, ind_sector in INDUSTRIES:
        # Main industry page
        slug = f"ewaste-{ind_slug}-kochi"
        h1 = f"E-Waste Recycling for {ind_singular}s Kochi | {ind_sector} Certified"
        meta_desc = f"Certified e-waste disposal for {ind_plural} in Kochi. KSPCB authorised, NIST data destruction, EPR compliance. Free service for qualifying institutions."
        u = write_page("industries", slug, h1, meta_desc, f"{ind_sector} e-waste Kochi", "Industries We Serve",
                        industry=ind_singular)
        ALL_URLS.append((u, "industries"))
        ind_count += 1
        
        # Data destruction for industry
        slug2 = f"data-destruction-{ind_slug}-kochi"
        h1_2 = f"Data Destruction for {ind_singular}s Kochi | Compliance Certified"
        meta_desc2 = f"Certified data destruction for {ind_plural} in Kochi. NIST 800-88, DPDP Act 2023 compliant, Certificate of Destruction. Meets {ind_sector} regulatory requirements."
        u2 = write_page("data-security", slug2, h1_2, meta_desc2, f"{ind_sector} data destruction Kochi", "Data Security & ITAD",
                         industry=ind_singular)
        ALL_URLS.append((u2, "data-security"))
        ind_count += 1
        
        # Industry × Location pages (top 5 locations)
        for loc_slug, loc_name, lat, lng in LOCATIONS[:5]:
            slug3 = f"ewaste-{ind_slug}-{loc_slug}"
            h1_3 = f"E-Waste for {ind_singular}s {loc_name} | {ind_sector} Certified"
            meta_desc3 = f"Certified e-waste disposal for {ind_plural} in {loc_name}. KSPCB authorised, free pickup, NIST data destruction."
            u3 = write_page("industries", slug3, h1_3, meta_desc3, f"{ind_sector} e-waste {loc_name}", "Industries We Serve",
                             lat, lng, loc_name, industry=ind_singular)
            ALL_URLS.append((u3, "industries"))
            ind_count += 1

    total += ind_count
    print(f"  ✓ {ind_count} industry pages")

    print("🔨 Generating pincode location pages...")
    pin_count = 0
    for pin in range(682001, 682260):
        slug = f"ewaste-{pin}"
        h1 = f"E-Waste Recycling {pin} | Certified Kochi Pincode Service"
        meta_desc = f"E-waste recycling for pincode {pin}, Kochi. KSPCB certified, free corporate pickup, NIST data destruction. Book via WhatsApp."
        u = write_page("locations", slug, h1, meta_desc, f"e-waste {pin} Kochi", "Kochi Locations")
        ALL_URLS.append((u, "locations"))
        pin_count += 1
    total += pin_count
    print(f"  ✓ {pin_count} pincode pages")

    print("🔨 Generating data security deep-dive pages...")
    ds_pages = [
        ("what-is-data-destruction", "What Is Data Destruction? | Complete Guide India 2026",
         "Complete guide to data destruction in India. NIST 800-88 methods, DPDP Act 2023 requirements, certified providers in Kochi.",
         "what is data destruction"),
        ("nist-800-88-methods-explained", "NIST 800-88 Data Destruction Methods | India Guide 2026",
         "NIST SP 800-88 Rev.1 Clear, Purge, Destroy explained. Which method for HDD, SSD, USB? India DPDP Act implications.",
         "NIST 800-88 data destruction"),
        ("dpdp-act-2023-data-disposal-obligations", "DPDP Act 2023 Data Disposal Obligations | Kerala Business",
         "Your DPDP Act 2023 obligations for IT asset disposal in Kerala. Certified destruction requirements, penalties, compliance guide.",
         "DPDP Act 2023 data disposal"),
        ("hard-drive-shredding-vs-wiping", "Hard Drive Shredding vs Wiping | Which Is More Secure?",
         "Hard drive shredding vs data wiping — which is more secure? NIST standards, legal requirements, and when to use each method.",
         "hard drive shredding vs wiping"),
        ("ssd-data-destruction-guide", "SSD Data Destruction Guide | Why Wiping Isn't Enough",
         "SSD data destruction guide. Why ATA Secure Erase fails for SSDs. NIST 800-88 Destroy-level physical shredding explained.",
         "SSD data destruction"),
        ("certificate-of-destruction-template", "Certificate of Destruction Template | DPDP Act Compliant",
         "What should a Certificate of Destruction contain for DPDP Act 2023 compliance? Template, required fields, and legal validity.",
         "certificate of destruction"),
        ("on-site-vs-offsite-data-destruction", "On-Site vs Off-Site Data Destruction Kochi | Comparison",
         "Compare on-site vs off-site data destruction in Kochi. Cost, security, compliance considerations for your business.",
         "on-site data destruction"),
        ("epr-compliance-kochi-guide", "EPR Compliance Kochi | Extended Producer Responsibility Guide",
         "Complete EPR compliance guide for Kochi businesses. CPCB registration, credit system, penalties, certified recyclers.",
         "EPR compliance kochi"),
        ("e-waste-audit-checklist-kerala", "E-Waste Audit Checklist Kerala | Corporate IT Assets 2026",
         "Complete e-waste audit checklist for Kerala businesses. IT asset inventory, data destruction verification, EPR credits.",
         "e-waste audit checklist"),
        ("iso-14001-environmental-compliance", "ISO 14001 E-Waste Compliance Kochi | Green Certification",
         "ISO 14001 aligned e-waste disposal for Kochi businesses. Environmental management system integration, KSPCB alignment.",
         "ISO 14001 e-waste"),
        ("brsr-ewaste-reporting-kochi", "BRSR E-Waste Reporting Kochi | SEBI Mandatory Disclosure",
         "SEBI BRSR mandatory e-waste disclosure for Kochi listed companies. Weight metrics, EPR data, CO2 avoided for annual report.",
         "BRSR e-waste reporting"),
        ("r2v3-certified-recycling-guide", "R2v3 Certified Recycling Guide India | What It Means",
         "R2v3 certification explained for India. How it relates to KSPCB authorisation, responsible recycling, and vendor selection.",
         "R2v3 certification"),
        ("corporate-itad-programme-kochi", "Corporate ITAD Programme Kochi | End-to-End IT Lifecycle",
         "Complete corporate ITAD programme for Kochi businesses. Asset inventory, data destruction, recycling, reporting in one service.",
         "corporate ITAD"),
        ("ewaste-carbon-footprint-guide", "E-Waste Carbon Footprint Guide | CO2 Calculations India",
         "Calculate e-waste carbon savings in India. GHG emission factors, CO2 avoided calculations, ESG reporting methodology.",
         "e-waste carbon footprint"),
        ("data-center-decommission-checklist", "Data Center Decommissioning Checklist Kochi | 2026 Guide",
         "Complete data center decommissioning checklist for Kochi. Data destruction, asset recovery, compliance documentation.",
         "data center decommissioning"),
    ]
    ds_count = 0
    for slug, h1, meta_desc, primary_kw in ds_pages:
        u = write_page("data-security", slug, h1, meta_desc, primary_kw, "Data Security & ITAD")
        ALL_URLS.append((u, "data-security"))
        ds_count += 1
    total += ds_count
    print(f"  ✓ {ds_count} data security deep-dive pages")

    print(f"\n✅ Total pages generated: {total}")
    return total

if __name__ == "__main__":
    os.makedirs(BASE, exist_ok=True)
    total = gen()
    
    # Write URL list
    with open(os.path.join(BASE, "_all_urls.txt"), "w") as f:
        for url, folder in ALL_URLS:
            f.write(url + "\n")
    
    print(f"\n📊 Stats:")
    from collections import Counter
    folder_counts = Counter(folder for _, folder in ALL_URLS)
    for folder, count in sorted(folder_counts.items(), key=lambda x: -x[1]):
        print(f"  {folder}: {count}")
    
    print(f"\n✅ All done! {len(ALL_URLS)} pages ready.")
