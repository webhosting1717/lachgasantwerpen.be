#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Controleer contentmodules (fase 3 / Brabant): lengtes, verboden inhoud, links, slugs, dubbele zinnen.
Gebruik: python3 check_content.py <contentmap> [<repo>]   (repo = bestaande site voor bestaande paden)"""
import importlib.util, os, re, sys, collections
cdir = sys.argv[1]; repo = sys.argv[2] if len(sys.argv) > 2 else None
BAD = [r"€", r"\beuro\b", r"\bbel ons\b", r"\+31 ?6", r"\b06[- ]?\d{8}\b", r"nachtkoerier|247gas|lachgas010|partygas|fastgass|directlachgas|lachgasnu|spacegas|040lachgas|brabantgas|nachtboer|gas2go",
       r"goedkoopst", r"\bonschuldig\b(?!\s*\.)", r"&rsquo;|&amp;|&#\d", r"<(?!/?(a|strong)\b)[a-z]", r"\bballonnen\b.*\b\d+\b|\b\d+\s*ballonnen", r"(?<!geen )(?<!zonder )\bgarantie\b(?! dat)", r"\bgegarandeerd\b", r"legaal voor recreatief", r"\bveilig middel\b"]
mods = {}
for f in sorted(os.listdir(cdir)):
    if f.endswith(".py"):
        spec = importlib.util.spec_from_file_location(f[:-3], os.path.join(cdir, f)); m = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(m); mods[f] = m
        except Exception as e:
            print("IMPORTFOUT %s: %s (bestand overgeslagen)" % (f, str(e)[:80]))
            if "--strict" in sys.argv: sys.exit(1)
# toegestane paden: bestaand in repo + alles wat de modules definiëren
allowed = set(); slugs = set()
if repo:
    for d, _, fs in os.walk(repo):
        if ".git" in d: continue
        for x in fs:
            if x == "index.html":
                allowed.add("/" + os.path.relpath(d, repo).replace(os.sep, "/").strip(".").strip("/") + "/")
    allowed.add("/")
    allowed = {a.replace("//", "/") for a in allowed}
cfg = None
for m in mods.values():
    if hasattr(m, "CONFIG"): cfg = m.CONFIG
area_dir = (cfg or {}).get("area_dir", "/bezorggebied"); info_dir = (cfg or {}).get("info_dir", "/lachgas-informatie"); faq_dir = (cfg or {}).get("faq_dir", "/veelgestelde-vragen"); svc_dir = (cfg or {}).get("service_dir", "")
for m in mods.values():
    for a in getattr(m, "AREAS", []): allowed.add("%s/%s/" % (area_dir, a["slug"])); slugs.add(a["slug"])
    for a in getattr(m, "HUBS", []): allowed.add("%s/%s/" % (area_dir, a["slug"])); slugs.add(a["slug"])
    for a in getattr(m, "ARTICLES", []): allowed.add("%s/%s/" % (info_dir, a["slug"]))
    for a in getattr(m, "SERVICE_PAGES", []): allowed.add("%s/%s/" % (svc_dir, a["slug"]) if svc_dir else "/%s/" % a["slug"])
    for a in getattr(m, "FAQ_TOPICS", []): allowed.add("%s/%s/" % (faq_dir, a["slug"]))
    for a in getattr(m, "TANKS", {}).get("TANKS", []) if isinstance(getattr(m, "TANKS", None), dict) else []: allowed.add("/lachgas-tanks/%s/" % a["slug"])
allowed |= set((cfg or {}).get("extra_allowed", [])); slugs |= set((cfg or {}).get("slugs", []))
ext_ok = (cfg or {}).get("external", ["https://www.rijksoverheid.nl", "https://www.drugsinfo.nl", "https://www.trimbos.nl"])
if repo:
    for d in os.listdir(os.path.join(repo, area_dir.strip("/"))) if os.path.isdir(os.path.join(repo, area_dir.strip("/"))) else []: slugs.add(d)
probs = 0
def warn(w, msg):
    global probs; probs += 1; print("%-48s %s" % (w, msg))
def txt(where, t, maxlinks=2):
    for b in BAD:
        mm = re.search(b, t, re.I)
        if mm: warn(where, "VERBODEN %r -> %s" % (b[:25], t[max(0, mm.start()-30):mm.end()+20].replace("\n", " ")))
    for h in re.findall(r'href="([^"]+)"', t):
        if h.startswith("/"):
            if h.split("#")[0] not in allowed: warn(where, "LINK onbekend " + h)
        elif not any(h.startswith(e) for e in ext_ok): warn(where, "EXTERNE link " + h)
    if t.count("<a ") > maxlinks: warn(where, "%d links" % t.count("<a "))
def meta(where, d):
    if len(d["title"]) > 60: warn(where, "TITLE %d" % len(d["title"]))
    if not 120 <= len(d["description"]) <= 155: warn(where, "DESC %d" % len(d["description"]))
    for k in ("title", "description", "h1", "lead"):
        if k in d: txt(where + " " + k, d[k])
    if len(d.get("lead", "")) > 200: warn(where, "LEAD %d tekens" % len(d["lead"]))
seen = {}
def sentences(where, texts):
    for p in texts:
        for s in re.split(r"(?<=[.!?])\s+", re.sub(r"<[^>]+>", "", p)):
            if len(s) > 55:
                if s in seen and seen[s] != where: warn(where, "DUBBELE ZIN ook in %s: %s" % (seen[s], s[:70]))
                seen[s] = where
def wc(t): return len(re.sub(r"<[^>]+>", "", t).split())
for f, m in mods.items():
    for a in getattr(m, "AREAS", []) + getattr(m, "HUBS", []):
        w = f + ":" + a["slug"]; meta(w, a)
        n_intro = len(a["intro"])
        if n_intro != 3: warn(w, "intro %d alinea's" % n_intro)
        for i, p in enumerate(a["intro"]):
            if not 55 <= wc(p) <= 125: warn(w, "intro %d: %d woorden" % (i, wc(p)))
            txt(w + " intro%d" % i, p)
        if "groups" in a or "places" in a:
            for g in a.get("groups", []):
                txt(w + " group", g["text"])
                for s in g["slugs"]:
                    if s not in slugs: warn(w, "group slug onbekend " + s)
            for s in a.get("places", []):
                if s not in slugs: warn(w, "place slug onbekend " + s)
            for g in a.get("gemeenten", []):
                txt(w + " gemeente", g[1])
                if "meestal" not in g[2]: warn(w, "gemeente levertijd zonder meestal: " + g[0])
            if "card" in a and len(a["card"]) > 120: warn(w, "card %d tekens" % len(a["card"]))
            if len(a["faq"]) < 4: warn(w, "hub faq %d" % len(a["faq"]))
        else:
            if len(a["faq"]) != 3: warn(w, "faq %d" % len(a["faq"]))
            if len(a["nearby"]) != 3 or any(s not in slugs for s in a["nearby"]): warn(w, "nearby %r" % (a["nearby"],))
            if a["slug"] in a["nearby"]: warn(w, "nearby bevat zichzelf")
            txt(w + " wijken", a["wijken"])
            if "meestal" not in a["levertijd"]: warn(w, "levertijd zonder 'meestal'")
            if len(a["wijken"].split(",")) < 5: warn(w, "wijken: slechts %d" % len(a["wijken"].split(",")))
        for q, ans in a["faq"]: txt(w + " faq", q + " " + ans, 1)
        sentences(w, a["intro"] + [x[1] for x in a["faq"]])
    for art in list(getattr(m, "ARTICLES", [])) + list(getattr(m, "SERVICE_PAGES", [])) + (getattr(m, "TANKS", {}).get("TANKS", []) if isinstance(getattr(m, "TANKS", None), dict) else []):
        w = f + ":" + art["slug"]; meta(w, art); words = 0; paras = []
        for sec in art["sections"]:
            for p in sec.get("paragraphs", []) + sec.get("bullets", []):
                txt(w + " " + sec["h2"][:18], p); words += wc(p); paras.append(p)
        is_svc = "faq" in art
        lo, hi = (380, 700) if is_svc else (550, 950)
        if not lo <= words <= hi: warn(w, "%d woorden (%s)" % (words, "service" if is_svc else "artikel"))
        if art.get("note"): txt(w + " note", art["note"])
        for q, ans in art.get("faq", []): txt(w + " faq", q + " " + ans, 1)
        if is_svc and len(art["faq"]) != 3: warn(w, "faq %d" % len(art["faq"]))
        for r in art.get("related", []):
            if not any(("/%s/" % r) in a for a in allowed): warn(w, "related onbekend " + r)
        sentences(w, paras)
    for t in getattr(m, "FAQ_TOPICS", []):
        w = f + ":faq:" + t["slug"]; meta(w, t)
        if not 8 <= len(t["items"]) <= 12: warn(w, "items %d" % len(t["items"]))
        for q, ans in t["items"]: txt(w + " item", q + " " + ans, 1)
        for p in t["intro"]: txt(w + " intro", p)
        sentences(w, [x[1] for x in t["items"]])
    for key in ("HOME", "AREA_INDEX", "INFO_INDEX", "SERVICE_INDEX", "FAQ_INDEX", "CONTACT", "ABOUT", "TERMS", "PRIVACY", "SITE_TEXTS", "PAGES_EXTRA"):
        d = getattr(m, key, None)
        if isinstance(d, dict):
            w = f + ":" + key
            if "title" in d: meta(w, d)
            def walk(x, path):
                if isinstance(x, str): txt(path, x, 3)
                elif isinstance(x, dict):
                    for k, v in x.items(): walk(v, path + "." + k)
                elif isinstance(x, (list, tuple)):
                    for i, v in enumerate(x): walk(v, path)
            walk(d, w)
print("modules:", ", ".join(mods), "| problemen:", probs)
sys.exit(1 if probs else 0)
