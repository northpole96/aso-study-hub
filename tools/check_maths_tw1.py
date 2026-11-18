#!/usr/bin/env python3
"""Recompute every answer of the Time and Work set and compare with the first option.  python3 tools/check_maths_tw1.py"""
import importlib.util, os, re
from fractions import Fraction as F
spec = importlib.util.spec_from_file_location("q", os.path.join(os.path.dirname(__file__), "maths_tw1_questions.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
Q = {q["id"]: q for q in m.Q}

def mixed(x, unit):
    x = F(x); w, r = divmod(x.numerator, x.denominator)
    return ("%d %d/%d %s" % (w, r, x.denominator, unit)) if r else ("%d %s" % (w, unit))

R = {}
R["together"] = mixed(1 / (F(1, 12) + F(1, 18)), "days")
R["bAlone"] = mixed(1 / (F(1, 10) - F(1, 15)), "days")
allr = (F(1, 12) + F(1, 15) + F(1, 20)) / 2
R["pairsAll"] = mixed(1 / allr, "days")
R["pairsA"] = mixed(1 / (allr - F(1, 15)), "days")
done = 6 * (F(1, 20) + F(1, 30)); R["leavesAfter"] = mixed(6 + (1 - done) * 30, "days")
R["leavesBefore"] = mixed(next(F(t, 10) for t in range(1, 1000) if (F(t, 10) - 5) / 10 + F(t, 10) / 15 == 1), "days")
b = F(1, 14) / 3; R["efficient"] = mixed(1 / (2 * b), "days")
w, d = F(0), 0
while w < 1:
    d += 1; w += F(1, 10) if d % 2 else F(1, 15)
assert w == 1  # ends exactly at the end of a day
R["alternate"] = mixed(d, "days")
c = 1 - F(3, 6) - F(3, 8); R["wages"] = "Rs. {:,}".format(int(3200 * c))
# 4m+6w = 1/8 and 3m+7w = 1/10, solved exactly
det = 4 * 7 - 6 * 3; mm = (F(1, 8) * 7 - 6 * F(1, 10)) / det; ww = (4 * F(1, 10) - 3 * F(1, 8)) / det
assert 4 * mm + 6 * ww == F(1, 8) and 3 * mm + 7 * ww == F(1, 10)
R["menWomen"] = mixed(1 / (10 * ww), "days")
R["mhd"] = mixed(F(15 * 8 * 20, 120) * 60 / (10 * 6), "days")
R["extraMen"] = 60 * 25 // (40 - 25) - 60
ra = F(3, 5) / 12; R["helperJoins"] = mixed(1 / (F(2, 5) / 3 - ra), "days")
R["pipeLeak"] = mixed(F(1, 2) / (F(1, 12) - F(1, 18)), "hours")

bad = 0
norm = lambda z: re.sub(r"[\s,]", "", str(z))
for k, q in Q.items():
    ok = norm(R[k]) == norm(q["o"][0])
    bad += not ok
    print(("OK  " if ok else "BAD ") + k.ljust(13), q["o"][0], "|", R[k])
    assert len(set(q["o"])) == 4
assert set(Q) == set(R), set(Q) ^ set(R)
print(len(Q), "questions,", bad, "mismatches")
raise SystemExit(1 if bad else 0)
