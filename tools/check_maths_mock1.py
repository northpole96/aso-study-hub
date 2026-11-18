#!/usr/bin/env python3
"""Recompute every answer of Maths Mock 01 and compare with the first option.  python3 tools/check_maths_mock1.py"""
import importlib.util, os, math, re
from fractions import Fraction as F
from itertools import product, combinations
from math import comb
spec = importlib.util.spec_from_file_location("q", os.path.join(os.path.dirname(__file__), "maths_mock1_questions.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
Q = {q["id"]: q for q in m.Q}
R = {}
R["sub23"] = 2010 % 23
R["sq2135"] = (math.isqrt(2135) + 1) ** 2 - 2135
R["div90"] = [x for x in range(10) if int("748%d0" % x) % 90 == 0][0]
R["hcfratio"] = "%d and %d" % (13 * 17, 8 * 17)
l = math.lcm(6, 8, 12, 18); R["bells"] = "%d:%02d a.m." % (9 + l // 60, l % 60)
R["succdiv"] = next(n for n in range(1, 500) if n % 3 == 2 and (n // 3) % 4 == 3 and (n // 3 // 4) % 5 == 4)
R["salary"] = "Rs. {:,}".format(int(6000 / (F(3, 5) * F(2, 3))))
s = next(s for s in range(1, 100) if (s + 20 - 5) == 3 * (s - 5)); g = math.gcd(s + 20, s); R["ages"] = "%d : %d" % ((s + 20) // g, s // g)
n = next(n for n in range(1, 99, 2) if (n + 2) ** 2 - n ** 2 == 64); R["oddsq"] = 2 * n + 2
R["keepers"] = next(k for k in range(100) if (80 + 120 + 24 + 2 * k) - (76 + k) == 160)
R["rect"] = "%g%% increase" % round((1.2 * 0.9 - 1) * 100, 6)
red = 240 * 0.2 / 2; R["sugar"] = "Rs. %g" % (red / 0.8)
R["votes"] = "{:,}".format(int(1120 / 0.16 + 0.5))
R["toffee"] = "%g" % (6 / 1.2)
c = next(c for c in range(0, 8001) if 25 * c - 10 * (8000 - c) == 4 * 8000); R["cowcalf"] = "Rs. {:,}".format(c)
r = F(288 * 100, 1200 * 4); R["sirate"] = "Rs. {:,}".format(int(1200 + 1200 * (r + 2) * 4 / 100))
R["cisi3"] = "Rs. %s" % (F(8000) * (F(21, 20) ** 3 - 1) - 8000 * F(15, 100))
x = F(4500 * 12 * 8, 9 * 8); R["partner"] = "Rs. {:,}".format(int(x))
R["avgclass"] = "%g kg" % ((20 * 42 + 30 * 37) / 50)
R["reap"] = 12 * 8 * 15 // (16 * 9)
R["fort"] = 200 * 24 // 240
R["menboys"] = F(3 * 16, 6 + 6)
t = 1 / (F(1, 20) + F(1, 30) - F(1, 15)); R["pipes3"] = "%s minutes" % t
R["pipeclose"] = "%g minutes" % float((1 - F(15, 20)) * 30)
v = next(v for v in range(1, 200) if F(150, 10) * F(18, 5) + 6 == v); R["train"] = "%d km/h" % v
R["car"] = "%d km/h" % next(v for v in range(1, 200) if F(360, v) - F(360, v + 10) == 3)
a = 1000 / (40 / 8) - 8; R["race"] = "%d min %d s" % (a // 60, a % 60)
tm = F(29 * 60 * 1440, 1450); hh = 8 * 60 + tm; hh %= 24 * 60; R["clock"] = "%d:%02d p.m." % ((hh // 60 - 1) % 12 + 1, hh % 60)
R["telescope"] = sum(F(1, a * (a + 3)) for a in (2, 5, 8, 11))
R["venn"] = 60 - (35 + 30 - 10)
R["indices"] = next(F(n, d) for d in (1, 2, 3) for n in range(-9, 10) if F(n, d) + 2 * (F(n, d) + 1) == 5)
R["surd"] = "a = %s, b = %s" % (F(11, 7), F(6, 7))  # (3+r2)^2/7 = (11+6r2)/7
assert abs((3 + 2 ** .5) / (3 - 2 ** .5) - (11 / 7 + 6 / 7 * 2 ** .5)) < 1e-12
roots = [x for x in range(-20, 21) if x * x - 7 * x + 12 == 0]; R["alphabeta"] = sum(r * r for r in roots)
R["equalroots"] = "k = ±%d" % math.isqrt(4 * 2 * 8)
R["infinite"] = F(6 * 2, 4)
d = F(41 - 17, 6); a0 = 17 - 3 * d; R["apterm"] = a0 + 19 * d
S_ = lambda n: 2 * n * n + 3 * n; R["apsum"] = S_(10) - S_(9)
R["remainder"] = next(k for k in range(-10, 11) if 8 - 8 + 2 * k + 5 == 11)
R["det"] = "±2√3"; assert abs(math.sqrt(2 * 6 - 4 * 3 + 12) - 2 * math.sqrt(3)) < 1e-12
R["wire"] = "%g m" % ((F(4, 3) * 6 ** 3) / F(4, 100) / 100)
R["wheel"] = 110000 // (F(22, 7) * 70)
R["cone"] = "%d cm²" % (F(22, 7) * 7 * math.isqrt(7 * 7 + 24 * 24))
sums = [a + b for a, b in product(range(1, 7), repeat=2)]
R["diceprime"] = F(sum(1 for s in sums if s in (2, 3, 5, 7, 11)), 36)
R["leap"] = F(2, 7)
R["coins"] = F(sum(1 for t in product("HT", repeat=3) if t.count("H") >= 2), 8)
R["socks"] = F(comb(5, 2) + comb(4, 2), comb(9, 2))
R["committee"] = comb(9, 4)
R["median"] = "%g" % (20 + (25 - 20) / 20 * 10)
R["mean3"] = 3 * 14 + 3 * 17 - 5 * 15
R["empirical"] = "%g" % (3 * 32 - 2 * 34.5)
bad = 0
for k, q in Q.items():
    want = str(R[k]); got = q["o"][0]
    norm = lambda z: re.sub(r"[\s,]", "", z)
    ok = norm(want) == norm(got)
    if not ok: bad += 1
    print(("OK  " if ok else "BAD ") + k.ljust(12), got, "|", want)
    assert len(set(q["o"])) == 4
assert set(Q) == set(R), set(Q) ^ set(R)
print(len(Q), "questions,", bad, "mismatches")
