import os
import re

sitemap_path = "/media/hp-ml10/Projects/ewastekochi-production/ewastekochi/sitemap.xml"
queries = [
    "where to recycle batteries",
    "where to recycle old electronics",
    "where to donate electronics",
    "local recycling centers",
    "how to recycle electronics",
    "where to sell electronics locally",
    "e waste collection kochi",
    "hard drive destruction service",
    "e waste kochi",
    "e waste",
    "india dpdp act data privacy act data protection act compliance",
    "e waste collection near me",
    "cashify kochi alternative",
    "recycle device",
    "ewaste recycling near me",
    "waste management kochi",
    "e waste recycling near me",
    "waste collection near me",
    "ewaste recycling",
    "bed disposal near me",
    "secure e waste destruction",
    "e waste destruction",
    "secure computer recycling",
    "electronics recycling near me",
    "electronic e waste near me",
    "sell electronic waste",
    "e waste near me",
    "waste disposal kochi",
    "e waste buyers near me",
    "ewaste",
    "e waste disposal near me",
    "e waste sale",
    "ewaste hub",
    "recycling computers",
    "data-secure it recycling",
    "secure e-waste recycling",
    "secure electronic disposal",
    "hard drive disposal",
    "hard drive shredding",
    "itad companies in india",
    "secure disposal of computers",
    "e-waste security",
    "certified it asset destruction",
    "disposing e waste",
    "tv e waste near me",
    "aakri shop near me",
    "building waste near me",
    "dell latitude 5419 recycling buyback",
    "e waste dealer near me",
    "e waste scrap buyers near me",
    "electronic recycle",
    "electronic waste",
    "ewaste computer",
    "computer waste",
    "electronic waste disposal near me",
    "ewaste disposal",
    "secure waste disposal",
    "waste box near me",
    "where to dispose electronic waste near me",
    "ac recycle",
    "electric waste bin",
    "cd recycling near me",
    "e-waste",
    "ewaste scrap",
    "itad",
    "682207 ewaste pickup",
    "damaged mobile phone recycling",
    "e waste recycling centers",
    "old phone disposal near me",
    "waste taking near me",
    "battery recycling",
    "e waste buyers",
    "sell old electronics near me",
    "e waste laptop",
    "e waste shop near me",
    "electronic waste near me",
    "sell electronics",
    "ewaste pickup",
    "e waste dealers",
    "electronics re",
    "how to dispose old computers and hardware safely",
    "waste management near me",
    "disposal electronics",
    "e scrap buyers",
    "waste management companies in kochi",
    "gdpr compliance in cochin",
    "hard drive shredding company",
    "it disposal services for education",
    "secure computer disposal",
    "secure laptop disposal",
    "it disposal services",
    "mobile recycle",
    "business it decommissioning services",
    "it equipment disposal",
    "device recycle",
    "plasma tv disposal"
]

def make_slug(query):
    slug = re.sub(r'[^a-zA-Z0-9]+', '-', query.lower())
    return slug.strip('-')

def main():
    if not os.path.exists(sitemap_path):
        print("Sitemap not found!")
        return

    with open(sitemap_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Find the closing </urlset> tag
    if "</urlset>" in content:
        # Generate new nodes
        nodes = []
        for q in set(queries): # Ensure unique just in case
            slug = make_slug(q)
            node = f"""
  <!-- Auto-generated long-tail SEO page -->
  <url>
    <loc>https://ewastekochi.com/{slug}</loc>
    <lastmod>2026-04-10</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.8</priority>
  </url>"""
            # Add to content if not already exists (avoid duplicates)
            if f"<loc>https://ewastekochi.com/{slug}</loc>" not in content:
                nodes.append(node)

        if nodes:
            new_nodes_str = "".join(nodes) + "\n</urlset>"
            new_content = content.replace("</urlset>", new_nodes_str)
            with open(sitemap_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Added {len(nodes)} new URLs to sitemap.")
        else:
            print("All URLs were already in the sitemap.")
    else:
        print("Could not find </urlset> tag.")

if __name__ == "__main__":
    main()
