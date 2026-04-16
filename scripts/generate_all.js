import { mkdirSync, writeFileSync } from 'node:fs';
import { resolve } from 'node:path';
import {
  blogLibraryCategories,
  blogLibraryPosts,
  blogLibraryStats,
} from '../src/data/programmaticBlogEngine.js';

const outDir = resolve(process.cwd(), 'public', 'seo');
mkdirSync(outDir, { recursive: true });

const manifest = {
  generatedAt: new Date().toISOString(),
  stats: blogLibraryStats,
  categories: blogLibraryCategories.map((category) => ({
    slug: category.slug,
    name: category.name,
    pageContext: category.pageContext,
    articleCount: category.articleCount,
    shortTailKeywords: category.shortTailKeywords,
    serviceLinks: category.serviceLinks,
  })),
  samplePosts: blogLibraryPosts.slice(0, 20).map((post) => ({
    title: post.title,
    keyword: post.keyword,
    categorySlug: post.categorySlug,
    slug: post.slug,
    canonical: post.canonical,
    primaryService: post.primaryService.slug,
  })),
};

const csvHeader = ['category', 'cluster', 'location', 'keyword', 'url', 'primary_service'];
const csvRows = blogLibraryPosts.map((post) =>
  [
    post.categorySlug,
    post.clusterLabel,
    post.location.titleLabel,
    post.keyword,
    post.canonical,
    post.primaryService.slug,
  ]
    .map((value) => `"${String(value).replace(/"/g, '""')}"`)
    .join(','),
);

writeFileSync(resolve(outDir, 'blog-library-manifest.json'), JSON.stringify(manifest, null, 2));
writeFileSync(resolve(outDir, 'blog-library-keywords.csv'), `${csvHeader.join(',')}\n${csvRows.join('\n')}\n`);

console.log(`Generated ${blogLibraryStats.posts} programmatic blog records across ${blogLibraryStats.categories} categories.`);
console.log(`Manifest: ${resolve(outDir, 'blog-library-manifest.json')}`);
console.log(`CSV: ${resolve(outDir, 'blog-library-keywords.csv')}`);
