"""2015 General Awareness and English Paper III from the Udyam IAS books, tagged by hand (topic, family) for the PYQ Bank and the Analysis page.
The skill's own data (mock drawing) does not use 2015 for these two papers yet. Keys and notes are the publisher's, not OPSC's.
GA 2015 question numbers are the book's order (it sorts the paper by topic and restarts its own numbers), not the paper's.
English 2015 numbers are the paper's (the book keeps the paper order)."""
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import udyam_ga_en as U

GA = {}
def _g(ks, topic, fam):
    for k in ks: GA[k] = (topic, fam)
_g([2, 5, 6, 10, 11, 13, 87, 99], "cur", "sports")
_g([1, 4], "cur", "awards-govt"); _g([3], "cur", "new-appointments"); _g([7, 8, 82, 86, 91, 92, 97], "cur", "culture")
_g([9, 15], "cur", "books"); _g([12], "cur", "awards-arts"); _g([14], "cur", "world-news"); _g([42], "cur", "schemes"); _g([43], "cur", "infrastructure")
_g([16], "his", "inc-sessions"); _g([17, 18, 23], "his", "leaders"); _g([19], "his", "viceroys"); _g([20], "his", "education-commissions")
_g([21], "his", "acts"); _g([22], "his", "gandhi-movements"); _g([76], "his", "organisations"); _g([81], "his", "british-expansion")
_g([83, 84, 85, 95], "his", "medieval"); _g([96], "his", "culture")
_g([24], "pol", "dpsp"); _g([25], "pol", "president-vp"); _g([26, 88], "pol", "judiciary"); _g([27], "pol", "money-bill"); _g([28], "pol", "emergency")
_g([29], "wge", "oceans"); _g([30], "wge", "rocks-interior"); _g([31], "wge", "volcanoes-quakes"); _g([32], "wge", "earth-motions")
_g([33], "wge", "atmosphere"); _g([90, 94], "wge", "landforms")
_g([34, 79], "ige", "borders-states")
_g([35], "eco", "planning"); _g([36, 98], "eco", "banking"); _g([37, 38], "eco", "industry-places"); _g([39, 41], "eco", "census-population")
_g([40], "eco", "poverty-schemes"); _g([44], "eco", "economics-terms")
_g([45, 49, 50, 51, 52, 53, 55, 56, 57, 60, 61, 62, 63, 64, 65, 67, 68, 69, 71], "sci", "everyday-science")
_g([46], "sci", "inventions"); _g([47], "sci", "space-world"); _g([48, 58, 59, 66], "sci", "diseases"); _g([89, 93], "sci", "nobel"); _g([77], "sci", "isro-missions")
_g([54], "env", "renewable-energy"); _g([70], "env", "parks-reserves")
_g([72], "ins", "hq-cities"); _g([73], "ins", "finance-trade"); _g([75], "ins", "groupings"); _g([78], "ins", "reports-publishers")
_g([74], "odi", "news-projects"); _g([80], "odi", "history"); _g([100], "odi", "physiography")
assert sorted(GA) == list(range(1, 101)), sorted(set(range(1, 101)) - set(GA))

EN = {}
def _e(ks, topic, fam):
    for k in ks: EN[k] = (topic, fam)
_e(list(range(1, 6)) + list(range(56, 61)), "pos", "identify")
_e([6, 11, 14], "ten", "wish-unreal"); _e([7], "ten", "present-simple"); _e([8], "ten", "present-continuous"); _e([9, 13], "ten", "past-simple")
_e([10], "ten", "past-perfect"); _e([12, 15], "ten", "conditionals")
_e([16, 18, 21, 22, 24], "prep", "fixed-verb"); _e([19, 20], "prep", "fixed-adjective"); _e([17, 23], "prep", "phrase-prep"); _e([25], "prep", "time-place")
_e([26, 27], "adv", "placement"); _e([28], "adv", "intensifiers"); _e([29], "adv", "degree"); _e([30], "adv", "adj-vs-adv")
_e([31], "sva", "singular-subject"); _e([32], "sva", "few-some"); _e([33], "sva", "number-of"); _e([34], "sva", "as-well-as"); _e([35], "sva", "collective")
_e(list(range(36, 41)), "err", "pick-correct"); _e(list(range(41, 46)), "err", "spot-segment")
_e([46], "art", "determiners"); _e([47, 48, 49, 50], "adv", "connectors")
_e([51], "art", "a-an-sound"); _e([52, 55], "art", "the-specific"); _e([53], "art", "determiners"); _e([54], "art", "zero-article")
_e(list(range(61, 66)), "prep", "phrasal-verbs"); _e(list(range(66, 76)), "voc", "one-word"); _e(list(range(76, 86)), "ant", "word")
_e([86, 91, 92], "com", "passage-inference"); _e([87, 88, 89, 90], "com", "passage-detail")
_e([93, 94, 95, 96], "voc", "idioms-phrases"); _e([97, 98, 99, 100], "voc", "word-forms")
assert sorted(EN) == list(range(1, 101))
EN_PASSAGE = {(86, 88): 0, (89, 90): 1, (91, 92): 2}

def clean(t):
    t = t.replace("‐ ", "").replace("‐", "-").replace("‑", "-")
    t = re.sub(r"\bJoin ASO Test Series.*?tinyurl\.com/\S+", "", t)
    t = re.sub(r"\b([TW]) (?=[a-z])", r"\1", t)
    return re.sub(r"[ \t]+", " ", t).strip()

def note(w, limit=420):
    w = clean(re.sub(r"^Answer\s*:\s*[A-E]?\s*-?\s*", "", w)).replace("•", "").strip()
    w = re.sub(r"\s+", " ", w)
    if len(w) > limit:
        cut = w[:limit]; i = max(cut.rfind(". "), cut.rfind("; "))
        w = cut[:i + 1] if i > 150 else cut.rsplit(" ", 1)[0] + "..."
    return "Udyam book: " + w

def en_passages():
    txt = "\n".join(U.lines_of("en")); i = txt.find("2015 ASO English"); j = txt.find("2018 ASO English"); seg = txt[i:j]
    out = []
    for m in re.finditer(r"\nPassage\n(.*?)\n(?=\d{2}\. )", seg, re.S): out.append(clean(m.group(1)).replace("\n", " "))
    assert len(out) == 3, len(out)
    return out

def entries():
    """Bank rows for 2015 GA and English: dicts like the builder's (p, y, q, s, o, a, w, c, t, f[, g]) plus 'passages' list for English."""
    res = []
    G = {k: v for (y, k), v in U.load("ga").items() if y == 2015}
    for k in range(1, 101):
        v = G[k]; t, f = GA[k]; a = v["a"] if v["a"] in "ABCD" else ""
        why = note(v["w"]) if v["w"] else ""
        e = dict(p="ga", y=2015, q=k, s=clean(v["s"]), o=[clean(x) for x in v["o"]], a=a, w=why, c=not a, t="ga:" + t, f=f)
        res.append(e)
    E = {k: v for (y, k), v in U.load("en").items() if y == 2015}
    for k in range(1, 101):
        v = E[k]; t, f = EN[k]; a = v["a"] if v["a"] in "ABCD" else ""
        s = clean(v["s"])
        if 41 <= k <= 45: s = "Find out which part of the sentence contains an error (parts A to D)."
        res.append(dict(p="en", y=2015, q=k, s=s, o=[clean(x) for x in v["o"]], a=a, w=note(v["w"]), c=False, t="en:" + t, f=f))
    return res

if __name__ == "__main__":
    es = entries(); print(len(es), sum(1 for e in es if not e["a"]), [ (e["p"], e["q"]) for e in es if not e["a"]])
    print([e for e in es if e["p"] == "en" and e["q"] in (3, 41)][0]); print(en_passages()[1][:120])
    print(es[5]["w"])
