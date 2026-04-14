import csv
import os

DATA_DIR = "/media/hp-ml10/Projects/EwasteKochi.com/automation/data"

PHONES = [("iPhone 15 Pro Max", "125000"), ("iPhone 15 Pro", "105000"), ("iPhone 15", "75000"), ("Samsung S24 Ultra", "95000")]
for i in range(15, 6, -1):
    PHONES.append((f"iPhone {i} Pro Max", str(i*6500)))
    PHONES.append((f"iPhone {i}", str(i*4500)))
    PHONES.append((f"Samsung Galaxy S{i} Ultra", str(i*4200)))
    PHONES.append((f"Samsung Galaxy A{i+10}", str(i*1500)))
    PHONES.append((f"Google Pixel {i} Pro", str(i*3500)))
    PHONES.append((f"OnePlus {i} Pro", str(i*3000)))
    PHONES.append((f"Nothing Phone {i%4+1}", str(i*2500)))
    PHONES.append((f"Xiaomi Redmi Note {i+5}", str(i*1200)))

LAPTOPS = [("MacBook Pro M3 Max", "295000"), ("MacBook Pro M3", "145000"), ("Dell XPS 17", "185000"), ("ThinkPad X1 Carbon Gen 12", "165000")]
for i in range(1, 101):
    LAPTOPS.append((f"ThinkPad T{400+i}s", str(25000+i*1100)))
    LAPTOPS.append((f"MacBook Air M{max(1, i%5)}", str(55000+i*1000)))
    LAPTOPS.append((f"Dell Latitude {5400+i}", str(35000+i*1000)))
    LAPTOPS.append((f"HP EliteBook {840+i}", str(45000+i*800)))
    LAPTOPS.append((f"Asus ROG Zephyrus G1{max(4, i%16)}", str(95000+i*2000)))

LOCATIONS = [
    "Kochi", "Ernakulam", "Kakkanad", "Infopark", "Vyttila", "Edappally", "Aluva", "Angamaly", "Thrippunithura",
    "Palarivattom", "Kaloor", "Marine Drive", "Fort Kochi", "Mattancherry", "Kalamassery", "Eloor",
    "North Paravur", "Perumbavoor", "Muvattupuzha", "Kothamangalam", "Tripunithura",
    "Maradu", "Nettoor", "Cheranallur", "Ambalamukku", "Infopark Phase 1", "Infopark Phase 2", "Smart City",
    "Ravipuram", "Kadavanthra", "Panampilly Nagar", "Thammanam", "Vazhakkala", "Poochakhal", "Aroor", "Eramalloor"
]
for p in range(682001, 682250): # 250+ pincodes
    LOCATIONS.append(str(p))

BLOG_TOPICS = [
    ("Why NIST 800-88 Data Destruction is Crucial in 2026", "Compliance"),
    ("Selling Your Dead MacBook Pro in Kochi: Best Prices", "Buyback"),
    ("DPDP Act 2023 Penalties: A Checklist for Kochi Businesses", "Legal"),
    ("Hard Drive Shredding Cost in Ernakulam: 2026 Price Guide", "Pricing")
]
for i in range(1, 201):
    BLOG_TOPICS.append((f"Best E-Waste Recycling Practices for Kerala Households #{i}", "Environment"))

def write_csv(filename, data, header):
    with open(os.path.join(DATA_DIR, filename), "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)

if __name__ == "__main__":
    write_csv("phones.csv", PHONES, ["Model", "Price"])
    write_csv("laptops.csv", LAPTOPS, ["Model", "Price"])
    write_csv("locations.csv", [[l] for l in LOCATIONS], ["Name"])
    write_csv("blog_topics.csv", BLOG_TOPICS, ["Title", "Category"])
    print(f"✅ Master Data Hub (800-Node DNA) finalized with {len(PHONES)+len(LAPTOPS)+len(LOCATIONS)+len(BLOG_TOPICS)} records.")
