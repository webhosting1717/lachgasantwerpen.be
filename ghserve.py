#!/usr/bin/env python3
"""Lokale server die GitHub Pages nabootst: gzip, Cache-Control max-age=600, trailing-slash directories, 404.html."""
import gzip, http.server, os, sys, mimetypes
ROOT = sys.argv[1]; PORT = int(sys.argv[2])
class H(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k): super().__init__(*a, directory=ROOT, **k)
    def log_message(self, *a): pass
    def do_GET(self):
        path = self.path.split("?")[0]
        fs = os.path.join(ROOT, path.lstrip("/"))
        if os.path.isdir(fs):
            if not path.endswith("/"):
                self.send_response(301); self.send_header("Location", path + "/"); self.end_headers(); return
            fs = os.path.join(fs, "index.html")
        code = 200
        if not os.path.isfile(fs):
            fs = os.path.join(ROOT, "404.html"); code = 404
        data = open(fs, "rb").read()
        ctype = mimetypes.guess_type(fs)[0] or "application/octet-stream"
        if ctype.startswith("text/") or ctype in ("application/javascript", "application/json", "image/svg+xml", "application/manifest+json"):
            if ctype.startswith("text/"): ctype += "; charset=utf-8"
        gz = "gzip" in self.headers.get("Accept-Encoding", "") and (ctype.startswith("text/") or "javascript" in ctype or "json" in ctype or "svg" in ctype or "xml" in ctype)
        body = gzip.compress(data, 6) if gz else data
        self.send_response(code)
        self.send_header("Content-Type", ctype); self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "max-age=600"); self.send_header("Vary", "Accept-Encoding")
        if gz: self.send_header("Content-Encoding", "gzip")
        self.end_headers(); self.wfile.write(body)
    def do_HEAD(self): self.do_GET()
http.server.ThreadingHTTPServer(("127.0.0.1", PORT), H).serve_forever()
