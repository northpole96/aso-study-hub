# Questions for Maths Mock 01 (OPSC ASO Paper II (B) Mathematics, 50 questions, 45 minutes).
# In every item the FIRST option is the right one (the builder shuffles options).
# s: syllabus topic (Arithmetic | Algebra | Mensuration | Statistics & Probability), t: sub-type (used only to keep
# neighbours apart), id: short name used by tools/check_maths_mock1.py, which recomputes every answer.
#
# Weights come from the three real papers, read from the scans (18 Nov 2026):
#   2018 and 2021 used one Class-10 template (about 15 arithmetic, 15 algebra, 3 mensuration, 17 statistics & probability).
#   2025 (booklet ASG(AG)-2/25) was 44 arithmetic questions in R. S. Aggarwal style, 5 indices/surds, 1 combinations.
#   2025 Q71 repeated 2021 Q93 word for word.
# Every question here is a "next angle" of a past question: same idea, new numbers or a new twist.
# None copies a past question, so the 2021 Paper II mock stays separate.

Q = []
def add(s, t, id, q, o, e, c=False):
    Q.append(dict(s=s, t=t, id=id, q=q, o=o, e=e, k="one", n=False, c=c, a=None))

A, B, M, S = "Arithmetic", "Algebra", "Mensuration", "Statistics & Probability"

# ============================================================ ARITHMETIC: NUMBER SYSTEM (2025 Q56, 61, 70, 79, 99, 100)
add(A, "num", "sub23",
    "What least number must be subtracted from 2010 so that the result is exactly divisible by 23?",
    ["9", "7", "11", "14"],
    "Divide 2010 by 23. 23 × 87 = 2001, so the remainder is 2010 − 2001 = 9. Take away the remainder and the number divides exactly. "
    "Rule: to make a number divisible, subtract the remainder, or add (divisor − remainder). Here the 'add' answer would be 23 − 9 = 14, which is why 14 sits in the options as a trap. "
    "Grew from 2025 Q56 (1672 and 17). Likely next: the least number to be ADDED.")
add(A, "sq", "sq2135",
    "What is the smallest number that must be added to 2135 to make it a perfect square?",
    ["74", "19", "81", "69"],
    "Find the squares on either side. 46² = 2116 and 47² = 2209. 2135 lies between them, so the next square is 2209. Add 2209 − 2135 = 74. "
    "The trap is 19: that is what you SUBTRACT (2135 − 2116) to reach the square below. "
    "Grew from 2025 Q99 (1780). Learn squares up to 50 by heart; they save a minute here.")
add(A, "div", "div90",
    "If the five-digit number 748xy is divisible by 90, then (x + y) = ?",
    ["8", "6", "9", "10"],
    "90 = 9 × 10. Divisible by 10 means the last digit y = 0. Divisible by 9 means the digit sum is a multiple of 9: 7 + 4 + 8 + x + 0 = 19 + x. The next multiple of 9 is 27, so x = 8. "
    "Then x + y = 8 + 0 = 8. "
    "Grew from 2025 Q100 (653xy). Likely next: divisible by 72 (= 8 × 9) or 88 (= 8 × 11).")
add(A, "hcf", "hcfratio",
    "Two numbers are in the ratio 13 : 8 and their H.C.F. is 17. The numbers are:",
    ["221 and 136", "208 and 128", "221 and 128", "234 and 144"],
    "When two numbers are in the ratio a : b and their HCF is h, the numbers are a × h and b × h (13 and 8 share no factor). So 13 × 17 = 221 and 8 × 17 = 136. "
    "Quick check: 221 ÷ 17 = 13 and 136 ÷ 17 = 8. "
    "Grew from 2025 Q79 (15 : 11, HCF 13). Likely next: find the LCM, which is 13 × 8 × 17 = 1768.")
add(A, "lcm", "bells",
    "Four bells ring at intervals of 6, 8, 12 and 18 minutes. They all ring together at 9 a.m. When will they next ring together?",
    ["10:12 a.m.", "10:24 a.m.", "9:48 a.m.", "10:36 a.m."],
    "Bells ring together again after the LCM of the gaps. 6 = 2 × 3, 8 = 2³, 12 = 2² × 3, 18 = 2 × 3². LCM = 2³ × 3² = 72 minutes = 1 hour 12 minutes. "
    "9 a.m. + 1 h 12 min = 10:12 a.m. "
    "Grew from 2025 Q61 (devices that beep). 'Together again' always means LCM; 'biggest measure' always means HCF.")
add(A, "succ", "succdiv",
    "A number is divided successively by 3, 4 and 5. The remainders are 2, 3 and 4 respectively. The least such number is:",
    ["59", "69", "47", "89"],
    "Work from the last division backwards. Take the last quotient as 0. Then the number before the 5-division is 5 × 0 + 4 = 4. Before the 4-division: 4 × 4 + 3 = 19. Before the 3-division: 19 × 3 + 2 = 59. "
    "Check: 59 ÷ 3 = 19 r 2, 19 ÷ 4 = 4 r 3, 4 ÷ 5 = 0 r 4. "
    "Grew from 2025 Q70 (4, 5, 6 with remainders 2, 3, 4).")

# ============================================================ ARITHMETIC: FRACTIONS, NUMBERS, AGES (2025 Q51, 52, 71, 75)
add(A, "frac", "salary",
    "A man spends 2/5 of his salary on rent and 1/3 of the remaining on food. He is left with Rs. 6,000. What is his salary?",
    ["Rs. 15,000", "Rs. 12,000", "Rs. 18,000", "Rs. 20,000"],
    "After rent, 3/5 of the salary is left. Food takes 1/3 of that, so 2/3 of it stays. Money left = 3/5 × 2/3 = 2/5 of the salary. "
    "2/5 of the salary = 6,000, so the salary = 6,000 × 5/2 = Rs. 15,000. "
    "Grew from 2025 Q51 (a boy reads parts of a book). The trick is the word 'remaining': the second fraction is of what is left, not of the whole.")
add(A, "age", "ages",
    "Five years ago, a father was three times as old as his son. The father is 20 years older than the son. What is the ratio of their present ages?",
    ["7 : 3", "3 : 1", "5 : 2", "8 : 3"],
    "Let the son be S now; the father is S + 20. Five years ago: (S + 20 − 5) = 3(S − 5), so S + 15 = 3S − 15, which gives S = 15. The father is 35. "
    "Ratio 35 : 15 = 7 : 3. "
    "Grew from 2025 Q52 (Promila and Sakshi). The age gap between two people never changes, so 'exceeds by 20 years' is true at every point in time.")
add(A, "num", "oddsq",
    "The difference of the squares of two consecutive odd numbers is 64. What is their sum?",
    ["32", "30", "34", "36"],
    "Let the numbers be n and n + 2. (n + 2)² − n² = 4n + 4 = 64, so n = 15. The numbers are 15 and 17, and their sum is 32. "
    "Shortcut: a² − b² = (a + b)(a − b). Here a − b = 2, so a + b = 64 ÷ 2 = 32 straight away. "
    "Grew from 2021 Q93, which 2025 copied word for word as Q71 (even numbers, 84). The examiner reuses this one, so learn the shortcut.")
add(A, "num", "keepers",
    "In a farm there are 40 hens, 30 goats and 6 camels, along with some keepers. The total number of feet is 160 more than the total number of heads. How many keepers are there?",
    ["12", "10", "14", "16"],
    "Each animal or person has one head. Hens and keepers have 2 feet; goats and camels have 4. "
    "Feet = 40 × 2 + 30 × 4 + 6 × 4 + 2k = 224 + 2k. Heads = 40 + 30 + 6 + k = 76 + k. "
    "Feet − heads = 148 + k = 160, so k = 12. "
    "Grew from 2025 Q75 (hens, goats, camels and keepers), a classic R. S. Aggarwal problem.")

# ============================================================ ARITHMETIC: PERCENTAGE (2025 Q57, 66, 94, 96)
add(A, "pct", "rect",
    "The length of a rectangle is increased by 20% and its breadth is decreased by 10%. What is the effect on its area?",
    ["8% increase", "10% increase", "2% decrease", "8% decrease"],
    "New area = 1.20 × 0.90 = 1.08 times the old area, so the area goes up by 8%. "
    "Shortcut for two changes x% and y%: x + y + xy/100 = 20 − 10 + (20 × −10)/100 = 10 − 2 = 8%. "
    "Grew from 2025 Q66 (each side of a square up 25%, area up 56.25%). For a square, put x = y: 25 + 25 + 6.25 = 56.25.")
add(A, "pct", "sugar",
    "A reduction of 20% in the price of sugar enables a man to buy 2 kg more for Rs. 240. What was the original price per kg?",
    ["Rs. 30", "Rs. 24", "Rs. 32", "Rs. 36"],
    "20% of Rs. 240 = Rs. 48 is saved. With the saving he buys 2 kg more, so the reduced price = 48 ÷ 2 = Rs. 24 per kg. "
    "The reduced price is 80% of the original, so the original = 24 ÷ 0.8 = Rs. 30 per kg. "
    "Trap: Rs. 24 is the NEW price. Read which price the question asks for. Grew from 2025 Q94.")
add(A, "pct", "votes",
    "In an election between two candidates, the winner got 58% of the valid votes and won by 1,120 votes. What was the total number of valid votes?",
    ["7,000", "6,500", "8,000", "5,600"],
    "The loser got 42%. The gap is 58% − 42% = 16% of the valid votes = 1,120. So 1% = 70, and 100% = 7,000. "
    "Grew from 2025 Q96 (one student's marks were 56% of the total and 9 more than the other's). The same idea: the gap between two shares is a known number of units.")


# ============================================================ ARITHMETIC: PROFIT AND LOSS (2025 Q72, 89)
add(A, "pl", "toffee",
    "A shopkeeper buys pens at 6 for a rupee. How many must he sell for a rupee to gain 20%?",
    ["5", "4", "3", "6"],
    "Cost of 6 pens = Re 1. To gain 20% he must get Rs. 1.20 for those 6 pens. So for Re 1 he must sell 6 ÷ 1.2 = 5 pens. "
    "Grew from 2025 Q72 (toffees at 3 for a rupee, gain 50%) and 2021 Q59 (11 for Rs. 10, 10 for Rs. 11).")
add(A, "pl", "cowcalf",
    "A man bought a cow and a calf for Rs. 8,000. He sold the cow at a gain of 25% and the calf at a loss of 10%, and gained 4% on the whole. What was the cost of the cow?",
    ["Rs. 3,200", "Rs. 4,800", "Rs. 3,000", "Rs. 3,600"],
    "Total gain = 4% of 8,000 = Rs. 320. Let the cow cost c; the calf costs 8,000 − c. "
    "0.25c − 0.10(8,000 − c) = 320, so 0.35c = 320 + 800 = 1,120, and c = 3,200. "
    "Trap: 4,800 is the calf. Grew from 2025 Q89 (horse and carriage).")

# ============================================================ ARITHMETIC: INTEREST, PARTNERSHIP, AVERAGE
add(A, "si", "sirate",
    "A sum of Rs. 1,200 amounts to Rs. 1,488 in 4 years at simple interest. If the rate of interest is increased by 2%, what will it amount to?",
    ["Rs. 1,584", "Rs. 1,560", "Rs. 1,600", "Rs. 1,632"],
    "Interest = 1,488 − 1,200 = 288 for 4 years, so the rate = 288 × 100 ÷ (1,200 × 4) = 6%. "
    "At 8% the interest is 1,200 × 8 × 4 ÷ 100 = 384, so the amount = 1,200 + 384 = Rs. 1,584. "
    "Faster: 2% more for 4 years adds 8% of 1,200 = 96 to the old amount: 1,488 + 96 = 1,584. Grew from 2025 Q78 and Q90.")
add(A, "si", "cisi3",
    "What is the difference between compound interest and simple interest on Rs. 8,000 for 3 years at 5% per annum?",
    ["Rs. 61", "Rs. 20", "Rs. 60", "Rs. 63"],
    "SI = 8,000 × 5 × 3 ÷ 100 = 1,200. CI = 8,000 × (1.05³ − 1) = 8,000 × 0.157625 = 1,261. Difference = Rs. 61. "
    "Shortcut for 3 years: P × (r/100)² × (3 + r/100) = 8,000 × 0.0025 × 3.05 = 61. For 2 years it is just P × (r/100)², which gives Rs. 20 (the trap). "
    "Grew from 2018 Q60 and 2021 Q60, both about the 2-year difference. The 3-year version is the next step.")
add(A, "part", "partner",
    "A starts a business with Rs. 4,500. After 4 months B joins him. At the end of the year the profit is divided between A and B in the ratio 9 : 8. How much did B invest?",
    ["Rs. 6,000", "Rs. 5,400", "Rs. 6,500", "Rs. 7,200"],
    "Profit is shared in the ratio of (money × months). A: 4,500 × 12 = 54,000. B: x × 8. "
    "54,000 : 8x = 9 : 8, so 8x = 54,000 × 8 ÷ 9 = 48,000 and x = Rs. 6,000. "
    "Grew from 2025 Q81 (A with Rs. 3,500, B joins after 5 months) and Q63 (milkmen renting a pasture: cows × months).")
add(A, "avg", "avgclass",
    "The average weight of 20 boys in a class is 42 kg and the average weight of the 30 girls is 37 kg. What is the average weight of the whole class?",
    ["39 kg", "39.5 kg", "38.5 kg", "40 kg"],
    "Total weight = 20 × 42 + 30 × 37 = 840 + 1,110 = 1,950 kg for 50 children. Average = 1,950 ÷ 50 = 39 kg. "
    "Trap: 39.5 is the simple average of 42 and 37, which is wrong because the groups are of different sizes. Grew from 2025 Q68.")

# ============================================================ ARITHMETIC: TIME AND WORK, PIPES (2025 Q53, 74, 77, 83, 91, 95, 97)
add(A, "work", "reap",
    "12 men working 8 hours a day can reap a field in 15 days. In how many days can 16 men reap the same field working 9 hours a day?",
    ["10", "9", "12", "8"],
    "Total work = men × hours × days = 12 × 8 × 15 = 1,440 man-hours. With 16 men for 9 hours a day: 1,440 ÷ (16 × 9) = 10 days. "
    "Rule: M1 × H1 × D1 = M2 × H2 × D2 when the work is the same. Grew from 2025 Q77 (15 men, 9 hours, 16 days).")
add(A, "work", "fort",
    "A fort has food for 200 men for 30 days. After 6 days, 40 more men join. For how many days will the remaining food last?",
    ["20", "24", "18", "22"],
    "After 6 days the food left is enough for 200 men for 24 days, that is 4,800 man-days. Now there are 240 men, so it lasts 4,800 ÷ 240 = 20 days. "
    "Grew from 2025 Q95 (men LEAVE the fort). When men join, the days go down; when they leave, the days go up.")
add(A, "work", "menboys",
    "2 men or 3 boys can do a piece of work in 16 days. How many days will 4 men and 6 boys take to do the same work?",
    ["4", "6", "8", "5"],
    "2 men = 3 boys, so 4 men = 6 boys. Then 4 men + 6 boys = 12 boys. "
    "3 boys take 16 days, so the work is 48 boy-days. 12 boys take 48 ÷ 12 = 4 days. "
    "Grew from 2025 Q83 (3 men or 6 boys). Always turn everyone into one kind of worker first.")
add(A, "pipe", "pipes3",
    "Pipes A and B can fill a tank in 20 minutes and 30 minutes. Pipe C can empty the full tank in 15 minutes. If all three are opened together, the tank will be full in:",
    ["60 minutes", "45 minutes", "50 minutes", "90 minutes"],
    "In one minute: A fills 1/20, B fills 1/30, C empties 1/15. Net = 1/20 + 1/30 − 1/15 = (3 + 2 − 4)/60 = 1/60 of the tank. So it fills in 60 minutes. "
    "Grew from 2025 Q91 (two pipes) and Q74 (a pump with a leak). An emptying pipe is just a negative worker.")
add(A, "pipe", "pipeclose",
    "Pipes A and B can fill a tank in 20 minutes and 30 minutes. Both are opened together. After how many minutes should B be closed so that the tank is full in 15 minutes?",
    ["7.5 minutes", "10 minutes", "6 minutes", "8 minutes"],
    "A runs for all 15 minutes and fills 15/20 = 3/4 of the tank. B must fill the other 1/4. B fills 1/30 per minute, so it must run 30 × 1/4 = 7.5 minutes. "
    "Grew from 2025 Q97 (24 and 32 minutes, full in 18). Work out the pipe that runs the whole time first.")

# ============================================================ ARITHMETIC: SPEED, TRAINS, RACES, CLOCKS (2025 Q54, 55, 59, 60, 64, 65, 69, 82)
add(A, "speed", "train",
    "A train 150 m long passes a man running at 6 km/h in the same direction as the train in 10 seconds. What is the speed of the train?",
    ["60 km/h", "54 km/h", "48 km/h", "66 km/h"],
    "Relative speed = 150 m ÷ 10 s = 15 m/s = 15 × 18/5 = 54 km/h. In the same direction, relative speed = train − man, so the train = 54 + 6 = 60 km/h. "
    "Trap: 54 is the relative speed; 48 is what you get if you subtract instead of add. Grew from 2025 Q59 and Q82 (man walking the OPPOSITE way, where you subtract).")
add(A, "speed", "car",
    "A car covers 360 km at a constant speed. If its speed were 10 km/h more, it would take 3 hours less. What is the original speed of the car?",
    ["30 km/h", "40 km/h", "36 km/h", "45 km/h"],
    "360/v − 360/(v + 10) = 3. This gives v(v + 10) = 1,200, so v² + 10v − 1,200 = 0 = (v + 40)(v − 30). Speed = 30 km/h. "
    "Faster: test the options. At 30 km/h the trip takes 12 h; at 40 km/h it takes 9 h. 12 − 9 = 3. Correct. Grew from 2025 Q64 (715 km, 2 hours less).")
add(A, "speed", "race",
    "In a 1 km race, A beats B by 40 metres or 8 seconds. What is A's time over the course?",
    ["3 min 12 s", "3 min 20 s", "3 min 4 s", "3 min 28 s"],
    "B runs 40 m in 8 seconds, so B's speed is 5 m/s and B takes 1,000 ÷ 5 = 200 seconds. A finishes 8 seconds sooner: 192 s = 3 min 12 s. "
    "Grew from 2025 Q60 (A beats B by 28 m in 7 s) and Q65 (a start of 4 m).")
add(A, "clock", "clock",
    "A clock is set right at 8 a.m. It gains 10 minutes in 24 hours. What is the true time when the clock shows 1 p.m. on the next day?",
    ["12:48 p.m.", "12:50 p.m.", "12:45 p.m.", "12:52 p.m."],
    "The clock shows 24 h 10 min (1,450 min) while 24 true hours (1,440 min) pass. From 8 a.m. to 1 p.m. next day the clock shows 29 hours = 1,740 min. "
    "True time passed = 1,740 × 1,440 ÷ 1,450 = 1,728 min = 28 h 48 min. 8 a.m. + 28 h 48 min = 12:48 p.m. next day. "
    "A fast clock is ahead, so the true time is earlier than what it shows. Grew from 2025 Q55 (a clock that loses) and Q69.")

# ============================================================ ARITHMETIC: THE 2018/2021 TEMPLATE
add(A, "series", "telescope",
    "1/(2·5) + 1/(5·8) + 1/(8·11) + 1/(11·14) = ?",
    ["1/7", "2/7", "3/14", "1/14"],
    "Each term splits: 1/(a·b) = 1/(b − a) × (1/a − 1/b), and here b − a = 3. The middle terms cancel, leaving 1/3 × (1/2 − 1/14) = 1/3 × 6/14 = 1/7. "
    "This came as Q51 in BOTH 2018 and 2021 (1·3, 3·5 ... in 2021). If the template comes back, this is a sure mark.")
add(A, "sets", "venn",
    "In a group of 60 people, 35 like tea, 30 like coffee and 10 like both. How many people like neither tea nor coffee?",
    ["5", "15", "10", "0"],
    "People who like at least one = 35 + 30 − 10 = 55 (take away the 10 counted twice). Neither = 60 − 55 = 5. "
    "Grew from 2018 Q78 (programmers) and 2021 Q78 (Hindi and English speakers). Learn n(A ∪ B) = n(A) + n(B) − n(A ∩ B).")

# ============================================================ ALGEBRA (2018 Q64–77, 2021 Q64–77, 2025 Q67, 76, 80, 86, 93)
add(B, "ind", "indices",
    "If 3^x × 9^(x + 1) = 243, then x = ?",
    ["1", "2", "3/2", "1/3"],
    "Write everything as a power of 3. 9^(x + 1) = 3^(2x + 2) and 243 = 3⁵. So 3^(x + 2x + 2) = 3⁵, which gives 3x + 2 = 5 and x = 1. "
    "Grew from 2025 Q80 (2^x × 8^5) and 2021 Q65. Bring both sides to one base, then compare powers.")
add(B, "surd", "surd",
    "If (3 + √2)/(3 − √2) = a + b√2, then:",
    ["a = 11/7, b = 6/7", "a = 11/7, b = −6/7", "a = 6/7, b = 11/7", "a = 1, b = 6/7"],
    "Multiply top and bottom by (3 + √2). Bottom: 9 − 2 = 7. Top: (3 + √2)² = 9 + 6√2 + 2 = 11 + 6√2. So the fraction is 11/7 + (6/7)√2. "
    "Grew from 2025 Q93 ((5 + 2√3)/(7 + 4√3)). Rationalise with the conjugate: change the sign in the middle.")
add(B, "quad", "alphabeta",
    "If α and β are the roots of x² − 7x + 12 = 0, then α² + β² = ?",
    ["25", "49", "24", "37"],
    "Sum of roots α + β = 7 and product αβ = 12. α² + β² = (α + β)² − 2αβ = 49 − 24 = 25. (Check: the roots are 3 and 4, and 9 + 16 = 25.) "
    "2018 Q64 and 2021 Q64 both gave α + β and α − β and asked for the equation. This is the reverse direction of the same family.")
add(B, "quad", "equalroots",
    "For what values of k does 2x² + kx + 8 = 0 have equal roots?",
    ["k = ±8", "k = ±4", "k = 8 only", "k = ±16"],
    "Equal roots when the discriminant b² − 4ac = 0. Here k² − 4 × 2 × 8 = 0, so k² = 64 and k = +8 or −8. "
    "Grew from 2018 Q72 and 2021 Q72 (find the discriminant). Remember: D > 0 two real roots, D = 0 equal roots, D < 0 no real roots.")
add(B, "lin", "infinite",
    "For what value of k will the equations kx + 2y = 6 and 6x + 4y = 12 have infinitely many solutions?",
    ["3", "2", "6", "12"],
    "Infinitely many solutions when a1/a2 = b1/b2 = c1/c2. Here 2/4 = 6/12 = 1/2, so k/6 = 1/2 and k = 3. "
    "2018 Q71 and 2021 Q71 asked the 'no solution' case (a1/a2 = b1/b2 ≠ c1/c2), and Q73 in both years asked for the name: parallel lines are 'inconsistent'. This is the third case.")
add(B, "ap", "apterm",
    "The 4th term of an A.P. is 17 and its 10th term is 41. What is its 20th term?",
    ["81", "85", "77", "89"],
    "From the 4th to the 10th term there are 6 steps: 6d = 41 − 17 = 24, so d = 4. Then a = 17 − 3 × 4 = 5. The 20th term = 5 + 19 × 4 = 81. "
    "Grew from 2021 Q74 (7th and 13th terms) and 2018 Q74.")
add(B, "ap", "apsum",
    "The sum of the first n terms of an A.P. is 2n² + 3n. What is its 10th term?",
    ["41", "43", "39", "230"],
    "The nth term = S(n) − S(n − 1). S(10) = 200 + 30 = 230 and S(9) = 162 + 27 = 189. The 10th term = 230 − 189 = 41. "
    "Shortcut: for S = pn² + qn, the nth term is p(2n − 1) + q = 2 × 19 + 3 = 41. Trap: 230 is the SUM of 10 terms. Grew from 2021 Q75 and Q76.")
add(B, "poly", "remainder",
    "When x³ − 2x² + kx + 5 is divided by (x − 2), the remainder is 11. What is the value of k?",
    ["3", "2", "4", "−3"],
    "Remainder theorem: the remainder on dividing by (x − 2) is the value at x = 2. 8 − 8 + 2k + 5 = 11, so 2k = 6 and k = 3. "
    "Grew from 2018 Q66 (x³ + 3x² − kx + 4 divided by x − 2).")
add(B, "det", "det",
    "If the determinant |x 4; 3 x| equals the determinant |2 4; 3 6|, then x = ? (Each pair of numbers after a semicolon is one row.)",
    ["±2√3", "±3", "2√3 only", "±4"],
    "A 2 × 2 determinant |a b; c d| = ad − bc. Left: x² − 12. Right: 12 − 12 = 0. So x² = 12 and x = ±√12 = ±2√3. "
    "Grew from 2021 Q69 and Q70 (determinant and 2M + N). Only 2 × 2 work has been asked so far.")

# ============================================================ MENSURATION (2018 Q86–88, 2021 Q86–88)
add(M, "vol", "wire",
    "A solid metal sphere of radius 6 cm is melted and drawn into a wire of radius 0.2 cm. What is the length of the wire?",
    ["72 m", "36 m", "144 m", "7.2 m"],
    "Volume stays the same. Sphere: 4/3 × π × 6³ = 288π cm³. Wire (a cylinder): π × 0.2² × h = 0.04πh. So h = 288 ÷ 0.04 = 7,200 cm = 72 m. "
    "Grew from 2018 Q86 (a cylinder recast into spheres). Watch the units: the answer options are in metres.")
add(M, "area", "wheel",
    "A wheel of diameter 70 cm rolls without slipping. How many revolutions will it make in covering 1.1 km? (Take π = 22/7.)",
    ["500", "250", "400", "550"],
    "One turn covers the circumference: π × 70 = 22/7 × 70 = 220 cm. 1.1 km = 1,10,000 cm. Turns = 1,10,000 ÷ 220 = 500. "
    "Trap: 250 comes from using the radius (2πr with r = 70). Grew from 2018 Q87 (diameter 105 cm, 330 m).")
add(M, "surf", "cone",
    "A cone has base radius 7 cm and height 24 cm. What is its curved surface area? (Take π = 22/7.)",
    ["550 cm²", "704 cm²", "616 cm²", "528 cm²"],
    "Slant height l = √(7² + 24²) = √625 = 25 cm. Curved surface = πrl = 22/7 × 7 × 25 = 550 cm². "
    "Trap: 704 cm² is the TOTAL surface (550 + base 154). Grew from 2021 Q88 (cone, base and surface ratio). 7, 24, 25 is a Pythagorean triple worth learning.")

# ============================================================ STATISTICS AND PROBABILITY (2018 Q79–100, 2021 Q79–100, 2025 Q88)
add(S, "prob", "diceprime",
    "Two dice are thrown together. What is the probability that the sum of the numbers is a prime number?",
    ["5/12", "1/2", "7/18", "1/3"],
    "There are 36 outcomes. Prime sums: 2 (1 way), 3 (2 ways), 5 (4 ways), 7 (6 ways), 11 (2 ways) = 15 ways. Probability = 15/36 = 5/12. "
    "Grew from 2018 Q80 (sum 6) and Q92 (sum 5). Learn the sum counts: 2→1, 3→2, 4→3, 5→4, 6→5, 7→6, then back down to 12→1.")
add(S, "prob", "leap",
    "What is the probability that a leap year, chosen at random, has 53 Sundays?",
    ["2/7", "1/7", "3/7", "5/7"],
    "A leap year has 366 days = 52 weeks + 2 extra days. The 2 extra days can be (Sun, Mon), (Mon, Tue) ... (Sat, Sun): 7 pairs, and 2 of them include a Sunday. So 2/7. "
    "2021 Q80 asked the non-leap year (1 extra day, answer 1/7). The leap year is the obvious next question.")
add(S, "prob", "coins",
    "Three coins are tossed together. What is the probability of getting at least two heads?",
    ["1/2", "3/8", "1/8", "7/8"],
    "There are 8 outcomes. At least two heads: HHT, HTH, THH, HHH = 4. Probability = 4/8 = 1/2. "
    "Trap: 3/8 is 'exactly two heads'. Grew from 2018 Q83 (all heads) and 2021 Q90 (exactly 2 heads with 4 coins).")
add(S, "prob", "socks",
    "A bag has 5 red and 4 green balls. Two balls are drawn at random. What is the probability that both are of the same colour?",
    ["4/9", "5/9", "1/2", "2/9"],
    "Ways to pick 2 from 9 = 9C2 = 36. Both red = 5C2 = 10. Both green = 4C2 = 6. Probability = (10 + 6)/36 = 16/36 = 4/9. "
    "Grew from 2018 Q91 (5 brown and 4 white socks). 5/9 is the chance of DIFFERENT colours.")
add(S, "comb", "committee",
    "In how many ways can a committee of 4 be chosen from 9 people?",
    ["126", "3,024", "252", "84"],
    "Order does not matter in a committee, so use combinations: 9C4 = (9 × 8 × 7 × 6)/(4 × 3 × 2 × 1) = 3,024/24 = 126. "
    "Trap: 3,024 is the number of ordered arrangements. Grew from 2025 Q88 (a cricket eleven from 15 players = 15C11 = 15C4 = 1,365).")
add(S, "stat", "median",
    "Find the median of this distribution. Class: 0–10, 10–20, 20–30, 30–40, 40–50. Frequency: 6, 14, 20, 6, 4.",
    ["22.5", "25", "21.5", "23.5"],
    "N = 50, so N/2 = 25. Running totals: 6, 20, 40 ... The 25th value lies in 20–30. "
    "Median = L + (N/2 − cf)/f × h = 20 + (25 − 20)/20 × 10 = 22.5. "
    "Grew from 2021 Q100 and 2018 Q97. L is the lower limit of the median class, cf the running total BEFORE it, f its frequency, h the class width.")
add(S, "stat", "mean3",
    "The mean of 5 observations is 15. The mean of the first three is 14 and the mean of the last three is 17. What is the third observation?",
    ["18", "15", "16", "17"],
    "Total of all 5 = 75. First three = 42 and last three = 51. Together they make 93, which counts the third observation twice. So the third = 93 − 75 = 18. "
    "Grew from 2021 Q95 (30 numbers, find the last) and 2018 Q96 (sum of 7 variates).")
add(S, "stat", "empirical",
    "For a moderately skewed distribution, the mean is 34.5 and the median is 32. Using the empirical relation, the mode is:",
    ["27", "29.5", "37", "33.25"],
    "Empirical relation: Mode = 3 × Median − 2 × Mean = 96 − 69 = 27. "
    "This is the one Class 10 statistics formula that has not yet come in the paper. 2018 Q98 asked a mode from a table and 2021 Q97/99 asked about deviations, so the family is live.")

assert len(Q) == 50, len(Q)
