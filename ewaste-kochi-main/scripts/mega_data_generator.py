import json
import random
import os
import re

p_bank = [
    "The electronic waste management sector in {location} is currently undergoing a paradigm shift towards sustainable practices.",
    "Data security in {location} is more critical than ever before. Every IT manager in {district} must ensure compliance.",
    "Logistical efficiency in {location} allows for same-day pickup for bulk collections.",
    "The circular economy is our operational reality in {location}. We recover precious metals like gold collected in {location}.",
    "In the heart of {location}, technology adoption makes the need for professional {service} pressing.",
] * 40

faq_q_bank = [
    "Why is {service} essential for businesses in {location}?",
    "How does EWaste Kochi ensure data security for {service} in {district}?",
    "What are the KSPCB regulations for {location} regarding e-waste?",
] * 35

def generate_mega_content(loc, svc):
    content = ""
    chosen_p = random.sample(p_bank, 8) # Reduced paragraphs to keep JSON sizes sane
    for p in chosen_p:
        long_p = " ".join([p] * 3)
        content += f"<h3>{svc['name']} Analysis in {loc['name']}</h3>\n"
        content += f"<p>{long_p.format(location=loc['name'], district=loc['district'], service=svc['name'])}</p>\n"
    faqs = []
    for i in range(25): # Reduced FAQs to 25 to help build speed and size
        q = faq_q_bank[i % len(faq_q_bank)].format(location=loc['name'], service=svc['name'], district=loc['district'])
        ans = "Professional {service} management in {location} involves NIST 800-88 and KSPCB protocols. ".format(location=loc['name'], service=svc['name']) + " ".join(["Zero-landfill in {location}.".format(location=loc['name'])] * 15)
        faqs.append({"question": f"{i+1}. {q}", "answer": ans})
    return {"content": content, "faqs": faqs}

with open('src/data/locations.js', 'r') as f:
    loc_js = f.read()
loc_slugs = re.findall(r"['\"]?slug['\"]?:\s*['\"]([^'\"]+)['\"]", loc_js)
loc_names = re.findall(r"['\"]?name['\"]?:\s*['\"]([^'\"]+)['\"]", loc_js)
loc_districts = re.findall(r"['\"]?district['\"]?:\s*['\"]([^'\"]+)['\"]", loc_js)

locations_data = []
for i in range(len(loc_slugs)):
    locations_data.append({"slug": loc_slugs[i], "name": loc_names[i], "district": loc_districts[i]})

with open('src/data/services.js', 'r') as f:
    svc_js = f.read()
svc_slugs = re.findall(r"['\"]?slug['\"]?:\s*['\"]([^'\"]+)['\"]", svc_js)
svc_names = re.findall(r"['\"]?name['\"]?:\s*['\"]([^'\"]+)['\"]", svc_js)

services_data = []
for i in range(len(svc_slugs)):
    services_data.append({"slug": svc_slugs[i], "name": svc_names[i]})

all_keys = []
for loc in locations_data:
    for svc in services_data:
        all_keys.append((loc, svc))

num_parts = 12
part_size = len(all_keys) // num_parts + 1
for i in range(num_parts):
    part_keys = all_keys[i*part_size : (i+1)*part_size]
    mega_data = {}
    for loc, svc in part_keys:
        key = f"{loc['slug']}-{svc['slug']}"
        mega_data[key] = generate_mega_content(loc, svc)
    with open(f'src/data/megaContent_part{i+1}.json', 'w') as f:
        json.dump(mega_data, f, indent=2)

print(f"Generated {len(all_keys)} pages content across {num_parts} parts.")
