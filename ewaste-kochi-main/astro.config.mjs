import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import tailwind from '@astrojs/tailwind';
import vercel from '@astrojs/vercel';

// https://astro.build/config
export default defineConfig({
  site: 'https://ewastekochi.com',
  output: 'static',
  trailingSlash: 'always',
  redirects: {
    '/itad-kochi': '/itad',
    '/itad-kochi.html': '/itad',
    '/it-asset-inventory-audit.html': '/services/it-asset-inventory-audit',
    '/sell-old-phone-kochi.html': '/services/mobile-recycling-kochi',
    '/hard-drive-degaussing-kochi.html': '/services/hard-drive-degaussing-kochi',
  },
  adapter: vercel({
    webAnalytics: { enabled: true }
  }),
  integrations: [
    sitemap({
      filter: (page) => !page.includes('/admin') && !page.includes('/draft') && !page.includes('404'),
      serialize(item) {
        if (/https:\/\/ewastekochi\.com\/$/.test(item.url)) {
          item.changefreq = 'daily';
          item.priority = 1.0;
        } else if (item.url.includes('/locations/')) {
          item.changefreq = 'weekly';
          item.priority = 0.9;
        } else if (item.url.includes('/e-waste/') || item.url.includes('/itad/')) {
          item.changefreq = 'daily';
          item.priority = 0.8;
        } else if (item.url.includes('/blog/')) {
          item.changefreq = 'monthly';
          item.priority = 0.6;
        }
        return item;
      },
    }),
    tailwind({
      applyBaseStyles: false,
    }),
  ],
  build: {
    format: 'directory',
    // Increase concurrency limit for 10k+ pages
    concurrency: 4,
  },
  image: {
    service: {
      entrypoint: 'astro/assets/services/sharp',
    },
  },
  vite: {
    build: {
      cssCodeSplit: true,
      // Increase chunk size limit for large data files
      chunkSizeWarningLimit: 5000,
    },
    // Optimise dev server for large data imports
    optimizeDeps: {
      exclude: [],
    },
    // Increase JSON import memory limit
    server: {
      fs: { allow: ['..'] },
    },
  },
});
