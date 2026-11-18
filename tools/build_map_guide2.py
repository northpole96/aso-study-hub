#!/usr/bin/env python3
"""Build ASO-Map-Guide-World-India-2.html (v1 was ASO-Map-Guide-World-India.html, from map_guide_content.py): a study guide on one world map with Indian states.
Chapters and places: tools/map_guide2_*.py (full explanations, Nov 2026 rewrite). Page: tools/map_guide_template.html.
Map data: tools/mapdata/ (same files as Map Test 01; the template fixes inside-out polygons).
Run: python3 tools/build_map_guide.py"""
import json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from map_guide2_india import CH_INDIA
from map_guide2_india_b import CH_INDIA_B
from map_guide2_world import CH_WORLD
from map_guide2_world_b import CH_WORLD_B
CH = CH_INDIA + CH_INDIA_B + CH_WORLD + CH_WORLD_B
D = ROOT / "tools/mapdata"

def area(r): return sum(r[i][0]*r[i+1][1]-r[i+1][0]*r[i][1] for i in range(len(r)-1))
def tiny_delta(poly):   # Sundarbans: hundreds of tiny islands print as a black blob
    r = poly[0]; x = sum(p[0] for p in r)/len(r); y = sum(p[1] for p in r)/len(r)
    return 88.0 < x < 89.2 and 21.4 < y < 22.4 and abs(area(r))/2 < 0.004
def clean(fc):
    for f in fc["features"]:
        g = f["geometry"]
        if g and g["type"] == "MultiPolygon": g["coordinates"] = [pl for pl in g["coordinates"] if not tiny_delta(pl)]
    return fc
world = json.load(open(D / "world.json"))
states = clean(json.load(open(D / "states.json")))
ij = json.load(open(D / "india.json"))
if ij["type"] == "GeometryCollection":
    ij = {"type": "FeatureCollection", "features": [{"type": "Feature", "properties": {}, "geometry": g} for g in ij["geometries"]]}
india = clean(ij)
rivers = json.load(open(D / "rivers.json"))

names = {f["properties"]["name"] for f in world["features"]}
sts = {f["properties"]["ST_NM"] for f in states["features"]}
rv = {f["properties"]["n"] for f in rivers["features"]}
seen = set()
for c in CH:
    assert c["part"] in ("India", "World") and c["P"], c["id"]
    for p in c["P"]:
        assert p["n"] not in seen, p["n"]; seen.add(p["n"])
        lon, lat = p["g"]; assert -180 <= lon <= 180 and -90 <= lat <= 90, p["n"]
        if p.get("c"): assert p["c"] in names, p["c"]
        if p.get("s"): assert p["s"] in sts, p["s"]
        if p.get("r"): assert p["r"] in rv, p["r"]
        if c["part"] == "India": assert 60 < lon < 100 and 5 < lat < 40, ("India chapter place far away", p["n"])
J = lambda o: json.dumps(o, ensure_ascii=False, separators=(",", ":"))
h = (ROOT / "tools/map_guide_template.html").read_text()
h = (h.replace("__KEY__", "aso-map-guide-2").replace("__NCH__", str(len(CH))).replace("__NP__", str(len(seen))).replace("__CH__", J(CH))
      .replace("__WORLD__", J(world)).replace("__STATES__", J(states)).replace("__RIVERS__", J(rivers)).replace("__INDIA__", J(india)))
(ROOT / "ASO-Map-Guide-World-India-2.html").write_text(h)
print("written", len(h)//1024, "KB,", len(CH), "chapters,", len(seen), "places")
