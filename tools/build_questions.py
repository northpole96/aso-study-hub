#!/usr/bin/env python3
"""Build app/questions.json from questions/*.json (one file per chapter).

Each source question: {"id"?, "q", "o": [correct, wrong, wrong, wrong], "x", "pyq"?, "check"?, "card"?}
The first option is always the right one; the app shuffles them.
A missing id is made from a hash of the chapter and question text.
"""
import datetime, glob, hashlib, json, os, re, shutil, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "questions")
OUT_SITE = os.path.join(ROOT, "app", "questions.json")
OUT_APP = os.path.join(ROOT, "ios-app", "ASOCards", "Content", "questions.json")

def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()

def main():
    cards = json.load(open(os.path.join(ROOT, "app", "cards.json")))
    chapters = {c["id"]: c for c in cards["chapters"]}
    card_ids = {k["id"] for c in cards["chapters"] for p in c["parts"] for k in p["cards"]}
    out, seen_ids, seen_q, errors = [], set(), {}, []
    for path in sorted(glob.glob(os.path.join(SRC, "*.json"))):
        ch = os.path.basename(path).split(".")[0]   # ga-polity.json, ga-polity.2.json …
        if ch not in chapters:
            errors.append(f"{ch}: no chapter with this id in cards.json"); continue
        for i, q in enumerate(json.load(open(path))):
            where = f"{ch}#{i+1}"
            opts = q.get("o", [])
            if len(opts) != 4: errors.append(f"{where}: needs 4 options, has {len(opts)}")
            if len({norm(o) for o in opts}) != len(opts): errors.append(f"{where}: repeated option")
            if not q.get("q") or not q.get("x"): errors.append(f"{where}: missing q or x")
            qid = q.get("id") or hashlib.sha1(f"{ch}|{q['q']}".encode()).hexdigest()[:10]
            if qid in seen_ids: errors.append(f"{where}: duplicate id {qid}")
            seen_ids.add(qid)
            key = norm(q["q"])
            if key in seen_q: errors.append(f"{where}: same question as {seen_q[key]}")
            seen_q[key] = where
            card = q.get("card") or (qid if qid in card_ids else None)
            item = {"id": qid, "ch": ch, "q": q["q"], "o": opts, "x": q["x"]}
            if card: item["card"] = card
            if q.get("pyq"): item["pyq"] = q["pyq"]
            if q.get("check"): item["check"] = True
            out.append(item)
    if errors:
        print("\n".join(errors)); sys.exit(1)
    data = {"version": datetime.datetime.now().strftime("%Y%m%d%H%M"), "questions": out}
    os.makedirs(os.path.dirname(OUT_SITE), exist_ok=True)
    with open(OUT_SITE, "w") as f:
        json.dump(data, f, ensure_ascii=False, separators=(",", ":"))
    shutil.copy(OUT_SITE, OUT_APP)
    books = {}
    for q in out: books[chapters[q["ch"]]["book"]] = books.get(chapters[q["ch"]]["book"], 0) + 1
    print(f"{len(out)} questions {books} → app/questions.json")

if __name__ == "__main__":
    main()
