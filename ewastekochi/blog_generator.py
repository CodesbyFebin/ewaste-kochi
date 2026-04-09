import os
import random

# CONFIG
OUTPUT_DIR = "/media/hp-ml10/Projects/ewastekochi-production/ewastekochi/blog/"
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

CATEGORIES = ["ITAD", "Recycling", "Security", "Compliance", "Sustainability", "Electronic Waste", "Corporate Services", "Kochi Locals", "Legal Guide", "Buyback Guide"]

TOPICS = [
    "How to dispose of {item} in {area}",
    "Benefits of {service} for businesses in {area}",
    "Why {area} companies need certified {service}",
    "{item} recycling guide for residents of {area}",
    "Top 10 {service} providers in Kochi including {area}",
    "DPDP Act compliance for {item} in {area}",
    "Physical shredding vs degaussing in {area}",
    "Where to sell old {item} for cash in {area}",
    "Environmentally friendly {item} disposal in {area}",
    "Legal requirements for {service} in Kochi's {area}"
]

ITEMS = ["Laptops", "Desktops", "Servers", "iPhones", "MacBooks", "Printers", "Monitors", "Hard Drives", "SSDs", "Networking Gear", "Cables", "Keyboards"]
SERVICES = ["IT Asset Disposal", "Data Destruction", "E-Waste Recycling", "Hard Drive Shredding", "Corporate Buyback", "Office Clearance", "Certificate of Destruction"]
AREAS = ["Kakkanad", "Edapally", "Aluva", "Vyttila", "Palarivattom", "Kaloor", "Marine Drive", "Fort Kochi", "Angamaly", "Perumbavoor", "Kalamassery", "Maradu", "Kadavanthra", "Thrippunithura", "Eloor", "Cheranallur", "Nedumbassery", "Cusat", "Infopark", "SmartCity"]

TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | Kochi Authority Blog</title>
<meta name="description" content="Expert guide on {title}. Learn how EWaste Kochi handles e-waste and data security for organizations in Kerala.">
<link rel="stylesheet" href="/css/style.css">
<style>
    body {{ background: #0a0f0c; color: #9bb8a2; font-family: 'Outfit', sans-serif; line-height: 1.8; }}
    .wrap {{ max-width: 800px; margin: 0 auto; padding: 60px 24px; }}
    h1 {{ color: #fff; font-family: 'Bebas Neue'; font-size: 3.5rem; line-height: 1.1; margin-bottom: 20px; }}
    h2 {{ color: #00e664; margin-top: 40px; }}
    .meta {{ font-size: 0.8rem; color: #5a7a62; margin-bottom: 40px; text-transform: uppercase; letter-spacing: 1px; }}
    .cta-box {{ background: #111a14; border: 1px solid #00e664; padding: 30px; border-radius: 15px; margin-top: 50px; text-align: center; }}
    .btn {{ display: inline-block; padding: 12px 30px; background: #00e664; color: #000; font-weight: 800; border-radius: 8px; text-decoration: none; margin-top: 20px; }}
</style>
</head>
<body>
    <div class="wrap">
        <div class="meta">Category: {category} | Updated: March 2026</div>
        <h1>{title}</h1>
        <p>In the heart of Kochi, specifically within the bustling area of {area}, managing electronic assets is becoming a top priority for both residents and enterprises. Whether you are dealing with {item.lower()} or looking for comprehensive {service.lower()}, understanding the local landscape is key.</p>
        
        <h2>The Importance of Professional {service}</h2>
        <p>Many organizations in {area} still rely on informal scrap dealers for their {item.lower()} disposal. However, this poses significant risks under the DPDP Act 2023. Certified {service.lower()} ensures that your data is destroyed according to NIST 800-88 standards, providing you with a court-admissible Certificate of Destruction.</p>
        
        <h2>Why {area} is Leading in Tech Recycling</h2>
        <p>With hubs like Infopark and SmartCity nearby, {area} has become a center for technological innovation. This growth comes with the responsibility of handling e-waste correctly. At EWaste Kochi, we offer specialized pickup services for {area}, ensuring that {item.lower()} are processed in a 100% eco-friendly manner.</p>
        
        <div class="cta-box">
            <h3>Need Help with {item} in {area}?</h3>
            <p>Our team is available 24/7 for corporate e-waste consultations.</p>
            <a href="https://wa.me/919876543210" class="btn">Chat on WhatsApp</a>
        </div>
    </div>
</body>
</html>
"""

def generate_500_blogs():
    count = 0
    while count < 510:
        area = random.choice(AREAS)
        item = random.choice(ITEMS)
        service = random.choice(SERVICES)
        category = random.choice(CATEGORIES)
        stem = random.choice(TOPICS)
        
        title = stem.format(area=area, item=item, service=service)
        slug = title.lower().replace(" ", "-").replace("?", "").replace(".", "").replace(",", "")
        
        html = TEMPLATE.format(
            title=title,
            area=area,
            item=item,
            service=service,
            category=category
        )
        
        with open(os.path.join(OUTPUT_DIR, f"{slug}.html"), "w", encoding="utf-8") as f:
            f.write(html)
        
        count += 1
        if count % 100 == 0:
            print(f"Generated {count} blogs...")

    print(f"✅ Blog Generator: {count} pages created in {OUTPUT_DIR}")

if __name__ == "__main__":
    generate_500_blogs()
