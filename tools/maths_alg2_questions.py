# Questions for Algebra Set 02 (50 questions, 45 minutes), made 19 Nov 2026 on the user's request ("another set of 50").
# No question repeats Set 01; each is a new angle of the same 2018/2021 families. FIRST option is right (builder shuffles).
# t = family (keeps neighbours apart); id = name used by tools/check_maths_alg2.py, which recomputes every answer.
Q = []
def add(t, id, q, o, e, c=False):
    Q.append(dict(s="Algebra", t=t, id=id, q=q, o=o, e=e, k="one", n=False, c=c, a=None))

# ---- 1 identities
add(1, "i1", "If x + 1/x = 3, what is the value of x³ + 1/x³?", ["18", "27", "24", "9"],
    "Family 1 · Identities. a³ + b³ = (a + b)³ − 3ab(a + b). With ab = 1: 27 − 3 × 3 = 18. Trap: 27 is only the cube of 3.")
add(1, "i2", "If a + b = 7 and a² + b² = 29, what is the value of a³ + b³?", ["133", "343", "154", "112"],
    "Family 1 · Identities. First find ab: (a + b)² = a² + b² + 2ab, so 49 = 29 + 2ab and ab = 10. Then a³ + b³ = 343 − 3 × 10 × 7 = 343 − 210 = 133. Trap: 343 forgets the 3ab(a + b) part.")
add(1, "i3", "If x − 1/x = 3, what is the value of x² + 1/x²?", ["11", "9", "7", "13"],
    "Family 1 · Identities. Square both sides: x² − 2 + 1/x² = 9, so x² + 1/x² = 11. Note the sign: with (x − 1/x) you ADD 2 back; with (x + 1/x) you take 2 away. Trap: 7 takes 2 away by mistake.")
add(1, "i4", "What is the value of 997 × 1003?", ["999991", "999999", "1000009", "999009"],
    "Family 1 · Identities. 997 × 1003 = (1000 − 3)(1000 + 3) = 1000² − 3² = 1,000,000 − 9 = 999,991. Spot the middle number (1000) and use (a − b)(a + b) = a² − b².")
add(1, "i5", "If a + b + c = 9 and ab + bc + ca = 26, what is the value of a² + b² + c²?", ["29", "55", "81", "107"],
    "Family 1 · Identities. (a + b + c)² = a² + b² + c² + 2(ab + bc + ca). So 81 = a² + b² + c² + 52, giving 29. Trap: 55 takes away 26 only once; 107 adds.")

# ---- 2 linear equations
add(2, "l1", "Solve: x/2 + x/3 = 10.", ["12", "10", "15", "20"],
    "Family 2 · Linear equation. x/2 + x/3 = 5x/6 = 10, so x = 12. Check: 6 + 4 = 10.")
add(2, "l2", "Solve: 0.3x + 0.5 = 0.2x + 1.2.", ["7", "12", "1.7", "0.7"],
    "Family 2 · Linear equation. Bring x terms together: 0.1x = 0.7, so x = 7. Trap: 0.7 is the right side, not yet divided by 0.1.")
add(2, "l3", "Solve: 2(x + 3) − 3(x − 2) = 3.", ["9", "−3", "15", "3"],
    "Family 2 · Linear equation. 2x + 6 − 3x + 6 = 3, so −x + 12 = 3 and x = 9. Trap: −3 comes from forgetting that −3 × −2 = +6.")
add(2, "l4", "Solve: (2x − 3)/(3x + 1) = 1/2.", ["7", "5", "9", "−7"],
    "Family 2 · Linear equation. Cross-multiply: 2(2x − 3) = 3x + 1, so 4x − 6 = 3x + 1 and x = 7. Check: 11/22 = 1/2.")
add(2, "l5", "A father is 4 times as old as his son. After 5 years the sum of their ages will be 55. How old is the father now?", ["36", "9", "45", "40"],
    "Family 2 · Linear word problem. Now: son S, father 4S. After 5 years the sum is 4S + S + 10 = 55, so 5S = 45 and S = 9. Father = 36. Trap: 9 is the son's age.")

# ---- 3 pairs of linear equations
add(3, "p1", "If x + y = 14 and x − y = 4, what is the value of xy?", ["45", "56", "81", "70"],
    "Family 3 · Pair of equations. Add: 2x = 18, x = 9; then y = 5. xy = 45. Trap: 56 is 14 × 4.")
add(3, "p2", "If 1/x + 1/y = 5/6 and 1/x − 1/y = 1/6, what is x + y?", ["5", "6", "1/5", "11/6"],
    "Family 3 · Pair of equations (reciprocals). Treat 1/x and 1/y as the unknowns: adding gives 2/x = 1, so 1/x = 1/2 and x = 2; then 1/y = 1/3 and y = 3. x + y = 5. Trap: do not stop at 1/x.")
add(3, "p3", "The digits of a two-digit number add up to 9. The number is 27 more than the number with the digits reversed. What is the number?", ["63", "72", "54", "36"],
    "Family 3 · Pair of equations (digits). Tens digit x, units y: x + y = 9. The number minus its reverse = 9(x − y) = 27, so x − y = 3. Then x = 6, y = 3 and the number is 63. Check: 63 − 36 = 27. Trap: 36 is the reversed number.")
add(3, "p4", "3 chairs and 2 tables cost ₹600. 2 chairs and 3 tables cost ₹650. What is the cost of one table?", ["₹150", "₹100", "₹125", "₹200"],
    "Family 3 · Pair of equations (prices). Add: 5 chairs + 5 tables = 1250, so chair + table = 250. Take away: table − chair = 50. Table = 150, chair = 100. Check: 300 + 300 = 600. Trap: ₹100 is the chair.")
add(3, "p5", "For what value of k do the equations 2x + ky = 5 and 3x + 4y = 7 NOT have a unique solution?", ["8/3", "3/8", "2/3", "6"],
    "Family 3 · Nature of solution. Not unique means the lines are parallel (or the same): a₁/a₂ = b₁/b₂, so 2/3 = k/4 and k = 8/3. Trap: 3/8 turns the ratio upside down.")
add(3, "p6", "The sum of the ages of A and B is 50 years. Five years ago A was three times as old as B. What is A's present age?", ["35", "15", "30", "40"],
    "Family 3 · Pair of equations (ages). A + B = 50 and A − 5 = 3(B − 5), so A = 3B − 10. Then 4B − 10 = 50, B = 15 and A = 35. Check: 30 = 3 × 10. Trap: 15 is B.")
add(3, "p7", "A fraction becomes 1 when 1 is added to its numerator, and becomes 1/2 when 1 is added to its denominator. What is the fraction?", ["2/3", "3/4", "1/2", "3/5"],
    "Family 3 · Pair of equations (fraction). (x + 1)/y = 1 gives y = x + 1. x/(y + 1) = 1/2 gives 2x = y + 1 = x + 2, so x = 2 and y = 3. Fraction 2/3. Check: 3/3 = 1 and 2/4 = 1/2.")

# ---- 4 roots alpha and beta
add(4, "a1", "If α and β are the roots of x² − 5x + 3 = 0, what is α² + β²?", ["19", "25", "31", "22"],
    "Family 4 · Roots α, β. α + β = 5 and αβ = 3. α² + β² = 25 − 2 × 3 = 19. Trap: 25 forgets 2αβ; 31 adds it.")
add(4, "a2", "If α and β are the roots of x² − 3x + 2 = 0, what is α³ + β³?", ["9", "27", "18", "15"],
    "Family 4 · Roots α, β. α + β = 3, αβ = 2. α³ + β³ = (α + β)³ − 3αβ(α + β) = 27 − 18 = 9. Check: the roots are 1 and 2, and 1 + 8 = 9.")
add(4, "a3", "If α and β are the roots of x² − 7x + 10 = 0, what is the value of |α − β|?", ["3", "9", "7", "√89"],
    "Family 4 · Roots α, β. (α − β)² = (α + β)² − 4αβ = 49 − 40 = 9, so |α − β| = 3. Check: the roots are 2 and 5. Trap: √89 uses +4αβ instead of −4αβ.")
add(4, "a4", "If 3 is a root of x² − kx − 6 = 0, what is k?", ["1", "−1", "3", "5"],
    "Family 4 · Root given. Put x = 3: 9 − 3k − 6 = 0, so k = 1. Then x² − x − 6 = (x − 3)(x + 2), the other root is −2.")
add(4, "a5", "If α and β are the roots of x² − 6x + 4 = 0, what is α/β + β/α?", ["7", "9", "5", "28"],
    "Family 4 · Roots α, β. α/β + β/α = (α² + β²)/αβ = ((α + β)² − 2αβ)/αβ = (36 − 8)/4 = 7. Trap: 9 is (α + β)²/αβ, which skips the −2αβ.")

# ---- 5 nature of roots
add(5, "n1", "For what positive value of k does x² + kx + 4 = 0 have equal roots?", ["4", "2", "8", "16"],
    "Family 5 · Nature of roots. Equal roots: k² − 16 = 0, so k = ±4. The positive value is 4. Check: x² + 4x + 4 = (x + 2)².")
add(5, "n2", "For what positive value of k does x² − kx + 16 = 0 have equal roots?", ["8", "4", "16", "32"],
    "Family 5 · Nature of roots. D = k² − 64 = 0, so k = ±8. The positive value is 8. Trap: 4 is the square root of 16, not of 64.")
add(5, "n3", "What is the nature of the roots of 3x² − 5x + 2 = 0?", ["Two distinct real roots", "Two equal real roots", "No real roots", "Only one root"],
    "Family 5 · Nature of roots. D = 25 − 24 = 1 > 0, so two distinct real roots (they are 1 and 2/3).")
add(5, "n4", "How many distinct real roots does x² + 4x + 4 = 0 have?", ["1", "2", "0", "4"],
    "Family 5 · Nature of roots. D = 16 − 16 = 0. The equation is (x + 2)² = 0, so there is one repeated root, x = −2. 'Equal roots' means ONE distinct value.")

# ---- 6 solving quadratics
add(6, "s1", "What is the positive root of x² − x − 12 = 0?", ["4", "3", "−3", "12"],
    "Family 6 · Solving. x² − x − 12 = (x − 4)(x + 3), so x = 4 or −3. The positive root is 4.")
add(6, "s2", "Find the roots of 6x² − x − 2 = 0.", ["2/3 and −1/2", "−2/3 and 1/2", "3/2 and −2", "1/3 and −2"],
    "Family 6 · Solving. Split the middle: 6x² − 4x + 3x − 2 = 2x(3x − 2) + (3x − 2) = (3x − 2)(2x + 1). So x = 2/3 or −1/2. Check: sum 1/6 = −b/a ✓.")
add(6, "s3", "If x + 1/x = 10/3 and x > 1, what is x?", ["3", "1/3", "10/3", "9"],
    "Family 6 · Solving. Multiply by 3x: 3x² + 3 = 10x, so 3x² − 10x + 3 = 0, i.e. (3x − 1)(x − 3) = 0. x = 3 or 1/3. Since x > 1, x = 3.")
add(6, "s4", "If (x − 2)(x + 3) = 24, what is the positive value of x?", ["5", "6", "4", "−6"],
    "Family 6 · Solving. x² + x − 6 = 24, so x² + x − 30 = 0, i.e. (x + 6)(x − 5) = 0. Positive root: 5. Trap: do not set each bracket equal to 24.")
add(6, "s5", "What is the positive root of x² − 2x − 2 = 0?", ["1 + √3", "1 − √3", "2 + √3", "√3 − 2"],
    "Family 6 · Formula. x = [2 ± √(4 + 8)]/2 = (2 ± 2√3)/2 = 1 ± √3. The positive one is 1 + √3 (about 2.73). 1 − √3 is negative.")

# ---- 7 quadratic word problems
add(7, "w1", "The sum of the squares of two consecutive positive integers is 145. What is the larger integer?", ["9", "8", "10", "7"],
    "Family 7 · Quadratic problem. x² + (x + 1)² = 145 gives 2x² + 2x − 144 = 0, so x² + x − 72 = 0, (x + 9)(x − 8) = 0. x = 8, the larger is 9. Check: 64 + 81 = 145.")
add(7, "w2", "In a right triangle the two shorter sides are x and x + 7, and the hypotenuse is 13. What is the length of the shortest side?", ["5", "6", "12", "7"],
    "Family 7 · Quadratic problem. x² + (x + 7)² = 169, so x² + 7x − 60 = 0, (x + 12)(x − 5) = 0. x = 5; sides 5, 12, 13. Trap: 12 is the other side.")
add(7, "w3", "A train covers 360 km at a uniform speed. If its speed were 5 km/h more, it would take 1 hour less. What is its speed?", ["40 km/h", "45 km/h", "36 km/h", "30 km/h"],
    "Family 7 · Quadratic problem. 360/x − 360/(x + 5) = 1 gives x² + 5x − 1800 = 0, (x + 45)(x − 40) = 0. Speed 40 km/h. Check: 9 h and 8 h. Trap: 45 is the faster speed.")
add(7, "w4", "Rahul's age 5 years ago multiplied by his age 9 years from now is 15. What is his present age?", ["6", "10", "5", "9"],
    "Family 7 · Quadratic problem. (x − 5)(x + 9) = 15, so x² + 4x − 60 = 0, (x + 10)(x − 6) = 0. Present age 6. Check: 1 × 15 = 15.")
add(7, "w5", "The base of a triangle is 4 cm more than its altitude, and its area is 48 cm². What is the altitude?", ["8 cm", "12 cm", "6 cm", "4 cm"],
    "Family 7 · Quadratic problem. (1/2) h (h + 4) = 48, so h² + 4h − 96 = 0, (h + 12)(h − 8) = 0. Altitude 8 cm, base 12 cm. Trap: 12 cm is the base.")

# ---- 8 A.P.
add(8, "ap1", "What is the 20th term of the A.P. 12, 9, 6, ...?", ["−45", "−48", "−51", "−42"],
    "Family 8 · A.P. a = 12, d = −3. 20th term = 12 + 19 × (−3) = −45. Trap: −48 uses n = 20 instead of n − 1 = 19.")
add(8, "ap2", "How many terms are there in the A.P. 4, 9, 14, ..., 99?", ["20", "19", "21", "18"],
    "Family 8 · A.P. 99 = 4 + (n − 1) × 5, so n − 1 = 19 and n = 20. Trap: 19 forgets to add the 1 back.")
add(8, "ap3", "What is the sum of the first 15 terms of an A.P. whose first term is 6 and common difference is 4?", ["510", "450", "540", "480"],
    "Family 8 · A.P. sum. S = 15/2 × [2 × 6 + 14 × 4] = 7.5 × 68 = 510.")
add(8, "ap4", "In an A.P. the 5th term is 17 and the 9th term is 33. What is the sum of the first 10 terms?", ["190", "180", "200", "170"],
    "Family 8 · A.P. 4d = 33 − 17 = 16, so d = 4 and a = 17 − 16 = 1. S₁₀ = 5 × [2 + 9 × 4] = 5 × 38 = 190.")
add(8, "ap5", "What is the sum of all two-digit numbers that are divisible by 7?", ["728", "700", "770", "784"],
    "Family 8 · A.P. The numbers are 14, 21, ..., 98. Number of terms: 98 = 14 + 7(n − 1), so n = 13. Sum = 13/2 × (14 + 98) = 13 × 56 = 728. Trap: 784 counts 14 terms (14 × 56).")
add(8, "ap6", "The sum of the first n terms of an A.P. is n² + 2n. What is its 10th term?", ["21", "120", "19", "23"],
    "Family 8 · A.P. from the sum. 10th term = S₁₀ − S₉ = (100 + 20) − (81 + 18) = 120 − 99 = 21. Trap: 120 is the sum, not the term.")
add(8, "ap7", "Three numbers in A.P. add up to 21 and their product is 315. What is the greatest number?", ["9", "7", "11", "10"],
    "Family 8 · A.P. Take the numbers as 7 − d, 7, 7 + d (the sum 21 gives the middle 7). Product: 7(49 − d²) = 315, so d² = 4, d = 2. Numbers 5, 7, 9. Greatest 9.")
add(8, "ap8", "In the A.P. 100, 95, 90, ..., which is the first negative term?", ["22nd", "21st", "20th", "23rd"],
    "Family 8 · A.P. nth term = 100 − 5(n − 1). It is 0 when n − 1 = 20, i.e. the 21st term is 0 (not negative). The 22nd term is −5. Trap: 21st is zero.")

# ---- 9 series
add(9, "r1", "Find the value of 1/(2×3) + 1/(3×4) + ... + 1/(19×20).", ["9/20", "19/20", "1/2", "8/19"],
    "Family 9 · Series of fractions. Split 1/(n(n + 1)) = 1/n − 1/(n + 1). The sum is (1/2 − 1/3) + ... + (1/19 − 1/20) = 1/2 − 1/20 = 9/20. Note it starts at 2, not 1.")
add(9, "r2", "Find the value of 1/(1×3) + 1/(3×5) + 1/(5×7) + 1/(7×9).", ["4/9", "8/9", "1/9", "2/9"],
    "Family 9 · Series of fractions. The gap between the two numbers is 2, so 1/(n(n + 2)) = (1/2)(1/n − 1/(n + 2)). The sum is (1/2)(1 − 1/9) = (1/2)(8/9) = 4/9. Trap: 8/9 forgets the 1/2.")
add(9, "r3", "What is the value of 1 + 2 + 3 + ... + 60?", ["1830", "1800", "1860", "3660"],
    "Family 9 · Sum of natural numbers. n(n + 1)/2 = 60 × 61/2 = 1830. Trap: 3660 forgets to halve.")

# ---- 10 polynomials
add(10, "y1", "What is the remainder when x³ + 4x² − x + 6 is divided by (x + 2)?", ["16", "−16", "0", "8"],
    "Family 10 · Remainder theorem. Divide by (x + 2) means put x = −2: −8 + 16 + 2 + 6 = 16. Trap: use x = −2, not +2.")
add(10, "y2", "If (x − 1) is a factor of x³ − 6x² + 11x − k, what is k?", ["6", "−6", "12", "1"],
    "Family 10 · Factor theorem. Put x = 1: 1 − 6 + 11 − k = 0, so k = 6. The cubic is x³ − 6x² + 11x − 6 = (x − 1)(x − 2)(x − 3).")
add(10, "y3", "Which of these is a factor of x³ − 7x + 6?", ["x − 2", "x + 2", "x − 3", "x + 1"],
    "Family 10 · Factor theorem. Test the number that makes the bracket zero. At x = 2: 8 − 14 + 6 = 0, so (x − 2) is a factor. At x = −2, 3, −1 the value is 12, not 0. Full factors: (x − 1)(x − 2)(x + 3).")

assert len(Q) == 50, len(Q)
