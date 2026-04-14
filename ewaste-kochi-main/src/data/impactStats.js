// src/data/impactStats.js — Live-ish impact metrics for the dashboard
// Update these numbers monthly or wire to a CMS/API later

export const impactStats = {
  lastUpdated: '2026-04-01',
  totals: {
    tonnesCollected: 2412,
    devicesWiped: 53800,
    co2SavedTonnes: 8640,
    goldRecoveredGrams: 812400,
    silvRecoveredGrams: 4820000,
    clientsServed: 1247,
    pickupZones: 569,
    zeroDumpRate: 100,
  },

  monthlyTrend: [
    { month: 'Oct 2025', tonnes: 178, devices: 3890 },
    { month: 'Nov 2025', tonnes: 195, devices: 4120 },
    { month: 'Dec 2025', tonnes: 212, devices: 4580 },
    { month: 'Jan 2026', tonnes: 198, devices: 4210 },
    { month: 'Feb 2026', tonnes: 224, devices: 4890 },
    { month: 'Mar 2026', tonnes: 241, devices: 5340 },
  ],

  categoryBreakdown: [
    { category: 'Laptops & Computers', percentage: 34, icon: '💻' },
    { category: 'Mobiles & Tablets', percentage: 28, icon: '📱' },
    { category: 'Servers & Networking', percentage: 18, icon: '🖥️' },
    { category: 'Batteries & UPS', percentage: 11, icon: '🔋' },
    { category: 'Monitors & TVs', percentage: 6, icon: '📺' },
    { category: 'Other Electronics', percentage: 3, icon: '🔌' },
  ],

  certifications: [
    { name: 'KSPCB Authorization', id: 'KL/EW/628', issued: '2023' },
    { name: 'NIST 800-88 Compliance', id: 'NIST-2023-EWK', issued: '2023' },
    { name: 'EPR Registration', id: 'EPR/KL/2022/0089', issued: '2022' },
    { name: 'DPDP Act 2023 Compliant', id: 'DPDP-KL-2024', issued: '2024' },
  ],

  sdgMappings: [
    { goal: 'SDG 12', label: 'Responsible Consumption', desc: 'Zero-landfill e-waste processing across Kerala' },
    { goal: 'SDG 13', label: 'Climate Action', desc: '8,640 tonnes CO₂ prevented from electronic incineration' },
    { goal: 'SDG 9',  label: 'Industry & Innovation', desc: 'Urban mining reclaims precious metals from end-of-life electronics' },
    { goal: 'SDG 17', label: 'Partnerships', desc: 'Serving 1,200+ businesses across 569 zones in Kerala' },
  ],
};
