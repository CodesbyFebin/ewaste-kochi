#!/bin/bash
SOURCE_DIR="/media/hp-ml10/Projects/ewastekochi-production/ewastekochi"
DEST_DIR="/media/hp-ml10/Projects/ewastekochi-production/ewaste-kochi-main"

echo "Organizing and migrating files..."

# Move Python scripts to scripts/
mkdir -p "$DEST_DIR/scripts"
find "$SOURCE_DIR" -maxdepth 1 -name "*.py" -exec cp {} "$DEST_DIR/scripts/" \;

# Move CSV/JSON data files to data/
mkdir -p "$DEST_DIR/data"
find "$SOURCE_DIR" -maxdepth 1 \( -name "*.csv" -o -name "*.json" \) -exec cp {} "$DEST_DIR/data/" \;

# Move HTML files to legacy_html_backup/ instead of public/ (Astro will handle routes)
LEGACY_HTML_DIR="$DEST_DIR/legacy_html_backup"
mkdir -p "$LEGACY_HTML_DIR"
find "$SOURCE_DIR" -maxdepth 1 -name "*.html" -exec cp {} "$LEGACY_HTML_DIR/" \;

# Move XML files (like sitemaps) into public/
find "$SOURCE_DIR" -maxdepth 1 -name "*.xml" -exec cp {} "$DEST_DIR/public/" \;

# Move .txt files to public/ (like robots.txt, url lists)
find "$SOURCE_DIR" -maxdepth 1 -name "*.txt" -exec cp {} "$DEST_DIR/public/" \;

# Directories to move to public/ (exclude known python caches, etc)
DIRS_TO_PUBLIC=("assets" "blog" "buyback" "collection" "comparisons" "compliance" "css" "data-security" "disposal" "general-waste" "guides" "images" "industries" "itad" "js" "locations" "media" "proof" "recycling" "resources" "services" "trading" "img")

for dir in "${DIRS_TO_PUBLIC[@]}"; do
    if [ -d "$SOURCE_DIR/$dir" ]; then
        cp -r "$SOURCE_DIR/$dir" "$DEST_DIR/public/"
    fi
done

echo "Migrated files successfully."
