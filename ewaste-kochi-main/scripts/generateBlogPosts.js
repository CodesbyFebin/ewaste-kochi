#!/usr/bin/env node
// scripts/generateBlogPosts.js
// Run: node scripts/generateBlogPosts.js
// Generates src/data/blogPosts.json with 10,000 entries (100 per cluster × 100 clusters)

import { readFileSync, writeFileSync, existsSync } from 'fs';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const ROOT = join(__dirname, '..');

function loadJSON(rel) {
  return JSON.parse(readFileSync(join(ROOT, rel), 'utf8'));
}

const pillars = loadJSON('src/data/pillars.json');
const templates = loadJSON('src/data/contentTemplates.json');
const faqDb = loadJSON('src/data/faqDatabase.json');

// ─── Deterministic seeded hash (no random = no hydration mismatches) ──────────
function hash(str) {
  let h = 5381;
  for (let i = 0; i < str.length; i++) h = ((h << 5) + h) ^ str.charCodeAt(i);
  return Math.abs(h);
}
function pick(arr, seed) { return arr[seed % arr.length]; }
function pickN(arr, seed, n) {
  const out = [];
  for (let i = 0; i < n; i++) out.push(arr[(seed + i * 31) % arr.length]);
  return out;
}

// ─── Slug helpers ────────────────────────────────────────────────────────────
function slugify(str) {
  return str.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '');
}

// ─── Master cluster list: 10 pillars × 10 clusters = 100 clusters ─────────
const allClusters = [];
for (const pillar of pillars) {
  for (const cluster of pillar.clusters) {
    allClusters.push({ pillarSlug: pillar.slug, pillarName: pillar.name, ...cluster });
  }
}

// ─── Post title generators per cluster ────────────────────────────────────
const titlePatterns = [
  (kw, n) => `${kw}: Complete Guide for ${pick(templates.cities, n)} Businesses (2025)`,
  (kw, n) => `How to Choose the Best ${kw} Provider in ${pick(templates.cities, n+7)}`,
  (kw, n) => `${kw} in ${pick(templates.cities, n+3)}: Costs, Process & Certifications`,
  (kw, n) => `Why ${pick(templates.cities, n+2)} Companies Must Prioritise ${kw} Today`,
  (kw, n) => `${kw}: The ${pick(templates.cities, n+5)} Business Owner's Complete Checklist`,
  (kw, n) => `Top 10 Questions About ${kw} in ${pick(templates.cities, n+1)}, Answered`,
  (kw, n) => `${kw} Mistakes ${pick(templates.cities, n+4)} Companies Make and How to Fix Them`,
  (kw, n) => `The Legal Requirements for ${kw} in Kerala — ${pick(templates.years, n)} Update`,
  (kw, n) => `${kw}: What KSPCB Authorisation Actually Means for ${pick(templates.cities, n+6)} Clients`,
  (kw, n) => `${kw} in ${pick(templates.cities, n+8)}: From Pickup to Certificate`,
  (kw, n) => `Comparing ${kw} Providers in Kerala — What to Look For`,
  (kw, n) => `${kw}: Data Security Standards Every ${pick(templates.cities, n+9)} CISO Should Know`,
  (kw, n) => `How ${pick(templates.cities, n+11)} IT Managers Streamline ${kw}`,
  (kw, n) => `${kw} Compliance Under DPDP Act 2023 — A ${pick(templates.cities, n+12)} Guide`,
  (kw, n) => `The Environmental Impact of Proper ${kw} in Kerala`,
  (kw, n) => `${kw}: Understanding EPR Credits and Form-6 Filing`,
  (kw, n) => `How Hospitals in ${pick(templates.cities, n+13)} Handle ${kw} Securely`,
  (kw, n) => `${kw} for Banks and NBFCs — RBI Compliance Guide`,
  (kw, n) => `Schools and ${kw}: A Budget-Friendly Compliance Approach`,
  (kw, n) => `${kw}: The Circular Economy Story from ${pick(templates.cities, n+14)} to Recovery`,
];

// ─── Meta description templates ──────────────────────────────────────────────
const metaPatterns = [
  (kw, city) => `Complete guide to ${kw} in ${city}. Costs, compliance, KSPCB certification, and how to book free pickup. Updated for E-Waste Rules 2022.`,
  (kw, city) => `Learn everything about ${kw} in ${city}, Kerala. KSPCB compliance, data destruction certificates, costs, and same-day pickup options.`,
  (kw, city) => `Trusted ${kw} service in ${city}. Free doorstep collection, NIST 800-88 data wiping, Certificate of Destruction for every device.`,
  (kw, city) => `${kw} in ${city}: your comprehensive compliance checklist. KSPCB, EPR, DPDP Act, and RBI requirements explained simply.`,
  (kw, city) => `Why ${city} businesses choose EWaste Kochi for ${kw}. Same-day pickup, audit-ready docs, 4.9★ rated service across Ernakulam.`,
];

// ─── H1 templates ────────────────────────────────────────────────────────────
const h1Patterns = [
  (kw, city) => `${kw} in ${city} — Certified, Compliant & Free for Bulk Collections`,
  (kw, city) => `The Complete ${kw} Guide for ${city}, Kerala`,
  (kw, city) => `${kw} in ${city}: KSPCB Authorised, NIST Certified, Same-Day Pickup`,
  (kw, city) => `How to Handle ${kw} in ${city} — Step-by-Step Compliance Guide`,
  (kw, city) => `${kw} in ${city} — What Every Business Must Know in 2025`,
];

// ─── Generate 30 body paragraphs per post (deterministic from seed) ──────────
function generateContent(kw, city, area, seed) {
  const paragraphs = [];

  // Intro paragraph
  const introTpl = templates.intros[(seed) % templates.intros.length];
  paragraphs.push(introTpl
    .replace(/{city}/g, city)
    .replace(/{area}/g, area)
    .replace(/{keyword}/g, kw)
  );

  // Body paragraphs: pick 15 from templates, inject vars
  const bodyCount = 15;
  for (let i = 0; i < bodyCount; i++) {
    const tpl = templates.bodyParagraphs[(seed + i * 7) % templates.bodyParagraphs.length];
    paragraphs.push(tpl
      .replace(/{keyword}/g, kw)
      .replace(/{city}/g, city)
      .replace(/{area}/g, area)
      .replace(/{number}/g, pick(templates.numbers, seed + i))
      .replace(/{percentage}/g, pick(templates.percentages, seed + i + 3))
    );
  }

  // Section: Key Benefits
  paragraphs.push(`## Key Benefits of Certified ${kw} in ${city}`);
  for (const benefit of templates.benefits) {
    paragraphs.push(`- ${benefit}`);
  }

  // Section: Our Process
  paragraphs.push(`## Our ${kw} Process in ${city}`);
  for (const step of templates.processSteps) {
    paragraphs.push(`### ${step.step}\n${step.desc}`);
  }

  // Additional body to hit 3000+ words
  for (let i = 0; i < 8; i++) {
    const tpl = templates.bodyParagraphs[(seed + i * 13 + 5) % templates.bodyParagraphs.length];
    paragraphs.push(tpl
      .replace(/{keyword}/g, kw)
      .replace(/{city}/g, city)
      .replace(/{area}/g, area)
      .replace(/{number}/g, pick(templates.numbers, seed + i + 10))
      .replace(/{percentage}/g, pick(templates.percentages, seed + i + 7))
    );
  }

  return paragraphs.join('\n\n');
}

// ─── Select 15 FAQs per post from faqDatabase (deterministic) ────────────────
function selectFaqs(seed, topicTags) {
  // Filter FAQs that match the cluster tags, fall back to general if not enough
  const tagged = faqDb.filter(f => topicTags.some(t => f.tags && f.tags.includes(t)));
  const pool = tagged.length >= 15 ? tagged : [...tagged, ...faqDb.filter(f => !tagged.includes(f))];
  const selected = [];
  const used = new Set();
  let i = 0;
  while (selected.length < 15 && i < pool.length * 2) {
    const idx = (seed + i * 37) % pool.length;
    if (!used.has(idx)) { used.add(idx); selected.push(pool[idx]); }
    i++;
  }
  return selected;
}

// ─── Main generation loop: 10 pillars × 10 clusters × 100 posts = 10,000 ────
const blogPosts = [];
let postCounter = 0;

for (const pillar of pillars) {
  for (const cluster of pillar.clusters) {
    for (let postNum = 1; postNum <= 100; postNum++) {
      const seed = hash(`${pillar.slug}|${cluster.id}|${postNum}`);
      const city = pick(templates.cities, seed + postNum);
      const area = pick(templates.areas, seed + postNum + 3);
      const kw = cluster.keyword;
      const titleIdx = (seed + postNum) % titlePatterns.length;
      const title = titlePatterns[titleIdx](kw, seed + postNum);
      const metaDesc = metaPatterns[(seed + postNum) % metaPatterns.length](kw, city);
      const h1 = h1Patterns[(seed + postNum) % h1Patterns.length](kw, city);
      const postSlug = slugify(`${cluster.keyword}-${postNum}`);
      const topicTags = [cluster.id, pillar.slug, 'general'];
      const faqs = selectFaqs(seed + postNum * 7, topicTags);
      const content = generateContent(kw, city, area, seed + postNum);

      blogPosts.push({
        pillarSlug: pillar.slug,
        clusterSlug: cluster.id,
        slug: postSlug,
        title,
        metaDesc,
        h1,
        city,
        area,
        keyword: kw,
        content,
        faqs,
        dateModified: `2025-${String(((seed % 9) + 1)).padStart(2,'0')}-${String(((seed % 25) + 1)).padStart(2,'0')}`,
        wordCount: content.split(/\s+/).length,
      });

      postCounter++;
      if (postCounter % 500 === 0) {
        process.stdout.write(`\r  ✓ Generated ${postCounter}/10,000 posts...`);
      }
    }
  }
}

console.log(`\n\n✅ Generated ${blogPosts.length} blog posts`);

// Write output in 10 parts for LFS optimization and matching [slug].astro
const CHUNK_SIZE = 1000;
for (let i = 0; i < 10; i++) {
  const part = blogPosts.slice(i * CHUNK_SIZE, (i + 1) * CHUNK_SIZE);
  const partPath = join(ROOT, `src/data/blogPosts_part${i + 1}.json`);
  writeFileSync(partPath, JSON.stringify(part, null, 0));
}

console.log(`\n✅ Split ${blogPosts.length} posts into 10 JSON parts in src/data/`);

// Optionally write the main file too, but we should gitignore it
const outPath = join(ROOT, 'src/data/blogPosts.json');
writeFileSync(outPath, JSON.stringify(blogPosts, null, 0));
const fileSizeKB = Math.round(readFileSync(outPath).length / 1024);
console.log(`✅ Wrote master index ${outPath} (${fileSizeKB} KB)`);
console.log(`\n🚀 Run 'npm run build' to generate the 10,010+ page site.`);
