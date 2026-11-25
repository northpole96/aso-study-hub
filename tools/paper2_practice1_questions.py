# Paper II Practice 01 (25 Nov 2026): 50 questions, 45 minutes, mock style. User asked "a set of 50 practice question from
# number series, number rank, divisibility, then time and work, train in mock style".
# 12 Number series (only rules not used in Set 01, Set 02 or the patterns sheet, plus new ones), 10 Number ranking,
# 8 divisibility, 10 time and work (with pipes), 10 trains. Hand-made from the Number Series Guide, the Ranking
# set and Arithmetic Guide chapters 8 to 10 and the work and train families; order given (booklet order: Reasoning then Maths).
# Build: python3 .claude/skills/aso-mock/scripts/build.py tools/paper2_practice1_questions.py  (calc re-checks every number answer)

META = dict(
    paper="maths",
    extra_labels=["Number series", "Number ranking"],
    title="ASO Paper II Practice 01",
    hub_title="Paper II Practice 01",
    masthead="Practice P2-01",
    heading="Paper II · Reasoning and Maths · Practice set",
    tagline="50 questions on <b>number series, ranking, divisibility,<br>time and work, and trains</b>, in mock style.",
    key="aso-paper2-practice-1",
    code="P2P1",
    out="ASO-Paper-II-Practice-1.html",
    minutes=45,
    seed=20261125,
    order="given",
    date="25 Nov 2026",
    draw="hand-made on the user's request (no draw)",
    topic="ari",
    weights_note="The mix is the user's choice: 12 number series, 10 ranking, 8 divisibility, 10 time and work, 10 trains.",
    intro=[
        "This is a practice set in mock style: fifty questions in forty-five minutes, in booklet order. The first twenty-two "
        "are Reasoning (number series, then ranking and order). The last twenty-eight are Maths: divisibility, time and work "
        "(pipes included) and trains. Each question is a likely next angle of a past question of 2018, 2021 or 2025.",
        "The series use only rules that Number Series Set 01 and Set 02 did not use, plus a few new ones. Every answer shows "
        "its working and its type, so a wrong answer tells you which rule to revise. Press Copy answers at the end and paste "
        "the report into the chat for a redo set.",
    ],
)

Q = []
def add(s, q, o, e, k="one", n=False, c=False, a=None, **x):
    d = dict(s=s, q=q, o=o, e=e, k=k, n=n, c=c, a=a); d.update(x); Q.append(d)

S = "Number series"
R = "Number ranking"
A = "Arithmetic"
SQ = "Find the missing number in the series:\n"

# ------------------------------------------------------------------ number series (12)
add(S, SQ + "3, 4, 8, 17, 33, ?", ["58", "57", "56", "60"],
    "Type: gaps are squares. Gaps: 1, 4, 9, 16, so the next gap is 25. 33 + 25 = 58.", nocalc=True)
add(S, SQ + "2, 3, 11, 38, 102, ?", ["227", "217", "197", "232"],
    "Type: gaps are cubes. Gaps: 1³, 2³, 3³, 4³ = 1, 8, 27, 64. The next gap is 5³ = 125. 102 + 125 = 227.", nocalc=True)
add(S, SQ + "12, 20, 30, 42, 56, ?", ["72", "70", "68", "64"],
    "Type: n² + n. The terms are 3×4, 4×5, 5×6, 6×7, 7×8, so the next is 8×9 = 72. Check: the gaps 8, 10, 12, 14 grow by 2, so the next gap is 16 and 56 + 16 = 72.", nocalc=True)
add(S, SQ + "3, 8, 15, ?, 35, 48", ["24", "23", "25", "26"],
    "Type: n² − 1. The terms are 2²−1, 3²−1, 4²−1, 5²−1 = 24, 6²−1 = 35, 7²−1 = 48. The gaps 5, 7, 9, 11, 13 also fit.", nocalc=True)
add(S, SQ + "6, 24, 60, 120, 210, ?", ["336", "330", "320", "342"],
    "Type: n³ − n. The terms are 2³−2, 3³−3, 4³−4, 5³−5, 6³−6 = 210, so the next is 7³ − 7 = 343 − 7 = 336.", nocalc=True)
add(S, SQ + "4, 18, 48, 100, 180, ?", ["294", "288", "300", "276"],
    "Type: n³ − n². The terms are 2³−2², 3³−3², 4³−4², 5³−5², 6³−6² = 180. The next is 7³ − 7² = 343 − 49 = 294.", nocalc=True)
add(S, SQ + "1, 2, 6, 21, 88, ?", ["445", "440", "450", "441"],
    "Type: × n + n. 1×1+1 = 2, 2×2+2 = 6, 6×3+3 = 21, 21×4+4 = 88. Next: 88×5 + 5 = 445.", nocalc=True)
add(S, SQ + "3, 8, 23, 68, ?", ["203", "204", "202", "208"],
    "Type: × 3 − 1. 3×3−1 = 8, 8×3−1 = 23, 23×3−1 = 68. Next: 68×3 − 1 = 203.", nocalc=True)
add(S, SQ + "20, 23, 19, 24, 18, ?", ["25", "17", "26", "24"],
    "Type: signs alternate, sizes grow by 1. +3, −4, +5, −6, then +7. 18 + 7 = 25. Trap: 17 comes from keeping the minus sign.", nocalc=True)
add(S, "Find the wrong number in the series:\n9, 16, 23, 30, 38, 44, 51", ["38", "30", "44", "23"],
    "Type: wrong-term, fixed gap. Most gaps are 7, so the series is 9, 16, 23, 30, 37, 44, 51. Only 38 breaks it (it should be 37).", nocalc=True)
add(S, SQ + "2, 3, 6, 10, 17, ?", ["28", "27", "29", "26"],
    "Type: sum of the two before, plus 1. 2+3+1 = 6, 3+6+1 = 10, 6+10+1 = 17, so the next is 10+17+1 = 28.", nocalc=True)
add(S, SQ + "40, 25, 15, 10, 5, ?", ["5", "0", "10", "15"],
    "Type: difference of the two before. 40−25 = 15, 25−15 = 10, 15−10 = 5, 10−5 = 5. So the next term is 5.", nocalc=True)

# ------------------------------------------------------------------ number ranking and order (10)
add(R, "Meena is 14th from the left end and 19th from the right end of a row of girls. How many girls are there in the row?",
    ["32", "33", "34", "31"],
    "Type: row total = left rank + right rank − 1 = 14 + 19 − 1 = 32. Trap: 33 forgets to take Meena out once.", calc="14+19-1")
add(R, "Ajay is 12th from the left and Vijay is 15th from the right in a row. When they swap places, Ajay becomes 20th from the left. How many persons are in the row?",
    ["34", "35", "32", "33"],
    "Type: swap. After the swap Ajay sits in Vijay's old seat, so Vijay's seat is 20th from the left and 15th from the right. Total = 20 + 15 − 1 = 34.", calc="20+15-1")
add(R, "In a row of 50 children, Sita is 18th from the left end and Gita is 15th from the right end. How many children are between them?",
    ["17", "16", "18", "19"],
    "Type: persons between. Gita from the left = 50 − 15 + 1 = 36. Between 18 and 36 there are 36 − 18 − 1 = 17 children.", calc="50-15+1-18-1")
add(R, "In a class of 40 students, Rohit is 25th from the top and Mohit is 22nd from the bottom. How many students are between them?",
    ["5", "4", "6", "3"],
    "Type: persons between. Mohit from the top = 40 − 22 + 1 = 19. Between 19 and 25 there are 25 − 19 − 1 = 5 students.", calc="25-(40-22+1)-1")
add(R, "In a row, Amit is 9th from the left end and Binod is 14th from the right end. Exactly 5 persons stand between them, and Amit is to the left of Binod. How many persons are in the row?",
    ["28", "27", "29", "30"],
    "Type: row total with persons between. Binod from the left = 9 + 5 + 1 = 15. Total = 15 + 14 − 1 = 28.", calc="9+5+1+14-1")
add(R, "If the letters of the word TRAIN are arranged in alphabetical order, which letter will be third from the left?",
    ["N", "I", "R", "A"],
    "Type: dictionary order of letters. A, I, N, R, T. The third letter from the left is N.", nocalc=True)
add(R, "Arrange these words as they come in a dictionary and choose the one that comes third:\nPencil, Pearl, Peace, Pebble, Pear",
    ["Pearl", "Pear", "Pebble", "Peace"],
    "Type: dictionary order of words. Peace (c is before r), Pear, Pearl (a shorter word comes first), Pebble (b after a), Pencil. The third word is Pearl.", nocalc=True)
add(R, "Five friends P, Q, R, S and T have different heights. P is taller than Q but shorter than R. S is taller than R. T is shorter than Q. Who is in the middle when they stand in order of height?",
    ["P", "Q", "R", "S"],
    "Type: ordering puzzle. S > R > P > Q > T. The middle (third) person is P.", nocalc=True)
add(R, "In a class, Kavita is 11th from the top. Lata is 16 places below Kavita and is 9th from the bottom. How many students are in the class?",
    ["35", "36", "34", "37"],
    "Type: rank from both ends. Lata from the top = 11 + 16 = 27. Total = 27 + 9 − 1 = 35.", calc="11+16+9-1")
add(R, "What is the 9th letter to the left of the 14th letter from the right end of the English alphabet?",
    ["D", "E", "C", "F"],
    "Type: alphabet position. The 14th from the right end is 26 − 14 + 1 = 13th from the left, which is M. The 9th letter to the left of M is the 13 − 9 = 4th letter, D.", nocalc=True)

# ------------------------------------------------------------------ divisibility (8)
add(A, "Which of the following numbers is exactly divisible by 11?",
    ["8547", "8557", "8447", "8741"],
    "Type: divisibility by 11. Subtract the sums of alternate digits. 8547: (8 + 4) − (5 + 7) = 0, so it divides: 8547 = 11 × 777. The others leave 1, 1 and 4 as the difference, so none divides.",
    calc="8547 * (8547 % 11 == 0)")
add(A, "If the four-digit number 47x5 is exactly divisible by 9, what is the digit x?",
    ["2", "3", "6", "7"],
    "Type: divisibility by 9. The digit sum 4 + 7 + x + 5 = 16 + x must be a multiple of 9. 16 + 2 = 18, so x = 2.",
    calc="(9 - 16 % 9) % 9")
add(A, "What is the least number that must be added to 5000 to make it exactly divisible by 12?",
    ["4", "8", "6", "2"],
    "Type: least number to add. 5000 ÷ 12 leaves remainder 8 (12 × 416 = 4992). So add 12 − 8 = 4. Trap: 8 is what you take away.",
    calc="(12 - 5000 % 12) % 12")
add(A, "The greatest four-digit number exactly divisible by 15 is:",
    ["9990", "9995", "9975", "9900"],
    "Type: greatest number with a limit. 9999 ÷ 15 leaves 9 (15 × 666 = 9990). Take the remainder away: 9999 − 9 = 9990.",
    calc="9999 - 9999 % 15")
add(A, "How many numbers from 1 to 100 are divisible by 3 or by 5?",
    ["47", "53", "33", "52"],
    "Type: counting multiples. Multiples of 3: 33. Multiples of 5: 20. Multiples of both (15): 6, counted twice. So 33 + 20 − 6 = 47.",
    calc="100//3 + 100//5 - 100//15")
add(A, "A number leaves remainder 5 when it is divided by 7. What remainder will twice that number leave when divided by 7?",
    ["3", "5", "10", "2"],
    "Type: remainder of a multiple. Twice the remainder is 10, and 10 is more than 7, so divide again: 10 ÷ 7 leaves 3. Check with 12: 24 ÷ 7 leaves 3.",
    calc="(2 * 5) % 7")
add(A, "A number leaves remainder 29 when divided by 56. What is the remainder when the same number is divided by 8?",
    ["5", "3", "7", "1"],
    "Type: remainder by a factor. 8 divides 56, so the remainder by 8 is the remainder of 29 by 8: 29 = 3 × 8 + 5. Answer 5. (This works only because 8 is a factor of 56.)",
    calc="29 % 8")
add(A, "If the five-digit number 82x46 is exactly divisible by 11, what is the digit x?",
    ["3", "4", "2", "0"],
    "Type: divisibility by 11. Digits at odd places from the right: 6, x, 8 add to 14 + x. Digits at even places: 4 and 2 add to 6. The difference 8 + x must be 0 or 11, so x = 3 (82346 = 11 × 7486).",
    calc="(11 - 8) % 11")

# ------------------------------------------------------------------ time and work (10)
add(A, "A can finish a piece of work in 15 days and B can finish it in 10 days. Working together, in how many days will they finish it?",
    ["6", "5", "8", "12"],
    "Type: A + B together. One day's work: 1/15 + 1/10 = 5/30 = 1/6. So 6 days. (Shortcut: 15 × 10 ÷ 25 = 6.)",
    calc="1/(1/15 + 1/10)")
add(A, "A and B together can do a job in 8 days. A alone can do it in 12 days. In how many days can B alone do it?",
    ["24", "20", "16", "28"],
    "Type: find the partner. B's one day = 1/8 − 1/12 = 3/24 − 2/24 = 1/24. So B alone takes 24 days.",
    calc="1/(1/8 - 1/12)")
add(A, "A and B together can do a work in 10 days, B and C in 15 days, and A and C in 12 days. In how many days can all three together do it?",
    ["8", "9", "10", "7"],
    "Type: pairs. Add the three pair-rates: 1/10 + 1/15 + 1/12 = (6 + 4 + 5)/60 = 1/4. That is twice (A + B + C), so A + B + C = 1/8 and the three take 8 days.",
    calc="2/(1/10 + 1/15 + 1/12)")
add(A, "A can do a work in 20 days and B in 30 days. They work together for 6 days and then A leaves. In how many more days will B finish the rest?",
    ["15", "12", "18", "10"],
    "Type: one leaves. Together one day = 1/20 + 1/30 = 1/12. In 6 days they do 6/12 = 1/2. The other half is left for B at 1/30 per day: (1/2) ÷ (1/30) = 15 days.",
    calc="(1 - 6*(1/20 + 1/30))*30")
add(A, "12 men can build a wall in 15 days. How many days will 20 men take to build the same wall?",
    ["9", "10", "8", "12"],
    "Type: men and days (inverse). Total work = 12 × 15 = 180 man-days. 20 men take 180 ÷ 20 = 9 days.",
    calc="12*15/20")
add(A, "8 men working 6 hours a day can finish a work in 10 days. In how many days can 10 men working 8 hours a day finish it?",
    ["6", "5", "8", "4"],
    "Type: men, hours and days. Total work = 8 × 6 × 10 = 480 man-hours. 10 men × 8 hours = 80 man-hours a day, so 480 ÷ 80 = 6 days.",
    calc="8*6*10/(10*8)")
add(A, "A is twice as efficient as B. Together they can finish a work in 12 days. In how many days can B alone finish it?",
    ["36", "24", "18", "30"],
    "Type: efficiency ratio. A : B = 2 : 1, so together they do 3 parts a day. Total work = 3 × 12 = 36 parts. B does 1 part a day, so B alone needs 36 days.",
    calc="12*3")
add(A, "Pipe A can fill a tank in 6 hours and pipe B in 12 hours. Pipe C can empty the full tank in 8 hours. If all three pipes are opened together, in how many hours will the empty tank be full?",
    ["8", "6", "10", "12"],
    "Type: pipes with an outlet. In one hour: 1/6 + 1/12 − 1/8 = (4 + 2 − 3)/24 = 3/24 = 1/8. So the tank fills in 8 hours.",
    calc="1/(1/6 + 1/12 - 1/8)")
add(A, "A pump can fill a tank in 4 hours. Because of a leak in the bottom, it takes 5 hours. In how many hours can the leak alone empty the full tank?",
    ["20", "9", "10", "25"],
    "Type: a leak. Leak's one hour = 1/4 − 1/5 = 1/20. So the leak alone empties the full tank in 20 hours. Trap: 9 comes from adding 4 and 5.",
    calc="1/(1/4 - 1/5)")
add(A, "A can finish a work in 10 days and B in 15 days. They work on alternate days, A on the first day. In how many days will the work be finished?",
    ["12", "11", "13", "10"],
    "Type: alternate days. In two days (A then B) they do 1/10 + 1/15 = 1/6. After 6 such pairs, that is 12 days, the whole work is done, and the last day (the 12th) is B's. So 12 days.",
    calc="6*2")

# ------------------------------------------------------------------ trains (10)
add(A, "A train 120 m long runs at 54 km/h. How many seconds does it take to pass a telegraph pole?",
    ["8", "6", "10", "9"],
    "Type: train and pole. 54 km/h = 54 × 5/18 = 15 m/s. The train covers its own length: 120 ÷ 15 = 8 seconds.",
    calc="120/(54*5/18)")
add(A, "A train 200 m long passes a platform 300 m long in 25 seconds. What is the speed of the train in km/h?",
    ["72", "60", "80", "64"],
    "Type: train and platform. Distance = 200 + 300 = 500 m in 25 s = 20 m/s. 20 × 18/5 = 72 km/h.",
    calc="500/25*18/5")
add(A, "Two trains 90 m and 120 m long run in opposite directions at 60 km/h and 66 km/h. In how many seconds will they cross each other?",
    ["6", "7", "5", "8"],
    "Type: two trains, opposite. Relative speed = 60 + 66 = 126 km/h = 126 × 5/18 = 35 m/s. Distance = 90 + 120 = 210 m. Time = 210 ÷ 35 = 6 seconds.",
    calc="210/(126*5/18)")
add(A, "A train 120 m long runs at 90 km/h and overtakes another train 80 m long running in the same direction at 54 km/h. How many seconds does it take to pass it completely?",
    ["20", "18", "25", "10"],
    "Type: two trains, same direction. Relative speed = 90 − 54 = 36 km/h = 10 m/s. Distance = 120 + 80 = 200 m. Time = 200 ÷ 10 = 20 seconds.",
    calc="200/(36*5/18)")
add(A, "A train 180 m long passes a man walking at 6 km/h in the same direction in 18 seconds. What is the speed of the train in km/h?",
    ["42", "30", "36", "48"],
    "Type: train and a man, same direction. Relative speed = 180 ÷ 18 = 10 m/s = 36 km/h. The man walks the same way, so the train is 6 km/h faster than him: 36 + 6 = 42 km/h.",
    calc="180/18*18/5 + 6")
add(A, "A train 150 m long passes a man running at 9 km/h in the opposite direction in 10 seconds. What is the speed of the train in km/h?",
    ["45", "54", "63", "36"],
    "Type: train and a man, opposite direction. Relative speed = 150 ÷ 10 = 15 m/s = 54 km/h. The man comes towards the train, so subtract his speed: 54 − 9 = 45 km/h.",
    calc="150/10*18/5 - 9")
add(A, "Two trains, each 150 m long, run on parallel tracks in opposite directions. They take 15 seconds and 10 seconds to cross a telegraph pole. In how many seconds will they cross each other?",
    ["12", "15", "10", "13"],
    "Type: two trains, opposite, speeds from poles. Speeds: 150/15 = 10 m/s and 150/10 = 15 m/s. Relative speed 25 m/s. Distance 300 m. Time = 300 ÷ 25 = 12 seconds.",
    calc="300/(150/15 + 150/10)")
add(A, "A train passes a pole in 20 seconds and a 250 m long bridge in 30 seconds. What is the length of the train?",
    ["500 m", "450 m", "400 m", "550 m"],
    "Type: pole and bridge. The extra 10 seconds are spent on the bridge's 250 m, so the speed is 25 m/s. Length of train = 25 × 20 = 500 m. Check: (500 + 250) ÷ 30 = 25 m/s.",
    calc="250*20/(30-20)")
add(A, "A train 300 m long, running at 72 km/h, passes completely through a tunnel in 40 seconds. What is the length of the tunnel?",
    ["500 m", "800 m", "400 m", "600 m"],
    "Type: train and tunnel. Speed = 72 × 5/18 = 20 m/s. Distance in 40 s = 800 m = train + tunnel. Tunnel = 800 − 300 = 500 m.",
    calc="72*5/18*40 - 300")
add(A, "A train leaves a station at 60 km/h. Two hours later a second train leaves the same station on the same track in the same direction at 80 km/h. After how many hours from its own start will the second train overtake the first?",
    ["6", "5", "8", "4"],
    "Type: overtaking from a station. In 2 hours the first train is 60 × 2 = 120 km ahead. The second gains 80 − 60 = 20 km every hour, so it needs 120 ÷ 20 = 6 hours.",
    calc="60*2/(80-60)")
