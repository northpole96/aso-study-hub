#!/usr/bin/env python3
"""Recompute every answer of the Speed, Trains, Races and Boats set.  python3 tools/check_maths_speed1.py"""
import importlib.util, os, re, math
from fractions import Fraction as F
spec = importlib.util.spec_from_file_location("q", os.path.join(os.path.dirname(__file__), "maths_speed1_questions.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
Q = {q["id"]: q for q in m.Q}
kmh = lambda ms: F(ms) * F(18, 5)
ms = lambda k: F(k) * F(5, 18)

def num(x, unit):
    x = F(x)
    if x.denominator == 1: return "%d %s" % (x, unit)
    w, r = divmod(x.numerator, x.denominator)
    if x.denominator in (2, 5, 10): return "%g %s" % (float(x), unit)
    return "%d %d/%d %s" % (w, r, x.denominator, unit)

R = {}
R["conv"] = "{:,} m".format(int(ms(72) * 15))
usual = next(t for t in range(1, 200) if F(5, 4) * t - t == 10); R["late"] = num(usual, "minutes")
R["lateEarly"] = num(next(F(d, 10) for d in range(1, 500) if F(d, 10) / 5 - F(d, 10) / 6 == F(10, 60)), "km")
d = next(d for d in range(1, 500) if F(d, 12) - F(d, 18) == 2); start = 15 - d // 12
R["cycle"] = num(F(d, 14 - start), "km/h")
R["newSpeed"] = num(60 * 6 / F(9, 2), "km/h")
ta = next(t for t in range(1, 500) if t - F(3, 4) * t == 30); R["ratioTime"] = num(F(ta, 60), "hours")
R["avg2"] = num(F(240, F(120, 40) + F(120, 60)), "km/h")
R["avg3"] = num(F(180, F(60, 10) + F(60, 20) + F(60, 60)), "km/h")
R["avgParts"] = num(F(60, F(24, 6) + F(36, 12)), "km/h")
R["stoppage"] = num(F(54 - 45, 54) * 60, "minutes")
t = F(310 - 40, 90); assert t == 3; R["meet"] = "12 noon"
tc = F(F(200, 1000), 12 - 10); R["chase"] = num(10 * tc, "km")
R["pole"] = num(kmh(F(240, 16)), "km/h")
R["platform"] = num(ms(54) * 20 - 180, "m")
R["poleAndPlatform"] = num(next(L for L in range(1, 1000) if F(L, 15) == F(L + 100, 25)), "m")
R["manSame"] = num(kmh(F(125, 10)) + 5, "km/h")
R["opposite"] = num(F(300) / ms(60 + 48), "seconds")
R["sameDir"] = num(F(250) / ms(72 - 54), "seconds")
g = math.gcd(math.isqrt(16), math.isqrt(9)); R["afterMeet"] = "%d : %d" % (math.isqrt(16) // g, math.isqrt(9) // g)
R["chainBeat"] = num(1000 - F(900 * 900, 1000), "m")
a, b = F(5, 3), 1; R["startGiven"] = num(80 / (a - b) * a, "m")
tA = F(200) / ms(18); R["startBeat"] = num(kmh(F(180) / (tA + 5)), "km/h")
R["circle"] = num(F(600, 5 - 3) / 60, "minutes")
dn, up = F(30, 2), F(18, 2); R["boatBasic"] = num((dn + up) / 2, "km/h")
R["boatRatio"] = num(next(b for b in range(5, 100) if b + 4 == 2 * (b - 4)), "km/h")
R["boatRound"] = num(next(d for d in range(1, 1000) if F(d, 12) + F(d, 8) == 25), "km")

bad = 0
norm = lambda z: re.sub(r"[\s,]", "", str(z))
for k, q in Q.items():
    ok = norm(R[k]) == norm(q["o"][0])
    bad += not ok
    print(("OK  " if ok else "BAD ") + k.ljust(16), q["o"][0], "|", R[k])
    assert len(set(q["o"])) == 4, k
assert set(Q) == set(R), set(Q) ^ set(R)
print(len(Q), "questions,", bad, "mismatches")
raise SystemExit(1 if bad else 0)
