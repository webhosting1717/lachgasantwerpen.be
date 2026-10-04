#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Valideer een site-repo: HTML-tagbalans, JSON-LD, interne links, meta-lengtes, Tailwind-klassen, dubbele ids."""
import html
import json
import os
import re
import sys
from html.parser import HTMLParser

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}


class P(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.errs = []
        self.classes = set()
        self.ids = []

    def handle_starttag(self, t, attrs):
        for k, v in attrs:
            if k == "class" and v:
                self.classes.update(v.split())
            if k == "id" and v:
                self.ids.append(v)
        if t not in VOID:
            self.stack.append(t)

    def handle_startendtag(self, t, attrs):
        for k, v in attrs:
            if k == "class" and v:
                self.classes.update(v.split())

    def handle_endtag(self, t):
        if t in VOID:
            return
        if not self.stack or self.stack[-1] != t:
            self.errs.append((t, self.stack[-3:]))
            if t in self.stack:
                while self.stack and self.stack[-1] != t:
                    self.stack.pop()
        if self.stack and self.stack[-1] == t:
            self.stack.pop()


def css_classes(repo):
    cls = set()
    srcs = []
    for f in ("css/tailwind.css", "css/site.css"):
        p = os.path.join(repo, f)
        if os.path.exists(p):
            srcs.append(open(p, encoding="utf-8").read())
    if not srcs:  # geen losse CSS-bestanden: inline <style> van de homepage gebruiken
        p = os.path.join(repo, "index.html")
        if os.path.exists(p):
            srcs += re.findall(r"<style>(.*?)</style>", open(p, encoding="utf-8").read(), re.S)
    for css in srcs:
        for m in re.finditer(r"\.((?:\\.|[A-Za-z0-9_-])+)", css):
            cls.add(m.group(1).replace("\\", ""))
    return cls


def main(repo, changed_only=None):
    known = css_classes(repo)
    files = sorted(os.path.join(d, f) for d, _, fs in os.walk(repo) if ".git" not in d for f in fs if f.endswith(".html"))
    existing = set()
    for f in files:
        rel = "/" + os.path.relpath(f, repo).replace(os.sep, "/")
        existing.add(rel)
        if rel.endswith("/index.html"):
            existing.add(rel[:-len("index.html")])
    for d, _, fs in os.walk(repo):
        if ".git" in d:
            continue
        for f in fs:
            existing.add("/" + os.path.relpath(os.path.join(d, f), repo).replace(os.sep, "/"))
    problems = 0
    unknown_total = {}
    for f in files:
        rel = os.path.relpath(f, repo)
        s = open(f, encoding="utf-8").read()
        p = P()
        p.feed(s)
        notes = []
        if p.errs or p.stack:
            notes.append("TAGERR %s %s" % (p.errs[:2], p.stack[:3]))
        for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
            try:
                json.loads(m.group(1).replace("<\\/", "</"))
            except Exception as e:
                notes.append("JSONERR %s" % e)
        t = re.search(r"<title>(.*?)</title>", s, re.S)
        ds = re.search(r'name="description" content="([^"]*)"', s)
        tl = len(html.unescape(t.group(1).strip())) if t else 0
        dl = len(html.unescape(ds.group(1))) if ds else 0
        if tl > 60 or tl == 0:
            notes.append("TITLE %d" % tl)
        if dl > 160 or dl < 50:
            notes.append("DESC %d" % dl)
        if "noindex" not in s:
            if 'rel="canonical"' not in s:
                notes.append("NOCANON")
            if 'hreflang=' not in s:
                notes.append("NOHREFLANG")
        if 'rel="stylesheet" href="/css/' in s:
            notes.append("CSS-LINK")
        ids = p.ids
        dup = {i for i in ids if ids.count(i) > 1}
        if dup:
            notes.append("DUPID %s" % sorted(dup)[:3])
        for m in re.finditer(r'(?:href|src)="(/[^"#?]*)', s):
            h = m.group(1)
            if h not in existing and (h + "/") not in existing and not h.startswith("/#"):
                notes.append("BROKEN " + h)
        unknown = {c for c in p.classes if c not in known and not c.startswith(("animate-", "no-scroll"))}
        if unknown:
            for c in unknown:
                unknown_total.setdefault(c, set()).add(rel)
        if notes:
            problems += 1
            print("%-55s %s" % (rel, " | ".join(dict.fromkeys(notes))))
    if unknown_total:
        print("ONBEKENDE KLASSEN (niet in tailwind.css/site.css):")
        for c, fs in sorted(unknown_total.items()):
            print("   %-40s in %d bestanden, bijv. %s" % (c, len(fs), sorted(fs)[0]))
    print("bestanden: %d, bestanden met problemen: %d, onbekende klassen: %d" % (len(files), problems, len(unknown_total)))
    return problems


if __name__ == "__main__":
    sys.exit(1 if main(sys.argv[1]) else 0)
