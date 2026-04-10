import os
import json

ROOT = "/media/hp-ml10/Projects/ewastekochi-production/ewastekochi/"
INDEX_PATH = os.path.join(ROOT, "index.html")

def inject_massive_base():
    with open("faq_database.json", "r") as f:
        faq_db = json.load(f)
    
    # Use the first topic (E-Waste Recycling Kochi) as the main one for index.html
    main_topic = "E-Waste Recycling Kochi"
    faqs = faq_db.get(main_topic, [])
    
    faq_html = '<section class="section" id="authority-lake" style="background:#050806;padding:100px 0;border-top:1px solid #00e664"><div class="wrap">'
    faq_html += '<h2 style="font-family:\'Bebas Neue\';font-size:4rem;color:#fff;margin-bottom:40px;text-align:center">Master Authority Knowledge Base (200+ Guides)</h2>'
    faq_html += '<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px">'
    
    for faq in faqs:
        faq_html += f"""
        <div style="background:rgba(0,230,100,.02);border:1px solid rgba(0,230,100,.1);padding:24px;border-radius:12px">
            <h3 style="color:#fff;font-size:1.1rem;margin-bottom:12px;font-weight:700">Q: {faq['question']}</h3>
            <p style="color:#9bb8a2;font-size:0.95rem;line-height:1.7">{faq['answer']}</p>
        </div>"""
    
    faq_html += '</div></div></section>'
    
    with open(INDEX_PATH, "r") as f:
        content = f.read()
    
    if "<!-- AUTHORITY_BASE_START -->" in content:
        # Prevent double injection
        return
        
    # Inject before footer
    if "<footer>" in content:
        new_content = content.replace("<footer>", f"<!-- AUTHORITY_BASE_START -->\n{faq_html}\n<!-- AUTHORITY_BASE_END -->\n<footer>")
        with open(INDEX_PATH, "w") as f:
            f.write(new_content)
        print("✅ Index.html: Massive Authority Base injected!")

if __name__ == "__main__":
    inject_massive_base()
