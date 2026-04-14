import re

src = "/media/hp-ml10/Projects/EwasteKochi.com/final_v2.html"
with open(src, "r") as f:
    html = f.read()

# Update Fonts in <head>
font_links_old = r'<link href="https://fonts.googleapis.com/css2[^>]+>'
font_links_new = """<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
<link href="https://api.fontshare.com/v2/css?f[]=clash-display@600,700&display=swap" rel="stylesheet">"""
html = re.sub(font_links_old, font_links_new, html)

# Update CSS variables
css_var_replacements = {
    r'--bg:#060A08;': '--bg:#07100A;',
    r'--surface:#0A110D;': '--surface:#0A160E;',
    r'--card:#0E1812;': '--card:#0E1F14;',
    r'--card2:#131F16;': '--card2:#11281A;',
    r'--border:#1A2B1E;': '--border:#17301F;',
    r'--border2:#243628;': '--border2:#1E4028;',
    r'--green:#00E896;': '--green:#00E87A;',
    r'--green2:#00C07A;': '--green2:#00C767;',
    r'--amber:#F5A623;': '--amber:#F5A827;',
    r"--font:'Space Grotesk',sans-serif;": "--font:'DM Sans',sans-serif;",
    r"--mono:'DM Mono',monospace;": "--mono:'JetBrains Mono',monospace;",
    r"--display:'Bebas Neue',cursive;": "--display:'Clash Display',sans-serif;"
}
for old, new in css_var_replacements.items():
    html = html.replace(old, new)
    
# Replace color hexes that were hardcoded
html = html.replace('rgba(0,232,150,', 'rgba(0,232,122,')
html = html.replace('#061009', '#07100A')

# Swap Hero .terminal with SVG
hero_svg = """        <div class="hero-image-wrapper" style="position:relative;">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" width="100%" height="auto" style="border-radius:18px; border:1px solid rgba(0,232,122,0.2); box-shadow:0 12px 40px rgba(0,232,122,0.1)">
            <!-- Background -->
            <rect width="800" height="600" fill="#07100A"/>
            <!-- Tech Grid Background -->
            <pattern id="techGrid" width="40" height="40" patternUnits="userSpaceOnUse">
              <path d="M 40 0 L 0 0 0 40" fill="none" stroke="rgba(0,232,122,0.05)" stroke-width="1"/>
              <circle cx="0" cy="0" r="1.5" fill="#00E87A" opacity="0.3"/>
            </pattern>
            <rect width="800" height="600" fill="url(#techGrid)"/>
            
            <!-- Glowing central node (Motherboard Processor) -->
            <g transform="translate(400, 300)">
              <!-- Circuit traces -->
              <path d="M-150,-100 L-100,-100 L-50,-50 M150,-100 L100,-100 L50,-50 M-150,100 L-100,100 L-50,50 M150,100 L100,100 L50,50 M-200,0 L-100,0 M200,0 L100,0" fill="none" stroke="#00E87A" stroke-width="3" opacity="0.6"/>
              <circle cx="-150" cy="-100" r="4" fill="#00E87A"/>
              <circle cx="150" cy="-100" r="4" fill="#00E87A"/>
              <circle cx="-150" cy="100" r="4" fill="#00E87A"/>
              <circle cx="150" cy="100" r="4" fill="#00E87A"/>
              
              <!-- Central CPU structure -->
              <rect x="-80" y="-80" width="160" height="160" rx="8" fill="#0E1F14" stroke="#00E87A" stroke-width="2"/>
              <rect x="-60" y="-60" width="120" height="120" fill="none" stroke="#F5A827" stroke-width="1" stroke-dasharray="4 4"/>
              
              <!-- Abstract layers for complexity -->
              <path d="M-40,-40 L40,-40 L40,40 L-40,40 Z" fill="#00E87A" opacity="0.1"/>
              <rect x="-30" y="-30" width="60" height="60" rx="4" fill="#11281A" stroke="#00E87A" stroke-width="1.5"/>
              <circle cx="0" cy="0" r="12" fill="#F5A827" opacity="0.8"/>
            </g>

            <!-- Hard Drive elements floating -->
            <g transform="translate(200, 180) rotate(-15)">
              <rect x="-50" y="-70" width="100" height="140" rx="6" fill="#0A160E" stroke="#17301F" stroke-width="2"/>
              <circle cx="0" cy="-10" r="35" fill="none" stroke="#00E87A" stroke-width="1.5" opacity="0.5"/>
              <circle cx="0" cy="-10" r="8" fill="#F5A827"/>
              <path d="M-20,40 L20,40 M-20,50 L10,50" stroke="#17301F" stroke-width="3"/>
              <path d="M30,-40 L0,-10" fill="none" stroke="#00E87A" stroke-width="2"/>
            </g>

            <g transform="translate(600, 400) rotate(20)">
              <rect x="-50" y="-70" width="100" height="140" rx="6" fill="#0A160E" stroke="#17301F" stroke-width="2"/>
              <!-- Shattered / Shredded effect -->
              <path d="M-50,0 L50,10 L30,-20 L-40,-10 Z" fill="#FF4757" opacity="0.15"/>
              <path d="M-50,0 L10,5 L-20,30" fill="none" stroke="#FF4757" stroke-width="2"/>
              <text x="0" y="55" font-family="'JetBrains Mono', monospace" font-size="12" fill="#F5A827" text-anchor="middle">DATA DESTROYED</text>
            </g>

            <!-- Abstract Hands holding components -->
            <g transform="translate(400, 480)" opacity="0.8">
              <!-- Digital structural lines representing hands -->
              <path d="M-140,120 C-90,80 -70,60 -50,40 C-30,20 -10,10 0,0 C10,10 30,20 50,40 C70,60 90,80 140,120" fill="none" stroke="#00E87A" stroke-width="3" stroke-linecap="round"/>
              <path d="M-60,50 C-70,-10 -40,-30 -20,-40 C-5,-45 5,-35 10,-20 C20,5 5,30 -10,40" fill="none" stroke="#00E87A" stroke-width="2" stroke-linecap="round"/>
              <path d="M60,50 C70,-10 40,-30 20,-40 C5,-45 -5,-35 -10,-20 C-20,5 -5,30 10,40" fill="none" stroke="#00E87A" stroke-width="2" stroke-linecap="round"/>
            </g>
            
            <!-- Overlay glow -->
            <radialGradient id="glow" cx="50%" cy="50%" r="50%">
              <stop offset="0%" stop-color="#00E87A" stop-opacity="0.15"/>
              <stop offset="100%" stop-color="#07100A" stop-opacity="0"/>
            </radialGradient>
            <rect width="800" height="600" fill="url(#glow)"/>

            <!-- Scanning Line Effect -->
            <line x1="0" y1="200" x2="800" y2="200" stroke="#00E87A" stroke-width="1" opacity="0.5"/>
            <rect x="0" y="200" width="800" height="40" fill="url(#glow)" opacity="0.3"/>
          </svg>
        </div>"""

# Remove terminal block and replace with the SVG
html = re.sub(r'<div class="terminal" role="presentation">.*?</div>\n        </div>', hero_svg, html, flags=re.DOTALL)

# Add Chatbot CSS
chatbot_css = """
/* ── CHATBOT WIDGET ── */
.chatbot-float {
  position:fixed; bottom:24px; right:24px; z-index:9000;
  display:flex; align-items:center; gap:10px;
  background:var(--green); color:var(--bg); border-radius:50px;
  padding:14px 24px 14px 18px; font-weight:700; font-family:var(--font);
  box-shadow:0 8px 30px rgba(0,232,122,0.3); transition:all 0.3s;
  text-decoration:none;
}
.chatbot-float:hover { transform:translateY(-5px); box-shadow:0 12px 40px rgba(0,232,122,0.4); color:var(--bg); }
.cb-icon { font-size:1.6rem; line-height:1; }
"""

# Inject chatbot CSS before </style>
html = html.replace('</style>', chatbot_css + '\n</style>')

# Remove old `.float-cta` floaters since Chatbot replaces it
html = re.sub(r'<div class="float-cta">.*?</div>', '', html, flags=re.DOTALL)

# Inject Chatbot HTML before closing body
chatbot_html = """
<a href="https://wa.me/919876543210" class="chatbot-float" target="_blank" aria-label="Chat with us on WhatsApp">
  <div class="cb-icon">💬</div>
  <div class="cb-text">Chat with us</div>
</a>
</body>"""

html = html.replace('</body>', chatbot_html)

with open(src, "w") as f:
    f.write(html)
