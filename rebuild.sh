#!/bin/bash
# EWaste Kochi — One-Command Full Rebuild
# Usage: ./rebuild.sh

set -e
DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$DIR"

echo "═══════════════════════════════════════════"
echo "  EWaste Kochi — SEO Powerhouse Rebuilder  "
echo "═══════════════════════════════════════════"

echo ""
echo "▶  Building 10 Ultra-Pillar pages..."
python3 build_10_pillars.py

echo ""
echo "▶  Regenerating sitemap.xml..."
python3 sitemap_generator.py

echo ""
echo "═══════════════════════════════════════════"
echo "  ✅ REBUILD COMPLETE"
echo "  📁 $(ls *.html | wc -l) HTML pages in root"
echo "  📁 $(ls blog/*.html 2>/dev/null | wc -l) blog pages"
echo "  🗺️  sitemap.xml updated"
echo "═══════════════════════════════════════════"
