#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fase 3 voor de bestaande sites (breda, groningen, antwerpen: 'template'; rotterdam: 'rotterdam').
- herschrijft dunne gebiedspagina's met nieuwe content (zelfde URL)
- nieuwe gebieds-, hub-, artikel-, service- en FAQ-themapagina's
- FAQ-hub, HTML-sitemap, werkwijze; per-site unieke gedeelde blokken (SITE_TEXTS)
- bijgewerkte overzichten, footer, LocalBusiness-schema; daarna performance-upgrade en sitemap/llms.
Gebruik: python3 phase3.py <site>   (SITE_REPO=/pad/naar/kopie voor een testrun)
Vereist een schone repo-checkout (de generator is niet idempotent voor chips/kaarten)."""
import html, importlib.util, json, os, re, sys, types
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_sites as B  # noqa
import perf_upgrade as PU  # noqa

CONTENT_ROOT = os.environ.get("P3_CONTENT", os.path.join(os.path.dirname(HERE), "content", "p3"))


def load_dir(cdir):
    mods = []
    for f in sorted(os.listdir(cdir)):
        if f.endswith(".py") and not f.startswith("_"):
            spec = importlib.util.spec_from_file_location(f[:-3], os.path.join(cdir, f)); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); mods.append(m)
    ns = types.SimpleNamespace(AREAS=[], ARTICLES=[], SERVICE_PAGES=[], FAQ_TOPICS=[], HUBS=[], PRODUCTS=[], SITE_TEXTS=None, FAQ_INDEX=None, ABOUT=None, PAGES_EXTRA=None)
    for m in mods:
        for k in ("AREAS", "ARTICLES", "SERVICE_PAGES", "FAQ_TOPICS", "HUBS", "PRODUCTS"):
            getattr(ns, k).extend(getattr(m, k, []))
        for k in ("SITE_TEXTS", "FAQ_INDEX", "ABOUT", "PAGES_EXTRA"):
            if hasattr(m, k): setattr(ns, k, getattr(m, k))
    return ns


class P3(B.Builder):
    def __init__(self, key, c):
        super().__init__(key, c)
        s = self.site
        self.faq_dir = "/faq/" if s["kind"] == "rotterdam" else "/veelgestelde-vragen/"
        self.area_label_kind = "Bezorggebieden" if s["kind"] == "rotterdam" else "Bezorggebied"
        self.rewrite = {a["slug"] for a in c.AREAS if a["slug"] in self.existing_areas}
        self.hub_paths = {h["slug"]: "/%s/%s/" % (s["area_dir"], h["slug"]) for h in c.HUBS}

    # -- gebiedspagina met regio-link en nette labels --------------------------
    def area_page(self, a):
        super().area_page(a)
        p = os.path.join(self.repo, self.site["area_dir"], a["slug"], "index.html")
        d = B.read(p)
        want = "Wijken en plekken" if a.get("kind") in ("stad", "gemeente", "district") else "Buurten en plekken"
        d = re.sub(r'<strong class="text-gray-900">(Wijken en plekken|Buurten en plekken) in ', '<strong class="text-gray-900">%s in ' % want, d, count=1)
        if self.c.HUBS:
            h = self.c.HUBS[0]
            d = d.replace('<a href="%s" class="%s">Bekijk volledig bezorggebied</a>' % (self.area_overview, B.CHIP),
                          '<a href="%s" class="%s">%s</a>\n        <a href="%s" class="%s">Bekijk volledig bezorggebied</a>' % (self.hub_paths[h["slug"]], B.CHIP, B.esc(h["name"]), self.area_overview, B.CHIP), 1)
        B.write(p, d)

    # -- regio-hub -------------------------------------------------------------
    def hub_page(self, h):
        s = self.site
        path = self.hub_paths[h["slug"]]
        crumbs = [("Home", "/"), (self.area_label, self.area_overview), (h["name"], None)]
        intro = "".join('      <p class="text-gray-600 leading-relaxed mb-4">%s</p>\n' % B.rich(p) for p in h["intro"])
        groups = ""
        for i, g in enumerate(h["groups"]):
            links = [("/%s/%s/" % (s["area_dir"], sl), self.area_names[sl]) for sl in g["slugs"] if sl in self.area_names]
            chips = "\n          ".join('<a href="%s" class="%s">%s</a>' % (hh, B.CHIP if i % 2 else B.CHIP_DARK, B.esc(t)) for hh, t in links)
            groups += ('      <div class="%s">\n        <h2 class="mb-2 font-heading text-2xl font-bold sm:text-3xl">%s</h2>\n        <p class="mb-6 text-gray-500">%s</p>\n'
                       '        <div class="flex flex-wrap gap-3">\n          %s\n        </div>\n      </div>\n' % ("mb-12" if i < len(h["groups"]) - 1 else "", B.esc(g["h2"]), B.rich(g["text"]), chips))
        main = ("\n  " + B.hero(crumbs, "Regio", h["h1"], h["lead"])
                + '  <section class="px-4 py-16 sm:px-6 md:py-20 lg:px-8 lg:py-24">\n    <div class="mx-auto max-w-4xl">\n%s    </div>\n  </section>\n' % intro
                + '  <section class="bg-surface-50 px-4 py-16 sm:px-6 md:py-20 lg:px-8 lg:py-24">\n    <div class="mx-auto max-w-4xl">\n%s    </div>\n  </section>\n' % groups
                + "  " + self.sec_waarom.replace("In %s meestal" % self.tpl_area_name, "In de regio meestal").replace(self.tpl_area_name, "de regio") + "\n  "
                + B.faq_block(h["faq"], "Veelgestelde vragen over bezorgen in de regio", alt=False) + "  " + self.sec_cta.replace(self.tpl_area_name, h["name"]) + "\n")
        served = [{"@type": "City", "name": self.area_names[sl]} for g in h["groups"] for sl in g["slugs"] if sl in self.area_names]
        schemas = [B.crumbs_schema(s, [("Home", "/"), (self.area_label, self.area_overview), (h["name"], path)]),
                   {"@context": "https://schema.org", "@type": "Service", "name": h["h1"], "description": h["description"], "url": s["domain"] + path, "serviceType": "Lachgas bezorgservice",
                    "provider": {"@type": "LocalBusiness", "name": s["brand"], "url": s["domain"] + "/", "@id": s["domain"] + "/#business"}, "areaServed": [{"@type": "AdministrativeArea", "name": h["name"]}] + served},
                   B.faq_schema(h["faq"])]
        d = self.doc(h["title"], h["description"], path, schemas, main, self.area_overview)
        B.write(os.path.join(self.repo, path.strip("/"), "index.html"), d)
        self.new_pages.append((path, h["title"], h["description"]))

    # -- FAQ-thema's en FAQ-hub ------------------------------------------------
    def faq_topic_page(self, t):
        s = self.site
        path = self.faq_dir + t["slug"] + "/"
        hub_name = "Veelgestelde vragen"
        crumbs = [("Home", "/"), (hub_name, self.faq_dir), (t["h1"], None)]
        intro = "".join('      <p class="text-gray-600 leading-relaxed mb-4">%s</p>\n' % B.rich(p) for p in t["intro"])
        others = [(self.faq_dir + x["slug"] + "/", x["h1"]) for x in self.c.FAQ_TOPICS if x["slug"] != t["slug"]] + [(self.faq_dir, "Alle veelgestelde vragen")]
        main = ("\n  " + B.hero(crumbs, "FAQ", t["h1"], t["lead"])
                + '  <section class="px-4 py-16 sm:px-6 md:py-20 lg:px-8 lg:py-24">\n    <div class="mx-auto max-w-3xl">\n%s    </div>\n  </section>\n' % intro
                + "  " + B.faq_block(t["items"], t["h1"], alt=True) + "  " + B.chips_section("Andere onderwerpen", "Meer vragen", others, alt=False) + "  " + self.sec_cta + "\n")
        schemas = [B.crumbs_schema(s, [("Home", "/"), (hub_name, self.faq_dir), (t["h1"], path)]), B.faq_schema(t["items"]), B.webpage_schema(s, t["title"], t["description"], path)]
        d = self.doc(t["title"], t["description"], path, schemas, main, self.faq_dir)
        B.write(os.path.join(self.repo, path.strip("/"), "index.html"), d)
        self.new_pages.append((path, t["title"], t["description"]))

    def faq_hub(self):
        """Bestaande FAQ-pagina wordt hub: kaarten naar thema's boven de bestaande vragen."""
        s = self.site
        p = os.path.join(self.repo, self.faq_dir.strip("/"), "index.html")
        d = B.read(p)
        cards = "".join(B.card(self.faq_dir + t["slug"] + "/", t["h1"], t["description"], "Bekijk de vragen") for t in self.c.FAQ_TOPICS)
        F = self.c.FAQ_INDEX or {}
        intro = "".join('      <p class="text-gray-600 leading-relaxed mb-4">%s</p>\n' % B.rich(x) for x in F.get("intro", []))
        block = ('  <section class="px-4 py-16 sm:px-6 md:py-20 lg:px-8 lg:py-24">\n    <div class="mx-auto max-w-4xl">\n%s    </div>\n'
                 '    <div class="mx-auto mt-6 max-w-5xl">\n      <div class="grid gap-4 sm:grid-cols-2">\n%s      </div>\n    </div>\n  </section>\n' % (intro, cards))
        # invoegen direct na de paginakop (eerste </section>)
        i = d.find("</section>") + len("</section>")
        d = d[:i] + "\n" + block + d[i:]
        if F.get("title"):
            d = re.sub(r"<title>.*?</title>", "<title>%s</title>" % B.esc(F["title"]), d, flags=re.S)
            d = re.sub(r'(<meta (?:property|name)="(?:og|twitter):title" content=")[^"]*(")', lambda m: m.group(1) + B.esc(F["title"]) + m.group(2), d)
        if F.get("description"):
            d = re.sub(r'(<meta name="description" content=")[^"]*(")', lambda m: m.group(1) + B.esc(F["description"]) + m.group(2), d, count=1)
            d = re.sub(r'(<meta (?:property|name)="(?:og|twitter):description" content=")[^"]*(")', lambda m: m.group(1) + B.esc(F["description"]) + m.group(2), d)
        B.write(p, d)

    # -- gedeelde blokken per site uniek maken ---------------------------------
    def apply_site_texts(self):
        T = self.c.SITE_TEXTS
        if not T: return
        s = self.site
        # 1. 'Waarom wij'-blok: vier h3 + p's in sec_waarom (en op alle pagina's die het blok bevatten)
        old = self.sec_waarom
        new = old
        items = re.findall(r'(<h3[^>]*>)(.*?)(</h3>\s*<p class="text-sm text-gray-500">)(.*?)(</p>)', old, re.S)
        if len(items) == 4 and len(T.get("why", [])) == 4:
            for (h3o, title, mid, text, pc), (nt, ntext) in zip(items, T["why"]):
                new = new.replace(h3o + title + mid + text + pc, h3o + B.esc(nt) + mid + B.esc(ntext) + pc, 1)
            new = re.sub(r'(<h2[^>]*>)[^<]*(</h2>)', lambda m: m.group(1) + B.esc(T["why_h2"]) + m.group(2), new, count=1)
        self.sec_waarom_new = new
        # 2. CTA-blok
        cta_old = self.sec_cta; cta_new = cta_old
        if T.get("cta_h2"):
            cta_new = re.sub(r'(<h2[^>]*>)[^<]*(</h2>)', lambda m: m.group(1) + B.esc(T["cta_h2"]) + m.group(2), cta_new, count=1)
        if T.get("cta_text"):
            cta_new = re.sub(r'(</h2>\s*<p[^>]*>)[^<]*(</p>)', lambda m: m.group(1) + B.esc(T["cta_text"]) + m.group(2), cta_new, count=1)
        self.sec_cta_new = cta_new
        # toepassen op alle pagina's: exacte blokken vervangen (ook gelokaliseerde varianten met andere plaatsnaam)
        why_re = self._loose_re(old) if new != old else None
        cta_re = self._loose_re(cta_old) if cta_new != cta_old else None
        n = 0
        for root, dirs, files in os.walk(self.repo):
            if ".git" in root: continue
            for f in files:
                if not f.endswith(".html"): continue
                p = os.path.join(root, f); d = B.read(p); o = d
                if why_re:
                    d = why_re.sub(lambda m: self._localized(new, m.group(0)), d)
                if cta_re:
                    d = cta_re.sub(lambda m: self._localized(cta_new, m.group(0)), d)
                if d != o: B.write(p, d); n += 1
        self.sec_waarom = new; self.sec_cta = cta_new
        print("   gedeelde blokken vervangen op %d pagina's" % n)

    def _loose_re(self, block):
        """Regex die het blok matcht ongeacht de ingevulde plaatsnaam/levertijd (dynamische stukken)."""
        esc = re.escape(block)
        esc = esc.replace(re.escape(self.tpl_area_name), r"[^<]{1,60}")
        esc = re.sub(r"In\\ [^<]{1,60}\\ meestal\\ binnen\\ [^<]*?\\.", r"In [^<]*?\\.", esc)
        esc = re.sub(r"meestal\\ binnen\\ \d+\\ tot\\ \d+\\ minuten", r"meestal binnen \\d+ tot \\d+ minuten", esc)
        return re.compile(esc, re.S)

    def _localized(self, new, matched):
        """Vervang het blok maar behoud de plaatsnaam/levertijd uit het oorspronkelijke blok."""
        m = re.search(r'Snelle levering</h3>\s*<p class="text-sm text-gray-500">([^<]*)</p>', matched)
        out = new
        if m:
            out = re.sub(r'(Snelle levering</h3>\s*<p class="text-sm text-gray-500">)[^<]*(</p>)', lambda mm: mm.group(1) + m.group(1) + mm.group(2), out, count=1)
        return out

    # -- overzichten, home, footer, schema --------------------------------------
    def update_existing(self):
        s = self.site
        new_areas = [a for a in self.c.AREAS if a["slug"] not in self.rewrite]
        towns = [a for a in new_areas if a.get("kind") in ("stad", "dorp", "gemeente")]
        wijken = [a for a in new_areas if a.get("kind") in ("wijk", "district")]
        # homepage + overzicht: chips
        for rel in ("index.html", self.area_overview.strip("/") + "/index.html"):
            p = os.path.join(self.repo, rel)
            if not os.path.exists(p): continue
            d = B.read(p)
            dark = re.findall(r'<a href="/%s/[a-z0-9-]+/" class="%s">[^<]*</a>' % (s["area_dir"], re.escape(B.CHIP_DARK)), d)
            light = re.findall(r'<a href="/%s/[a-z0-9-]+/" class="%s">[^<]*</a>' % (s["area_dir"], re.escape(B.CHIP)), d)
            if dark:
                add = "\n        ".join('<a href="/%s/%s/" class="%s">%s</a>' % (s["area_dir"], a["slug"], B.CHIP_DARK, B.esc(a["name"])) for a in wijken)
                if add: d = d.replace(dark[-1], dark[-1] + "\n        " + add, 1)
                rest = towns
            else:
                rest = wijken + towns if rel == "index.html" else new_areas
            if light and rest:
                add = "\n        ".join('<a href="/%s/%s/" class="%s">%s</a>' % (s["area_dir"], a["slug"], B.CHIP, B.esc(a["name"])) for a in rest)
                d = d.replace(light[-1], light[-1] + "\n        " + add, 1)
            elif not light and dark and rest:
                add = "\n        ".join('<a href="/%s/%s/" class="%s">%s</a>' % (s["area_dir"], a["slug"], B.CHIP_DARK, B.esc(a["name"])) for a in rest)
                d = d.replace(dark[-1], dark[-1] + "\n        " + add, 1)
            # overzicht: kaarten (rotterdam-stijl) + hub-link
            if rel != "index.html":
                cards = re.findall(r'        <a href="/%s/[a-z0-9-]+/" class="group flex flex-col.*?</a>\n' % s["area_dir"], d, re.S)
                if cards:
                    tpl = cards[-1]; add = ""
                    for a in new_areas:
                        cc = re.sub(r'href="/%s/[a-z0-9-]+/"' % s["area_dir"], 'href="/%s/%s/"' % (s["area_dir"], a["slug"]), tpl, 1)
                        cc = re.sub(r'(<h3[^>]*>)[^<]*(</h3>)', lambda m: m.group(1) + B.esc("Lachgas " + a["name"]) + m.group(2), cc, 1)
                        cc = re.sub(r'(<p class="mb-4 flex-1 text-sm text-gray-500">)[^<]*(</p>)', lambda m: m.group(1) + B.esc(a["lead"]) + m.group(2), cc, 1)
                        cc = re.sub(r'(group-hover:text-brand-600">)Lachgas bestellen in [^<]*(<svg)', lambda m: m.group(1) + B.esc("Lachgas bestellen in " + a["name"] + " ") + m.group(2), cc, 1)
                        add += cc
                    d = d.replace(tpl, tpl + add, 1)
                for h in self.c.HUBS:
                    link = ('\n      <div class="mt-10 text-center">\n        <a href="%s" class="inline-flex items-center gap-1 text-sm font-bold text-brand-600 hover:text-brand-700">Alles over bezorgen in %s %s</a>\n      </div>'
                            % (self.hub_paths[h["slug"]], B.esc(h["name"]), B.ARROW))
                    last = re.findall(r'<a href="/%s/[a-z0-9-]+/" class="%s">[^<]*</a>\n      </div>' % (s["area_dir"], re.escape(B.CHIP_DARK if dark else B.CHIP)), d)
                    if last: d = d.replace(last[-1], last[-1] + link, 1)
            B.write(p, d)
        # informatie-overzicht (template): kaarten voor nieuwe artikelen
        if s["kind"] == "template":
            p = os.path.join(self.repo, s["info_dir"], "index.html"); d = B.read(p)
            cards = re.findall(r'        <a href="/lachgas-informatie/[a-z0-9-]+/" class="group flex flex-col.*?</a>\n', d, re.S)
            tpl = cards[-1]; add = ""
            for a in self.c.ARTICLES:
                cc = re.sub(r'href="/lachgas-informatie/[a-z0-9-]+/"', 'href="/lachgas-informatie/%s/"' % a["slug"], tpl, 1)
                cc = re.sub(r'(<h2[^>]*>)[^<]*(</h2>)', lambda m: m.group(1) + B.esc(a["h1"]) + m.group(2), cc, 1)
                cc = re.sub(r'(<p class="mb-4 flex-1 text-sm text-gray-500">)[^<]*(</p>)', lambda m: m.group(1) + B.esc(a["description"]) + m.group(2), cc, 1)
                add += cc
            d = d.replace(tpl, tpl + add, 1); B.write(p, d)
        else:
            self.rotterdam_hub_refresh()
        # LocalBusiness areaServed
        p = os.path.join(self.repo, "index.html"); d = B.read(p)
        def fix_lb(m):
            data = json.loads(m.group(1))
            if data.get("@type") != "LocalBusiness": return m.group(0)
            served = data.get("areaServed", [])
            if served and isinstance(served[0], str): served = [{"@type": "City", "name": x} for x in served]
            names = {x.get("name") for x in served if isinstance(x, dict)}
            for h in self.c.HUBS:
                if h["name"] not in names: served.append({"@type": "AdministrativeArea", "name": h["name"]})
            for a in self.c.AREAS:
                if a["name"] not in names: served.append({"@type": "City" if a.get("kind") in ("stad", "gemeente") else "AdministrativeArea", "name": a["name"]})
            data["areaServed"] = served
            return '<script type="application/ld+json">%s</script>' % json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
        d = re.sub(r'<script type="application/ld\+json">(\{.*?\})</script>', fix_lb, d, count=1, flags=re.S)
        B.write(p, d)

    def rotterdam_hub_refresh(self):
        """Rotterdam: informatie-hub opnieuw opbouwen met alle artikelen (hergebruik van rotterdam2.hub_page-logica)."""
        s = self.site
        import rotterdam2 as R2  # noqa
        old = R2.load(os.path.join(os.path.dirname(HERE), "content", "rotterdam.py"), "rold")
        self.c.HUB = old.HUB
        R2.R2.hub_page(self)

    # -- homepage-teksten per site ---------------------------------------------
    def home_texts(self):
        T = self.c.SITE_TEXTS or {}
        s = self.site
        p = os.path.join(self.repo, "index.html"); d = B.read(p)
        if T.get("home_h1"):
            h1 = B.esc(T["home_h1"]).replace(B.esc(s["city"]), '<span class="text-brand-600">%s</span>' % B.esc(s["city"]), 1)
            d = re.sub(r"(<h1[^>]*>)(.*?)(</h1>)", lambda m: m.group(1) + "\n          " + h1 + "\n        " + m.group(3), d, count=1, flags=re.S)
        if T.get("home_hero_lead"):
            d = re.sub(r'(<p class="mb-8 max-w-xl text-lg text-gray-500">)\s*.*?\s*(</p>)', lambda m: m.group(1) + "\n          " + B.rich(T["home_hero_lead"]) + "\n        " + m.group(2), d, count=1, flags=re.S)
        if len(T.get("home_why", [])) == 4:
            items = list(re.finditer(r'(<h3 class="mb-1 font-bold">)(.*?)(</h3>\s*<p class="[^"]*">)(.*?)(</p>)', d, re.S))
            if len(items) >= 4:
                for m, (nt, ntext) in reversed(list(zip(items[:4], T["home_why"]))):
                    d = d[:m.start()] + m.group(1) + B.esc(nt) + m.group(3) + B.esc(ntext) + m.group(5) + d[m.end():]
            if T.get("home_why_h2"):
                i = d.find('<h3 class="mb-1 font-bold">'); j = d.rfind("<h2", 0, i)
                d = d[:j] + re.sub(r"(<h2[^>]*>)[^<]*(</h2>)", lambda m: m.group(1) + B.esc(T["home_why_h2"]) + m.group(2), d[j:], count=1)
        if T.get("home_areas_text"):
            m = re.search(r'(<h2[^>]*>Lachgas bezorgd in [^<]*</h2>\s*<p class="text-gray-500">)[^<]*(</p>)', d)
            if m: d = d[:m.start()] + m.group(1) + B.esc(T["home_areas_text"]) + m.group(2) + d[m.end():]
        if T.get("home_faq"):
            items = T["home_faq"]
            blk = "".join('\n        <details class="group rounded-xl border border-gray-100 bg-white overflow-hidden transition-shadow hover:shadow-sm"%s>\n'
                          '          <summary class="flex w-full cursor-pointer items-center justify-between px-6 py-5 text-left">\n'
                          '            <span class="pr-4 text-base font-semibold text-gray-900">%s</span>\n            %s\n          </summary>\n'
                          '          <div class="px-6 pb-5 text-sm text-gray-500 leading-relaxed">%s</div>\n        </details>' % (" open" if i == 0 else "", B.esc(q), B.CHEVRON, B.rich(a)) for i, (q, a) in enumerate(items))
            first = d.find("<details "); last = d.rfind("</details>") + len("</details>")
            if first > 0:
                d = d[:first].rstrip() + blk + "\n" + d[last:].lstrip("\n")
            def fix(m):
                data = json.loads(m.group(1))
                if data.get("@type") != "FAQPage": return m.group(0)
                data["mainEntity"] = [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": B.strip_tags(a)}} for q, a in items]
                return '<script type="application/ld+json">%s</script>' % json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
            d = re.sub(r'<script type="application/ld\+json">(\{.*?\})</script>', fix, d, flags=re.S)
        if T.get("home_title"):
            d = re.sub(r"<title>.*?</title>", "<title>%s</title>" % B.esc(T["home_title"]), d, flags=re.S)
            d = re.sub(r'(<meta (?:property|name)="(?:og|twitter):title" content=")[^"]*(")', lambda m: m.group(1) + B.esc(T["home_title"]) + m.group(2), d)
        if T.get("home_description"):
            d = re.sub(r'(<meta name="description" content=")[^"]*(")', lambda m: m.group(1) + B.esc(T["home_description"]) + m.group(2), d, count=1)
            d = re.sub(r'(<meta (?:property|name)="(?:og|twitter):description" content=")[^"]*(")', lambda m: m.group(1) + B.esc(T["home_description"]) + m.group(2), d)
        B.write(p, d)
        # assortiment-intro
        A = T.get("assortiment")
        pa = os.path.join(self.repo, "assortiment", "index.html")
        if A and os.path.exists(pa):
            d = B.read(pa)
            if A.get("lead"): d = re.sub(r'(<p class="mx-auto max-w-2xl text-white/60">)[^<]*(</p>)', lambda m: m.group(1) + B.esc(A["lead"]) + m.group(2), d, count=1)
            if A.get("intro"):
                ps = list(re.finditer(r'<p class="text-gray-600 leading-relaxed[^"]*">.*?</p>', d, re.S))[:len(A["intro"])]
                for m, txt in reversed(list(zip(ps, A["intro"]))):
                    cls = re.search(r'class="([^"]*)"', m.group(0)).group(1)
                    d = d[:m.start()] + '<p class="%s">%s</p>' % (cls, B.rich(txt)) + d[m.end():]
            B.write(pa, d)

    # -- over ons ---------------------------------------------------------------
    def about_page(self):
        A = self.c.ABOUT
        if not A: return
        s = self.site
        path = "/over-ons/"
        crumbs = [("Home", "/"), (A["h1"], None)]
        main = ("\n  " + B.hero(crumbs, "Over ons", A["h1"], A["lead"]) + "  " + B.article_body(A["sections"], A.get("note"))
                + "  " + B.chips_section("Verder lezen", "Meer over ons", [("/werkwijze/" if os.path.exists(os.path.join(self.repo, "werkwijze")) else self.area_overview, "Werkwijze" if os.path.exists(os.path.join(self.repo, "werkwijze")) else self.area_label), (self.area_overview, self.area_label), ("/contact/", "Contact"), ("/%s/" % s["info_dir"], "Lachgas informatie")], alt=True)
                + "  " + self.sec_cta + "\n")
        schemas = [B.crumbs_schema(s, [("Home", "/"), (A["h1"], path)]), {"@context": "https://schema.org", "@type": "AboutPage", "name": A["title"], "url": s["domain"] + path, "description": A["description"], "mainEntity": {"@id": s["domain"] + "/#business"}}]
        d = self.doc(A["title"], A["description"], path, schemas, main, None)
        B.write(os.path.join(self.repo, "over-ons", "index.html"), d)
        self.new_pages.append((path, A["title"], A["description"]))

    # -- productpagina's ---------------------------------------------------------
    def product_page(self, pr):
        s = self.site
        path = "/product/%s/" % pr["slug"]
        crumbs = [("Home", "/"), ("Assortiment", "/assortiment/"), (pr["h1"], None)]
        specs = "".join('        <div class="flex justify-between gap-4 border-b border-gray-100 py-3 text-sm"><span class="text-gray-500">%s</span><span class="font-semibold text-gray-900">%s</span></div>\n' % (B.esc(k), B.esc(v)) for k, v in pr["facts"])
        spec_block = ('<section class="bg-surface-50 px-4 py-16 sm:px-6 md:py-20 lg:px-8 lg:py-24">\n    <div class="mx-auto max-w-3xl">\n      <div class="mb-8 text-center"><span class="mb-4 inline-block rounded-full bg-gray-900 px-4 py-1.5 text-xs font-bold uppercase tracking-wide text-white">Specificaties</span>\n'
                      '        <h2 class="font-heading text-3xl font-bold sm:text-4xl">%s in het kort</h2></div>\n      <div class="rounded-2xl border border-gray-100 bg-white p-6">\n%s      </div>\n    </div>\n  </section>\n' % (B.esc(pr["h1"]), specs))
        others = [("/product/%s/" % x["slug"], x["h1"]) for x in self.c.PRODUCTS if x["slug"] != pr["slug"]] + [("/assortiment/", "Volledig assortiment")]
        main = ("\n  " + B.hero(crumbs, "Assortiment", pr["h1"], pr["lead"]) + "  " + B.article_body(pr["sections"], pr.get("note")) + "  " + spec_block
                + "  " + B.faq_block(pr["faq"], "Veelgestelde vragen over de %s" % pr["h1"].lower(), alt=False) + "  " + B.chips_section("Andere producten", "Ook leverbaar", others, alt=True) + "  " + self.sec_cta + "\n")
        schema = {"@context": "https://schema.org", "@type": "Product", "name": pr["h1"], "description": pr["description"], "url": s["domain"] + path, "brand": {"@type": "Brand", "name": s["brand"]},
                  "offers": {"@type": "Offer", "availability": "https://schema.org/InStock", "priceCurrency": "EUR", "url": s["domain"] + path, "seller": {"@type": "LocalBusiness", "name": s["brand"], "@id": s["domain"] + "/#business"}}}
        og = re.search(r'<meta property="og:image" content="([^"]+)"', self.area_doc)
        if og: schema["image"] = og.group(1)
        schemas = [B.crumbs_schema(s, [("Home", "/"), ("Assortiment", "/assortiment/"), (pr["h1"], path)]), schema, B.faq_schema(pr["faq"])]
        d = self.doc(pr["title"], pr["description"], path, schemas, main, "/assortiment/")
        B.write(os.path.join(self.repo, "product", pr["slug"], "index.html"), d)
        self.new_pages.append((path, pr["title"], pr["description"]))

    # -- assortiment, bezorggebied-index, informatie-index, contact: unieke teksten per site ----
    def extra_pages(self):
        X = self.c.PAGES_EXTRA
        if not X: return
        s = self.site
        def set_lead(d, lead):
            return re.sub(r'(<p class="mx-auto max-w-2xl text-white/60">)[^<]*(</p>)', lambda m: m.group(1) + B.esc(lead) + m.group(2), d, count=1)
        def set_meta(d, title=None, desc=None):
            if title:
                d = re.sub(r"<title>.*?</title>", "<title>%s</title>" % B.esc(title), d, flags=re.S)
                d = re.sub(r'(<meta (?:property|name)="(?:og|twitter):title" content=")[^"]*(")', lambda m: m.group(1) + B.esc(title) + m.group(2), d)
            if desc:
                d = re.sub(r'(<meta name="description" content=")[^"]*(")', lambda m: m.group(1) + B.esc(desc) + m.group(2), d, count=1)
                d = re.sub(r'(<meta (?:property|name)="(?:og|twitter):description" content=")[^"]*(")', lambda m: m.group(1) + B.esc(desc) + m.group(2), d)
            return d
        # a. assortiment: volledig opnieuw opgebouwd, productkaarten uit de bestaande pagina hergebruikt
        A = X.get("assortiment")
        pa = os.path.join(self.repo, "assortiment", "index.html")
        if A and os.path.exists(pa):
            old = B.read(pa)
            cards_sec = B.extract_section(old, "Het volledige aanbod")
            if cards_sec and self.c.PRODUCTS:
                for pr in self.c.PRODUCTS:
                    cards_sec = re.sub(r'(href="/product/%s/".*?<p class="mb-4 flex-1 text-sm text-gray-500">)[^<]*(</p>)' % re.escape(pr["slug"]), lambda m: m.group(1) + B.esc(pr["lead"]) + m.group(2), cards_sec, count=1, flags=re.S)
            path = "/assortiment/"
            crumbs = [("Home", "/"), ("Assortiment", None)]
            intro = "".join('      <p class="text-gray-600 leading-relaxed mb-4">%s</p>\n' % B.rich(x) for x in A["intro"])
            main = ("\n  " + B.hero(crumbs, "Assortiment", A["h1"], A["lead"])
                    + '  <section class="px-4 py-16 sm:px-6 md:py-20 lg:px-8 lg:py-24">\n    <div class="mx-auto max-w-4xl">\n%s    </div>\n  </section>\n' % intro
                    + "  " + (cards_sec or "") + "\n  " + B.article_body(A["sections"], A.get("note")).replace('<section class="px-4', '<section class="bg-surface-50 px-4', 1)
                    + "  " + B.faq_block(A["faq"], "Vragen over ons assortiment", alt=False) + "  " + self.sec_cta + "\n")
            schemas = [B.crumbs_schema(s, [("Home", "/"), ("Assortiment", path)]), B.faq_schema(A["faq"]),
                       B.webpage_schema(s, A["title"], A["description"], path),
                       {"@context": "https://schema.org", "@type": "ItemList", "name": A["h1"], "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": s["domain"] + "/product/%s/" % pr["slug"], "name": pr["h1"]} for i, pr in enumerate(self.c.PRODUCTS)]}]
            d = self.doc(A["title"], A["description"], path, schemas, main, "/assortiment/")
            B.write(pa, d)
        # b. bezorggebied-index: lead, h2 en intro-alinea's
        G = X.get("areas_index")
        pg = os.path.join(self.repo, self.area_overview.strip("/"), "index.html")
        if G and os.path.exists(pg):
            d = B.read(pg)
            d = set_lead(d, G["lead"]); d = set_meta(d, G.get("title"), G.get("description"))
            d = re.sub(r'(<h2 class="mb-4 font-heading text-3xl font-bold sm:text-4xl">)[^<]*(</h2>)', lambda m: m.group(1) + B.esc(G["h2"]) + m.group(2), d, count=1)
            ps = list(re.finditer(r'<p class="text-gray-600 leading-relaxed[^"]*">.*?</p>', d, re.S))[:len(G["intro"])]
            for m, txt in reversed(list(zip(ps, G["intro"]))):
                cls = re.search(r'class="([^"]*)"', m.group(0)).group(1)
                d = d[:m.start()] + '<p class="%s">%s</p>' % (cls, B.rich(txt)) + d[m.end():]
            B.write(pg, d)
        # c. informatie-index: lead + intro-sectie direct na de paginakop
        I = X.get("info_index")
        pi = os.path.join(self.repo, s["info_dir"], "index.html")
        if I and os.path.exists(pi):
            d = B.read(pi)
            d = set_lead(d, I["lead"]); d = set_meta(d, I.get("title"), I.get("description"))
            if 'data-intro="site"' not in d:
                block = ('  <section class="px-4 py-16 sm:px-6 md:py-20 lg:px-8 lg:py-24" data-intro="site">\n    <div class="mx-auto max-w-4xl">\n%s    </div>\n  </section>\n'
                         % "".join('      <p class="text-gray-600 leading-relaxed mb-4">%s</p>\n' % B.rich(x) for x in I["intro"]))
                i = d.find("</section>") + len("</section>")
                d = d[:i] + "\n" + block + d[i:]
            B.write(pi, d)
        # d. contact: lead + korte intro-sectie
        Cc = X.get("contact")
        pc = os.path.join(self.repo, "contact", "index.html")
        if Cc and os.path.exists(pc):
            d = B.read(pc)
            d = set_lead(d, Cc["lead"]); d = set_meta(d, Cc.get("title"), Cc.get("description"))
            if 'data-intro="site"' not in d:
                block = ('  <section class="px-4 py-16 sm:px-6 md:py-20 lg:px-8 lg:py-24" data-intro="site">\n    <div class="mx-auto max-w-4xl">\n%s    </div>\n  </section>\n'
                         % "".join('      <p class="text-gray-600 leading-relaxed mb-4">%s</p>\n' % B.rich(x) for x in Cc["intro"]))
                i = d.find("</section>") + len("</section>")
                d = d[:i] + "\n" + block + d[i:]
            B.write(pc, d)

    def footer_links(self, doc):
        doc = super().footer_links(doc)
        s = self.site
        T = self.c.SITE_TEXTS or {}
        for anchor, add in T.get("footer_links", []):
            if anchor in doc and add.split('href="')[1].split('"')[0] not in doc.split("<footer")[-1]:
                doc = doc.replace(anchor, anchor + "\n        " + add, 1)
        # sitemap-link in de juridische regel van de footer (template-sites hadden die niet)
        m = re.search(r'(<a href="/privacy/" class="([^"]*)">Privacy(?:verklaring)?</a>)', doc)
        if m and 'href="/sitemap/"' not in doc.split("<footer")[-1]:
            doc = doc.replace(m.group(1), m.group(1) + '\n        <a href="/sitemap/" class="%s">Sitemap</a>' % m.group(2), 1)
        return doc

    def html_sitemap(self, pages):
        s = self.site
        p = os.path.join(self.repo, "sitemap", "index.html")
        li = '<li><a href="%s" class="font-semibold text-brand-600 hover:text-brand-700">%s</a></li>'
        h2a = '<h2 class="mb-4 font-heading text-2xl font-bold sm:text-3xl">%s</h2>'
        h2 = '<h2 class="mb-4 mt-10 font-heading text-2xl font-bold sm:text-3xl">%s</h2>'
        ul = '<ul class="space-y-2.5 text-gray-600">%s</ul>'
        docs = {path: doc for path, t, ds, doc in pages}
        def name(path):
            m = re.search(r"<h1[^>]*>(.*?)</h1>", docs[path], re.S)
            return B.strip_tags(m.group(1)).strip() if m else path
        area_prefix = "/%s/" % s["area_dir"]
        areas = sorted([pth for pth in docs if pth.startswith(area_prefix)], key=name)
        info = sorted([pth for pth in docs if pth.startswith("/%s/" % s["info_dir"]) and pth != "/%s/" % s["info_dir"]], key=name)
        faqs = sorted([pth for pth in docs if pth.startswith(self.faq_dir) and pth != self.faq_dir], key=name)
        products = sorted([pth for pth in docs if pth.startswith("/product/") or pth.startswith("/lachgas-tanks/")], key=name)
        rest = sorted([pth for pth in docs if pth.count("/") == 2 and pth not in ("/sitemap/", "/404.html") and not pth.startswith(("/privacy", "/algemene-voorwaarden", "/voorwaarden"))], key=name)
        groups = [("Hoofdpagina's", [("/", "Home")] + [(pth, name(pth)) for pth in rest if pth != "/"]), ("Bezorggebied", [(pth, name(pth)) for pth in areas]),
                  ("Assortiment", [(pth, name(pth)) for pth in products]), ("Lachgas informatie", [("/%s/" % s["info_dir"], "Overzicht")] + [(pth, name(pth)) for pth in info]),
                  ("Veelgestelde vragen", [(self.faq_dir, "Overzicht")] + [(pth, name(pth)) for pth in faqs]),
                  ("Juridisch", [(pth, name(pth)) for pth in docs if pth.startswith(("/privacy", "/algemene-voorwaarden", "/voorwaarden"))])]
        inner = "".join((h2a if i == 0 else h2) % B.esc(h) + ul % "".join(li % (u, B.esc(n)) for u, n in items) for i, (h, items) in enumerate(groups) if items)
        if os.path.exists(p):
            d = B.read(p)
            d = re.sub(r'<h2 class="mb-4 font-heading text-2xl font-bold sm:text-3xl">Hoofdpagina\'s</h2>.*?(?=<p )', inner, d, count=1, flags=re.S)
        else:
            path = "/sitemap/"
            main = ("\n  " + B.hero([("Home", "/"), ("Sitemap", None)], "Overzicht", "Sitemap", "Alle pagina's van %s op een rij." % s["brand"])
                    + '  <section class="px-4 py-16 sm:px-6 md:py-20 lg:px-8 lg:py-24">\n    <div class="mx-auto max-w-4xl">\n      %s<p class="mt-8"><a href="/sitemap.xml" class="%s">XML-sitemap voor zoekmachines</a></p>\n    </div>\n  </section>\n' % (inner, B.LINK) + "  " + self.sec_cta + "\n")
            schemas = [B.crumbs_schema(s, [("Home", "/"), ("Sitemap", path)])]
            d = self.doc("Sitemap | %s" % s["brand"], "Overzicht van alle pagina's van %s: bezorggebied, assortiment, informatie, veelgestelde vragen en service. Snel naar de pagina die je zoekt." % s["brand"], path, schemas, main, None)
            d = d.replace('<meta name="robots" content="index,follow', '<meta name="robots" content="index,follow') if "robots" in d else d
        B.write(p, d)
        self.new_pages.append(("/sitemap/", "Sitemap", ""))


def main():
    key = sys.argv[1]
    c = load_dir(os.path.join(CONTENT_ROOT, key))
    if os.environ.get("SITE_REPO"): B.SITES[key]["repo"] = os.environ["SITE_REPO"]
    b = P3(key, c)
    s = b.site
    b.apply_site_texts()
    for a in c.AREAS: b.area_page(a)
    for h in c.HUBS: b.hub_page(h)
    if s["kind"] == "template":
        for art in c.ARTICLES: b.article_page(art, s["info_dir"], (s["info_label"], "/%s/" % s["info_dir"]), "/%s/" % s["info_dir"])
    else:
        import rotterdam2 as R2
        old = R2.load(os.path.join(os.path.dirname(HERE), "content", "rotterdam.py"), "rold")
        for art in c.ARTICLES: b.article_page(art, s["info_dir"], (old.HUB["h1"], "/%s/" % s["info_dir"]), None)
    for sp in c.SERVICE_PAGES: b.article_page(sp, "", None, None, service=True)
    for t in c.FAQ_TOPICS: b.faq_topic_page(t)
    if c.FAQ_TOPICS: b.faq_hub()
    b.about_page()
    b.extra_pages()
    for pr in getattr(c, "PRODUCTS", []): b.product_page(pr)
    b.update_existing()
    b.home_texts()
    pages = b.finish()
    b.html_sitemap(pages)
    b.upgrade_all()
    PU.main_repo(b.repo)
    pages = b.finish()
    print("%s: %d nieuwe/herschreven pagina's, %d pagina's in sitemap" % (key, len(b.new_pages), len(pages)))


if __name__ == "__main__":
    main()
