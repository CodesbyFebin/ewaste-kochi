import json
import os

# CONFIG
OUTPUT_DIR = "/media/hp-ml10/Projects/ewastekochi-production/ewastekochi/"
FAQ_DB_PATH = os.path.join(OUTPUT_DIR, "faq_database.json")

def generate_schema(topic, slug):
    with open(FAQ_DB_PATH, "r") as f:
        faq_db = json.load(f)
    
    faqs = faq_db.get(topic, [])[:20] # Take first 20 for schema to avoid bloating
    
    faq_entities = []
    for faq in faqs:
        faq_entities.append({
            "@type": "Question",
            "name": faq["question"],
            "acceptedAnswer": {
                "@type": "Answer",
                "text": faq["answer"]
            }
        })
        
    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Service",
                "name": topic,
                "serviceType": "E-Waste Recycling & ITAD",
                "provider": {
                    "@type": "LocalBusiness",
                    "name": "EWaste Kochi",
                    "address": {
                        "@type": "PostalAddress",
                        "streetAddress": "710A Hill Palace Rd, East Fort Gate",
                        "addressLocality": "Thrippunithura",
                        "addressRegion": "Kerala",
                        "postalCode": "682301",
                        "addressCountry": "IN"
                    }
                },
                "areaServed": ["Kochi", "Ernakulam", "Kakkanad", "Aluva", "Vyttila"]
            },
            {
                "@type": "FAQPage",
                "mainEntity": faq_entities
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": 1,
                        "name": "Home",
                        "item": "https://ewastekochi.com/"
                    },
                    {
                        "@type": "ListItem",
                        "position": 2,
                        "name": topic,
                        "item": f"https://ewastekochi.com/{slug}.html"
                    }
                ]
            }
        ]
    }
    return json.dumps(schema, indent=2)

def inject_schema_to_all():
    # This would open each pillar and inject the schema
    # For now, we'll just demonstrate it
    print("✅ Schema Generator: Ready to inject Service + FAQ + Breadcrumb schema.")

if __name__ == "__main__":
    inject_schema_to_all()
