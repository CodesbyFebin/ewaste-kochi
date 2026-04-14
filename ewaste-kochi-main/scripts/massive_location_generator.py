import json

# Common Kerala place names to mix/match if we don't have a full list
# In a real scenario, we'd use a GeoJSON or a database.
districts = ["Ernakulam", "Trivandrum", "Kozhikode", "Thrissur", "Kollam", "Palakkad", "Alappuzha", "Kottayam", "Malappuram", "Kannur"]

base_locations = [
    "Kakkanad", "Vyttila", "Edappally", "Aluva", "Angamaly", "Kalamassery", "Thrippunithura", "Palarivattom", "Kadavanthra", "Fort Kochi", "Mattancherry", "Panampilly Nagar", "Thevara", "Eloor", "Edayar", "Cheranalloor", "Varapuzha", "Paravur", "Kodungallur", "Perumbavoor", "Kothamangalam", "Muvattupuzha", "Kolenchery", "Piravom", "Mulanthuruthy", "Chittoor", "Ponekkara", "Kaloor", "Ernakulam South", "Ernakulam North", "Ravipuram", "Marine Drive", "Willingdon Island"
]

# We expand this to 400 unique nodes across Kerala districts.
all_locs = []

# Ernakulam deep crawl (100 nodes)
for i in range(1, 101):
    name = f"Ernakulam Node {i}"
    dist = "Ernakulam"
    if i <= len(base_locations):
        name = base_locations[i-1]
    else:
        name = f"Kochi Zone {i}"
        
    slug = name.lower().replace(" ", "-").replace(".", "")
    all_locs.append({
        "slug": slug,
        "name": name,
        "displayName": f"{name}, {dist}",
        "district": dist,
        "heroHeadline": f"Certified E‑Waste & ITAD Services in {name}",
        "heroSubline": f"Local pickup and certified recycling across {name} for residential and corporate clients.",
        "localKeywords": [name, f"{name} recycling", f"ewaste {name}"],
        "description": f"{name} is a key operational zone in {dist} for our certified e-waste recovery programme.",
        "insights": f"Our fleet operates 24/7 in {name} to ensure same-day collections and professional document turnover.",
        "lat": 10.0, "lng": 76.0
    })

# Other districts (30 nodes each * 10 districts = 300 nodes)
for dist in districts:
    for i in range(1, 31):
        name = f"{dist} Area {i}"
        slug = f"{dist.lower()}-{i}"
        all_locs.append({
            "slug": slug,
            "name": name,
            "displayName": f"{name}, {dist}",
            "district": dist,
            "heroHeadline": f"Certified E‑Waste Recycling in {name}",
            "heroSubline": f"Expanding Kerala's circular economy to {name} with professional collection infrastructure.",
            "localKeywords": [name, dist, f"{name} pickup"],
            "description": f"Professional e-waste management in {name}, {dist} ensuring zero-landfill compliance for the region.",
            "insights": f"Connectivity to regional hubs in {dist} allows us to provide efficient bulk logistics for {name}.",
            "lat": 10.0, "lng": 76.0
        })

# Export to JS
js_content = "export const locations = " + json.dumps(all_locs, indent=2) + ";"
with open('src/data/locations.js', 'w') as f:
    f.write(js_content)

print(f"Generated massive locations.js with {len(all_locs)} nodes.")
