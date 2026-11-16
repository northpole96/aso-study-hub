#!/usr/bin/env python3
"""Build app/stories.json for the ASO Stories iPhone app.

    python3 tools/build_stories.py

Source: stories/*.txt. Format:
    # book id | Book name | one line about the book
    ## story id | Title | Teaser | mock question indexes (0-based, in tools/gs_mock2_questions.py)
    Paragraphs, with a blank line between them. **bold** marks an exam fact, ⟨CHECK⟩ an unconfirmed one.
    + one "keep" line (the facts to carry into the hall)

The script links each story to its mock questions (number, text, answer), checks that
every mock question is used once, writes app/stories.json and copies it into the app.
Bump nothing by hand: the version is the build time.
"""
import glob, importlib.util, json, os, re, shutil, time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location("qs", os.path.join(ROOT, "tools", "gs_mock2_questions.py"))
qs = importlib.util.module_from_spec(spec); spec.loader.exec_module(qs)
SRC = qs.Q

# question numbers as printed in the mock page
html = open(os.path.join(ROOT, "ASO-GS-Mock-Test-2027-2.html"), encoding="utf-8").read()
i = html.index("var Q = ") + 8; j = html.index("];\n(function(){", i) + 1
PAGE = json.loads(html[i:j])
NUM = {q["q"]: n + 1 for n, q in enumerate(PAGE)}

def curly(t):
    """Straight quotes to curly ones, for the story text."""
    t = re.sub(r'"(?=[\w(])', "\u201c", t).replace('"', "\u201d")
    return re.sub(r"(?<=\w)'", "\u2019", t).replace(" '", " \u2018").replace("'", "\u2019")

def answer(q):
    return q["o"][q["a"] if q["a"] is not None else 0]

books, book, story, used = [], None, None, []
for f in sorted(glob.glob(os.path.join(ROOT, "stories", "*.txt"))):
    for raw in open(f, encoding="utf-8").read().split("\n"):
        line = raw.strip()
        if line.startswith("## "):
            sid, title, teaser, idx = [x.strip() for x in curly(line[3:]).split("|")]
            ids = [int(x) for x in idx.split(",") if x.strip()]
            used += ids
            asked = sorted(({"no": NUM[SRC[k]["q"]], "q": SRC[k]["q"], "a": answer(SRC[k])} for k in ids), key=lambda a: a["no"])
            story = {"id": sid, "title": title, "teaser": teaser, "body": [], "keep": [], "asked": asked}
            book["stories"].append(story)
        elif line.startswith("# "):
            bid, name, sub = [x.strip() for x in curly(line[2:]).split("|")]
            book = {"id": bid, "no": "%02d" % (len(books) + 1), "name": name, "sub": sub, "stories": []}
            books.append(book)
        elif line.startswith("+ "):
            story["keep"].append(curly(line[2:].strip()))
        elif line:
            story["body"].append(curly(line))

assert sorted(used) == list(range(len(SRC))), "mock questions missing or used twice: %s" % sorted(set(range(len(SRC))) ^ set(used))
ids = [s["id"] for b in books for s in b["stories"]]
assert len(ids) == len(set(ids)), "duplicate story id"
words = 0
for b in books:
    for s in b["stories"]:
        assert s["body"] and s["keep"] and s["asked"], s["id"]
        for p in s["body"]:
            assert p.count("**") % 2 == 0, (s["id"], p[:50])
        n = sum(len(re.sub(r"\*\*|⟨CHECK⟩", "", p).split()) for p in s["body"])
        s["min"] = max(2, round(n / 170))
        words += n

out = {"version": int(time.time()), "source": "GS Mock 02", "books": books}
dst = os.path.join(ROOT, "app", "stories.json")
json.dump(out, open(dst, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
app = os.path.join(ROOT, "ios-stories", "ASOStories", "Content")
if os.path.isdir(app):
    shutil.copy(dst, os.path.join(app, "stories.json"))
print("%d books, %d stories, %d words, %d mock questions -> %s" % (len(books), len(ids), words, len(used), dst))
for b in books:
    print(" ", b["no"], b["name"], len(b["stories"]), "stories,", sum(s["min"] for s in b["stories"]), "min")
