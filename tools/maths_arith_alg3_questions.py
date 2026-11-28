# Arithmetic & Algebra Mock 03 (28 Nov 2026): 50 questions, 45 min, on the arithmetic and algebra FAMILIES of the
# 2018 and 2021 papers (the Class 10 template, slot by slot) at their own difficulty. User: "another mock set but
# completely follow the arithmetic and algebraic family of 2018 and 2021 and almost same difficulty".
# Hand-made on the template (no draw): arithmetic Q51-63 in two passes (a 2018-style and a 2021-style question for
# every slot), four extras (Q82, Q93, Q95, Q96 types), then algebra Q64-77 once and six twins (Q64, Q71, Q74, Q75,
# Q78 sets, Q83 power set).
# Exact past questions: 2021 Q51, 2021 Q68, 2021 Q76. Everything else is new; none repeats Mock 01/02 or the other
# maths sets. First option is right (the builder shuffles). Order is given.

META = dict(
    paper="maths",
    title="ASO Arithmetic & Algebra Mock 03",
    hub_title="Arithmetic & Algebra Mock 03 · 2018-21 template",
    masthead="Ari+Alg M03",
    heading="Paper II (B) · Arithmetic and Algebra · Mock 03",
    tagline="50 questions on the <b>2018 and 2021 template</b>,<br>the same families and the same level as those papers.",
    key="aso-maths-arith-alg-3",
    code="AA03",
    out="ASO-Maths-Mock-Arithmetic-Algebra-3.html",
    minutes=45,
    seed=20261130,
    order="given",
    date="28 Nov 2026",
    draw="hand-made on the 2018 and 2021 Class 10 template (no draw)",
    intro=[
        "The 2018 and 2021 maths papers used one Class 10 template, slot by slot: a fraction series, a divisibility "
        "question, the H.C.F. of fractions, a decimal product, an identity with big numbers, recurring decimals, "
        "percentages, profit and loss, CI minus SI, work, speed and a root, and then the algebra block of roots, "
        "indices, ratios, matrices, linear pairs, the discriminant and the A.P. This mock follows that template "
        "exactly and keeps its difficulty: short questions, one idea each, no long word problems.",
        "The arithmetic block runs through the slots twice, once in the style of 2018 and once in the style of 2021, "
        "with four extras of the counting and averages kind. The algebra block runs through the slots once and then "
        "adds a second question for the roots, linear pairs, A.P. and sets slots. Three questions are real past "
        "questions word for word (2021 Q51, Q68 and Q76). Press Copy answers at the end and paste the report into "
        "the chat for a redo set.",
    ],
)

Q = []
def add(s, q, o, e, k="one", n=False, c=False, a=None, **x):
    d = dict(s=s, q=q, o=o, e=e, k=k, n=n, c=c, a=a); d.update(x); Q.append(d)

A = "Arithmetic"
G = "Algebra"

# ================================================================ ARITHMETIC, first pass (2018 style)

add(A, "1/(2·4) + 1/(4·6) + 1/(6·8) + 1/(8·10) + 1/(10·12) = ?",
    ["5/24", "5/12", "1/6", "7/24"],
    "Each term is ½ × (1/a − 1/b) because the gap is 2. The sum telescopes: ½ × (1/2 − 1/12) = ½ × 5/12 = 5/24. "
    "Trap: 5/12 forgets the ½. Slot: Q51 of 2018 and 2021 (a fraction series). Next: the same with gap 3 or gap 4.",
    calc="5/24")

add(A, "What least number of four digits is exactly divisible by 53?",
    ["1007", "1060", "954", "1113"],
    "The smallest 4-digit number is 1000. 1000 ÷ 53 = 18 remainder 46, so the next multiple is 53 × 19 = 1007. "
    "Trap: 954 = 53 × 18 has only three digits. Slot: Q52 of 2018 (least five-digit number divisible by 41). "
    "Next: the greatest 3-digit number divisible by a given number.",
    calc="53*19")

add(A, "The H.C.F. of 2/3, 4/9 and 8/15 is:",
    ["2/45", "2/3", "8/45", "4/15"],
    "H.C.F. of fractions = H.C.F. of the numerators ÷ L.C.M. of the denominators. H.C.F.(2, 4, 8) = 2 and "
    "L.C.M.(3, 9, 15) = 45. So the H.C.F. is 2/45. Trap: 8/45 uses the largest numerator. Slot: Q53 (H.C.F. of fractions, "
    "2018 and 2021). Next: the L.C.M. of fractions (L.C.M. of numerators ÷ H.C.F. of denominators).",
    calc="2/45")

add(A, "0.07 × 0.0135 is equal to:",
    ["0.000945", "0.00945", "0.0945", "0.0000945"],
    "Multiply 7 × 135 = 945. The first number has 2 decimal places and the second has 4, so the answer has 6 places: "
    "0.000945. Trap: counting 5 places gives 0.00945. Slot: Q54 (0.04 × 0.0162 in 2018, 0.03 × 0.0165 in 2021). "
    "Next: the answer in standard form.",
    calc="0.07*0.0135")

add(A, "[(654 + 346)² − (654 − 346)²] ÷ (654 × 346) = ?",
    ["4", "2", "308", "1000"],
    "(a + b)² − (a − b)² = 4ab. So the expression is 4ab ÷ ab = 4. No work with the big numbers is needed. Trap: 2 is "
    "the answer for the plus sign version. Slot: Q55 of 2018 and 2021 (the same identity with 489, 375 and 799, 267). "
    "Next: the plus-sign version, which is 2.",
    calc="((654+346)**2-(654-346)**2)/(654*346)")

add(A, "0.(27) + 0.(54) + 0.(19) = ? (a bar over two digits means that block repeats)",
    ["100/99", "1.0", "100/100", "98/99"],
    "A block of two repeating digits ab is ab/99. So the sum is (27 + 54 + 19)/99 = 100/99. Trap: adding as plain decimals "
    "0.27 + 0.54 + 0.19 gives 1.0. Slot: Q56 (0.(63) + 0.(37) + 0.(80) in 2018, 0.68̅ + 0.73̅ in 2021). "
    "Next: one digit repeating, such as 0.4̅ = 4/9.",
    calc="100/99")

add(A, "Two numbers are 30% and 50% more than a third number. The ratio of the two numbers is:",
    ["13 : 15", "15 : 13", "3 : 5", "30 : 50"],
    "Let the third number be 100. The numbers are 130 and 150, so the ratio is 130 : 150 = 13 : 15. Trap: 3 : 5 uses the "
    "percentages directly. Slot: Q57 (20% and 50% in 2018, 20% and 40% in 2021). Next: x% and y% less than a third number.",
    calc="13")

add(A, "A man sells 35% of his mangoes and still has 520 mangoes. How many mangoes did he have at first?",
    ["800", "700", "900", "780"],
    "After selling 35%, 65% are left. 65% of the total = 520, so the total = 520 ÷ 0.65 = 800. Trap: 520 + 35% of 520 = 702, "
    "a wrong base. Slot: Q58 (an 'sells x% and still has' question: 40% and 420 in 2018, 30% and 140 in 2021). "
    "Next: sells some and gives away some.",
    calc="520/0.65")

add(A, "100 mangoes are bought for Rs. 400 and sold at Rs. 60 per dozen. What is the profit per cent?",
    ["25%", "20%", "50%", "12.5%"],
    "Cost of one mango = Rs. 4. Selling price of one = 60 ÷ 12 = Rs. 5. Profit = 1 on cost 4, which is 25%. Trap: 20% divides "
    "by the selling price. Slot: Q59 (2018: 100 oranges bought and sold per dozen; 2021: 11 oranges for Rs. 10). "
    "Next: a loss instead of a gain.",
    calc="(5-4)/4*100")

add(A, "The difference between compound interest and simple interest on Rs. 5,000 for 2 years at 8% per annum is:",
    ["Rs. 32", "Rs. 40", "Rs. 64", "Rs. 16"],
    "For 2 years, CI − SI = P (r/100)² = 5000 × 0.0064 = Rs. 32. Check: SI = 800 and CI = 5000 × (1.1664 − 1) = 832. "
    "Trap: Rs. 64 uses the rate 8 twice instead of squaring 0.08. Slot: Q60 (Rs. 4,000 at 10% in 2018; Rs. 2.50 at 5% in 2021). "
    "Next: the sum is asked.",
    calc="5000*0.08**2")

add(A, "A and B can do a work in 10 days, B and C in 15 days, and A, B and C together in 8 days. In how many days can "
       "A and C together do the work?",
    ["12 days", "10 days", "15 days", "9 days"],
    "C alone = 1/8 − 1/10 = 1/40 and A alone = 1/8 − 1/15 = 7/120. A and C together = 7/120 + 3/120 = 10/120 = 1/12 a day. "
    "So 12 days. Shortcut: A + C = 2(A + B + C) − (A + B) − (B + C) = 2/8 − 1/10 − 1/15 = 1/12. Trap: 10 days is "
    "the A + B time. Slot: Q61 of 2018 (the same pairs with 8, 12 and 6 days). Next: A alone.",
    calc="1/(2/8-1/10-1/15)")

add(A, "A man crosses a street 900 m long in 6 minutes. What is his speed in km per hour?",
    ["9 km/h", "7.5 km/h", "15 km/h", "5.4 km/h"],
    "Speed = 900 m ÷ 6 min = 150 m/min = 150 × 60 = 9,000 m/h = 9 km/h. Trap: 15 km/h is 900 ÷ 60. Slot: Q62 of 2018 "
    "(600 m in 5 minutes gives 7.2 km/h). Next: the time is asked from the speed.",
    calc="900/6*60/1000")

add(A, "The value of √1.4641 is:",
    ["1.21", "1.11", "1.31", "1.41"],
    "1.4641 has four decimal places, so its root has two. 121 × 121 = 14641, so √1.4641 = 1.21. Trap: 1.11 or 1.31 (a "
    "wrong square). Slot: Q63 of 2021 (√1.5625 = 1.25). Next: the root of a number such as 0.000441 (0.021).",
    calc="1.21")

# ================================================================ ARITHMETIC, second pass (2021 style)

add(A, "1/(1·3) + 1/(3·5) + 1/(5·7) + 1/(7·9) = ?",
    ["4/9", "5/11", "6/11", "9/4"],
    "Exact past question (2021 Q51). Each term is ½ × (1/a − 1/b), so the sum is ½ × (1 − 1/9) = ½ × 8/9 = 4/9. "
    "Slot: Q51 of 2018 (gap 3) and 2021 (gap 2). Next: gap 4 or a different start.",
    src="2021 Q51", calc="4/9")

add(A, "What is the smallest 4-digit number which is exactly divisible by 8 and 12?",
    ["1008", "1000", "1032", "1020"],
    "The L.C.M. of 8 and 12 is 24. 1000 ÷ 24 = 41 remainder 16, so the next multiple is 24 × 42 = 1008. Trap: 1000 is "
    "divisible by 8 but not by 12. Slot: Q52 of 2021 (smallest 3-digit number divisible by 6 and 12 = 108). "
    "Next: three divisors.",
    calc="24*42")

add(A, "What is the H.C.F. of 3/4, 9/10 and 12/25?",
    ["3/100", "3/4", "1/100", "36/25"],
    "H.C.F. of numerators (3, 9, 12) = 3. L.C.M. of denominators (4, 10, 25) = 100. So the H.C.F. is 3/100. Trap: 3/4 "
    "uses only one denominator. Slot: Q53 (1/5, 2/7, 3/11 gave 1/385 in 2021). Next: L.C.M. of fractions.",
    calc="3/100")

add(A, "0.012 × 0.0025 is equal to:",
    ["0.00003", "0.0003", "0.000003", "0.003"],
    "12 × 25 = 300. The decimal places are 3 + 4 = 7, so 300 becomes 0.0000300 = 0.00003. Trap: 0.0003 counts one place "
    "less. Slot: Q54. Next: a product with a power of 10 in standard form (3 × 10⁻⁵).",
    calc="0.012*0.0025")

add(A, "[(583 + 417)² + (583 − 417)²] ÷ (583² + 417²) = ?",
    ["2", "4", "1000", "166"],
    "(a + b)² + (a − b)² = 2(a² + b²). So the expression is 2(a² + b²) ÷ (a² + b²) = 2. Trap: 4 is the answer when "
    "the sign between the squares is minus (and the divisor is ab). Slot: Q55. Next: a³ + b³ over a² − ab + b².",
    calc="((583+417)**2+(583-417)**2)/(583**2+417**2)")

add(A, "0.(15) + 0.(36) = ? (a bar over two digits means that block repeats)",
    ["17/33", "51/100", "51/99 as 0.51", "1/2"],
    "Each block over 99: (15 + 36)/99 = 51/99 = 17/33. Trap: 0.51 adds the plain decimals 0.15 + 0.36. Slot: Q56 "
    "(0.68̅ + 0.73̅ in 2021). Next: three recurring decimals.",
    calc="17/33")

add(A, "Two numbers are 20% less and 36% less than a third number. The ratio of the two numbers is:",
    ["5 : 4", "4 : 5", "20 : 36", "9 : 16"],
    "Let the third number be 100. The numbers are 80 and 64, so the ratio is 80 : 64 = 5 : 4. Trap: 4 : 5 reverses it; "
    "20 : 36 uses the percentages. Slot: Q57. Next: one number more and one less.",
    calc="5")

add(A, "A fruit seller sells 45% of his oranges and still has 330 oranges. How many oranges did he have at first?",
    ["600", "480", "750", "595"],
    "55% are left. 55% of the total = 330, so the total = 330 ÷ 0.55 = 600. Trap: 330 + 45% of 330 = 478.5 (wrong base). "
    "Slot: Q58 (30% and 140 in 2021). Next: two stages of selling.",
    calc="330/0.55")

add(A, "15 oranges are bought for Rs. 12 and 12 oranges are sold for Rs. 15. What is the gain per cent?",
    ["56.25%", "25%", "50%", "62.5%"],
    "Cost of one orange = 12/15 = Rs. 0.80. Selling price of one = 15/12 = Rs. 1.25. Gain = 0.45 on cost 0.80 = 56.25%. "
    "Trap: 25% is just 15 − 12 divided by 12. Slot: Q59 (11 oranges for Rs. 10 and 10 for Rs. 11 in 2021). Next: a loss "
    "with the numbers reversed.",
    calc="(15/12-12/15)/(12/15)*100")

add(A, "The difference between compound interest and simple interest for 2 years at 5% per annum is Rs. 6. Find the sum.",
    ["Rs. 2,400", "Rs. 1,200", "Rs. 3,000", "Rs. 4,800"],
    "For 2 years, CI − SI = P × (5/100)² = P × 0.0025. So P = 6 ÷ 0.0025 = Rs. 2,400. Trap: Rs. 120 would be 6 ÷ 0.05. "
    "Slot: Q60 (Rs. 2.50 gave Rs. 1,000 in 2021). Next: the rate is asked.",
    calc="6/0.0025")

add(A, "A can finish a work in 12 days and B in 16 days. B works for 8 days and then leaves. In how many days will A "
       "finish the remaining work?",
    ["6 days", "4 days", "8 days", "9 days"],
    "B does 8/16 = ½ of the work. The other ½ is left. A does 1/12 a day, so ½ ÷ 1/12 = 6 days. Trap: 8 days forgets "
    "that B already did half. Slot: Q61 of 2021 (A in 18 days, B in 15 days, B works 10 days). Next: A and B work "
    "together for some days first.",
    calc="0.5*12")

add(A, "The ratio of the speeds of two trains is 5 : 6. If the second train runs 360 km in 4 hours, what is the speed "
       "of the first train?",
    ["75 km/h", "90 km/h", "108 km/h", "60 km/h"],
    "Second train: 360 ÷ 4 = 90 km/h. First = 90 × 5/6 = 75 km/h. Trap: 108 km/h reverses the ratio. Slot: Q62 of 2021 "
    "(7 : 8 and 400 km in 4 hours). Next: the first train's distance in 3 hours.",
    calc="90*5/6")

add(A, "(243)^(1/5) × (1024)^(1/10) = ?",
    ["6", "5", "12", "9"],
    "243 = 3⁵, so 243^(1/5) = 3. 1024 = 2¹⁰, so 1024^(1/10) = 2. The product is 3 × 2 = 6. Trap: 5 adds instead of "
    "multiplying. Slot: Q63 of 2018 (64^(1/3) × ∛32768 = 128). Next: a cube root of a power of 2.",
    calc="3*2")

# ================================================================ ARITHMETIC, extras (counting and averages)

add(A, "How many natural numbers are there between 40 and 200 which are exactly divisible by 7?",
    ["23", "22", "24", "28"],
    "The multiples of 7 between 40 and 200 are 42, 49, …, 196. Count = (196 − 42) ÷ 7 + 1 = 22 + 1 = 23. Trap: 22 forgets "
    "the +1. Slot: Q82 of 2021 (between 23 and 100 divisible by 6 gives 13). Next: divisible by 6 and 8 together.",
    calc="(196-42)//7+1")

add(A, "The average of 40 numbers is 15. The average of the first 25 of them is 14 and that of the next 14 is 16. "
       "What is the last number?",
    ["26", "24", "30", "15"],
    "Total of all 40 = 600. First 25 add up to 350 and the next 14 add up to 224, together 574. The last (40th) "
    "number = 600 − 574 = 26. Trap: 15 is the overall average. Slot: Q95 of 2021 (30 numbers, first 20 and next 9). "
    "Next: the average of the last 15.",
    calc="40*15-25*14-14*16")

add(A, "The average of A and B is 30, that of B and C is 32 and that of C and A is 34. What is the value of A?",
    ["32", "30", "34", "36"],
    "A + B = 60, B + C = 64 and C + A = 68. Adding, 2(A + B + C) = 192, so A + B + C = 96. A = 96 − (B + C) = 96 − 64 = 32. "
    "Trap: 34 is half of C + A, not A. Slot: Q96 of 2021 (averages 20, 19 and 21). Next: the value of C.",
    calc="96-64")

add(A, "The difference of the squares of two consecutive odd numbers is 96. What is the sum of the two numbers?",
    ["48", "46", "24", "50"],
    "(n + 2)² − n² = (n + 2 − n)(n + 2 + n) = 2 × (sum of the two numbers). So the sum = 96 ÷ 2 = 48 (the numbers are 23 and 25). "
    "Trap: 24 divides by 4. Slot: Q93 of 2021 (consecutive even numbers, difference 84, sum 42). Next: the larger number.",
    calc="96/2")

# ================================================================ ALGEBRA, first pass (Q64-77 in booklet order)

add(G, "If α and β are the roots of a quadratic equation such that α + β = 10 and α − β = 2, then the equation is:",
    ["x² − 10x + 24 = 0", "x² + 10x + 24 = 0", "x² − 10x + 16 = 0", "x² − 12x + 24 = 0"],
    "Adding: 2α = 12, so α = 6 and β = 4. Sum = 10 and product = 24. The equation is x² − (sum)x + product = x² − 10x + 24 = 0. "
    "Trap: the sign of the middle term is minus. Slot: Q64 of 2018 (24 and 8) and 2021 (12 and 4). Next: the sum "
    "of the squares of the roots.",
    nocalc=True)

add(G, "If p ≠ 1 and p^(7x + 2) = 1, then x = ?",
    ["−2/7", "2/7", "−7/2", "0"],
    "A power equals 1 (with base not 1) only when the power is 0. So 7x + 2 = 0 and x = −2/7. Trap: 2/7 loses the sign. "
    "Slot: Q65 of 2021 (p^(5x + 3) = 1 gives −3/5). Next: an equation such as 2^(3x) = 1.",
    calc="-2/7")

add(G, "When x³ + 4x² − kx + 5 is divided by (x − 1), the remainder is k. The value of k is:",
    ["5", "10", "2", "−5"],
    "Remainder theorem: the remainder is the value at x = 1: 1 + 4 − k + 5 = 10 − k. Set 10 − k = k, so k = 5. Trap: 10 is the "
    "value of the constant part only. Slot: Q66 of 2018 (x³ + 3x² − kx + 4 divided by x − 2). Next: the remainder on "
    "division by x + 1.",
    calc="5")

add(G, "If (4x + 3y) : (2x + y) = 9 : 4, then x : y is:",
    ["3 : 2", "2 : 3", "9 : 4", "1 : 2"],
    "Cross-multiply: 4(4x + 3y) = 9(2x + y), so 16x + 12y = 18x + 9y and 3y = 2x. Then x : y = 3 : 2. Check: x = 3, y = 2 "
    "gives 18 : 8 = 9 : 4. Trap: 2 : 3 turns it over. Slot: Q67 of 2018 ((2x + 5y) : (5x − 7y) = 5 : 3). Next: "
    "x/3 = y/8 gives (x + 3) : (y + 8) = 3 : 8.",
    calc="3")

add(G, "The fourth proportional to 5, 8, 15 is:",
    ["24", "18", "21", "19"],
    "Exact past question (2021 Q68). 5 : 8 = 15 : x, so x = 8 × 15 ÷ 5 = 24. Slot: Q68 of 2018 (5, 4, 25 gives 20). "
    "Next: the third proportional.",
    src="2021 Q68", calc="24")

add(G, "If the determinant |x + 1  2 ; 3  4| equals the determinant |6  3 ; 2  4| (a b ; c d means ad − bc), then x = ?",
    ["5", "4", "6", "3"],
    "Left: 4(x + 1) − 6 = 4x − 2. Right: 6 × 4 − 3 × 2 = 24 − 6 = 18. So 4x − 2 = 18 and x = 5. Trap: dropping the −6 on "
    "the left gives x = 3.5, which is not an option. Slot: Q69 of 2018 and 2021 (equal determinants). Next: a determinant with x on the diagonal.",
    calc="5")

add(G, "If M = [[1, 2], [0, 3]] and N = [[2, 0], [1, −1]] (each inner bracket is a row), then 3M − N is:",
    ["[[1, 6], [−1, 10]]", "[[5, 6], [1, 8]]", "[[1, 6], [1, 10]]", "[[1, 2], [−1, 10]]"],
    "3M = [[3, 6], [0, 9]]. Subtract N entry by entry: [[3 − 2, 6 − 0], [0 − 1, 9 − (−1)]] = [[1, 6], [−1, 10]]. Trap: "
    "9 − (−1) = 10, and 0 − 1 = −1; the sign slips are the usual mistake. Slot: Q70 of 2018 (M + 2N) and 2021 (2M + N). "
    "Next: the product M × N.",
    nocalc=True)

add(G, "For what value of k does the pair of equations 2x + 3y = 7 and 4x + ky = 9 not have a unique solution?",
    ["6", "3", "−6", "12"],
    "No unique solution means a₁/a₂ = b₁/b₂. 2/4 = 3/k, so k = 6. (Then c₁/c₂ = 7/9 differs, so there is no solution at all.) "
    "Slot: Q71 of 2018 (4x + py + 8 = 0, x + y + 1 = 0) and 2021 (no solution). "
    "Next: infinitely many solutions.",
    calc="6")

add(G, "The discriminant of the quadratic equation 4x² − 5x + 2 = 0 is:",
    ["−7", "7", "−32", "57"],
    "D = b² − 4ac = (−5)² − 4 × 4 × 2 = 25 − 32 = −7. Trap: 57 adds instead of subtracting. A negative D means no real "
    "roots. Slot: Q72 of 2018 (2x² − 4x + 3: −8) and 2021 (3x² − 5x + 3: −11). Next: the value of k for equal roots.",
    calc="-7")

add(G, "A pair of linear equations a₁x + b₁y + c₁ = 0 and a₂x + b₂y + c₂ = 0 has a₁/a₂ = b₁/b₂ = c₁/c₂. Then the pair has:",
    ["infinitely many solutions", "no solution", "exactly one solution", "exactly two solutions"],
    "All three ratios equal means the two lines are the same line (coincident), so every point on it is a solution: "
    "infinitely many. The pair is called consistent and dependent. Trap: 'no solution' is for the last ratio being "
    "different. Slot: Q73 of 2018 (a₁/a₂ ≠ b₁/b₂, a unique solution) and 2021 (the first two equal, the third not, "
    "no solution). Next: the name of each case.",
    nocalc=True)

add(G, "If the 7th and 11th terms of an A.P. are 40 and 56 respectively, then its 15th term is:",
    ["72", "64", "68", "76"],
    "11th − 7th = 4d = 16, so d = 4. The 15th term = 11th term + 4d = 56 + 16 = 72. Shortcut: the terms 7, 11, 15 are in A.P. "
    "too, so 15th = 2 × 56 − 40 = 72. Trap: 64 adds 8 only. Slot: Q74 of 2018 (5th and 8th) and 2021 (7th and 13th). "
    "Next: the first term.",
    calc="2*56-40")

add(G, "If the sum of n terms of an A.P. is 2n² + 3n, then which of its terms is 81?",
    ["20th", "19th", "21st", "40th"],
    "Term n = Sₙ − Sₙ₋₁ = (2n² + 3n) − [2(n − 1)² + 3(n − 1)] = 4n + 1. Set 4n + 1 = 81, so n = 20. Trap: 19th or 21st come from an "
    "off-by-one slip in Sₙ − Sₙ₋₁. Slot: Q75 of 2021 (3n² + 5n gives 164, the 27th term). Next: the common difference.",
    calc="20")

add(G, "If the sum of n terms of an A.P. be 3n² + n and the common difference is 6, then its 1st term is:",
    ["2", "3", "1", "4"],
    "Exact past question (2021 Q76). The first term = S₁ = 3 × 1 + 1 = 4. (Check: S₂ = 14, so the 2nd term is 10, and 10 − 4 = 6.) "
    "Slot: Q76 of 2021; Q77 of 2018 asked the sum of 11 terms. Next: the 10th term.",
    src="2021 Q76", a=3, calc="4")

add(G, "In an A.P. the 7th term is 38. What is the sum of its first 13 terms?",
    ["494", "456", "507", "266"],
    "The 7th term is the middle term of 13 terms, so S₁₃ = 13 × (middle term) = 13 × 38 = 494. Trap: 266 is 7 × 38. "
    "Slot: Q77 of 2018 (the 6th term 45 gives S₁₁ = 495). Next: S₉ from the 5th term.",
    calc="13*38")

# ================================================================ ALGEBRA, second pass (twins) and sets

add(G, "If α and β are the roots of a quadratic equation such that α + β = 14 and α − β = 6, then the equation is:",
    ["x² − 14x + 40 = 0", "x² + 14x + 40 = 0", "x² − 14x + 24 = 0", "x² − 8x + 40 = 0"],
    "Adding: 2α = 20, so α = 10 and β = 4. Sum 14 and product 40. The equation is x² − 14x + 40 = 0. Trap: the product "
    "is 40, not 24. Slot: Q64. Next: the roots are asked.",
    nocalc=True)

add(G, "For what value of k does the pair of equations kx + 2y = 3 and 3x − y = 4 have no solution?",
    ["−6", "6", "−3", "3/2"],
    "No solution: a₁/a₂ = b₁/b₂ ≠ c₁/c₂. k/3 = 2/(−1) = −2, so k = −6. Check the last ratio: c₁/c₂ = 3/4, which is not −2, "
    "so there really is no solution. Trap: 6 loses the sign of b₂. Slot: Q71 of 2021 (αx + y = 3, 2x − 3y = 5). "
    "Next: infinitely many solutions.",
    calc="-6")

add(G, "The 3rd term of an A.P. is 14 and its 9th term is 38. What is its 20th term?",
    ["82", "78", "86", "74"],
    "6d = 38 − 14 = 24, so d = 4. The 20th term = 9th term + 11d = 38 + 44 = 82. Trap: 78 counts 10 steps. Slot: Q74 of 2018 "
    "and 2021. Next: which term is 150.",
    calc="38+11*4")

add(G, "Which of the following lists of numbers is an A.P.?",
    ["2, 5, 8, 11, …", "1, 3, 9, 27, …", "1, 4, 9, 16, …", "1/2, 1/3, 1/4, 1/5, …"],
    "In an A.P. the gap between neighbouring terms is the same. 2, 5, 8, 11 has a gap of 3 every time. The others have "
    "gaps that change (2, 6, 18; 3, 5, 7; −1/6, −1/12, −1/20). Trap: 1, 4, 9, 16 looks regular but its gaps grow. "
    "Slot: Q75 of 2018 (which of the following are in A.P.). Next: terms with surds.",
    nocalc=True)

add(G, "In a group of 300 students every student speaks Odia or English. 200 speak Odia and 120 speak English. "
       "How many students speak Odia only?",
    ["180", "100", "80", "20"],
    "Everyone speaks at least one: n(O ∪ E) = 300. n(both) = 200 + 120 − 300 = 20. Odia only = 200 − 20 = 180. Trap: "
    "20 is the number who speak both. Slot: Q78 of 2021 (500 students, Hindi only = 300) and 2018 (the programmers). "
    "Next: English only (100).",
    calc="200-(200+120-300)")

add(G, "A set has 128 subsets. How many elements does the set have?",
    ["7", "6", "8", "64"],
    "A set with n elements has 2ⁿ subsets. 2ⁿ = 128 = 2⁷, so n = 7. Trap: 64 is the number of subsets of a 6-element "
    "set. Slot: Q83 of 2018 and 2021 (the power set of a set with 5 elements has 32 elements). Next: the number of "
    "proper subsets (127).",
    calc="7")
