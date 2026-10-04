#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Controleer de fase-2-content: lengtes, verboden inhoud, links, slugs."""
import importlib.util, os, re, sys
R2 = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "content", "r2")
ALLOWED = {"/lachgas-tanks/", "/veilig-gebruik/", "/lachgas-nachtbezorging/", "/lachgas-feest-evenement/", "/werkwijze/", "/voordelen/", "/faq/", "/contact/",
           "/bezorggebieden/", "/lachgas-informatie/", "/privacy/", "/lachgas-informatie/wat-is-lachgas/", "/lachgas-informatie/lachgas-en-vitamine-b12/",
           "/lachgas-informatie/lachgas-tank-bewaren-en-vervoeren/", "/lachgas-informatie/is-lachgas-legaal-in-nederland/", "/lachgas-informatie/lachgas-in-het-verkeer/",
           "/lachgas-bestellen/zuid-holland/", "/lachgas-spoedbezorging/", "/lachgas-bezorgen-weekend/", "/lachgas-bestellen-zonder-account/"}
SLUGS = set("""centrum noord kralingen-crooswijk delfshaven feijenoord ijsselmonde charlois prins-alexander hillegersberg-schiebroek overschie hoogvliet hoek-van-holland
schiedam vlaardingen capelle-aan-den-ijssel spijkenisse barendrecht ridderkerk berkel-en-rodenrijs maassluis delft zoetermeer krimpen-aan-den-ijssel nieuwerkerk-aan-den-ijssel rhoon
hellevoetsluis brielle rozenburg dordrecht zwijndrecht gouda pijnacker bergschenhoek bleiswijk hendrik-ido-ambacht naaldwijk oud-beijerland nesselande ommoord zevenkamp kop-van-zuid blijdorp pernis lombardijen""".split())
NEW_ART = {"lachgas-en-alcohol", "lachgas-bijwerkingen-en-eerste-hulp", "lachgas-bezorgservice-kiezen", "lachgastank-2kg-4kg-of-10kg", "lachgas-en-het-milieu", "lachgas-afkicken-en-hulp"}
for a in NEW_ART:
    ALLOWED.add("/lachgas-informatie/%s/" % a)
for s in SLUGS:
    ALLOWED.add("/lachgas-bestellen/%s/" % s)
BAD = [r"€", r"\beuro\b", r"\bbel ons\b", r"\bbellen\b", r"\+31 ?6", r"06-?\d{8}", r"nachtkoerier", r"247gas", r"lachgas010", r"partygas", r"goedkoopst", r"\bonschuldig\b",
       r"&rsquo;|&amp;|&#", r"<(?!/?(a|strong)\b)[a-z]"]
def load(n):
    p = os.path.join(R2, n); spec = importlib.util.spec_from_file_location(n[:-3], p); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
probs = 0
def warn(where, msg):
    global probs; probs += 1; print("%-45s %s" % (where, msg))
def check_text(where, t):
    for b in BAD:
        if re.search(b, t, re.I):
            warn(where, "VERBODEN %r: %s" % (b, re.search(b, t, re.I).group(0)))
    for h in re.findall(r'href="([^"]+)"', t):
        if h.startswith("/") and h not in ALLOWED:
            warn(where, "LINK onbekend " + h)
        elif h.startswith("http") and not re.match(r"https://www\.(drugsinfo|rijksoverheid|trimbos)\.nl", h):
            warn(where, "EXTERNE link " + h)
    if t.count("<a ") > 2:
        warn(where, "%d links in een alinea" % t.count("<a "))
def check_meta(where, d):
    if len(d["title"]) > 60: warn(where, "TITLE %d" % len(d["title"]))
    if not 120 <= len(d["description"]) <= 155: warn(where, "DESC %d" % len(d["description"]))
    check_text(where + " title", d["title"]); check_text(where + " desc", d["description"])
    for k in ("h1", "lead"):
        check_text(where + " " + k, d[k])
seen_sent = {}
for f in sorted(os.listdir(R2)):
    if not f.endswith(".py"): continue
    m = load(f)
    for a in getattr(m, "AREAS", []):
        w = f + ":" + a["slug"]
        if a["slug"] not in SLUGS: warn(w, "slug onbekend")
        check_meta(w, a)
        if len(a["intro"]) != 3: warn(w, "intro %d alinea's" % len(a["intro"]))
        for i, p in enumerate(a["intro"]):
            n = len(re.sub(r"<[^>]+>", "", p).split())
            if not 55 <= n <= 120: warn(w, "intro %d: %d woorden" % (i, n))
            check_text(w + " intro%d" % i, p)
        if len(a["faq"]) != 3: warn(w, "faq %d" % len(a["faq"]))
        for q, ans in a["faq"]:
            check_text(w + " faq", q + " " + ans)
        if len(a["nearby"]) != 3 or any(s not in SLUGS for s in a["nearby"]): warn(w, "nearby %r" % a["nearby"])
        if a["slug"] in a["nearby"]: warn(w, "nearby bevat zichzelf")
        check_text(w + " wijken", a["wijken"])
        if "meestal" not in a["levertijd"]: warn(w, "levertijd zonder 'meestal'")
        for p in a["intro"] + [x[1] for x in a["faq"]]:
            for sent in re.split(r"(?<=[.!?])\s+", re.sub(r"<[^>]+>", "", p)):
                if len(sent) > 60:
                    if sent in seen_sent and seen_sent[sent] != w: warn(w, "DUBBELE ZIN ook in %s: %s" % (seen_sent[sent], sent[:60]))
                    seen_sent[sent] = w
    for art in list(getattr(m, "ARTICLES", [])) + list(getattr(m, "SERVICE_PAGES", [])):
        w = f + ":" + art["slug"]
        check_meta(w, art)
        words = 0
        for sec in art["sections"]:
            for p in sec.get("paragraphs", []) + sec.get("bullets", []):
                check_text(w + " " + sec["h2"][:20], p); words += len(re.sub(r"<[^>]+>", "", p).split())
        if art.get("note"): check_text(w + " note", art["note"])
        for q, ans in art.get("faq", []): check_text(w + " faq", q + " " + ans)
        for r in art.get("related", []):
            if r not in NEW_ART and not os.path.exists("/home/user/lachgasrotterdam.nl/lachgas-informatie/%s/index.html" % r): warn(w, "related onbekend " + r)
        print("%-45s %d woorden, %d secties" % (w, words, len(art["sections"])))
    if hasattr(m, "REGIO"):
        R = m.REGIO; check_meta("REGIO", R)
        for p in R["intro"]: check_text("REGIO intro", p)
        for g in R["groups"]:
            check_text("REGIO " + g["h2"], g["text"])
            for s in g["slugs"]:
                if s not in SLUGS: warn("REGIO", "slug onbekend " + s)
        for q, ans in R["faq"]: check_text("REGIO faq", q + " " + ans)
    if hasattr(m, "HOME"):
        H = m.HOME
        for k in ("regio_text", "compare_text"): check_text("HOME " + k, H[k])
        for r in H["compare_rows"]: check_text("HOME row", " ".join(r))
        for q, ans in H["faq_extra"]: check_text("HOME faq", q + " " + ans)
        print("HOME: %d rijen, %d faq" % (len(H["compare_rows"]), len(H["faq_extra"])))
print("problemen:", probs)
