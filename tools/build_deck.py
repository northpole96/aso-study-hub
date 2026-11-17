#!/usr/bin/env python3
"""Build app/deck.json, the recall cards for the ASO Stories iPhone app.

    python3 tools/build_deck.py

Source: cards/*.txt. Format:
    # topic id | Topic name
    ## story id            (a story in stories/*.txt; the cards under it grew from that story)
    = key                  (cards under one key are about the same fact, so the app keeps them apart)
    Q question             (no options: the reader answers from memory)
    A answer
    N note                 (optional: one or two lines shown under the answer)
    F title | text         (a fact card)
    D year | title | text  (a date card)
    S title | text         (a short tale that stands alone)
**bold** marks an exam fact, ⟨CHECK⟩ an unconfirmed one.

The script checks the cards (lengths, story ids, repeats), writes app/deck.json and copies
it into the app. A card's id comes from its question or title, so progress on the phone
survives a rebuild unless that text changes. The version is the build time.
"""
import glob, hashlib, json, os, re, shutil, time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIMIT = {"q": 30, "a": 14, "n": 34, "f": 58, "d": 44, "s": 98, "title": 9}

def curly(t):
    t = re.sub(r'"(?=[\w(.])', "“", t).replace('"', "”")
    return re.sub(r"(?<=\w)'", "’", t).replace(" '", " ‘").replace("'", "’")

def words(t):
    return len(re.sub(r"\*\*|⟨CHECK⟩", "", t).split())

stories = {s["id"] for b in json.load(open(os.path.join(ROOT, "app", "stories.json"), encoding="utf-8"))["books"] for s in b["stories"]}
topics, cards, seen = [], [], set()
topic = story = key = None

def add(kind, where, **f):
    assert topic and story and key, "card before a topic, story or key: %s" % where
    base = f.get("q") or (f.get("year", "") + f["title"])
    cid = kind + hashlib.md5((topic + "|" + base).encode("utf-8")).hexdigest()[:9]
    assert cid not in seen, "same card twice: %s" % base
    seen.add(cid)
    for k, v in f.items():
        if k != "year":
            assert v.count("**") % 2 == 0, "odd ** in %s" % where
    card = {"id": cid, "t": kind, "topic": topic, "story": story, "k": topic + "/" + key}
    card.update({k: curly(v) for k, v in f.items()})
    cards.append(card)
    return card

def fits(text, what, where):
    assert words(text) <= LIMIT[what], "%s is %d words (limit %d): %s" % (what, words(text), LIMIT[what], where)

for path in sorted(glob.glob(os.path.join(ROOT, "cards", "*.txt"))):
    last = None
    for n, raw in enumerate(open(path, encoding="utf-8").read().split("\n"), 1):
        line = raw.strip()
        where = "%s:%d" % (os.path.basename(path), n)
        if not line:
            continue
        if line.startswith("## "):
            story = line[3:].strip(); key = None
            assert story in stories, "no such story: %s (%s)" % (story, where)
        elif line.startswith("# "):
            tid, name = [x.strip() for x in line[2:].split("|")]
            if tid not in [t["id"] for t in topics]:
                topics.append({"id": tid, "name": name})
            topic = tid; story = key = None
        elif line.startswith("= "):
            key = line[2:].strip()
        elif line.startswith("Q "):
            fits(line[2:], "q", where)
            last = add("q", where, q=line[2:].strip(), a="")
        elif line.startswith("A "):
            assert last and last["t"] == "q" and not last["a"], "A without Q: %s" % where
            fits(line[2:], "a", where)
            last["a"] = curly(line[2:].strip())
        elif line.startswith("N "):
            assert last and last["t"] == "q" and last["a"] and "n" not in last, "N without Q and A: %s" % where
            fits(line[2:], "n", where)
            last["n"] = curly(line[2:].strip())
        elif line[:2] in ("F ", "S "):
            title, body = [x.strip() for x in line[2:].split("|")]
            kind = line[0].lower()
            fits(title, "title", where); fits(body, kind, where)
            last = add(kind, where, title=title, body=body)
        elif line.startswith("D "):
            year, title, body = [x.strip() for x in line[2:].split("|")]
            assert re.fullmatch(r"\d{4}", year), "bad year: %s" % where
            fits(title, "title", where); fits(body, "d", where)
            last = add("d", where, year=year, title=title, body=body)
        else:
            raise SystemExit("cannot read %s: %s" % (where, line[:60]))

for c in cards:
    if c["t"] == "q":
        assert c["a"], "question without an answer: %s" % c["q"]

out = {"version": int(time.time()), "topics": topics, "cards": cards}
dst = os.path.join(ROOT, "app", "deck.json")
json.dump(out, open(dst, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
app = os.path.join(ROOT, "ios-stories", "ASOStories", "Content")
if os.path.isdir(app):
    shutil.copy(dst, os.path.join(app, "deck.json"))
kinds = {"q": "questions", "f": "facts", "d": "dates", "s": "tales"}
print("%d cards -> %s" % (len(cards), dst))
for t in topics:
    mine = [c for c in cards if c["topic"] == t["id"]]
    print(" ", t["name"] + ":", ", ".join("%d %s" % (sum(c["t"] == k for c in mine), v) for k, v in kinds.items()))
    for s in sorted({c["story"] for c in mine}, key=[c["story"] for c in mine].index):
        print("    %-14s %s" % (s, " ".join("%s%d" % (k, sum(c["t"] == k and c["story"] == s for c in mine)) for k in kinds)))
long = sorted(cards, key=lambda c: -words(c.get("body", c.get("q", "") + c.get("a", "") + c.get("n", ""))))[:3]
print("  longest:", ", ".join(c["id"] for c in long))
