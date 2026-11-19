#!/usr/bin/env python3
"""Recompute every answer of Algebra Set 02 and compare with the first option.  python3 tools/check_maths_alg2.py"""
import importlib.util, os, re, math
from fractions import Fraction as F
spec = importlib.util.spec_from_file_location("q", os.path.join(os.path.dirname(os.path.abspath(__file__)), "maths_alg2_questions.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
Q = {q["id"]: q for q in m.Q}
R = {}
def xs(f, lo=-300, hi=300, den=1): return [F(x, den) for x in range(lo*den, hi*den) if f(F(x, den))]
x = (3 + 5**.5)/2; R["i1"] = round(x**3 + 1/x**3)
R["i2"] = next(a**3 + b**3 for a in range(-20, 21) for b in range(-20, 21) if a+b == 7 and a*a+b*b == 29) if any(a+b==7 and a*a+b*b==29 for a in range(-20,21) for b in range(-20,21)) else (lambda ab: 343 - 3*ab*7)(F(49-29, 2))
x = (3 + 13**.5)/2; assert abs(x - 1/x - 3) < 1e-9; R["i3"] = round(x**2 + 1/x**2)
R["i4"] = 997*1003
R["i5"] = 81 - 2*26
R["l1"] = xs(lambda x: x/2 + x/3 == 10)[0]
R["l2"] = xs(lambda x: F(3,10)*x + F(1,2) == F(1,5)*x + F(6,5), den=10)[0]
R["l3"] = xs(lambda x: 2*(x+3) - 3*(x-2) == 3)[0]
R["l4"] = xs(lambda x: 3*x+1 != 0 and (2*x-3)/(3*x+1) == F(1, 2))[0]
R["l5"] = next(4*s for s in range(1, 100) if 4*s + s + 10 == 55)
sol = [(x, y) for x in range(-30, 30) for y in range(-30, 30) if x+y == 14 and x-y == 4]; R["p1"] = sol[0][0]*sol[0][1]
sol = [(x, y) for x in range(1, 30) for y in range(1, 30) if F(1,x)+F(1,y) == F(5,6) and F(1,x)-F(1,y) == F(1,6)]; assert len(sol) == 1; R["p2"] = sum(sol[0])
sol = [10*t+u for t in range(1, 10) for u in range(10) if t+u == 9 and (10*t+u) - (10*u+t) == 27]; assert len(sol) == 1; R["p3"] = sol[0]
sol = [(c, t) for c in range(1, 400) for t in range(1, 400) if 3*c+2*t == 600 and 2*c+3*t == 650]; assert len(sol) == 1; R["p4"] = "₹%d" % sol[0][1]
R["p5"] = str(F(2, 3) * 4)
sol = [(a, b) for a in range(1, 50) for b in range(1, 50) if a+b == 50 and a-5 == 3*(b-5)]; assert len(sol) == 1; R["p6"] = sol[0][0]
sol = [(x, y) for x in range(1, 30) for y in range(1, 30) if x+1 == y and 2*x == y+1]; R["p7"] = "%d/%d" % sol[0]
R["a1"] = 25 - 6
R["a2"] = 27 - 3*2*3
R["a3"] = round(abs(2 - 5))  # roots 2 and 5
assert sorted([2, 5]) == sorted(r for r in range(-20, 20) if r*r - 7*r + 10 == 0)
R["a4"] = next(k for k in range(-20, 20) if 9 - 3*k - 6 == 0)
R["a5"] = str(F(36 - 8, 4))
R["n1"] = next(k for k in range(1, 50) if k*k - 16 == 0)
R["n2"] = next(k for k in range(1, 50) if k*k - 64 == 0)
R["n3"] = "Two distinct real roots" if 25 - 24 > 0 else "?"
R["n4"] = 1 if 16 - 16 == 0 else 2
R["s1"] = next(x for x in range(1, 50) if x*x - x - 12 == 0)
assert sorted(xs(lambda x: 6*x*x - x - 2 == 0, den=6)) == [F(-1, 2), F(2, 3)]; R["s2"] = "2/3 and −1/2"
R["s3"] = str(next(x for x in xs(lambda x: x > 1 and x != 0 and x + 1/x == F(10, 3)))); 
R["s4"] = next(x for x in range(1, 50) if (x-2)*(x+3) == 24)
r = 1 + 3**.5; assert abs(r*r - 2*r - 2) < 1e-9; R["s5"] = "1 + √3"
x = next(x for x in range(1, 100) if x*x + (x+1)**2 == 145); R["w1"] = x + 1
R["w2"] = next(x for x in range(1, 20) if x*x + (x+7)**2 == 169)
R["w3"] = "%d km/h" % next(x for x in range(1, 200) if F(360, x) - F(360, x+5) == 1)
R["w4"] = next(x for x in range(6, 100) if (x-5)*(x+9) == 15)
R["w5"] = "%d cm" % next(h for h in range(1, 100) if h*(h+4) == 96)
R["ap1"] = 12 + 19*(-3)
R["ap2"] = next(n for n in range(1, 100) if 4 + (n-1)*5 == 99)
R["ap3"] = sum(6 + 4*i for i in range(15))
d = F(33 - 17, 4); a = 17 - 4*d; R["ap4"] = sum(a + d*i for i in range(10))
R["ap5"] = sum(n for n in range(10, 100) if n % 7 == 0)
S = lambda n: n*n + 2*n; R["ap6"] = S(10) - S(9)
sol = [(7-d, 7, 7+d) for d in range(-10, 11) if (7-d)*7*(7+d) == 315]; R["ap7"] = max(sol[0])
n = next(n for n in range(1, 100) if 100 - 5*(n-1) < 0); R["ap8"] = {21: "21st", 22: "22nd"}[n]
R["r1"] = str(sum(F(1, n*(n+1)) for n in range(2, 20)))
R["r2"] = str(sum(F(1, n*(n+2)) for n in (1, 3, 5, 7)))
R["r3"] = sum(range(1, 61))
R["y1"] = (-2)**3 + 4*(-2)**2 - (-2) + 6
R["y2"] = next(k for k in range(-20, 20) if 1 - 6 + 11 - k == 0)
p = lambda x: x**3 - 7*x + 6; R["y3"] = [f for f, z in (("x − 2", 2), ("x + 2", -2), ("x − 3", 3), ("x + 1", -1)) if p(z) == 0]; assert len(R["y3"]) == 1; R["y3"] = R["y3"][0]
assert set(Q) == set(R), set(Q) ^ set(R)
norm = lambda z: re.sub(r"[\s,]", "", str(z)).replace("−", "-")
bad = 0
for k, q in Q.items():
    ok = norm(R[k]) == norm(q["o"][0]); bad += not ok
    print(("OK  " if ok else "BAD ") + k.ljust(4), q["o"][0], "|", R[k])
    assert len(set(q["o"])) == 4, k
print(len(Q), "questions,", bad, "mismatches"); raise SystemExit(1 if bad else 0)
