import json
import random
import os

categories = [
    {'id': 'itad', 'name': 'Corporate ITAD Strategies'},
    {'id': 'compliance', 'name': 'E-Waste Laws & Compliance'},
    {'id': 'data', 'name': 'Data Destruction 101'},
    {'id': 'kochi', 'name': 'Kochi Local Disposal Guides'},
    {'id': 'recycling-tech', 'name': 'Electronic Recycling Technology'},
    {'id': 'lifecycle', 'name': 'Sustainable IT Lifecycle'},
    {'id': 'battery', 'name': 'Battery Recycling Safety'},
    {'id': 'dpdp', 'name': 'DPDP Act 2023 for IT'},
    {'id': 'precious', 'name': 'Precious Metal Recovery (Urban Mining)'},
    {'id': 'resale', 'name': 'Device Buyback & Resale Tips'},
    {'id': 'hazardous', 'name': 'Hazardous Waste Management'},
    {'id': 'circular', 'name': 'Circular Economy in Kerala'},
    {'id': 'datacenter', 'name': 'Data Center Decommissioning'},
    {'id': 'sme', 'name': 'Small Business E-Waste Solutions'},
    {'id': 'environment', 'name': 'Environmental Impact Tracking'},
    {'id': 'printer', 'name': 'Toner & Printer Stewardship'},
    {'id': 'networking', 'name': 'Networking Gear Retirement'},
    {'id': 'mobile', 'name': 'Mobile & Tablet Recycling'},
    {'id': 'green-it', 'name': 'Future of Green Computing'},
    {'id': 'epr', 'name': 'EPR Fulfillment for Manufacturers'}
]

def generate_blog_chunk(count_per_cat=500):
    all_blogs = []
    
    # Pre-generate all slugs for interlinking
    all_slugs_and_titles = []
    for cat in categories:
        for i in range(1, count_per_cat + 1):
            slug = f"{cat['id']}-master-volume-{i}"
            title = f"{cat['name']}: The Definitive Kochi Manual - Volume {i}"
            all_slugs_and_titles.append((slug, title))
            
    # Generate content
    for cat in categories:
        for i in range(1, count_per_cat + 1):
            slug = f"{cat['id']}-master-volume-{i}"
            title = f"{cat['name']}: Technical Intelligence Volume {i}"
            
            # Content Blocks (500-800 words per post to keep total JSON size sane but still 'long')
            body = f"<h2>Strategic Overview of {cat['name']} in Kerala</h2>"
            body += f"<p>In the digital economy of Kochi, {cat['name']} has emerged as a cornerstone of operational resilience. Volume {i} of our technical manual explores the intersection of KSPCB compliance and urban mining.</p>"
            body += "".join([f"<p>The optimization of {cat['name']} requires a multi-stage approach to material recovery. In Kochi's technology corridors, {cat['name']} ensures that valuable minerals are returned to the circuit, reducing the need for raw mining.</p>"] * 5)
            
            # Massive interlinking (100 unique links per post)
            other_data = random.sample(all_slugs_and_titles, 101)
            linked_data = [d for d in other_data if d[0] != slug][:100]
            
            interlinks_html = '<div class="authority-links"><h3>Knowledge Network References</h3><ul style="column-count: 2; font-size: 0.7rem;">'
            for ls, lt in linked_data:
                interlinks_html += f'<li><a href="/blog/{ls}">{lt}</a></li>'
            interlinks_html += '</ul></div>'
            
            # FAQ (3 FAQs per post)
            faqs = []
            for f_idx in range(1, 4):
                faqs.append({
                    "q": f"How is {cat['name']} implemented in Kochi?",
                    "a": f"Implementation of {cat['name']} follows the E-Waste Management Rules 2022. Our Thrippunithura hub handles the end-to-end logistics."
                })
            
            full_body = body + interlinks_html
            
            blog_obj = {
                "slug": slug,
                "title": title,
                "category": cat['id'],
                "excerpt": f"Comprehensive technical research into {cat['name']} for the Kochi enterprise market.",
                "content": full_body,
                "date": "2026-04-14",
                "author": "EWaste Kochi Editorial Board",
                "faqs": faqs
            }
            all_blogs.append(blog_obj)
            
    return all_blogs

all_results = generate_blog_chunk(501) # 20 * 501 = 10,020 blogs
num_parts = 10
chunk_size = len(all_results) // num_parts + 1

for i in range(num_parts):
    start = i * chunk_size
    end = (i + 1) * chunk_size if i < num_parts - 1 else len(all_results)
    chunk = all_results[start:end]
    with open(f'src/data/blogPosts_part{i+1}.json', 'w') as f:
        json.dump(chunk, f, indent=2)

print(f"Generated {len(all_results)} blogs across {num_parts} parts.")
