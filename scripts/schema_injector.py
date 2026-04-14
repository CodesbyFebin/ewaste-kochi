#!/usr/bin/env python3
"""Injects JSON-LD schema into all pages that don't already have it. Run from root."""
import os, json

BASE_SCHEMA = {"@context":"https://schema.org","@type":"LocalBusiness","name":"EWaste Kochi","url":"https://ewastekochi.com/","telephone":"+91-9876543210","email":"info@ewastekochi.com","address":{"@type":"PostalAddress","streetAddress":"710A Hill Palace Rd, East Fort Gate, Kannankulangara","addressLocality":"Thrippunithura","addressRegion":"Kerala","postalCode":"682301","addressCountry":"IN"},"geo":{"@type":"GeoCoordinates","latitude":9.9390,"longitude":76.3590},"openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],"opens":"08:00","closes":"20:00"},{"@type":"OpeningHoursSpecification","dayOfWeek":"Sunday","opens":"10:00","closes":"16:00"}],"aggregateRating":{"@type":"AggregateRating","ratingValue":"4.9","reviewCount":"143"},"priceRange":"₹"}

def inject(path):
    with open(path,"r",encoding="utf-8") as f: c = f.read()
    if "application/ld+json" in c: return
    tag = f'<script type="application/ld+json">\n{json.dumps(BASE_SCHEMA,indent=2)}\n</script>\n'
    c = c.replace("</head>", tag + "</head>", 1)
    with open(path,"w",encoding="utf-8") as f: f.write(c)
    print(f"  Schema injected: {path}")

count = 0
for root, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if d not in ["scripts","css","js","images","__pycache__"]]
    for f in files:
        if f.endswith(".html"):
            inject(os.path.join(root,f))
            count += 1
print(f"Processed {count} files.")
