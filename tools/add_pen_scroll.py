"""Adds <script src="pen-scroll.js" defer> to every tracked page (idempotent). Run it after any builder that rewrites pages.
Skips ASO-GA-Study-Guide.html (never touched); the hub still injects the script into it when it is opened inside the hub."""
import subprocess, re, os
VERSION = 6   # bump when pen-scroll.js changes: it busts the 10-minute browser cache that made old and new copies mix
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
files = subprocess.run(["git", "ls-files", "*.html"], cwd=ROOT, capture_output=True, text=True).stdout.split()
n = 0
for f in files:
    if f.endswith("ASO-GA-Study-Guide.html"): continue
    p = os.path.join(ROOT, f); t = open(p, encoding="utf-8").read()
    src = ("../pen-scroll.js" if "/" in f else "pen-scroll.js") + "?v=%d" % VERSION
    if "pen-scroll.js" in t:
        t2 = re.sub(r'(src=")(\.\./)?pen-scroll\.js(\?v=\d+)?(")', lambda m: m.group(1) + (m.group(2) or "") + "pen-scroll.js?v=%d" % VERSION + m.group(4), t)
        if t2 != t: open(p, "w", encoding="utf-8").write(t2); n += 1
        continue
    tag = '<script src="%s" defer></script>' % src
    i = t.lower().rfind("</body>")
    t = (t[:i] + tag + "\n" + t[i:]) if i >= 0 else (t.rstrip("\n") + "\n" + tag + "\n")
    open(p, "w", encoding="utf-8").write(t); n += 1
print("patched", n, "of", len(files))
