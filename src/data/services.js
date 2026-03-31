// ═══════════════════════════════════════════════════════════════════
// SERVICES DATA — Single Source of Truth
// 80+ services for programmatic SEO generation
// Each service generates: /services/[slug] page
// ═══════════════════════════════════════════════════════════════════

export const services = [
  // ── PILLAR SERVICES (Primary money pages) ──────────────────────
  {
    slug: 'e-waste-recycling-kochi',
    name: 'E-Waste Recycling Kochi',
    shortName: 'E-Waste Recycling',
    category: 'recycling',
    isPillar: true,
    icon: '♻️',
    tagline: 'Kerala\'s Most Trusted Certified E-Waste Recycler',
    description: 'Certified e-waste collection, processing and recycling in Kochi. Free bulk pickup for corporates. Eco-friendly disposal compliant with E-Waste Rules 2022 and EPR guidelines.',
    longDescription: `EWaste Kochi provides comprehensive e-waste recycling services across Kochi, Ernakulam and Kerala. As an authorized KSPCB recycler operating under EPR authorization, we handle all categories of electronic waste from consumer electronics to large industrial equipment.

Our facility in Thrippunithura uses state-of-the-art processing equipment to safely dismantle, sort, and recover valuable materials from discarded electronics — including gold, silver, copper, and rare earth metals — while ensuring zero hazardous material reaches landfills.

Free bulk pickup is available for corporate clients disposing of 10+ devices across all of Kochi including Infopark, Smart City, Kakkanad, Edapally, and beyond.`,
    keywords: ['e-waste recycling kochi', 'ewaste kochi', 'e-waste disposal kochi', 'electronics recycling kerala', 'certified e-waste recycler kochi', 'e-waste collection kochi'],
    metaTitle: 'E-Waste Recycling Kochi | Certified KSPCB Authorized | Free Pickup | EWaste Kochi',
    metaDescription: 'Kerala\'s #1 certified e-waste recycling in Kochi. Free bulk pickup across Ernakulam, KSPCB authorized, EPR compliant. Call 24/7 for same-day collection.',
    price: 'Free bulk pickup (10+ devices)',
    priceSchema: '0',
    priceCurrency: 'INR',
    badges: ['KSPCB Authorized', 'EPR Compliant', 'Free Pickup'],
    relatedServices: ['itad-kochi', 'data-destruction-kochi', 'battery-recycling-kochi'],
    schemaType: 'RecyclingService',
  },
  {
    slug: 'itad-kochi',
    name: 'ITAD Services Kochi',
    shortName: 'ITAD',
    category: 'itad',
    isPillar: true,
    icon: '🏢',
    tagline: 'NIST/DoD Certified IT Asset Disposition',
    description: 'Complete IT Asset Disposition for businesses in Kochi. Asset tagging, NIST/DoD certified data destruction, remarketing, and full audit trail documentation.',
    longDescription: `IT Asset Disposition (ITAD) is the certified, auditable process of safely retiring your organization's IT equipment. EWaste Kochi offers end-to-end ITAD services for corporate clients across Kochi, Infopark, Smart City, and all of Kerala.

Our ITAD process includes: complete asset inventory and tagging, chain-of-custody documentation, NIST 800-88/DoD 5220.22-M certified data destruction, remarketing of residual value equipment, EPR-compliant recycling, and Certificate of Destruction for every device.

We are DPDP Act 2023 compliant, making us the right choice for banks, IT companies, hospitals, and government organizations with strict data governance requirements.`,
    keywords: ['ITAD kochi', 'IT asset disposal kochi', 'IT asset disposition kerala', 'corporate ITAD kochi', 'IT equipment disposal kochi', 'ITAD infopark'],
    metaTitle: 'ITAD Services Kochi Kerala | Certified IT Asset Disposition | EWaste Kochi',
    metaDescription: 'Certified ITAD in Kochi — complete IT asset disposition with NIST/DoD data destruction, Certificate of Destruction, DPDP Act 2023 compliant. Serving Infopark, Kakkanad & all Kerala.',
    price: 'Quote-based',
    badges: ['NIST 800-88', 'DoD 5220.22-M', 'DPDP Compliant', 'Certificate of Destruction'],
    relatedServices: ['data-destruction-kochi', 'hard-drive-shredding-kochi', 'e-waste-recycling-kochi'],
    schemaType: 'ProfessionalService',
  },
  {
    slug: 'data-destruction-kochi',
    name: 'Data Destruction Kochi',
    shortName: 'Data Destruction',
    category: 'data',
    isPillar: true,
    icon: '🔐',
    tagline: 'NIST 800-88 & DoD Certified Data Sanitization',
    description: 'NIST 800-88 and DoD 5220.22-M certified data destruction in Kochi. Software wiping and physical shredding. Certificate of Destruction issued for every device.',
    longDescription: `Data destruction is not just formatting — it's verifiable, certified elimination of all data from storage media. EWaste Kochi provides two levels of certified data destruction:

**Software-Based Wiping (NIST 800-88 Purge):** Multi-pass overwriting using industry-standard algorithms that renders data permanently unrecoverable while preserving the physical drive for reuse or resale.

**Physical Shredding:** Industrial-grade shredding that reduces hard drives, SSDs, and storage media to metal fragments. The highest security option for classified or highly sensitive data.

Every job — regardless of size — receives a Certificate of Destruction listing each device's serial number, destruction method, date, and our authorization details. Essential for DPDP Act 2023, RBI, SEBI, and ISO 27001 compliance.`,
    keywords: ['data destruction kochi', 'data wiping kochi', 'certified data destruction kerala', 'NIST data destruction kochi', 'DoD data wiping kochi', 'secure data erasure kochi'],
    metaTitle: 'Data Destruction Kochi | NIST 800-88 & DoD Certified | Certificate of Destruction | EWaste Kochi',
    metaDescription: 'Certified data destruction in Kochi — NIST 800-88 wiping + physical shredding. Certificate of Destruction every job. DPDP Act 2023 & RBI audit compliant.',
    price: '₹200 – ₹1,500 per device',
    priceSchema: '200',
    priceCurrency: 'INR',
    badges: ['NIST 800-88', 'DoD 5220.22-M', 'Certificate of Destruction', 'DPDP Compliant'],
    relatedServices: ['hard-drive-shredding-kochi', 'itad-kochi', 'server-recycling-kochi'],
    schemaType: 'ProfessionalService',
  },
  {
    slug: 'hard-drive-shredding-kochi',
    name: 'Hard Drive Shredding Kochi',
    shortName: 'Hard Drive Shredding',
    category: 'data',
    isPillar: true,
    icon: '⚙️',
    tagline: 'Physical Destruction of Hard Drives & SSDs',
    description: 'Industrial hard drive shredding in Kochi. Reduces HDDs, SSDs, tapes, and all storage media to fragments. On-site witnessed destruction available. CoD included.',
    longDescription: `Physical hard drive shredding is the gold standard for irreversible data destruction. EWaste Kochi's industrial shredders reduce hard drives, SSDs, magnetic tapes, USB drives, and all storage media to small metal fragments — making data recovery physically impossible.

**What we shred:** HDDs (all sizes), SSDs, NVMe drives, M.2 drives, magnetic tapes, LTO tapes, USB flash drives, memory cards, optical media, mobile phones, and tablets.

**On-Site Witnessed Destruction:** For maximum security and compliance, we offer on-site shredding at your Kochi premises with a secure destruction unit. Watch the shredding happen, receive photos/video evidence, and get your Certificate of Destruction same-day.

Pricing starts at ₹500 per drive for standard shredding with Certificate of Destruction included.`,
    keywords: ['hard drive shredding kochi', 'HDD shredding kochi', 'SSD destruction kochi', 'hard drive destruction kerala', 'on-site shredding kochi', 'physical data destruction kochi'],
    metaTitle: 'Hard Drive Shredding Kochi | On-Site & Facility | Certificate of Destruction | EWaste Kochi',
    metaDescription: 'Industrial hard drive shredding in Kochi. HDDs, SSDs, tapes, all media. On-site witnessed destruction available. Certificate of Destruction included from ₹500/drive.',
    price: 'From ₹500 per drive',
    priceSchema: '500',
    priceCurrency: 'INR',
    badges: ['Physical Shredding', 'On-Site Available', 'Certificate Included', 'All Media Types'],
    relatedServices: ['data-destruction-kochi', 'itad-kochi', 'e-waste-recycling-kochi'],
    schemaType: 'ProfessionalService',
  },
  {
    slug: 'laptop-buyback-kochi',
    name: 'Laptop Buyback Kochi',
    shortName: 'Laptop Buyback',
    category: 'buyback',
    isPillar: true,
    icon: '💻',
    tagline: 'Best Laptop Buyback Prices in Kochi',
    description: 'Sell your old laptop in Kochi at the best prices. All brands accepted — Dell, HP, Lenovo, Apple, Asus, Acer. Same-day payment via UPI/bank transfer.',
    longDescription: `Get the best value for your old laptops in Kochi. EWaste Kochi buys used laptops, MacBooks, gaming laptops, notebooks, and Chromebooks from all major brands in any condition — working, damaged, or non-functional.

**Brands we buy:** Dell, HP, Lenovo, Apple MacBook, Asus, Acer, MSI, Razer, Samsung, Toshiba, Sony, and all other brands.

**How it works:** Use our online calculator for an instant estimate → book a free pickup or walk in → device inspection (15 min) → data securely wiped → same-day payment via Cash, UPI, NEFT, or bank transfer.

**Best prices for:** Business laptops (ThinkPad, EliteBook, Latitude), MacBook Pro, MacBook Air, gaming laptops, and bulk office laptop disposal (10+ units get special rates).`,
    keywords: ['laptop buyback kochi', 'sell old laptop kochi', 'sell laptop kochi', 'sell macbook kochi', 'laptop resale kochi', 'used laptop buyer kochi'],
    metaTitle: 'Laptop Buyback Kochi | Best Prices | All Brands | Same-Day Payment | EWaste Kochi',
    metaDescription: 'Sell your old laptop in Kochi at the best prices. All brands, any condition. Dell, HP, Lenovo, Apple MacBook. Free pickup, same-day UPI payment. Instant online estimate.',
    price: '₹2,000 – ₹80,000+ depending on model',
    badges: ['All Brands', 'Same-Day Payment', 'Free Pickup', 'Data Wiped'],
    relatedServices: ['mobile-recycling-kochi', 'e-waste-recycling-kochi', 'itad-kochi'],
    schemaType: 'BuyAction',
  },
  {
    slug: 'free-ewaste-pickup-kochi',
    name: 'Free E-Waste Pickup Kochi',
    shortName: 'Free Pickup',
    category: 'pickup',
    isPillar: true,
    icon: '🚚',
    tagline: 'Same-Day & Next-Day E-Waste Collection',
    description: 'Free e-waste pickup across Kochi and Ernakulam. Corporate clients with 10+ devices get free doorstep collection. Same-day pickup available for Infopark and Smart City.',
    longDescription: `EWaste Kochi offers free doorstep e-waste pickup across all of Kochi and Ernakulam for corporate clients disposing of 10 or more devices. For urgent requirements at Infopark, Smart City, or Kakkanad, we can often arrange pickup within 2–4 hours.

**Coverage area:** Infopark, Smart City, Kakkanad, Edapally, Vyttila, Palarivattom, Aluva, Angamaly, Thrissur road, Perumbavoor, Muvattupuzha, Thrippunithura, Maradu, Kalamassery, Eloor, Kalady, Piravom, and all of Ernakulam district.

**What happens during pickup:** Our uniformed team arrives with a secure vehicle → signs your inventory manifest → issues a pickup receipt → transports to our certified facility → you receive your Certificate of Destruction within 24 hours.

Individual/residential walk-in drop-off is always free at our Thrippunithura facility.`,
    keywords: ['free e-waste pickup kochi', 'ewaste collection kochi', 'free ewaste collection ernakulam', 'same day pickup ewaste kochi', 'e-waste doorstep pickup kochi'],
    metaTitle: 'Free E-Waste Pickup Kochi | Same-Day Collection | Infopark, Kakkanad, Edapally | EWaste Kochi',
    metaDescription: 'Free e-waste pickup across Kochi & Ernakulam. 10+ devices = free corporate collection. Same-day pickup at Infopark & Smart City. Call 24/7.',
    price: 'Free for 10+ devices',
    priceSchema: '0',
    priceCurrency: 'INR',
    badges: ['Free Pickup', 'Same-Day', '24/7 Service', 'All Areas'],
    relatedServices: ['e-waste-recycling-kochi', 'itad-kochi', 'data-destruction-kochi'],
    schemaType: 'Service',
  },
  {
    slug: 'battery-recycling-kochi',
    name: 'Battery Recycling Kochi',
    shortName: 'Battery Recycling',
    category: 'recycling',
    isPillar: true,
    icon: '🔋',
    tagline: 'Safe Li-Ion, Lead-Acid & Laptop Battery Disposal',
    description: 'Safe and legal battery recycling in Kochi. Li-ion, lead-acid, laptop batteries, UPS batteries, EV batteries. KSPCB authorized. Free bulk collection.',
    longDescription: `Batteries are among the most hazardous e-waste. Lithium-ion, lead-acid, and NiMH batteries contain toxic heavy metals that can cause fires, explosions, and severe environmental contamination if improperly disposed.

EWaste Kochi has KSPCB authorization to safely collect, transport, and recycle all battery types including laptop/phone Li-ion packs, lead-acid UPS and automotive batteries, large EV/industrial battery packs, alkaline and NiMH consumer batteries, and data center battery backup systems.

**Why certified battery recycling matters:** Under the Battery Waste Management Rules 2022, producers, importers, and large consumers of batteries must use authorized recyclers. Penalties for non-compliance can reach ₹1 lakh per ton.`,
    keywords: ['battery recycling kochi', 'battery disposal kochi', 'laptop battery disposal kochi', 'lithium battery recycling kerala', 'UPS battery disposal kochi', 'EV battery recycling kochi'],
    metaTitle: 'Battery Recycling Kochi | Li-Ion, Lead-Acid, UPS, EV Batteries | KSPCB Authorized | EWaste Kochi',
    metaDescription: 'Safe battery recycling in Kochi. Li-ion, lead-acid, laptop, UPS, EV batteries. KSPCB authorized. Free bulk collection. Battery Waste Rules 2022 compliant.',
    price: 'Free bulk collection',
    badges: ['KSPCB Authorized', 'All Battery Types', 'Battery Rules 2022', 'Free Bulk Pickup'],
    relatedServices: ['e-waste-recycling-kochi', 'server-recycling-kochi', 'mobile-recycling-kochi'],
    schemaType: 'RecyclingService',
  },
  {
    slug: 'server-recycling-kochi',
    name: 'Server & Data Centre Recycling Kochi',
    shortName: 'Server Recycling',
    category: 'itad',
    isPillar: false,
    icon: '🖥️',
    tagline: 'Secure Decommissioning of Servers & Data Centres',
    description: 'Complete server and data centre decommissioning in Kochi. Rack servers, blade systems, network equipment. ITAD compliance, data destruction, and eco-friendly recycling.',
    longDescription: `Decommissioning servers and data centre infrastructure requires careful planning, certified data destruction, and compliant recycling. EWaste Kochi provides end-to-end data centre decommissioning services for IT companies, banks, hospitals, and government organizations across Kerala.

**What we handle:** Rack servers (Dell PowerEdge, HP ProLiant, IBM), blade systems, UPS systems, network switches and routers, storage arrays (SAN/NAS), patch panels, PDUs, server racks and cabinets, cabling, and KVM equipment.

**Our process:** Inventory → chain-of-custody documentation → NIST/DoD data destruction on all drives → physical shredding for HDDs/SSDs → responsible recycling of hardware → full ITAD audit report and Certificate of Destruction.`,
    keywords: ['server recycling kochi', 'data centre decommissioning kochi', 'server disposal kochi', 'rack server recycling kerala', 'IT equipment disposal kochi'],
    metaTitle: 'Server & Data Centre Recycling Kochi | ITAD Decommissioning | EWaste Kochi',
    metaDescription: 'Server and data centre decommissioning in Kochi. Rack servers, blade systems, network equipment. Certified ITAD, data destruction, Certificate of Destruction.',
    price: 'Quote-based',
    badges: ['Data Centre Spec', 'Chain of Custody', 'Certificate Included', 'All Brands'],
    relatedServices: ['itad-kochi', 'data-destruction-kochi', 'hard-drive-shredding-kochi'],
    schemaType: 'ProfessionalService',
  },
  {
    slug: 'mobile-recycling-kochi',
    name: 'Mobile Phone Recycling Kochi',
    shortName: 'Mobile Recycling',
    category: 'buyback',
    isPillar: false,
    icon: '📱',
    tagline: 'Buy Old Phones & Tablets in Kochi',
    description: 'Sell or recycle your old smartphone in Kochi. All brands — iPhone, Samsung, OnePlus, Xiaomi, Vivo, Oppo. Data wiped, safe recycling or best buyback price.',
    longDescription: `Old smartphones and tablets are treasure troves of valuable materials — gold, silver, platinum, rare earth elements — and repositories of sensitive personal data. EWaste Kochi handles both aspects responsibly.

**Buyback:** We offer competitive prices for used iPhones, Samsung Galaxy, OnePlus, Xiaomi, Oppo, Vivo, Realme, and all Android/iOS devices. Data is professionally wiped before any resale.

**Recycling:** Non-working, broken, or very old devices are recycled through our KSPCB-authorized facility, ensuring hazardous materials like lithium, lead, and arsenic don't contaminate Kochi's environment.

**Bulk mobile recycling:** IT companies, telecom operators, and retailers with bulk handsets get free pickup and priority processing.`,
    keywords: ['mobile recycling kochi', 'sell old phone kochi', 'sell iphone kochi', 'smartphone recycling kerala', 'tablet recycling kochi', 'phone buyback kochi'],
    metaTitle: 'Mobile Phone Recycling & Buyback Kochi | iPhone, Samsung, All Brands | EWaste Kochi',
    metaDescription: 'Sell or recycle your old phone in Kochi. iPhone, Samsung, OnePlus, all brands. Data wiped, best buyback prices or responsible recycling. Free bulk pickup.',
    price: '₹500 – ₹50,000+ depending on model',
    badges: ['All Brands', 'Data Wiped', 'Same-Day Payment', 'Free Pickup'],
    relatedServices: ['laptop-buyback-kochi', 'e-waste-recycling-kochi', 'battery-recycling-kochi'],
    schemaType: 'BuyAction',
  },
  {
    slug: 'corporate-ewaste-kochi',
    name: 'Corporate E-Waste Management Kochi',
    shortName: 'Corporate E-Waste',
    category: 'corporate',
    isPillar: false,
    icon: '🏛️',
    tagline: 'Your Compliance Partner for E-Waste Rules 2022',
    description: 'End-to-end corporate e-waste management in Kochi. EPR compliance, annual disposal programs, CSR documentation, and dedicated account manager for enterprises.',
    keywords: ['corporate e-waste kochi', 'corporate ITAD kochi', 'enterprise e-waste management kerala', 'EPR compliance kochi', 'corporate electronics disposal kochi'],
    metaTitle: 'Corporate E-Waste Management Kochi | EPR Compliance | Annual Programs | EWaste Kochi',
    metaDescription: 'Corporate e-waste management in Kochi. EPR compliance, annual disposal programs, CSR documentation. DPDP Act 2023 + E-Waste Rules 2022 compliant. Dedicated account manager.',
    price: 'Annual contract available',
    badges: ['EPR Compliant', 'Annual Programs', 'CSR Documentation', 'Dedicated Manager'],
    relatedServices: ['itad-kochi', 'e-waste-recycling-kochi', 'data-destruction-kochi'],
    schemaType: 'ProfessionalService',
  },
  {
    slug: 'printer-recycling-kochi',
    name: 'Printer & MFD Recycling Kochi',
    shortName: 'Printer Recycling',
    category: 'recycling',
    isPillar: false,
    icon: '🖨️',
    tagline: 'Safe Disposal of Printers, Copiers & MFDs',
    description: 'Eco-friendly printer and multifunction device recycling in Kochi. Toner cartridges, inkjet, laser printers, photocopiers. Free corporate pickup.',
    keywords: ['printer recycling kochi', 'copier disposal kochi', 'MFD recycling kerala', 'toner cartridge recycling kochi', 'photocopier disposal kochi'],
    metaTitle: 'Printer & Copier Recycling Kochi | Toner, MFD, Laser Printers | EWaste Kochi',
    metaDescription: 'Printer, copier, and MFD recycling in Kochi. Toner cartridges, inkjet, laser printers, photocopiers. KSPCB authorized. Free corporate pickup.',
    price: 'Free bulk pickup',
    badges: ['All Printer Types', 'Toner Accepted', 'KSPCB Certified', 'Free Pickup'],
    relatedServices: ['e-waste-recycling-kochi', 'corporate-ewaste-kochi', 'itad-kochi'],
    schemaType: 'RecyclingService',
  },
  {
    slug: 'tv-monitor-recycling-kochi',
    name: 'TV & Monitor Recycling Kochi',
    shortName: 'TV & Monitor Recycling',
    category: 'recycling',
    isPillar: false,
    icon: '📺',
    tagline: 'CRT, LCD, LED, OLED Monitor & TV Disposal',
    description: 'Safe TV and computer monitor recycling in Kochi. CRT, LCD, LED, OLED, plasma screens. Contains hazardous lead and mercury — requires certified recycler.',
    keywords: ['TV recycling kochi', 'monitor recycling kochi', 'CRT disposal kochi', 'LCD recycling kerala', 'TV disposal kochi', 'screen recycling kochi'],
    metaTitle: 'TV & Monitor Recycling Kochi | CRT, LCD, LED, OLED | EWaste Kochi',
    metaDescription: 'Safe TV and monitor recycling in Kochi. CRT, LCD, LED, OLED, plasma. Contains lead/mercury — KSPCB authorized disposal. Free corporate pickup.',
    price: 'Free bulk pickup',
    badges: ['CRT Specialists', 'All Screen Types', 'Hazardous Waste Certified', 'Free Pickup'],
    relatedServices: ['e-waste-recycling-kochi', 'corporate-ewaste-kochi', 'printer-recycling-kochi'],
    schemaType: 'RecyclingService',
  },
  {
    slug: 'network-equipment-disposal-kochi',
    name: 'Network Equipment Disposal Kochi',
    shortName: 'Network Equipment',
    category: 'itad',
    isPillar: false,
    icon: '🔌',
    tagline: 'Routers, Switches, Firewalls & Network Gear',
    description: 'Secure disposal of networking equipment in Kochi. Cisco, Juniper, HP, Dell, Aruba switches, routers, firewalls. Configuration wiped, Certificate of Disposal issued.',
    keywords: ['network equipment disposal kochi', 'router disposal kochi', 'switch recycling kochi', 'Cisco disposal kochi', 'firewall disposal kerala'],
    metaTitle: 'Network Equipment Disposal Kochi | Routers, Switches, Firewalls | ITAD | EWaste Kochi',
    metaDescription: 'Secure network equipment disposal in Kochi. Cisco, Juniper, HP switches, routers, firewalls. Configuration wiped, Certificate of Disposal. Free bulk pickup.',
    price: 'Free bulk disposal',
    badges: ['Config Wiped', 'All Brands', 'Certificate Issued', 'ITAD Compliant'],
    relatedServices: ['server-recycling-kochi', 'itad-kochi', 'data-destruction-kochi'],
    schemaType: 'ProfessionalService',
  },
  {
    slug: 'ups-inverter-recycling-kochi',
    name: 'UPS & Inverter Recycling Kochi',
    shortName: 'UPS & Inverter',
    category: 'recycling',
    isPillar: false,
    icon: '⚡',
    tagline: 'Safe UPS, Inverter & Lead-Acid Battery Disposal',
    description: 'Certified UPS and inverter recycling in Kochi. Lead-acid batteries, APC, Eaton, Luminous UPS systems. Hazardous battery disposal done right.',
    keywords: ['UPS recycling kochi', 'inverter disposal kochi', 'UPS battery recycling kerala', 'APC UPS disposal kochi', 'lead acid battery recycling kochi'],
    metaTitle: 'UPS & Inverter Recycling Kochi | Lead-Acid Battery Disposal | KSPCB Authorized | EWaste Kochi',
    metaDescription: 'UPS and inverter recycling in Kochi. Lead-acid batteries, APC, Eaton, Luminous. KSPCB authorized, Battery Rules 2022 compliant. Free bulk collection.',
    price: 'Free bulk collection',
    badges: ['Battery Rules 2022', 'Lead-Acid Certified', 'KSPCB Authorized', 'All Brands'],
    relatedServices: ['battery-recycling-kochi', 'server-recycling-kochi', 'e-waste-recycling-kochi'],
    schemaType: 'RecyclingService',
  },
  {
    slug: 'air-conditioner-recycling-kochi',
    name: 'Air Conditioner Recycling Kochi',
    shortName: 'AC Recycling',
    category: 'recycling',
    isPillar: false,
    icon: '❄️',
    tagline: 'Eco-Friendly AC & Refrigerator Disposal',
    description: 'Certified air conditioner and large appliance recycling in Kochi. Safe refrigerant recovery, compressor recycling. KSPCB authorized.',
    keywords: ['AC recycling kochi', 'air conditioner disposal kochi', 'refrigerator recycling kochi', 'large appliance disposal kerala', 'old AC disposal kochi'],
    metaTitle: 'Air Conditioner Recycling Kochi | AC Disposal, Refrigerant Recovery | KSPCB | EWaste Kochi',
    metaDescription: 'Certified AC and large appliance recycling in Kochi. Safe refrigerant recovery, compressor recycling. KSPCB authorized. Free corporate pickup.',
    price: 'Free bulk pickup',
    badges: ['Refrigerant Recovery', 'KSPCB Certified', 'All Brands', 'Free Pickup'],
    relatedServices: ['e-waste-recycling-kochi', 'corporate-ewaste-kochi'],
    schemaType: 'RecyclingService',
  },
  {
    slug: 'dpdp-act-compliance-kochi',
    name: 'DPDP Act 2023 Compliance Kochi',
    shortName: 'DPDP Compliance',
    category: 'compliance',
    isPillar: false,
    icon: '⚖️',
    tagline: 'Data Destruction for DPDP Act 2023 Compliance',
    description: 'DPDP Act 2023 compliant data destruction services in Kochi. Certificate of Destruction, audit trail, and compliance documentation for Indian data protection law.',
    keywords: ['DPDP Act 2023 compliance kochi', 'DPDP ewaste kochi', 'data protection compliance kochi', 'DPDP data destruction kerala'],
    metaTitle: 'DPDP Act 2023 Compliance Kochi | Certified Data Destruction | EWaste Kochi',
    metaDescription: 'DPDP Act 2023 compliant data destruction in Kochi. Certificate of Destruction + full audit trail. India\'s data protection law compliance made simple.',
    price: '₹200 – ₹1,500 per device',
    badges: ['DPDP Compliant', 'Audit Trail', 'Certificate of Destruction', 'Legal Documentation'],
    relatedServices: ['data-destruction-kochi', 'itad-kochi', 'hard-drive-shredding-kochi'],
    schemaType: 'ProfessionalService',
  },
  {
    slug: 'certificate-of-destruction-kochi',
    name: 'Certificate of Destruction Kochi',
    shortName: 'Certificate of Destruction',
    category: 'compliance',
    isPillar: false,
    icon: '📜',
    tagline: 'Legal CoD for Every Data Destruction Job',
    description: 'Legally valid Certificate of Destruction issued for every job. RBI, SEBI, ISO 27001, DPDP Act compliant. Lists device serial numbers, destruction method and date.',
    keywords: ['certificate of destruction kochi', 'CoD ewaste kochi', 'data destruction certificate kerala', 'CoD for RBI audit kochi'],
    metaTitle: 'Certificate of Destruction Kochi | RBI, SEBI, ISO 27001 | EWaste Kochi',
    metaDescription: 'Legally valid Certificate of Destruction for every data destruction job in Kochi. RBI, SEBI, ISO 27001, DPDP Act compliant. Issued within 24 hours.',
    price: 'Included in all jobs',
    badges: ['RBI Compliant', 'SEBI Compliant', 'ISO 27001', 'DPDP Act'],
    relatedServices: ['data-destruction-kochi', 'hard-drive-shredding-kochi', 'itad-kochi'],
    schemaType: 'ProfessionalService',
  },
];

// Derived collections for convenience
export const pillarServices = services.filter(s => s.isPillar);
export const supportingServices = services.filter(s => !s.isPillar);
export const servicesByCategory = services.reduce((acc, s) => {
  if (!acc[s.category]) acc[s.category] = [];
  acc[s.category].push(s);
  return acc;
}, {});

export const getServiceBySlug = (slug) => services.find(s => s.slug === slug);

export const categories = [
  { id: 'recycling', name: 'E-Waste Recycling', icon: '♻️' },
  { id: 'itad', name: 'ITAD & Data Security', icon: '🔐' },
  { id: 'data', name: 'Data Destruction', icon: '💾' },
  { id: 'buyback', name: 'Buyback & Resale', icon: '💰' },
  { id: 'pickup', name: 'Pickup & Logistics', icon: '🚚' },
  { id: 'corporate', name: 'Corporate Programs', icon: '🏢' },
  { id: 'compliance', name: 'Compliance & Legal', icon: '⚖️' },
];
