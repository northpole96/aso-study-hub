#!/usr/bin/env python3
"""Turn the two GA guides into cards for the ASO Cards iOS app.

    python3 tools/build_app_cards.py

Reads   ASO-GA-Reference-Manual.html and ASO-Current-Affairs-2026-Manual.html
Writes  app/cards.json and app/figures/*.png        (published on the hub site; the app checks it for updates)
        ios-app/ASOCards/Content/...               (the same files, built into the app)

Inline markup used inside card text (the app turns it into styled text):
    **bold**     ⟦2025 Q32⟧ = past-paper chip     ⟨CHECK⟩ = unverified tag
"""
import hashlib, json, os, re, shutil, subprocess, sys, tempfile, datetime
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOKS = [
    ("ga", "GA Reference Manual", "ASO-GA-Reference-Manual.html", {"contents"}),
    ("ca", "Current Affairs 2026", "ASO-Current-Affairs-2026-Manual.html", {"contents", "practice"}),
]
OUT_SITE = os.path.join(ROOT, "app")
OUT_APP = os.path.join(ROOT, "ios-app", "ASOCards", "Content")
TEXT_LIMIT = 430          # characters of text per story card
ROWS_PER_TABLE = 6        # table rows per card
ITEMS_PER_LIST = 6        # "asked before" items per card

# ---------------------------------------------------------------- tiny DOM
VOID = {"br", "img", "meta", "link", "input", "hr", "source", "wbr", "path", "circle", "rect", "line",
        "ellipse", "polygon", "polyline", "use", "stop"}


class Node:
    def __init__(self, tag, attrs, parent):
        self.tag, self.a, self.c, self.p = tag, dict(attrs), [], parent

    @property
    def cls(self):
        return self.a.get("class", "").split()

    def kids(self):
        return [k for k in self.c if isinstance(k, Node)]


class Parser(HTMLParser):
    def __init__(self, src):
        super().__init__(convert_charrefs=True)
        self.src, self.root = src, Node("root", [], None)
        self.cur = self.root
        self.svg_start = []

    def handle_starttag(self, t, a):
        n = Node(t, a, self.cur)
        self.cur.c.append(n)
        if t == "svg":
            n.start = self.getpos()
        if t not in VOID:
            self.cur = n

    def handle_startendtag(self, t, a):
        self.cur.c.append(Node(t, a, self.cur))

    def handle_endtag(self, t):
        x = self.cur
        while x is not self.root and x.tag != t:
            x = x.p
        if x is not self.root:
            if t == "svg":
                x.end = self.getpos()
            self.cur = x.p

    def handle_data(self, d):
        self.cur.c.append(d)


def text(n):
    return n if isinstance(n, str) else "".join(text(c) for c in n.c)


def find(n, pred):
    if isinstance(n, str):
        return
    if pred(n):
        yield n
    for c in n.c:
        yield from find(c, pred)


def first(n, pred):
    return next(find(n, pred), None)


def squash(s):
    return re.sub(r"\s+", " ", s).strip()


def rich(n):
    """Inline HTML -> app markup."""
    if isinstance(n, str):
        return n
    cl = n.cls
    if n.tag == "br":
        return "\n"
    if n.tag in ("svg", "script", "style", "input", "button"):
        return ""
    if n.tag == "span" and ("pyq" in cl or "yr" in cl):
        return " ⟦" + squash(text(n)) + "⟧ "
    if ("chk" in cl or "check" in cl) and n.tag == "span":
        return " ⟨CHECK⟩"
    inner = "".join(rich(c) for c in n.c)
    if n.tag in ("b", "strong") and squash(inner):
        return "**" + inner.strip() + "**"
    return inner


def clean(s):
    s = re.sub(r"[ \t\r\f\v]+", " ", s)
    s = re.sub(r" *\n *", "\n", s).strip()
    s = re.sub(r"\*\*\s*\*\*", "", s)
    s = re.sub(r"⟧\s+⟦", "⟧ ⟦", s)
    s = re.sub(r"\s+([,.;:)])", r"\1", s)
    return s


def plain(s):
    s = s.replace("**", "")
    s = re.sub(r"⟦[^⟧]*⟧", "", s)
    s = s.replace("⟨CHECK⟩", "")
    return squash(s)


# ---------------------------------------------------------------- cards
class Book:
    def __init__(self, bid, title, path, skip):
        self.id, self.title, self.path, self.skip = bid, title, path, skip
        src = open(os.path.join(ROOT, path), encoding="utf8").read()
        self.src = src
        self.style = re.search(r"<style>([\s\S]*?)</style>", src).group(1)
        p = Parser(src)
        p.feed(src)
        self.root = p.root
        self.lines = src.split("\n")


class Builder:
    def __init__(self, book, sec, figs):
        self.book, self.sec, self.figs = book, sec, figs
        self.parts, self.part = [], None
        self.buf, self.ids = [], set()

    # parts are the story segments (one h3 each)
    def new_part(self, title, num=""):
        self.flush()
        self.part = {"title": title, "num": num, "cards": []}
        self.parts.append(self.part)

    def add(self, card):
        if self.part is None:
            self.new_part("Overview")
        key = card["type"] + "|" + json.dumps(card, ensure_ascii=False, sort_keys=True)[:400]
        cid = hashlib.sha1((self.sec + "|" + key).encode()).hexdigest()[:10]
        while cid in self.ids:
            cid = hashlib.sha1((cid + "x").encode()).hexdigest()[:10]
        self.ids.add(cid)
        card["id"] = cid
        self.part["cards"].append(card)

    # text blocks pile up into one story card until it is full
    def text_block(self, kind, t):
        t = clean(t)
        if not plain(t):
            return
        size = sum(len(plain(b["t"])) for b in self.buf)
        last = self.buf[-1] if self.buf else None
        lead_in = last and last["k"] == "p" and len(plain(last["t"])) < 90
        if self.buf and size + len(plain(t)) > TEXT_LIMIT and not lead_in:
            self.flush()
        self.buf.append({"k": kind, "t": t})

    def flush(self):
        if self.buf:
            blocks, self.buf = self.buf, []
            self.add({"type": "story", "blocks": blocks})

    def list_items(self, ul):
        return [clean(rich(li)) for li in ul.kids() if li.tag == "li"]

    def ul(self, ul, kind="li"):
        for it in self.list_items(ul):
            self.text_block(kind, it)

    def table(self, tw, title=""):
        t = first(tw, lambda n: n.tag == "table")
        cols = [squash(text(th)) for th in find(t, lambda n: n.tag == "th")]
        rows = []
        for tr in find(t, lambda n: n.tag == "tr"):
            cells = [clean(rich(td)) for td in tr.kids() if td.tag == "td"]
            if cells:
                rows.append(cells)
        if not rows:
            return
        intro = ""
        if self.buf and self.buf[-1]["k"] == "p" and len(plain(self.buf[-1]["t"])) < 140:
            intro = self.buf.pop()["t"]
        self.flush()
        for i in range(0, len(rows), ROWS_PER_TABLE):
            c = {"type": "table", "title": title + (" (cont.)" if i else ""), "cols": cols,
                 "rows": rows[i:i + ROWS_PER_TABLE]}
            if intro and not i: c["intro"] = intro
            self.add(c)

    def box(self, kind, label, blocks):
        self.flush()
        self.add({"type": "box", "kind": kind, "label": label, "blocks": blocks})

    def asked(self, items, label="Asked in past papers"):
        self.flush()
        for i in range(0, len(items), ITEMS_PER_LIST):
            self.add({"type": "asked", "label": label, "items": items[i:i + ITEMS_PER_LIST]})

    def qa(self, q, a, x="", tag="", pyq=""):
        self.flush()
        c = {"type": "qa", "q": clean(q), "a": clean(a)}
        if x: c["x"] = clean(x)
        if tag: c["tag"] = tag
        if pyq: c["pyq"] = pyq
        self.add(c)

    def fact(self, title, body, hot=False):
        self.flush()
        c = {"type": "fact", "title": clean(title), "body": clean(body)}
        if hot: c["hot"] = True
        self.add(c)

    def figure(self, fig, caption=""):
        svg = first(fig, lambda n: n.tag == "svg")
        if svg is None:
            return
        b = self.book
        start, end = svg.start, svg.end
        lines = b.lines[start[0] - 1:end[0]]
        lines[-1] = lines[-1][:end[1]]
        lines[0] = lines[0][start[1]:]
        raw = "\n".join(lines) + "</svg>"
        name = "fig-" + hashlib.sha1(raw.encode()).hexdigest()[:10]
        self.figs[name] = (b, raw)
        label = squash(text(first(fig, lambda n: "fr" in n.cls) or ""))
        fid = squash(text(first(fig, lambda n: "fl" in n.cls) or ""))
        self.flush()
        self.add({"type": "figure", "image": name, "label": label.strip("[] "), "fig": fid,
                  "caption": clean(re.sub(r"^FIG_\d+\s*", "", caption))})


def build_ga_section(b, sec, figs):
    B = Builder(b, b.id + "-" + sec.a["id"], figs)
    title, eyebrow = "", ""
    for ch in sec.kids():
        cl = ch.cls
        if "sectrule" in cl:
            eyebrow = squash(text(first(ch, lambda n: "eyebrow" in n.cls)))
        elif ch.tag == "h2":
            title = squash(text(ch))
        elif ch.tag == "h3":
            t = squash(text(ch))
            m = re.match(r"^(\d+\.\d+)\s+(.*)$", t)
            B.new_part(m.group(2) if m else t, m.group(1) if m else "")
        elif ch.tag == "p":
            B.text_block("p", rich(ch))
        elif ch.tag in ("ul", "ol"):
            B.ul(ch)
        elif "tw" in cl:
            B.table(ch, B.part["title"] if B.part else title)
        elif "figwrap" in cl:
            cap = first(ch, lambda n: "figcap" in n.cls)
            B.figure(first(ch, lambda n: "fig" in n.cls), squash(text(cap)) if cap else "")
        elif ch.tag == "aside" and "box" in cl:
            label = squash(text(first(ch, lambda n: "box-t" in n.cls) or ""))
            if "asked" in cl:
                ul = first(ch, lambda n: n.tag == "ul")
                B.asked(B.list_items(ul) if ul else [], label or "Asked in past papers")
            elif "next" in cl:
                B.new_part("Likely next")
                for d in find(ch, lambda n: n.tag == "details"):
                    s = first(d, lambda n: n.tag == "summary")
                    a = " ".join(clean(rich(p)) for p in d.kids() if p.tag != "summary")
                    B.qa(rich(s), a, tag=title)
            else:
                kind = next((k for k in ("warn", "check", "key", "fix", "tip") if k in cl), "tip")
                blocks = []
                for k in ch.kids():
                    if "box-t" in k.cls: continue
                    if k.tag in ("ul", "ol"):
                        blocks += [{"k": "li", "t": t} for t in B.list_items(k)]
                    else:
                        blocks.append({"k": "p", "t": clean(rich(k))})
                B.box(kind, label, blocks)
    B.flush()
    return title, eyebrow, B.parts


def build_ca_section(b, sec, figs):
    B = Builder(b, b.id + "-" + sec.a["id"], figs)
    title, eyebrow = "", ""
    for ch in sec.kids():
        cl = ch.cls
        if "sh" in cl:
            eyebrow = squash(text(first(ch, lambda n: "eyebrow" in n.cls)))
            title = squash(text(first(ch, lambda n: n.tag == "h2")))
            B.new_part("Overview")
            intro = first(ch, lambda n: "intro" in n.cls)
            for p in (intro.kids() if intro else []):
                B.text_block("p", rich(p))
            fig = first(ch, lambda n: n.tag == "figure")
            if fig is not None:
                B.figure(fig)
        elif "asked" in cl:
            ul = first(ch, lambda n: n.tag == "ul")
            B.asked(B.list_items(ul) if ul else [], "Asked before")
        elif ch.tag == "h3":
            B.new_part(squash(text(ch)))
        elif "slips" in cl:
            for s in ch.kids():
                t = first(s, lambda n: "t" in n.cls)
                d = first(s, lambda n: "d" in n.cls)
                B.fact(rich(t) if t else "", rich(d) if d else "", "hot" in s.cls)
        elif "rows" in cl:
            for r in ch.kids():
                if "head" in r.cls:
                    continue
                cells = r.kids()
                if len(cells) >= 2:
                    B.fact(rich(cells[0]), " · ".join(rich(c) for c in cells[1:]))
        elif "prose" in cl:
            for p in ch.kids():
                B.text_block("p", rich(p))
        elif "method" in cl:
            for m in ch.kids():
                big = first(m, lambda n: "big" in n.cls)
                p = first(m, lambda n: n.tag == "p")
                B.fact(squash(text(big)) if big else "", rich(p) if p else "")
        elif "trap" in cl:
            lab = first(ch, lambda n: n.tag == "b")
            body = clean(rich(ch))
            label = squash(text(lab)).rstrip(".") if lab else "Trap"
            body = re.sub(r"^\*\*" + re.escape(squash(text(lab))) + r"\*\*\s*", "", body) if lab else body
            B.box("warn", label, [{"k": "p", "t": body}])
        elif "likely" in cl:
            B.new_part("Likely next")
            for c in find(ch, lambda n: n.tag == "button" and "card" in n.cls):
                g = lambda k: first(c, lambda n: k in n.cls)
                q, a, x, n_, seal = g("q"), g("a"), g("x"), g("n"), g("seal")
                if q is None or a is None:
                    continue
                B.qa(rich(q), rich(a), rich(x) if x else "", squash(text(n_)) if n_ else title,
                     squash(text(seal)) if seal else "")
        elif ch.tag in ("ul", "ol"):
            B.ul(ch)
        elif ch.tag == "p":
            B.text_block("p", rich(ch))
    B.flush()
    return title, eyebrow, B.parts


# ---------------------------------------------------------------- dates
MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
          "October", "November", "December"]
DATE_RE = re.compile(r"\b(\d{1,2})(?:\s*[–-]\s*\d{1,2})?\s+(" + "|".join(MONTHS) + r")\b(?:,?\s+(\d{4}))?")


def first_sentence(s):
    s = plain(s)
    m = re.search(r"\. [A-Z]", s)
    return s[:m.start() + 1] if m else s


def card_texts(c):
    """(text to search, how to label a date found in it) pairs"""
    t = c["type"]
    if t == "story": return [(b["t"], None) for b in c["blocks"]]
    if t == "fact":
        return [(c["title"], plain(c["title"]) + " — " + first_sentence(c["body"])), (c["body"], plain(c["title"]) + ": ")]
    if t == "box": return [(b["t"], None) for b in c["blocks"]]
    if t == "asked": return [(x, None) for x in c["items"]]
    if t == "table": return [(" — ".join(r), plain(" — ".join(r))) for r in c["rows"]]
    return []


def extract_dates(chapters):
    out, seen = [], set()
    for ch in chapters:
        for pi, part in enumerate(ch["parts"]):
            for c in part["cards"]:
                for t, label in card_texts(c):
                    p = plain(t)
                    for m in DATE_RE.finditer(p):
                        d, mon, y = int(m.group(1)), MONTHS.index(m.group(2)) + 1, m.group(3)
                        if d < 1 or d > 31:
                            continue
                        # the sentence (or · piece) around the date
                        s = max(p.rfind(". ", 0, m.start()), p.rfind(" · ", 0, m.start()))
                        s = 0 if s < 0 else s + 2
                        e = [x for x in (p.find(". ", m.end()), p.find(" · ", m.end())) if x > 0]
                        e = min(e) + 1 if e else len(p)
                        snip = p[s:e].strip(" ·")
                        if label and label.endswith(": "):
                            snip = label + snip
                        elif label:
                            snip = label
                        if len(snip) > 170:
                            snip = snip[:167].rsplit(" ", 1)[0] + "…"
                        key = (d, mon, snip[:60])
                        if key in seen:
                            continue
                        seen.add(key)
                        out.append({"d": d, "m": mon, "y": int(y) if y else None, "t": snip,
                                    "chapter": ch["id"], "part": part["title"], "card": c["id"]})
    out.sort(key=lambda x: (x["m"], x["d"], x["y"] or 0))
    return out


# ---------------------------------------------------------------- figures
RENDER_SWIFT = os.path.join(ROOT, "tools", "render_figures.swift")


def render_figures(figs, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    todo = {k: v for k, v in figs.items() if not os.path.exists(os.path.join(out_dir, k + ".png"))}
    for f in os.listdir(out_dir):
        if f.endswith(".png") and f[:-4] not in figs:
            os.remove(os.path.join(out_dir, f))
    if not todo:
        return
    fonts = os.path.join(ROOT, "ios-app", "ASOCards", "Fonts")
    face = "".join(
        "@font-face{font-family:'%s';src:url('file://%s/%s');font-weight:%s}" % (fam, fonts, f, w)
        for fam, f, w in [("IBM Plex Mono", "IBMPlexMono-Regular.ttf", 400), ("IBM Plex Mono", "IBMPlexMono-Medium.ttf", 500),
                          ("Silkscreen", "Silkscreen-Regular.ttf", 400), ("EB Garamond", "EBGaramond-Regular.ttf", 400)])
    tmp = tempfile.mkdtemp(prefix="asofig")
    for name, (book, raw) in todo.items():
        page = ("<!doctype html><meta charset=utf-8><style>%s\n%s\n"
                ":root{color-scheme:light}html,body{margin:0;background:#fff}figure.fig{border:0!important;background:#fff!important;"
                "padding:0!important;margin:0!important;max-width:none!important;width:640px}"
                ".fig>span{display:none!important}</style><body><figure class=\"fig\">%s</figure>"
                % (face, book.style, raw))
        open(os.path.join(tmp, name + ".html"), "w", encoding="utf8").write(page)
    print("rendering %d figures…" % len(todo))
    subprocess.run(["swift", RENDER_SWIFT, tmp, out_dir], check=True)
    shutil.rmtree(tmp, ignore_errors=True)


# ---------------------------------------------------------------- main
def main():
    chapters, figs = [], {}
    for bid, btitle, path, skip in BOOKS:
        b = Book(bid, btitle, path, skip)
        for sec in find(b.root, lambda n: n.tag == "section" and n.a.get("id")):
            if sec.a["id"] in skip:
                continue
            fn = build_ga_section if bid == "ga" else build_ca_section
            title, eyebrow, parts = fn(b, sec, figs)
            parts = [p for p in parts if p["cards"]]
            if not parts:
                continue
            m = re.search(r"(\d+)", eyebrow)
            asked = re.search(r"·\s*([^·]+?)\s*$", eyebrow)
            chapters.append({"id": bid + "-" + sec.a["id"], "book": bid, "title": title,
                             "no": m.group(1) if m else "", "eyebrow": eyebrow,
                             "note": asked.group(1).strip(" ·") if (asked and bid == "ga") else "", "parts": parts})
    data = {"version": datetime.datetime.now().strftime("%Y%m%d%H%M"),
            "books": [{"id": b[0], "title": b[1], "source": b[2]} for b in BOOKS],
            "chapters": chapters, "dates": extract_dates(chapters)}
    os.makedirs(OUT_SITE, exist_ok=True)
    render_figures(figs, os.path.join(OUT_SITE, "figures"))
    js = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    open(os.path.join(OUT_SITE, "cards.json"), "w", encoding="utf8").write(js)
    # copy into the app bundle
    if os.path.isdir(os.path.dirname(OUT_APP)):
        if os.path.isdir(OUT_APP):
            shutil.rmtree(OUT_APP)
        os.makedirs(OUT_APP)
        shutil.copy(os.path.join(OUT_SITE, "cards.json"), OUT_APP)
        for f in os.listdir(os.path.join(OUT_SITE, "figures")):
            shutil.copy(os.path.join(OUT_SITE, "figures", f), OUT_APP)
    n = {}
    for ch in chapters:
        for p in ch["parts"]:
            for c in p["cards"]:
                n[c["type"]] = n.get(c["type"], 0) + 1
    print("chapters %d · parts %d · cards %d %s · dates %d · figures %d · %d KB"
          % (len(chapters), sum(len(c["parts"]) for c in chapters), sum(n.values()), n,
             len(data["dates"]), len(figs), len(js) // 1024))


if __name__ == "__main__":
    main()
