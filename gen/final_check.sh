#!/bin/bash
# Eindcontrole per repo: validator, SEO-audit, duplicatie, aantallen
cd "$(dirname "$0")/.."
for r in "$@"; do
  echo "################ $r"
  python3 gen/validate.py "$r" | tail -3
  python3 seo_audit.py "$r" 2>&1 | head -12
  echo "sitemap-urls: $(grep -c '<loc>' $r/sitemap.xml)  html: $(find $r -name '*.html' -not -path '*/.git/*' | wc -l)  speculationrules: $(grep -l speculationrules -r $r --include=*.html | wc -l)  googleapis-css: $(grep -l 'fonts.googleapis.com/css' -r $r --include=*.html | wc -l)"
done
echo "################ duplicatie"
python3 dup.py "$@" | head -8
