// src/utils/slugify.ts
export function slugify(input: string): string {
  return input
    .toLowerCase()
    .normalize('NFKD') // decompose accented characters
    .replace(/[\u0300-\u036f]/g, '') // remove diacritics
    .replace(/[^a-z0-9]+/g, '-') // replace non-alphanumeric with hyphens
    .replace(/^-+|-+$/g, ''); // trim leading/trailing hyphens
}
