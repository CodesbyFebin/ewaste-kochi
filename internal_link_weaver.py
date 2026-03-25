import os
import re

# Config
BASE_DIR = "/media/hp-ml10/Projects/EwasteKochi.com"

# ── 1. NEURAL MAP (The User's Exact Logic) ──
CONTEXT_MAP = {
    "phone": "/sell-old-phone-kochi.html",
    "laptop": "/sell-old-laptop-kochi.html",
    "data": "/data-destruction-kochi.html",
    "server": "/server-disposal-kochi.html",
    "shredding": "/hard-drive-shredding-kochi.html",
    "certificate": "/certificate-of-destruction.html",
    "infopark": "/industries/it-companies-infopark.html",
    "bank": "/industries/banks-financial-data-destruction.html",
    "compliance": "/compliance/dpdp-act-2023-penalties.html",
    "nist": "/compliance/nist-800-88-explained.html",
}

PAGE_TYPE_LINKS = {
    "blog": ["/itad-kochi.html", "/compliance/nist-800-88-explained.html", "/book-free-pickup-kochi.html", "/ewaste-kochi-complete-guide.html"],
    "location": ["/sell-old-phone-kochi.html", "/itad-kochi.html", "/book-free-pickup-kochi.html", "/ewaste-kochi-complete-guide.html"],
    "industry": ["/data-destruction-kochi.html", "/hard-drive-shredding-kochi.html", "/compliance/dpdp-act-2023-penalties.html"],
    "compliance": ["/data-destruction-kochi.html", "/itad-kochi.html", "/certificate-of-destruction.html"]
}

# ── 2. THE WEAVER ENGINE ──
class NeuralWeaver:
    def __init__(self, root):
        self.root = root

    def get_files(self):
        all_files = []
        for d, _, fs in os.walk(self.root):
            for f in fs:
                if f.endswith(".html"):
                    all_files.append(os.path.join(d, f))
        return all_files

    def get_type(self, path):
        if "/blog/" in path: return "blog"
        if "/locations/" in path: return "location"
        if "/industries/" in path: return "industry"
        if "/compliance/" in path: return "compliance"
        return "pillar"

    def weave(self, path):
        with open(path, "r", encoding="utf-8") as f:
            html = f.read()
            
        ptype = self.get_type(path)
        
        # Relative path calculation
        rel_to_root = ""
        depth = path.replace(self.root, "").lstrip("/").count("/")
        if depth > 0:
            rel_to_root = "../" * depth

        # 1. Neural Footer Injection
        if ptype in PAGE_TYPE_LINKS:
            links = PAGE_TYPE_LINKS[ptype]
            footer_html = f'\n<!-- NEURAL_FLOW_START -->\n<div style="margin-top:40px;padding:20px;border-top:1px dashed rgba(0,232,122,.15);font-size:12px">\n  <strong>Related Resource Path:</strong><br>\n'
            for link in links:
                name = link.split("/")[-1].replace(".html", "").replace("-", " ").title()
                footer_html += f'  <a href="{rel_to_root}{link.lstrip("/")}" style="color:#00E87A;margin-right:15px;text-decoration:none">↳ {name}</a>\n'
            footer_html += "</div>\n<!-- NEURAL_FLOW_END -->\n"
            
            # Remove old flow and add new
            html = re.sub(r'<!-- NEURAL_FLOW_START -->.*?<!-- NEURAL_FLOW_END -->', '', html, flags=re.DOTALL)
            if "</body>" in html:
                html = html.replace("</body>", f"{footer_html}\n</body>")

        with open(path, "w", encoding="utf-8") as f:
            f.write(html)

if __name__ == "__main__":
    nw = NeuralWeaver(BASE_DIR)
    my_files = nw.get_files()
    print(f"Neural Weaver starting on {len(my_files)} files...")
    for f in my_files:
        nw.weave(f)
    print("🚀 NEURAL WEAVING COMPLETE!")
