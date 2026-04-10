import os
import re

PROJECT_DIR = "/media/hp-ml10/Projects/EwasteKochi.com"

# The literal replacements
REPLACEMENTS = [
    # Fonts
    ("family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&family=JetBrains+Mono:wght@400;600;700&family=Syne:wght@600;700;800", "family=Bebas+Neue&family=Outfit:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600"),
    ("family=DM+Sans:wght@400;500;700&family=Syne:wght@700;800", "family=Bebas+Neue&family=Outfit:wght@300;400;500;600;700;800"),
    ("'Syne'", "'Bebas Neue'"),
    ("'DM Sans'", "'Outfit'"),
    
    # Colors
    ("#07100A", "#0A0F0C"), # bg
    ("#162019", "#182118"), # surface
    ("#00E87A", "#00E664"), # primary green
    ("#0C180F", "#111A14"), # bg2
    ("#111F15", "#1C2A1E"), # bg3 -> panel
    ("#A8C4AE", "#9BB8A2"), # text
    ("rgba(0,232,122,.15)", "rgba(0,230,100,.13)"), # border rim
    ("rgba(0,232,122,.13)", "rgba(0,230,100,.13)"), # border rim
    ("#F0F7F2", "#E8F2EA"), # white -> cream
]

TARGETS = [
    "index.html",
    "final_v2.html",
    "mass_page_generator.py",
    "mega_pages_generator.py",
    "mega_services_generator.py"
]

NOISE_CSS = """
/* Noise texture overlay */
body::before {
  content: ''; position: fixed; inset: 0;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.035'/%3E%3C/svg%3E");
  background-size: 200px 200px;
  pointer-events: none; z-index: 0; opacity: .5;
}
/* Grid lines */
body::after {
  content: ''; position: fixed; inset: 0;
  background-image: linear-gradient(rgba(0,230,100,.018) 1px, transparent 1px), linear-gradient(90deg, rgba(0,230,100,.018) 1px, transparent 1px);
  background-size: 40px 40px; pointer-events: none; z-index: 0;
}
"""

def apply_theme():
    for filename in TARGETS:
        filepath = os.path.join(PROJECT_DIR, filename)
        if not os.path.exists(filepath):
            continue
            
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # Apply raw replacements
        for old_str, new_str in REPLACEMENTS:
            content = content.replace(old_str, new_str)
            
        # Inject the noise grid CSS right before </style> if not already there
        if "body::before" not in content:
            injected_css = NOISE_CSS
            if filename.endswith(".py"):
                injected_css = injected_css.replace("{", "{{").replace("}", "}}")
            content = content.replace("</style>", injected_css + "\n</style>", 1)
            
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✅ Updated {filename}")

if __name__ == "__main__":
    apply_theme()
