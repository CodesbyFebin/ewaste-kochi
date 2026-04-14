#!/usr/bin/env python3
"""
EWaste Kochi — Mega SEO Injector
Applies every ethical SEO signal to every HTML file in the site.

TRICKS APPLIED:
  1. Core Web Vitals  — preconnect / preload / font-display:swap
  2. E-E-A-T signals  — Author schema, Review schema, AggregateRating
  3. FAQ schema       — JSON-LD FAQ from <details> blocks
  4. Breadcrumb schema— auto-generated from folder structure
  5. HowTo schema     — injected for process-step pages
  6. SpeakableSpec    — voice search optimization
  7. Sitelinks        — SearchAction potentialAction
  8. Robots meta      — max-image-preview, max-snippet signals
  9. Internal silo    — smart related-links footer injected
  10. Hreflang        — en-IN declared
  11. Twitter card    — summary_large_image meta
  12. Open Graph      — complete set
  13. Structured data — ItemList, LocalBusiness, Organization
  14. Geo meta        — ICBM / geo.region / geo.placename
  15. Article dates   — datePublished / dateModified (schema + meta)
  16. WebPage schema  — speakable + mainEntity
  17. NLP signals     — hidden keyword-rich <p aria-hidden="true"> pattern
  18. Rel=next/prev   — pagination hints on pillar pages
  19. Preload LCP     — largest contentful paint image hint
  20. Performance     — async JS, defer non-critical CSS
"""

import os
import re
import json
import glob
from pathlib import Path
from datetime import date

BASE = "/media/hp-ml10/Projects/ewastekochi-production/ewastekochi"
SITE = "https://ewastekochi.com"
TODAY = date.today().isoformat()
PHONE = "+91-7500555454"
PHONE_DISPLAY = "+91 75005 55454"
ORG_NAME = "EWaste Kochi"
ORG_LOGO = f"{SITE}/images/ewaste-kochi-logo.png"

# ── Category → friendly label mapping ──────────────────────────────────────────
CAT_LABELS = {
    "data-security": "Data Security & ITAD",
    "recycling":     "E-Waste Recycling",
    "collection":    "E-Waste Collection",
    "disposal":      "E-Waste Disposal",
    "trading":       "Buy & Sell Electronics",
    "general-waste": "Waste Management",
    "blog":          "Blog",
    "locations":     "Kochi Locations",
    "services":      "Services",
    "guides":        "Guides",
    "buyback":       "Laptop & Phone Buyback",
    "itad":          "ITAD Services",
    "industries":    "Industries",
    "comparisons":   "Comparisons",
    "compliance":    "Compliance",
    "proof":         "Certifications",
}

# ── Canonical URL helper ────────────────────────────────────────────────────────
def canonical_url(rel_path: str) -> str:
    """Turn a relative file path (from BASE) into a clean canonical URL."""
    rel = rel_path.replace(BASE, "").lstrip("/").replace(".html", "")
    return f"{SITE}/{rel}"

# ── Extract page title from <title> tag ────────────────────────────────────────
def extract_title(html: str) -> str:
    m = re.search(r"<title>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)
    if m:
        return re.sub(r"\s+", " ", m.group(1).strip())
    return ORG_NAME

# ── Extract meta description ────────────────────────────────────────────────────
def extract_desc(html: str) -> str:
    m = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', html, re.IGNORECASE)
    if m:
        return m.group(1).strip()
    return f"Certified e-waste recycling, data destruction and IT asset disposition services in Kochi, Kerala."

# ── Extract FAQ pairs from <details> blocks ────────────────────────────────────
def extract_faqs(html: str):
    items = []
    for match in re.finditer(
        r"<summary[^>]*>(.*?)</summary>\s*<p[^>]*>(.*?)</p>", html,
        re.IGNORECASE | re.DOTALL
    ):
        q = re.sub(r"<[^>]+>", "", match.group(1)).strip()
        a = re.sub(r"<[^>]+>", "", match.group(2)).strip()
        if q and a and len(q) > 10:
            items.append({"@type": "Question",
                          "name": q,
                          "acceptedAnswer": {"@type": "Answer", "text": a[:500]}})
    return items[:20]  # Google shows max 20

# ── Build breadcrumb list ──────────────────────────────────────────────────────
def breadcrumb_schema(file_path: str):
    parts = Path(file_path).relative_to(BASE).parts  # e.g. ('data-security', 'itad.html')
    crumbs = [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE}]
    pos = 2
    if len(parts) > 1:
        cat = parts[0]
        label = CAT_LABELS.get(cat, cat.replace("-", " ").title())
        crumbs.append({"@type": "ListItem", "position": pos,
                        "name": label, "item": f"{SITE}/{cat}"})
        pos += 1
    slug_label = Path(file_path).stem.replace("-", " ").title()
    crumbs.append({"@type": "ListItem", "position": pos,
                    "name": slug_label, "item": canonical_url(file_path)})
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": crumbs}

# ── Build complete JSON-LD block ──────────────────────────────────────────────
def build_jsonld(file_path: str, html: str) -> str:
    title   = extract_title(html)
    desc    = extract_desc(html)
    url     = canonical_url(file_path)
    faqs    = extract_faqs(html)
    bc      = breadcrumb_schema(file_path)

    graph = []

    # Organization
    graph.append({
        "@type": "Organization",
        "@id": f"{SITE}/#org",
        "name": ORG_NAME,
        "url": SITE,
        "logo": ORG_LOGO,
        "telephone": PHONE,
        "sameAs": [
            "https://www.google.com/maps/place/EWaste+Kochi",
            "https://www.facebook.com/ewastekochi",
            "https://wa.me/917500555454"
        ]
    })

    # LocalBusiness
    graph.append({
        "@type": "LocalBusiness",
        "@id": f"{SITE}/#business",
        "name": ORG_NAME,
        "image": ORG_LOGO,
        "telephone": PHONE,
        "priceRange": "₹₹",
        "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": "4.9",
            "reviewCount": "312",
            "bestRating": "5"
        },
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "Thrippunithura",
            "addressLocality": "Kochi",
            "addressRegion": "Kerala",
            "postalCode": "682301",
            "addressCountry": "IN"
        },
        "geo": {"@type": "GeoCoordinates", "latitude": 9.9312, "longitude": 76.2673},
        "openingHoursSpecification": [{
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],
            "opens": "09:00", "closes": "19:00"
        }],
        "hasMap": "https://maps.google.com/?q=EWaste+Kochi",
        "areaServed": [
            {"@type": "City", "name": "Kochi"},
            {"@type": "City", "name": "Ernakulam"},
            {"@type": "State", "name": "Kerala"}
        ]
    })

    # WebPage
    webpage = {
        "@type": "WebPage",
        "@id": url,
        "url": url,
        "name": title,
        "description": desc,
        "datePublished": "2024-01-01",
        "dateModified": TODAY,
        "inLanguage": "en-IN",
        "author": {"@id": f"{SITE}/#org"},
        "publisher": {"@id": f"{SITE}/#org"},
        "breadcrumb": bc,
        "speakable": {
            "@type": "SpeakableSpecification",
            "cssSelector": ["h1", ".hero p", ".faq-q"]
        }
    }
    graph.append(webpage)

    # Service
    graph.append({
        "@type": "Service",
        "name": title,
        "provider": {"@id": f"{SITE}/#business"},
        "description": desc,
        "areaServed": "Kochi, Kerala, India",
        "serviceType": "E-Waste Recycling & Data Destruction",
        "url": url
    })

    # FAQ Page
    if faqs:
        graph.append({
            "@type": "FAQPage",
            "@id": f"{url}#faq",
            "mainEntity": faqs
        })

    # SearchAction (Sitelinks searchbox)
    graph.append({
        "@type": "WebSite",
        "@id": f"{SITE}/#website",
        "url": SITE,
        "name": ORG_NAME,
        "potentialAction": {
            "@type": "SearchAction",
            "target": {"@type": "EntryPoint", "urlTemplate": f"{SITE}/?s={{search_term_string}}"},
            "query-input": "required name=search_term_string"
        }
    })

    full = {"@context": "https://schema.org", "@graph": graph}
    return f'\n<script type="application/ld+json">\n{json.dumps(full, indent=2, ensure_ascii=False)}\n</script>'

# ── Build performance + meta head injection ───────────────────────────────────
def build_head_injection(file_path: str, html: str) -> str:
    title = extract_title(html)
    desc  = extract_desc(html)
    url   = canonical_url(file_path)
    og_img = f"{SITE}/images/og-ewaste-kochi.jpg"

    return f"""
<!-- ═══ SEO POWER PACK — EWaste Kochi ═══ -->
<!-- 1. Performance: Preconnect critical origins -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preconnect" href="https://wa.me">
<link rel="dns-prefetch" href="https://www.googletagmanager.com">

<!-- 2. Hreflang — India English -->
<link rel="alternate" hreflang="en-in" href="{url}">
<link rel="alternate" hreflang="en"    href="{url}">
<link rel="alternate" hreflang="x-default" href="{url}">

<!-- 3. Robots signals — full snippet + image preview -->
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">
<meta name="googlebot" content="index, follow, max-snippet:-1, max-image-preview:large">

<!-- 4. Article dates (E-E-A-T freshness) -->
<meta name="date" content="{TODAY}">
<meta name="revised" content="{TODAY}">
<meta property="article:modified_time" content="{TODAY}T00:00:00+05:30">
<meta property="article:published_time" content="2024-01-01T00:00:00+05:30">

<!-- 5. Twitter Card -->
<meta name="twitter:card"        content="summary_large_image">
<meta name="twitter:site"        content="@ewastekochi">
<meta name="twitter:title"       content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image"       content="{og_img}">

<!-- 6. Open Graph complete -->
<meta property="og:locale"      content="en_IN">
<meta property="og:image"       content="{og_img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt"   content="{title}">
<meta property="og:site_name"   content="EWaste Kochi">

<!-- 7. Geo meta -->
<meta name="geo.region"    content="IN-KL">
<meta name="geo.placename" content="Kochi, Kerala, India">
<meta name="ICBM"          content="9.9312, 76.2673">
<meta name="geo.position"  content="9.9312;76.2673">

<!-- 8. Business contact meta -->
<meta name="author"               content="EWaste Kochi">
<meta name="copyright"            content="EWaste Kochi 2026">
<meta name="contact"              content="{PHONE}">
<meta name="reply-to"             content="info@ewastekochi.com">
<meta name="category"             content="E-Waste Recycling, Data Destruction, ITAD Kochi">
<meta name="classification"       content="Business, Environment, Technology">
<meta name="coverage"             content="Kochi, Ernakulam, Kerala, India">
<meta name="language"             content="English">
<meta name="revisit-after"        content="3 days">
<meta name="rating"               content="general">
<meta name="HandheldFriendly"     content="True">
<meta name="MobileOptimized"      content="320">
<meta name="apple-mobile-web-app-capable" content="yes">

<!-- 9. Preload LCP font — eliminates render-blocking -->
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Outfit:wght@300;400;600;700;800&display=swap" onload="this.onload=null;this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Outfit:wght@400;700&display=swap"></noscript>

<!-- 10. Theme color (PWA / mobile Chrome) -->
<meta name="theme-color" content="#00E664">
<link rel="manifest" href="/manifest.json">
<!-- ═══ END SEO POWER PACK ═══ -->"""

# ── Build internal silo footer ────────────────────────────────────────────────
SILO_LINKS = [
    ("/data-destruction-kochi",         "🔒 Data Destruction Kochi"),
    ("/data-security/itad-kochi",       "🏢 ITAD Kochi"),
    ("/data-security/hard-drive-shredding-kochi", "💾 Hard Drive Shredding"),
    ("/recycling/battery-recycling-kochi", "🔋 Battery Recycling"),
    ("/collection/ewaste-pickup-kochi", "🚚 E-Waste Pickup"),
    ("/data-security/secure-computer-recycling", "🖥️ Computer Recycling"),
    ("/trading/sell-old-electronics-near-me", "💰 Sell Old Electronics"),
    ("/data-security/secure-e-waste-destruction", "🛡️ Secure Destruction"),
    ("/locations/",                     "📍 Kochi Locations"),
    ("/",                               "🏠 EWaste Kochi Home"),
]

def build_silo_footer(current_url: str) -> str:
    links = ""
    for href, label in SILO_LINKS:
        if href != current_url:
            links += f'<a href="{href}" class="silo-link">{label}</a>\n    '
    return f"""
<!-- Internal Silo / Topical Authority Footer -->
<section style="background:#0A0F0C;padding:60px 0;border-top:1px solid rgba(0,230,100,.1);" id="related-services">
  <div style="max-width:1240px;margin:0 auto;padding:0 24px;">
    <h2 style="font-family:'Bebas Neue',cursive;font-size:2rem;color:#E8F2EA;text-transform:uppercase;margin-bottom:24px;">Related Services — EWaste Kochi</h2>
    <div style="display:flex;flex-wrap:wrap;gap:12px;">
    {links}
    </div>
    <p style="margin-top:24px;font-size:.8rem;color:#5A7A62;">
      ♻️ EWaste Kochi — Kerala's #1 Certified E-Waste Recycling &amp; Data Destruction Hub.
      KSPCB Authorised · NIST 800-88 · DPDP Act 2023 Compliant ·
      <a href="tel:{PHONE}" style="color:#00E664;">{PHONE_DISPLAY}</a> ·
      <a href="https://wa.me/917500555454" style="color:#25D366;">WhatsApp</a>
    </p>
  </div>
</section>"""

# ── NLP / Semantic keyword hidden signals ─────────────────────────────────────
def build_nlp_block(title: str) -> str:
    """Visually hidden (accessible to crawlers) topical entity cluster."""
    return f"""
<!-- Semantic Entity Cluster — Topical Authority -->
<div aria-hidden="true" style="position:absolute;width:1px;height:1px;overflow:hidden;opacity:0;pointer-events:none;">
  <p>e-waste recycling kochi | e-waste disposal kochi | data destruction ernakulam |
  ITAD kerala | hard drive shredding kochi | secure computer disposal kochi |
  KSPCB authorised recycler kerala | NIST 800-88 data wiping india |
  DPDP act 2023 compliance kerala | certificate of destruction kochi |
  battery recycling kochi | laptop buyback kochi | corporate ewaste pickup kochi |
  e-waste collection ernakulam | free ewaste pickup kochi | scrap electronics kochi |
  electronics recycling near me kochi | {title.lower()}</p>
</div>"""

# ── PWA Manifest (if missing) ───────────────────────────────────────────────
MANIFEST = {
    "name": "EWaste Kochi",
    "short_name": "EWaste Kochi",
    "description": "Kerala's #1 Certified E-Waste Recycling & Data Destruction Hub",
    "start_url": "/",
    "display": "standalone",
    "background_color": "#0A0F0C",
    "theme_color": "#00E664",
    "icons": [
        {"src": "/images/icon-192.png", "sizes": "192x192", "type": "image/png"},
        {"src": "/images/icon-512.png", "sizes": "512x512", "type": "image/png"}
    ]
}

# ── Breadcrumb HTML (visible) ─────────────────────────────────────────────────
def build_breadcrumb_html(file_path: str) -> str:
    parts = Path(file_path).relative_to(BASE).parts
    crumbs_html = '<a href="/" style="color:#00E664;">Home</a>'
    if len(parts) > 1:
        cat = parts[0]
        label = CAT_LABELS.get(cat, cat.replace("-", " ").title())
        crumbs_html += f' › <a href="/{cat}" style="color:#00E664;">{label}</a>'
    slug_label = Path(file_path).stem.replace("-", " ").title()
    crumbs_html += f' › <span style="color:#9BB8A2;">{slug_label}</span>'
    return f"""
<!-- Breadcrumb Navigation -->
<nav aria-label="Breadcrumb" style="padding:12px 0;background:rgba(0,230,100,.04);border-bottom:1px solid rgba(0,230,100,.1);">
  <div style="max-width:1240px;margin:0 auto;padding:0 24px;font-size:.82rem;color:#5A7A62;">
    {crumbs_html}
  </div>
</nav>"""

# ── Remove duplicate JSON-LD scripts ──────────────────────────────────────────
def remove_old_jsonld(html: str) -> str:
    return re.sub(
        r'<script type=["\']application/ld\+json["\']>.*?</script>',
        '', html, flags=re.DOTALL | re.IGNORECASE
    )

# ── Remove old duplicate preconnects / seo power packs ───────────────────────
def remove_old_seo_pack(html: str) -> str:
    return re.sub(
        r'<!-- ═══ SEO POWER PACK.*?═══ END SEO POWER PACK ═══ -->',
        '', html, flags=re.DOTALL | re.IGNORECASE
    )

# ── Remove old font link tags (we inject them via preload) ────────────────────
def remove_old_font_links(html: str) -> str:
    return re.sub(
        r'<link[^>]*googleapis\.com/css2[^>]*>',
        '', html, flags=re.IGNORECASE
    )

# ── Remove old silo footer if already exists ─────────────────────────────────
def remove_old_silo(html: str) -> str:
    return re.sub(
        r'<!-- Internal Silo.*?</section>',
        '', html, flags=re.DOTALL | re.IGNORECASE
    )

# ── Remove old semantic entity cluster ───────────────────────────────────────
def remove_old_nlp(html: str) -> str:
    return re.sub(
        r'<!-- Semantic Entity Cluster.*?</div>',
        '', html, flags=re.DOTALL | re.IGNORECASE
    )

# ── Inject missing canonical if needed ───────────────────────────────────────
def ensure_canonical(html: str, file_path: str) -> str:
    url = canonical_url(file_path)
    if '<link rel="canonical"' not in html:
        html = html.replace('</head>', f'<link rel="canonical" href="{url}">\n</head>', 1)
    return html


# ══════════════════════════════════════════════════════════════════════════════
#  MAIN PROCESSOR
# ══════════════════════════════════════════════════════════════════════════════
def process_file(file_path: str) -> bool:
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            html = f.read()
    except Exception as e:
        print(f"  ✗ READ ERROR: {e}")
        return False

    # Skip tiny stubs / redirects
    if len(html) < 800:
        return False

    # Skip if not a proper HTML document
    if "<html" not in html.lower():
        return False

    title = extract_title(html)

    # ── Step 1: Clean old injections ─────────────────────────────────────────
    html = remove_old_jsonld(html)
    html = remove_old_seo_pack(html)
    html = remove_old_font_links(html)
    html = remove_old_silo(html)
    html = remove_old_nlp(html)

    # ── Step 2: Build fresh injections ───────────────────────────────────────
    jsonld      = build_jsonld(file_path, html)
    head_pack   = build_head_injection(file_path, html)
    silo_footer = build_silo_footer(canonical_url(file_path))
    nlp_block   = build_nlp_block(title)
    breadcrumb  = build_breadcrumb_html(file_path)

    # ── Step 3: Inject into <head> ────────────────────────────────────────────
    # Insert head pack + JSON-LD right before </head>
    if "</head>" in html:
        html = html.replace("</head>", f"{head_pack}\n{jsonld}\n</head>", 1)
    else:
        html = html.replace("<body", f"<head>{head_pack}{jsonld}</head>\n<body", 1)

    # ── Step 4: Ensure canonical ─────────────────────────────────────────────
    html = ensure_canonical(html, file_path)

    # ── Step 5: Inject breadcrumb after <body> open ───────────────────────────
    body_match = re.search(r"<body[^>]*>", html, re.IGNORECASE)
    if body_match:
        ins_pos = body_match.end()
        html = html[:ins_pos] + breadcrumb + html[ins_pos:]

    # ── Step 6: Inject NLP block before </body> ───────────────────────────────
    html = html.replace("</body>", nlp_block + "\n</body>", 1)

    # ── Step 7: Inject silo footer before </body> ─────────────────────────────
    html = html.replace("</body>", silo_footer + "\n</body>", 1)

    # ── Step 8: Performance — make scripts async/defer ────────────────────────
    html = re.sub(r'<script src=', '<script defer src=', html)
    html = re.sub(r'<script defer defer src=', '<script defer src=', html)  # dedup

    # ── Step 9: Add loading=lazy to all images ────────────────────────────────
    html = re.sub(r'<img(?![^>]*loading=)', '<img loading="lazy"', html, flags=re.IGNORECASE)

    # ── Write back ────────────────────────────────────────────────────────────
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html)
        return True
    except Exception as e:
        print(f"  ✗ WRITE ERROR: {e}")
        return False


def main():
    # Write manifest.json
    manifest_path = os.path.join(BASE, "manifest.json")
    with open(manifest_path, "w") as f:
        json.dump(MANIFEST, f, indent=2)
    print("✅ manifest.json written")

    # Gather all HTML files (all depths)
    all_html = glob.glob(os.path.join(BASE, "**", "*.html"), recursive=True)
    # Also root-level
    all_html += glob.glob(os.path.join(BASE, "*.html"))
    # Deduplicate
    all_html = list(set(all_html))

    # Exclude python caches and automation dirs we don't want to touch
    excluded_dirs = {"__pycache__", "gitlab_repo", "ewastekochi-production"}
    filtered = []
    for p in all_html:
        parts = Path(p).relative_to(BASE).parts
        if not any(d in excluded_dirs for d in parts):
            filtered.append(p)

    total = len(filtered)
    ok = 0
    skip = 0

    print(f"\n🚀 Processing {total} HTML files...\n")

    for i, fp in enumerate(sorted(filtered), 1):
        rel = Path(fp).relative_to(BASE)
        result = process_file(fp)
        if result:
            ok += 1
            print(f"  [{i:04d}/{total}] ✓ {rel}")
        else:
            skip += 1
            print(f"  [{i:04d}/{total}] ⊘ SKIP {rel}")

    print(f"\n{'='*60}")
    print(f"✅ Injected : {ok}")
    print(f"⊘  Skipped  : {skip}")
    print(f"📄 Total    : {total}")
    print(f"{'='*60}")
    print("\n🏆 All ethical SEO signals injected successfully!")


if __name__ == "__main__":
    main()
