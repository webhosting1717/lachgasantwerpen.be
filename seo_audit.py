#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Technische SEO-audit per repo: headings, alt, canonical, links, orphans, dubbele titles, woordaantal, noindex."""
import os, re, sys, html, json, collections
from html.parser import HTMLParser
class P(HTMLParser):
    def __init__(s): super().__init__(); s.h=[]; s.imgs=[]; s.links=[]; s.text=[]; s.cur=None; s.skip=0
    def handle_starttag(s,t,a):
        a=dict(a)
        if t in ("h1","h2","h3"): s.cur=t; s.h.append([t,""])
        if t=="img": s.imgs.append(a)
        if t=="a" and a.get("href"): s.links.append(a["href"])
        if t in ("script","style","nav","footer","header"): s.skip+=1
    def handle_endtag(s,t):
        if t in ("h1","h2","h3"): s.cur=None
        if t in ("script","style","nav","footer","header") and s.skip: s.skip-=1
    def handle_data(s,d):
        if s.cur and s.h: s.h[-1][1]+=d
        if not s.skip: s.text.append(d)
def audit(repo):
    pages={}
    for d,_,fs in os.walk(repo):
        if ".git" in d: continue
        for f in fs:
            if f.endswith(".html"):
                rel="/"+os.path.relpath(os.path.join(d,f),repo).replace(os.sep,"/")
                url=rel[:-len("index.html")] if rel.endswith("/index.html") else rel
                pages[url]=open(os.path.join(d,f),encoding="utf-8").read()
    inbound=collections.Counter(); titles=collections.Counter(); descs=collections.Counter(); issues=[]; words={}
    sitemap=set(re.findall(r"<loc>https?://[^/]+(/[^<]*)</loc>", open(os.path.join(repo,"sitemap.xml")).read()))
    for url,s in pages.items():
        p=P(); p.feed(s)
        noindex="noindex" in s
        t=re.search(r"<title>(.*?)</title>",s,re.S); t=html.unescape(t.group(1).strip()) if t else ""
        dm=re.search(r'name="description" content="([^"]*)"',s); dsc=html.unescape(dm.group(1)) if dm else ""
        can=re.search(r'rel="canonical" href="([^"]+)"',s); can=can.group(1) if can else ""
        h1=[x for x in p.h if x[0]=="h1"]
        if not noindex:
            titles[t]+=1; descs[dsc]+=1
            if len(h1)!=1: issues.append((url,"H1 x%d"%len(h1)))
            if can and not can.endswith(url): issues.append((url,"CANONICAL "+can))
            if url not in sitemap and url!="/404.html": issues.append((url,"NIET IN SITEMAP"))
            if 'property="og:image"' not in s: issues.append((url,"GEEN OG:IMAGE"))
            if '"@type":"BreadcrumbList"' not in s and url!="/": issues.append((url,"GEEN BREADCRUMB-SCHEMA"))
        for a in p.imgs:
            if not a.get("alt") and a.get("alt")!="": issues.append((url,"IMG ZONDER ALT "+a.get("src","")[:50]))
            if a.get("loading")!="lazy" and "fetchpriority" not in a and "hero" not in a.get("src",""): pass
            if not a.get("width") or not a.get("height"): issues.append((url,"IMG ZONDER WIDTH/HEIGHT "+a.get("src","")[:50]))
        for l in p.links:
            if l.startswith("/") and not l.startswith("//"):
                h=l.split("#")[0].split("?")[0]
                if h and not h.endswith("/") and "." not in h.split("/")[-1]: issues.append((url,"LINK ZONDER SLASH "+h))
                if h!=url: inbound[h]+=1
            if l.startswith("http") and "wa.me" not in l and "mailto" not in l and 'rel="noopener' not in s: pass
        txt=" ".join(p.text); words[url]=len(re.findall(r"\w+",txt))
    for url in pages:
        if url not in ("/404.html",) and "noindex" not in pages[url] and inbound.get(url,0)==0: issues.append((url,"WEES (0 inbound)"))
        elif inbound.get(url,0)<=2 and url!="/" and "noindex" not in pages[url]: issues.append((url,"ZWAK GELINKT (%d inbound)"%inbound.get(url,0)))
    for t,n in titles.items():
        if n>1: issues.append(("*","DUBBELE TITLE x%d: %s"%(n,t[:60])))
    for t,n in descs.items():
        if n>1: issues.append(("*","DUBBELE DESCRIPTION x%d"%n))
    thin=[(u,w) for u,w in words.items() if w<350 and "noindex" not in pages[u]]
    print("== %s: %d pagina's, %d in sitemap, woorden gem. %d, dun (<350 w): %s"%(os.path.basename(repo),len(pages),len(sitemap),sum(words.values())//len(words),sorted(thin,key=lambda x:x[1])[:8]))
    c=collections.Counter(i[1].split(" ")[0]+" "+i[1].split(" ")[1] if i[1].startswith(("LINK","IMG","GEEN","DUBBELE","ZWAK","NIET","WEES")) else i[1] for i in issues)
    for k,v in c.most_common(): print("   %-32s %d"%(k,v))
    for u,i in issues:
        if i.startswith(("H1","CANONICAL","WEES","NIET")): print("     ",u,i)
    # robots/404/redirect
    print("   404.html noindex:", "noindex" in pages.get("/404.html",""), "| robots:", open(os.path.join(repo,"robots.txt")).read().replace("\n"," | "))
    return issues
for r in sys.argv[1:]: audit(r)
