#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generator voor de SEO-upgrade van lachgasbreda.nl, lachgasgroningen.nl, lachgasantwerpen.be en lachgasrotterdam.nl.

Gebruik: python3 build_sites.py <site> [--content pad.py]
Werkt in de repo-map van de site (in place). Nieuwe pagina's worden opgebouwd uit de bestaande
templates van de site zelf (header/footer/secties), zodat stijl en Tailwind-klassen gelijk blijven.
"""
import html
import importlib.util
import json
import os
import re
import sys

TODAY = "2026-10-02"
MONTH_NL = "oktober 2026"
IDX_KEY = {"breda": "4d2b8c6e1f9a4a7c9e3d5b1f8a2c6e4d", "groningen": "9f1e3c5a7b2d4e6f8a0c2e4b6d8f1a3c",
           "antwerpen": "2c4e6a8b0d1f3a5c7e9b1d3f5a7c9e2b", "rotterdam": "6b8d0f2a4c6e8a1c3e5b7d9f1a3c5e7b"}

SITES = {
    "breda": dict(repo="/home/user/lachgasbreda.nl", domain="https://lachgasbreda.nl", brand="Lachgas Breda", city="Breda",
                  kind="template", lang="nl-NL", hl="nl", area_dir="bezorggebied", area_tpl="bezorggebied/ginneken/index.html",
                  article_tpl="lachgas-informatie/veilig-gebruik/index.html", info_dir="lachgas-informatie", info_label="Lachgas Informatie",
                  geo=(51.5719, 4.7683), country="NL", region="Noord-Brabant", wa="31684453071", mail="info@lachgasbreda.nl"),
    "groningen": dict(repo="/home/user/lachgasgroningen.nl", domain="https://lachgasgroningen.nl", brand="Lachgas Groningen", city="Groningen",
                      kind="template", lang="nl-NL", hl="nl", area_dir="bezorggebied", area_tpl="bezorggebied/helpman/index.html",
                      article_tpl="lachgas-informatie/veilig-gebruik/index.html", info_dir="lachgas-informatie", info_label="Lachgas Informatie",
                      geo=(53.2194, 6.5665), country="NL", region="Groningen", wa="31684453071", mail="info@lachgasgroningen.nl"),
    "antwerpen": dict(repo="/home/user/lachgasantwerpen.be", domain="https://lachgasantwerpen.be", brand="Lachgas Antwerpen", city="Antwerpen",
                      kind="template", lang="nl-BE", hl="nl-BE", area_dir="bezorggebied", area_tpl="bezorggebied/berchem/index.html",
                      article_tpl="lachgas-informatie/veilig-gebruik/index.html", info_dir="lachgas-informatie", info_label="Lachgas Informatie",
                      geo=(51.2194, 4.4025), country="BE", region="Antwerpen", wa="31684453071", mail="info@lachgasantwerpen.be", theme="#111827"),
    "rotterdam": dict(repo="/home/user/lachgasrotterdam.nl", domain="https://lachgasrotterdam.nl", brand="Lachgas Rotterdam", city="Rotterdam",
                      kind="rotterdam", lang="nl-NL", hl="nl", area_dir="lachgas-bestellen", area_tpl="lachgas-bestellen/noord/index.html",
                      article_tpl="veilig-gebruik/index.html", info_dir="lachgas-informatie", info_label="Lachgas informatie",
                      geo=(51.9244, 4.4777), country="NL", region="Zuid-Holland", wa="31684453071", mail="info@lachgasrotterdam.nl"),
}

TITLE_FIX = {
    "rotterdam": {
        "lachgas-bestellen/hoek-van-holland/index.html": "Lachgas Hoek van Holland | Snel bezorgd via WhatsApp",
        "lachgas-bestellen/kralingen-crooswijk/index.html": "Lachgas Kralingen-Crooswijk | Snel bezorgd via WhatsApp",
        "lachgas-bestellen/prins-alexander/index.html": "Lachgas Prins Alexander | Snel bezorgd via WhatsApp",
        "lachgas-feest-evenement/index.html": "Lachgas voor feest of evenement Rotterdam | Op tijd bezorgd",
    }
}


def trim_desc(d):
    """Kort een meta description netjes in tot max 158 tekens, bij voorkeur op een zinsgrens."""
    t = html.unescape(d)
    if len(t) <= 160:
        return d
    cut = t[:158]
    k = max(cut.rfind(". "), cut.rfind("? "), cut.rfind("! "))
    if k >= 100:
        return esc(t[:k + 1])
    k = cut.rfind(", ")
    if k >= 100:
        return esc(t[:k] + ".")
    k = cut.rfind(" ")
    return esc(t[:k].rstrip(",;:") + ".")


CHIP = 'rounded-full border border-gray-200 bg-white px-5 py-2.5 text-sm font-semibold text-gray-700 transition hover:border-brand-300 hover:bg-brand-50 hover:text-brand-700'
CHIP_DARK = 'rounded-full bg-gray-900 px-5 py-2.5 text-sm font-semibold text-white transition hover:bg-gray-800'
LINK = 'font-semibold text-brand-600 hover:text-brand-700'
ARROW = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg>'
CHEVRON = '<svg class="shrink-0 text-gray-400 transition-transform group-open:rotate-180" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>'


def esc(s):
    return html.escape(s, quote=False).replace('"', "&quot;")


def rich(s):
    """Sta alleen <strong>, <em>, <a href> toe en voeg de huisstijl-klassen toe."""
    s = re.sub(r'<strong(?! class)>', '<strong class="text-gray-900">', s)
    s = re.sub(r'<a href="(/[^"]*)"(?! class)>', r'<a href="\1" class="%s">' % LINK, s)
    s = re.sub(r'<a href="(https?://[^"]*)"(?! class)>', r'<a href="\1" target="_blank" rel="noopener nofollow" class="%s">' % LINK, s)
    return s


def strip_tags(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s)).strip()


def read(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def write(p, s):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(s)


def load_content(path):
    spec = importlib.util.spec_from_file_location("content", path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


# ---------------------------------------------------------------------------
# Template helpers
# ---------------------------------------------------------------------------
def split_tpl(doc):
    i = doc.index("<main")
    i = doc.index(">", i) + 1
    j = doc.rindex("</main>")
    return doc[:i], doc[i:j], doc[j:]


def extract_section(main_html, marker):
    """Geef de <section>…</section> terug waarin `marker` voorkomt (geen geneste secties in deze templates)."""
    k = main_html.find(marker)
    if k < 0:
        raise ValueError("marker niet gevonden: " + marker)
    s = main_html.rfind("<section", 0, k)
    e = main_html.find("</section>", k) + len("</section>")
    return main_html[s:e]


def set_nav_active(doc, href):
    """Zet aria-current op het menu-item met `href` (desktop nav) en haal het van de rest af."""
    def deactivate(m):
        return '<a href="%s" class="rounded-lg px-4 py-2 text-sm font-medium text-gray-600 transition hover:bg-gray-50 hover:text-gray-900">' % m.group(1)
    doc = re.sub(r'<a href="([^"]+)" class="rounded-lg bg-gray-50 px-4 py-2 text-sm font-medium text-gray-900" aria-current="page">', deactivate, doc)
    if href:
        doc = doc.replace('<a href="%s" class="rounded-lg px-4 py-2 text-sm font-medium text-gray-600 transition hover:bg-gray-50 hover:text-gray-900">' % href,
                          '<a href="%s" class="rounded-lg bg-gray-50 px-4 py-2 text-sm font-medium text-gray-900" aria-current="page">' % href, 1)
    return doc


def set_head(head, site, title, desc, path, schemas, og_type="website"):
    url = site["domain"] + path
    head = re.sub(r"<title>.*?</title>", "<title>%s</title>" % esc(title), head, flags=re.S)
    head = re.sub(r'<meta name="description" content="[^"]*"/?>', '<meta name="description" content="%s"/>' % esc(desc), head)
    head = re.sub(r'<link rel="canonical" href="[^"]*"/?>', '<link rel="canonical" href="%s"/>' % url, head)
    head = re.sub(r'<meta property="og:url" content="[^"]*"/?>', '<meta property="og:url" content="%s"/>' % url, head)
    head = re.sub(r'<meta property="og:type" content="[^"]*"/?>', '<meta property="og:type" content="%s"/>' % og_type, head)
    for prop in ("og:title", "twitter:title"):
        head = re.sub(r'<meta (?:property|name)="%s" content="[^"]*"/?>' % prop,
                      lambda m: m.group(0).split(' content=')[0] + ' content="%s"/>' % esc(title), head)
    for prop in ("og:description", "twitter:description"):
        head = re.sub(r'<meta (?:property|name)="%s" content="[^"]*"/?>' % prop,
                      lambda m: m.group(0).split(' content=')[0] + ' content="%s"/>' % esc(desc), head)
    head = re.sub(r'<link rel="alternate" hreflang="[^"]*" href="[^"]*"/?>\n?', "", head)
    head = re.sub(r'<script type="application/ld\+json">.*?</script>\n?', "", head, flags=re.S)
    extra = ""
    for sc in schemas:
        extra += '<script type="application/ld+json">%s</script>\n' % json.dumps(sc, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    head = head.replace("</head>", extra + "</head>")
    return head


# ---------------------------------------------------------------------------
# Schema helpers
# ---------------------------------------------------------------------------
def crumbs_schema(site, items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": site["domain"] + h} for i, (n, h) in enumerate(items)]}


def faq_schema(items):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": strip_tags(q), "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}} for q, a in items]}


def service_schema(site, a, path):
    return {"@context": "https://schema.org", "@type": "Service", "serviceType": "Lachgas bezorgservice",
            "name": "Lachgas bezorgen in %s" % a["name"], "description": a["description"], "url": site["domain"] + path,
            "provider": {"@type": "LocalBusiness", "name": site["brand"], "url": site["domain"] + "/", "telephone": "+" + site["wa"]},
            "areaServed": {"@type": "Place", "name": a["name"], "geo": {"@type": "GeoCoordinates", "latitude": a["lat"], "longitude": a["lon"]}}}


def article_schema(site, art, path):
    return {"@context": "https://schema.org", "@type": "Article", "headline": art["h1"], "description": art["description"],
            "url": site["domain"] + path, "mainEntityOfPage": site["domain"] + path, "inLanguage": site["lang"],
            "datePublished": TODAY, "dateModified": TODAY,
            "author": {"@type": "Organization", "name": site["brand"], "url": site["domain"] + "/"},
            "publisher": {"@type": "Organization", "name": site["brand"], "url": site["domain"] + "/"}}


def webpage_schema(site, title, desc, path):
    return {"@context": "https://schema.org", "@type": "WebPage", "name": title, "description": desc, "url": site["domain"] + path,
            "inLanguage": site["lang"], "dateModified": TODAY, "isPartOf": {"@type": "WebSite", "name": site["brand"], "url": site["domain"] + "/"}}


# ---------------------------------------------------------------------------
# Blocks
# ---------------------------------------------------------------------------
def hero(crumbs, badge, h1, lead):
    parts = []
    for i, (name, href) in enumerate(crumbs):
        if i:
            parts.append('<span aria-hidden="true">/</span>')
        if href:
            parts.append('<a href="%s" class="hover:text-white/70">%s</a>' % (href, esc(name)))
        else:
            parts.append('<span class="text-white/70" aria-current="page">%s</span>' % esc(name))
    return ('<section class="relative overflow-hidden bg-gray-900 pt-28 pb-16 lg:pt-36 lg:pb-20">\n'
            '    <div class="absolute -top-10 -right-10 h-72 w-72 rounded-full bg-brand-600/20 blur-[100px]"></div>\n'
            '    <div class="relative mx-auto max-w-4xl px-4 text-center sm:px-6 lg:px-8">\n'
            '      <nav aria-label="Kruimelpad" class="mb-6 flex flex-wrap items-center justify-center gap-1.5 text-xs text-white/40">\n        %s\n      </nav>\n'
            '      <span class="mb-4 inline-block rounded-full bg-white/10 px-4 py-1.5 text-xs font-bold uppercase tracking-wide text-white">%s</span>\n'
            '      <h1 class="mb-4 font-heading text-4xl font-extrabold text-white sm:text-5xl">%s</h1>\n'
            '      <p class="mx-auto max-w-2xl text-white/60">%s</p>\n    </div>\n  </section>\n'
            % ("\n        ".join(parts), esc(badge), esc(h1), rich(lead)))


def faq_block(items, title="Veelgestelde vragen", intro=None, alt=True, h2_level="h2"):
    out = ['<section class="%spx-4 py-16 sm:px-6 md:py-20 lg:px-8 lg:py-24">\n    <div class="mx-auto max-w-3xl">\n' % ("bg-surface-50 " if alt else "")]
    out.append('      <div class="mb-10 text-center">\n        <span class="mb-4 inline-block rounded-full bg-gray-900 px-4 py-1.5 text-xs font-bold uppercase tracking-wide text-white">FAQ</span>\n'
               '        <%s class="font-heading text-3xl font-bold sm:text-4xl">%s</%s>\n' % (h2_level, esc(title), h2_level))
    if intro:
        out.append('        <p class="mt-4 text-gray-500">%s</p>\n' % rich(intro))
    out.append('      </div>\n      <div class="space-y-3">\n')
    for i, (q, a) in enumerate(items):
        out.append('        <details class="group rounded-xl border border-gray-100 bg-white overflow-hidden transition-shadow hover:shadow-sm"%s>\n'
                   '          <summary class="flex w-full cursor-pointer items-center justify-between px-6 py-5 text-left">\n'
                   '            <span class="pr-4 text-base font-semibold text-gray-900">%s</span>\n            %s\n          </summary>\n'
                   '          <div class="px-6 pb-5 text-sm text-gray-500 leading-relaxed">%s</div>\n        </details>\n'
                   % (" open" if i == 0 else "", esc(q), CHEVRON, rich(a)))
    out.append('      </div>\n    </div>\n  </section>\n')
    return "".join(out)


def chips_section(title, badge, links, alt=True, intro=None):
    chips = "\n        ".join('<a href="%s" class="%s">%s</a>' % (h, CHIP, esc(t)) for h, t in links)
    return ('<section class="%spx-4 py-16 sm:px-6 md:py-20 lg:px-8 lg:py-24">\n    <div class="mx-auto max-w-4xl text-center">\n'
            '      <span class="mb-4 inline-block rounded-full bg-gray-900 px-4 py-1.5 text-xs font-bold uppercase tracking-wide text-white">%s</span>\n'
            '      <h2 class="mb-%s font-heading text-3xl font-bold sm:text-4xl">%s</h2>\n%s'
            '      <div class="flex flex-wrap justify-center gap-3">\n        %s\n      </div>\n    </div>\n  </section>\n'
            % ("bg-surface-50 " if alt else "", esc(badge), "4" if intro else "6", esc(title),
               ('      <p class="mb-8 text-gray-500">%s</p>\n' % rich(intro)) if intro else "", chips))


def article_body(sections, note, updated=MONTH_NL):
    out = ['<section class="px-4 py-16 sm:px-6 md:py-20 lg:px-8 lg:py-24">\n    <div class="mx-auto max-w-3xl">\n'
           '      <p class="mb-8 text-sm text-gray-400">Laatst bijgewerkt: %s</p>\n' % updated]
    for i, sec in enumerate(sections):
        out.append('      <h2 class="mb-4%s font-heading text-2xl font-bold sm:text-3xl">%s</h2>\n' % ("" if i == 0 else " mt-10", esc(sec["h2"])))
        for p in sec.get("paragraphs", []):
            out.append('      <p class="mb-4 text-gray-600 leading-relaxed">%s</p>\n' % rich(p))
        if sec.get("bullets"):
            out.append('      <ul class="mb-6 space-y-2 text-gray-600">\n')
            for b in sec["bullets"]:
                out.append('        <li class="flex gap-3"><span class="mt-1 h-1.5 w-1.5 shrink-0 rounded-full bg-brand-600"></span><span>%s</span></li>\n' % rich(b))
            out.append('      </ul>\n')
    if note:
        out.append('      <div class="mt-10 rounded-2xl border border-gray-100 bg-surface-50 p-6">\n'
                   '        <p class="text-sm text-gray-500 leading-relaxed"><strong class="text-gray-900">Let op:</strong> %s</p>\n      </div>\n' % rich(note))
    out.append('    </div>\n  </section>\n')
    return "".join(out)


def card(href, title, text, cta="Lees meer", icon_svg=None):
    icon = icon_svg or '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>'
    return ('        <a href="%s" class="group flex flex-col rounded-2xl border border-gray-100 bg-white p-6 transition-all duration-300 hover:shadow-card hover:border-gray-200 hover:-translate-y-1">\n'
            '          <div class="mb-4 flex h-14 w-14 items-center justify-center rounded-2xl bg-gray-900 text-white transition-colors group-hover:bg-brand-600">%s</div>\n'
            '          <h2 class="mb-2 text-lg font-bold group-hover:text-brand-600">%s</h2>\n'
            '          <p class="mb-4 flex-1 text-sm text-gray-500">%s</p>\n'
            '          <div class="flex items-center gap-1 text-sm font-semibold group-hover:text-brand-600">%s %s</div>\n        </a>\n'
            % (href, icon, esc(title), esc(text), esc(cta), ARROW))


# ---------------------------------------------------------------------------
# Page builders
# ---------------------------------------------------------------------------
class Builder:
    def __init__(self, key, content):
        self.key = key
        self.site = SITES[key]
        self.c = content
        self.repo = self.site["repo"]
        self.area_doc = read(os.path.join(self.repo, self.site["area_tpl"]))
        self.art_doc = read(os.path.join(self.repo, self.site["article_tpl"]))
        self.head, area_main, self.tail = split_tpl(self.area_doc)
        self.sec_waarom = extract_section(area_main, ">Waarom wij<")
        self.sec_products = extract_section(area_main, "Lachgastanks in drie formaten")
        self.sec_cta = extract_section(area_main, "Klaar om te bestellen?")
        m = re.search(r"<h1[^>]*>(.*?)</h1>", self.area_doc, re.S)
        self.tpl_area_name = re.sub(r"^Lachgas (Rotterdam )?", "", strip_tags(m.group(1)))
        self.area_overview = "/bezorggebied/" if self.site["kind"] == "template" else "/bezorggebieden/"
        self.area_label = "Bezorggebied" if self.site["kind"] == "template" else "Bezorggebieden"
        self.new_pages = []  # (path, title, description)
        self.existing_areas = sorted(d for d in os.listdir(os.path.join(self.repo, self.site["area_dir"]))
                                     if os.path.isdir(os.path.join(self.repo, self.site["area_dir"], d)))
        self.area_names = {}
        for slug in self.existing_areas:
            doc = read(os.path.join(self.repo, self.site["area_dir"], slug, "index.html"))
            m = re.search(r'<h1[^>]*>(.*?)</h1>', doc, re.S)
            name = strip_tags(m.group(1))
            name = re.sub(r"^Lachgas (Rotterdam )?", "", name)
            self.area_names[slug] = name
        for a in content.AREAS:
            self.area_names[a["slug"]] = a["name"]

    def doc(self, title, desc, path, schemas, main_html, nav_href, og_type="website"):
        head = set_head(self.head, self.site, title, desc, path, schemas, og_type)
        d = head + "\n" + main_html + self.tail
        return set_nav_active(d, nav_href)

    # -- bezorggebied -------------------------------------------------------
    def area_page(self, a):
        s = self.site
        path = "/%s/%s/" % (s["area_dir"], a["slug"])
        name = a["name"]
        crumbs = [("Home", "/"), (self.area_label, self.area_overview), (name, None)]
        def localize(block):
            return re.sub(r"\b%s\b" % re.escape(self.tpl_area_name), esc(name), block)
        waarom = re.sub(r'(Snelle levering</h3>\s*<p class="text-sm text-gray-500">)[^<]*(</p>)',
                        lambda m: m.group(1) + esc("In %s %s." % (name, a["levertijd"])) + m.group(2), localize(self.sec_waarom))
        products = localize(self.sec_products)
        cta = localize(self.sec_cta)
        intro = ['      <p class="text-gray-600 leading-relaxed mb-4">%s</p>\n' % rich(p) for p in a["intro"]]
        intro.append('      <p class="text-gray-600 leading-relaxed"><strong class="text-gray-900">%s in %s:</strong> %s.</p>\n'
                     % ("Wijken en plekken" if a.get("kind") in ("wijk", "district") else "Buurten en plekken", esc(name), esc(a["wijken"].rstrip("."))))
        intro_sec = ('<section class="px-4 py-16 sm:px-6 md:py-20 lg:px-8 lg:py-24">\n    <div class="mx-auto max-w-4xl">\n%s    </div>\n  </section>\n' % "".join(intro))
        near = []
        for slug in a["nearby"]:
            if slug in self.area_names:
                near.append(("/%s/%s/" % (s["area_dir"], slug), self.area_names[slug]))
        near.append((self.area_overview, "Bekijk volledig bezorggebied"))
        nearby = chips_section("Wij bezorgen ook hier", "Ook actief in de buurt", near, alt=True)
        main = ("\n  " + hero(crumbs, "Bezorggebied", a["h1"], a["lead"]) + "  " + intro_sec + "  " + waarom + "\n  "
                + faq_block(a["faq"], "Veelgestelde vragen over lachgas in %s" % name, alt=False) + "  " + products + "\n  "
                + nearby + "  " + cta + "\n")
        schemas = [crumbs_schema(s, [("Home", "/"), (self.area_label, self.area_overview), (name, path)]), service_schema(s, a, path), faq_schema(a["faq"])]
        d = self.doc(a["title"], a["description"], path, schemas, main, self.area_overview)
        write(os.path.join(self.repo, path.strip("/"), "index.html"), d)
        self.new_pages.append((path, a["title"], a["description"]))

    # -- artikel / servicepagina ------------------------------------------
    def article_page(self, art, base_dir, crumb_parent, nav_href, service=False):
        s = self.site
        path = "/%s%s/" % ((base_dir + "/") if base_dir else "", art["slug"])
        crumbs = [("Home", "/")] + ([crumb_parent] if crumb_parent else []) + [(art["h1"], None)]
        related = []
        for slug in art.get("related", []):
            href = "/%s/%s/" % (s["info_dir"], slug)
            if os.path.exists(os.path.join(self.repo, s["info_dir"], slug, "index.html")) or any(x["slug"] == slug for x in self.c.ARTICLES):
                t = self.article_title(slug)
                related.append((href, t))
            elif os.path.exists(os.path.join(self.repo, slug, "index.html")):
                related.append(("/%s/" % slug, self.article_title(slug, root=True)))
        if s["kind"] == "rotterdam":
            related.append(("/veilig-gebruik/", "Veilig gebruik"))
        related.append(("/%s/" % s["info_dir"], "Alle informatie"))
        main = "\n  " + hero(crumbs, art["label"], art["h1"], art["lead"]) + "  " + article_body(art["sections"], art.get("note"))
        if service and art.get("faq"):
            main += "  " + faq_block(art["faq"], "Veelgestelde vragen", alt=True)
        main += "  " + chips_section("Verder lezen", "Meer weten", related, alt=not (service and art.get("faq"))) + "  " + self.sec_cta + "\n"
        schemas = [crumbs_schema(s, [("Home", "/")] + ([crumb_parent] if crumb_parent else []) + [(art["h1"], path)])]
        if service:
            schemas.append({"@context": "https://schema.org", "@type": "Service", "name": art["h1"], "description": art["description"],
                            "url": s["domain"] + path, "serviceType": "Lachgas bezorgservice",
                            "provider": {"@type": "LocalBusiness", "name": s["brand"], "url": s["domain"] + "/"},
                            "areaServed": {"@type": "City", "name": s["city"]}})
            if art.get("faq"):
                schemas.append(faq_schema(art["faq"]))
        else:
            schemas.append(article_schema(s, art, path))
        d = self.doc(art["title"], art["description"], path, schemas, main, nav_href, og_type="article" if not service else "website")
        write(os.path.join(self.repo, path.strip("/"), "index.html"), d)
        self.new_pages.append((path, art["title"], art["description"]))

    def article_title(self, slug, root=False):
        for x in self.c.ARTICLES:
            if x["slug"] == slug:
                return x["h1"]
        for x in getattr(self.c, "SERVICE_PAGES", []):
            if x["slug"] == slug:
                return x["h1"]
        p = os.path.join(self.repo, slug if root else os.path.join(self.site["info_dir"], slug), "index.html")
        m = re.search(r"<h1[^>]*>(.*?)</h1>", read(p), re.S)
        return strip_tags(m.group(1))

    # -- FAQ-pagina (template sites) --------------------------------------
    def faq_page(self):
        s = self.site
        F = self.c.FAQ
        path = "/veelgestelde-vragen/"
        main = "\n  " + hero([("Home", "/"), ("Veelgestelde vragen", None)], "FAQ", F["h1"], F["lead"])
        for i, g in enumerate(F["groups"]):
            main += "  " + faq_block(g["items"], g["h2"], alt=(i % 2 == 0))
        main += "  " + self.sec_cta + "\n"
        all_items = [it for g in F["groups"] for it in g["items"]]
        schemas = [crumbs_schema(s, [("Home", "/"), ("Veelgestelde vragen", path)]), faq_schema(all_items), webpage_schema(s, F["title"], F["description"], path)]
        d = self.doc(F["title"], F["description"], path, schemas, main, None)
        write(os.path.join(self.repo, "veelgestelde-vragen", "index.html"), d)
        self.new_pages.append((path, F["title"], F["description"]))

    # -- Rotterdam: informatie-hub ----------------------------------------
    def hub_page(self):
        s = self.site
        H = self.c.HUB
        path = "/%s/" % s["info_dir"]
        cards = "".join(card("/%s/%s/" % (s["info_dir"], a["slug"]), a["h1"], a["description"]) for a in self.c.ARTICLES)
        cards += card("/veilig-gebruik/", "Veilig gebruik van lachgas", "De basisregels voor verantwoord gebruik: nooit uit de tank, niet in het verkeer, niet combineren en altijd 18+.")
        intro = "".join('      <p class="text-gray-600 leading-relaxed mb-4">%s</p>\n' % rich(p) for p in H["intro"])
        main = ("\n  " + hero([("Home", "/"), (H["h1"], None)], "Informatie", H["h1"], H["lead"])
                + '  <section class="px-4 py-16 sm:px-6 md:py-20 lg:px-8 lg:py-24">\n    <div class="mx-auto max-w-4xl">\n%s    </div>\n'
                  '    <div class="mx-auto mt-10 max-w-5xl">\n      <div class="grid gap-4 sm:grid-cols-2">\n%s      </div>\n    </div>\n  </section>\n' % (intro, cards)
                + "  " + self.sec_cta + "\n")
        schemas = [crumbs_schema(s, [("Home", "/"), (H["h1"], path)]), webpage_schema(s, H["title"], H["description"], path)]
        d = self.doc(H["title"], H["description"], path, schemas, main, None)
        write(os.path.join(self.repo, s["info_dir"], "index.html"), d)
        self.new_pages.append((path, H["title"], H["description"]))

    # -- bestaande pagina's bijwerken -------------------------------------
    def update_existing(self):
        s = self.site
        new_areas = self.c.AREAS
        # 1. homepage + overzicht: chips voor nieuwe gebieden
        for rel in ("index.html", s["area_dir"].replace("lachgas-bestellen", "bezorggebieden") + "/index.html"):
            p = os.path.join(self.repo, rel)
            if not os.path.exists(p):
                continue
            d = read(p)
            last_links = re.findall(r'<a href="/%s/[a-z0-9-]+/" class="%s">[^<]*</a>' % (s["area_dir"], re.escape(CHIP)), d)
            last_dark = re.findall(r'<a href="/%s/[a-z0-9-]+/" class="%s">[^<]*</a>' % (s["area_dir"], re.escape(CHIP_DARK)), d)
            towns = [a for a in new_areas if a.get("kind") in ("stad", "dorp", "gemeente")]
            wijken = [a for a in new_areas if a.get("kind") in ("wijk", "district")]
            if last_dark and towns:
                add = "\n        ".join('<a href="/%s/%s/" class="%s">%s</a>' % (s["area_dir"], a["slug"], CHIP_DARK, esc(a["name"])) for a in towns)
                d = d.replace(last_dark[-1], last_dark[-1] + "\n        " + add, 1)
                rest = wijken
            else:
                rest = new_areas
            if last_links and rest:
                add = "\n        ".join('<a href="/%s/%s/" class="%s">%s</a>' % (s["area_dir"], a["slug"], CHIP, esc(a["name"])) for a in rest)
                d = d.replace(last_links[-1], last_links[-1] + "\n        " + add, 1)
            # Rotterdam: ook kaarten op de overzichtspagina
            if rel.startswith("bezorggebieden"):
                cards = re.findall(r'        <a href="/lachgas-bestellen/[a-z-]+/" class="group flex flex-col.*?</a>\n', d, re.S)
                if cards:
                    tpl = cards[-1]
                    add = ""
                    for a in new_areas:
                        c = re.sub(r'href="/lachgas-bestellen/[a-z-]+/"', 'href="/lachgas-bestellen/%s/"' % a["slug"], tpl, 1)
                        c = re.sub(r'(<h3[^>]*>)[^<]*(</h3>)', lambda m: m.group(1) + esc("Lachgas " + a["name"]) + m.group(2), c, 1)
                        c = re.sub(r'(<p class="mb-4 flex-1 text-sm text-gray-500">)[^<]*(</p>)', lambda m: m.group(1) + esc(a["lead"]) + m.group(2), c, 1)
                        c = re.sub(r'(group-hover:text-brand-600">)Lachgas bestellen in [^<]*(<svg)', lambda m: m.group(1) + esc("Lachgas bestellen in " + a["name"] + " ") + m.group(2), c, 1)
                        add += c
                    d = d.replace(tpl, tpl + add, 1)
            write(p, d)
        # 2. informatie-overzicht (template sites): kaarten voor nieuwe artikelen
        if s["kind"] == "template":
            p = os.path.join(self.repo, s["info_dir"], "index.html")
            d = read(p)
            cards = re.findall(r'        <a href="/lachgas-informatie/[a-z0-9-]+/" class="group flex flex-col.*?</a>\n', d, re.S)
            tpl = cards[-1]
            add = ""
            for a in self.c.ARTICLES:
                c = re.sub(r'href="/lachgas-informatie/[a-z0-9-]+/"', 'href="/lachgas-informatie/%s/"' % a["slug"], tpl, 1)
                c = re.sub(r'(<h2[^>]*>)[^<]*(</h2>)', lambda m: m.group(1) + esc(a["h1"]) + m.group(2), c, 1)
                c = re.sub(r'(<p class="mb-4 flex-1 text-sm text-gray-500">)[^<]*(</p>)', lambda m: m.group(1) + esc(a["description"]) + m.group(2), c, 1)
                add += c
            d = d.replace(tpl, tpl + add, 1)
            write(p, d)
        # 3. LocalBusiness-schema op de homepage: areaServed uitbreiden (+ Antwerpen: telefoon, geo, id)
        p = os.path.join(self.repo, "index.html")
        d = read(p)
        def fix_lb(m):
            data = json.loads(m.group(1))
            if data.get("@type") != "LocalBusiness":
                return m.group(0)
            served = data.get("areaServed", [])
            if served and isinstance(served[0], str):
                for a in new_areas:
                    if a["name"] not in served:
                        served.append(a["name"])
            else:
                names = {x.get("name") for x in served if isinstance(x, dict)}
                for a in new_areas:
                    if a["name"] not in names:
                        served.append({"@type": "City" if a.get("kind") in ("stad", "gemeente") else "AdministrativeArea", "name": a["name"]})
            data["areaServed"] = served
            data.setdefault("@id", s["domain"] + "/#business")
            data.setdefault("telephone", "+" + s["wa"])
            data.setdefault("geo", {"@type": "GeoCoordinates", "latitude": s["geo"][0], "longitude": s["geo"][1]})
            data.setdefault("image", None)
            if not data["image"]:
                og = re.search(r'<meta property="og:image" content="([^"]+)"', d)
                data["image"] = og.group(1) if og else s["domain"] + "/favicon.svg"
            data.setdefault("priceRange", "€€")
            return '<script type="application/ld+json">%s</script>' % json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
        d = re.sub(r'<script type="application/ld\+json">(\{.*?\})</script>', fix_lb, d, count=1, flags=re.S)
        write(p, d)

    def footer_links(self, doc):
        """Voeg links naar nieuwe pagina's toe in de footerkolom 'Info & bezorging'."""
        s = self.site
        if s["kind"] == "template":
            anchor = '<li><a href="/bezorggebied/" class="hover:text-white">Bezorggebied</a></li>'
            add = ('\n        <li><a href="/veelgestelde-vragen/" class="hover:text-white">Veelgestelde vragen</a></li>'
                   '\n        <li><a href="/lachgas-nachtbezorging/" class="hover:text-white">Lachgas &rsquo;s avonds en &rsquo;s nachts</a></li>'
                   '\n        <li><a href="/lachgas-feest-evenement/" class="hover:text-white">Feest &amp; evenement</a></li>')
        else:
            anchor = '<li><a href="/veilig-gebruik/" class="hover:text-white">Veilig gebruik</a></li>'
            add = '\n        <li><a href="/lachgas-informatie/" class="hover:text-white">Lachgas informatie</a></li>'
        if anchor in doc and add.strip() not in doc:
            doc = doc.replace(anchor, anchor + add, 1)
        return doc

    # -- technische upgrade op elke pagina --------------------------------
    def upgrade_all(self):
        s = self.site
        css = read(os.path.join(self.repo, "css/tailwind.css")).strip() + "\n" + re.sub(r"/\*.*?\*/", "", read(os.path.join(self.repo, "css/site.css")), flags=re.S).strip()
        css = re.sub(r"\s+", " ", css).strip()
        for root, dirs, files in os.walk(self.repo):
            if ".git" in root:
                continue
            for f in files:
                if not f.endswith(".html"):
                    continue
                p = os.path.join(root, f)
                d = read(p)
                o = d
                # inline CSS i.p.v. twee render-blokkerende stylesheets
                d = re.sub(r'<link rel="stylesheet" href="/css/tailwind\.css"/?>\s*<link rel="stylesheet" href="/css/site\.css"/?>', lambda m: "<style>%s</style>" % css, d)
                # Google Fonts asynchroon laden
                d = re.sub(r'<link href="(https://fonts\.googleapis\.com/css2\?[^"]+)" rel="stylesheet"/?>',
                           lambda m: '<link rel="preload" as="style" href="%s" onload="this.onload=null;this.rel=\'stylesheet\'"/>\n<noscript><link rel="stylesheet" href="%s"/></noscript>' % (m.group(1), m.group(1)), d)
                # hreflang
                m = re.search(r'<link rel="canonical" href="([^"]+)"/?>', d)
                if m and "noindex" not in d and 'hreflang=' not in d:
                    u = m.group(1)
                    d = d.replace(m.group(0), m.group(0) + '\n<link rel="alternate" hreflang="%s" href="%s"/>\n<link rel="alternate" hreflang="x-default" href="%s"/>' % (s["hl"], u, u), 1)
                # favicons / manifest / theme-color
                d = re.sub(r'<link rel="icon" href="/favicon\.ico" sizes="32x32"/?>', '<link rel="icon" href="/favicon.ico" sizes="32x32 48x48"/>', d)
                if '<link rel="manifest"' not in d:
                    d = d.replace('<link rel="apple-touch-icon" href="/apple-touch-icon.png"/>', '<link rel="apple-touch-icon" href="/apple-touch-icon.png"/>\n<link rel="manifest" href="/manifest.webmanifest"/>', 1)
                if '<meta name="theme-color"' not in d and s.get("theme"):
                    d = d.replace('<link rel="icon" href="/favicon.svg"', '<meta name="theme-color" content="%s"/>\n<link rel="icon" href="/favicon.svg"' % s["theme"], 1)
                # horizontale overflow door decoratieve cirkel in de paginakop (mobiel): overflow-hidden
                d = d.replace('<section class="relative bg-gray-900 pt-28 pb-16 lg:pt-36 lg:pb-20">', '<section class="relative overflow-hidden bg-gray-900 pt-28 pb-16 lg:pt-36 lg:pb-20">')
                # te lange titels/descriptions inkorten (bestaande pagina's)
                rel = os.path.relpath(p, self.repo).replace(os.sep, "/")
                if rel in TITLE_FIX.get(self.key, {}):
                    nt = TITLE_FIX[self.key][rel]
                    d = re.sub(r"<title>.*?</title>", "<title>%s</title>" % esc(nt), d, flags=re.S)
                    d = re.sub(r'(<meta (?:property|name)="(?:og|twitter):title" content=")[^"]*(")', lambda m: m.group(1) + esc(nt) + m.group(2), d)
                dm = re.search(r'<meta name="description" content="([^"]*)"', d)
                if dm and len(html.unescape(dm.group(1))) > 160:
                    nd = trim_desc(dm.group(1))
                    d = d.replace('content="%s"' % dm.group(1), 'content="%s"' % nd)
                # scripts uitgesteld
                d = d.replace('<script src="/js/site.js"></script>', '<script src="/js/site.js" defer></script>')
                # hero-afbeelding met hoge prioriteit + preload (homepage)
                hm = re.search(r'<img src="(/[^"]*hero[^"]*\.webp)"[^>]*>', d)
                if hm and f == "index.html" and root.rstrip("/") == self.repo.rstrip("/"):
                    tag = hm.group(0)
                    if "fetchpriority" not in tag:
                        new = tag.replace("<img ", '<img fetchpriority="high" ', 1).replace(' loading="lazy"', "")
                        d = d.replace(tag, new, 1)
                    if 'rel="preload" as="image"' not in d:
                        d = d.replace("</head>", '<link rel="preload" as="image" href="%s" type="image/webp" fetchpriority="high"/>\n</head>' % hm.group(1), 1)
                d = self.footer_links(d)
                if d != o:
                    write(p, d)

    # -- sitemap, llms, indexnow, manifest --------------------------------
    def finish(self):
        s = self.site
        pages = []
        for root, dirs, files in os.walk(self.repo):
            if ".git" in root:
                continue
            for f in files:
                if f.endswith(".html") and f != "404.html":
                    rel = os.path.relpath(os.path.join(root, f), self.repo).replace(os.sep, "/")
                    d = read(os.path.join(root, f))
                    if "noindex" in d:
                        continue
                    path = "/" if rel == "index.html" else "/" + rel[:-len("index.html")] if rel.endswith("/index.html") else "/" + rel
                    t = re.search(r"<title>(.*?)</title>", d, re.S)
                    ds = re.search(r'name="description" content="([^"]*)"', d)
                    pages.append((path, strip_tags(t.group(1)) if t else path, html.unescape(ds.group(1)) if ds else "", d))
        pages.sort(key=lambda x: (x[0] != "/", x[0].count("/"), x[0]))
        def prio(p):
            if p == "/": return "1.0"
            if p.count("/") == 2 and p.strip("/") in ("assortiment", "bezorggebied", "bezorggebieden", "lachgas-tanks", "lachgas-informatie"): return "0.9"
            if p.startswith(("/product/", "/bezorggebied/", "/lachgas-bestellen/")): return "0.8"
            if p.strip("/") in ("privacy", "algemene-voorwaarden", "voorwaarden", "sitemap"): return "0.3"
            return "0.7"
        sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
        for path, t, ds, d in pages:
            sm.append("  <url><loc>%s%s</loc><lastmod>%s</lastmod><changefreq>%s</changefreq><priority>%s</priority></url>"
                      % (s["domain"], path, TODAY, "weekly" if prio(path) >= "0.8" else "monthly", prio(path)))
        sm.append("</urlset>")
        write(os.path.join(self.repo, "sitemap.xml"), "\n".join(sm) + "\n")
        # llms.txt + llms-full.txt
        lines = ["# %s" % s["brand"], "", "> %s: lachgas bestellen in %s en omgeving, snel en discreet bezorgd via WhatsApp (+%s). Uitsluitend voor volwassenen (18+)." % (s["brand"], s["city"], s["wa"]),
                 "", "Volledige tekst van alle pagina's: %s/llms-full.txt" % s["domain"], "", "## Pagina's"]
        full = ["# %s - volledige inhoud" % s["brand"], "", "WhatsApp: +%s | E-mail: %s" % (s["wa"], s["mail"]), ""]
        for path, t, ds, d in pages:
            lines.append("- [%s](%s%s): %s" % (t, s["domain"], path, ds))
            body = re.sub(r"<(script|style|nav|header|footer)\b.*?</\1>", "", d, flags=re.S)
            body = re.sub(r"</(p|li|h1|h2|h3|dd|dt|tr|div|section|article|summary)>", "\n", body)
            txt = re.sub(r"[ \t]+", " ", strip_tags(body))
            txt = re.sub(r"\n\s*\n+", "\n", txt).strip()
            full += ["---", "", "## " + t, "URL: " + s["domain"] + path, "", txt, ""]
        lines += ["", "## Contact", "- WhatsApp: +%s" % s["wa"], "- E-mail: %s" % s["mail"], ""]
        write(os.path.join(self.repo, "llms.txt"), "\n".join(lines))
        write(os.path.join(self.repo, "llms-full.txt"), "\n".join(full))
        key = IDX_KEY[self.key]
        write(os.path.join(self.repo, key + ".txt"), key)
        # manifest (Antwerpen had er geen)
        mp = os.path.join(self.repo, "manifest.webmanifest")
        if not os.path.exists(mp):
            write(mp, json.dumps({"name": s["brand"], "short_name": s["brand"], "description": "%s: lachgas bestellen en snel aan huis bezorgd via WhatsApp." % s["brand"],
                                  "id": "/", "start_url": "/", "scope": "/", "display": "standalone", "background_color": "#ffffff",
                                  "theme_color": s.get("theme", "#111827"), "lang": "nl",
                                  "icons": [{"src": "/icon-192.png", "sizes": "192x192", "type": "image/png"}, {"src": "/icon-512.png", "sizes": "512x512", "type": "image/png"}]}, indent=2) + "\n")
        return pages


def main():
    key = sys.argv[1]
    cpath = sys.argv[sys.argv.index("--content") + 1] if "--content" in sys.argv else None
    content = load_content(cpath)
    if os.environ.get("SITE_REPO"):
        SITES[key]["repo"] = os.environ["SITE_REPO"]
    b = Builder(key, content)
    for a in content.AREAS:
        b.area_page(a)
    s = b.site
    if s["kind"] == "template":
        for art in content.ARTICLES:
            b.article_page(art, s["info_dir"], (s["info_label"], "/%s/" % s["info_dir"]), "/%s/" % s["info_dir"])
        for sp in content.SERVICE_PAGES:
            b.article_page(sp, "", None, None, service=True)
        b.faq_page()
    else:
        for art in content.ARTICLES:
            b.article_page(art, s["info_dir"], (content.HUB["h1"], "/%s/" % s["info_dir"]), None)
        b.hub_page()
    b.update_existing()
    b.upgrade_all()
    pages = b.finish()
    print("%s: %d nieuwe pagina's, %d pagina's in sitemap" % (key, len(b.new_pages), len(pages)))
    for p in b.new_pages:
        print("  ", p[0])


if __name__ == "__main__":
    main()
