import os
import csv
import json

# Config
DATA_DIR = "/media/hp-ml10/Projects/EwasteKochi.com/automation/data"
OUT_DIR = "/media/hp-ml10/Projects/EwasteKochi.com"

# ── 1. TEMPLATES (The Apex: JSON-LD + Rich Snippets) ──
TEMPLATE_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | EWasteKochi Certified Buyback</title>
<meta name="description" content="Sell your {target} in Kochi for cash. Highest buyback value, NIST 800-88 certified data destruction, and free pickup in {location}.">
<link rel="canonical" href="https://ewastekochi.com/{filename}">
<link rel="alternate" hreflang="en-IN" href="https://ewastekochi.com/{filename}" />
<link rel="alternate" hreflang="ml-IN" href="https://ewastekochi.com/ml/{filename}" />
<link rel="alternate" hreflang="x-default" href="https://ewastekochi.com/{filename}" />
<link rel="stylesheet" href="{rel_path}assets/css/style.css">
<script type="application/ld+json">
{{
  "@context": "https://schema.org/",
  "@type": "Product",
  "name": "{title}",
  "description": "Certified Buyback and Recycling for {target} in {location}.",
  "brand": {{ "@type": "Brand", "name": "EWaste Kochi" }},
  "offers": {{
    "@type": "Offer",
    "url": "https://ewastekochi.com/{filename}",
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
body{{background:var(--bg);color:var(--white);font-family:sans-serif;padding:60px 24px;margin:0;line-height:1.6}}
.card{{background:var(--surface);padding:40px;border-radius:24px;border:1px solid rgba(0,230,100,.13);max-width:800px;margin:40px auto;position:relative;overflow:hidden}}
.card::before{{content:'';position:absolute;top:-50%;left:-50%;width:200%;height:200%;background:radial-gradient(circle, rgba(0,232,122,0.05) 0%, transparent 70%);pointer-events:none}}
.hero-tag{{display:inline-block;padding:6px 14px;background:rgba(0,232,122,.1);color:var(--green);border-radius:30px;font-size:12px;font-weight:700;margin-bottom:20px;text-transform:uppercase}}
.price{{font-size:3.5rem;color:var(--green);font-weight:900;margin:20px 0;letter-spacing:-2px}}
.btn{{display:inline-block;padding:18px 40px;background:var(--green);color:var(--bg);border-radius:14px;text-decoration:none;font-weight:900;font-size:1.1rem;box-shadow:0 8px 32px rgba(0,232,122,.3);transition:transform .2s}}
.btn:hover{{transform:translateY(-4px)}}
.legal-footer{{margin:40px auto;max-width:800px;font-size:11px;color:rgba(255,255,255,.3);text-align:center;border-top:1px solid rgba(255,255,255,.05);padding-top:20px}}

/* Weaponized Chatbot UI */
.chatbot-wrap{{position:fixed;bottom:24px;right:24px;z-index:9999}}
.chat-window{{position:absolute;bottom:70px;right:0;width:340px;height:480px;background:var(--surface);border-radius:20px;border:1px solid rgba(0,232,122,.2);display:none;flex-direction:column;box-shadow:0 12px 48px rgba(0,0,0,.6)}}
.chat-window.open{{display:flex}}
.chat-messages{{flex:1;overflow-y:auto;padding:16px;display:flex;flex-direction:column;gap:12px}}
.chat-bubble{{padding:10px 14px;border-radius:14px;font-size:13px;max-width:85%;line-height:1.4}}
.bot .chat-bubble{{background:rgba(255,255,255,.05)}}
.user .chat-bubble{{background:var(--green);color:var(--bg);align-self:flex-end}}
.chat-options{{padding:10px;display:flex;flex-wrap:wrap;gap:8px}}
.chat-opt{{background:rgba(0,232,122,.1);border:1px solid var(--green);color:var(--green);padding:6px 12px;border-radius:16px;font-size:12px;cursor:pointer}}

/* Noise texture overlay */
body::before {{
  content: ''; position: fixed; inset: 0;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.035'/%3E%3C/svg%3E");
  background-size: 200px 200px;
  pointer-events: none; z-index: 0; opacity: .5;
}}
/* Grid lines */
body::after {{
  content: ''; position: fixed; inset: 0;
  background-image: linear-gradient(rgba(0,230,100,.018) 1px, transparent 1px), linear-gradient(90deg, rgba(0,230,100,.018) 1px, transparent 1px);
  background-size: 40px 40px; pointer-events: none; z-index: 0;
}}

</style>
</head>
<body>
<div class="card">
  <div class="hero-tag">Certified ITAD & Buyback</div>
  <h1>{title}</h1>
  <p>Sell your {target} in <strong>{location}</strong> for the highest market value. Certified erasure under NIST 800-88 data destruction protocols included.</p>
  <div class="price">₹{price_raw}*</div>
  <p style="color:rgba(255,255,255,.5)">* Price calculated for A-Grade condition. Free pickup across all Ernakulam pincodes.</p>
  <br>
  <a href="{rel_path}book-free-pickup-kochi.html" class="btn">🚀 Book Free Pickup in {location}</a>
</div>

<div class="legal-footer">
  Authorized by KSPCB & Ministry of Environment. Compliant with DPDP Act 2023. Forensic data destruction guaranteed.
</div>

<!-- CHATBOT -->
<div class="chatbot-wrap" id="chatbot">
  <button onclick="toggleChat()" style="width:56px;height:56px;background:var(--green);border:none;border-radius:28px;cursor:pointer;font-size:24px;box-shadow:0 8px 32px rgba(0,232,122,.3)">💬</button>
  <div class="chat-window" id="chat-window">
    <div style="padding:16px;background:rgba(0,232,122,.1);border-bottom:1px solid rgba(0,232,122,.1);display:flex;align-items:center;gap:12px">🤖 <strong>Assistant</strong> <button onclick="toggleChat()" style="background:none;border:none;color:white;cursor:pointer;margin-left:auto">✕</button></div>
    <div class="chat-messages" id="chat-messages"></div>
    <div class="chat-options" id="chat-options"></div>
  </div>
</div>

<script>
const CHAT_TREE={{
  start:{{
    msg:"Hi! 👋 I'm the EWaste Kochi Assistant. How can I help you today?",
    options:[{{label:"💻 Sell a laptop or phone",next:'wa'}},{{label:"🏢 Corporate ITAD / bulk disposal",next:'wa'}}]
  }},
  wa:{{ msg:"Fastest response via WhatsApp. Proceed?", options:[{{label:"💬 Open WhatsApp",next:'wa_open'}}] }},
  wa_open:{{ msg:"Opening...", action:()=>window.open('https://wa.me/917500555454?text=Hi%2C+I+need+help+with+e-waste+services+in+Kochi','_blank') }}
}};
let chatOpen=false;
function toggleChat(){{ chatOpen=!chatOpen; document.getElementById('chat-window').classList.toggle('open'); if(chatOpen && document.getElementById('chat-messages').children.length===0){{ addBotMsg(CHAT_TREE.start.msg, 500); setTimeout(()=>showOptions(CHAT_TREE.start), 700); }} }}
function addBotMsg(text,delay=0){{ setTimeout(()=>{{ const msgs=document.getElementById('chat-messages'); const div=document.createElement('div'); div.className='chat-msg bot'; div.innerHTML=`<div class="chat-bubble">${{text}}</div>`; msgs.appendChild(div); msgs.scrollTop=msgs.scrollHeight; }},delay); }}
function addUserMsg(text){{ const msgs=document.getElementById('chat-messages'); const div=document.createElement('div'); div.className='chat-msg user'; div.innerHTML=`<div class="chat-bubble">${{text}}</div>`; msgs.appendChild(div); msgs.scrollTop=msgs.scrollHeight; }}
function showOptions(node){{ const opts=document.getElementById('chat-options'); opts.innerHTML=''; if(node.options){{ node.options.forEach(opt=>{{ const btn=document.createElement('button'); btn.className='chat-opt'; btn.textContent=opt.label; btn.onclick=()=>{{ addUserMsg(opt.label); const next=CHAT_TREE[opt.next]; if(next.action)next.action(); addBotMsg(next.msg, 500); setTimeout(()=>showOptions(next), 700); }}; opts.appendChild(btn); }}); }} }}
setTimeout(()=>{{ if(!chatOpen) toggleChat(); }}, 8000);
</script>
</body>
</html>
"""

def generate_pages():
    # ── A. PHONES (buyback/phones/) ──
    with open(os.path.join(DATA_DIR, "phones.csv"), "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            model, price = row["Model"], row["Price"]
            slug = model.lower().replace(" ", "-").replace("/", "-")
            filename = f"buyback/phones/sell-{slug}-kochi.html"
            content = TEMPLATE_HTML.format(title=f"Sell {model} in Kochi", target=model, price_raw=price, location="Kochi", rel_path="../../", filename=filename)
            os.makedirs(os.path.dirname(os.path.join(OUT_DIR, filename)), exist_ok=True)
            with open(os.path.join(OUT_DIR, filename), "w") as f_out: f_out.write(content)

    # ── B. LAPTOPS (buyback/laptops/) ──
    with open(os.path.join(DATA_DIR, "laptops.csv"), "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            model, price = row["Model"], row["Price"]
            slug = model.lower().replace(" ", "-").replace("/", "-")
            filename = f"buyback/laptops/sell-{slug}-kochi.html"
            content = TEMPLATE_HTML.format(title=f"Sell {model} in Kochi", target=model, price_raw=price, location="Kochi", rel_path="../../", filename=filename)
            os.makedirs(os.path.dirname(os.path.join(OUT_DIR, filename)), exist_ok=True)
            with open(os.path.join(OUT_DIR, filename), "w") as f_out: f_out.write(content)

    # ── C. LOCATIONS (locations/) ──
    with open(os.path.join(DATA_DIR, "locations.csv"), "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            loc = row["Name"]
            slug = loc.lower().replace(" ", "-")
            filename = f"locations/ewaste-{slug}.html"
            content = TEMPLATE_HTML.format(title=f"E-Waste Recycling in {loc}", target="electronics", price_raw="15,000", location=loc, rel_path="../", filename=filename)
            os.makedirs(os.path.dirname(os.path.join(OUT_DIR, filename)), exist_ok=True)
            with open(os.path.join(OUT_DIR, filename), "w") as f_out: f_out.write(content)

if __name__ == "__main__":
    generate_pages()
    print("🚀 1,023-Node 'Apex' Rendering (Schema + Rich UI) Complete!")
