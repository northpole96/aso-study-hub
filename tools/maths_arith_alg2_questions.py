# Arithmetic & Algebra Mock 02 (28 Nov 2026): the second 50-question mock on syllabus topics (a) Arithmetic and
# (b) Algebra only, moderate to hard (user: "another set").
# Plan: python3 .claude/skills/aso-mock/scripts/draw.py maths --topics ari,alg --n 50 --seed 731204
# (37 arithmetic, 13 algebra; exact past questions 2021 Q55 and 2021 Q72).
# No question repeats Arithmetic & Algebra Mock 01, Maths Mock 01, the Time and Work, Speed, Number System and
# Algebra 1/2 sets or Paper II Practice 01. Every other question is a past type plus a twist.
# Build: python3 .claude/skills/aso-mock/scripts/build.py tools/maths_arith_alg2_questions.py
# First option is right (the builder shuffles). Order given, families spread by hand.

META = dict(
    paper="maths",
    title="ASO Arithmetic & Algebra Mock 02",
    hub_title="Arithmetic & Algebra Mock 02",
    masthead="Ari+Alg M02",
    heading="Paper II (B) · Arithmetic and Algebra · Mock 02",
    tagline="50 <b>moderate-to-hard</b> questions on arithmetic and algebra,<br>a new set drawn from the 2018, 2021 and 2025 papers.",
    key="aso-maths-arith-alg-2",
    code="AA02",
    out="ASO-Maths-Mock-Arithmetic-Algebra-2.html",
    minutes=45,
    seed=20261129,
    order="given",
    date="28 Nov 2026",
    draw="python3 scripts/draw.py maths --topics ari,alg --n 50 --seed 731204",
    intro=[
        "This is the second mock on arithmetic and algebra only: fifty new questions in forty-five minutes, at the "
        "same moderate-to-hard level as Mock 01. A new plan was drawn by probability from the 2018, 2021 and 2025 "
        "papers: 37 arithmetic questions and 13 algebra questions. None of the questions repeats Mock 01 or any older "
        "maths set.",
        "Each question takes a type the examiner has asked and adds a twist. Two are real past questions word for word "
        "(2021 Q55 and 2021 Q72). Every answer shows the working, the common trap, the past question it grew from and "
        "the next twist to expect. Press Copy answers at the end and paste the report into the chat for a redo set.",
    ],
)

Q = []
def add(s, q, o, e, k="one", n=False, c=False, a=None, **x):
    d = dict(s=s, q=q, o=o, e=e, k=k, n=n, c=c, a=a); d.update(x); Q.append(d)

A = "Arithmetic"
G = "Algebra"

# ================================================================ ARITHMETIC (37)

add(A, "A alone can finish a work in 9 days less than B alone. Working together, they finish it in 6 days. "
       "In how many days can B alone finish the work?",
    ["18 days", "15 days", "21 days", "12 days"],
    "Let B take x days, so A takes x − 9. 1/x + 1/(x − 9) = 1/6, so 6(2x − 9) = x(x − 9), which gives x² − 21x + 54 = 0 "
    "= (x − 18)(x − 3). x = 3 is impossible (A would take −6 days), so B takes 18 days and A takes 9. Check: "
    "1/9 + 1/18 = 1/6. Trap: 15 days is just 6 + 9. Grew from: 2018 Q61 and 2025 Q91 (two workers together). "
    "Next twist: A takes 5 days less than B and 6 days longer than the pair.",
    calc="18")

add(A, "An article is sold at a discount of 12% on its marked price and gives a profit of 10%. If it were sold at "
       "the marked price, what would be the profit per cent?",
    ["25%", "20%", "22%", "28%"],
    "Let the cost price be 100. Selling price = 110, and this is 88% of the marked price. Marked price = 110 ÷ 0.88 = 125. "
    "Selling at 125 gives a profit of 25%. Trap: 22% simply adds 12 and 10. Grew from: 2025 Q72 and Q89 (profit and "
    "loss) and 2018 Q59. Next twist: the marked price is above cost by x% and the discount and profit are asked.",
    calc="110/0.88-100")

add(A, "(1 − 1/2)(1 − 1/3)(1 − 1/4) … (1 − 1/50) = ?",
    ["1/50", "1/49", "1/25", "49/50"],
    "Each bracket is (n − 1)/n: 1/2 × 2/3 × 3/4 × … × 49/50. Everything cancels except 1/50. Trap: 1/49 or 49/50 from "
    "miscounting the last bracket. Grew from: 2018 Q51 and 2021 Q51 (telescoping series). Next twist: the sum "
    "version, 1/(2·3) + 1/(3·4) + … + 1/(49·50).",
    calc="1/50")

add(A, "The value of 1 ÷ [1 + 1 ÷ (2 + 1 ÷ (3 + 1/4))] is:",
    ["30/43", "43/30", "13/30", "17/43"],
    "Work from the inside. 3 + 1/4 = 13/4. Then 2 + 1 ÷ (13/4) = 2 + 4/13 = 30/13. Then 1 + 1 ÷ (30/13) = 1 + 13/30 = 43/30. "
    "Finally 1 ÷ (43/30) = 30/43. Trap: stopping one step early gives 43/30. Grew from: 2018 Q51 and 2021 Q51 (fraction "
    "series) and the nested-fraction type in the map. Next twist: a continued fraction with decimals.",
    calc="30/43")

add(A, "The ratio of the present ages of two persons is 4 : 5. After 8 years the ratio will be 5 : 6. What was the "
       "age of the younger person 3 years ago?",
    ["29 years", "32 years", "40 years", "35 years"],
    "Let the ages be 4x and 5x. (4x + 8)/(5x + 8) = 5/6, so 24x + 48 = 25x + 40 and x = 8. The ages are 32 and 40. "
    "Three years ago the younger was 32 − 3 = 29. Trap: 32 stops before the last step. Grew from: 2025 Q52 and Q85 "
    "(ages). Next twist: the sum of the ages after some years is given instead of a ratio.",
    calc="32-3")

add(A, "The average of 11 numbers is 60. The average of the first 6 is 58 and the average of the last 6 is 63. "
       "What is the 6th number?",
    ["66", "63", "60", "69"],
    "The sum of all 11 = 660. The first 6 add up to 348 and the last 6 add up to 378, together 726. The 6th number is "
    "counted twice, so it equals 726 − 660 = 66. Trap: 63 is the last six's average. Grew from: 2021 Q95 and Q96 "
    "(averages of overlapping groups). Next twist: the average of 9 numbers with the 5th number in both halves.",
    calc="6*58+6*63-11*60")

add(A, "A can run 1 km in 3 minutes 10 seconds and B can run 1 km in 3 minutes 20 seconds. In a 1 km race, by how "
       "many metres does A beat B?",
    ["50 m", "40 m", "60 m", "30 m"],
    "A takes 190 seconds. B's speed = 1000 ÷ 200 = 5 m/s, so in 190 seconds B runs 950 m. A wins by 1000 − 950 = 50 m. "
    "Trap: 10 seconds is the time gap, not a distance; use B's speed, 10 × 5 = 50 m. Grew from: 2025 Q60 and Q65 (beats by metres or by "
    "seconds). Next twist: by how many seconds does A beat B (10 seconds)?",
    calc="1000-190*1000/200")

add(A, "If the H.C.F. of 306 and 657 is 9, what is their L.C.M.?",
    ["22338", "22328", "20138", "22248"],
    "H.C.F. × L.C.M. = product of the two numbers. 306 × 657 = 201,042, and 201,042 ÷ 9 = 22,338. Check by factors: "
    "306 = 2 × 9 × 17 and 657 = 9 × 73, so L.C.M. = 9 × 2 × 17 × 73 = 22,338. Grew from: 2015 Q51-53 (H.C.F. × L.C.M. = "
    "product) and 2025 Q79. Next twist: the product and the L.C.M. are given, find the H.C.F.",
    calc="306*657//9")

add(A, "What is the least number which, when divided by 12, 18 and 30, leaves a remainder 5 in each case, and is also "
       "exactly divisible by 7?",
    ["1085", "905", "545", "1265"],
    "L.C.M. of 12, 18, 30 = 180, so the number is 180k + 5. Now 180 leaves remainder 5 when divided by 7, so 180k + 5 "
    "leaves 5k + 5 (mod 7). That must be 0, so k = 6 (5 × 6 + 5 = 35). The number is 180 × 6 + 5 = 1085, and 1085 ÷ 7 = 155. "
    "Trap: 905, 545 and 1265 have the form 180k + 5 but are not multiples of 7. Grew from: 2018 Q82 and 2025 Q70 (least number with given "
    "remainders). Next twist: the greatest 4-digit number of this kind.",
    calc="180*6+5")

add(A, "The sum of the present ages of a father and his son is 60 years. Six years ago the father's age was five times "
       "the age of the son. After how many years will the father's age be three times the son's age?",
    ["2 years", "3 years", "4 years", "5 years"],
    "Let the son be s now, so the father is 60 − s. Six years ago: 60 − s − 6 = 5(s − 6), so 54 − s = 5s − 30 and s = 14. "
    "The father is 46. After x years: 46 + x = 3(14 + x) = 42 + 3x, so 2x = 4 and x = 2. Check: 48 = 3 × 16. "
    "Grew from: 2025 Q52 and Q85. Next twist: the "
    "sum of ages after some years is given.",
    calc="2")

add(A, "What is the least number by which 1512 must be multiplied so that the product is a perfect square?",
    ["42", "21", "14", "7"],
    "Break 1512 into prime factors: 1512 = 2³ × 3³ × 7. For a perfect square, every power must be even. The powers of "
    "2 and 3 are odd (3) and the power of 7 is odd (1), so multiply by 2 × 3 × 7 = 42. The product is 2⁴ × 3⁴ × 7² = "
    "63,504 = 252². Trap: 7 alone fixes only one prime. Grew from: 2025 Q99 (the smallest number to add for a perfect "
    "square) and 2021 Q63. Next twist: the least number by which to divide.",
    calc="42")

add(A, "If x = 3 + 2√2, then the value of x² + 1/x² is:",
    ["34", "36", "32", "18"],
    "1/x = 1/(3 + 2√2) = (3 − 2√2)/(9 − 8) = 3 − 2√2. So x + 1/x = 6. Then x² + 1/x² = (x + 1/x)² − 2 = 36 − 2 = 34. "
    "Trap: 36 forgets the −2. Grew from: 2025 Q93 (rationalising) and 2018 Q65 (surd equation). Next twist: x³ + 1/x³ = "
    "6³ − 3 × 6 = 198.",
    calc="34")

add(A, "A, B and C invest in the ratio 3 : 4 : 5 for 4, 6 and 8 months respectively. If the total profit is "
       "Rs. 7,600, what is B's share?",
    ["Rs. 2,400", "Rs. 2,000", "Rs. 1,800", "Rs. 3,200"],
    "Share ∝ money × time. A : B : C = 3 × 4 : 4 × 6 : 5 × 8 = 12 : 24 : 40 = 3 : 6 : 10. The total is 19 parts. B's share = "
    "7,600 × 6/19 = Rs. 2,400. Trap: using the money ratio 3 : 4 : 5 alone gives B = Rs. 2,533. Grew from: 2025 Q81 and "
    "Q63. Next twist: the investment is given as amounts and a partner leaves early.",
    calc="7600*6/19")

add(A, "A batsman's average after 12 innings is 48. In his 13th innings he scores some runs and his average rises "
       "by 2 runs. How many runs did he score in the 13th innings?",
    ["74", "72", "76", "50"],
    "Total after 12 innings = 12 × 48 = 576. New average 50 over 13 innings = 650. Runs in the 13th innings = 650 − 576 = 74. "
    "Shortcut: 50 + 12 × 2 = 74 (the new average plus 2 for each earlier innings). Trap: 50 is only the new average. "
    "Grew from: 2025 Q68 and 2021 Q95. Next twist: the average falls and the score is asked.",
    calc="13*50-12*48")

add(A, "What is the greatest 4-digit number which, when divided by 6, 8 and 9, leaves a remainder 5 in each case?",
    ["9941", "9936", "9869", "9933"],
    "L.C.M. of 6, 8, 9 = 72. The greatest 4-digit multiple of 72: 9999 ÷ 72 = 138 remainder 63, so 72 × 138 = 9936. Add the "
    "remainder: 9936 + 5 = 9941. Trap: 9936 forgets the remainder 5. Grew from: 2018 Q52 (the least 5-digit number "
    "divisible by 41) and 2025 Q56. Next twist: the least 4-digit number of this kind (1013).",
    calc="72*138+5")

add(A, "A watch gains 5 seconds in every 3 minutes. It was set right at 7 a.m. What time will it show when the "
       "correct time is 4 p.m. on the same day?",
    ["4:15 p.m.", "4:10 p.m.", "4:20 p.m.", "4:05 p.m."],
    "From 7 a.m. to 4 p.m. is 9 hours = 540 minutes = 180 periods of 3 minutes. The watch gains 180 × 5 = 900 seconds = "
    "15 minutes. When the true time is 4:00 p.m. it shows 4:15 p.m. Grew from: 2025 Q55 and Q69. Next twist: the watch loses and shows 3:45 p.m.; find the true time.",
    nocalc=True)

add(A, "If the five-digit number 7x35y is exactly divisible by 72, what is the value of x + y?",
    ["3", "4", "2", "10"],
    "72 = 8 × 9, and the two factors have no common factor. For 8, the last three digits 35y must divide by 8: 352 = 8 × 44, "
    "so y = 2. For 9, the digit sum must divide by 9: 7 + x + 3 + 5 + 2 = 17 + x, so x = 1. The number is 71,352 = 72 × 991. "
    "x + y = 3. Trap: using the test for 6 or 12 instead of 8 and 9. Grew from: 2025 Q100 (653xy divisible by 90). "
    "Next twist: divisible by 88 (8 and 11).",
    calc="1+2")

add(A, "Two cars start at the same time from towns 240 km apart and drive towards each other at 50 km/h and 70 km/h. "
       "A bird starts with them and flies between the cars at 120 km/h until they meet. How far does the bird fly?",
    ["240 km", "120 km", "200 km", "280 km"],
    "The cars meet after 240 ÷ (50 + 70) = 2 hours. The bird flies the whole time at 120 km/h, so it covers 120 × 2 = 240 km. "
    "No need to add up the back-and-forth trips. Trap: 120 km is only one hour of flight. Grew from: 2025 Q54 and Q64 "
    "(speed and time). Next twist: the cars start in the same direction.",
    calc="120*240/(50+70)")

add(A, "The incomes of A and B are in the ratio 5 : 4 and their expenditures are in the ratio 3 : 2. If each saves "
       "Rs. 1,600, what is A's income?",
    ["Rs. 4,000", "Rs. 5,000", "Rs. 3,200", "Rs. 4,800"],
    "Let the incomes be 5x and 4x and the expenditures 3y and 2y. 5x − 3y = 1600 and 4x − 2y = 1600. From the second, "
    "y = 2x − 800. Then 5x − 6x + 2400 = 1600, so x = 800. A's income = 5 × 800 = Rs. 4,000. Check: A spends 2,400 and B "
    "spends 1,600 (B's income 3,200). Grew from: 2018 Q67 and 2021 Q67 (ratios). "
    "Next twist: the expenditure of B is asked.",
    calc="5*800")

add(A, "A student walks to a bus stop at 4 km/h and misses the bus by 5 minutes. If he walks at 5 km/h, he reaches "
       "10 minutes before the bus arrives. How far is the bus stop?",
    ["5 km", "4 km", "6 km", "3 km"],
    "The two walking times differ by 5 + 10 = 15 minutes = 1/4 hour. d/4 − d/5 = 1/4, so d/20 = 1/4 and d = 5 km. "
    "Trap: using only the 10 minutes, not 5 + 10, gives 3⅓ km. Grew from: 2025 Q54 (late and early at "
    "two speeds). Next twist: the time the bus arrives is asked.",
    calc="5")

add(A, "[(799 + 267)² − (799 − 267)²] ÷ (799 × 267) = ?",
    ["4", "2", "532", "1066"],
    "Exact past question (2021 Q55). (a + b)² − (a − b)² = 4ab, so the whole expression is 4ab ÷ ab = 4. "
    "No arithmetic with the big numbers is needed. Family: 2018 Q55 (the same with 489 and 375). Next twist: "
    "(a + b)² + (a − b)² over a² + b² = 2.",
    src="2021 Q55", calc="4")

add(A, "12 men can finish a work in 15 days. After 5 days, 8 more men join them. In how many days in all is the work "
       "finished?",
    ["11 days", "10 days", "12 days", "9 days"],
    "Total work = 12 × 15 = 180 man-days. In 5 days 12 men do 60, leaving 120. Now there are 20 men, so the rest takes "
    "120 ÷ 20 = 6 days. Total = 5 + 6 = 11 days. Trap: 6 days is only the second part. Grew from: 2025 Q53 and Q77 "
    "(men, days, extra men). Next twist: some men leave after some days.",
    calc="5+120/20")

add(A, "(555 × 555 × 555 + 445 × 445 × 445) ÷ (555 × 555 − 555 × 445 + 445 × 445) = ?",
    ["1000", "110", "100", "10"],
    "This is (a³ + b³) ÷ (a² − ab + b²) = a + b with a = 555 and b = 445. So the value is 555 + 445 = 1000. Trap: 110 is "
    "a − b. Grew from: 2018 Q55 and 2021 Q55 (identities with big numbers). Next twist: the a³ − b³ form, which gives "
    "a − b.",
    calc="(555**3+445**3)/(555**2-555*445+445**2)")

add(A, "In a race of 600 m, A can beat B by 60 m. In a race of 500 m, B can beat C by 25 m. By how many metres will "
       "A beat C in a race of 400 m?",
    ["58 m", "52 m", "60 m", "40 m"],
    "A : B = 600 : 540 = 10 : 9. B : C = 500 : 475 = 20 : 19. So A : C = (10/9) × (20/19) = 200 : 171. When A runs 400 m, "
    "C runs 400 × 171/200 = 342 m, so A wins by 58 m. Trap: 60 m adds the two margins scaled to 400 m (40 + 20). Grew from: 2025 Q60 and Q65. Next twist: three runners and a start.",
    calc="400-400*171/200")

add(A, "A man has 50 coins, some of 50 paise and the rest of 25 paise. The total value is Rs. 17. How many 50-paise "
       "coins has he?",
    ["18", "20", "22", "16"],
    "If all 50 coins were 25 paise they would be worth Rs. 12.50. The extra Rs. 4.50 = 450 paise comes from replacing 25-paise "
    "coins by 50-paise coins, 25 paise more each. So 450 ÷ 25 = 18 coins of 50 paise (and 32 of 25 paise: 900 + 800 = 1700). "
    "Trap: 32 is the number of 25-paise coins. Grew from: 2025 Q75 (heads and feet, the same two-groups method). "
    "Next twist: three kinds of coin.",
    calc="(1700-50*25)/25")

add(A, "A boat rows at 6 km/h in still water and the river flows at 2 km/h. It takes 1½ hours longer to go a certain "
       "distance upstream than downstream. What is the distance?",
    ["12 km", "9 km", "15 km", "18 km"],
    "Downstream speed = 8 km/h and upstream speed = 4 km/h. d/4 − d/8 = 1.5, so d/8 = 1.5 and d = 12 km. Check: "
    "upstream 3 hours, downstream 1.5 hours. Trap: 18 km uses the difference of speeds, 2 km/h, instead of the "
    "difference of times. Grew from: 2015 Q66 (one hour more upstream for 24 km). Next twist: the time upstream "
    "and downstream are asked.",
    calc="1.5*8")

add(A, "The population of a town increased by 10% in the first year and decreased by 10% in the second year. If it is "
       "now 19,800, what was it at the beginning?",
    ["20,000", "19,600", "21,780", "18,000"],
    "Net factor = 1.10 × 0.90 = 0.99. Original = 19,800 ÷ 0.99 = 20,000. Trap: 19,800 is wrong because +10% and −10% "
    "do not cancel (the base changes). Grew from: 2025 Q66 (side up 25%, area up 56.25%) and 2021 Q57. Next twist: "
    "the change in the second year is a different percentage.",
    calc="19800/0.99")

add(A, "A boy reads 2/7 of a book on the first day and 3/5 of the remaining pages on the second day. If 40 pages are "
       "still unread, how many pages does the book have?",
    ["140", "120", "200", "280"],
    "After day 1, 5/7 remain. On day 2 he reads 3/5 of 5/7 = 3/7 of the book. Left = 1 − 2/7 − 3/7 = 2/7. So 2/7 of the "
    "book = 40 and the book has 40 × 7/2 = 140 pages. Trap: reading 3/5 of the whole book (not of the rest) gives a wrong total. Grew "
    "from: 2025 Q51 (3/8 and 4/5 of the rest, 30 pages left). Next twist: three days.",
    calc="40*7/2")

add(A, "1/(3 × 7) + 1/(7 × 11) + 1/(11 × 15) + 1/(15 × 19) = ?",
    ["4/57", "16/57", "1/57", "2/19"],
    "Each term is (1/4)(1/a − 1/b) because the gap is 4. The sum telescopes: (1/4)(1/3 − 1/19) = (1/4)(16/57) = 4/57. "
    "Trap: 16/57 forgets to divide by the gap 4. Grew from: 2018 Q51 (gap 3) and 2021 Q51 (gap 2). Next twist: the "
    "numerators are not 1, such as 4/(3 × 7).",
    calc="4/57")

add(A, "A train passes two bridges of lengths 800 m and 400 m in 100 seconds and 60 seconds respectively. What is "
       "the speed of the train?",
    ["36 km/h", "40 km/h", "72 km/h", "30 km/h"],
    "The extra 400 m of bridge takes the extra 40 seconds, so the speed is 400 ÷ 40 = 10 m/s = 10 × 18/5 = 36 km/h. "
    "(The train's own length is 10 × 100 − 800 = 200 m.) Trap: 72 km/h is 20 m/s, from 800 ÷ 40. Grew from: 2025 Q59 and "
    "Q82 (trains). Next twist: the length of the train is asked.",
    calc="400/40*18/5")

add(A, "Three pipes A, B and C together can fill a tank in 8 hours. A is twice as fast as B, and B is twice as fast as "
       "C. How long will A alone take to fill the tank?",
    ["14 hours", "28 hours", "16 hours", "12 hours"],
    "The rates are in the ratio 4 : 2 : 1, so A fills 4/7 of the combined work. Together they fill 1/8 per hour, so A fills "
    "(4/7)(1/8) = 1/14 per hour. A alone takes 14 hours. Trap: 28 hours is B's time. Grew from: 2025 Q91 and Q97 "
    "(two pipes). Next twist: the pipes fill in turn.",
    calc="14")

add(A, "The product of two numbers is 4107 and their H.C.F. is 37. What is the greater number?",
    ["111", "74", "148", "185"],
    "Write the numbers as 37a and 37b with a and b having no common factor. 37² × ab = 4107, so ab = 4107 ÷ 1369 = 3. "
    "So a and b are 1 and 3, and the numbers are 37 and 111. The greater is 111. Trap: 74 (a = 2) gives a product of "
    "37 × 74 = 2738. Grew from: 2025 Q79 (numbers from the H.C.F.). Next twist: the sum is given instead of the product.",
    calc="37*3")

add(A, "The difference between compound interest and simple interest on a sum for 3 years at 10% per annum is "
       "Rs. 31. What is the sum?",
    ["Rs. 1,000", "Rs. 1,100", "Rs. 900", "Rs. 1,200"],
    "For 3 years, CI − SI = P (r/100)² (3 + r/100) = P × 0.01 × 3.1 = 0.031P. So 0.031P = 31 and P = Rs. 1,000. Check: SI "
    "= 300 and CI = 1000 × (1.331 − 1) = 331. Trap: using the 2-year shortcut P(r/100)² gives Rs. 3,100. Grew from: "
    "2018 Q60 and 2021 Q60 (CI − SI for 2 years). Next twist: the 2-year difference with a different rate.",
    calc="31/0.031")

add(A, "In a 400 m race, A beats B by 40 m and C by 76 m. By how many metres does B beat C in the same race?",
    ["40 m", "36 m", "44 m", "38 m"],
    "When A has run 400 m, B has run 360 m and C has run 324 m. So C runs 324 while B runs 360, ratio 9 : 10. When B runs "
    "400 m, C runs 400 × 9/10 = 360 m. B wins by 40 m. Trap: 36 m is the plain difference 76 − 40. Grew from: 2025 Q60 "
    "and Q65. Next twist: the same in a 1 km race.",
    calc="400-400*324/360")

add(A, "If 18 men working 8 hours a day can build a wall 40 m long in 12 days, in how many days can 12 men working "
       "6 hours a day build a similar wall 30 m long?",
    ["18 days", "24 days", "16 days", "12 days"],
    "Work in man-hours: 18 × 8 × 12 = 1,728 for 40 m. For 30 m the work is 1,728 × 30/40 = 1,296 man-hours. Now 12 men × 6 "
    "hours = 72 man-hours a day, so the time = 1,296 ÷ 72 = 18 days. Trap: 24 days forgets that the wall is shorter. "
    "Grew from: 2025 Q77 and Q83 (men, hours, days). Next twist: a wall of different height as well as length.",
    calc="1296/72")

add(A, "In an election 20% of the voters did not vote. Of those who voted, 5% of the votes were invalid. The "
       "winner got 55% of the valid votes. If there were 6,000 voters, by how many votes did the winner win?",
    ["456", "480", "528", "600"],
    "Voters who voted = 6,000 × 0.8 = 4,800. Valid votes = 4,800 × 0.95 = 4,560. The winner got 55% and the loser 45%, so the "
    "margin is 10% of 4,560 = 456. Trap: 480 is 10% of 4,800 (invalid votes ignored). Grew from: 2025 Q96 and Q58 "
    "(percentages of a total). Next twist: the winner's margin is given and the number of voters is asked.",
    calc="6000*0.8*0.95*0.10")

add(A, "If a : b = 2 : 3, b : c = 4 : 5 and a + b + c = 70, what is the value of c?",
    ["30", "25", "35", "28"],
    "Make b the same in both ratios: a : b = 8 : 12 and b : c = 12 : 15, so a : b : c = 8 : 12 : 15. The total is 35 parts, "
    "so each part is 70 ÷ 35 = 2 and c = 15 × 2 = 30. Trap: 35 comes from reading the ratio as 2 : 3 : 5 without matching b. Grew from: "
    "2018 Q68 and 2021 Q68 (proportion) and 2025 Q92. Next twist: the ratio of a to c.",
    calc="15*2")

# ================================================================ ALGEBRA (13)

add(G, "In a class of 60 students, 35 like Mathematics, 30 like Science and 12 like neither. How many students like "
       "both Mathematics and Science?",
    ["17", "13", "18", "23"],
    "Students who like at least one subject = 60 − 12 = 48. n(M ∪ S) = n(M) + n(S) − n(M ∩ S), so 48 = 35 + 30 − n(M ∩ S) "
    "and n(M ∩ S) = 17. Trap: 18 is 48 − 30, the number who like only Mathematics. Grew from: 2018 Q78 and 2021 Q78 "
    "(overlap word problems). Next twist: only one subject.",
    calc="35+30-48")

add(G, "If (3x + 5y) : (3x − 5y) = 7 : 3, then x : y is:",
    ["25 : 6", "6 : 25", "5 : 3", "7 : 3"],
    "Cross-multiply: 3(3x + 5y) = 7(3x − 5y), so 9x + 15y = 21x − 35y and 50y = 12x. Then x : y = 50 : 12 = 25 : 6. Check: x = 25, "
    "y = 6 gives 75 + 30 = 105 and 75 − 30 = 45, ratio 7 : 3. Trap: 6 : 25 turns it over. Grew from: 2018 Q67 and "
    "2021 Q67. Next twist: find (x² + y²) : (x² − y²).",
    calc="25")

add(G, "For what value of k does the pair of equations kx + 3y = k − 3 and 12x + ky = k have no solution?",
    ["−6", "6", "12", "−12"],
    "No solution needs k/12 = 3/k ≠ (k − 3)/k. From k/12 = 3/k, k² = 36, so k = 6 or −6. Now test the third ratio. For k = 6: "
    "(k − 3)/k = 3/6 = 1/2, which equals 3/k = 1/2, so the lines coincide (infinitely many solutions). For k = −6: "
    "(k − 3)/k = (−9)/(−6) = 3/2, but 3/k = −1/2, so they differ. So k = −6. Trap: 6 gives infinitely many solutions, "
    "not none. Grew from: 2021 Q71 and 2018 Q71. Next twist: asked for the value giving infinitely many solutions.",
    calc="-6")

add(G, "If 3^(x + y) = 81 and 3^(x − y) = 3, what is the value of x × y?",
    ["15/4", "4", "3", "5/2"],
    "Equal bases: x + y = 4 and x − y = 1. Adding, 2x = 5, so x = 5/2; then y = 3/2. Product = (5/2)(3/2) = 15/4. "
    "Trap: 5/2 is only x. Grew from: 2021 Q65 and 2025 Q80 (powers with equal bases). Next twist: 2^(x + y) = 32 and "
    "2^(x − y) = 8 with a third unknown.",
    calc="15/4")

add(G, "If α and β are the roots of x² − 6x + k = 0 and 3α + 2β = 20, what is the value of k?",
    ["−16", "16", "−8", "8"],
    "α + β = 6, so 3α + 2β = 2(α + β) + α = 12 + α = 20 and α = 8. Then β = −2 and k = αβ = −16. Check: 64 − 48 − 16 = 0 for "
    "x = 8. Trap: 16 loses the sign. Grew from: 2018 Q64 and 2021 Q64 (α + β and α − β are given). Next twist: "
    "one root is a multiple of the other.",
    calc="-16")

add(G, "If α, β and γ are the zeroes of the polynomial x³ − 4x² + x + 6, what is the value of α² + β² + γ²?",
    ["14", "16", "18", "10"],
    "Sum of zeroes = 4 and sum of products two at a time = 1. α² + β² + γ² = (α + β + γ)² − 2(αβ + βγ + γα) = 16 − 2 = 14. "
    "Check: the zeroes are −1, 2 and 3, and 1 + 4 + 9 = 14. Trap: 16 forgets the 2 × 1. Grew from: 2015 Q71-73 "
    "(zeroes and the sum of their squares). Next twist: the sum of the cubes.",
    calc="14")

add(G, "If a/3 = b/4 = c/7 and a − b + c = 24, then a + b + c = ?",
    ["56", "48", "42", "64"],
    "Let a = 3k, b = 4k and c = 7k. a − b + c = 3k − 4k + 7k = 6k = 24, so k = 4. Then a + b + c = 14k = 56. Grew from: 2021 Q67 (x/5 = y/9) and 2018 Q67. Next twist: a² + b² + c².",
    calc="14*4")

add(G, "What is the sum of all natural numbers between 100 and 300 that are divisible by 6?",
    ["6534", "6834", "6336", "6666"],
    "The first multiple is 102 and the last is 294. Number of terms = (294 − 102)/6 + 1 = 33. Sum = 33/2 × (102 + 294) = "
    "33 × 198 = 6,534. Trap: 6,834 counts 300 as well (not 'between'); 6,336 forgets the +1. Grew from: 2021 Q77 and Q82 "
    "(sums and counts of numbers divisible by a given number). Next twist: divisible by 6 or 9.",
    calc="33*198")

add(G, "For what value of k are the numbers k + 2, 4k − 6 and 3k − 2 three consecutive terms of an A.P.?",
    ["3", "2", "4", "6"],
    "In an A.P. the middle term is the mean of the other two, so 2(4k − 6) = (k + 2) + (3k − 2). 8k − 12 = 4k, so k = 3. "
    "The terms are 5, 6, 7. Trap: using 2(k + 2) as the middle gives a different k. Grew from: 2018 Q75 (which are "
    "in A.P.). Next twist: the terms are given with a square or a fraction.",
    calc="3")

add(G, "The sum of the first 15 terms of an A.P. is 600 and its common difference is 5. What is the first term?",
    ["5", "10", "8", "15"],
    "S15 = 15/2 × [2a + 14 × 5] = 600, so 2a + 70 = 80 and a = 5. Check: the A.P. is 5, 10, 15, …, 75 and 15 terms average "
    "40: 15 × 40 = 600. Trap: 10 forgets the 2 in 2a. Grew from: 2018 Q77 and 2021 Q75 (sum of terms). Next twist: "
    "the first term and the sum are given, find the number of terms.",
    calc="5")

add(G, "In a town, 65% of the people read The Hindu, 40% read The Times and 25% read both. What per cent of the "
       "people read neither paper?",
    ["20%", "30%", "25%", "35%"],
    "Readers of at least one = 65 + 40 − 25 = 80%. So 100 − 80 = 20% read neither. Trap: 35% is 100 − 65, forgetting "
    "the second paper. Grew from: 2021 Q78 and 2018 Q78 (n(A ∪ B)). Next twist: the % reading only one paper (55%).",
    calc="100-(65+40-25)")

add(G, "If M is the matrix [[3, −1], [2, 5]] and N is the matrix [[1, 4], [−2, 0]] (each inner bracket is a row), "
       "what is the sum of all the entries of 3M − 2N?",
    ["21", "15", "33", "9"],
    "3M = [[9, −3], [6, 15]] and 2N = [[2, 8], [−4, 0]]. So 3M − 2N = [[7, −11], [10, 15]]. The sum of all entries is "
    "7 − 11 + 10 + 15 = 21. Trap: 33 is the sum of the entries of 3M + 2N. Grew from: 2021 "
    "Q70 (2M + N) and 2018 Q70 (M + 2N). Next twist: the determinant of the result.",
    calc="21")

add(G, "The discriminant of the quadratic equation 3x² − 5x + 3 = 0 is:",
    ["−11", "−5", "3", "−1"],
    "Exact past question (2021 Q72). b² − 4ac = (−5)² − 4 × 3 × 3 = 25 − 36 = −11. Because it is negative, the equation "
    "has no real roots. Family: 2018 Q72 (2x² − 4x + 3 = 0, value −8). Next twist: the nature of the roots or the value "
    "of k for equal roots.",
    src="2021 Q72", calc="-11")
