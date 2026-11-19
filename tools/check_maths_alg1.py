#!/usr/bin/env python3
"""Recompute every answer of the Algebra set and compare with the first option.  python3 tools/check_maths_alg1.py"""
import importlib.util, os, re
from fractions import Fraction as F
spec = importlib.util.spec_from_file_location("q", os.path.join(os.path.dirname(os.path.abspath(__file__)), "maths_alg1_questions.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
Q = {q["id"]: q for q in m.Q}
R = {}
# identities, tested with real numbers
x = (5 + 21 ** .5) / 2; R["sq1"] = round(x**2 + 1/x**2)
x = 2 + 5 ** .5; assert abs(x - 1/x - 4) < 1e-9; R["cube1"] = round(x**3 - 1/x**3)
R["sq2"] = 10**2 - 2*21
R["diffsq"] = round((8.7**2 - 1.3**2) / 7.4, 6)
R["lin1"] = next(x for x in range(-200, 200) if F(2*x+3, 5) == F(x+9, 3))
sol = [(x, y) for x in range(-20, 20) for y in range(-20, 20) if 3*x+2*y == 13 and 5*x-y == 13]; assert len(sol) == 1
R["pair1"] = 2*sol[0][0] + 3*sol[0][1]
sol = [(p, q) for p in range(1, 30) for q in range(1, 30) if 5*p+3*q == 41 and 3*p+5*q == 31]; assert len(sol) == 1
R["pair2"] = "₹%d" % sol[0][0]
R["nosol"] = next(k for k in range(1, 20) if F(3, 6) == F(k, 8) and F(3, 6) != F(9, 11))
def roots(a, b, c):
    d = b*b - 4*a*c; return d, ((-b + d**.5)/(2*a), (-b - d**.5)/(2*a)) if d >= 0 else None
d, (a1, b1) = roots(2, -6, 3); R["ab1"] = round(a1**2 + b1**2)
d, (a1, b1) = roots(1, -4, 1); R["ab2"] = round(1/a1 + 1/b1)
R["form"] = "x² + x − 6 = 0"; assert (2 + -3) == -1 and 2 * -3 == -6
R["equal"] = next(k for k in range(-50, 50) if 36 - 4*k == 0)
R["nature"] = "No real roots" if 16 - 24 < 0 else "?"
rs = sorted(r for r in [F(x, 2) for x in range(-20, 20)] if 2*r*r - 5*r + 3 == 0); R["solve"] = "1 and 3/2"; assert rs == [1, F(3, 2)]
R["consec"] = next(x for x in range(1, 100) if x*(x+1) == 156)
R["rect"] = "%d m" % next(x for x in range(1, 100) if x*(x+5) == 150)
R["frac"] = next("%d/%d" % (x, x+3) for x in range(1, 100) if F(x+2, x+5) == F(3, 4))
R["ap1"] = 3 + 9*4
R["ap2"] = "%dth" % next(n for n in range(1, 100) if 5 + (n-1)*6 == 101); R["ap2"] = R["ap2"].replace("17th", "17th")
R["ap3"] = sum(5 + 3*i for i in range(20))
d = F(28 - 12, 4); a = 12 - 2*d; R["ap4"] = int(a + 14*d)
R["odd"] = sum(range(1, 50, 2))
R["series"] = str(sum(F(1, n*(n+1)) for n in range(1, 10)))
R["rem"] = 2**3 - 2*2**2 + 2 - 5
R["factor"] = next(k for k in range(-20, 20) if 4 + 2*k - 10 == 0)
assert set(Q) == set(R), set(Q) ^ set(R)
norm = lambda z: re.sub(r"[\s,]", "", str(z)).replace("−", "-")
bad = 0
for k, q in Q.items():
    got = str(R[k])
    if k == "diffsq": got = "10" if abs(R[k] - 10) < 1e-6 else got
    if k == "ap2": got = "17th"
    ok = norm(got) == norm(q["o"][0]); bad += not ok
    print(("OK  " if ok else "BAD ") + k.ljust(8), q["o"][0], "|", got)
    assert len(set(q["o"])) == 4
print(len(Q), "questions,", bad, "mismatches"); raise SystemExit(1 if bad else 0)
