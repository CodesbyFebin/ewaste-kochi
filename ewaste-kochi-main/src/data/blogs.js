// ═══════════════════════════════════════════════════════════════════
// BLOG HUB — 20 Categories (Pillar-driven Content Strategy)
// ═══════════════════════════════════════════════════════════════════

export const blogCategories = [
  { id: 'itad', name: 'Corporate ITAD Strategies' },
  { id: 'compliance', name: 'E-Waste Laws & Compliance' },
  { id: 'data', name: 'Data Destruction 101' },
  { id: 'kochi', name: 'Kochi Local Disposal Guides' },
  { id: 'recycling-tech', name: 'Electronic Recycling Technology' },
  { id: 'lifecycle', name: 'Sustainable IT Lifecycle' },
  { id: 'battery', name: 'Battery Recycling Safety' },
  { id: 'dpdp', name: 'DPDP Act 2023 for IT' },
  { id: 'precious', name: 'Precious Metal Recovery (Urban Mining)' },
  { id: 'resale', name: 'Device Buyback & Resale Tips' },
  { id: 'hazardous', name: 'Hazardous Waste Management' },
  { id: 'circular', name: 'Circular Economy in Kerala' },
  { id: 'datacenter', name: 'Data Center Decommissioning' },
  { id: 'sme', name: 'Small Business E-Waste Solutions' },
  { id: 'environment', name: 'Environmental Impact Tracking' },
  { id: 'printer', name: 'Toner & Printer Stewardship' },
  { id: 'networking', name: 'Networking Gear Retirement' },
  { id: 'mobile', name: 'Mobile & Tablet Recycling' },
  { id: 'green-it', name: 'Future of Green Computing' },
  { id: 'epr', name: 'EPR Fulfillment for Manufacturers' },
];

/**
 * Programmatic Blog Generator Blueprint
 * Every category aims for 100 long-tail keywords. 
 * This array can be scaled with thousands of titles.
 */
export const blogs = [
  {
    slug: 'dpdp-act-2023-it-disposal-compliance',
    title: 'How India’s DPDP Act 2023 Influences IT Disposal for Kochi Businesses',
    category: 'dpdp',
    excerpt: 'The DPDP Act 2023 mandates strict data privacy rules for retired devices. Failing to follow NIST standards in Kochi can now cost corporatations ₹250 crore...',
    content: `
      <h2>The New Data Reality for Kerala Enterprises</h2>
      <p>India's landmark <strong>DPDP Act 2023</strong> has changed the legal landscape for IT procurement and disposal. In Kochi's thriving IT corridors, every discarded laptop is now a potential liability.</p>
      
      <h3>The Rule of Data Destruction</h3>
      <p>Under the act, businesses are data fiduciaries. When you retire a computer, you must ensure all personal data is permanently deleted. Simply formatting a drive does not satisfy the legal requirement of the act.</p>
      
      <h3>How to Stay Compliant in Kochi</h3>
      <p>To avoid massive statutory penalties, companies in Infopark and Smart City should adopt a three-pillar ITAD strategy: 
      1. Certified Wiping; 2. Documentation of Disposal; 3. Use of KSPCB authorized recyclers.</p>
    `,
    date: '2026-03-31',
    author: 'Compliance Team, EWaste Kochi',
  },
  {
    slug: 'itad-roi-kochi-enterprise',
    title: 'Maximizing ROI: Why Kochi Enterprises are Switching to Certified ITAD',
    category: 'itad',
    excerpt: 'Most companies treat old hardware as junk. We show you how IT Asset Disposition can actually recover up to 20% of your initial procurement cost...',
    content: `
      <h2>ROI in the IT Hardware Lifecycle</h2>
      <p>Professional ITAD is a financial strategy as much as an environmental one. For large Kochi businesses, retiring 500+ laptops is a major logistical event.</p>
      
      <h3>Remarketing Functional Assets</h3>
      <p>Functional devices can be refurbishd and resold insecondary markets. We handle the secure wiping and remarketing for you, returning a portion of the value to your budget.</p>
      
      <h3>Logistics Savings in Ernakulam</h3>
      <p>By using an authorized local partner like EWaste Kochi, you save on transportation costs and ensure a faster, more transparent decommissioning cycle.</p>
    `,
    date: '2026-03-25',
    author: 'Operations Head, EWaste Kochi',
  },
  // Scale this to 2000+ entries
];

export const getPillarBlogs = (catId) => blogs.filter(b => b.category === catId);
export const getBlogBySlug = (slug) => blogs.find(b => b.slug === slug);
export const getRecentBlogs = (count = 10) => blogs.slice(0, count);
