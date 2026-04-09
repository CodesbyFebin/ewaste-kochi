#!/usr/bin/env python3
"""
EWaste Kochi — Lightweight Internal Link Weaver v3
Uses simple string splitting to avoid regex catastrophic backtracking.
Injects Related Services / Related Articles blocks sitewide.
Run from /media/hp-ml10/Projects/EwasteKochi.com/
"""
import os, re

ROOT = "/media/hp-ml10/Projects/ewastekochi-production/ewastekochi"

# Keyword → URL  (ordered longest-first to avoid partial matches)
LINKS = [
    ("Digital Personal Data Protection", "/compliance/dpdp-act-2023-penalties.html"),
    ("DPDP Act 2023", "/compliance/dpdp-act-2023-penalties.html"),
    ("DPDP Act", "/compliance/dpdp-act-2023-penalties.html"),
    ("NIST SP 800-88", "/compliance/nist-800-88-explained.html"),
    ("NIST 800-88", "/compliance/nist-800-88-explained.html"),
    ("DoD 5220.22-M", "/compliance/dod-5220-22m-guide.html"),
    ("Certificate of Destruction", "/certificate-of-destruction.html"),
    ("chain of custody", "/compliance/chain-of-custody.html"),
    ("ISO 27001", "/compliance/iso-27001-compliance.html"),
    ("certified data sanitization", "/data-destruction-kochi.html"),
    ("data destruction", "/data-destruction-kochi.html"),
    ("hard drive shredding", "/hard-drive-shredding-kochi.html"),
    ("physical shredding", "/hard-drive-shredding-kochi.html"),
    ("SSD destruction", "/hard-drive-shredding-kochi.html"),
    ("bulk laptop buyback", "/bulk-laptop-buyback.html"),
    ("MacBook buyback", "/sell-old-laptop-kochi.html"),
    ("sell old laptop", "/sell-old-laptop-kochi.html"),
    ("sell your laptop", "/sell-old-laptop-kochi.html"),
    ("laptop buyback", "/sell-old-laptop-kochi.html"),
    ("sell old phone", "/sell-old-phone-kochi.html"),
    ("sell your phone", "/sell-old-phone-kochi.html"),
    ("smartphone buyback", "/sell-old-phone-kochi.html"),
    ("server disposal", "/server-disposal-kochi.html"),
    ("office clearance", "/office-clearance.html"),
    ("IT asset disposal", "/itad-kochi.html"),
    ("IT asset disposition", "/itad-kochi.html"),
    ("free corporate pickup", "/book-free-pickup.html"),
    ("free pickup", "/book-free-pickup.html"),
    ("book a pickup", "/book-free-pickup.html"),
    ("instant quote", "/get-instant-quote.html"),
    ("KSPCB", "/compliance/kerala-pcb-authorization.html"),
    ("EPR", "/compliance/epr-framework-india.html"),
]

RELATED_SERVICES = """
<div class="section section-alt" style="padding:48px 0">
  <div class="wrap">
    <div class="section-tag">Explore Services</div>
    <h2 class="section-title" style="margin-bottom:28px">Related Services</h2>
    <div class="grid-3">
      <a href="/itad-kochi.html" class="card" style="display:block"><div class="card-icon">🏢</div><div class="card-title">Corporate ITAD</div><div class="card-desc">End-to-end IT Asset Disposition with NIST wipe and Certificate of Destruction.</div></a>
      <a href="/data-destruction-kochi.html" class="card" style="display:block"><div class="card-icon">💾</div><div class="card-title">Data Destruction</div><div class="card-desc">NIST 800-88 and DoD 5220.22-M certified wipe or physical shredding.</div></a>
      <a href="/sell-old-laptop-kochi.html" class="card" style="display:block"><div class="card-icon">💻</div><div class="card-title">Laptop Buyback</div><div class="card-desc">We beat Cashify by 15–20% on business models. Same-day UPI payment.</div></a>
      <a href="/hard-drive-shredding-kochi.html" class="card" style="display:block"><div class="card-icon">⚙️</div><div class="card-title">Hard Drive Shredding</div><div class="card-desc">Physical destruction with auditable chain of custody. On-site available.</div></a>
      <a href="/compliance/dpdp-act-2023-penalties.html" class="card" style="display:block"><div class="card-icon">⚖️</div><div class="card-title">DPDP Act 2023</div><div class="card-desc">Understand penalties up to ₹250 Crore and what your business must do.</div></a>
      <a href="/get-instant-quote.html" class="card" style="display:block"><div class="card-icon">📋</div><div class="card-title">Get Free Quote</div><div class="card-desc">2-hour response. Free pickup for 50+ devices anywhere in Ernakulam.</div></a>
    </div>
  </div>
</div>
"""

RELATED_ARTICLES = """
<div class="section" style="padding:48px 0">
  <div class="wrap">
    <div class="section-tag">Knowledge Hub</div>
    <h2 class="section-title" style="margin-bottom:28px">Related Articles</h2>
    <div class="grid-3">
      <a href="/blog/is-formatting-enough-delete-data.html" class="card" style="display:block;text-decoration:none"><div style="font-size:.7rem;font-weight:700;color:var(--green);margin-bottom:10px">🔥 Most Read</div><div class="card-title">Is Formatting Your Hard Drive Enough to Delete Data?</div><div style="font-size:.72rem;color:var(--muted);margin-top:8px">📖 8 min read</div></a>
      <a href="/blog/dpdp-act-impact-startups.html" class="card" style="display:block;text-decoration:none"><div style="font-size:.7rem;font-weight:700;color:var(--green);margin-bottom:10px">⚖️ Compliance</div><div class="card-title">DPDP Act 2023 — What Kerala Startups Must Do Now</div><div style="font-size:.72rem;color:var(--muted);margin-top:8px">📖 6 min read</div></a>
      <a href="/blog/nist-800-88-vs-dod-standards.html" class="card" style="display:block;text-decoration:none"><div style="font-size:.7rem;font-weight:700;color:var(--green);margin-bottom:10px">🛡️ Technical</div><div class="card-title">NIST 800-88 vs DoD 5220.22-M — Which Standard?</div><div style="font-size:.72rem;color:var(--muted);margin-top:8px">📖 8 min read</div></a>
      <a href="/blog/corporate-itad-checklist.html" class="card" style="display:block;text-decoration:none"><div style="font-size:.7rem;font-weight:700;color:var(--green);margin-bottom:10px">✅ Checklist</div><div class="card-title">Corporate ITAD Checklist — 20 Steps for IT Managers</div><div style="font-size:.72rem;color:var(--muted);margin-top:8px">📖 7 min read</div></a>
      <a href="/blog/cashify-vs-ewaste-kochi-laptop-buyback.html" class="card" style="display:block;text-decoration:none"><div style="font-size:.7rem;font-weight:700;color:var(--green);margin-bottom:10px">🏆 Comparison</div><div class="card-title">Cashify vs EWaste Kochi — Better Resale Value?</div><div style="font-size:.72rem;color:var(--muted);margin-top:8px">📖 5 min read</div></a>
      <a href="/blog/ewaste-laws-kerala.html" class="card" style="display:block;text-decoration:none"><div style="font-size:.7rem;font-weight:700;color:var(--green);margin-bottom:10px">📋 Legal</div><div class="card-title">E-Waste Laws in Kerala 2026 — Business Compliance Guide</div><div style="font-size:.72rem;color:var(--muted);margin-top:8px">📖 9 min read</div></a>
    </div>
  </div>
</div>
"""

def link_text_in_body(body, url_path):
    """Simple word-boundary injection into text nodes only.
    Avoids regex catastrophic backtracking by pre-splitting on '<'."""
    result = []
    used = set()
    # Split into alternating text / tag segments
    segments = re.split(r'(<[^>]+>)', body)
    for seg in segments:
        if seg.startswith('<'):
            result.append(seg)
            continue
        # Text node — try each keyword
        for kw, url in LINKS:
            if url in url_path or url in used:
                continue
            idx = seg.lower().find(kw.lower())
            if idx == -1:
                continue
            # Confirm word boundary (no alpha before/after)
            pre = seg[idx-1] if idx > 0 else ' '
            post = seg[idx+len(kw)] if idx+len(kw) < len(seg) else ' '
            if pre.isalpha() or post.isalpha():
                continue
            anchor = f'<a href="{url}" style="color:var(--green);text-decoration:underline;text-decoration-color:rgba(0,232,122,.3)">{seg[idx:idx+len(kw)]}</a>'
            seg = seg[:idx] + anchor + seg[idx+len(kw):]
            used.add(url)
            break  # one keyword at a time per segment pass
        result.append(seg)
    return ''.join(result)


def inject_before_footer(content, block, marker):
    if marker in content:
        return content
    pos = content.find('<footer>')
    if pos == -1:
        return content
    return content[:pos] + f'<!-- {marker} -->\n' + block + '\n' + content[pos:]


def classify(filepath):
    r = filepath.replace(ROOT, '')
    if '/blog/' in r and 'index' not in r: return 'blog'
    if '/compliance/' in r and 'index' not in r: return 'compliance'
    if '/industries/' in r and 'index' not in r: return 'industry'
    if '/locations/' in r and 'index' not in r: return 'location'
    if '/comparisons/' in r and 'index' not in r: return 'comparison'
    basename = os.path.basename(filepath)
    generics = {'contact.html','faq.html','portal-login.html','privacy-policy.html',
                'terms-of-service.html','refund-policy.html','about.html','404.html'}
    if basename in generics: return 'skip'
    return 'service'


def run():
    skip_dirs = {'scripts','css','js','images','__pycache__','.git','gitlab_repo'}
    all_html = []
    for root, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in skip_dirs]
        all_html += [os.path.join(root, f) for f in files if f.endswith('.html')]

    changed = 0
    for fp in all_html:
        ptype = classify(fp)
        if ptype == 'skip':
            print(f'  — skip: {fp.replace(ROOT,"")}')
            continue

        with open(fp, 'r', encoding='utf-8') as fh:
            content = fh.read()
        original = content
        url_path = fp.replace(ROOT, '')

        # Find the body content area (after nav, before footer)
        crumb_pos = content.find('<div class="wrap"><div class="breadcrumb">')
        footer_pos = content.find('<footer>')
        if crumb_pos != -1 and footer_pos != -1:
            head = content[:crumb_pos]
            body = content[crumb_pos:footer_pos]
            tail = content[footer_pos:]
            body = link_text_in_body(body, url_path)
            content = head + body + tail

        # Inject related blocks
        if ptype == 'blog':
            content = inject_before_footer(content, RELATED_SERVICES, 'REL_SERVICES')
        elif ptype in ('service','compliance','industry','comparison'):
            content = inject_before_footer(content, RELATED_ARTICLES, 'REL_ARTICLES')
        elif ptype == 'location':
            content = inject_before_footer(content, RELATED_SERVICES, 'REL_SERVICES')

        if content != original:
            with open(fp, 'w', encoding='utf-8') as fh:
                fh.write(content)
            print(f'  ✓ wired: {url_path}')
            changed += 1

    print(f'\n✅ Wired {changed} pages.')

run()
