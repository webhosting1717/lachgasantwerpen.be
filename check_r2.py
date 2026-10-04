import re, sys, importlib.util
sys.path.insert(0, "/tmp/claude-0/-home-user-lachgasantwerpen-be/67fc4ab1-ced0-522e-b4aa-cfe5831e8c00/scratchpad/content/r2")
sys.path.insert(0, "/tmp/claude-0/-home-user-lachgasantwerpen-be/67fc4ab1-ced0-522e-b4aa-cfe5831e8c00/scratchpad/content")
import articles, rotterdam
existing = {a["slug"] for a in rotterdam.ARTICLES}
new = {a["slug"] for a in articles.ARTICLES}
allowed_links = set("""/lachgas-tanks/ /veilig-gebruik/ /lachgas-nachtbezorging/ /lachgas-feest-evenement/ /werkwijze/ /voordelen/ /faq/ /contact/ /bezorggebieden/ /lachgas-informatie/ /privacy/""".split())
allowed_links |= {"/lachgas-informatie/%s/" % s for s in existing | new}
allowed_ext = {"https://www.drugsinfo.nl", "https://www.rijksoverheid.nl", "https://www.trimbos.nl"}
strip = lambda s: re.sub(r"<[^>]+>", "", s)
wc = lambda s: len(strip(s).split())
errors = []
def check_text(where, t):
    tags = re.findall(r"<(/?)(\w+)", t)
    for _, name in tags:
        if name not in ("a", "strong"):
            errors.append(f"{where}: tag <{name}>")
    links = re.findall(r'href="([^"]+)"', t)
    if len(links) > 2:
        errors.append(f"{where}: {len(links)} links")
    for l in links:
        if l not in allowed_links and l not in allowed_ext:
            errors.append(f"{where}: link not allowed {l}")
    if "€" in t or re.search(r"\beuro\b", t, re.I) or "goedkoop" in t.lower() or "ballon" in t.lower():
        errors.append(f"{where}: forbidden word/price")
    if "&" in t and re.search(r"&\w+;", t):
        errors.append(f"{where}: html entity")
def check_page(p, kind):
    s = p["slug"]
    tl, dl = len(p["title"]), len(p["description"])
    total = wc(p["lead"])
    for i, sec in enumerate(p["sections"]):
        for j, para in enumerate(sec["paragraphs"]):
            w = wc(para); total += w
            check_text(f"{s} s{i} p{j}", para)
            if kind == "article" and not (60 <= w <= 120):
                errors.append(f"{s} s{i} p{j}: {w} words")
        for j, b in enumerate(sec["bullets"]):
            total += wc(b); check_text(f"{s} s{i} b{j}", b)
        check_text(f"{s} s{i} h2", sec["h2"])
    check_text(f"{s} note", p["note"])
    for r in p["related"]:
        if r not in existing | new:
            errors.append(f"{s}: related {r} unknown")
    nsec = len(p["sections"])
    if kind == "article":
        if not (4 <= nsec <= 6): errors.append(f"{s}: {nsec} sections")
        if not (600 <= total <= 900): errors.append(f"{s}: {total} words total")
        if not (2 <= len(p["related"]) <= 4): errors.append(f"{s}: related count")
    else:
        if not (3 <= nsec <= 5): errors.append(f"{s}: {nsec} sections")
        if not (400 <= total <= 650): errors.append(f"{s}: {total} words total")
        if len(p["faq"]) != 3: errors.append(f"{s}: faq count")
        for q, a in p["faq"]:
            check_text(f"{s} faq", a)
    if tl > 60: errors.append(f"{s}: title {tl}")
    if not (120 <= dl <= 155): errors.append(f"{s}: description {dl}")
    print(f"{kind:8} {s:38} title={tl:2} desc={dl:3} sections={nsec} words={total}")
for a in articles.ARTICLES: check_page(a, "article")
for p in articles.SERVICE_PAGES: check_page(p, "service")
print("\n".join(errors) if errors else "ALL OK")
