import os
import csv

# Config
DATA_DIR = "/media/hp-ml10/Projects/EwasteKochi.com/automation/data"
OUT_DIR = "/media/hp-ml10/Projects/EwasteKochi.com/ml" # Fixed output directory for Malayalam

# ── 1. MALAYALAM TEMPLATE (The Apex-ML: Schema + Malayalam Content) ──
TEMPLATE_ML = """
<!DOCTYPE html>
<html lang="ml">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title_ml} | ഇ-വേസ്റ്റ് കൊച്ചി</title>
<meta name="description" content="{target_ml} {location}-ൽ വിൽക്കുക. ഏറ്റവും ഉയർന്ന വില, സുരക്ഷിതമായ ഡാറ്റാ നശീകരണം (NIST 800-88).">
<link rel="canonical" href="https://ewastekochi.com/ml/{filename}">
<link rel="alternate" hreflang="en-IN" href="https://ewastekochi.com/{en_filename}" />
<link rel="alternate" hreflang="ml-IN" href="https://ewastekochi.com/ml/{filename}" />
<link rel="alternate" hreflang="x-default" href="https://ewastekochi.com/{en_filename}" />
<link rel="stylesheet" href="{rel_path}assets/css/style.css">
<script type="application/ld+json">
{{
  "@context": "https://schema.org/",
  "@type": "Product",
  "name": "{title_ml}",
  "description": "{model} കൊച്ചിയിൽ വിൽക്കുക. ഏറ്റവും ഉയർന്ന വില, സുരക്ഷിതമായ ഡാറ്റാ നശീകരണം.",
  "brand": {{ "@type": "Brand", "name": "EWaste Kochi" }},
  "offers": {{
    "@type": "Offer",
    "url": "https://ewastekochi.com/ml/{filename}",
    "priceCurrency": "INR",
    "price": "{price_raw}",
    "priceValidUntil": "2026-12-31",
    "availability": "https://schema.org/InStock",
    "itemCondition": "https://schema.org/UsedCondition"
  }}
}}
</script>
<style>
:root{{--bg:#0A0F0C;--white:#E8F2EA;--green:#00E664;--surface:#182118}}
body{{background:var(--bg);color:var(--white);font-family:sans-serif;padding:60px 24px;margin:0;line-height:1.7}}
.card{{background:var(--surface);padding:40px;border-radius:24px;border:1px solid rgba(0,230,100,.13);max-width:800px;margin:40px auto;position:relative;overflow:hidden}}
.hero-tag{{display:inline-block;padding:6px 14px;background:rgba(0,232,122,.1);color:var(--green);border-radius:30px;font-size:12px;font-weight:700;margin-bottom:20px;text-transform:uppercase}}
.price{{font-size:3.5rem;color:var(--green);font-weight:900;margin:20px 0;letter-spacing:-2px}}
.btn{{display:inline-block;padding:18px 40px;background:var(--green);color:var(--bg);border-radius:14px;text-decoration:none;font-weight:900;font-size:1.1rem;box-shadow:0 8px 32px rgba(0,232,122,.3)}}
.legal-footer{{margin:40px auto;max-width:800px;font-size:12px;color:rgba(255,255,255,.3);text-align:center;border-top:1px solid rgba(255,255,255,.05);padding-top:20px}}
</style>
</head>
<body>
<div class="card" style="text-align:right">
  <div class="hero-tag">സർട്ടിഫൈഡ് ഇ-വേസ്റ്റ് സർവീസ്</div>
  <h1 style="font-size:2.5rem">{title_ml}</h1>
  <p>നിങ്ങളുടെ പഴയ {model} കൊച്ചിയിൽ (<strong>{location}</strong>) ഏറ്റവും ഉയർന്ന വിലയ്ക്ക് വിൽക്കൂ. NIST 800-88 ഡാറ്റാ സുരക്ഷാ മാനദണ്ഡങ്ങൾ അനുസരിച്ചുള്ള ഡാറ്റാ നശീകരണം ഞങ്ങൾ ഉറപ്പ് നൽകുന്നു.</p>
  <div class="price">₹{price_raw}*</div>
  <p style="color:rgba(255,255,255,.5)">* A-Grade ഉപകരണങ്ങൾക്കുള്ള വില. കൊച്ചിയിലെ എല്ലാ പിൻകോഡുകളിലും സൗജന്യ പിക്കപ്പ് ലഭ്യമാണ്.</p>
  <br>
  <a href="https://wa.me/917500555454?text=Hi, I want to sell my {model} in {location}" class="btn">🚀 ഇപ്പോൾ വിൽക്കൂ (WhatsApp)</a>
</div>

<div class="legal-footer">
  KSPCB അംഗീകാരമുള്ള ഏക സ്ഥാപനം. DPDP Act 2023 മാനദണ്ഡങ്ങൾ പാലിച്ച് പ്രവർത്തിക്കുന്നു.
</div>
</body>
</html>
"""

def generate_ml_pages():
    # Only generating for phones and laptops to save space and focus on high-traffic buyback keywords
    
    # ── A. PHONES (ml/buyback/phones/) ──
    with open(os.path.join(DATA_DIR, "phones.csv"), "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            model, price = row["Model"], row["Price"]
            slug = model.lower().replace(" ", "-").replace("/", "-")
            filename = f"buyback/phones/sell-{slug}-kochi.html"
            en_filename = f"buyback/phones/sell-{slug}-kochi.html"
            
            title_ml = f"{model} കൊച്ചിയിൽ വിൽക്കുക"
            content = TEMPLATE_ML.format(
                title_ml=title_ml, 
                model=model, 
                target_ml=model,
                price_raw=price, 
                location="കൊച്ചി", 
                rel_path="../../", 
                filename=filename, 
                en_filename=en_filename
            )
            
            target_path = os.path.join(OUT_DIR, filename)
            os.makedirs(os.path.dirname(target_path), exist_ok=True)
            with open(target_path, "w") as f_out:
                f_out.write(content)

    # ── B. LAPTOPS (ml/buyback/laptops/) ──
    with open(os.path.join(DATA_DIR, "laptops.csv"), "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            model, price = row["Model"], row["Price"]
            slug = model.lower().replace(" ", "-").replace("/", "-")
            filename = f"buyback/laptops/sell-{slug}-kochi.html"
            en_filename = f"buyback/laptops/sell-{slug}-kochi.html"
            
            title_ml = f"പഴയ {model} കൊച്ചിയിൽ വിൽക്കാം"
            content = TEMPLATE_ML.format(
                title_ml=title_ml, 
                model=model, 
                target_ml=model,
                price_raw=price, 
                location="കൊച്ചി", 
                rel_path="../../", 
                filename=filename, 
                en_filename=en_filename
            )
            
            target_path = os.path.join(OUT_DIR, filename)
            os.makedirs(os.path.dirname(target_path), exist_ok=True)
            with open(target_path, "w") as f_out:
                f_out.write(content)

    # ── C. LOCATIONS (ml/locations/) ──
    with open(os.path.join(DATA_DIR, "locations.csv"), "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            loc = row["Name"]
            slug = loc.lower().replace(" ", "-")
            filename = f"locations/ewaste-{slug}.html"
            en_filename = f"locations/ewaste-{slug}.html"
            
            # Simple mapping for common suburbs to Malayalam
            loc_ml = loc # Fallback
            if loc == "Kakkanad": loc_ml = "കാക്കനാട്"
            elif loc == "Edapally": loc_ml = "ഇടപ്പള്ളി"
            elif loc == "Aluva": loc_ml = "ആലുവ"
            elif loc == "Thrippunithura": loc_ml = "തൃപ്പൂണിത്തുറ"
            elif loc == "Vyttila": loc_ml = "വൈറ്റില"
            elif loc == "Palarivattom": loc_ml = "പാലാരിവട്ടം"
            elif loc == "Kochi": loc_ml = "കൊച്ചി"
            elif loc == "Ernakulam": loc_ml = "എറണാകുളം"
            
            title_ml = f"{loc_ml}-ൽ ഇ-വേസ്റ്റ് റീസൈക്ലിംഗ്"
            content = TEMPLATE_ML.format(
                title_ml=title_ml, 
                model="ഇലക്ട്രോണിക്സ്", 
                target_ml="ഇലക്ട്രോണിക്സ്",
                price_raw="15,000", 
                location=loc_ml, 
                rel_path="../", 
                filename=filename, 
                en_filename=en_filename
            )
            
            target_path = os.path.join(OUT_DIR, filename)
            os.makedirs(os.path.dirname(target_path), exist_ok=True)
            with open(target_path, "w") as f_out:
                f_out.write(content)

if __name__ == "__main__":
    generate_ml_pages()
    print("🚀 Malayalam SEO Cluster (ML-Apex) Generation Complete!")
