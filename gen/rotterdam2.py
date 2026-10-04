#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fase 2 voor lachgasrotterdam.nl: regio-uitbreiding Zuid-Holland, wijkpagina's, extra artikelen en servicepagina's,
regio-overzicht, sterkere homepage (regio, vergelijking, extra FAQ), bijgewerkt bezorggebieden-overzicht, footer en HTML-sitemap.
Gebruik: python3 rotterdam2.py   (optioneel SITE_REPO=/pad/naar/kopie)
"""
import html
import importlib.util
import json
import os
import re
import sys
import types

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_sites as B  # noqa: E402

CONTENT = os.environ.get("R2_CONTENT", os.path.join(os.path.dirname(HERE), "content"))


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def content():
    a = load(os.path.join(CONTENT, "r2", "areas_a.py"), "ra")
    b = load(os.path.join(CONTENT, "r2", "areas_b.py"), "rb")
    c = load(os.path.join(CONTENT, "r2", "areas_c.py"), "rc")
    art = load(os.path.join(CONTENT, "r2", "articles.py"), "rart")
    old = load(os.path.join(CONTENT, "rotterdam.py"), "rold")
    ns = types.SimpleNamespace()
    ns.AREAS = list(a.AREAS) + list(b.AREAS) + list(c.AREAS)
    ns.ARTICLES = list(art.ARTICLES)
    ns.SERVICE_PAGES = list(art.SERVICE_PAGES)
    ns.HUB = old.HUB
    ns.REGIO = c.REGIO
    ns.HOME = c.HOME
    ns.OLD_AREAS = list(old.AREAS)
    return ns


ROTTERDAM_GEBIEDEN = ["centrum", "noord", "kralingen-crooswijk", "delfshaven", "feijenoord", "ijsselmonde", "charlois", "prins-alexander",
                      "hillegersberg-schiebroek", "overschie", "hoogvliet", "hoek-van-holland"]
REGIO_PATH = "/lachgas-bestellen/zuid-holland/"


class R2(B.Builder):
    def __init__(self, c):
        super().__init__("rotterdam", c)
        self.wijken = [a for a in c.AREAS if a.get("kind") == "wijk"]
        self.towns = [a for a in c.AREAS if a.get("kind") != "wijk"]
        self.old_towns = c.OLD_AREAS  # schiedam ... berkel-en-rodenrijs (al aanwezig)

    # gebiedspagina: label "Wijken en plekken" voor steden/gemeenten, "Buurten en plekken" voor dorpen/wijken
    def area_page(self, a):
        super().area_page(a)
        p = os.path.join(self.repo, self.site["area_dir"], a["slug"], "index.html")
        d = B.read(p)
        want = "Wijken en plekken" if a.get("kind") in ("stad", "gemeente") else "Buurten en plekken"
        d = re.sub(r'<strong class="text-gray-900">(Wijken en plekken|Buurten en plekken) in ', '<strong class="text-gray-900">%s in ' % want, d, count=1)
        # link naar het regio-overzicht in de "ook in de buurt"-sectie
        d = d.replace('<a href="/bezorggebieden/" class="%s">Bekijk volledig bezorggebied</a>' % B.CHIP,
                      '<a href="%s" class="%s">Heel Zuid-Holland</a>\n        <a href="/bezorggebieden/" class="%s">Bekijk volledig bezorggebied</a>' % (REGIO_PATH, B.CHIP, B.CHIP), 1)
        B.write(p, d)

    # informatie-hub: kaarten voor bestaande + nieuwe artikelen
    def hub_page(self):
        s = self.site
        H = self.c.HUB
        path = "/%s/" % s["info_dir"]
        existing = []
        for slug in sorted(os.listdir(os.path.join(self.repo, s["info_dir"]))):
            p = os.path.join(self.repo, s["info_dir"], slug, "index.html")
            if os.path.isdir(os.path.dirname(p)) and os.path.exists(p) and not any(x["slug"] == slug for x in self.c.ARTICLES):
                d = B.read(p)
                h1 = B.strip_tags(re.search(r"<h1[^>]*>(.*?)</h1>", d, re.S).group(1))
                ds = html.unescape(re.search(r'name="description" content="([^"]*)"', d).group(1))
                existing.append((slug, h1, ds))
        order = ["wat-is-lachgas", "is-lachgas-legaal-in-nederland", "lachgas-en-vitamine-b12", "lachgas-bijwerkingen-en-eerste-hulp", "lachgas-en-alcohol",
                 "lachgas-in-het-verkeer", "lachgas-tank-bewaren-en-vervoeren", "lachgastank-2kg-4kg-of-10kg", "lachgas-bezorgservice-kiezen",
                 "lachgas-en-het-milieu", "lachgas-afkicken-en-hulp"]
        items = {slug: (h1, ds) for slug, h1, ds in existing}
        for a in self.c.ARTICLES:
            items[a["slug"]] = (a["h1"], a["description"])
        slugs = [x for x in order if x in items] + [x for x in items if x not in order]
        cards = "".join(B.card("/%s/%s/" % (s["info_dir"], sl), items[sl][0], items[sl][1]) for sl in slugs)
        cards += B.card("/veilig-gebruik/", "Veilig gebruik van lachgas", "De basisregels voor verantwoord gebruik: nooit uit de tank, niet in het verkeer, niet combineren en altijd 18+.")
        intro = "".join('      <p class="text-gray-600 leading-relaxed mb-4">%s</p>\n' % B.rich(p) for p in H["intro"])
        if "lachgas-en-alcohol" in items and "lachgas-bijwerkingen-en-eerste-hulp" in items:
            intro += ('      <p class="text-gray-600 leading-relaxed mb-4">Nieuw zijn de artikelen over <a href="/lachgas-informatie/lachgas-en-alcohol/" class="%s">lachgas en alcohol</a>, '
                      '<a href="/lachgas-informatie/lachgas-bijwerkingen-en-eerste-hulp/" class="%s">bijwerkingen en eerste hulp</a>, de keuze tussen een 2KG, 4KG of 10KG tank, '
                      'het milieu, hulp bij problematisch gebruik en waar je op let bij het kiezen van een bezorgservice.</p>\n' % (B.LINK, B.LINK))
        main = ("\n  " + B.hero([("Home", "/"), (H["h1"], None)], "Informatie", H["h1"], H["lead"])
                + '  <section class="px-4 py-16 sm:px-6 md:py-20 lg:px-8 lg:py-24">\n    <div class="mx-auto max-w-4xl">\n%s    </div>\n'
                  '    <div class="mx-auto mt-10 max-w-5xl">\n      <div class="grid gap-4 sm:grid-cols-2">\n%s      </div>\n    </div>\n  </section>\n' % (intro, cards)
                + "  " + self.sec_cta + "\n")
        schemas = [B.crumbs_schema(s, [("Home", "/"), (H["h1"], path)]), B.webpage_schema(s, H["title"], H["description"], path),
                   {"@context": "https://schema.org", "@type": "ItemList", "name": H["h1"], "itemListOrder": "https://schema.org/ItemListUnordered",
                    "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": s["domain"] + "/%s/%s/" % (s["info_dir"], sl), "name": items[sl][0]} for i, sl in enumerate(slugs)]}]
        d = self.doc(H["title"], H["description"], path, schemas, main, None)
        B.write(os.path.join(self.repo, s["info_dir"], "index.html"), d)
        self.new_pages.append((path, H["title"], H["description"]))

    # regio-overzicht Zuid-Holland
    def regio_page(self):
        s = self.site
        R = self.c.REGIO
        path = REGIO_PATH
        crumbs = [("Home", "/"), ("Bezorggebieden", "/bezorggebieden/"), (R["h1"], None)]
        intro = "".join('      <p class="text-gray-600 leading-relaxed mb-4">%s</p>\n' % B.rich(p) for p in R["intro"])
        groups = ""
        for i, g in enumerate(R["groups"]):
            links = [("/lachgas-bestellen/%s/" % sl, self.area_names[sl]) for sl in g["slugs"] if sl in self.area_names]
            chips = "\n          ".join('<a href="%s" class="%s">%s</a>' % (h, B.CHIP if i % 2 else B.CHIP_DARK, B.esc(t)) for h, t in links)
            groups += ('      <div class="%s">\n        <h2 class="mb-2 font-heading text-2xl font-bold sm:text-3xl">%s</h2>\n        <p class="mb-6 text-gray-500">%s</p>\n'
                       '        <div class="flex flex-wrap gap-3">\n          %s\n        </div>\n      </div>\n'
                       % ("mb-12" if i < len(R["groups"]) - 1 else "", B.esc(g["h2"]), B.rich(g["text"]), chips))
        main = ("\n  " + B.hero(crumbs, "Regio", R["h1"], R["lead"])
                + '  <section class="px-4 py-16 sm:px-6 md:py-20 lg:px-8 lg:py-24">\n    <div class="mx-auto max-w-4xl">\n%s    </div>\n  </section>\n' % intro
                + '  <section class="bg-surface-50 px-4 py-16 sm:px-6 md:py-20 lg:px-8 lg:py-24">\n    <div class="mx-auto max-w-4xl">\n%s    </div>\n  </section>\n' % groups
                + "  " + self.sec_waarom.replace("In %s meestal" % self.tpl_area_name, "In de regio meestal").replace(self.tpl_area_name, "de regio") + "\n  "
                + B.faq_block(R["faq"], "Veelgestelde vragen over bezorgen in de regio", alt=False) + "  " + self.sec_cta.replace(self.tpl_area_name, "Zuid-Holland") + "\n")
        served = [{"@type": "City", "name": self.area_names[sl]} for g in R["groups"] for sl in g["slugs"] if sl in self.area_names]
        schemas = [B.crumbs_schema(s, [("Home", "/"), ("Bezorggebieden", "/bezorggebieden/"), (R["h1"], path)]),
                   {"@context": "https://schema.org", "@type": "Service", "name": R["h1"], "description": R["description"], "url": s["domain"] + path,
                    "serviceType": "Lachgas bezorgservice", "provider": {"@type": "LocalBusiness", "name": s["brand"], "url": s["domain"] + "/", "@id": s["domain"] + "/#business"},
                    "areaServed": [{"@type": "AdministrativeArea", "name": "Zuid-Holland"}] + served},
                   B.faq_schema(R["faq"])]
        d = self.doc(R["title"], R["description"], path, schemas, main, "/bezorggebieden/")
        B.write(os.path.join(self.repo, path.strip("/"), "index.html"), d)
        self.new_pages.append((path, R["title"], R["description"]))

    # homepage + overzicht + LocalBusiness
    def update_existing(self):
        s = self.site
        H = self.c.HOME
        all_towns = self.old_towns + self.towns
        # ---- homepage ----
        p = os.path.join(self.repo, "index.html")
        d = B.read(p)
        d = d.replace("24/7 actief in heel Rotterdam\n", "24/7 actief in Rotterdam en de regio\n", 1)
        d = d.replace("Dag en nacht, van Centrum tot Hoek van Holland.", "Dag en nacht, van Centrum tot Hoek van Holland, en in ruim 25 plaatsen in de regio: van Westland tot Dordrecht, Delft, Zoetermeer en Gouda.", 1)
        d = d.replace('<p class="font-heading text-sm font-bold text-gray-900">Heel Rotterdam</p>\n        <p class="text-xs text-gray-400">12 gebieden, alle wijken</p>',
                      '<p class="font-heading text-sm font-bold text-gray-900">Rotterdam en regio</p>\n        <p class="text-xs text-gray-400">Ruim 40 gebieden en plaatsen</p>', 1)
        # bestaande chips-sectie: alleen Rotterdamse gebieden + wijken; regio-chips verhuizen naar eigen sectie
        for a in self.old_towns:
            d = re.sub(r'\n\s*<a href="/lachgas-bestellen/%s/" class="%s">[^<]*</a>' % (a["slug"], re.escape(B.CHIP)), "", d, count=1)
        last = re.findall(r'<a href="/lachgas-bestellen/[a-z0-9-]+/" class="%s">[^<]*</a>' % re.escape(B.CHIP), d)[-1]
        add = "\n        ".join('<a href="/lachgas-bestellen/%s/" class="%s">%s</a>' % (a["slug"], B.CHIP, B.esc(a["name"])) for a in self.wijken)
        d = d.replace(last, last + "\n        " + add, 1)
        d = d.replace("Aan beide kanten van de Maas, van de Kop van Zuid tot Hillegersberg en van Hoek van Holland tot Nesselande. Klik op je gebied voor de lokale details.",
                      "Aan beide kanten van de Maas: alle twaalf stadsgebieden en populaire wijken als Nesselande, Kop van Zuid en Blijdorp. Klik op je gebied voor wijken, bezorgtijden en lokale details.", 1)
        # regio-sectie na de chips-sectie (voor de sectie met 3 stappen)
        regio_links = [("/lachgas-bestellen/%s/" % a["slug"], a["name"]) for a in all_towns]
        regio = B.chips_section(H["regio_h2"], H["regio_badge"], regio_links, alt=True, intro=H["regio_text"])
        regio = regio.replace('      </div>\n    </div>\n  </section>\n',
                              '      </div>\n      <div class="mt-10 text-center">\n        <a href="%s" class="inline-flex items-center gap-1 text-sm font-bold text-brand-600 hover:text-brand-700">Bekijk het volledige bezorggebied in Zuid-Holland %s</a>\n      </div>\n    </div>\n  </section>\n' % (REGIO_PATH, B.ARROW), 1)
        marker = '  <section class="bg-surface-50 px-4 py-16 sm:px-6 md:py-20 lg:px-8 lg:py-24">\n    <div class="mx-auto max-w-6xl">\n      <div class="mx-auto mb-12 max-w-2xl text-center">'
        idx = d.find("Lachgas bestellen in Rotterdam in 3 stappen")
        start = d.rfind("  <section ", 0, idx)
        # de regio-sectie is grijs (alt); de stappen-sectie is ook grijs: maak de regio-sectie wit en laat stappen grijs
        regio = regio.replace('<section class="bg-surface-50 px-4', '<section class="px-4', 1)
        d = d[:start] + regio + "\n" + d[start:]
        # vergelijkingstabel voor de FAQ
        rows = "".join('            <tr class="border-b border-gray-100">\n              <th scope="row" class="py-4 pr-4 text-left font-semibold text-gray-900">%s</th>\n'
                       '              <td class="py-4 px-4 text-whatsapp-600 font-semibold">%s</td>\n              <td class="py-4 px-4 text-gray-500">%s</td>\n            </tr>\n'
                       % (B.esc(r[0]), B.esc(r[1]), B.esc(r[2])) for r in H["compare_rows"])
        cards = "".join('        <div class="rounded-2xl border border-gray-100 bg-white p-5 shadow-card">\n'
                        '          <p class="mb-2 text-xs font-bold uppercase tracking-wide text-gray-400">%s</p>\n'
                        '          <p class="mb-1 text-sm font-semibold text-whatsapp-600">%s</p>\n'
                        '          <p class="text-sm text-gray-500">Elders vaak: %s</p>\n        </div>\n' % (B.esc(r[0]), B.esc(r[1]), B.esc(r[2])) for r in H["compare_rows"])
        table = ('  <section class="bg-surface-50 px-4 py-16 sm:px-6 md:py-20 lg:px-8 lg:py-24">\n    <div class="mx-auto max-w-4xl">\n'
                 '      <div class="mx-auto mb-10 max-w-2xl text-center">\n'
                 '        <span class="mb-4 inline-block rounded-full bg-gray-900 px-4 py-1.5 text-xs font-bold uppercase tracking-wide text-white">%s</span>\n'
                 '        <h2 class="mb-4 font-heading text-3xl font-bold sm:text-4xl">%s</h2>\n        <p class="text-gray-500">%s</p>\n      </div>\n'
                 '      <div class="grid gap-4 sm:grid-cols-2 lg:hidden">\n%s      </div>\n'
                 '      <div class="hidden lg:block overflow-x-auto rounded-2xl border border-gray-100 bg-white p-4 shadow-card">\n        <table class="w-full text-sm">\n'
                 '          <thead>\n            <tr class="border-b border-gray-200">\n              <th scope="col" class="py-3 pr-4 text-left text-xs font-bold uppercase tracking-wide text-gray-400">Kenmerk</th>\n'
                 '              <th scope="col" class="py-3 px-4 text-left text-xs font-bold uppercase tracking-wide text-gray-900">Lachgas Rotterdam</th>\n'
                 '              <th scope="col" class="py-3 px-4 text-left text-xs font-bold uppercase tracking-wide text-gray-400">Elders vaak</th>\n            </tr>\n          </thead>\n'
                 '          <tbody>\n%s          </tbody>\n        </table>\n      </div>\n'
                 '      <p class="mt-6 text-center text-sm text-gray-500">Lees meer over <a href="/voordelen/" class="%s">onze voordelen</a> en <a href="/lachgas-informatie/lachgas-bezorgservice-kiezen/" class="%s">waar je op let bij het kiezen van een bezorgservice</a>.</p>\n'
                 '    </div>\n  </section>\n\n' % (B.esc(H["compare_badge"]), B.esc(H["compare_h2"]), B.rich(H["compare_text"]), cards, rows, B.LINK, B.LINK))
        idx = d.find(">Nog vragen?<")
        start = d.rfind("  <section ", 0, idx)
        d = d[:start] + table + d[start:]
        # extra FAQ-items toevoegen (index opnieuw bepalen na het invoegen van de tabel)
        idx = d.find(">Nog vragen?<")
        end = d.find("</section>", idx)
        assert d.rfind("</details>", idx, end) > 0
        last_details = d.rfind("</details>", idx, end) + len("</details>")
        extra = "".join('\n        <details class="group rounded-xl border border-gray-100 bg-white overflow-hidden transition-shadow hover:shadow-sm">\n'
                        '          <summary class="flex w-full cursor-pointer items-center justify-between px-6 py-5 text-left">\n'
                        '            <span class="pr-4 text-base font-semibold text-gray-900">%s</span>\n            %s\n          </summary>\n'
                        '          <div class="px-6 pb-5 text-sm text-gray-500 leading-relaxed">%s</div>\n        </details>' % (B.esc(q), B.CHEVRON, B.rich(a)) for q, a in H["faq_extra"])
        d = d[:last_details] + extra + d[last_details:]
        # FAQPage-schema uitbreiden + LocalBusiness areaServed
        def fix(m):
            data = json.loads(m.group(1))
            if data.get("@type") == "FAQPage":
                for q, a in H["faq_extra"]:
                    data["mainEntity"].append({"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": B.strip_tags(a)}})
            elif data.get("@type") == "LocalBusiness":
                served = data.get("areaServed", [])
                names = {x.get("name") for x in served if isinstance(x, dict)}
                if "Zuid-Holland" not in names:
                    served.append({"@type": "AdministrativeArea", "name": "Zuid-Holland"})
                for a in self.c.AREAS:
                    if a["name"] not in names:
                        served.append({"@type": "City" if a.get("kind") in ("stad", "gemeente") else "AdministrativeArea", "name": a["name"]})
                data["areaServed"] = served
            else:
                return m.group(0)
            return '<script type="application/ld+json">%s</script>' % json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
        d = re.sub(r'<script type="application/ld\+json">(\{.*?\})</script>', fix, d, flags=re.S)
        B.write(p, d)
        # ---- bezorggebieden-overzicht ----
        p = os.path.join(self.repo, "bezorggebieden", "index.html")
        d = B.read(p)
        d = d.replace("<title>Lachgas bezorggebieden Rotterdam | Alle wijken</title>", "<title>Lachgas bezorggebieden Rotterdam en Zuid-Holland</title>", 1)
        d = re.sub(r'(<meta (?:property|name)="(?:og|twitter):title" content=")[^"]*(")', r'\1Lachgas bezorggebieden Rotterdam en Zuid-Holland\2', d)
        nd = "Wij bezorgen lachgas in heel Rotterdam en in ruim 25 plaatsen in Zuid-Holland, van Westland tot Dordrecht. Bestel via WhatsApp, snel en discreet aan de deur. 18+."
        d = re.sub(r'(<meta name="description" content=")[^"]*(")', lambda m: m.group(1) + nd + m.group(2), d, count=1)
        d = re.sub(r'(<meta (?:property|name)="(?:og|twitter):description" content=")[^"]*(")', lambda m: m.group(1) + nd + m.group(2), d)
        d = d.replace("Wij bezorgen lachgastanks in heel Rotterdam, aan beide kanten van de Maas. Snel, discreet en besteld via WhatsApp. Uitsluitend voor 18+.",
                      "Wij bezorgen lachgastanks in heel Rotterdam en in ruim 25 plaatsen in Zuid-Holland. Snel, discreet en besteld via WhatsApp. Uitsluitend voor 18+.", 1)
        # donkere chips: Rotterdamse gebieden + wijken; regio apart
        for a in self.old_towns:
            d = re.sub(r'\n\s*<a href="/lachgas-bestellen/%s/" class="%s">[^<]*</a>' % (a["slug"], re.escape(B.CHIP_DARK)), "", d, count=1)
        last = re.findall(r'<a href="/lachgas-bestellen/[a-z0-9-]+/" class="%s">[^<]*</a>' % re.escape(B.CHIP_DARK), d)[-1]
        add = "\n        ".join('<a href="/lachgas-bestellen/%s/" class="%s">%s</a>' % (a["slug"], B.CHIP_DARK, B.esc(a["name"])) for a in self.wijken)
        d = d.replace(last, last + "\n        " + add, 1)
        d = d.replace('<p class="mb-3 text-center text-xs font-bold uppercase tracking-wide text-gray-400">Gebieden</p>',
                      '<p class="mb-3 text-center text-xs font-bold uppercase tracking-wide text-gray-400">Rotterdam: gebieden en wijken</p>', 1)
        # regio-blok direct na de donkere chips (zelfde sectie)
        m = re.search(r'(<a href="/lachgas-bestellen/%s/" class="%s">[^<]*</a>\n      </div>)' % (self.wijken[-1]["slug"], re.escape(B.CHIP_DARK)), d)
        regio_chips = "\n        ".join('<a href="/lachgas-bestellen/%s/" class="%s">%s</a>' % (a["slug"], B.CHIP, B.esc(a["name"])) for a in all_towns)
        block = ('\n      <p class="mb-3 mt-10 text-center text-xs font-bold uppercase tracking-wide text-gray-400">Regio Zuid-Holland</p>\n'
                 '      <div class="flex flex-wrap justify-center gap-3">\n        %s\n      </div>\n'
                 '      <div class="mt-10 text-center">\n        <a href="%s" class="inline-flex items-center gap-1 text-sm font-bold text-brand-600 hover:text-brand-700">Alles over bezorgen in Zuid-Holland %s</a>\n      </div>' % (regio_chips, REGIO_PATH, B.ARROW))
        d = d[:m.end()] + block + d[m.end():]
        # kaarten voor alle nieuwe gebieden
        cards = re.findall(r'        <a href="/lachgas-bestellen/[a-z0-9-]+/" class="group flex flex-col.*?</a>\n', d, re.S)
        tpl = cards[-1]
        add = ""
        for a in self.wijken + self.towns:
            c = re.sub(r'href="/lachgas-bestellen/[a-z0-9-]+/"', 'href="/lachgas-bestellen/%s/"' % a["slug"], tpl, 1)
            c = re.sub(r'(<h3[^>]*>)[^<]*(</h3>)', lambda m: m.group(1) + B.esc("Lachgas " + a["name"]) + m.group(2), c, 1)
            c = re.sub(r'(<p class="mb-4 flex-1 text-sm text-gray-500">)[^<]*(</p>)', lambda m: m.group(1) + B.esc(a["lead"]) + m.group(2), c, 1)
            c = re.sub(r'(group-hover:text-brand-600">)Lachgas bestellen in [^<]*(<svg)', lambda m: m.group(1) + B.esc("Lachgas bestellen in " + a["name"] + " ") + m.group(2), c, 1)
            add += c
        d = d.replace(tpl, tpl + add, 1)
        d = d.replace("Onder elk gebied vallen meerdere wijken. Staat jouw buurt er niet bij? Stuur ons je postcode, dan bevestigen we of we bij jou kunnen bezorgen.",
                      "Onder elk gebied vallen meerdere wijken en buurten; de regiopagina's beschrijven de hele gemeente. Staat jouw plaats er niet bij? Stuur ons je postcode, dan bevestigen we of we bij jou kunnen bezorgen.", 1)
        B.write(p, d)

    def footer_links(self, doc):
        doc = super().footer_links(doc)
        a1 = '<li><a href="/bezorggebieden/" class="hover:text-white">Bezorggebieden</a></li>'
        n1 = '\n        <li><a href="%s" class="hover:text-white">Lachgas in Zuid-Holland</a></li>' % REGIO_PATH
        a2 = '<li><a href="/lachgas-feest-evenement/" class="hover:text-white">Feest &amp; evenement</a></li>'
        n2 = ('\n        <li><a href="/lachgas-spoedbezorging/" class="hover:text-white">Spoedbezorging</a></li>'
              '\n        <li><a href="/lachgas-bezorgen-weekend/" class="hover:text-white">Weekendbezorging</a></li>')
        if a1 in doc and n1.strip() not in doc:
            doc = doc.replace(a1, a1 + n1, 1)
        if a2 in doc and "/lachgas-spoedbezorging/" not in doc.split("<footer")[-1]:
            doc = doc.replace(a2, a2 + n2, 1)
        return doc

    def html_sitemap(self, pages):
        """HTML-sitemap (/sitemap/) opnieuw opbouwen uit alle pagina's."""
        p = os.path.join(self.repo, "sitemap", "index.html")
        d = B.read(p)
        li = '<li><a href="%s" class="font-semibold text-brand-600 hover:text-brand-700">%s</a></li>'
        h2a = '<h2 class="mb-4 font-heading text-2xl font-bold sm:text-3xl">%s</h2>'
        h2 = '<h2 class="mb-4 mt-10 font-heading text-2xl font-bold sm:text-3xl">%s</h2>'
        ul = '<ul class="space-y-2.5 text-gray-600">%s</ul>'
        titles = {path: t for path, t, ds, doc in pages}
        def name(path):
            doc = [x for x in pages if x[0] == path][0][3]
            m = re.search(r"<h1[^>]*>(.*?)</h1>", doc, re.S)
            return B.strip_tags(m.group(1)).strip() if m else titles[path]
        main_paths = ["/", "/lachgas-tanks/", "/bezorggebieden/", REGIO_PATH, "/werkwijze/", "/voordelen/", "/lachgas-nachtbezorging/", "/lachgas-bezorgen-weekend/",
                      "/lachgas-spoedbezorging/", "/lachgas-feest-evenement/", "/lachgas-bestellen-zonder-account/", "/veilig-gebruik/", "/faq/", "/contact/"]
        main_items = "".join(li % (pth, "Home: lachgas Rotterdam" if pth == "/" else name(pth)) for pth in main_paths if pth in titles)
        areas = [pth for pth, *_ in pages if pth.startswith("/lachgas-bestellen/") and pth != REGIO_PATH]
        rdam = [pth for pth in areas if pth.split("/")[2] in ROTTERDAM_GEBIEDEN + [w["slug"] for w in self.wijken]]
        regio = [pth for pth in areas if pth not in rdam]
        rdam_items = "".join(li % (pth, name(pth)) for pth in rdam)
        regio_items = "".join(li % (pth, name(pth)) for pth in sorted(regio, key=lambda x: name(x)))
        info = [pth for pth, *_ in pages if pth.startswith("/lachgas-informatie/")]
        info_items = "".join(li % (pth, name(pth) if pth != "/lachgas-informatie/" else "Overzicht lachgas informatie") for pth in info)
        legal = "".join(li % (pth, t) for pth, t in (("/voorwaarden/", "Algemene voorwaarden"), ("/privacy/", "Privacyverklaring")))
        new = (h2a % "Hoofdpagina's" + ul % main_items + h2 % "Lachgas bestellen in Rotterdam" + ul % rdam_items + h2 % "Lachgas bestellen in de regio Zuid-Holland" + ul % regio_items
               + h2 % "Lachgas informatie" + ul % info_items + h2 % "Juridisch" + ul % legal)
        d = re.sub(r'<h2 class="mb-4 font-heading text-2xl font-bold sm:text-3xl">Hoofdpagina\'s</h2>.*?(?=<p )', new, d, count=1, flags=re.S)
        B.write(p, d)


def main():
    c = content()
    if os.environ.get("SITE_REPO"):
        B.SITES["rotterdam"]["repo"] = os.environ["SITE_REPO"]
    b = R2(c)
    for a in c.AREAS:
        b.area_page(a)
    s = b.site
    for art in c.ARTICLES:
        b.article_page(art, s["info_dir"], (c.HUB["h1"], "/%s/" % s["info_dir"]), None)
    for sp in c.SERVICE_PAGES:
        b.article_page(sp, "", None, None, service=True)
    b.hub_page()
    b.regio_page()
    b.update_existing()
    b.upgrade_all()
    pages = b.finish()
    b.html_sitemap(pages)
    pages = b.finish()  # sitemap-pagina is gewijzigd: llms-full opnieuw
    print("rotterdam fase 2: %d nieuwe pagina's, %d pagina's in sitemap" % (len(b.new_pages), len(pages)))
    for p in b.new_pages:
        print("  ", p[0])


if __name__ == "__main__":
    main()
