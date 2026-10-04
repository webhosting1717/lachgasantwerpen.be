#!/bin/bash
# Bouwt alle sites opnieuw vanaf een schone checkout (fase 3) en draait de controles.
# Gebruik: gen/build_all.sh [breda groningen antwerpen rotterdam brabant]
set -e
SP="$(cd "$(dirname "$0")/.." && pwd)"
declare -A REPO=( [breda]=/home/user/lachgasbreda.nl [groningen]=/home/user/lachgasgroningen.nl [antwerpen]=/home/user/lachgasantwerpen.be [rotterdam]=/home/user/lachgasrotterdam.nl )
for site in "$@"; do
  echo "################ $site"
  if [ "$site" = "brabant" ]; then
    OUT=/home/user/lachgasbrabant.nl
    mkdir -p "$OUT/_build" "$OUT/assets"
    cp "$SP"/brabant/_build/{common.py,pages.py,build.py,site.css,fonts.css} "$OUT/_build/"
    rm -rf "$OUT/_build/content" && mkdir -p "$OUT/_build/content" && cp "$SP"/content/brabant/*.py "$OUT/_build/content/" && rm -f "$OUT/_build/content/_config.py"
    cp "$SP"/brabant/assets/{icon-512.png,icon-192.png,apple-touch-icon.png,og-lachgas-brabant.png} "$OUT/assets/" && cp "$SP"/brabant/assets/favicon.ico "$OUT/"
    (cd "$OUT" && python3 _build/build.py)
    python3 "$SP/gen/validate.py" "$OUT" | tail -3
    python3 "$SP/seo_audit.py" "$OUT" | head -8
  else
    R="${REPO[$site]}"
    (cd "$R" && git checkout -q . && git clean -fdq && git status --short | wc -l)
    (cd "$SP" && python3 gen/phase3.py "$site" | tail -3)
    python3 "$SP/gen/validate.py" "$R" | tail -3
    python3 "$SP/seo_audit.py" "$R" | head -8
  fi
done
