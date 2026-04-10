export interface Product {
  id: string;
  name: string;
  category: 'laptop' | 'tablet' | 'projector' | 'headphone' | 'accessory';
  brand: string;
  price: number;
  description: string;
  specs: Record<string, string>;
  image?: string;
  condition: 'Refurbished' | 'Open Box' | 'Pre-owned';
}

export const products: Product[] = [
  {
    id: 'macbook-air-m1',
    name: 'MacBook Air M1',
    category: 'laptop',
    brand: 'Apple',
    price: 52900,
    description: 'Thin and light laptop with the revolutionary M1 chip. Ideal for students and professionals.',
    specs: {
      cpu: 'Apple M1 (8-Core)',
      gpu: '7-Core / 8-Core GPU',
      ram: '8GB / 16GB',
      storage: '256GB / 512GB SSD',
      display: '13.3-inch Retina'
    },
    condition: 'Refurbished'
  },
  {
    id: 'macbook-air-m2',
    name: 'MacBook Air M2',
    category: 'laptop',
    brand: 'Apple',
    price: 79900,
    description: 'Redesigned with the M2 chip. Thinner, lighter, and more powerful.',
    specs: {
      cpu: 'Apple M2 (8-Core)',
      gpu: '8-Core / 10-Core GPU',
      ram: '8GB / 16GB / 24GB',
      storage: '256GB / 512GB / 1TB SSD',
      display: '13.6-inch Liquid Retina'
    },
    condition: 'Open Box'
  },
  {
    id: 'macbook-pro-m1-14',
    name: 'MacBook Pro 14" M1 Pro',
    category: 'laptop',
    brand: 'Apple',
    price: 125000,
    description: 'Pro performance for developers and creators.',
    specs: {
      cpu: 'M1 Pro (8-Core / 10-Core)',
      gpu: '14-Core / 16-Core GPU',
      ram: '16GB / 32GB',
      storage: '512GB / 1TB SSD',
      display: '14.2-inch Liquid Retina XDR'
    },
    condition: 'Refurbished'
  },
  {
    id: 'macbook-pro-m3-14',
    name: 'MacBook Pro 14" M3',
    category: 'laptop',
    brand: 'Apple',
    price: 159900,
    description: 'The latest MacBook Pro with the M3 chip family.',
    specs: {
      cpu: 'Apple M3 (8-Core)',
      gpu: '10-Core GPU',
      ram: '8GB / 16GB / 24GB',
      storage: '512GB / 1TB SSD',
      display: '14.2-inch Liquid Retina XDR'
    },
    condition: 'Open Box'
  },
  {
    id: 'zenbook-flip-s13',
    name: 'ASUS ZenBook Flip S13 OLED',
    category: 'laptop',
    brand: 'ASUS',
    price: 94999,
    description: 'Ultra-thin 2-in-1 with a stunning 4K OLED HDR display.',
    specs: {
      cpu: 'Intel Core i7-1165G7',
      ram: '16GB LPDDR4X',
      storage: '1TB PCIe SSD',
      display: '13.3-inch 4K OLED Touch'
    },
    condition: 'Refurbished'
  },
  {
    id: 'epson-eb-e01',
    name: 'Epson EB-E01 XGA Projector',
    category: 'projector',
    brand: 'Epson',
    price: 32000,
    description: 'High-quality, mobile projector for the home or office with 3LCD technology.',
    specs: {
      brightness: '3300 Lumens',
      resolution: 'XGA (1024x768)',
      contrast: '15,000:1',
      lampLife: '12,000 hours (Eco)'
    },
    condition: 'Refurbished'
  },
  {
    id: 'samsung-tab-s9',
    name: 'Samsung Galaxy Tab S9',
    category: 'tablet',
    brand: 'Samsung',
    price: 64999,
    description: 'The definitive Android tablet experience with Dynamic AMOLED 2X.',
    specs: {
      display: '11-inch AMOLED 120Hz',
      processor: 'Snapdragon 8 Gen 2',
      ram: '8GB / 12GB',
      battery: '8,400 mAh',
      protection: 'IP68 Water/Dust'
    },
    condition: 'Open Box'
  },
  {
    id: 'sony-wh1000xm5',
    name: 'Sony WH-1000XM5 Wireless Headphones',
    category: 'headphone',
    brand: 'Sony',
    price: 24990,
    description: 'Industry-leading noise cancellation and exceptional sound quality.',
    specs: {
      type: 'Over-ear',
      battery: '30 hours',
      noise_cancelling: 'HD Noise Cancelling Processor QN1',
      connection: 'Bluetooth 5.2'
    },
    condition: 'Refurbished'
  },
  {
    id: 'logitech-mx-master-3s',
    name: 'Logitech MX Master 3S',
    category: 'accessory',
    brand: 'Logitech',
    price: 8995,
    description: 'The ultimate performance mouse, remastered for speed and precision.',
    specs: {
      sensor: '8K DPI Track-on-glass',
      buttons: '7 Buttons',
      scrolling: 'MagSpeed Electromagnetic',
      battery: 'USB-C Rechargeable'
    },
    condition: 'Open Box'
  }
];
