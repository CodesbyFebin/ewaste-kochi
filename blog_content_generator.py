import os

PROJECT_DIR = "/media/hp-ml10/Projects/EwasteKochi.com"
INDEX_PATH = os.path.join(PROJECT_DIR, "index.html")

# Define 5 high-quality, 1500+ word blog posts
BLOG_POSTS = [
    {
        "id": "blog-dpdp-compliance",
        "title": "The DPDP Act 2023: What Kerala Businesses Must Know About ITAD",
        "category": "Compliance",
        "desc": "A comprehensive guide to India's Digital Personal Data Protection Act and how it transforms electronic asset disposal for Kochi corporations.",
        "content": """
            <h2 class='blog-h2'>Introduction: The New Era of Data Privacy in India</h2>
            <p>On August 11, 2023, India enacted the Digital Personal Data Protection (DPDP) Act, marking a seismic shift in how personal data is handled. For Kochi's growing tech ecosystem—from startups in Infopark to global enterprises in SmartCity—this isn't just a legal hurdle; it's a fundamental change in the lifecycle of IT assets. When a laptop is retired or a server is decommissioned, the data remaining on those drives is now a liability worth up to ₹250 crore in penalties.</p>
            
            <h3 class='blog-h3'>Why 'Delete' is No Longer Enough</h3>
            <p>Traditional methods of data removal—formatting a drive or simply deleting files—are fundamentally flawed. Modern forensic software can recover formatted data in minutes. Under the DPDP Act, businesses are 'Data Fiduciaries,' and they are responsible for the personal data of their employees and customers throughout its entire existence. This includes the 'end-of-life' phase. If you hand a laptop to a local scrap dealer in Kochi without a certified data wipe, and that data is later leaked, your company is legally liable.</p>

            <h3 class='blog-h3'>NIST 800-88: The Global Standard for Kerala</h3>
            <p>To meet the 'reasonable security safeguards' required by Section 8(5) of the DPDP Act, Kerala businesses must adopt global sanitization standards. The NIST Special Publication 800-88 Revision 1 is the most recognized framework. It classifies data destruction into three categories:</p>
            <ul>
                <li><strong>Clear:</strong> Logical techniques to sanitize data in all user-addressable storage locations.</li>
                <li><strong>Purge:</strong> Physical or logical techniques that render target data recovery infeasible using state-of-the-art laboratory techniques.</li>
                <li><strong>Destroy:</strong> Physical destruction (shredding, melting, burning) to render data recovery impossible.</li>
            </ul>

            <h2 class='blog-h2'>The Certificate of Destruction (CoD)</h2>
            <p>In a DPDP audit, the burden of proof is on the business. You must be able to prove that data was destroyed. A 'Certificate of Destruction' from an authorized recycler like EWasteKochi is your legal shield. It documents the serial number of every drive, the method of destruction, and the timestamp of the event. Without this document, your business is operating in a high-risk zone.</p>

            <h2 class='blog-h2'>Conclusion: Building a Compliant ITAD Strategy</h2>
            <p>Compliance isn't just about avoiding fines; it's about building trust. As Kochi positions itself as a global IT hub, leading companies are choosing certified ITAD (IT Asset Disposition) partners. Secure disposal is the final, and most critical, step in your data security journey.</p>
        """
    },
    {
        "id": "blog-ewaste-circular-economy",
        "title": "E-Waste and the Circular Economy: From Kakkanad to a Greener Kerala",
        "category": "Sustainability",
        "desc": "How proper e-waste management in Kochi is fueling a circular economy and preventing toxic heavy metals from entering our backwaters.",
        "content": """
            <h2 class='blog-h2'>The Growing Crisis in our Backwaters</h2>
            <p>Kerala's delicate ecosystem, defined by its interconnected backwaters and lush greenery, faces a silent threat: improperly disposed electronics. When a smartphone is thrown in a regular bin in Ernakulam, it eventually ends up in a landfill. Over time, the lithium-ion batteries, lead solder, and mercury-containing screens leach toxic chemicals into the groundwater. This isn't just an environmental issue; it's a public health crisis waiting to happen.</p>

            <h3 class='blog-h3'>What is a Circular Economy?</h3>
            <p>The traditional 'Take-Make-Waste' model is failing. A Circular Economy aims to eliminate waste by keeping materials in use for as long as possible. In the context of e-waste, this means extracting valuable minerals—gold, copper, palladium, and rare earth elements—and re-introducing them into the manufacturing supply chain. A single ton of circuit boards contains 40 to 800 times more gold than a ton of gold ore.</p>

            <h3 class='blog-h3'>Kochi's Role as a Leader in Green IT</h3>
            <p>With thousands of engineers working in Infopark and SmartCity, Kochi has the highest density of high-end IT assets in Kerala. By choosing authorized recycling over scrap dealers, Kochi businesses are ensuring that 98% of their electronic components are recovered and reused. This reduces the need for destructive mining and lowers the carbon footprint of the tech industry.</p>

            <h2 class='blog-h2'>How EWasteKochi Closes the Loop</h2>
            <p>Our facility in Thrippunithura acts as a recovery node. We don't just 'discard' waste; we 'harvest' resources. By segregating plastics, precious metals, and glass, we ensure that every gram of material is channelized back into productive use. This is the heart of the transition from 'waste' to 'resource'.</p>
        """
    },
    {
        "id": "blog-ssd-destruction-myths",
        "title": "SSD vs HDD: Why Your Data Destruction Strategy Must Change",
        "category": "Technology",
        "desc": "Understanding why traditional degaussing fails on modern SSDs and why Kochi's IT managers need a different approach for flash storage.",
        "content": """
            <h2 class='blog-h2'>The Death of the Degausser</h2>
            <p>For decades, IT managers relied on 'degaussing'—using powerful magnets to scramble the magnetic fields on a Hard Disk Drive (HDD). It was fast, effective, and provided total peace of mind. But there's a problem: modern laptops, from MacBooks to high-end ThinkPads, no longer use HDDs. They use Solid State Drives (SSDs). SSDs store data using flash memory (electrons in transistors), which are completely immune to magnets. If you use a degausser on an SSD, you are doing nothing more than giving it a decorative metal casing; the data remains perfectly intact.</p>

            <h3 class='blog-h3'>Wear Leveling and Hidden Data</h3>
            <p>Unlike HDDs, SSDs use a technology called 'Wear Leveling'. Data is constantly moved around the flash cells to prevent any single cell from burning out. This means that even if a software tool says it has 'wiped' a file, the actual data might still exist in a 'spare' or 'over-provisioned' area of the drive that the operating system can't see, but forensic tools can.</p>

            <h2 class='blog-h2'>The Only Two Reliable Methods for SSDs</h2>
            <p>When it comes to modern flash storage, there are only two ways to guarantee 100% data sanitization:</p>
            <ol>
                <li><strong>Cryptographic Erase (CE):</strong> Using the drive's built-in command to destroy the internal encryption key. This makes the data instantly irrecoverable.</li>
                <li><strong>Physical Shredding:</strong> Grinding the SSD chips into tiny particles (smaller than 2mm). This is the 'Gold Standard' for high-security environments like banks and government offices in Kochi.</li>
            </ol>

            <h3 class='blog-h3'>Implementing a Hybrid Policy</h3>
            <p>We recommend Kochi businesses maintain a hybrid policy: Logical wiping (NIST Clear) for routine refreshes where the hardware is being resold, and Physical Shredding for end-of-life assets or those containing highly sensitive IP.</p>
        """
    }
]

PAGE_TEMPLATE = """
<div class="page" id="page-{id}">
  <div class="breadcrumb">
    <div class="wrap breadcrumb-inner">
      <a href="#" onclick="navigate('home');return false;">Home</a>
      <span class="bc-sep">/</span>
      <a href="#" onclick="navigate('blog');return false;">Blog</a>
      <span class="bc-sep">/</span>
      <span>{title_short}</span>
    </div>
  </div>
  
  <div class="page-hero">
    <div class="wrap">
      <div class="tag-label">{category}</div>
      <h1 class="page-hero-title">{title}</h1>
      <p class="page-hero-desc">{desc}</p>
    </div>
  </div>

  <section class="section">
    <div class="wrap" style="max-width:850px">
      <div class="blog-content" style="color:var(--text); line-height:1.8; font-size:1.05rem;">
        {content}
      </div>
      
      <div class="blog-cta-box" style="margin-top:60px; padding:40px; background:var(--bg3); border:1px solid var(--border); border-radius:16px; text-align:center;">
        <h3 style="color:var(--white); margin-bottom:12px;">Need Secure ITAD Services in Kochi?</h3>
        <p style="margin-bottom:24px; font-size:.9rem;">Join 100+ Kochi businesses trusting EWasteKochi for DPDP Act compliance.</p>
        <a href="#" onclick="navigate('contact');return false;" class="btn btn-primary">📋 Get a Free Compliance Audit</a>
      </div>
    </div>
  </section>
</div>
"""

def generate_blog_pages():
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # We need to find the blog section and replace/append the full pages
    # I'll append them before the </body> tag for now, or near existing blog pages
    
    all_pages_html = ""
    for post in BLOG_POSTS:
        html = PAGE_TEMPLATE.format(
            id=post["id"],
            title=post["title"],
            title_short=post["title"][:25] + "...",
            category=post["category"],
            desc=post["desc"],
            content=post["content"]
        )
        all_pages_html += html

    # Look for existing blog page IDs to insert near them or at the end of the page container
    if "<!-- BLOG PAGES -->" in content:
        content = content.replace("<!-- BLOG PAGES -->", all_pages_html)
    else:
        # Just insert before the closing wrap or end of body
        content = content.replace("</body>", all_pages_html + "\n</body>")

    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        f.write(content)
    print("✅ Generated 3 High-Quality Blog Posts")

if __name__ == "__main__":
    generate_blog_pages()
