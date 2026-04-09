import json
import os

# CONFIG
PILLAR_TOPICS = [
    "E-Waste Recycling Kochi",
    "IT Asset Disposal (ITAD) Kochi",
    "Data Destruction & Hard Drive Shredding",
    "Laptop Buyback & Recycling",
    "Corporate E-Waste Management",
    "Computer Disposal Kochi",
    "Electronics Scrap Buyer Kochi",
    "Mobile Phone Recycling",
    "Battery Recycling Kochi",
    "E-Waste Rules & Compliance Kerala"
]

def generate_faqs(topic):
    """Generate 200 relevant FAQs for a given topic."""
    faqs = []
    
    # Core FAQs (Specific to the topic)
    core_questions = [
        f"What is the process for {topic} in Kochi?",
        f"How much does {topic} cost for corporate clients?",
        f"Is {topic} compliant with KSPCB rules?",
        f"Do you provide a Certificate of Destruction for {topic}?",
        f"Which areas in Kochi do you cover for {topic}?",
        f"Is {topic} available for individual households?",
        f"What are the environmental benefits of {topic}?",
        f"How does EWaste Kochi ensure data security during {topic}?",
        f"How long does {topic} take to complete?",
        f"Can I get a custom quote for bulk {topic}?"
    ]
    
    # Location-based variations for 200 FAQs
    micro_areas = [
        "Kakkanad", "Edapally", "Aluva", "Vyttila", "Palarivattom", "Kaloor", 
        "Marine Drive", "Fort Kochi", "Angamaly", "Perumbavoor", "Kalamassery", 
        "Maradu", "Kadavanthra", "Thrippunithura", "Eloor", "Cheranallur", 
        "Nedumbassery", "Calamassery", "Infopark", "SmartCity", "MG Road", 
        "Panampilly Nagar", "Thevara", "Kundannoor", "Nettoor", "Eroor"
    ]
    
    question_stems = [
         "How to arrange pickup in {area} for {topic}?",
         "Is same-day {topic} service available in {area}?",
         "Do you have a drop-off point for {topic} near {area}?",
         "What are the {topic} regulations for businesses in {area}?",
         "Who is the best {topic} provider in {area}?",
         "Cost of {topic} in {area} for 50+ laptops?",
         "Certified {topic} facility near {area}?",
         "E-waste collection schedule for {area} regarding {topic}?",
         "ITAD services for Infopark companies near {area}?",
         "Hard drive shredding for banks in {area}?"
    ]

    # Mix and match to reach 200
    count = 0
    # First, the core ones
    for q in core_questions:
        faqs.append({
            "question": q,
            "answer": f"For {topic}, EWaste Kochi follows the highest standards of certification including NIST 800-88 and KSPCB authorization. We serve over 150+ corporate clients across Kochi with 100% data security guarantee."
        })
        count += 1

    # Then, location variations
    while count < 200:
        for area in micro_areas:
            if count >= 200: break
            stem = question_stems[count % len(question_stems)]
            question = stem.format(area=area, topic=topic)
            answer = f"Yes, EWaste Kochi provides full {topic} coverage in {area}. We offer free corporate pickup for 50+ units for all organizations in the {area} vicinity, ensuring full DPDP Act 2023 compliance."
            faqs.append({"question": question, "answer": answer})
            count += 1
            
    return faqs

def save_faq_database():
    db = {}
    for topic in PILLAR_TOPICS:
        db[topic] = generate_faqs(topic)
    
    with open("faq_database.json", "w") as f:
        json.dump(db, f, indent=2)
    print("✅ FAQ Engine: 2,000 FAQs generated and saved to faq_database.json")

if __name__ == "__main__":
    save_faq_database()
