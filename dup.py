#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cross-site en intra-site duplicatie: aandeel zinnen (>=8 woorden) in <main> die ook op een andere site/pagina voorkomen."""
import os,re,sys,html,collections
def pages(repo):
    out={}
    for d,_,fs in os.walk(repo):
        if ".git" in d: continue
        for f in fs:
            if f.endswith(".html") and f!="404.html":
                s=open(os.path.join(d,f),encoding="utf-8").read()
                m=re.search(r"<main.*?</main>",s,re.S); body=m.group(0) if m else s
                body=re.sub(r"<(script|style)\b.*?</\1>","",body,flags=re.S)
                txt=html.unescape(re.sub(r"<[^>]+>"," ",body)); txt=re.sub(r"\s+"," ",txt)
                sents=[x.strip() for x in re.split(r"(?<=[.!?])\s+",txt) if len(x.split())>=8]
                out["/"+os.path.relpath(os.path.join(d,f),repo).replace(os.sep,"/")]=sents
    return out
repos={os.path.basename(r):pages(r) for r in sys.argv[1:]}
# cross-site
allsite={name:collections.Counter(s for p in pg.values() for s in set(p)) for name,pg in repos.items()}
for name,pg in repos.items():
    tot=sum(len(set(p)) for p in pg.values())
    others=set().union(*[set(c) for n,c in allsite.items() if n!=name])
    dup=sum(1 for p in pg.values() for s in set(p) if s in others)
    # intra-site: sentences appearing on >=3 pages of this site
    intra=sum(1 for p in pg.values() for s in set(p) if allsite[name][s]>=3)
    print("%-22s zinnen: %5d | ook op andere site: %4d (%2.0f%%) | op >=3 eigen pagina's: %4d (%2.0f%%)"%(name,tot,dup,100*dup/tot,intra,100*intra/tot))
# meest herhaalde zinnen over alle sites
tot=collections.Counter()
for c in allsite.values(): tot.update({s:1 for s in c})
print("\nZinnen die op meerdere sites staan (voorbeelden):")
for s,n in [x for x in tot.most_common(400) if x[1]>=3][:8]: print("  [%d sites] %s"%(n,s[:110]))
