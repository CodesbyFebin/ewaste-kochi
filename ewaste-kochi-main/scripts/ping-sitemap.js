// scripts/ping-sitemap.js
import https from 'https';

const sitemapUrl = 'https://ewastekochi.com/sitemap-index.xml';
const searchEngines = [
  `https://www.google.com/ping?sitemap=${encodeURIComponent(sitemapUrl)}`,
  `https://www.bing.com/ping?sitemap=${encodeURIComponent(sitemapUrl)}`,
];

console.log('🚀 Starting sitemap ping sequence...');

searchEngines.forEach((url) => {
  https.get(url, (res) => {
    console.log(`✅ Pinged ${url.split('?')[0]} – Status: ${res.statusCode}`);
  }).on('error', (err) => {
    console.error(`❌ Error pinging ${url}:`, err.message);
  });
});
