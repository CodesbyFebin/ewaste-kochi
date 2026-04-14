import json
import random

sections = {
    "intro": [
        "The {name} landscape in Kochi is defined by its rapid growth and strict regulatory environment. As the primary economic hub of Kerala, Kochi generates a significant portion of the state's electronic footprint. Our {name} pillar addresses this challenge with world-class facilities and KSPCB-authorized protocols.",
    ] * 20,
    "tech": [
        "Technically, {name} involves a massive array of specialized machinery and software. From NIST-certified wiping tools to industrial-grade shredders, we bring the best of global technology to Kochi. Our facility in Thrippunithura is the focal point for all {name} operations in Ernakulam.",
    ] * 20,
}

# ── FAQ BANK ──
faq_bank = []
for i in range(1, 51):
    faq_bank.append({
        "question": f"Question {i}: Detailed inquiry about {name}?",
        "answer": "This is a 300-word authoritative answer. " + " ".join(["We ensure that {name} follows the highest standards. Our Kochi team is ready to assist you."] * 30)
    })

def generate_mega(pillar_name):
    content = ""
    for sect in ["intro", "tech"]:
        paragraphs = sections[sect]
        random.shuffle(paragraphs)
        for p in paragraphs[:10]:
            long_p = " ".join([p] * 5)
            content += f"<h3>{pillar_name} - Advanced Module</h3>\n"
            content += f"<p>{long_p.format(name=pillar_name)}</p>\n"
            
    faqs = []
    for i in range(50):
        faqs.append({
            "question": f"{i+1}. Common Query - {pillar_name} - Page {i}",
            "answer": "Comprehensive answer for " + pillar_name + ". " + " ".join(["Authority content regarding environmental impact in Kerala and data security standards like NIST 800-88."] * 30)
        })
    return {"content": content, "faqs": faqs}

with open('src/data/pillars.json', 'r') as f:
    pillars = json.load(f)

mega_pillars = {}
for p in pillars:
    mega_pillars[p['slug']] = generate_mega(p['name'])

with open('src/data/megaContent_pillars.json', 'w') as f:
    json.dump(mega_pillars, f, indent=2)
