import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import tailwind from '@astrojs/tailwind';
import cloudflare from "@astrojs/cloudflare";

// https://astro.build/config
export default defineConfig({
  site: 'https://ewastekochi.com',
  output: 'static',
  adapter: cloudflare(),
  integrations: [
    sitemap({
      changefreq: 'weekly',
      priority: 0.7,
      lastmod: new Date(),
      customPages: [
        // Pillar pages get highest priority
        'https://ewastekochi.com/services/e-waste-recycling-kochi',
        'https://ewastekochi.com/services/itad-kochi',
        'https://ewastekochi.com/services/data-destruction-kochi',
        'https://ewastekochi.com/services/hard-drive-shredding-kochi',
        'https://ewastekochi.com/services/laptop-buyback-kochi',
        'https://ewastekochi.com/services/battery-recycling-kochi',
        'https://ewastekochi.com/services/server-recycling-kochi',
        'https://ewastekochi.com/services/mobile-recycling-kochi',
      ],
    }),
    tailwind({
      applyBaseStyles: false,
    }),
  ],
  build: {
    format: 'directory',
  },
  image: {
    service: {
      entrypoint: 'astro/assets/services/sharp',
    },
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'ewastekochi.com',
      },
    ],
  },
  vite: {
    build: {
      cssCodeSplit: true,
      rollupOptions: {
        output: {
          manualChunks: {
            'vendor': [],
          },
        },
      },
    },
  },
});
