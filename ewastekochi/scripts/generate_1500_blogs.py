#!/usr/bin/env python3
"""
Generate 1,500 blog posts for ewastekochi.com
Targets local, informational, and future-tech keywords.
Each post gets FAQ schema and internal links.
"""

import os
import re
import csv
import random
import itertools
from pathlib import Path
from datetime import datetime
import json

# ===== CONFIGURATION =====

CATEGORIES = {
    "disposal": {
        "name": "E-Waste Disposal",
        "short_name": "disposal",
        "post_count": 150,
        "keywords": [
            "where to dispose e waste in {loc}",
            "e waste drop off {loc}",
            "electronic waste disposal near me {loc}",
            "free e waste disposal {loc}",
            "how to dispose electronics {loc}",
            "nearest e waste recycling center {loc}",
            "e waste collection {loc}",
            "computer waste disposal {loc}",
            "tv disposal {loc}",
            "printer disposal {loc}",
            "bulk e waste pickup {loc}",
            "household e waste disposal {loc}",
            "e waste management services {loc}",
            "authorized e waste disposal {loc}",
            "government approved e waste collection {loc}",
        ],
    },
    "recycling": {
        "name": "E-Waste Recycling",
        "short_name": "recycling",
        "post_count": 150,
        "keywords": [
            "how to recycle electronics in {loc}",
            "e waste recycling process india",
            "recycle old electronics {loc}",
            "electronics recycling center {loc}",
            "computer recycling {loc}",
            "laptop recycling {loc}",
            "mobile recycling {loc}",
            "tv recycling {loc}",
            "printer recycling {loc}",
            "battery recycling {loc}",
            "certified e waste recycler {loc}",
            "eco friendly recycling {loc}",
            "recycling electronics for cash {loc}",
            "e waste recycling plant {loc}",
            "recycling benefits environment",
        ],
    },
    "laptop-disposal": {
        "name": "Laptop Disposal",
        "short_name": "laptop",
        "post_count": 150,
        "keywords": [
            "how to dispose old laptop {loc}",
            "laptop recycling {loc} free pickup",
            "sell old laptop {loc}",
            "laptop data destruction {loc}",
            "laptop scrap value {loc}",
            "where to recycle laptop {loc}",
            "laptop disposal service {loc}",
            "laptop recycling center {loc}",
            "secure laptop disposal {loc}",
            "laptop hard drive shredding {loc}",
            "laptop battery recycling {loc}",
            "donate old laptop {loc}",
            "laptop recycling price {loc}",
            "old laptop buyer {loc}",
            "broken laptop disposal {loc}",
        ],
    },
    "mobile-recycling": {
        "name": "Mobile Phone Recycling",
        "short_name": "mobile",
        "post_count": 150,
        "keywords": [
            "where to recycle old phones in {loc}",
            "mobile disposal {loc}",
            "sell old mobile {loc}",
            "mobile recycling center {loc}",
            "phone data destruction {loc}",
            "recycle smartphone {loc}",
            "mobile scrap value {loc}",
            "how to recycle mobile battery {loc}",
            "old phone recycling {loc}",
            "mobile recycling kerala",
            "iphone recycling {loc}",
            "android phone disposal {loc}",
            "mobile recycling for cash {loc}",
            "recycle phone near me {loc}",
            "secure mobile recycling {loc}",
        ],
    },
    "corporate-itad": {
        "name": "Corporate ITAD",
        "short_name": "itad",
        "post_count": 150,
        "keywords": [
            "IT asset disposal {loc}",
            "company e waste recycling {loc}",
            "ITAD services {loc}",
            "bulk computer recycling {loc}",
            "corporate data destruction {loc}",
            "server recycling {loc}",
            "data center decommissioning {loc}",
            "IT equipment disposal {loc}",
            "corporate e waste management {loc}",
            "EPR compliance {loc}",
            "IT asset management {loc}",
            "bulk electronics pickup {loc}",
            "corporate recycling certificate {loc}",
            "secure IT disposal {loc}",
            "itad companies {loc}",
        ],
    },
    "data-destruction": {
        "name": "Data Destruction",
        "short_name": "data",
        "post_count": 150,
        "keywords": [
            "hard drive shredding {loc}",
            "secure data destruction {loc}",
            "data destruction certificate {loc}",
            "degaussing service {loc}",
            "ssd destruction {loc}",
            "hard drive disposal {loc}",
            "data destruction cost {loc}",
            "certified data destruction {loc}",
            "tape destruction {loc}",
            "media shredding {loc}",
            "data destruction standards",
            "nist 800-88 compliance",
            "onsite data destruction {loc}",
            "data wiping service {loc}",
            "data sanitization {loc}",
        ],
    },
    "scrap-electronics": {
        "name": "Scrap Electronics",
        "short_name": "scrap",
        "post_count": 150,
        "keywords": [
            "computer scrap buyers {loc}",
            "electronics scrap value {loc}",
            "scrap computer price {loc}",
            "old electronics scrap {loc}",
            "scrap laptop buyers {loc}",
            "electronic waste scrap {loc}",
            "scrap metal from electronics {loc}",
            "pc scrap price {loc}",
            "server scrap value {loc}",
            "mobile scrap price {loc}",
            "scrap motherboard price {loc}",
            "cpu scrap buyers {loc}",
            "ram scrap value {loc}",
            "electronic scrap dealer {loc}",
            "best scrap price for electronics {loc}",
        ],
    },
    "battery-recycling": {
        "name": "Battery Recycling",
        "short_name": "battery",
        "post_count": 150,
        "keywords": [
            "lithium battery disposal {loc}",
            "battery recycling {loc} rules",
            "UPS battery recycling {loc}",
            "car battery recycling {loc}",
            "inverter battery disposal {loc}",
            "laptop battery recycling {loc}",
            "mobile battery disposal {loc}",
            "lead acid battery recycling {loc}",
            "battery scrap price {loc}",
            "hazardous battery disposal {loc}",
            "lithium ion recycling {loc}",
            "battery collection center {loc}",
            "rechargeable battery recycling {loc}",
            "battery disposal near me {loc}",
            "safely dispose batteries {loc}",
        ],
    },
    "government-rules": {
        "name": "E-Waste Rules & Compliance",
        "short_name": "rules",
        "post_count": 150,
        "keywords": [
            "e waste rules {loc}",
            "PCB guidelines India e waste",
            "kerala pollution control board e waste",
            "EPR registration {loc}",
            "e waste management rules 2022",
            "authorized recycler list kerala",
            "e waste certificate {loc}",
            "hazardous waste rules {loc}",
            "environmental clearance e waste",
            "compliance for e waste recyclers",
            "extended producer responsibility",
            "e waste handling rules india",
            "kerala e waste policy",
            "penalties for illegal dumping",
            "how to get e waste authorization",
        ],
    },
    "environmental-impact": {
        "name": "Environmental Impact",
        "short_name": "environment",
        "post_count": 150,
        "keywords": [
            "effects of e waste pollution",
            "why recycle electronics india",
            "e waste health hazards",
            "environmental benefits of recycling",
            "carbon footprint e waste",
            "e waste and water pollution",
            "toxic materials in electronics",
            "e waste in landfills",
            "circular economy e waste",
            "precious metal recovery e waste",
            "e waste impact on soil",
            "air pollution from e waste",
            "climate change e waste",
            "sustainable e waste management",
            "green electronics recycling",
        ],
    },
}

# Locations
LOCATIONS = [
    "Kochi", "Ernakulam", "Edappally", "Kakkanad", "Vytilla", "MG Road", "Aluva",
    "Palarivattom", "Kalamassery", "Thrikkakara", "Maradu", "Thoppumpady", "Fort Kochi",
    "Mattancherry", "Thevara", "Panampilly Nagar", "Kadavanthra", "Elamkulam", "Pachalam",
    "Kaloor", "Changampuzha Park", "Kacheripady", "Perumbavoor", "Angamaly", "Muvattupuzha",
    "Koovappady", "Piravom", "Kothamangalam", "Njarakkal", "Cherai", "North Paravur",
    "Alangad", "Choornikkara", "Pallikara", "Puthuvype", "Vypin", "Moolampilly",
    "Kumbalangi", "Kumbalam", "Ayyampuzha", "Palluruthy", "Kuzhuppilly",
    "Kakkanad Infopark", "Kakkanad SmartCity", "Edappally Toll", "Vytilla Hub",
    "Palarivattom Junction", "MG Road Kochi", "Marine Drive", "Broadway", "South Kochi",
    "Thripunithura", "Poonithura", "Kumbalam", "Cheranalloor", "Varapuzha",
    "Kumbalam", "Kuzhuppilly", "Chellanam", "Kumbalangi", "Puthuvype"
]

# FAQ templates
FAQ_TEMPLATES = {
    "default": [
        ("What is {topic}?", "At EWasteKochi, {topic} involves local expertise and certified processing of tech waste."),
        ("Is {topic} free in {loc}?", "We offer free pickup for bulk {topic} throughout the {loc} region."),
        ("How do I schedule {topic}?", "You can book online or call us at +91-7500555454."),
        ("What items are accepted for {topic}?", "We accept all electronic devices including IT assets and residential scrap."),
        ("Do you provide a certificate after {topic}?", "Yes, we provide a certificate of recycling/data destruction for every job."),
    ],
    "disposal": [
        ("Where can I dispose e-waste in {loc}?", "EWasteKochi offers doorstep collection and certified disposal in {loc}."),
        ("Is there free e-waste pickup in {loc}?", "Yes, for bulk items we provide complimentary extraction across {loc}."),
    ],
    "data": [
        ("How is data destroyed?", "We use NIST 800-88 degaussing, shredding, and certified erasure."),
        ("Do you provide a data destruction certificate?", "Yes, with full chain of custody documentation."),
    ],
}

# HTML template
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{title}} | EWasteKochi Blogs</title>
    <meta name="description" content="{{meta_description}}">
    <meta name="keywords" content="{{keywords}}">
    <link rel="canonical" href="https://blogs.ewastekochi.com/{{canonical_url}}">
    <link rel="stylesheet" href="/assets/css/blog.css">
    <script type="application/ld+json">
    {{faq_schema}}
    </script>
</head>
<body>
    <header>
        <nav>
            <a href="/">EWasteKochi Blogs</a>
            <a href="https://ewastekochi.com">Main Site</a>
        </nav>
    </header>
    <main>
        <article>
            <h1>{{h1}}</h1>
            <p class="date">Published: {{date}}</p>
            {{content}}
            <div class="cta">
                <h3>Need e-waste pickup in {{location}}?</h3>
                <p>Call us: +91-7500555454 or <a href="https://ewastekochi.com/contact">Book Online</a></p>
                <a href="https://wa.me/917500555454?text=I%20need%20e-waste%20pickup%20in%20{{location_encoded}}" class="whatsapp-btn" target="_blank">Chat on WhatsApp</a>
            </div>
        </article>
        <aside>
            <h3>Related Posts</h3>
            <ul>
                {{related_links}}
            </ul>
        </aside>
    </main>
    <footer>
        <p>&copy; {{year}} EWasteKochi. All rights reserved.</p>
    </footer>
</body>
</html>
"""

def slugify(text):
    text = re.sub(r'[^\w\s-]', '', text)
    return re.sub(r'[-\s]+', '-', text).strip('-').lower()

def generate_faq_schema(faq_list):
    items = [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq_list]
    schema = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": items}
    return json.dumps(schema, ensure_ascii=False, indent=2)

def generate_post_content(category, keyword, location):
    topic = category["name"].lower()
    sections = []
    intro = f"Looking for {keyword.format(loc=location).lower()} in {location}? EWasteKochi offers free pickup, certified recycling, and data destruction."
    sections.append(f"<p>{intro}</p>")
    sections.append(f"<h2>Certified E-Waste Pickup in {location}</h2>")
    sections.append(f"<p>EWasteKochi provide professional collection in {location}. We handle all ITAD and electronic scrap with KSPCB authorization.</p>")
    return "\\n".join(sections)

def generate_blog_post(cat_key, category, keyword, location, index):
    title = keyword.format(loc=location).capitalize()
    meta_description = f"Looking for {title.lower()} in {location}? Certified e-waste recycling and data destruction by EWasteKochi."
    keywords = f"{title.lower()}, e-waste, recycling, {location.lower()}"
    canonical_url = f"{cat_key}/{slugify(title)}/"
    content = generate_post_content(category, keyword, location)
    
    faq_items = []
    for q, a in FAQ_TEMPLATES.get("default", []):
        faq_items.append((q.format(topic=category["name"], loc=location), a.format(topic=category["name"], loc=location)))
    faq_schema = generate_faq_schema(faq_items)
    
    html = HTML_TEMPLATE.replace("{{title}}", title).replace("{{meta_description}}", meta_description[:155]).replace("{{keywords}}", keywords).replace("{{canonical_url}}", canonical_url).replace("{{h1}}", title).replace("{{content}}", content).replace("{{date}}", datetime.now().strftime("%B %d, %Y")).replace("{{year}}", str(datetime.now().year)).replace("{{location}}", location).replace("{{location_encoded}}", location.replace(" ", "%20")).replace("{{faq_schema}}", faq_schema)
    return html, canonical_url, title

def generate_all_blogs():
    # ADJUSTED PATH for Antigravity environment
    output_root = Path("/media/hp-ml10/Projects/ewastekochi-production/gitlab_repo/blogs")
    output_root.mkdir(parents=True, exist_ok=True)
    
    all_posts = []
    for cat_key, cat_data in CATEGORIES.items():
        cat_folder = output_root / cat_key
        cat_folder.mkdir(exist_ok=True)
        posts_needed = cat_data["post_count"]
        posts_generated = 0
        
        kw_cycle = itertools.cycle(cat_data["keywords"])
        loc_cycle = itertools.cycle(LOCATIONS)
        while posts_generated < posts_needed:
            kw = next(kw_cycle)
            loc = next(loc_cycle)
            html, url, title = generate_blog_post(cat_key, cat_data, kw, loc, posts_generated)
            post_dir = output_root / url.strip('/')
            if not post_dir.exists():
                post_dir.mkdir(parents=True, exist_ok=True)
                (post_dir / "index.html").write_text(html, encoding="utf-8")
                all_posts.append((cat_key, url, title))
                posts_generated += 1
        print(f"Post {posts_generated} in {cat_key}")

    # Second pass: related links
    for cat_key, url, title in all_posts:
        same_cat = [p for p in all_posts if p[0] == cat_key and p[1] != url]
        related = random.sample(same_cat, min(len(same_cat), 3))
        rel_html = "".join([f'<li><a href="/{r[1]}">{r[2]}</a></li>' for r in related])
        f_p = output_root / url.strip('/') / "index.html"
        if f_p.exists():
            c = f_p.read_text(encoding="utf-8")
            f_p.write_text(c.replace("{{related_links}}", rel_html), encoding="utf-8")

    # Index pages
    idx_html = "<html><body><h1>Blog Index</h1><ul>"
    for cat_key, cat_data in CATEGORIES.items():
        idx_html += f"<li><a href='/{cat_key}/'>{cat_data['name']}</a></li>"
        cat_idx = f"<html><body><h1>{cat_data['name']}</h1><ul>"
        for p in [x for x in all_posts if x[0] == cat_key]:
            cat_idx += f"<li><a href='/{p[1]}'>{p[2]}</a></li>"
        cat_idx += "</ul></body></html>"
        (output_root / cat_key / "index.html").write_text(cat_idx, encoding="utf-8")
    idx_html += "</ul></body></html>"
    (output_root / "index.html").write_text(idx_html, encoding="utf-8")

    # Blog Sitemap
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for k, url, t in all_posts:
        sm += f"  <url><loc>https://blogs.ewastekochi.com/{url}</loc></url>\n"
    sm += "</urlset>"
    (output_root / "sitemap.xml").write_text(sm, encoding="utf-8")

if __name__ == "__main__":
    generate_all_blogs()
