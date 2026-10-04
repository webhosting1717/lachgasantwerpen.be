#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Performance-upgrade voor de statische Tailwind-sites (idempotent).
- Google Fonts: geen aparte CSS-request meer; @font-face (latin/latin-ext) inline, fontbestanden rechtstreeks van fonts.gstatic.com.
- Speculation Rules: prerender van interne links bij hover/touch (Chrome/Edge/Android), waardoor paginawissels vrijwel direct zijn.
- Afbeeldingen: decoding="async", lazy loading onder de vouw, width/height aanwezig.
- HTML: inspringing en commentaar verwijderd (kleinere overdracht), zonder zichtbare wijzigingen.
Gebruik: python3 perf_upgrade.py <repo> [<repo> ...]
"""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
FONT_CSS = open(os.path.join(os.path.dirname(HERE), "fonts", "inline-fonts.css"), encoding="utf-8").read().strip()
SPEC = ('<script type="speculationrules">{"prerender":[{"where":{"and":[{"href_matches":"/*"},{"not":{"href_matches":"/*\\\\?*"}},'
        '{"not":{"selector_matches":"[rel~=nofollow]"}}]},"eagerness":"moderate"}]}</script>')
FONT_RE = re.compile(r'<link rel="preconnect" href="https://fonts\.googleapis\.com"/?>\s*<link rel="preconnect" href="https://fonts\.gstatic\.com" crossorigin/?>\s*'
                     r'<link rel="preload" as="style" href="https://fonts\.googleapis\.com/css2\?[^"]+" onload="[^"]*"/?>\s*'
                     r'<noscript><link rel="stylesheet" href="https://fonts\.googleapis\.com/css2\?[^"]+"/?></noscript>\s*', re.S)
FONT_RE2 = re.compile(r'<link rel="preconnect" href="https://fonts\.googleapis\.com"/?>\s*<link rel="preconnect" href="https://fonts\.gstatic\.com" crossorigin/?>\s*'
                      r'<link href="https://fonts\.googleapis\.com/css2\?[^"]+" rel="stylesheet"/?>\s*', re.S)

def upgrade_html(d, is_home):
    o = d
    # 1. fonts: alle Google-Fonts-CSS-verwijzingen weg, preconnect naar gstatic behouden/toevoegen
    d = re.sub(r'[ \t]*<link rel="preconnect" href="https://fonts\.googleapis\.com"/?>\s*\n?', "", d)
    d = re.sub(r'[ \t]*<link rel="preload" as="style" href="https://fonts\.googleapis\.com/css2\?[^"]+"[^>]*>\s*\n?', "", d)
    d = re.sub(r'[ \t]*<noscript><link rel="stylesheet" href="https://fonts\.googleapis\.com/css2\?[^"]+"/?></noscript>\s*\n?', "", d)
    d = re.sub(r'[ \t]*<link href="https://fonts\.googleapis\.com/css2\?[^"]+" rel="stylesheet"/?>\s*\n?', "", d)
    d = re.sub(r'[ \t]*<link rel="stylesheet" href="https://fonts\.googleapis\.com/css2\?[^"]+"/?>\s*\n?', "", d)
    if 'rel="preconnect" href="https://fonts.gstatic.com"' not in d:
        d = d.replace("<style>", '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>\n<style>', 1)
    if "@font-face" not in d:
        d = d.replace("<style>", "<style>" + FONT_CSS, 1)
    # 2. speculation rules (voor </head>)
    if 'type="speculationrules"' not in d:
        d = d.replace("</head>", SPEC + "\n</head>", 1)
    # 3. afbeeldingen
    def img(mm):
        tag = mm.group(0)
        if 'decoding=' not in tag:
            tag = tag.replace("<img ", '<img decoding="async" ', 1)
        if 'loading=' not in tag and 'fetchpriority="high"' not in tag:
            tag = tag.replace("<img ", '<img loading="lazy" ', 1)
        return tag
    d = re.sub(r"<img\b[^>]*>", img, d)
    # 4. inspringing en commentaar
    d = re.sub(r"<!--(?!\[if).*?-->", "", d, flags=re.S)
    d = re.sub(r"\n[ \t]+", "\n", d)
    d = re.sub(r"\n{2,}", "\n", d)
    return d

def main_repo(repo):
    main_list([repo])


def main():
    main_list(sys.argv[1:])


def main_list(repos):
    for repo in repos:
        n = 0; before = after = 0
        for root, dirs, files in os.walk(repo):
            if ".git" in root: continue
            for f in files:
                if not f.endswith(".html"): continue
                p = os.path.join(root, f)
                d = open(p, encoding="utf-8").read()
                nd = upgrade_html(d, f == "index.html" and root.rstrip("/") == repo.rstrip("/"))
                before += len(d.encode()); after += len(nd.encode())
                if nd != d:
                    open(p, "w", encoding="utf-8").write(nd); n += 1
        print("%s: %d bestanden aangepast, HTML %dKB -> %dKB" % (os.path.basename(repo), n, before // 1024, after // 1024))

if __name__ == "__main__":
    main()
