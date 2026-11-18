#!/usr/bin/env python3
"""Build ASO-Map-Test-World-India-1.html: 40 click-on-the-map questions on one world map with Indian states.
Questions: tools/map1_questions.py. Map data: tools/mapdata/*.json (Natural Earth 50m countries, DataMeet states
simplified with mapshaper, Natural Earth 10m rivers filtered to India + the biggest world rivers). Page: tools/map_quiz_template.html.
Run: python3 tools/build_map1.py"""
import json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from map1_questions import Q
D = ROOT / "tools/mapdata"
def area(r): return sum(r[i][0]*r[i+1][1]-r[i+1][0]*r[i][1] for i in range(len(r)-1))
def rewind(fc):   # d3 wants clockwise outer rings (negative area in lon/lat), counter-clockwise holes
    for f in fc["features"]:
        g = f["geometry"]
        if not g: continue
        polys = [g["coordinates"]] if g["type"] == "Polygon" else g["coordinates"] if g["type"] == "MultiPolygon" else []
        for poly in polys:
            for j, ring in enumerate(poly):
                if (area(ring) > 0) == (j == 0): ring.reverse()
    return fc
world = rewind(json.load(open(D / "world.json")))
states = json.load(open(D / "states.json"))
def tiny_delta(poly):   # the Sundarbans coast is hundreds of tiny islands that print as a black blob: drop the small ones
    r = poly[0]; x = sum(p[0] for p in r)/len(r); y = sum(p[1] for p in r)/len(r)
    return 88.0 < x < 89.2 and 21.4 < y < 22.4 and abs(area(r))/2 < 0.004
for f in states["features"]:
    g = f["geometry"]
    if g["type"] == "MultiPolygon": g["coordinates"] = [pl for pl in g["coordinates"] if not tiny_delta(pl)]
states = rewind(states)
ij = json.load(open(D / "india.json"))
if ij["type"] == "GeometryCollection": ij = {"type": "FeatureCollection", "features": [{"type": "Feature", "properties": {}, "geometry": g} for g in ij["geometries"]]}
for f in ij["features"]:
    g = f["geometry"]
    if g["type"] == "MultiPolygon": g["coordinates"] = [pl for pl in g["coordinates"] if not tiny_delta(pl)]
india = rewind(ij)

rivers = json.load(open(D / "rivers.json"))
names = {f["properties"]["name"] for f in world["features"]}
sts = {f["properties"]["ST_NM"] for f in states["features"]}
rv = {f["properties"]["n"] for f in rivers["features"]}
out = []
for i, q in enumerate(Q):
    assert q["t"] in ("pt", "state", "country", "river"), i
    if q["t"] == "country": assert q["g"] in names, q["g"]
    if q["t"] == "state": assert q["g"] in sts, q["g"]
    if q["t"] == "river": assert q["g"] in rv, q["g"]
    if q["t"] == "pt": assert len(q["g"]) == 2 and q.get("k"), i
    d = dict(q); d["a"] = 0          # hub scoring: answer 0 = right, 1 = wrong, -1 skipped
    out.append(d)
J = lambda o: json.dumps(o, ensure_ascii=False, separators=(",", ":"))
h = (ROOT / "tools/map_quiz_template.html").read_text()
h = (h.replace("__TITLE__", "ASO Map Test 01 · World + India").replace("__SUB__", "Set 01 · World + India · 40 places")
      .replace("__KEY__", "aso-map-world-india-1").replace("__Q__", J(out))
      .replace("__WORLD__", J(world)).replace("__STATES__", J(states)).replace("__RIVERS__", J(rivers)).replace("__INDIA__", J(india)))
(ROOT / "ASO-Map-Test-World-India-1.html").write_text(h)
print("written", len(h)//1024, "KB,", len(out), "questions")
