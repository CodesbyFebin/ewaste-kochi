// src/utils/dataLoader.ts
import { locations as rawLocations } from '../data/locations';
import { services as rawServices } from '../data/services';
import { industries as rawIndustries } from '../data/industries';
import { compliance as rawCompliance } from '../data/compliance';
import { trading as rawTrading } from '../data/trading';
import { slugify } from './slugify';

// ─── Types ────────────────────────────────────────────────────────────────────
export interface Location {
  slug: string;
  name: string;
  displayName?: string;
  district?: string;
  description?: string;
  heroHeadline?: string;
  heroSubline?: string;
  localKeywords?: string[];
  seo_title: string;
  meta_desc: string;
  h1: string;
  lat?: number;
  lng?: number;
}

export interface Service {
  slug: string;
  name: string;
  shortName?: string;
  category?: string;
  isPillar?: boolean;
  tagline?: string;
  description?: string;
  longDescription?: string;
  keywords?: string[];
  metaTitle?: string;
  metaDescription?: string;
  price?: string;
  priceCurrency?: string;
  badges?: string[];
  relatedServices?: string[];
  schemaType?: string;
  faqs?: Array<{ q: string; a: string }>;
}

export interface Industry {
  slug: string;
  name: string;
  shortName?: string;
  icon?: string;
  description?: string;
  heroHeadline?: string;
  heroSubline?: string;
  metaTitle?: string;
  metaDescription?: string;
  challenges?: string[];
  solutions?: string[];
  faqs?: Array<{ q: string; a: string }>;
  seo_title?: string;
  meta_desc?: string;
  h1?: string;
}

export interface Compliance {
  slug: string;
  name: string;
  shortName?: string;
  icon?: string;
  description?: string;
  heroHeadline?: string;
  heroSubline?: string;
  metaTitle?: string;
  metaDescription?: string;
  keyPoints?: string[];
  faqs?: Array<{ q: string; a: string }>;
  seo_title?: string;
  meta_desc?: string;
  h1?: string;
}

export interface Trading {
  slug: string;
  name: string;
  shortName?: string;
  icon?: string;
  description?: string;
  heroHeadline?: string;
  heroSubline?: string;
  metaTitle?: string;
  metaDescription?: string;
  priceRange?: string;
  categories?: string[];
  certifications?: string[];
  longDescription?: string;
  faqs?: Array<{ q: string; a: string }>;
  seo_title?: string;
  meta_desc?: string;
  h1?: string;
}

// ─── Loaders ──────────────────────────────────────────────────────────────────

export async function getLocations(): Promise<Location[]> {
  return (rawLocations as any[]).map((loc) => {
    const baseName = loc.displayName || loc.name || '';
    const slug = loc.slug || slugify(baseName);

    const seo_title =
      loc.metaTitle || `E‑Waste Recycling in ${baseName} | EWaste Kochi`;
    const meta_desc =
      loc.metaDescription ||
      loc.description ||
      `Doorstep e‑waste pickup and secure IT asset disposal in ${baseName}. Free pickup, data destruction certificates, KSPCB authorised.`;
    const h1 = loc.heroHeadline || `E‑Waste Recycling & ITAD in ${baseName}`;

    return {
      slug,
      name: loc.name || baseName,
      displayName: loc.displayName,
      district: loc.district,
      description: loc.description,
      heroHeadline: loc.heroHeadline,
      heroSubline: loc.heroSubline,
      localKeywords: loc.localKeywords,
      seo_title,
      meta_desc,
      h1,
      lat: loc.lat,
      lng: loc.lng,
    };
  });
}

export async function getServices(): Promise<Service[]> {
  return rawServices.map((svc) => ({
    ...svc,
    seo_title: svc.metaTitle || `${svc.name} | EWaste Kochi`,
    meta_desc: svc.metaDescription || svc.description || `Professional ${svc.name} in Kochi, Kerala.`,
    h1: svc.tagline || svc.name,
  }));
}

export async function getIndustries(): Promise<Industry[]> {
  return rawIndustries.map((ind) => ({
    ...ind,
    seo_title: ind.metaTitle || `${ind.name} E-Waste Services | EWaste Kochi`,
    meta_desc: ind.metaDescription || ind.description || `Certified e-waste services for the ${ind.name} sector in Kerala.`,
    h1: ind.heroHeadline || ind.name,
  }));
}

export async function getCompliance(): Promise<Compliance[]> {
  return rawCompliance.map((comp) => ({
    ...comp,
    seo_title: comp.metaTitle || `${comp.name} | EWaste Kochi Compliance`,
    meta_desc: comp.metaDescription || comp.description || `Guide to ${comp.name} for Kerala businesses.`,
    h1: comp.heroHeadline || comp.name,
  }));
}

export async function getTrading(): Promise<Trading[]> {
  return rawTrading.map((tr) => ({
    ...tr,
    seo_title: tr.metaTitle || `${tr.name} | EWaste Kochi Marketplace`,
    meta_desc: tr.metaDescription || tr.description || `${tr.name} from EWaste Kochi's ITAD programme.`,
    h1: tr.heroHeadline || tr.name,
  }));
}
