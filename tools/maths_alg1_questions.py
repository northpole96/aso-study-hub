# Questions for the Algebra set (25 questions, 30 minutes), made 19 Nov 2026 on the user's request.
# Algebra in 2018 and 2021 followed the Class 10 template (identities, linear pairs, quadratics with alpha and beta,
# A.P., series of fractions), so each question here is the next angle of one of those families.
# FIRST option is the right one (the builder shuffles). t = family number (keeps neighbours apart),
# id = name used by tools/check_maths_alg1.py, which recomputes every answer.

Q = []
def add(t, id, q, o, e, c=False):
    Q.append(dict(s="Algebra", t=t, id=id, q=q, o=o, e=e, k="one", n=False, c=c, a=None))

# ---- 1 identities
add(1, "sq1", "If x + 1/x = 5, what is the value of x² + 1/x²?",
    ["23", "25", "27", "21"],
    "Family 1 · Identities. Square both sides: (x + 1/x)² = x² + 2 + 1/x². So x² + 1/x² = 25 − 2 = 23. "
    "Trap: 25 forgets to take away the middle 2. 27 adds 2 instead of taking it away.")
add(1, "cube1", "If x − 1/x = 4, what is the value of x³ − 1/x³?",
    ["76", "64", "52", "60"],
    "Family 1 · Identities. Use a³ − b³ = (a − b)³ + 3ab(a − b). Here a = x, b = 1/x, so ab = 1. "
    "x³ − 1/x³ = 4³ + 3 × 4 = 64 + 12 = 76. Trap: 64 is only the cube of 4; the +3ab(a − b) part is missed.")
add(1, "sq2", "If x + y = 10 and xy = 21, what is the value of x² + y²?",
    ["58", "79", "100", "42"],
    "Family 1 · Identities. x² + y² = (x + y)² − 2xy = 100 − 42 = 58. Trap: 100 forgets the 2xy; 79 takes xy once, not twice.")
add(1, "diffsq", "What is the value of (8.7² − 1.3²) ÷ 7.4?",
    ["10", "7.4", "9.4", "1"],
    "Family 1 · Identities. a² − b² = (a − b)(a + b). Here a − b = 7.4 and a + b = 10, so the top is 7.4 × 10 and the 7.4 cancels. Answer 10. "
    "Never square the decimals one by one; spotting the identity makes it a one-line sum.")

# ---- 2 linear equation
add(2, "lin1", "Solve for x: (2x + 3)/5 = (x + 9)/3.",
    ["36", "24", "18", "12"],
    "Family 2 · Linear equation. Cross-multiply: 3(2x + 3) = 5(x + 9), so 6x + 9 = 5x + 45 and x = 36. "
    "Check: (72 + 3)/5 = 15 and (36 + 9)/3 = 15. Both sides match.")

# ---- 3 pair of linear equations
add(3, "pair1", "If 3x + 2y = 13 and 5x − y = 13, what is the value of 2x + 3y?",
    ["12", "13", "9", "15"],
    "Family 3 · Pair of linear equations. From the second, y = 5x − 13. Put it in the first: 3x + 10x − 26 = 13, so 13x = 39 and x = 3, y = 2. "
    "Then 2x + 3y = 6 + 6 = 12. Trap: 13 is just the number on the right of the first equation. Finish with what the question asks for, 2x + 3y, not only x and y.")
add(3, "pair2", "5 pens and 3 pencils cost ₹41. 3 pens and 5 pencils cost ₹31. What is the cost of one pen?",
    ["₹7", "₹5", "₹2", "₹9"],
    "Family 3 · Pair of linear equations (word problem). Add the two bills: 8 pens + 8 pencils = 72, so one pen + one pencil = 9. "
    "Take them away: 2 pens − 2 pencils = 10, so pen − pencil = 5. Then the pen is (9 + 5)/2 = 7 and the pencil is 2. "
    "Check: 35 + 6 = 41 and 21 + 10 = 31. Trap: ₹2 is the pencil.")
add(3, "nosol", "For what value of k do the equations 3x + ky = 9 and 6x + 8y = 11 have no solution?",
    ["4", "3", "8", "6"],
    "Family 3 · Pair of linear equations (nature of solution). No solution means the lines are parallel: a₁/a₂ = b₁/b₂ ≠ c₁/c₂. "
    "Here 3/6 = k/8, so k = 4. Then c₁/c₂ = 9/11, which is not 1/2, so the lines never meet. "
    "Likely next: if the last line were 6x + 8y = 18, the same k = 4 would give infinitely many solutions.")

# ---- 4 roots, sum and product (alpha, beta)
add(4, "ab1", "If α and β are the roots of 2x² − 6x + 3 = 0, what is the value of α² + β²?",
    ["6", "9", "3", "7.5"],
    "Family 4 · Roots α and β. For ax² + bx + c = 0: α + β = −b/a = 3 and αβ = c/a = 3/2. "
    "α² + β² = (α + β)² − 2αβ = 9 − 3 = 6. Trap: 9 forgets to take away 2αβ.")
add(4, "ab2", "If α and β are the roots of x² − 4x + 1 = 0, what is the value of 1/α + 1/β?",
    ["4", "1/4", "−4", "5"],
    "Family 4 · Roots α and β. 1/α + 1/β = (α + β)/αβ. Here α + β = 4 and αβ = 1, so the answer is 4/1 = 4. "
    "Trap: 1/4 turns the fraction upside down.")
add(4, "form", "Which quadratic equation has roots 2 and −3?",
    ["x² + x − 6 = 0", "x² − x − 6 = 0", "x² + x + 6 = 0", "x² − 5x − 6 = 0"],
    "Family 4 · Forming the equation. Sum of roots = 2 + (−3) = −1 and product = 2 × (−3) = −6. "
    "The equation is x² − (sum)x + (product) = 0, i.e. x² + x − 6 = 0. Trap: x² − x − 6 has the sum sign the wrong way.")

# ---- 5 nature of roots
add(5, "equal", "For what value of k does x² − 6x + k = 0 have two equal roots?",
    ["9", "6", "3", "36"],
    "Family 5 · Nature of roots. Equal roots need the discriminant b² − 4ac = 0. So 36 − 4k = 0 and k = 9. "
    "Check: x² − 6x + 9 = (x − 3)², a perfect square. Trap: 36 is b².")
add(5, "nature", "What is the nature of the roots of 2x² − 4x + 3 = 0?",
    ["No real roots", "Two equal real roots", "Two distinct real roots", "One real and one imaginary root"],
    "Family 5 · Nature of roots. Discriminant D = b² − 4ac = 16 − 24 = −8. D is negative, so there are no real roots. "
    "Rule: D > 0 two different real roots, D = 0 two equal roots, D < 0 no real roots.")
add(5, "solve", "Find the roots of 2x² − 5x + 3 = 0.",
    ["1 and 3/2", "−1 and −3/2", "1 and −3/2", "2 and 3"],
    "Family 5 · Solving by factors. Split the middle term: 2x² − 2x − 3x + 3 = 2x(x − 1) − 3(x − 1) = (2x − 3)(x − 1). "
    "So x = 3/2 or x = 1. Check with sum and product: 1 + 3/2 = 5/2 = −b/a and 1 × 3/2 = 3/2 = c/a.")

# ---- 6 quadratic word problems
add(6, "consec", "The product of two consecutive positive integers is 156. What is the smaller integer?",
    ["12", "13", "11", "14"],
    "Family 6 · Quadratic word problem. Let the numbers be x and x + 1. Then x² + x − 156 = 0, i.e. (x + 13)(x − 12) = 0. "
    "x = 12 (the −13 is not positive). The numbers are 12 and 13. Trap: 13 is the larger number; check what the question asks.")
add(6, "rect", "The length of a rectangle is 5 m more than its breadth, and its area is 150 m². What is the breadth?",
    ["10 m", "15 m", "5 m", "12 m"],
    "Family 6 · Quadratic word problem. Breadth x, length x + 5: x(x + 5) = 150, so x² + 5x − 150 = 0, i.e. (x + 15)(x − 10) = 0. "
    "Breadth = 10 m (a length cannot be −15). Length = 15 m. Trap: 15 m is the length.")
add(6, "frac", "The denominator of a fraction is 3 more than its numerator. If 2 is added to both, the fraction becomes 3/4. What was the fraction?",
    ["7/10", "5/8", "6/9", "9/12"],
    "Family 6 · Fraction problem. Let the fraction be x/(x + 3). Then (x + 2)/(x + 5) = 3/4, so 4x + 8 = 3x + 15 and x = 7. The fraction is 7/10. "
    "Check: 9/12 = 3/4. Trap: 9/12 is the NEW fraction, not the old one.")

# ---- 7 A.P.
add(7, "ap1", "What is the 10th term of the A.P. 3, 7, 11, ...?",
    ["39", "43", "40", "35"],
    "Family 7 · A.P. nth term = a + (n − 1)d. Here a = 3 and d = 4, so the 10th term = 3 + 9 × 4 = 39. "
    "Trap: 43 is the 11th term (using n instead of n − 1 gives 3 + 10 × 4 = 43).")
add(7, "ap2", "Which term of the A.P. 5, 11, 17, ... is 101?",
    ["17th", "16th", "18th", "15th"],
    "Family 7 · A.P. Use a + (n − 1)d = 101 with a = 5 and d = 6: (n − 1) × 6 = 96, so n − 1 = 16 and n = 17. "
    "Trap: 16 is n − 1. Do not forget to add the 1 back.")
add(7, "ap3", "What is the sum of the first 20 terms of the A.P. 5, 8, 11, ...?",
    ["670", "640", "335", "700"],
    "Family 7 · A.P. sum. S = n/2 × [2a + (n − 1)d] = 10 × [10 + 19 × 3] = 10 × 67 = 670. "
    "Trap: 335 is half the answer; it forgets the 2 in front of a, or the n/2 factor, in the formula.")
add(7, "ap4", "In an A.P. the 3rd term is 12 and the 7th term is 28. What is the 15th term?",
    ["60", "56", "64", "48"],
    "Family 7 · A.P. from two terms. Four steps of d take the 3rd term to the 7th: 4d = 28 − 12 = 16, so d = 4. "
    "Then a = 12 − 2 × 4 = 4. The 15th term = 4 + 14 × 4 = 60. Shortcut: 12 more steps of 4 from the 3rd term: 12 + 48 = 60.")
add(7, "odd", "What is the sum of the first 25 odd numbers (1 + 3 + 5 + ...)?",
    ["625", "650", "325", "600"],
    "Family 7 · A.P. Short rule: the sum of the first n odd numbers is n². So 25² = 625. "
    "Check with the formula: 25/2 × (2 + 24 × 2) = 12.5 × 50 = 625. Trap: 650 is the sum of the first 25 EVEN numbers, 25 × 26.")

# ---- 8 series of fractions
add(8, "series", "Find the value of 1/(1×2) + 1/(2×3) + 1/(3×4) + ... + 1/(9×10).",
    ["9/10", "1", "10/11", "8/9"],
    "Family 8 · Series of fractions. Split each term: 1/(n(n + 1)) = 1/n − 1/(n + 1). So the sum = (1 − 1/2) + (1/2 − 1/3) + ... + (1/9 − 1/10). "
    "Everything in the middle cancels, leaving 1 − 1/10 = 9/10. Rule: the sum up to n terms is n/(n + 1). Trap: 10/11 is for 10 terms.")

# ---- 9 polynomials
add(9, "rem", "What is the remainder when x³ − 2x² + x − 5 is divided by (x − 2)?",
    ["−3", "5", "−5", "3"],
    "Family 9 · Remainder theorem. The remainder on dividing by (x − a) is the value at x = a. Put x = 2: 8 − 8 + 2 − 5 = −3. "
    "Trap: 3 and −5 drop a sign or a term.")
add(9, "factor", "If (x − 2) is a factor of x² + kx − 10, what is the value of k?",
    ["3", "−3", "5", "−5"],
    "Family 9 · Factor theorem. If (x − 2) is a factor, putting x = 2 gives zero: 4 + 2k − 10 = 0, so 2k = 6 and k = 3. "
    "Check: x² + 3x − 10 = (x − 2)(x + 5).")

assert len(Q) == 25, len(Q)
