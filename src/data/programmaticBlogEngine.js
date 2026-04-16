import { blogs as legacyBlogs } from './blogs.js';
import { locations } from './locations.js';
import { services } from './services.js';

const serviceMap = new Map(services.map((service) => [service.slug, service]));
const locationMap = new Map(locations.map((location) => [location.slug, location]));
const legacyBlogMap = new Map(legacyBlogs.map((blog) => [blog.slug, blog]));

const topic = (slug, label, title, keyword, primaryServiceSlug, secondaryServiceSlug) => ({
  slug,
  label,
  title,
  keyword,
  primaryServiceSlug,
  secondaryServiceSlug,
});

export const blogLibraryConfig = {
  host: 'https://ewastekochi.com',
  basePath: '/blogs',
  subdomainHint: 'https://blogs.ewastekochi.com',
};

const geoTargets = [
  { slug: 'kakkanad', titleLabel: 'Kakkanad, Kochi', searchLabel: 'kakkanad kochi' },
  { slug: 'infopark-kochi', titleLabel: 'Infopark, Kochi', searchLabel: 'infopark kochi' },
  { slug: 'edappally', titleLabel: 'Edappally, Kochi', searchLabel: 'edappally kochi' },
  { slug: 'thrippunithura', titleLabel: 'Thrippunithura, Kochi', searchLabel: 'thrippunithura kochi' },
  { slug: 'vyttila', titleLabel: 'Vyttila, Kochi', searchLabel: 'vyttila kochi' },
  { slug: 'kalamassery', titleLabel: 'Kalamassery, Kochi', searchLabel: 'kalamassery kochi' },
  { slug: 'kottayam', titleLabel: 'Kottayam', searchLabel: 'kottayam kerala' },
  { slug: 'kollam', titleLabel: 'Kollam', searchLabel: 'kollam kerala' },
  { slug: 'kozhikode', titleLabel: 'Kozhikode', searchLabel: 'kozhikode kerala' },
  { slug: 'thiruvananthapuram', titleLabel: 'Thiruvananthapuram', searchLabel: 'thiruvananthapuram kerala' },
].map((target) => ({
  ...target,
  location: locationMap.get(target.slug),
}));

const categoryDefinitions = [
  {
    slug: 'disposal',
    name: 'Disposal Guides',
    emoji: 'Local',
    pageContext: 'pickup',
    summary: 'Local intent pages for disposal, drop-off, pickup, and item-specific recycling queries.',
    promise:
      'fast disposal answers with pickup, drop-off, and the right service path for homes, offices, and institutions',
    regulatoryLine:
      'Using a KSPCB-authorized partner matters because disposal is not just waste removal; it also involves data handling, transport records, and safe downstream recycling.',
    primaryServiceSlug: 'free-ewaste-pickup-kochi',
    supportServiceSlugs: ['e-waste-recycling-kochi', 'laptop-buyback-kochi', 'data-destruction-kochi'],
    legacySlugs: ['how-to-choose-itad-provider', 'ewaste-laws-kerala-2026'],
    shortTailKeywords: [
      'e waste disposal kochi',
      'electronics disposal near me',
      'where to recycle electronics',
      'free e waste pickup kochi',
      'e waste collection near me',
      'dispose old computers safely',
      'dispose old laptops kochi',
      'electronic waste disposal kochi',
      'electronics recycling near me',
      'ewaste pickup',
    ],
    publicQuestions: [
      'Where can I dispose old electronics without dealing with scrap shops?',
      'Can someone pick up mixed e-waste from my office?',
      'Is there a free drop-off option for small quantities?',
      'What should I do with devices that still contain data?',
    ],
    topics: [
      topic('old-laptops', 'old laptop disposal', 'Where to Dispose Old Laptops in {location} (Free Pickup Guide)', 'where to dispose old laptops in {location}', 'laptop-buyback-kochi', 'data-destruction-kochi'),
      topic('old-phones', 'old phone disposal', 'Where to Dispose Old Phones in {location} Without Data Risk', 'where to dispose old phones in {location}', 'mobile-recycling-kochi', 'battery-recycling-kochi'),
      topic('office-computers', 'office computer disposal', 'How to Dispose Office Computers in {location} Safely', 'office computer disposal in {location}', 'corporate-ewaste-kochi', 'data-destruction-kochi'),
      topic('monitors-tvs', 'monitor and TV disposal', 'Monitor and TV Disposal in {location}: What to Do First', 'monitor disposal in {location}', 'tv-monitor-recycling-kochi', 'e-waste-recycling-kochi'),
      topic('printers-copiers', 'printer disposal', 'Printer and Copier Disposal in {location} for Offices and Schools', 'printer disposal in {location}', 'printer-recycling-kochi', 'corporate-ewaste-kochi'),
      topic('servers-network', 'server disposal', 'Where to Dispose Servers and Network Gear in {location}', 'server disposal in {location}', 'server-recycling-kochi', 'network-equipment-disposal-kochi'),
      topic('mixed-household', 'mixed household e-waste', 'How to Dispose Mixed Household E-Waste in {location}', 'household e-waste disposal in {location}', 'free-ewaste-pickup-kochi', 'e-waste-recycling-kochi'),
      topic('corporate-clearance', 'corporate e-waste clearance', 'Corporate E-Waste Clearance Checklist for {location}', 'corporate e-waste clearance in {location}', 'corporate-ewaste-kochi', 'itad-kochi'),
      topic('same-day-pickup', 'same-day pickup', 'How Same-Day E-Waste Pickup Works in {location}', 'same day e-waste pickup in {location}', 'free-ewaste-pickup-kochi', 'e-waste-recycling-kochi'),
      topic('donate-or-recycle', 'donate or recycle electronics', 'Donate or Recycle Electronics in {location}: Which Is Better?', 'donate or recycle electronics in {location}', 'e-waste-recycling-kochi', 'laptop-buyback-kochi'),
    ],
  },
  {
    slug: 'recycling',
    name: 'Recycling Guides',
    emoji: 'Eco',
    pageContext: 'recycling',
    summary: 'Programmatic answers for recycling process, material recovery, and service-specific recycling intent.',
    promise:
      'clear recycling guidance that explains what can be recovered, what needs secure handling, and how pickup works in practice',
    regulatoryLine:
      'Searchers comparing recycling options usually need proof that the recycler is authorized, transparent about downstream handling, and able to document responsible disposal.',
    primaryServiceSlug: 'e-waste-recycling-kochi',
    supportServiceSlugs: ['free-ewaste-pickup-kochi', 'battery-recycling-kochi', 'server-recycling-kochi'],
    legacySlugs: ['ewaste-laws-kerala-2026', 'how-to-choose-itad-provider'],
    shortTailKeywords: [
      'e waste recycling kochi',
      'electronic recycling near me',
      'how to recycle electronics',
      'computer recycling kochi',
      'mobile recycling center',
      'battery recycling kochi',
      'certified e-waste recycler',
      'recycling electronics kerala',
      'local recycling centers',
      'recycle devices',
    ],
    publicQuestions: [
      'What actually happens after electronics are collected?',
      'Can working devices be reused instead of shredded?',
      'Do recyclers accept mixed loads from offices?',
      'How do I know recycling is legal and documented?',
    ],
    topics: [
      topic('electronics-process', 'electronics recycling process', 'How Electronics Recycling Works in {location}', 'electronics recycling in {location}', 'e-waste-recycling-kochi', 'free-ewaste-pickup-kochi'),
      topic('computer-recycling', 'computer recycling', 'Computer Recycling in {location} for Homes and Offices', 'computer recycling in {location}', 'e-waste-recycling-kochi', 'data-destruction-kochi'),
      topic('laptop-recycling', 'laptop recycling', 'Laptop Recycling in {location}: Reuse, Buyback, or Scrap?', 'laptop recycling in {location}', 'laptop-buyback-kochi', 'e-waste-recycling-kochi'),
      topic('mobile-recycling', 'mobile phone recycling', 'Mobile Phone Recycling in {location} with Safe Data Handling', 'mobile phone recycling in {location}', 'mobile-recycling-kochi', 'battery-recycling-kochi'),
      topic('printer-recycling', 'printer recycling', 'Printer Recycling in {location} for Offices, Schools, and Clinics', 'printer recycling in {location}', 'printer-recycling-kochi', 'corporate-ewaste-kochi'),
      topic('server-recycling', 'server recycling', 'Server Recycling in {location} for IT and Data Centre Teams', 'server recycling in {location}', 'server-recycling-kochi', 'itad-kochi'),
      topic('battery-recycling', 'battery recycling', 'Battery Recycling in {location}: What Needs Separate Handling?', 'battery recycling in {location}', 'battery-recycling-kochi', 'free-ewaste-pickup-kochi'),
      topic('zero-landfill', 'zero-landfill recycling', 'Zero-Landfill Electronics Recycling in {location}: What It Really Means', 'zero landfill electronics recycling in {location}', 'e-waste-recycling-kochi', 'corporate-ewaste-kochi'),
      topic('office-recycling', 'office recycling program', 'How to Run an Office Electronics Recycling Drive in {location}', 'office electronics recycling in {location}', 'corporate-ewaste-kochi', 'free-ewaste-pickup-kochi'),
      topic('pickup-vs-dropoff', 'pickup vs drop-off recycling', 'Pickup vs Drop-Off Recycling in {location}: Which Option Fits Better?', 'pickup vs drop off recycling in {location}', 'free-ewaste-pickup-kochi', 'e-waste-recycling-kochi'),
    ],
  },
  {
    slug: 'laptop-disposal',
    name: 'Laptop Disposal',
    emoji: 'Value',
    pageContext: 'laptop',
    summary: 'High-intent local pages focused on laptop buyback, disposal, secure wiping, and asset recovery.',
    promise:
      'a conversion-focused path for searchers who want either the best laptop value or a compliant retirement process',
    regulatoryLine:
      'Laptop searches often combine two different needs: resale value for working devices and certified data destruction for business-owned hardware.',
    primaryServiceSlug: 'laptop-buyback-kochi',
    supportServiceSlugs: ['data-destruction-kochi', 'itad-kochi', 'free-ewaste-pickup-kochi'],
    legacySlugs: ['laptop-resale-value-2026', 'is-formatting-enough-delete-data'],
    shortTailKeywords: [
      'sell old laptop kochi',
      'laptop recycling kochi',
      'laptop buyback kochi',
      'old laptop pickup',
      'macbook buyback kochi',
      'secure laptop disposal',
      'business laptop buyback',
      'damaged laptop recycling',
      'laptop resale value',
      'old computer buyers',
    ],
    publicQuestions: [
      'Should I sell the laptop or recycle it?',
      'Is formatting enough before I hand it over?',
      'Can a company retire 100 laptops in one pickup?',
      'Do damaged devices still have buyback value?',
    ],
    topics: [
      topic('sell-old-laptops', 'sell old laptops', 'Where to Sell Old Laptops in {location} for the Best Value', 'sell old laptops in {location}', 'laptop-buyback-kochi', 'data-destruction-kochi'),
      topic('business-laptop-buyback', 'business laptop buyback', 'Business Laptop Buyback in {location}: What IT Teams Should Expect', 'business laptop buyback in {location}', 'itad-kochi', 'laptop-buyback-kochi'),
      topic('macbook-buyback', 'MacBook buyback', 'MacBook Buyback in {location}: When to Resell vs Recycle', 'macbook buyback in {location}', 'laptop-buyback-kochi', 'data-destruction-kochi'),
      topic('damaged-laptop-recycling', 'damaged laptop recycling', 'Damaged Laptop Recycling in {location}: What Still Has Value?', 'damaged laptop recycling in {location}', 'laptop-buyback-kochi', 'e-waste-recycling-kochi'),
      topic('secure-laptop-disposal', 'secure laptop disposal', 'Secure Laptop Disposal in {location} for Teams Handling Client Data', 'secure laptop disposal in {location}', 'data-destruction-kochi', 'itad-kochi'),
      topic('school-laptop-disposal', 'school laptop disposal', 'School and College Laptop Disposal in {location}', 'school laptop disposal in {location}', 'corporate-ewaste-kochi', 'data-destruction-kochi'),
      topic('employee-returns', 'employee laptop returns', 'Employee Laptop Returns and Disposal Workflow in {location}', 'employee laptop disposal in {location}', 'itad-kochi', 'laptop-buyback-kochi'),
      topic('office-pickup', 'office laptop pickup', 'Office Laptop Pickup in {location} for Bulk Asset Refresh Projects', 'office laptop pickup in {location}', 'free-ewaste-pickup-kochi', 'itad-kochi'),
      topic('refurbish-vs-recycle', 'refurbish vs recycle laptops', 'Refurbish vs Recycle Laptops in {location}: Which Saves More Value?', 'refurbish or recycle laptops in {location}', 'laptop-buyback-kochi', 'e-waste-recycling-kochi'),
      topic('value-factors', 'laptop resale value', 'Laptop Resale Value in {location}: What Changes the Price Fast', 'laptop resale value in {location}', 'laptop-buyback-kochi', 'data-destruction-kochi'),
    ],
  },
  {
    slug: 'mobile-recycling',
    name: 'Mobile Recycling',
    emoji: 'Device',
    pageContext: 'mobile',
    summary: 'Question-led pages for smartphone buyback, tablet disposal, mobile fleet recycling, and secure data handling.',
    promise:
      'short, commercial-intent answers for users who want fast quotes, safe handling, and pickup-friendly mobile recycling',
    regulatoryLine:
      'Phone and tablet searches usually sit at the edge of resale and recycling, so the best pages explain both value recovery and safe battery handling.',
    primaryServiceSlug: 'mobile-recycling-kochi',
    supportServiceSlugs: ['battery-recycling-kochi', 'data-destruction-kochi', 'free-ewaste-pickup-kochi'],
    legacySlugs: ['laptop-resale-value-2026', 'is-formatting-enough-delete-data'],
    shortTailKeywords: [
      'mobile recycling kochi',
      'sell old phone kochi',
      'iphone buyback kochi',
      'tablet recycling',
      'phone disposal near me',
      'damaged mobile recycling',
      'mobile buyback price',
      'corporate phone disposal',
      'phone battery recycling',
      'same day mobile pickup',
    ],
    publicQuestions: [
      'What is the fastest way to sell an old phone safely?',
      'Can I recycle a dead phone with a swollen battery?',
      'Do you wipe data before resale or recycling?',
      'Can companies clear old mobile fleets in one job?',
    ],
    topics: [
      topic('phone-buyback', 'phone buyback', 'Phone Buyback in {location}: Best Route for Fast Local Quotes', 'phone buyback in {location}', 'mobile-recycling-kochi', 'data-destruction-kochi'),
      topic('smartphone-recycling', 'smartphone recycling', 'Smartphone Recycling in {location} Without Data or Battery Risk', 'smartphone recycling in {location}', 'mobile-recycling-kochi', 'battery-recycling-kochi'),
      topic('corporate-mobile-fleet', 'corporate mobile fleet disposal', 'Corporate Mobile Fleet Disposal in {location}', 'corporate mobile disposal in {location}', 'corporate-ewaste-kochi', 'data-destruction-kochi'),
      topic('tablet-ipad-disposal', 'tablet and iPad disposal', 'Tablet and iPad Disposal in {location}: Resale vs Recycling', 'tablet disposal in {location}', 'mobile-recycling-kochi', 'data-destruction-kochi'),
      topic('damaged-phone-recycling', 'damaged phone recycling', 'Damaged Phone Recycling in {location}: What Still Counts as Value?', 'damaged phone recycling in {location}', 'mobile-recycling-kochi', 'battery-recycling-kochi'),
      topic('secure-mobile-data-wipe', 'secure mobile data wipe', 'Secure Mobile Data Wipe in {location} Before Buyback or Recycling', 'secure mobile data wipe in {location}', 'data-destruction-kochi', 'mobile-recycling-kochi'),
      topic('accessory-recycling', 'charger and accessory recycling', 'Charger and Accessory Recycling in {location}: Small Electronics Done Right', 'charger recycling in {location}', 'e-waste-recycling-kochi', 'mobile-recycling-kochi'),
      topic('residential-phone-dropoff', 'residential phone drop-off', 'Residential Phone Drop-Off in {location}: What to Bring and What to Avoid', 'phone drop off in {location}', 'mobile-recycling-kochi', 'battery-recycling-kochi'),
      topic('classifieds-vs-buyback', 'classifieds vs buyback', 'Buyback vs Classifieds for Old Phones in {location}', 'sell old phone in {location}', 'mobile-recycling-kochi', 'data-destruction-kochi'),
      topic('same-day-phone-pickup', 'same-day phone pickup', 'Same-Day Mobile Pickup in {location} for Shops and Offices', 'same day mobile pickup in {location}', 'free-ewaste-pickup-kochi', 'mobile-recycling-kochi'),
    ],
  },
  {
    slug: 'corporate-itad',
    name: 'Corporate ITAD',
    emoji: 'B2B',
    pageContext: 'corporate',
    summary: 'Transaction-ready pages for ITAD contracts, device refreshes, chain of custody, and industry-specific compliance.',
    promise:
      'enterprise-focused content that turns ITAD, chain of custody, and asset recovery into easy next steps for decision-makers',
    regulatoryLine:
      'Corporate searches need stronger proof than consumer pages, so these articles lean into audit trails, pickup logistics, and documentation quality.',
    primaryServiceSlug: 'itad-kochi',
    supportServiceSlugs: ['data-destruction-kochi', 'corporate-ewaste-kochi', 'it-asset-inventory-audit'],
    legacySlugs: ['how-to-choose-itad-provider', 'itad-roi-kochi-enterprise'],
    shortTailKeywords: [
      'itad kochi',
      'it asset disposal kerala',
      'corporate e waste management',
      'data centre decommissioning',
      'it asset recovery',
      'audit trail itad',
      'asset inventory audit',
      'bank it disposal',
      'school it disposal',
      'annual itad contract',
    ],
    publicQuestions: [
      'Which documents matter most during an audit?',
      'How do I dispose of 200 employee laptops with one vendor?',
      'Can ITAD recover value instead of becoming a pure cost?',
      'What should be included in a chain-of-custody workflow?',
    ],
    topics: [
      topic('it-companies', 'ITAD for IT companies', 'IT Asset Disposal for IT Companies in {location}', 'it asset disposal for companies in {location}', 'itad-kochi', 'data-destruction-kochi'),
      topic('annual-contracts', 'annual ITAD contracts', 'Annual ITAD Contracts in {location}: What Procurement Teams Should Lock In', 'annual ITAD contract in {location}', 'itad-kochi', 'corporate-ewaste-kochi'),
      topic('inventory-audit', 'asset inventory and audit', 'Asset Inventory Audit in {location} Before ITAD Projects Begin', 'asset inventory audit in {location}', 'it-asset-inventory-audit', 'itad-kochi'),
      topic('data-centre-refresh', 'data centre refresh', 'Data Centre Refresh and Retirement Planning in {location}', 'data centre retirement in {location}', 'server-recycling-kochi', 'itad-kochi'),
      topic('employee-refresh', 'employee device refresh', 'Employee Device Refresh Workflow in {location}: Pickup, Wipe, Recover', 'employee device refresh in {location}', 'itad-kochi', 'laptop-buyback-kochi'),
      topic('banks-hospitals', 'bank and hospital ITAD', 'Bank and Hospital ITAD in {location}: Documentation That Actually Matters', 'hospital IT disposal in {location}', 'itad-kochi', 'data-destruction-kochi'),
      topic('schools-colleges', 'school and college IT disposal', 'School and College IT Disposal in {location}', 'education IT disposal in {location}', 'corporate-ewaste-kochi', 'it-asset-inventory-audit'),
      topic('startup-closures', 'startup office clear-outs', 'Startup Office Clear-Outs in {location}: Fast ITAD for Lean Teams', 'startup IT disposal in {location}', 'itad-kochi', 'laptop-buyback-kochi'),
      topic('chain-of-custody', 'chain of custody', 'Chain of Custody for ITAD in {location}: What Good Vendors Prove', 'chain of custody ITAD in {location}', 'itad-kochi', 'certificate-of-destruction-kochi'),
      topic('asset-recovery', 'asset recovery and remarketing', 'Asset Recovery and Remarketing in {location}: How ITAD Recovers Budget', 'asset recovery ITAD in {location}', 'laptop-buyback-kochi', 'itad-kochi'),
    ],
  },
  {
    slug: 'data-destruction',
    name: 'Data Destruction',
    emoji: 'Secure',
    pageContext: 'itad',
    summary: 'Pages designed for hard drive shredding, certified wiping, certificates, and DPDP-ready data retirement.',
    promise:
      'technical yet commercial content for teams that need NIST language, proof of destruction, and fast handoff to a trusted provider',
    regulatoryLine:
      'Data-destruction searchers are usually trying to reduce breach risk, so every page stresses verification, certificates, and chain of custody.',
    primaryServiceSlug: 'data-destruction-kochi',
    supportServiceSlugs: ['hard-drive-shredding-kochi', 'certificate-of-destruction-kochi', 'hard-drive-destruction-kochi'],
    legacySlugs: ['is-formatting-enough-delete-data', 'dpdp-act-2023-it-disposal-compliance'],
    shortTailKeywords: [
      'data destruction kochi',
      'hard drive shredding',
      'secure data wiping',
      'certificate of destruction',
      'nist 800-88 kochi',
      'ssd destruction',
      'hard drive degaussing',
      'on-site data destruction',
      'data secure it recycling',
      'secure laptop disposal',
    ],
    publicQuestions: [
      'Is formatting enough before device resale?',
      'When should I choose shredding over wiping?',
      'Can you issue a device-level certificate of destruction?',
      'How do I prove DPDP-ready disposal to auditors?',
    ],
    topics: [
      topic('hard-drive-shredding', 'hard drive shredding', 'Hard Drive Shredding in {location}: When Physical Destruction Is Best', 'hard drive shredding in {location}', 'hard-drive-shredding-kochi', 'certificate-of-destruction-kochi'),
      topic('nist-wiping', 'NIST 800-88 wiping', 'NIST 800-88 Wiping in {location}: What It Covers and What It Does Not', 'nist 800-88 wiping in {location}', 'data-destruction-kochi', 'certificate-of-destruction-kochi'),
      topic('ssd-destruction', 'SSD destruction', 'SSD Destruction in {location}: Why It Differs from HDD Disposal', 'ssd destruction in {location}', 'hard-drive-shredding-kochi', 'data-destruction-kochi'),
      topic('onsite-destruction', 'on-site data destruction', 'On-Site Data Destruction in {location}: Who Needs Witnessed Service?', 'on site data destruction in {location}', 'hard-drive-shredding-kochi', 'data-destruction-kochi'),
      topic('certificate-of-destruction', 'certificate of destruction', 'Certificate of Destruction in {location}: What Auditors Expect to See', 'certificate of destruction in {location}', 'certificate-of-destruction-kochi', 'data-destruction-kochi'),
      topic('laptop-data-wipe', 'laptop data wipe', 'Laptop Data Wipe in {location} Before Buyback or Recycling', 'laptop data wipe in {location}', 'data-destruction-kochi', 'laptop-buyback-kochi'),
      topic('server-drive-sanitization', 'server drive sanitization', 'Server Drive Sanitization in {location} for ITAD Projects', 'server drive sanitization in {location}', 'data-destruction-kochi', 'server-recycling-kochi'),
      topic('dpdp-proof', 'DPDP destruction proof', 'DPDP-Ready Data Destruction Evidence in {location}', 'dpdp compliant data destruction in {location}', 'dpdp-act-compliance-kochi', 'certificate-of-destruction-kochi'),
      topic('degaussing-vs-shredding', 'degaussing vs shredding', 'Degaussing vs Shredding in {location}: Which Method Fits Better?', 'degaussing vs shredding in {location}', 'hard-drive-degaussing-kochi', 'hard-drive-shredding-kochi'),
      topic('formatting-myths', 'formatting myths', 'Why Formatting Is Not Enough Before Disposal in {location}', 'is formatting enough before disposal in {location}', 'data-destruction-kochi', 'certificate-of-destruction-kochi'),
    ],
  },
  {
    slug: 'scrap-electronics',
    name: 'Scrap Electronics',
    emoji: 'Pricing',
    pageContext: 'scrap',
    summary: 'Commercial pages for electronics value recovery, scrap comparisons, and bulk device sale intent.',
    promise:
      'clear price-framing and buyback logic for users comparing certified buyers with unstructured local scrap channels',
    regulatoryLine:
      'Scrap-focused searchers still need compliance, especially when loads contain data-bearing devices, batteries, or mixed office equipment.',
    primaryServiceSlug: 'laptop-buyback-kochi',
    supportServiceSlugs: ['corporate-ewaste-kochi', 'network-equipment-disposal-kochi', 'server-recycling-kochi'],
    legacySlugs: ['laptop-resale-value-2026', 'itad-roi-kochi-enterprise'],
    shortTailKeywords: [
      'electronics scrap buyers',
      'computer scrap buyers',
      'scrap laptop price',
      'office e waste buyers',
      'server scrap buyers',
      'network equipment scrap',
      'motherboard scrap buyers',
      'bulk electronics sale',
      'sell electronic waste',
      'e waste buyers near me',
    ],
    publicQuestions: [
      'How is price decided for mixed electronics loads?',
      'Can certified buyers pay more than scrap shops?',
      'Do broken devices still have recoverable value?',
      'Should I separate working and non-working assets first?',
    ],
    topics: [
      topic('computer-scrap-buyers', 'computer scrap buyers', 'Computer Scrap Buyers in {location}: What Changes the Quote?', 'computer scrap buyers in {location}', 'laptop-buyback-kochi', 'corporate-ewaste-kochi'),
      topic('scrap-laptop-prices', 'scrap laptop prices', 'Scrap Laptop Prices in {location}: Value Signals Most Sellers Miss', 'scrap laptop prices in {location}', 'laptop-buyback-kochi', 'data-destruction-kochi'),
      topic('server-scrap', 'server scrap buyers', 'Server Scrap Buyers in {location}: Recovering More from Old Racks', 'server scrap buyers in {location}', 'server-recycling-kochi', 'itad-kochi'),
      topic('network-scrap', 'network equipment scrap', 'Network Equipment Scrap in {location}: Switches, Routers, Firewalls', 'network equipment scrap in {location}', 'network-equipment-disposal-kochi', 'server-recycling-kochi'),
      topic('pcb-scrap', 'PCB and motherboard scrap', 'PCB and Motherboard Scrap Buyers in {location}', 'motherboard scrap buyers in {location}', 'e-waste-recycling-kochi', 'laptop-buyback-kochi'),
      topic('office-clearance-scrap', 'office clearance scrap', 'Office Clearance Scrap Quotes in {location}: How to Prepare the Inventory', 'office clearance scrap in {location}', 'corporate-ewaste-kochi', 'laptop-buyback-kochi'),
      topic('working-vs-broken', 'working vs broken devices', 'Working vs Broken Device Value in {location}: What Gets a Better Quote?', 'working vs broken electronics in {location}', 'laptop-buyback-kochi', 'mobile-recycling-kochi'),
      topic('price-factors', 'electronics price factors', 'Electronics Price Factors in {location}: Why Two Loads Get Different Rates', 'electronics scrap price in {location}', 'laptop-buyback-kochi', 'corporate-ewaste-kochi'),
      topic('bulk-electronics-sale', 'bulk electronics sale', 'Bulk Electronics Sale in {location}: Certified Buyer vs Informal Dealer', 'bulk electronics sale in {location}', 'corporate-ewaste-kochi', 'laptop-buyback-kochi'),
      topic('scrap-vs-certified', 'scrap dealer vs certified buyer', 'Scrap Dealer vs Certified Buyer in {location}: Which Route Wins?', 'scrap dealer vs certified buyer in {location}', 'e-waste-recycling-kochi', 'laptop-buyback-kochi'),
    ],
  },
  {
    slug: 'battery-recycling',
    name: 'Battery Recycling',
    emoji: 'Hazmat',
    pageContext: 'battery',
    summary: 'Safety-first local pages for lithium-ion, lead-acid, UPS, EV, and solar battery disposal.',
    promise:
      'battery-specific pages that reduce confusion around hazardous handling, pickup rules, and the right recycling stream',
    regulatoryLine:
      'Battery content needs stronger safety framing because storage, packaging, and pickup conditions matter before the recycler even sees the load.',
    primaryServiceSlug: 'battery-recycling-kochi',
    supportServiceSlugs: ['free-ewaste-pickup-kochi', 'e-waste-recycling-kochi', 'corporate-ewaste-kochi'],
    legacySlugs: ['ewaste-laws-kerala-2026', 'how-to-choose-itad-provider'],
    shortTailKeywords: [
      'battery recycling kochi',
      'lithium battery disposal',
      'ups battery disposal',
      'laptop battery recycling',
      'phone battery recycling',
      'lead acid battery buyers',
      'solar battery disposal',
      'ev battery recycling',
      'battery pickup service',
      'battery waste rules',
    ],
    publicQuestions: [
      'Can swollen lithium batteries be picked up safely?',
      'Do UPS batteries need a different process from laptop batteries?',
      'What should a company do with mixed battery loads?',
      'How should batteries be stored before pickup arrives?',
    ],
    topics: [
      topic('laptop-batteries', 'laptop battery recycling', 'Laptop Battery Recycling in {location}: Storage, Pickup, and Safety', 'laptop battery recycling in {location}', 'battery-recycling-kochi', 'free-ewaste-pickup-kochi'),
      topic('phone-batteries', 'phone battery recycling', 'Phone Battery Recycling in {location}: What to Do with Loose Cells', 'phone battery recycling in {location}', 'battery-recycling-kochi', 'mobile-recycling-kochi'),
      topic('ups-batteries', 'UPS and inverter batteries', 'UPS and Inverter Battery Disposal in {location}', 'ups battery disposal in {location}', 'battery-recycling-kochi', 'corporate-ewaste-kochi'),
      topic('lithium-safety', 'lithium battery safety', 'Lithium Battery Disposal in {location}: How to Avoid Fire Risk', 'lithium battery disposal in {location}', 'battery-recycling-kochi', 'free-ewaste-pickup-kochi'),
      topic('lead-acid', 'lead-acid battery recycling', 'Lead-Acid Battery Recycling in {location}: What Businesses Need to Track', 'lead acid battery recycling in {location}', 'battery-recycling-kochi', 'corporate-ewaste-kochi'),
      topic('ev-batteries', 'EV battery recycling', 'EV Battery Recycling in {location}: When to Use a Specialist Pickup', 'ev battery recycling in {location}', 'battery-recycling-kochi', 'free-ewaste-pickup-kochi'),
      topic('solar-batteries', 'solar battery disposal', 'Solar Battery Disposal in {location}: Practical Steps for Safe Collection', 'solar battery disposal in {location}', 'battery-recycling-kochi', 'free-ewaste-pickup-kochi'),
      topic('office-battery-pickup', 'office battery pickup', 'Office Battery Pickup in {location}: How to Stage Mixed Loads', 'office battery pickup in {location}', 'free-ewaste-pickup-kochi', 'battery-recycling-kochi'),
      topic('battery-storage', 'battery storage before pickup', 'How to Store Batteries Before Pickup in {location}', 'battery storage before pickup in {location}', 'battery-recycling-kochi', 'free-ewaste-pickup-kochi'),
      topic('battery-rules', 'battery rules and compliance', 'Battery Waste Rules in {location}: What Bulk Users Should Know', 'battery waste rules in {location}', 'battery-recycling-kochi', 'corporate-ewaste-kochi'),
    ],
  },
  {
    slug: 'government-rules',
    name: 'Government Rules',
    emoji: 'Audit',
    pageContext: 'compliance',
    summary: 'Compliance-led pages for KSPCB rules, DPDP risk, manifests, and certificate-driven disposal decisions.',
    promise:
      'audit-ready explanations that translate laws, certificates, and vendor checks into practical disposal workflows',
    regulatoryLine:
      'These pages focus on due diligence, because legal searchers need proof, process, and document language that can survive procurement or audit review.',
    primaryServiceSlug: 'dpdp-act-compliance-kochi',
    supportServiceSlugs: ['itad-kochi', 'certificate-of-destruction-kochi', 'data-destruction-kochi'],
    legacySlugs: ['ewaste-laws-kerala-2026', 'dpdp-act-impact-startups'],
    shortTailKeywords: [
      'e waste laws kerala',
      'dpdp act e waste',
      'kspcb authorized recycler',
      'certificate of destruction audit',
      'bulk consumer e waste rules',
      'e waste compliance kochi',
      'data protection act india disposal',
      'form 6 e waste',
      'authorized e waste buyers',
      'dpdp act startup compliance',
    ],
    publicQuestions: [
      'What documents should a recycler provide after pickup?',
      'Do small companies also need DPDP-ready disposal records?',
      'How do I check whether a recycler is actually authorized?',
      'What is the safest way to answer an audit question on retired devices?',
    ],
    topics: [
      topic('ewaste-rules', 'E-Waste Rules 2022', 'E-Waste Rules 2022 for Businesses in {location}', 'e-waste rules in {location}', 'dpdp-act-compliance-kochi', 'itad-kochi'),
      topic('dpdp-retired-devices', 'DPDP and retired devices', 'DPDP Act and Retired Devices in {location}: What Changes for Disposal?', 'dpdp act disposal in {location}', 'dpdp-act-compliance-kochi', 'data-destruction-kochi'),
      topic('kspcb-check', 'KSPCB authorization check', 'How to Verify a KSPCB-Authorized Recycler in {location}', 'kspcb authorized recycler in {location}', 'dpdp-act-compliance-kochi', 'certificate-of-destruction-kochi'),
      topic('forms-manifests', 'forms and manifests', 'Forms and Manifests for E-Waste Pickup in {location}', 'e-waste manifest in {location}', 'corporate-ewaste-kochi', 'certificate-of-destruction-kochi'),
      topic('certificate-audits', 'certificate of destruction audits', 'Certificate of Destruction for Audits in {location}', 'certificate of destruction audit in {location}', 'certificate-of-destruction-kochi', 'data-destruction-kochi'),
      topic('bulk-consumer', 'bulk consumer obligations', 'Bulk Consumer E-Waste Obligations in {location}', 'bulk consumer e-waste in {location}', 'dpdp-act-compliance-kochi', 'itad-kochi'),
      topic('schools-hospitals', 'school and hospital compliance', 'School and Hospital E-Waste Compliance in {location}', 'school e-waste compliance in {location}', 'dpdp-act-compliance-kochi', 'corporate-ewaste-kochi'),
      topic('startup-sme', 'startup and SME compliance', 'Startup and SME E-Waste Compliance in {location}', 'startup e-waste compliance in {location}', 'dpdp-act-compliance-kochi', 'data-destruction-kochi'),
      topic('breach-risk', 'data breach disposal risk', 'How Disposal Mistakes Create Data Breach Risk in {location}', 'data breach disposal risk in {location}', 'data-destruction-kochi', 'dpdp-act-compliance-kochi'),
      topic('choose-authorized-vendor', 'choose an authorized vendor', 'How to Choose an Authorized E-Waste Vendor in {location}', 'choose authorized e-waste vendor in {location}', 'dpdp-act-compliance-kochi', 'itad-kochi'),
    ],
  },
  {
    slug: 'environmental-impact',
    name: 'Environmental Impact',
    emoji: 'ESG',
    pageContext: 'recycling',
    summary: 'Awareness and authority pages about circular economy, zero-landfill programs, hazardous components, and ESG value.',
    promise:
      'strong informational content that explains why recycling choices matter while still funneling visitors toward real collection and recycling services',
    regulatoryLine:
      'Environmental queries are upper-funnel, so the content connects public education with concrete services such as drives, pickups, and documented recycling.',
    primaryServiceSlug: 'e-waste-recycling-kochi',
    supportServiceSlugs: ['free-ewaste-pickup-kochi', 'battery-recycling-kochi', 'corporate-ewaste-kochi'],
    legacySlugs: ['ewaste-laws-kerala-2026', 'dpdp-act-impact-startups'],
    shortTailKeywords: [
      'impact of e waste',
      'why recycle electronics',
      'toxic components in electronics',
      'circular economy e waste',
      'zero landfill electronics',
      'carbon footprint recycling',
      'school e waste drive',
      'community e waste collection',
      'hazardous electronic waste',
      'environment friendly disposal',
    ],
    publicQuestions: [
      'Why is e-waste worse than normal dry waste?',
      'What valuable materials are recovered from old electronics?',
      'Can schools and apartments run structured collection drives?',
      'What does zero-landfill recycling really mean in practice?',
    ],
    topics: [
      topic('why-recycle', 'why recycle electronics', 'Why Recycle Electronics in {location}: The Local Impact', 'why recycle electronics in {location}', 'e-waste-recycling-kochi', 'free-ewaste-pickup-kochi'),
      topic('toxic-components', 'toxic components in electronics', 'Toxic Components in Electronics Collected in {location}', 'toxic electronic waste in {location}', 'e-waste-recycling-kochi', 'battery-recycling-kochi'),
      topic('landfill-risk', 'landfill risk', 'What Happens When Electronics Reach Landfills in {location}', 'electronics landfill risk in {location}', 'e-waste-recycling-kochi', 'free-ewaste-pickup-kochi'),
      topic('circular-economy', 'circular economy', 'Circular Economy and E-Waste in {location}: What Recovery Actually Looks Like', 'circular economy e-waste in {location}', 'e-waste-recycling-kochi', 'corporate-ewaste-kochi'),
      topic('precious-metals', 'precious metal recovery', 'Precious Metal Recovery from E-Waste in {location}', 'precious metal recovery from e-waste in {location}', 'e-waste-recycling-kochi', 'laptop-buyback-kochi'),
      topic('carbon-footprint', 'carbon footprint reduction', 'How E-Waste Recycling Reduces Carbon Footprint in {location}', 'carbon footprint e-waste in {location}', 'corporate-ewaste-kochi', 'e-waste-recycling-kochi'),
      topic('zero-landfill', 'zero-landfill policy', 'Zero-Landfill Electronics Programs in {location}', 'zero landfill electronics in {location}', 'e-waste-recycling-kochi', 'corporate-ewaste-kochi'),
      topic('school-drives', 'school awareness drives', 'School E-Waste Drives in {location}: Planning a Safer Collection Day', 'school e-waste drive in {location}', 'free-ewaste-pickup-kochi', 'e-waste-recycling-kochi'),
      topic('apartment-drives', 'apartment and community drives', 'Apartment and Community E-Waste Drives in {location}', 'community e-waste drive in {location}', 'free-ewaste-pickup-kochi', 'e-waste-recycling-kochi'),
      topic('sustainable-office-cleanouts', 'sustainable office clean-outs', 'Sustainable Office Clean-Outs in {location}: ESG-Friendly Disposal Moves', 'sustainable office disposal in {location}', 'corporate-ewaste-kochi', 'e-waste-recycling-kochi'),
    ],
  },
];

const truncate = (text, length) => (text.length > length ? `${text.slice(0, length - 3).trim()}...` : text);

const slugify = (value) =>
  value
    .toLowerCase()
    .replace(/&/g, ' and ')
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '');

const resolveService = (slug, fallbackSlug) => serviceMap.get(slug) || serviceMap.get(fallbackSlug) || services[0];

const resolveLegacyPosts = (slugs = []) => slugs.map((slug) => legacyBlogMap.get(slug)).filter(Boolean);

const buildCategoryLink = (categorySlug) => ({
  label: 'Category hub',
  href: `${blogLibraryConfig.basePath}/${categorySlug}/`,
});

const buildLocationLinks = (geo) =>
  [geo.location, ...(geo.location?.nearbyAreas || []).map((slug) => locationMap.get(slug))]
    .filter(Boolean)
    .slice(0, 3)
    .map((location) => ({
      label: location.displayName || location.name,
      href: `/locations/${location.slug}/`,
    }));

const buildServiceLinks = (primaryService, secondaryService, category) =>
  [primaryService, secondaryService, ...category.supportServiceSlugs.map((slug) => serviceMap.get(slug))]
    .filter(Boolean)
    .reduce((unique, service) => {
      if (unique.some((entry) => entry.href === `/services/${service.slug}/`)) return unique;
      unique.push({ label: service.shortName || service.name, href: `/services/${service.slug}/` });
      return unique;
    }, [])
    .slice(0, 4);

const buildLegacyLinks = (category) =>
  resolveLegacyPosts(category.legacySlugs).map((blog) => ({
    label: blog.title,
    href: `/blog/${blog.slug}/`,
  }));

const buildFaqs = (category, topicItem, geo, primaryService) => [
  {
    q: `Who handles ${topicItem.label} in ${geo.titleLabel}?`,
    a: `EWaste Kochi handles ${topicItem.label} in ${geo.titleLabel} using ${primaryService.shortName}. Pickup can be scheduled through WhatsApp, and data-bearing assets can be routed for secure destruction before recycling or resale.`,
  },
  {
    q: `Is pickup free for ${topicItem.label} in ${geo.titleLabel}?`,
    a: `Pickup is typically free for business and bulk loads. Smaller residential jobs can usually be combined with a drop-off or a paid doorstep slot, depending on location, quantity, and whether the devices still hold resale value.`,
  },
  {
    q: `Do you issue documents for ${topicItem.label} jobs in ${geo.titleLabel}?`,
    a: `Yes. EWaste Kochi can provide collection records, recycler routing details, and Certificate of Destruction support whenever the job includes data-bearing devices or an audit-sensitive disposal workflow.`,
  },
  {
    q: `What should I do before handing over ${topicItem.label} in ${geo.titleLabel}?`,
    a: `Set aside chargers, note any damaged batteries, and separate equipment that still contains storage media. If the load belongs to a business, prepare a simple asset list so pickup and documentation move faster.`,
  },
  {
    q: `Why use a certified recycler instead of an informal scrap buyer in ${geo.titleLabel}?`,
    a: `${category.regulatoryLine} A certified route also gives you a clearer decision between resale, secure destruction, and responsible recycling instead of treating every device as low-value scrap.`,
  },
];

const buildSections = (category, topicItem, geo, primaryService, secondaryService) => [
  {
    heading: `What this search usually means in ${geo.titleLabel}`,
    paragraphs: [
      `People searching for "${topicItem.keyword.replace('{location}', geo.searchLabel)}" usually need a fast local answer, not a generic explainer. They want to know who can collect the devices, whether pickup is free, and whether anything in the load still has resale or audit value.`,
      `${category.promise.charAt(0).toUpperCase()}${category.promise.slice(1)}. In ${geo.titleLabel}, that often means combining pickup logistics with a clearer decision between buyback, secure destruction, and authorized recycling.`,
    ],
    points: [
      `Local route built for ${geo.titleLabel} and nearby service areas`,
      `Primary service match: ${primaryService.shortName}`,
      `Support path available for data, batteries, and mixed-office loads`,
    ],
  },
  {
    heading: `Best-fit service route for ${topicItem.label}`,
    paragraphs: [
      `${primaryService.shortName} is usually the cleanest first step for ${topicItem.label}. ${primaryService.description || primaryService.metaDescription || `${primaryService.shortName} is one of EWaste Kochi's core services.`}`,
      `If the job also involves batteries, storage media, or mixed office equipment, pair it with ${secondaryService.shortName}. That keeps the workflow simpler and avoids handing the same load to multiple vendors.`,
    ],
    points: primaryService.badges?.slice(0, 3) || ['KSPCB-authorized workflow', 'Pickup-friendly process', 'WhatsApp-first booking'],
  },
  {
    heading: 'Pickup, documentation, and compliance',
    paragraphs: [
      `A strong workflow is usually inventory -> pickup or drop-off -> triage -> data handling -> value recovery or recycling -> documentation. That is the part many "near me" searchers do not see, but it is exactly where certified vendors separate themselves from informal buyers.`,
      `${category.regulatoryLine} For teams in ${geo.titleLabel}, the best next move is usually to confirm quantity, timeline, and whether the load includes any client data or hazardous components before collection is booked.`,
    ],
    points: [
      'Bulk and recurring loads can be scheduled through one collection contact',
      'Certificate-driven handling is available when the job includes storage devices',
      'Mixed loads can be split into resale, destruction, and recycling streams',
    ],
  },
  {
    heading: `Common mistakes to avoid in ${geo.titleLabel}`,
    paragraphs: [
      `The biggest mistake is treating ${topicItem.label} like low-value scrap before checking whether the devices hold audit risk, resale value, or separate battery requirements. That usually leads to weaker pricing, weaker documentation, or both.`,
      `A better move is to start with ${primaryService.shortName}, confirm the device mix, and then use the supporting services only where they actually improve value, compliance, or turnaround time.`,
    ],
    points: [
      'Do not rely on a simple factory reset when data is involved',
      'Do not mix swollen batteries into general electronics boxes',
      'Do not lose value by selling business-grade devices as undifferentiated scrap',
    ],
  },
];

const buildPost = (category, topicItem, geo, position) => {
  const title = topicItem.title.replace('{location}', geo.titleLabel);
  const slug = slugify(title);
  const keyword = topicItem.keyword.replace('{location}', geo.searchLabel);
  const primaryService = resolveService(topicItem.primaryServiceSlug, category.primaryServiceSlug);
  const secondaryService = resolveService(topicItem.secondaryServiceSlug, category.supportServiceSlugs[0]);
  const serviceLinks = buildServiceLinks(primaryService, secondaryService, category);
  const locationLinks = buildLocationLinks(geo);
  const legacyLinks = buildLegacyLinks(category);
  const canonical = `${blogLibraryConfig.host}${blogLibraryConfig.basePath}/${category.slug}/${slug}/`;
  const sections = buildSections(category, topicItem, geo, primaryService, secondaryService);
  const faqs = buildFaqs(category, topicItem, geo, primaryService);
  const summary = truncate(
    `${title}. ${primaryService.shortName} in ${geo.titleLabel} with pickup guidance, resale vs recycling advice, and KSPCB-authorized handling from EWaste Kochi.`,
    158,
  );

  return {
    id: `${category.slug}-${topicItem.slug}-${geo.slug}`,
    position,
    slug,
    title,
    excerpt: summary,
    summary,
    keyword,
    categorySlug: category.slug,
    categoryName: category.name,
    categoryEmoji: category.emoji,
    categorySummary: category.summary,
    clusterSlug: topicItem.slug,
    clusterLabel: topicItem.label,
    pageContext: category.pageContext,
    canonical,
    metaTitle: truncate(`${title} | EWaste Kochi`, 62),
    metaDescription: summary,
    keywords: [keyword, ...category.shortTailKeywords.slice(0, 4)],
    location: {
      slug: geo.slug,
      name: geo.location?.name || geo.titleLabel,
      titleLabel: geo.titleLabel,
      displayName: geo.location?.displayName || geo.titleLabel,
    },
    primaryService,
    secondaryService,
    serviceLinks,
    locationLinks,
    legacyLinks,
    sections,
    faqs,
    cta: {
      title: `Need ${topicItem.label} help in ${geo.titleLabel}?`,
      description: `Use ${primaryService.shortName} as the starting point, then layer in secure destruction, buyback, or recycling only where the load actually needs it.`,
      primaryHref: serviceLinks[0]?.href || '/contact/',
      primaryLabel: `Explore ${primaryService.shortName}`,
      secondaryHref: '/contact/',
      secondaryLabel: 'Book a pickup or quote',
    },
    contextualLinks: [
      ...serviceLinks,
      ...locationLinks,
      buildCategoryLink(category.slug),
      { label: 'SEO library home', href: `${blogLibraryConfig.basePath}/` },
      ...legacyLinks.slice(0, 2),
    ].slice(0, 8),
  };
};

export const blogLibraryCategories = categoryDefinitions.map((category) => ({
  ...category,
  articleCount: category.topics.length * geoTargets.length,
  geoTargets: geoTargets.map((geo) => ({
    slug: geo.slug,
    titleLabel: geo.titleLabel,
    href: `/locations/${geo.slug}/`,
  })),
  serviceLinks: category.supportServiceSlugs
    .map((slug) => serviceMap.get(slug))
    .filter(Boolean)
    .map((service) => ({
      label: service.shortName || service.name,
      href: `/services/${service.slug}/`,
    })),
}));

export const blogLibraryPosts = blogLibraryCategories.flatMap((category) =>
  geoTargets.flatMap((geo, geoIndex) =>
    category.topics.map((topicItem, topicIndex) =>
      buildPost(category, topicItem, geo, geoIndex * category.topics.length + topicIndex + 1),
    ),
  ),
);

export const blogLibraryStats = {
  categories: blogLibraryCategories.length,
  geoTargets: geoTargets.length,
  posts: blogLibraryPosts.length,
  shortTailKeywords: blogLibraryCategories.reduce((sum, category) => sum + category.shortTailKeywords.length, 0),
  longTailKeywords: blogLibraryPosts.length,
};

export const getBlogLibraryCategory = (categorySlug) =>
  blogLibraryCategories.find((category) => category.slug === categorySlug);

export const getBlogLibraryPostsByCategory = (categorySlug) =>
  blogLibraryPosts.filter((post) => post.categorySlug === categorySlug);

export const getBlogLibraryPost = (categorySlug, slug) =>
  blogLibraryPosts.find((post) => post.categorySlug === categorySlug && post.slug === slug);

export const getBlogLibraryCategoryClusters = (categorySlug) => {
  const category = getBlogLibraryCategory(categorySlug);
  if (!category) return [];

  return category.topics.map((topicItem) => ({
    ...topicItem,
    posts: getBlogLibraryPostsByCategory(categorySlug).filter((post) => post.clusterSlug === topicItem.slug),
  }));
};

export const getFeaturedLibraryPosts = () =>
  blogLibraryCategories
    .map((category) => getBlogLibraryPostsByCategory(category.slug)[0])
    .filter(Boolean);
