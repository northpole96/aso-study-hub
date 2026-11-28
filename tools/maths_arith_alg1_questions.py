# Arithmetic & Algebra Mock 01 (28 Nov 2026): 50 questions, 45 minutes, syllabus topics (a) Arithmetic and
# (b) Algebra only. User: "Make a 50 question mock on algebra and arithmetic only, moderate-to hard".
# Plan: python3 .claude/skills/aso-mock/scripts/draw.py maths --topics ari,alg --n 50 --seed 555924649
# (36 arithmetic, 14 algebra; exact past questions 2025 Q76 and 2025 Q65).
# Every other question is the next angle of a past question with a twist, and none repeats Maths Mock 01, the
# Time and Work, Speed, Number System, Algebra 1/2 sets or Paper II Practice 01.
# Build: python3 .claude/skills/aso-mock/scripts/build.py tools/maths_arith_alg1_questions.py  (calc re-checks answers)
# First option is right (the builder shuffles). Order is given: Arithmetic block, then Algebra, families spread by hand.

META = dict(
    paper="maths",
    title="ASO Arithmetic & Algebra Mock 01",
    hub_title="Arithmetic & Algebra Mock 01",
    masthead="Ari+Alg M01",
    heading="Paper II (B) · Arithmetic and Algebra · Mock 01",
    tagline="50 <b>moderate-to-hard</b> questions on arithmetic and algebra,<br>drawn from the 2018, 2021 and 2025 papers.",
    key="aso-maths-arith-alg-1",
    code="AA01",
    out="ASO-Maths-Mock-Arithmetic-Algebra-1.html",
    minutes=45,
    seed=20261128,
    order="given",
    date="28 Nov 2026",
    draw="python3 scripts/draw.py maths --topics ari,alg --n 50 --seed 555924649",
    intro=[
        "This mock covers only the first two topics of the Maths syllabus, arithmetic and algebra: fifty questions "
        "in forty-five minutes. The plan was drawn by probability from the 2018, 2021 and 2025 papers, so arithmetic "
        "gets 36 questions (the 2025 paper was almost all arithmetic) and algebra gets 14 (the Class 10 template of "
        "2018 and 2021).",
        "The level is moderate to hard. Most questions take a type the examiner has asked and add a twist: the "
        "unknown is reversed, a second condition is added, or two steps are joined. Two questions are real past "
        "questions word for word (2025 Q65 and 2025 Q76). Every answer shows the working, the past question it grew "
        "from and the next twist to expect. Press Copy answers at the end and paste the report into the chat for a "
        "redo set.",
    ],
)

Q = []
def add(s, q, o, e, k="one", n=False, c=False, a=None, **x):
    d = dict(s=s, q=q, o=o, e=e, k=k, n=n, c=c, a=a); d.update(x); Q.append(d)

A = "Arithmetic"
G = "Algebra"

# ================================================================ ARITHMETIC (36)

add(A, "In an examination, a candidate who gets 30% of the maximum marks fails by 30 marks. Another candidate who "
       "gets 45% of the maximum marks gets 15 marks more than the pass mark. What percentage of marks is needed to pass?",
    ["40%", "36%", "38%", "42%"],
    "Let the maximum be M. The pass mark is 0.30M + 30 and also 0.45M − 15. So 0.15M = 45 and M = 300. "
    "Pass mark = 90 + 30 = 120, which is 120/300 = 40%. Trap: 36% or 38% come from taking the average of 30% and 45% "
    "without the marks. Grew from: 2025 Q96 (marks as a share of a total). Next twist: the pass mark is given and "
    "the maximum is asked.",
    calc="(0.30*300+30)/300*100")

add(A, "A man covers a journey of 600 km partly by train and partly by car. If he goes 120 km by train and the rest "
       "by car, he takes 8 hours. If he goes 200 km by train and the rest by car, he takes 20 minutes longer. "
       "What is the ratio of the speed of the train to that of the car?",
    ["3 : 4", "4 : 3", "2 : 3", "3 : 2"],
    "Let the train take u hours per km and the car v hours per km. Then 120u + 480v = 8 and 200u + 400v = 25/3. "
    "From the first, u = (8 − 480v)/120. Putting it in the second: 40/3 − 800v + 400v = 25/3, so 400v = 5 and "
    "v = 1/80, u = 1/60. Train 60 km/h, car 80 km/h, ratio 3 : 4. Trap: 4 : 3 is the ratio the wrong way round. "
    "Grew from: 2021 Q62 (ratio of the speeds of two trains). Next twist: the total time is asked for a third split.",
    calc="60/80*4")

add(A, "Two pipes can fill a tank in 10 hours and 15 hours respectively. When both are opened together, a leak at "
       "the bottom makes the tank take 1 hour more to fill. In how many hours can the leak alone empty the full tank?",
    ["42 hours", "35 hours", "36 hours", "48 hours"],
    "Together the pipes fill 1/10 + 1/15 = 1/6 of the tank per hour, so 6 hours. With the leak it takes 7 hours. "
    "Leak per hour = 1/6 − 1/7 = 1/42, so the leak empties the tank in 42 hours. Shortcut: leak time = (6 × 7) ÷ (7 − 6). "
    "Grew from: 2025 Q74 (one pump and a leak, 3 hours becomes 3½). Twist here: two pipes first. "
    "Next twist: the leak is found only after the tank is half full.",
    calc="6*7/(7-6)")

add(A, "What is the remainder when (17²³ + 23²³) is divided by 40?",
    ["0", "1", "17", "23"],
    "Rule: when n is odd, aⁿ + bⁿ is always divisible by a + b. Here n = 23 is odd and 17 + 23 = 40, so the remainder "
    "is 0. (For aⁿ − bⁿ, the number a − b always divides it, for any n.) Grew from: the remainder questions of "
    "2025 Q56 and Q70. Next twist: (19³⁷ − 7³⁷) divided by 12.",
    calc="(17**23+23**23)%40")

add(A, "The value of √(248 + √(52 + √144)) is:",
    ["16", "14", "18", "15"],
    "Work from the inside out. √144 = 12. Then 52 + 12 = 64 and √64 = 8. Then 248 + 8 = 256 and √256 = 16. "
    "Trap: starting from the outside gives nothing clean. Grew from: 2021 Q63 (√1.5625) and 2025 Q86 (a root with a "
    "fraction inside). Next twist: a nested root with decimals, such as √(0.0169 × 0.0004).",
    calc="math.sqrt(248+math.sqrt(52+math.sqrt(144)))")

add(A, "If 6 men working 6 hours a day can do 6 units of work in 6 days, how many units of work can 12 men do "
       "working 12 hours a day for 12 days?",
    ["48", "12", "24", "96"],
    "Work is in proportion to men × hours × days. 6 × 6 × 6 = 216 man-hour-days do 6 units, so one unit needs 36. "
    "12 × 12 × 12 = 1728 man-hour-days do 1728 ÷ 36 = 48 units. Shortcut: each factor doubles, so the work grows "
    "2 × 2 × 2 = 8 times: 6 × 8 = 48. Trap: 12 (doubling once) or 96. Grew from: 2025 Q73 (x men, x hours, x days, "
    "x units). Next twist: the general form, y³/x² units.",
    calc="12*12*12/36")

add(A, "In a group of ducks and cows, the number of legs is 24 more than twice the number of heads. How many cows "
       "are there in the group?",
    ["12", "6", "24", "8"],
    "Let there be d ducks and c cows. Legs = 2d + 4c and heads = d + c. 2d + 4c = 2(d + c) + 24, so 2c = 24 and "
    "c = 12. The number of ducks cannot be found, and it is not needed. Trap: 24 (forgetting to halve) or 6. "
    "Grew from: 2025 Q75 (hens, goats, camels and keepers: feet 224 more than heads). Next twist: feet are 'n more "
    "than twice the heads' with three kinds of animal.",
    calc="24/2")

add(A, "A and B start a business with Rs. 20,000 and Rs. 30,000. After 4 months, A puts in Rs. 10,000 more and B "
       "takes out Rs. 10,000. At the end of the year the profit is Rs. 30,000. What is A's share?",
    ["Rs. 16,000", "Rs. 14,000", "Rs. 15,000", "Rs. 12,000"],
    "Multiply money by months. A: 20,000 × 4 + 30,000 × 8 = 3,20,000. B: 30,000 × 4 + 20,000 × 8 = 2,80,000. "
    "Ratio 32 : 28 = 8 : 7. A's share = 30,000 × 8/15 = Rs. 16,000. Trap: Rs. 12,000 uses the first amounts only "
    "(2 : 3). Grew from: 2025 Q81 (B joins after 5 months) and 2025 Q63 (cow-months of a pasture). Next twist: "
    "a partner leaves before the year ends and the shares are given.",
    calc="30000*8/15")

add(A, "What is the value of 1/(√1 + √2) + 1/(√2 + √3) + 1/(√3 + √4) + … + 1/(√99 + √100)?",
    ["9", "10", "99", "11"],
    "Rationalise one term: 1/(√n + √(n+1)) = √(n+1) − √n. The sum becomes (√2 − √1) + (√3 − √2) + … + (√100 − √99). "
    "Everything cancels except √100 − √1 = 10 − 1 = 9. Trap: 10 forgets the −1. Grew from: 2018 Q51 and 2021 Q51 "
    "(telescoping fractions 1/(1·3) + 1/(3·5) + …), joined with 2025 Q93 (rationalising surds). Next twist: the same "
    "sum stopping at √(n²), which is always n − 1.",
    calc="math.sqrt(100)-1")

add(A, "What is the angle between the hour hand and the minute hand of a clock at 4:40?",
    ["100°", "110°", "90°", "80°"],
    "Angle = |30H − 5.5M| = |30 × 4 − 5.5 × 40| = |120 − 220| = 100°. Why: the hour hand moves 0.5° a minute, so at "
    "4:40 it is at 120 + 20 = 140°; the minute hand is at 40 × 6 = 240°. Trap: 80° forgets that the hour hand moves "
    "past 4. Grew from: 2025 Q55 and Q69 (clocks that gain and lose). Next twist: the angle at a time like 7:20 is asked "
    "as the reflex angle.",
    calc="math.fabs(30*4-5.5*40)")

add(A, "The average age of 8 men goes up by 2 years when two of them, aged 21 years and 23 years, are replaced by "
       "two women. What is the average age of the two women?",
    ["30 years", "32 years", "24 years", "26 years"],
    "The total goes up by 8 × 2 = 16 years. The two women together = 21 + 23 + 16 = 60 years, so their average is "
    "30 years. Trap: 24 years adds only 2 to the average of the two men. Grew from: 2025 Q68 and 2021 Q95 (averages "
    "of groups). Next twist: the average falls and a new member's age is asked.",
    calc="(21+23+8*2)/2")

add(A, "The L.C.M. of two numbers is 48 times their H.C.F. The sum of their H.C.F. and L.C.M. is 1176. If one of "
       "the numbers is 72, what is the other?",
    ["384", "360", "288", "432"],
    "Let the H.C.F. be h. Then h + 48h = 1176, so h = 24 and L.C.M. = 1152. Product of two numbers = H.C.F. × L.C.M., "
    "so the other number = 24 × 1152 ÷ 72 = 384. Check: H.C.F.(72, 384) = 24. Grew from: 2025 Q79 (numbers from a "
    "ratio and the H.C.F.). Next twist: the H.C.F. and the sum of the numbers are given; how many pairs?",
    calc="24*1152/72")

add(A, "A's income is 20% more than B's income, and B's income is 25% less than C's income. By what percentage is "
       "A's income less than C's income?",
    ["10%", "5%", "15%", "12%"],
    "Let C = 100. B = 75 and A = 75 × 1.2 = 90. So A is 10 less than C, that is 10%. Trap: 5% comes from 25 − 20; "
    "percentages multiply, they do not subtract. Grew from: 2018 Q57 and 2021 Q57 (two numbers x% and y% more than a "
    "third). Next twist: A is p% more and B is q% less than C: ratio of A to B.",
    calc="100-75*1.2")

add(A, "A person goes to his office at one-third of the speed at which he returns. If his average speed for the "
       "whole trip is 12 km/h, what is his speed while going to the office?",
    ["8 km/h", "6 km/h", "16 km/h", "24 km/h"],
    "Let the going speed be x, so the return speed is 3x. For equal distances, average speed = 2 × x × 3x ÷ (x + 3x) "
    "= 1.5x. So 1.5x = 12 and x = 8 km/h. Trap: 24 km/h is the return speed; 6 km/h uses the simple average (x + 3x)/2. "
    "Grew from: 2018 Q62 and 2021 Q62 (speed and ratio of speeds). Next twist: the return speed is asked.",
    calc="12/1.5")

add(A, "0.3̅ + 0.6̅ + 0.7̅ + 0.8̅ = ? (the bar means the digit recurs)",
    ["8/3", "12/5", "2.4", "13/5"],
    "A single recurring digit a is a/9. The sum is (3 + 6 + 7 + 8)/9 = 24/9 = 8/3. Trap: 2.4 adds 0.3 + 0.6 + 0.7 + 0.8 "
    "as plain decimals. Grew from: 2021 Q56 (0.68̅ + 0.73̅) and 2018 Q56. Next twist: a mixed recurring decimal such "
    "as 0.12̅, which is (12 − 1)/90.",
    calc="24/9")

add(A, "A sum of money at compound interest amounts to Rs. 2,420 in 2 years and to Rs. 2,662 in 3 years. What is "
       "the sum?",
    ["Rs. 2,000", "Rs. 2,200", "Rs. 1,800", "Rs. 2,100"],
    "The third year's interest is 2662 − 2420 = 242, which is 10% of 2420, so the rate is 10%. Sum = 2420 ÷ (1.1)² "
    "= 2420 ÷ 1.21 = Rs. 2,000. Trap: Rs. 2,200 goes back only one year. Grew from: 2018 Q60 and 2021 Q60 (CI − SI) "
    "and 2025 Q78, Q90 (rates). Next twist: compounded half-yearly.",
    calc="2420/1.21")

add(A, "If 2^(x − 1) + 2^(x + 1) = 1280, then x = ?",
    ["9", "10", "8", "11"],
    "Take out the smaller power: 2^(x − 1) × (1 + 2²) = 5 × 2^(x − 1) = 1280. So 2^(x − 1) = 256 = 2⁸, x − 1 = 8 and "
    "x = 9. Trap: 8 stops at the power of 256. Grew from: 2025 Q80 (2^x × 8^(1/5) = 2^(1/5)). Next twist: "
    "3^(x + 2) − 3^x = 216.",
    calc="9")

add(A, "If (1/5)^(3y) = 0.008, then the value of (0.25)^y is:",
    ["0.26", "0.24", "0.27", "0.25"],
    "Exact past question (2025 Q76; wording from the Udyam IAS book, our scan lost the powers). 0.008 = 8/1000 = "
    "1/125 = (1/5)³. So 3y = 3 and y = 1. Then (0.25)¹ = 0.25. Family: equal bases, the same as 2025 Q80 and "
    "2021 Q65. Next twist: (0.2)^(2y) = 0.0016, find (0.5)^y.",
    a=3, src="2025 Q76", calc="0.25")

add(A, "(0.0036 × 2.5) ÷ (0.012 × 0.15) = ?",
    ["5", "0.5", "50", "0.05"],
    "Numerator: 36 × 25 = 900 with 4 + 1 = 5 decimal places, so 0.00900. Denominator: 12 × 15 = 180 with 3 + 2 = 5 "
    "places, so 0.00180. Both have 5 places, so the answer is 900 ÷ 180 = 5. Trap: counting places wrongly gives 0.5 "
    "or 50. Grew from: 2018 Q54 and 2021 Q54 (products of decimals). Next twist: the answer in standard form.",
    calc="(0.0036*2.5)/(0.012*0.15)")

add(A, "A hostel has food for 120 students for 40 days. After 10 days some students leave, and the remaining food "
       "lasts for 45 more days. How many students left?",
    ["40", "30", "20", "50"],
    "After 10 days the food left is enough for 120 students for 30 days = 3,600 student-days. It now lasts 45 days, "
    "so 3600 ÷ 45 = 80 students remain. 120 − 80 = 40 left. Trap: 30 uses 40 days instead of 30 days. Grew from: "
    "2025 Q95 (a fort, 25 men leave). Twist: the unknown is reversed. Next twist: men join and the food lasts fewer days.",
    calc="120-120*30/45")

add(A, "How many numbers from 1 to 500 are divisible by 3 but not by 5?",
    ["133", "166", "100", "143"],
    "Divisible by 3: 500 ÷ 3 = 166 numbers. Of these, those divisible by both 3 and 5 are divisible by 15: "
    "500 ÷ 15 = 33. So 166 − 33 = 133. Trap: 166 forgets to take out the multiples of 15. Grew from: 2021 Q82 "
    "(numbers between 23 and 100 divisible by 6). Next twist: divisible by 4 or 6 (use the L.C.M. 12).",
    calc="500//3-500//15")

add(A, "After how many places of decimals will the decimal expansion of 13/3125 terminate?",
    ["5", "4", "3", "6"],
    "3125 = 5⁵. Multiply top and bottom by 2⁵: 13 × 32 / 10⁵ = 416/100000 = 0.00416. That has 5 decimal places. "
    "Rule: if the denominator is 2^m × 5^n, the decimal ends after the larger of m and n places. Grew from: 2015 "
    "Q51-53 (theory of real numbers, NCERT Class 10). Next twist: which of four fractions has a non-terminating decimal.",
    calc="5")

add(A, "A is 50% more efficient than B. C does half as much work as A and B together do in the same time. If C "
       "alone can finish a work in 15 days, in how many days can A, B and C together finish it?",
    ["5 days", "6 days", "7.5 days", "10 days"],
    "Let B do b a day. A does 1.5b, and A + B do 2.5b. C does half of that: 1.25b = 1/15, so b = 4/75. A + B = 2.5b "
    "= 2/15 and C = 1/15. All three: 3/15 = 1/5 of the work a day, so 5 days. Trap: 7.5 days is A + B alone. "
    "Grew from: 2018 Q61 (A + B, B + C, A + B + C). Next twist: wages shared by efficiency.",
    calc="1/(2/15+1/15)")

add(A, "A can do a work in 15 days and B in 20 days. They work together for 4 days. Then A leaves and C joins B, "
       "and B and C finish the remaining work in 4 days. In how many days can C alone do the whole work?",
    ["12 days", "15 days", "10 days", "18 days"],
    "A + B do 1/15 + 1/20 = 7/60 a day; in 4 days 28/60 = 7/15. Left: 8/15. B + C do 8/15 in 4 days, so 2/15 a day. "
    "C = 2/15 − 1/20 = 8/60 − 3/60 = 5/60 = 1/12. C alone takes 12 days. Grew from: 2021 Q61 (B works 10 days and "
    "leaves, others finish). Next twist: C joins for the whole time and the total time is given.",
    calc="1/(2/15-1/20)")

add(A, "In a 100 m race, A runs at 8 km per hour. If A gives B a start of 4 m and still beats him by 15 seconds, "
       "what is the speed of B?",
    ["5.76 km/hr", "6.25 km/hr", "4.25 km/hr", "7.28 km/hr"],
    "Exact past question (2025 Q65). A's speed = 8 × 5/18 = 20/9 m/s, so A runs 100 m in 45 seconds. B runs only "
    "96 m (start of 4 m) and takes 45 + 15 = 60 seconds. B's speed = 96/60 = 1.6 m/s = 1.6 × 18/5 = 5.76 km/h. "
    "Family: 2025 Q60 (A beats B by 28 m in 7 s). Next twist: a dead heat, where the start is just enough.",
    src="2025 Q65", calc="96/60*18/5")

add(A, "At what time between 3 o'clock and 4 o'clock are the hands of a clock together?",
    ["16 4/11 minutes past 3", "15 minutes past 3", "16 6/11 minutes past 3", "17 1/11 minutes past 3"],
    "At 3:00 the minute hand is 15 minute-spaces behind the hour hand. It gains 55 minute-spaces in 60 minutes, so it "
    "gains 15 spaces in 15 × 60/55 = 180/11 = 16 4/11 minutes. The hands meet at 16 4/11 minutes past 3. Trap: "
    "15 minutes past 3 forgets that the hour hand also moves. Grew from: 2025 Q55 and Q69 (clocks). Next twist: when "
    "are the hands opposite (180°) between 3 and 4?",
    nocalc=True)

add(A, "[(2.3)³ − 0.027] ÷ [(2.3)² + 0.69 + 0.09] = ?",
    ["2", "2.6", "2.3", "1.7"],
    "Let a = 2.3 and b = 0.3. Then 0.027 = b³, 0.69 = ab and 0.09 = b². The expression is (a³ − b³) ÷ (a² + ab + b²) "
    "= a − b = 2.3 − 0.3 = 2. Trap: 2.6 is a + b, the answer for a³ + b³ over a² − ab + b². Grew from: 2018 Q55 and "
    "2021 Q55 ([(a + b)² − (a − b)²] ÷ ab = 4). Next twist: the a³ + b³ form.",
    calc="(2.3**3-0.027)/(2.3**2+0.69+0.09)")

add(A, "An examination has 60 questions. A right answer gets 4 marks and a wrong answer loses 1 mark. A student "
       "answers all the questions and scores 130. How many questions did he answer correctly?",
    ["38", "34", "40", "36"],
    "This is a heads-and-legs question. Let r be right. 4r − (60 − r) = 130, so 5r = 190 and r = 38. Check: "
    "38 × 4 − 22 = 152 − 22 = 130. Trap: 32.5 (not a whole number) comes from forgetting the minus marks, 4r = 130. Grew from: 2025 Q75 (heads and feet). Next twist: some "
    "questions are left out and both the score and the number attempted are given.",
    calc="(130+60)/5")

add(A, "Two trains run in the same direction at 50 km/h and 32 km/h. The faster train passes a man sitting in the "
       "slower train in 15 seconds. What is the length of the faster train?",
    ["75 m", "120 m", "135 m", "90 m"],
    "Same direction, so the relative speed is 50 − 32 = 18 km/h = 5 m/s. To pass a man, the train covers only its own "
    "length: 5 × 15 = 75 m. Trap: 135 m uses 32 km/h alone; 120 m does not convert units properly. Grew from: "
    "2025 Q59 and Q82 (a train passing a man walking). Next twist: the man walks inside the train.",
    calc="(50-32)*5/18*15")

add(A, "A man buys hens at Rs. 300 each and goats at Rs. 2,500 each. He buys 30 animals in all, which have 80 feet "
       "together. How much does he spend?",
    ["Rs. 31,000", "Rs. 37,000", "Rs. 25,000", "Rs. 43,000"],
    "If all 30 were hens there would be 60 feet. The 20 extra feet come from goats, 2 extra feet each, so 10 goats and "
    "20 hens. Cost = 20 × 300 + 10 × 2,500 = 6,000 + 25,000 = Rs. 31,000. Trap: Rs. 43,000 swaps hens and goats. "
    "Grew from: 2025 Q75 (heads and feet). Twist: a second step after the count.",
    calc="20*300+10*2500")

add(A, "Ten years ago, A was half as old as B. If the ratio of their present ages is 3 : 4, what is the sum of their "
       "present ages?",
    ["35 years", "30 years", "40 years", "45 years"],
    "Let the ages be 3x and 4x. Ten years ago: 3x − 10 = (4x − 10)/2, so 6x − 20 = 4x − 10 and x = 5. Ages 15 and 20, "
    "sum 35. Check: ten years ago 5 and 10. Grew from: 2025 Q52 (one year ago four times as old) and 2025 Q85. "
    "Next twist: the ratio after some years is given instead.",
    calc="7*5")

add(A, "A tank is 2/5 full. When 36 litres are drawn out, it is 1/4 full. What is the capacity of the tank?",
    ["240 litres", "180 litres", "200 litres", "144 litres"],
    "36 litres = 2/5 − 1/4 = 8/20 − 5/20 = 3/20 of the tank. Capacity = 36 × 20/3 = 240 litres. Trap: 144 litres is "
    "36 ÷ (1/4). Grew from: 2025 Q51 (3/8 and 4/5 of a book, 30 pages left). Next twist: water is added and the tank "
    "goes from 1/3 to 3/4 full.",
    calc="36*20/3")

add(A, "(476 + 424)² − 4 × 476 × 424 = ?",
    ["2704", "2800", "2600", "2916"],
    "(a + b)² − 4ab = (a − b)². So the value is (476 − 424)² = 52² = 2704. Grew from: 2018 Q55 and 2021 Q55 "
    "([(a + b)² − (a − b)²] ÷ ab). Next twist: (a + b)² + (a − b)² over a² + b², which is 2.",
    calc="(476+424)**2-4*476*424")

add(A, "What is the third proportional to 0.36 and 0.48?",
    ["0.64", "0.60", "0.42", "0.56"],
    "If a : b = b : c, then c is the third proportional and c = b²/a = 0.48² ÷ 0.36 = 0.2304 ÷ 0.36 = 0.64. Trap: 0.42 "
    "is the mean of the two; 0.60 adds the gap 0.12 again. Grew from: 2018 Q68 and 2021 Q68 (fourth proportional). "
    "Next twist: the mean proportional of 0.36 and 0.64 (= 0.48).",
    calc="0.48**2/0.36")

add(A, "Pipes A and B can fill a tank in 12 minutes and 15 minutes respectively. They are opened in turn for one "
       "minute each, A first. In how much time will the tank be full?",
    ["13¼ minutes", "13½ minutes", "12¾ minutes", "14 minutes"],
    "Two minutes (A then B) fill 1/12 + 1/15 = 9/60 = 3/20. Six rounds (12 minutes) fill 18/20. In the 13th minute A "
    "adds 1/12, making 18/20 + 1/12 = 59/60. B fills the last 1/60 in (1/60) ÷ (1/15) = 1/4 minute. Total 13¼ minutes. "
    "Trap: 13½ gives B a full half minute. Grew from: 2025 Q91 and Q97 (two pipes together). Next twist: one pipe "
    "empties while the other fills, in turn.",
    calc="13+0.25")

add(A, "In a 500 m race, the speeds of A and B are in the ratio 3 : 4. A has a start of 140 m. By how many metres "
       "does A win?",
    ["20 m", "40 m", "60 m", "80 m"],
    "A has to run 500 − 140 = 360 m. In that time B runs 360 × 4/3 = 480 m. So B is still 20 m short when A finishes: "
    "A wins by 20 m. Trap: 80 m compares 480 m with 400 m and forgets the start. Grew from: 2025 Q60 and Q65 (a start and still wins). "
    "Next twist: the start needed for a dead heat (here 125 m).",
    calc="500-360*4/3")

# ================================================================ ALGEBRA (14)

add(G, "If A is the matrix [[2, 3], [1, 4]] (each inner bracket is a row), what is the determinant of 3A?",
    ["45", "15", "135", "25"],
    "det A = 2 × 4 − 3 × 1 = 5. Multiplying a 2 × 2 matrix by 3 multiplies every entry, so each row gets a factor 3 "
    "and the determinant gets 3² = 9. det(3A) = 9 × 5 = 45. Trap: 15 multiplies by 3 only once. Grew from: 2018 Q70 "
    "and 2021 Q70 (M + 2N, 2M + N) and 2018 Q69 (determinants). Next twist: det(A × B) = det A × det B.",
    calc="9*(2*4-3*1)")

add(G, "In an A.P., 7 times the 7th term is equal to 11 times the 11th term. What is its 18th term?",
    ["0", "1", "18", "−1"],
    "7(a + 6d) = 11(a + 10d), so 7a + 42d = 11a + 110d, which gives 4a = −68d and a = −17d. The 18th term "
    "= a + 17d = 0. Grew from: 2018 Q74 and 2021 Q74 (a term from two given terms). Next twist: m times the mth term "
    "equals n times the nth term: the (m + n)th term is always 0.",
    calc="0")

add(G, "If 5^(x + 3) = 25^(3x − 4), then x = ?",
    ["11/5", "5/11", "7/5", "1"],
    "Write 25 as 5². Then 5^(x + 3) = 5^(6x − 8). Equal bases, so x + 3 = 6x − 8 and 5x = 11, x = 11/5. Trap: 7/5 "
    "forgets to double the 4. Grew from: 2021 Q65 (p^(5x + 3) = 1) and 2025 Q80. Next twist: 9^x = 27^(x − 1).",
    calc="11/5")

add(G, "For what values of a and b does the pair of equations 2x + 3y = 7 and (a − b)x + (a + b)y = 3a + b − 2 "
       "have infinitely many solutions?",
    ["a = 5, b = 1", "a = 1, b = 5", "a = 3, b = 1", "a = 5, b = 3"],
    "Infinitely many solutions: (a − b)/2 = (a + b)/3 = (3a + b − 2)/7. From the first two: 3a − 3b = 2a + 2b, so "
    "a = 5b. Then a + b = 6b and 3a + b − 2 = 16b − 2. From (a + b)/3 = (3a + b − 2)/7: 42b = 48b − 6, so b = 1 and "
    "a = 5. Grew from: 2018 Q71 and 2021 Q71 (value of k for no solution). Twist: two unknowns. Next twist: "
    "values for no solution.",
    calc="5")

add(G, "If α and β are the zeroes of the polynomial x² − 5x + k and α − β = 1, what is the value of k?",
    ["6", "4", "5", "8"],
    "α + β = 5 and αβ = k. Use (α − β)² = (α + β)² − 4αβ: 1 = 25 − 4k, so k = 6. Check: the zeroes are 3 and 2. "
    "Grew from: 2015 Q71-73 (zeroes of polynomials) and 2018 Q64, 2021 Q64 (α + β and α − β). Next twist: α − β is "
    "given and the polynomial is asked.",
    calc="(25-1)/4")

add(G, "The sum of the first 7 terms of an A.P. is 49 and the sum of its first 17 terms is 289. What is the sum of "
       "its first 20 terms?",
    ["400", "420", "380", "441"],
    "S7 = 7/2 (2a + 6d) = 49 gives a + 3d = 7. S17 = 17/2 (2a + 16d) = 289 gives a + 8d = 17. So d = 2 and a = 1: "
    "the A.P. is 1, 3, 5, … and Sn = n². S20 = 400. Trap: 441 is S21. Grew from: 2018 Q77 (S11 from the 6th term) "
    "and 2021 Q75, Q76 (Sn formulas). Next twist: the formula Sn itself is asked.",
    calc="20**2")

add(G, "If the matrices [[x + y, 2], [5, x − y]] and [[6, 2], [5, 2]] are equal (each inner bracket is a row), "
       "then:",
    ["x = 4, y = 2", "x = 2, y = 4", "x = 3, y = 3", "x = 4, y = −2"],
    "Equal matrices have equal entries in the same places. So x + y = 6 and x − y = 2. Adding: 2x = 8, x = 4, then "
    "y = 2. Trap: x = 2, y = 4 swaps the two. Grew from: 2021 Q69 and 2018 Q69 (x and y from equal determinants). "
    "Next twist: a 2 × 2 matrix equation with 2x + y and x − 3y.",
    calc="4")

add(G, "How many proper subsets does a set with 6 elements have?",
    ["63", "64", "62", "36"],
    "A set with n elements has 2ⁿ subsets. 2⁶ = 64. A proper subset is any subset except the set itself, so 64 − 1 = 63. "
    "Trap: 64 is the power set; 62 also leaves out the empty set; 36 is 6². Grew from: 2018 Q83 and 2021 Q83 (the power "
    "set has 2ⁿ elements). Next twist: the number of subsets with exactly 2 elements (6C2 = 15).",
    calc="2**6-1")

add(G, "If (a/b)^(x − 1) = (b/a)^(x − 3), then x = ?",
    ["2", "1", "3", "1/2"],
    "b/a = (a/b)^(−1), so the right side is (a/b)^(3 − x). Equal bases: x − 1 = 3 − x, so 2x = 4 and x = 2. Trap: writing "
    "x − 1 = x − 3 forgets the minus sign from turning the fraction over, and then there is no answer. Grew from: 2021 Q65 (p^(5x + 3) = 1). Next twist: "
    "(3/5)^x × (5/3)^(2x) = 125/27.",
    calc="2")

add(G, "What is the area of the triangle formed by the lines 2x + y = 6 and 2x − y + 2 = 0 and the x-axis?",
    ["8 sq units", "12 sq units", "6 sq units", "16 sq units"],
    "Solve the pair: adding gives 4x + 2 = 6, so x = 1 and y = 4. The lines meet at (1, 4). They cut the x-axis at "
    "x = 3 and x = −1, so the base is 4. Height = 4 (the y of the meeting point). Area = 1/2 × 4 × 4 = 8. Trap: 16 "
    "forgets the 1/2. Grew from: 2018 Q71-73 and 2021 Q71-73 (pairs of linear equations). Next twist: the triangle "
    "with the y-axis.",
    calc="0.5*4*4")

add(G, "If (3x − 2y) : (2x + 3y) = 5 : 6, then x : y is:",
    ["27 : 8", "8 : 27", "3 : 2", "9 : 4"],
    "Cross-multiply: 6(3x − 2y) = 5(2x + 3y), so 18x − 12y = 10x + 15y and 8x = 27y. So x : y = 27 : 8. Trap: 8 : 27 "
    "turns it over. Grew from: 2018 Q67 ((2x + 5y) : (5x − 7y) = 5 : 3). Next twist: find (x + y) : (x − y) next.",
    calc="27")

add(G, "How many terms of the A.P. 24, 21, 18, … must be taken so that their sum is 78?",
    ["4 or 13", "4 only", "13 only", "6 or 10"],
    "Sn = n/2 [2 × 24 + (n − 1)(−3)] = n(51 − 3n)/2 = 78. So 3n² − 51n + 156 = 0, that is n² − 17n + 52 = 0 = "
    "(n − 4)(n − 13). Both work: the 5th to 13th terms (12, 9, …, −12) add up to 0. Trap: '4 only' throws away a true "
    "answer. Grew from: 2021 Q75 (which term is 164) and 2018 Q77. Next twist: which term is the first negative one.",
    calc="4")

add(G, "If x³ + ax² + bx + 6 has (x − 2) as a factor and leaves a remainder 3 when divided by (x − 3), then:",
    ["a = −3, b = −1", "a = −1, b = −3", "a = 3, b = −13", "a = −3, b = 1"],
    "Factor: f(2) = 8 + 4a + 2b + 6 = 0, so 2a + b = −7. Remainder: f(3) = 27 + 9a + 3b + 6 = 3, so 3a + b = −10. "
    "Subtract: a = −3, then b = −1. Check: f(2) = 8 − 12 − 2 + 6 = 0. Grew from: 2018 Q66 (remainder k when divided "
    "by x − 2). Twist: two conditions, two unknowns. Next twist: two factors given.",
    calc="-3")

add(G, "If one root of the equation x² − 3x + k = 0 is double the other, what is the value of k?",
    ["2", "1", "3", "9/2"],
    "Let the roots be r and 2r. Sum: 3r = 3, so r = 1 and the roots are 1 and 2. Product: k = 1 × 2 = 2. Trap: 9/2 "
    "comes from b²/4a (the value for equal roots, k = 9/4, doubled). Grew from: 2018 Q64 and 2021 Q64 (equation from "
    "α + β and α − β). Next twist: one root is the square of the other.",
    calc="2")
