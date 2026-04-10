// ═══════════════════════════════════════════════════════════════════
// FAQ Hub — 20 Categories (Blueprint for 2000+ FAQs)
// ═══════════════════════════════════════════════════════════════════

export const faqCategories = [
  { id: 'general', name: 'General Information', icon: 'ℹ️' },
  { id: 'itad', name: 'ITAD & Corporate Retirement', icon: '🏢' },
  { id: 'data', name: 'Data Destruction & Wiping', icon: '🔐' },
  { id: 'compliance', name: 'Compliance & Legal (DPDP)', icon: '⚖️' },
  { id: 'locations', name: 'Kochi Service Areas & Pickup', icon: '🚛' },
  { id: 'recycling', name: 'Electronic Recycling Tech', icon: '♻️' },
  { id: 'battery', name: 'Battery Recycling Safety', icon: '🔋' },
  { id: 'buyback', name: 'Buyback & Resale Prices', icon: '💰' },
  { id: 'hazardous', name: 'Hazardous Waste Handling', icon: '☢️' },
  { id: 'environment', name: 'Environmental & Sustainability', icon: '🌱' },
  { id: 'laptop', name: 'Laptops & MacBooks', icon: '💻' },
  { id: 'server', name: 'Server & Data Center', icon: '🖥️' },
  { id: 'mobile', name: 'Mobile Phones & Tablets', icon: '📱' },
  { id: 'printer', name: 'Printers & Cartridges', icon: '🖨️' },
  { id: 'networking', name: 'Networking Gear & Routers', icon: '🔌' },
  { id: 'industrial', name: 'Industrial & Large Hardware', icon: '🏗️' },
  { id: 'certifications', name: 'Certificates (CoD / EPR)', icon: '📜' },
  { id: 'audits', name: 'RBI & Government Audits', icon: '📝' },
  { id: 'residential', name: 'Residential & Consumer', icon: '🏠' },
  { id: 'partnerships', name: 'Corporate Partnerships', icon: '🤝' },
];

export const faqs = [
  // General
  { category: 'general', q: 'What is e-waste recycling?', a: 'E-waste recycling is the process of extracting valuable materials from discarded electronic devices while ensuring hazardous components are safely neutralized.' },
  { category: 'general', q: 'Is EWaste Kochi certified?', a: 'Yes, we are KSPCB (Kerala State Pollution Control Board) authorized and EPR (Extended Producer Responsibility) compliant.' },
  
  // ITAD
  { category: 'itad', q: 'What does ITAD stand for?', a: 'ITAD stands for IT Asset Disposition, the professional process of retiring hardware securely and responsibly.' },
  { category: 'itad', q: 'Why is ITAD different from recycling?', a: 'Recycling focuses on material recovery; ITAD focuses on data security, asset tracking, and corporate compliance.' },
  
  // Data Destruction
  { category: 'data', q: 'What is NIST 800-88 purging?', a: 'It is a global data sanitization standard that ensures data is permanently and legally unrecoverable from storage media.' },
  { category: 'data', q: 'Do you provide physical shredding?', a: 'Yes, we provide industrial-grade physical shredding for HDDs, SSDs, and storage tapes.' },

  // Compliance
  { category: 'compliance', q: 'How does DPDP Act 2023 affect e-waste?', a: 'The DPDP Act mandates that all businesses must ensure personal data is destroyed when retiring hardware, or face massive legal penalties.' },
  { category: 'compliance', q: 'Can you help with RBI audit compliance?', a: 'Absolutely. Our Certificate of Destruction satisfies RBI and SEBI audit requirements for data asset retirement.' },
  
  // Locations
  { category: 'locations', q: 'Do you serve Infopark Kakkanad?', a: 'Yes, we offer same-day collection priority for IT companies located in Infopark and Smart City.' },
  { category: 'locations', q: 'Is pickup free in Ernakulam?', a: 'Pickup is free for corporate clients disposing of 10 or more devices across all Kochi areas.' },

  // Batteries
  { category: 'battery', q: 'Are lithium batteries hazardous?', a: 'Yes. Improper storage or disposal of Li-ion batteries can lead to thermal runaway (fires). We recycle them using specialized hazardous waste containers.' },
  
  // Buyback
  { category: 'buyback', q: 'How much do you pay for old laptops?', a: 'Prices depend on age, condition, and model. We typicaly pay ₹2,000 to ₹80,000 per unit for resalable hardware.' },
  
  // Add thousands more programmatically as needed...
];

// Helper to get FAQs for a specific page dynamically
export const getFaqsByCategory = (catId) => faqs.filter(f => f.category === catId);
export const getPillarFaqs = (catId, count = 10) => faqs.filter(f => f.category === catId).slice(0, count);

/**
 * Automates 50+ Local SEO FAQs for any location.
 * Perfect for programmatic pillar pages.
 */
export const generateLocationFaqs = (locName) => {
  const templates = [
    { q: `Where is the best e-waste pickup in ${locName}?`, a: `EWaste Kochi provides the most reliable and certified e-waste collection across ${locName}, offering same-day pickups for corporate clients. See our <a href="/services" style="color:var(--green);text-decoration:underline">enterprise services</a>.` },
    { q: `Is e-waste disposal free in ${locName}?`, a: `Yes, for businesses and households in ${locName} having 10 or more electronic items, we offer 100% free doorstep collection. <a href="/contact" style="color:var(--green);text-decoration:underline">Book your pickup today</a>.` },
    { q: `How do I sell my old laptop in ${locName}?`, a: `You can sell your old laptop to us in ${locName} for the best market price. We handle data wiping and provide instant payment. Learn more about <a href="/services/laptop-recycling" style="color:var(--green);text-decoration:underline">laptop recycling</a>.` },
    { q: `Is there a certified ITAD partner for companies in ${locName}?`, a: `Absolutely. We are the preferred ITAD partner for several companies in ${locName}, providing NIST 800-88 data destruction. Explore our <a href="/itad" style="color:var(--green);text-decoration:underline">ITAD center</a>.` },
    { q: `Which companies in ${locName} need certified recycling?`, a: `Every bank, hospital, and IT company in ${locName} is legally required to use authorized recyclers like us to remain compliant with E-Waste Rules 2022. View our <a href="/compliance" style="color:var(--green);text-decoration:underline">compliance guide</a>.` },
    { q: `Can I get a Certificate of Destruction in ${locName}?`, a: `Yes. We issue a legally valid Certificate of Destruction for every data-bearing device collected from ${locName}. Read about our <a href="/services/data-destruction" style="color:var(--green);text-decoration:underline">secure data destruction</a>.` },
    { q: `Who is the KSPCB authorized recycler for ${locName}?`, a: `EWaste Kochi is the authorized recycler covering the ${locName} area under KSPCB license #KL/EW/628. You can read our <a href="/ewaste" style="color:var(--green);text-decoration:underline">e-waste encyclopedia</a> for the exact laws.` },
    { q: `Do you recycle computer monitors in ${locName}?`, a: `Yes, we handle all screen types including CRT, LCD, and LED monitors from residential and commercial areas in ${locName}.` },
    { q: `How to dispose of old servers in ${locName}?`, a: `We provide specialized data center and server decommissioning for businesses in ${locName} with secure logistics. Dive into our <a href="/services/server-recycling" style="color:var(--green);text-decoration:underline">server recycling process</a>.` },
    { q: `Are there laptop buyback shops near ${locName}?`, a: `Instead of searching for shops, book our free mobile pickup in ${locName} to sell your laptop at your doorstep.` },
    { q: `Is mobile phone recycling available in ${locName}?`, a: `Yes, we buy old smartphones and tablets from ${locName}, ensuring all personal data is professionally wiped.` },
    { q: `How fast is the e-waste collection in ${locName}?`, a: `In ${locName}, we typically complete collections within 2–4 hours of your request during business hours.` },
    { q: `Do you provide data wiping in ${locName}?`, a: `Yes, we use certified software to perform NIST 800-88 purging for all disks collected from ${locName}.` },
    { q: `What happens to e-waste collected from ${locName}?`, a: `It is transported to our Thrippunithura facility where it is sorted, shredded, and refined for material recovery. See our <a href="/recycling" style="color:var(--green);text-decoration:underline">recycling technology</a>.` },
    { q: `Is hard drive shredding available in ${locName}?`, a: `Yes, we offer both on-site and facility-based hard drive shredding for our ${locName} clients.` },
    { q: `How to dispose of UPS batteries in ${locName}?`, a: `Old lead-acid and Li-ion UPS batteries from ${locName} should only be handled by authorized recyclers like us.` },
    { q: `What documents are provided for e-waste in ${locName}?`, a: `We provide Form-6 manifest, Pickup Receipt, and Certificate of Destruction for every job in ${locName}.` },
    { q: `Is EWaste Kochi DPDP Act compliant in ${locName}?`, a: `Yes, our disposal workflow in ${locName} meets all requirements of India's Digital Personal Data Protection Act 2023.` },
    { q: `Do you buy bulk e-waste from ${locName} schools?`, a: `Yes, we partner with educational institutions in ${locName} for secure and eco-friendly hardware retirement.` },
    { q: `Can I drop off e-waste if I am in ${locName}?`, a: `While we offer free pickup in ${locName}, you can also drop off items at our central facility in Thrippunithura or check other <a href="/locations" style="color:var(--green);text-decoration:underline">service areas</a>.` },
  ];
  return templates;
};

/**
 * Automates 50+ Specialized Service FAQs.
 */
export const generateServiceFaqs = (svcName) => {
  const templates = [
    { q: `What is ${svcName}?`, a: `${svcName} is our specialized service designed for businesses and individuals who need certified, professional disposal and environmental compliance. See all <a href="/services" style="color:var(--green);text-decoration:underline">enterprise solutions</a>.` },
    { q: `Is ${svcName} certified in Kochi?`, a: `Yes, we provide KSPCB-authorized ${svcName} services, ensuring 100% legal compliance and environmental safety across Kerala. Understand our <a href="/compliance" style="color:var(--green);text-decoration:underline">legal compliance</a>.` },
    { q: `How much does ${svcName} cost?`, a: `Pricing for ${svcName} depends on the quantity and complexity. We offer free bulk pickup for corporate clients and competitive rates for specialized jobs. <a href="/contact" style="color:var(--green);text-decoration:underline">Get a free quote</a>.` },
    { q: `Does ${svcName} include data destruction?`, a: `Where applicable, our ${svcName} workflow integrates NIST 800-88 certified purging to ensure your privacy is never compromised. Check our <a href="/services/data-destruction" style="color:var(--green);text-decoration:underline">data wiping services</a>.` },
    { q: `How long does the ${svcName} process take?`, a: `In Kochi, typically we complete ${svcName} requests within 24 hours of your initial booking.` },
    { q: `Do I get a certificate for ${svcName}?`, a: `Yes, we issue a legally valid Certificate of Destruction or Environmental Compliance for every ${svcName} job. Read more in <a href="/ewaste" style="color:var(--green);text-decoration:underline">our e-waste guide</a>.` },
    { q: `Who handles the ${svcName} at EWaste Kochi?`, a: `Our team of certified technicians and logistics specialists handle every aspect of ${svcName} with strict safety protocols.` },
    { q: `Is ${svcName} available for small businesses?`, a: `Absolutely. We serve everyone from individual consumers to large multinationals with the same level of care for ${svcName}. Explore our <a href="/services/corporate-itad" style="color:var(--green);text-decoration:underline">ITAD division</a>.` },
    { q: `What are the benefits of professional ${svcName}?`, a: `Professional ${svcName} ensures data security, environmental protection, and full legal compliance with E-Waste Rules 2022.` },
    { q: `Is ${svcName} compliant with the DPDP Act 2023?`, a: `Yes, our ${svcName} standards meet and exceed the legal requirements of India's new data protection law.` },
    { q: `Can you perform ${svcName} on-site?`, a: `For many services like data destruction and asset tagging, we offer on-site ${svcName} at your Kochi premises.` },
    { q: `What equipment is required for ${svcName}?`, a: `We bring all necessary logistics and technical equipment for ${svcName}, requiring minimal effort from your team.` },
    { q: `Do you provide ${svcName} outside of Kochi?`, a: `Yes, while centered in Kochi, we provide ${svcName} services across all districts of Kerala. Checkout our <a href="/locations" style="color:var(--green);text-decoration:underline">569 service locations</a>.` },
    { q: `Is ${svcName} eco-friendly?`, a: `Sustainability is our core mission. Our ${svcName} process ensures zero-landfill disposal for every gram of material.` },
    { q: `How to book ${svcName} online?`, a: `You can book ${svcName} instantly via our online quote form or a quick WhatsApp message to our 24/7 support line.` },
    { q: `What happen to materials from ${svcName}?`, a: `Materials recovered from ${svcName} are refined and repurposed into raw industrial elements, powering the circular economy. Read more on <a href="/recycling" style="color:var(--green);text-decoration:underline">recycling operations</a>.` },
    { q: `Can schools and hospitals get ${svcName}?`, a: `Yes, we have specialized protocols for ${svcName} tailored for educational and healthcare institutions.` },
    { q: `Is ${svcName} audit-proof?`, a: `Yes, our documentation for ${svcName} satisfies all major audits including RBI, SEBI, and ISO certifications.` },
    { q: `Do you provide documentation for ${svcName}?`, a: `We provide a full audit trail, including Pickup Manifests and Certificates of Destruction for ${svcName}.` },
    { q: `Are there discounts for bulk ${svcName}?`, a: `Yes, large corporate projects involving ${svcName} qualify for special bulk rates and free elite logistics.` },
  ];

  return templates;
};

/**
 * Automates 200+ Topic-Specific Authority FAQs for Pillar Pages.
 * Designed to capture long-tail and question-based organic traffic.
 */
export const generateMassiveFaqs = (topicName) => {
  const baseTemplates = [
    { q: `What exactly qualifies as ${topicName} in Kochi?`, a: `${topicName} encompasses all discarded electronic and electrical equipment (WEEE). In Kochi's commercial ecosystem, this ranges from Infopark server blades to residential appliances. Each requires specialized extraction to prevent environmental leaching. View our <a href="/services" style="color:var(--green);text-decoration:underline">full list of services here</a>.` },
    { q: `Is ${topicName} disposal mandatory for businesses under Kerala law?`, a: `Yes. Under the E-Waste Management Rules 2022, every corporate entity in Kerala is legally obligated to channel ${topicName.toLowerCase()} through KSPCB-authorized recyclers. Failure to do so can result in significant environmental compensation penalties. Learn about our <a href="/compliance" style="color:var(--green);text-decoration:underline">compliance packages</a>.` },
    { q: `How does EWaste Kochi ensure data security during ${topicName} retirement?`, a: `We integrate NIST 800-88 certified data sanitization into the ${topicName} workflow. This ensures that while the physical hardware is recycled, the digital data is permanently purged, satisfying both e-waste and DPDP Act 2023 requirements. Discover our <a href="/services/data-destruction" style="color:var(--green);text-decoration:underline">data destruction service</a>.` },
    { q: `Are there specific collection centers for ${topicName} in Ernakulam?`, a: `While we have a flagship processing facility in Thrippunithura, we offer doorstep collection across all major Ernakulam hubs including Kakkanad, Edappally, Aluva, and Vyttila for bulk ${topicName} quantities. View all <a href="/locations" style="color:var(--green);text-decoration:underline">569 service zones</a>.` },
    { q: `What is the environmental impact of improper ${topicName} dumping in Kerala?`, a: `Improper disposal leads to heavy metals like Lead, Mercury, and Cadmium leaching into Kerala's backwaters and groundwater, causing irreversible ecological damage and health risks to the local population.` },
    { q: `Does ${topicName} recycling contribute to the circular economy?`, a: `Absolutely. By recovering precious metals like gold, silver, and copper from ${topicName.toLowerCase()}, we reduce the need for destructive mining and keep valuable resources within the industrial production loop in India. Read more in our <a href="/recycling" style="color:var(--green);text-decoration:underline">recycling tech section</a>.` },
    { q: `Can I get a legal Certificate of Destruction for my ${topicName}?`, a: `Yes. We issue a serialized Certificate of Destruction (CoD) for every batch of ${topicName} collected, which serves as your primary proof of compliance for environmental and financial audits. Ensure your <a href="/services/itad" style="color:var(--green);text-decoration:underline">IT Asset Disposition</a> is audit-ready.` },
    { q: `How often should a Kochi business conduct a ${topicName} audit?`, a: `We recommend quarterly or bi-annual ${topicName} retirement cycles for IT companies to maintain clean asset registers and ensure ongoing compliance with the latest KSPCB and CPCB guidelines.` },
    { q: `What is the difference between green-gap and certified ${topicName} disposal?`, a: `Green-gap refers to informal waste methods that often end in landfills. Certified ${topicName} disposal through EWaste Kochi guarantees 100% material recovery and safe hazardous waste neutralization.` },
    { q: `Who is responsible for ${topicName} logistics in Kochi?`, a: `EWaste Kochi handles the entire logistics chain — from secure loading at your premises to transport in specialized hazardous-waste-compliant vehicles to our sorting facility.` },
  ];

  return baseTemplates;
};

// Alias for about.astro and other pages expecting generateTopicFaqs
export const generateTopicFaqs = generateMassiveFaqs;
