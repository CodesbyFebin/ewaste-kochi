import os

# Config
BASE_DIR = "/media/hp-ml10/Projects/EwasteKochi.com"
NODES = [
    ("buyback/sell-water-damaged-macbook-kochi.html", "Sell Water Damaged MacBook Kochi", "We buy water-damaged and dead MacBooks for the highest part-out value in Kerala."),
    ("buyback/sell-dead-iphone-kochi.html", "Sell Dead iPhone Kochi", "Highest cash price for dead iPhones in Kochi. Professional data destruction included."),
    ("buyback/sell-broken-laptop-kochi.html", "Sell Broken Screen Laptop Kochi", "Get instant cash for laptops with broken screens or damaged chassis in Ernakulam."),
    ("itad/services/sell-ups-batteries-kochi.html", "Bulk UPS Battery Recycling Kochi", "Certified disposal for industrial lead-acid and lithium-ion batteries in Kochi."),
    ("itad/services/sell-server-racks-kochi.html", "Server Rack & IT Cabinet Disposal", "Full removal of server racks, PDU, and cabinet infrastructure from Kochi data centers."),
    ("itad/services/networking-cables-scrap.html", "Networking Cable & Wire Scrap Buyer", "Bulk recycling of Cat6, Fiber Optic, and Power cables for Infopark businesses."),
    ("locations/ewaste-thrissur.html", "E-Waste Recycling Thrissur", "Professional E-waste collection and data destruction services now in Thrissur district."),
    ("locations/ewaste-kottayam.html", "E-Waste Recycling Kottayam", "Authorized ITAD and device buyback for businesses and homes in Kottayam."),
    ("compliance/how-to-get-itad-certificate.html", "How to Get ITAD Certificate Kerala", "The definitive guide to obtaining legally binding Electronic Waste Destruction Certificates."),
    ("compliance/legal-status-scrap-dealers.html", "Legal Risks: Selling E-Waste to Scrap Dealers", "Understand why selling corporate IT assets to unauthorized scrap dealers violates DPDP Act 2023."),
    ("blog/is-it-legal-to-throw-batteries.html", "Is it Legal to Throw Batteries in Trash?", "The legal implications of battery disposal in Kerala and the risk of hazardous waste penalties."),
    ("blog/why-recycling-macbooks-is-hard.html", "Why Recycling MacBooks is Scientifically Harder", "Deep dive into the environmental impact of T2/M-series security chips in the ITAD lifecycle.")
]
# Expand to 20 via duplicates or variations
for i in range(len(NODES), 20):
    NODES.append((f"blog/tech-sustainability-tip-{i}.html", f"Tech Sustainability Tip #{i}", "Localized advice for Kochi residents on sustainable electronics management."))

TEMPLATE_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | EWasteKochi Power Node</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="{rel_path}assets/css/style.css">
<style>
:root{{--bg:#07100A;--white:#F0F7F2;--green:#00E87A;--surface:#162019}}
body{{background:var(--bg);color:var(--white);font-family:sans-serif;padding:60px 24px;line-height:1.6}}
.card{{background:var(--surface);padding:40px;border-radius:24px;border:1px solid rgba(0,232,122,.15);max-width:800px;margin:0 auto}}
.btn{{display:inline-block;padding:16px 32px;background:var(--green);color:var(--bg);border-radius:12px;text-decoration:none;font-weight:800}}
</style>
</head>
<body>
<div class="card">
  <h1>{title}</h1>
  <p>{desc}</p>
  <br>
  <p><strong>Compliance Note:</strong> All items processed under NIST 800-88 Degaussing standards. KSPCB Authorized Recycler.</p>
  <br>
  <a href="{rel_path}book-free-pickup-kochi.html" class="btn">🚀 Book Authorized Pickup →</a>
</div>
</body>
</html>
"""

def generate_nano_nodes():
    for filename, title, desc in NODES:
        depth = filename.count("/")
        rel_path = "../" * depth
        content = TEMPLATE_HTML.format(title=title, desc=desc, rel_path=rel_path)
        
        full_path = os.path.join(BASE_DIR, filename)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)

if __name__ == "__main__":
    generate_nano_nodes()
    print("🚀 20 Nano-SEO Nodes Generated!")
