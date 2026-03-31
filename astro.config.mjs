import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import tailwind from '@astrojs/tailwind';
import cloudflare from "@astrojs/cloudflare";

// https://astro.build/config
export default defineConfig({
  site: 'https://ewastekochi.in',
  output: 'server',
  adapter: cloudflare(),
  integrations: [
    sitemap({
      changefreq: 'weekly',
      priority: 0.7,
      lastmod: new Date(),
      customPages: [
        // Pillar pages get highest priority
        'https://ewastekochi.in/services/e-waste-recycling-kochi',
        'https://ewastekochi.in/services/itad-kochi',
        'https://ewastekochi.in/services/data-destruction-kochi',
        'https://ewastekochi.in/services/hard-drive-shredding-kochi',
        'https://ewastekochi.in/services/laptop-buyback-kochi',
        'https://ewastekochi.in/services/battery-recycling-kochi',
        'https://ewastekochi.in/services/server-recycling-kochi',
        'https://ewastekochi.in/services/mobile-recycling-kochi',
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
        hostname: 'ewastekochi.in',
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
