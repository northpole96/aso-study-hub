# Reasoning Mock 01 (22 Nov 2026): the first Reasoning mock made with the aso-mock skill.
# Plan: python3 .claude/skills/aso-mock/scripts/draw.py reasoning --n 50 --seed 989549
# Build: python3 .claude/skills/aso-mock/scripts/build.py tools/reasoning_mock1_questions.py
# First option is right unless a is given. Figures are drawn below from small helpers, so the right
# figure and the traps come from the same shape (mirror, water image, rotation).
import math

META = dict(
    paper="reasoning",
    title="ASO Reasoning Mock 01",
    hub_title="Reasoning Mock 01",
    masthead="Reasoning 01",
    heading="Paper II (A) · Reasoning and Mental Ability · Mock 01",
    tagline="50 questions drawn by probability<br>from the <b>2018, 2021 and 2025</b> papers.",
    key="aso-reasoning-mock-2027-1",
    code="RE01",
    out="ASO-Reasoning-Mock-2027-1.html",
    minutes=45,
    seed=20261122,
    order="mixed",
    date="22 Nov 2026",
    draw="python3 scripts/draw.py reasoning --n 50 --seed 989549",
    intro=[
        "This is the first half of Paper II on its own: fifty Reasoning questions in forty-five minutes, the time you get "
        "in the hall if you split the ninety minutes evenly with Maths. Every topic has its share from the 2018, 2021 and "
        "2025 papers (2021 and 2025 at full weight, 2018 at half), and inside each topic the question families were drawn "
        "by how often the examiner uses them.",
        "Fifteen questions have figures, as in the real booklet: series, mirror and water images, a net, a die, paper "
        "folding, counting, grouping and an embedded figure. Three are real past questions word for word (2025 Q43, "
        "2021 Q20 and 2021 Q41), because this paper repeats itself more than any other. Every answer shows the working "
        "and the shortcut.",
    ],
)

Q = []
def add(s, q, o, e, k="one", n=False, c=False, a=None, **x):
    d = dict(s=s, q=q, o=o, e=e, k=k, n=n, c=c, a=a); d.update(x); Q.append(d)

# ---------------------------------------------------------------- figure helpers
INK, BLUE = "#111", "#2b4cff"
def svg(w, h, body):
    st = ' style="max-width:%dpx"' % int(w * 1.5) if w < 400 else ""
    return ('<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" fill="none" stroke="%s" stroke-width="1.5" '
            'stroke-linecap="round" stroke-linejoin="round" font-family="IBM Plex Mono, monospace"%s>%s</svg>' % (w, h, INK, st, body))
def tx(x, y, t, size=13, anchor="middle", color=INK, extra=""):
    return '<text x="%g" y="%g" font-size="%d" text-anchor="%s" dominant-baseline="central" fill="%s" stroke="none"%s>%s</text>' % (x, y, size, anchor, color, extra, t)
def rect(x, y, w, h, dash=False):
    return '<rect x="%g" y="%g" width="%g" height="%g"%s/>' % (x, y, w, h, ' stroke-dasharray="4 3"' if dash else "")
def line(x1, y1, x2, y2, dash=False, color=INK):
    return '<line x1="%g" y1="%g" x2="%g" y2="%g"%s%s/>' % (x1, y1, x2, y2, ' stroke-dasharray="4 3"' if dash else "", "" if color == INK else ' stroke="%s"' % color)
def poly(pts, closed=True):
    p = " ".join("%g,%g" % xy for xy in pts)
    return '<%s points="%s"/>' % ("polygon" if closed else "polyline", p)
def dot(x, y, r=3.2):
    return '<circle cx="%g" cy="%g" r="%g" fill="%s" stroke="none"/>' % (x, y, r, INK)
def ring(x, y, r):
    return '<circle cx="%g" cy="%g" r="%g"/>' % (x, y, r)
def lab(x, y, t):
    return tx(x, y, t, 12)
def rot(p, deg):
    a = math.radians(deg); x, y = p
    return (x * math.cos(a) - y * math.sin(a), x * math.sin(a) + y * math.cos(a))
def move(pts, cx, cy, deg=0, fx=1, fy=1, s=1):
    out = []
    for x, y in pts:
        x, y = rot((x * fx, y * fy), deg)
        out.append((round(cx + s * x, 1), round(cy + s * y, 1)))
    return out

# ---------------------------------------------------------------- Number series (5)
add("Number series", "Find the wrong term in the series:\n0, 2, 6, 12, 20, 30, 40, 56",
    ["40", "30", "20", "56"],
    "Each term is n × (n − 1): 1×0 = 0, 2×1 = 2, 3×2 = 6, 4×3 = 12, 5×4 = 20, 6×5 = 30, 7×6 = 42, 8×7 = 56. "
    "So 40 should be 42. Quick check: the gaps are 2, 4, 6, 8, 10, then 10 and 16 break the even run. "
    "Grew from: the wrong-term questions of 2021 Q30/Q32 and 2025 Q48–50 (asked in both papers, once word for word). "
    "Family: test the gaps first, then ×2, ×5 chains, then n² and n³ patterns.")
add("Number series", "If the English alphabet is written in reverse order, which letter will be seventh to the right of the twelfth letter from the left?",
    ["H", "I", "G", "S"],
    "Reverse order means Z is first. Twelfth from the left = 26 − 12 + 1 = 15th letter of the normal alphabet = O. "
    "Seventh to the right of it is the 19th from the left in the reversed list = 26 − 19 + 1 = 8th letter = H. "
    "Shortcut: in the reversed alphabet, position p holds the letter 27 − p. "
    "Grew from: 2018 Q6 (eighth to the right of the tenth from the left). Family: letter positions, swaps in a word, reversed alphabet.")
add("Number series", "Find the missing number:\n2, 5, 11, 20, 32, ?, 65",
    ["47", "45", "49", "44"],
    "The gaps are 3, 6, 9, 12, then 15 and 18 (multiples of 3). 32 + 15 = 47, and 47 + 18 = 65 confirms it. "
    "Grew from: 2018 Q13–15 and 2025 Q15 (missing number). Family: gaps in A.P., differences of differences, two series mixed, squares and cubes.")
add("Number series", "How many 7s in the following string are immediately preceded by an odd digit and immediately followed by a perfect square?\n5 7 4 8 3 7 9 2 7 1 6 9 7 4 3 7 8 1 7 9 2 7 6 5 7 2 4 7 0",
    ["4", "5", "3", "6"],
    "Check every 7 with its two neighbours. 5-7-4 yes; 3-7-9 yes; 2-7-1 no (2 is even); 9-7-4 yes; 3-7-8 no (8 is not a square); "
    "1-7-9 yes; 2-7-6 no; 5-7-2 no; 4-7-0 no (4 is even). So 4. "
    "Method: mark each 7, look left, then right; never count in your head. "
    "Grew from: 2018 Q3 (4s preceded by 7 but not followed by 3).")
add("Number series", "Find the missing number:\n2, 3, 8, 27, 112, ?",
    ["565", "560", "452", "570"],
    "The rule is × n + n: 2 × 1 + 1 = 3, 3 × 2 + 2 = 8, 8 × 3 + 3 = 27, 27 × 4 + 4 = 112, 112 × 5 + 5 = 565. "
    "When the terms grow fast, try 'multiply by 1, 2, 3 ...' before squares. "
    "Grew from: 2018 Q15 (1, 2, 3, 10, ?, 9802, an n² + 1 chain). Family: chains where each term is built from the one before.")

# ---------------------------------------------------------------- Direction sense (3)
add("Direction sense", "If North-West becomes South, South-West becomes East, and all other directions change in the same way, what will North become?",
    ["South-West", "South-East", "North-East", "East"],
    "North-West (315°) became South (180°): every direction turns by 135° anticlockwise (or 225° clockwise). "
    "Check: South-West (225°) − 135° = 90° = East. So North (0°) − 135° = 225° = South-West. "
    "Grew from: 2018 Q4 (South-East becomes North). Method: find the turn from one given pair, test it on the second, apply it.")
add("Direction sense", "Rahul is facing North-East. He turns 135° anticlockwise, then 270° clockwise and then 90° anticlockwise. In which direction is he facing now?",
    ["East", "West", "North", "South-East"],
    "Count in degrees from North, clockwise positive. North-East = 45°. 45 − 135 = −90 (West). −90 + 270 = 180 (South). 180 − 90 = 90 = East. "
    "Shortcut: add all turns first: −135 + 270 − 90 = +45 clockwise, and North-East + 45° = East. "
    "Grew from: 2021 Q37 = 2025 Q29 (facing West, 45°, 180°, 270°), asked word for word twice.")
add("Direction sense", "Leena walks 6 km towards the South. She turns left and walks 5 km, turns left again and walks 14 km, and then turns right and walks 1 km. How far and in which direction is she from her starting point?",
    ["10 km, North-East", "10 km, North-West", "14 km, North-East", "8 km, East"],
    "Track x (east) and y (north). South 6: (0, −6). Left of South is East, 5 km: (5, −6). Left of East is North, 14 km: (5, 8). "
    "Right of North is East, 1 km: (6, 8). Distance = √(6² + 8²) = 10 km; she is east and north of the start, so North-East. "
    "Grew from: 2025 Q4, Q17 and Q41 (walks with turns). The 6-8-10 and 3-4-5 triangles come again and again.")

# ---------------------------------------------------------------- Coding and decoding (5)
add("Coding and decoding", "If N = 28 and ORE = 76, then how will you code PALE?",
    ["68", "72", "76", "19"],
    "Exact past question. Each word = (sum of letter places) × 2. N = 14 × 2 = 28; ORE = (15 + 18 + 5) × 2 = 76. "
    "PALE = (16 + 1 + 12 + 5) × 2 = 34 × 2 = 68. "
    "Family: word = sum of letter values (VIRTUE 201, MOST 134), sum × letters, reverse values (Z = 1).", src="2025 Q43")
add("Coding and decoding", "In a certain code, GARDEN is written as TZIWVM. How will FLOWER be written in that code?",
    ["UOLDVI", "UOLDIV", "VOLDVI", "UOMDVI"],
    "Each letter is replaced by its opposite letter (A↔Z, B↔Y ...: the two places add up to 27). G(7)→T(20), A→Z, R(18)→I(9), D→W, E→V, N(14)→M(13). "
    "FLOWER: F(6)→U(21), L(12)→O(15), O→L, W(23)→D(4), E→V, R→I = UOLDVI. "
    "Learn the pairs: AZ, BY, CX, DW, EV, FU, GT, HS, IR, JQ, KP, LO, MN. "
    "Grew from: 2021 Q21, Q35, Q44 and 2025 Q2 (letter shifts).")
add("Coding and decoding", "In a code language:\n'pit na lo' means 'fresh milk daily'\n'na ro ke' means 'milk is sweet'\n'ke lo bi' means 'sweet fruits daily'\n'bi zu ro' means 'fruits is costly'\nWhich of the following is the code for 'fresh fruits'?",
    ["pit bi", "lo bi", "pit ke", "na bi"],
    "Common words give common codes. milk (lines 1, 2) = na; sweet (2, 3) = ke; daily (1, 3) = lo; so fresh = pit. "
    "fruits (3, 4) = bi; is (2, 4) = ro; costly = zu. So 'fresh fruits' = pit bi. "
    "Grew from: 2025 Q18 and Q30 (coded sentences, asked in every paper).")
add("Coding and decoding", "If SMART is coded as 41673 and TRAIN as 37652, how is SAINT coded?",
    ["46523", "46532", "64523", "46253"],
    "Each letter keeps one digit: S = 4, M = 1, A = 6, R = 7, T = 3, I = 5, N = 2 (A, R and T agree in both words). "
    "SAINT = 4 6 5 2 3. Trap: 46532 swaps N and T. "
    "Grew from: 2018 Q22 (ROSE = 6821, CHAIR = 73456: code SEARCH).")
add("Coding and decoding", "In a certain code, BOOK is written as CQRO. How will DESK be written in that code?",
    ["EGVO", "EGVN", "FGVO", "EFVO"],
    "Each letter moves forward by its place in the word: B+1 = C, O+2 = Q, O+3 = R, K+4 = O. "
    "DESK: D+1 = E, E+2 = G, S+3 = V, K+4 = O = EGVO. "
    "Grew from: 2021 Q21 (MOTHER → ONHURF) and 2025 Q2 (STRAIGHT → TSARGITH). Family: fixed shift, shift by place, opposite letters, reversed halves.")

# ---------------------------------------------------------------- Number ranking (5)
add("Number ranking", "P, Q, R, S, T, U and V each scored different marks in a test. Q scored more than only P. R scored less than T but more than S. V scored more than T. U scored more than V. Who scored the third highest marks?",
    ["T", "V", "R", "S"],
    "'More than only P' puts Q second from the bottom: P < Q < the rest. Then S < R < T < V < U. "
    "Full order from the top: U, V, T, R, S, Q, P. Third highest = T. "
    "Grew from: 2025 Q19 (seven persons of different heights).")
add("Number ranking", "In a row of 40 students facing North, Rohit is 15th from the left end. He moves 6 places to the right. What is his position from the right end now?",
    ["20th", "19th", "21st", "26th"],
    "New place from the left = 15 + 6 = 21. From the right = total − left + 1 = 40 − 21 + 1 = 20th. "
    "Grew from: 2025 Q32 (a row of 26: A moves three places left). Rule: left + right = total + 1.")
add("Number ranking", "Six friends A, B, C, D, E and F are of different heights. B is taller than D but shorter than E. A is taller than E. C is shorter than D. F is taller than A. How many of them are taller than B?",
    ["One", "Two", "Three", "Four"],
    "Build the chain: C < D < B < E < A < F. Taller than B: E, A and F = three. "
    "Grew from: 2025 Q19 (ordering by height).", a=2)
add("Number ranking", "Arrange the following words in the order in which they appear in a dictionary:\n1. Measure  2. Meadow  3. Meander  4. Mean  5. Meal",
    ["2, 5, 4, 3, 1", "2, 5, 3, 4, 1", "5, 2, 4, 3, 1", "2, 4, 5, 3, 1"],
    "All begin with MEA, so look at the fourth letter: d (Meadow), l (Meal), n (Mean, Meander), s (Measure). "
    "Mean comes before Meander because a shorter word that is the start of a longer one comes first. "
    "Order: Meadow, Meal, Mean, Meander, Measure = 2, 5, 4, 3, 1. "
    "Grew from: 2025 Q16, Q26, Q28 and 2021 Q42 (dictionary order, every year).")
add("Number ranking", "In a queue, Mina is 12th from the front and Tia is 18th from the back. Mina is ahead of Tia and there are 5 persons between them. How many persons are there in the queue?",
    ["35", "23", "34", "29"],
    "Mina's 12 (front to Mina) + 5 between + Tia's 18 (Tia to back) = 35. "
    "Trap 23 comes from the overlapping case (when Tia is ahead of Mina: 12 + 18 − 5 − 2). Read who is ahead before you add. "
    "Grew from: 2025 Q44 (Bhavuk and Bhavan with six boys between them).")

# ---------------------------------------------------------------- Arithmetic reasoning (5)
add("Arithmetic reasoning", "A tailor has a roll of cloth 60 metres long. He cuts a 2-metre piece from it every day. On which day will he make the last cut?",
    ["29th", "30th", "28th", "31st"],
    "60 m gives 30 pieces, but the last cut on day 29 leaves two pieces of 2 m at once. So only 30 − 1 = 29 cuts are needed. "
    "Grew from: 2021 Q6, Q7, Q11 and 2018 Q29 (word problems). Same idea: a log cut into 10 pieces needs 9 cuts.")
add("Arithmetic reasoning", "A purse has Rs 600 in 50 notes, all of them of Rs 10 or Rs 20. How many Rs 20 notes are there?",
    ["10", "40", "20", "15"],
    "If all 50 were Rs 10 notes, the total would be Rs 500. The extra Rs 100 comes from Rs 20 notes, each adding Rs 10, "
    "so there are 100 ÷ 10 = 10 Rs 20 notes (and 40 Rs 10 notes). "
    "Grew from: 2018 Q16 (two kinds of tickets) and 2021 Q11 (heads and legs): the same 'assume all are one kind' trick.")
add("Arithmetic reasoning", "The calendar for the year 2026 will be the same for which of the following years?",
    ["2037", "2032", "2036", "2043"],
    "2026 is not a leap year and begins on a Thursday. Add odd days year by year (1 for an ordinary year, 2 for a leap year): "
    "2026 to 2036 gives 1+1+2+1+1+1+2+1+1+1+2 = 14, a multiple of 7, so 1 January 2037 is again a Thursday, and 2037 is not a leap year. "
    "Shortcut for a year two after a leap year (2026 = 2024 + 2): add 11. "
    "Grew from: 2025 Q14 (the calendar for 2007).")
add("Arithmetic reasoning", "The average age of 30 students in a class is 15 years. When the teacher's age is included, the average rises by 1 year. What is the age of the teacher?",
    ["46 years", "31 years", "45 years", "47 years"],
    "Total of students = 30 × 15 = 450. With the teacher, 31 people average 16, total 496. Teacher = 496 − 450 = 46. "
    "Shortcut: teacher = old average + (new count × rise) = 15 + 31 × 1 = 46. "
    "Grew from: 2025 Q33 (averages of A, B, C and A, C, D) and 2021 Q28.")
add("Arithmetic reasoning", "If 26 January 2026 was a Monday, what day of the week was 15 August 2026?",
    ["Saturday", "Friday", "Sunday", "Thursday"],
    "Days from 26 January to 15 August: 5 (rest of January) + 28 + 31 + 30 + 31 + 30 + 31 + 15 = 201. "
    "201 = 7 × 28 + 5, so 5 days after Monday = Saturday. "
    "Grew from: 2021 Q12 (the day of 31 January 2007). Count the odd days, not the weeks.")

# ---------------------------------------------------------------- Blood relations (3)
FAM = ("Rani and Shreshtha are a married couple having two daughters, Medha and Deepti. Deepti is married to Anurag "
       "who is the son of Garima and Tarun. Nidhi is the daughter of Anurag. Komal, who is Anurag's sister, is married to "
       "Harshit and has two sons, Aman and Prem. Prem is the grandson of Garima and Tarun.")
add("Blood relations", "Read the passage above. Which of the following is true?",
    ["Garima is Harshit's mother-in-law", "Tarun is Deepti's maternal uncle", "Aman is the son of Medha", "Nidhi is cousin of Komal"],
    "Exact past question (the third of the 2021 Q18–20 set). Harshit is married to Komal, and Komal's mother is Garima, so Garima is Harshit's mother-in-law. "
    "The others: Tarun is Deepti's father-in-law; Aman is Komal's son; Nidhi is Komal's niece. "
    "Method: draw the tree first (couples on one line, children below) and answer from the drawing.", src="2021 Q20", p=FAM)
add("Blood relations", "P is the sister of Q. Q is the son of R. S is the father of R. T is the mother of S. How is P related to T?",
    ["Great-granddaughter", "Granddaughter", "Daughter", "Niece"],
    "Go up the chain: P and Q are children of R; R is a child of S; S is a child of T. So P is three steps below T, and P is a girl (sister): great-granddaughter. "
    "Grew from: 2018 Q11 (A is B's sister, C is B's mother, D is C's father, E is D's mother).")
add("Blood relations", "Pointing to a boy, Rekha said, \"His mother is the only daughter of my mother.\" How is the boy related to Rekha?",
    ["Son", "Nephew", "Brother", "Cousin"],
    "The only daughter of Rekha's mother is Rekha herself. So the boy's mother is Rekha, and he is her son. "
    "Grew from: 2018 Q9 and 2021 Q16 (pointing questions). Trap: 'only daughter of my mother' or 'only son of my father' is the speaker.")

# ---------------------------------------------------------------- Analogy and classification (6)
add("Analogy and classification", "Read these five words: THE MOD CPU RAM SHE\nIf the third alphabet in each of the word is changed to the next alphabet in English alphabetical order, how many words thus formed have more than two vowels?",
    ["None", "One", "Two", "Three"],
    "Exact past question. New words: THF, MOE, CPV, RAN, SHF. Vowels: 0, 2, 0, 1, 0. None has more than two. "
    "Same frame in 2025 Q27 (LAP BUT CAR SON HID). Expect the twin too: put the five words in dictionary order (CPU, MOD, RAM, SHE, THE).",
    src="2021 Q41", a=0)
add("Analogy and classification", "Arrange the following in a meaningful sequence:\n1. Harvesting  2. Sowing  3. Ploughing  4. Irrigation  5. Selling",
    ["3, 2, 4, 1, 5", "2, 3, 4, 1, 5", "3, 4, 2, 1, 5", "3, 2, 1, 4, 5"],
    "A farmer first ploughs (3), then sows (2), waters the crop (4), harvests (1) and sells (5). "
    "Grew from: 2018 Q1 (Presentation, Recommendation, Arrival, Discussion, Introduction).")
add("Analogy and classification", "Barometer : Pressure :: Hygrometer : ?",
    ["Humidity", "Temperature", "Rainfall", "Wind speed"],
    "A barometer measures air pressure; a hygrometer measures humidity (moisture in the air). "
    "Others in the family: anemometer – wind speed, rain gauge – rainfall, seismograph – earthquakes, tachometer – speed of rotation. "
    "Grew from: 2018 Q5 (Seismography : Earthquake :: Tachometer : ?).")
add("Analogy and classification", "Select the set in which the numbers are related in the same way as in the set (7, 3, 58).",
    ["(5, 4, 41)", "(6, 2, 38)", "(8, 3, 72)", "(9, 1, 81)"],
    "Rule: first² + second² = third. 7² + 3² = 49 + 9 = 58. (5, 4): 25 + 16 = 41. "
    "The others: 36 + 4 = 40 (not 38), 64 + 9 = 73 (not 72), 81 + 1 = 82 (not 81). "
    "Grew from: 2021 Q10/Q43 (24, 10, 392) and 2025 Q25 (18, 6, 216). Try ×, +, squares and cubes in that order.")
add("Analogy and classification", "Find the odd one out:\nWhale, Shark, Dolphin, Seal",
    ["Shark", "Whale", "Dolphin", "Seal"],
    "Whale, dolphin and seal are mammals (they breathe air and feed milk to their young). The shark is a fish. "
    "Grew from: 2025 Q40 (Parrot, Bat, Crow, Sparrow: the bat is the mammal among birds). The examiner likes 'looks alike, is not'.")
add("Analogy and classification", "Find the odd one out:\n51, 87, 91, 97",
    ["97", "51", "87", "91"],
    "97 is a prime number. The others look prime but are not: 51 = 3 × 17, 87 = 3 × 29, 91 = 7 × 13. "
    "Trap numbers to know: 51, 57, 87, 91, 119, 133, 143 are not prime. "
    "Grew from: 2018 Q24, 2021 Q22/Q23, 2025 Q40 (odd one out).")

# ---------------------------------------------------------------- Non-verbal series (2), figures
def arrow(cx, cy, deg):
    body = move([(0, 16), (0, -16)], cx, cy, deg)
    head = move([(-7, -8), (0, -17), (7, -8)], cx, cy, deg)
    return line(body[0][0], body[0][1], body[1][0], body[1][1]) + poly(head, False)
def nvs1_cell(x, y, deg, corner):
    s = rect(x, y, 70, 70) + arrow(x + 35, y + 35, deg)
    cx, cy = {"TL": (x + 11, y + 11), "BR": (x + 59, y + 59), "TR": (x + 59, y + 11), "BL": (x + 11, y + 59)}[corner]
    return s + dot(cx, cy)
def series_fig(cells_q, cells_a, cell):
    b = ""
    for i, args in enumerate(cells_q):
        x = 20 + i * 98
        b += cell(x, 22, *args) if args else rect(x, 22, 70, 70) + tx(x + 35, 57, "?", 26)
    b += line(10, 112, 510, 112, True)
    for i, args in enumerate(cells_a):
        x = 30 + i * 125
        b += cell(x, 140, *args) + lab(x + 35, 228, "(%d)" % (i + 1))
    return svg(520, 240, b)
F33 = series_fig([(0, "TL"), (45, "BR"), (90, "TL"), (135, "BR"), None],
                 [(180, "BR"), (180, "TL"), (225, "TL"), (0, "TL")], nvs1_cell)
add("Non-verbal series", "Which answer figure will come in place of the question mark (?) in the series?",
    ["1", "2", "3", "4"],
    "Two things change. The arrow turns 45° clockwise each step (up, up-right, right, down-right, so next is down). "
    "The dot jumps between the top-left and the bottom-right corner (TL, BR, TL, BR, so next is TL). Down arrow with the dot top-left = figure (2). "
    "Grew from: the five non-verbal series of 2025 (Q7, Q20, Q34, Q35). Look for two changes at once: a turn and a moving mark.",
    k="fig", a=1, f=F33)

def flag(cx, cy, deg):
    return poly(move([(0, -15), (13, 9), (-13, 9)], cx, cy, deg)) + dot(*move([(0, -5)], cx, cy, deg)[0], r=2.6)
def nvs2_cell(x, y, deg, n):
    b = rect(x, y, 70, 70) + flag(x + 35, y + 30, deg)
    start = x + 35 - (n - 1) * 5.5
    for i in range(n): b += dot(start + i * 11, y + 58, 2.6)
    return b
F34 = series_fig([(0, 1), (90, 2), (180, 3), (270, 4), None],
                 [(0, 5), (0, 4), (90, 5), (180, 5)], nvs2_cell)
add("Non-verbal series", "Select the answer figure that continues the series of figures.",
    ["1", "2", "3", "4"],
    "The triangle turns 90° clockwise each step (its point goes up, right, down, left), so the fifth points up again. "
    "One dot is added each step (1, 2, 3, 4), so the fifth has 5 dots. Point up with five dots = figure (1). "
    "Figure (2) has the right turn but only 4 dots. Grew from: 2025 Q7 and Q20 (series with a turn and a count).",
    k="fig", a=0, f=F34)

# ---------------------------------------------------------------- Mirror images (4)
add("Mirror images", "A clock seen in a mirror shows the time 4:25. What is the actual time?",
    ["7:35", "8:35", "7:25", "6:35"],
    "Actual time = 11:60 − shown time = 11:60 − 4:25 = 7:35. (If the result passes 12, take away 12.) "
    "Grew from: 2018 Q46, Q47 and 2021 Q50 (mirror clocks, three times). The same rule works backwards: shown = 11:60 − actual.")

WORD = "KONARK1250"
def word_row(x0, y, mode):
    chars = list(WORD)
    if mode in ("mirror", "rev"): chars = chars[::-1]
    out = ""
    for i, ch in enumerate(chars):
        x = x0 + i * 17
        if mode in ("mirror", "flipeach"): tr = ' transform="translate(%g %g) scale(-1 1)"' % (x, y)
        elif mode == "water": tr = ' transform="translate(%g %g) scale(1 -1)"' % (x, y)
        else: tr = ' transform="translate(%g %g)"' % (x, y)
        out += '<text x="0" y="0" font-size="21" text-anchor="middle" dominant-baseline="central" fill="%s" stroke="none"%s>%s</text>' % (INK, tr, ch)
    return out
def mirror_text_fig(opts):
    b = lab(30, 40, "(X)") + word_row(150, 40, "plain") + line(335, 14, 335, 66, True, BLUE) + tx(347, 40, "M", 11, "start", BLUE)
    b += line(10, 84, 510, 84, True)
    pos = [(40, 120), (290, 120), (40, 185), (290, 185)]
    for i, m in enumerate(opts):
        x, y = pos[i]
        b += lab(x - 12, y, "(%d)" % (i + 1)) + word_row(x + 22, y, m)
    return svg(520, 215, b)
F36 = mirror_text_fig(["water", "rev", "flipeach", "mirror"])
add("Mirror images", "Which answer figure is the correct mirror image of the word (X) when the mirror is held on its right side (line M)?",
    ["1", "2", "3", "4"],
    "A mirror on the right reverses the order (the last character comes first, next to the mirror) and also flips every character left to right. "
    "Figure (4) does both. (1) is the water image (upside down), (2) only reverses the order, (3) only flips each letter in place. "
    "Grew from: 2021 Q46 = 2018 Q42 (TARAIN1014A, asked twice) and 2025 Q36 (EFFECTIVE). Symmetric letters (A, O, H, I, M, T ...) look the same, so judge by K, N, R and the digits.",
    k="fig", a=3, f=F36)

FLAGPTS = [(-8, -26), (-8, 26)]
def flag_shape(cx, cy, fx=1, fy=1, deg=0):
    pole = move(FLAGPTS, cx, cy, deg, fx, fy)
    tri = move([(-8, -26), (16, -17), (-8, -8)], cx, cy, deg, fx, fy)
    foot = move([(-8, 26), (8, 26)], cx, cy, deg, fx, fy)
    d = move([(-18, 14)], cx, cy, deg, fx, fy)[0]
    return (line(pole[0][0], pole[0][1], pole[1][0], pole[1][1]) + poly(tri) +
            line(foot[0][0], foot[0][1], foot[1][0], foot[1][1]) + dot(d[0], d[1]))
def four_options(row_y, draws, size=80, gap=125, x0=25):
    b = ""
    for i, fn in enumerate(draws):
        x = x0 + i * gap
        b += rect(x, row_y, size, size) + fn(x + size / 2, row_y + size / 2) + lab(x + size / 2, row_y + size + 16, "(%d)" % (i + 1))
    return b
b = lab(150, 55, "(X)") + rect(190, 15, 80, 80) + flag_shape(230, 55) + line(290, 10, 290, 100, True, BLUE) + tx(300, 55, "M", 11, "start", BLUE)
b += line(10, 115, 510, 115, True)
b += four_options(135, [lambda x, y: flag_shape(x, y, 1, -1), lambda x, y: flag_shape(x, y, -1, 1),
                        lambda x, y: flag_shape(x, y, 1, 1, 180), lambda x, y: flag_shape(x, y, -1, 1, 90)])
F37 = svg(520, 240, b)
add("Mirror images", "If a mirror is placed on the line M, which of the answer figures is the right image of the figure (X)?",
    ["1", "2", "3", "4"],
    "A mirror standing on the right swaps left and right but keeps top and bottom. The flag now points to the left, stays at the top, "
    "and the dot moves to the other side of the pole: figure (2). (1) is the water image (top and bottom swapped), (3) is the figure turned half round, (4) is turned and flipped. "
    "Grew from: 2021 Q48 and 2025 Q8, Q39 (mirror image of a figure). Test one part at a time: what is at the top, which way it points.",
    k="fig", a=1, f=F37)

def hook(cx, cy, fx=1, fy=1, deg=0):
    p = move([(-20, -22), (20, -22), (20, 22)], cx, cy, deg, fx, fy)
    q = move([(-20, -2), (2, -2)], cx, cy, deg, fx, fy)
    d = move([(-12, 16)], cx, cy, deg, fx, fy)[0]
    c = move([(8, 10)], cx, cy, deg, fx, fy)[0]
    return poly(p, False) + line(q[0][0], q[0][1], q[1][0], q[1][1]) + dot(d[0], d[1]) + ring(c[0], c[1], 4.5)
b = lab(150, 50, "(X)") + rect(190, 12, 80, 76) + hook(230, 50) + line(175, 100, 285, 100, True, BLUE) + tx(295, 100, "W", 11, "start", BLUE)
b += line(10, 118, 510, 118, True)
b += four_options(135, [lambda x, y: hook(x, y, -1, 1), lambda x, y: hook(x, y, 1, 1, 180),
                        lambda x, y: hook(x, y, 1, -1), lambda x, y: hook(x, y, 1, 1, 90)])
F38 = svg(520, 240, b)
add("Mirror images", "Which answer figure is the water image of the figure (X)? (The water surface is the line W below it.)",
    ["1", "2", "3", "4"],
    "A water image flips the figure top to bottom and keeps left and right. In (X) the long arm is at the top and the vertical arm on the right; "
    "in the water image the long arm goes to the bottom, the vertical arm stays on the right, and the dot moves from the bottom to the top: figure (3). "
    "(1) is the mirror image (left and right swapped), (2) is the figure turned 180°, (4) is turned 90°. "
    "Grew from: 2021 Q47 (water image of a figure). Turned 180° is the common trap: it swaps both left-right and top-bottom.",
    k="fig", a=2, f=F38)

# ---------------------------------------------------------------- Cubes and dice (5)
def iso(cx, cy, s, top, left, right):
    h = s * 0.866
    T, RT, C, LT = (cx, cy - s), (cx + h, cy - s / 2), (cx, cy), (cx - h, cy - s / 2)
    B, RB, LB = (cx, cy + s), (cx + h, cy + s / 2), (cx - h, cy + s / 2)
    b = poly([T, RT, C, LT]) + poly([LT, C, B, LB]) + poly([C, RT, RB, B])
    b += tx(cx, cy - s / 2, top, 16) + tx(cx - h / 2, cy + s / 4, left, 16) + tx(cx + h / 2, cy + s / 4, right, 16)
    return b
# net:      [2]
#       [3] [1] [4] [6]
#           [5]
def net(x, y, s):
    cells = {(1, 0): "2", (0, 1): "3", (1, 1): "1", (2, 1): "4", (3, 1): "6", (1, 2): "5"}
    b = ""
    for (cx, cy), t in cells.items():
        b += rect(x + cx * s, y + cy * s, s, s) + tx(x + cx * s + s / 2, y + cy * s + s / 2, t, 15)
    return b
b = lab(140, 60, "(X)") + net(180, 8, 34)
b += line(10, 118, 510, 118, True)
cubes = [("6", "1", "4"), ("2", "1", "4"), ("2", "5", "3"), ("3", "4", "5")]
for i, (t, l, r) in enumerate(cubes):
    cx = 75 + i * 123
    b += iso(cx, 172, 36, t, l, r) + lab(cx, 228, "(%d)" % (i + 1))
F39 = svg(520, 240, b)
add("Cubes and dice", "The sheet (X) is folded to make a cube. Which of the answer cubes can be formed from it?",
    ["1", "2", "3", "4"],
    "In a cross-shaped net, faces with one face between them in a straight line are opposite: 3 and 4, 1 and 6 (1 and 6 have 4 between them), 2 and 5. "
    "Two opposite faces can never be seen together. (1) shows 6 and 1, (3) shows 2 and 5, (4) shows 3 and 4. Only (2) shows 2, 1 and 4, which all touch: "
    "fold 1 to the front, 2 folds up to the top and 4 to the right. "
    "Grew from: 2018 Q30 = 2021 Q9 (boxes from a sheet, the same words twice).",
    k="fig", a=1, f=F39)
add("Cubes and dice", "A cube is painted red on two opposite faces and blue on the other four faces. It is then cut into 64 equal small cubes. How many small cubes have both red and blue paint on them?",
    ["24", "16", "32", "8"],
    "64 = 4 × 4 × 4, so each face has a 4 × 4 grid. Let the red faces be the top and the bottom. A small cube has both colours if it is on a red face and also on a side face, "
    "that is, on the border of the top or bottom layer. Each 4 × 4 layer has 16 − 4 = 12 border cubes, so 12 + 12 = 24. "
    "Grew from: 2021 Q4, Q5 and 2025 Q21, Q45 (painted cubes, all three years). Standard counts for n: 8 corners (3 faces), 12(n − 2) with 2, 6(n − 2)² with 1, (n − 2)³ with none.")

def paper_sq(x, y, s, holes, dash_v=False, dash_h=False):
    b = rect(x, y, s, s)
    if dash_v: b += line(x + s / 2, y, x + s / 2, y + s, True)
    if dash_h: b += line(x, y + s / 2, x + s, y + s / 2, True)
    for hx, hy in holes: b += ring(x + hx * s / 80, y + hy * s / 80, 4)
    return b
GH = ' stroke="#9a9a9a" stroke-dasharray="3 3"'
b = paper_sq(30, 15, 80, [], dash_v=True) + '<path d="M52 60 q18 -22 36 0" stroke="%s"/>' % BLUE + poly([(82, 54), (88, 60), (80, 62)], False).replace("/>", ' stroke="%s"/>' % BLUE)
b += tx(130, 55, "→", 18)
b += rect(150, 15, 80, 80).replace("/>", GH + "/>") + rect(190, 15, 40, 80) + line(190, 55, 230, 55, True) + '<path d="M210 30 q14 12 0 24" stroke="%s"/>' % BLUE + poly([(206, 50), (210, 54), (214, 49)], False).replace("/>", ' stroke="%s"/>' % BLUE)
b += tx(250, 55, "→", 18)
b += rect(270, 15, 80, 80).replace("/>", GH + "/>") + rect(310, 55, 40, 40) + ring(310 + 12, 55 + 12, 4) + lab(390, 55, "(X)")
b += line(10, 118, 510, 118, True)
opts = [[(12, 12), (68, 12), (12, 68), (68, 68)], [(52, 52), (52, 28)],
        [(52, 52), (52, 28), (28, 52)], [(28, 28), (52, 28), (28, 52), (52, 52)]]
for i, hs in enumerate(opts):
    x = 30 + i * 123
    b += paper_sq(x, 135, 80, hs) + lab(x + 40, 230, "(%d)" % (i + 1))
F41 = svg(520, 240, b)
add("Cubes and dice", "A square sheet of paper is folded in half from left to right, then folded again from top to bottom, and a hole is punched as shown in (X); the grey dotted outline marks the full sheet. How will the paper look when it is opened?",
    ["1", "2", "3", "4"],
    "Two folds make four layers, so one punch makes four holes. Open it step by step: the hole sits near the fold corner, so each unfolding reflects it across a fold line, "
    "and the four holes cluster around the centre of the sheet: figure (4). (1) puts them at the corners (wrong side of the folds), (2) opens only one fold, (3) misses a layer. "
    "Grew from: 2018 Q35 (folded and cut paper). Rule: holes = 2 to the power of the number of folds, mirrored across each fold line.",
    k="fig", a=3, f=F41)

b = iso(110, 70, 42, "1", "2", "3") + lab(110, 138, "Position I") + iso(330, 70, 42, "1", "4", "2") + lab(330, 138, "Position II")
F42 = svg(440, 150, b)
add("Cubes and dice", "Two positions of the same die are shown. Which number is on the face opposite 3?",
    ["4", "5", "6", "2"],
    "In both positions 1 is on top. From I to II the die has turned about the vertical axis: 2 moved from the front to the right, so the face that comes to the front (4) was on the left in Position I. "
    "In Position I the left face (4) is opposite the right face (3). So 4 is opposite 3. "
    "Grew from: 2021 Q40 and 2025 Q9, Q37 (positions of a die). Shortcut: when one face is common in the same place, the faces that take each other's place are opposite.",
    k="fig", a=0, f=F42)
add("Cubes and dice", "What is the minimum number of colours needed to paint a square pyramid (a square base and four triangular faces) so that no two faces sharing an edge have the same colour?",
    ["3", "2", "4", "5"],
    "The base touches all four triangles, so it needs its own colour. The four triangles go round in a ring of four: opposite triangles do not share an edge, so two colours are enough for them (red, blue, red, blue). "
    "Total 1 + 2 = 3. "
    "Grew from: 2025 Q38 (minimum colours for a cube: 3, opposite faces share a colour). Rule: a ring of an even number of faces needs 2 colours, an odd ring needs 3.")

# ---------------------------------------------------------------- Grouping identical figures (6)
A, B_, C1, C2 = (80, 12), (10, 132), (57, 132), (103, 132)
D_ = (150, 132)
yl = 82; t = (yl - 12) / 120
b = poly([A, B_, D_]) + line(*A, *C1) + line(*A, *C2) + line(80 - 70 * t, yl, 80 + 70 * t, yl)
F44 = svg(160, 145, b)
add("Grouping identical figures", "How many triangles are there in the figure?",
    ["10", "12", "14", "15"],
    "Count by bases. With the base on the bottom line there are 3 small, 2 double and 1 whole triangle = 6 (for 3 parts: 3 + 2 + 1). "
    "The cross line cuts the same three lines from the top, so it makes another 6 triangles with the apex. Total 12. "
    "Grew from: 2021 Q8 (number of triangles). Rule: lines from one apex to a base cut in n parts make n(n + 1)/2 triangles; each cross line adds that many again.",
    k="fig", a=1, f=F44)

def ngon(cx, cy, r, n, rot0=-90, sx=1, sy=1):
    return poly([(round(cx + sx * r * math.cos(math.radians(rot0 + 360 * i / n)), 1),
                  round(cy + sy * r * math.sin(math.radians(rot0 + 360 * i / n)), 1)) for i in range(n)])
def nine(draws, title_y=0):
    b = ""
    for i, fn in enumerate(draws):
        x = 15 + (i % 9) * 56; y = 14
        b += fn(x + 26, y + 34) + lab(x + 26, y + 76, str(i + 1))
    return svg(520, 104, b)
G45 = [
    lambda x, y: poly([(x - 20, y + 18), (x + 18, y + 18), (x - 6, y - 20)]),                 # 1 triangle
    lambda x, y: poly([(x - 20, y - 16), (x + 20, y - 16), (x + 12, y + 18), (x - 12, y + 18)]),  # 2 quad (trapezium)
    lambda x, y: ngon(x, y, 22, 5),                                                           # 3 pentagon
    lambda x, y: poly([(x, y - 22), (x + 16, y), (x, y + 22), (x - 16, y)]),                  # 4 quad (rhombus)
    lambda x, y: poly([(x - 18, y + 18), (x - 18, y - 4), (x, y - 20), (x + 18, y - 4), (x + 18, y + 18)]),  # 5 pentagon (house)
    lambda x, y: poly([(x - 20, y - 18), (x + 20, y - 18), (x - 20, y + 18)]),                # 6 triangle (right)
    lambda x, y: poly([(x - 22, y), (x - 6, y - 20), (x + 20, y - 10), (x + 14, y + 18), (x - 12, y + 16)]),  # 7 pentagon (irregular)
    lambda x, y: ngon(x, y, 22, 3, 90),                                                       # 8 triangle (pointing down)
    lambda x, y: poly([(x - 18, y - 18), (x + 18, y - 18), (x + 18, y + 18), (x - 18, y + 18)]),  # 9 quad (square)
]
add("Grouping identical figures", "Group the nine figures into three classes on the basis of identical properties.",
    ["1, 6, 8; 2, 4, 9; 3, 5, 7", "1, 6, 9; 2, 4, 8; 3, 5, 7", "1, 5, 8; 2, 4, 9; 3, 6, 7", "1, 4, 8; 2, 6, 9; 3, 5, 7"],
    "Count the sides, not the look. Three sides: 1, 6, 8 (a slanted, a right-angled and an upside-down triangle). Four sides: 2, 4, 9 (trapezium, rhombus, square). "
    "Five sides: 3, 5, 7 (regular, house-shaped and irregular pentagons). "
    "Grew from: 2025 Q11, Q22, Q23, Q46 (five grouping questions in 2025). First test sides, then lines inside, then open or closed, then dots.",
    k="fig", a=0, f=nine(G45))

b = ring(80, 80, 66) + ring(80, 80, 24)
for deg in (-90, 30, 150):
    p1 = rot((0, -24), deg + 90); p2 = rot((0, -66), deg + 90)
    b += line(80 + p1[0], 80 + p1[1], 80 + p2[0], 80 + p2[1])
F46 = svg(160, 160, b)
add("Grouping identical figures", "What is the minimum number of colours needed to paint the figure so that no two regions sharing a boundary have the same colour?",
    ["3", "4", "5", "6"],
    "The ring is cut into three pieces. Each of the three touches the other two, so they need three different colours. "
    "The small circle in the middle touches all three, so it needs a fourth colour. Answer 4. "
    "Grew from: 2021 Q27 (concentric circles cut by lines). Rule: a ring cut into an even number of pieces needs 2 colours, an odd number needs 3; a centre touching all adds one.",
    k="fig", a=1, f=F46)

b = ""
x0, y0, cw, ch = 20, 12, 60, 45
for i in range(4): b += line(x0 + i * cw, y0, x0 + i * cw, y0 + 2 * ch)
for j in range(3): b += line(x0, y0 + j * ch, x0 + 3 * cw, y0 + j * ch)
F47 = svg(220, 115, b)
add("Grouping identical figures", "How many rectangles (squares included) are there in the figure?",
    ["12", "15", "16", "18"],
    "A rectangle needs two vertical lines and two horizontal lines. The figure has 4 vertical and 3 horizontal lines. "
    "Ways = (4 × 3 ÷ 2) × (3 × 2 ÷ 2) = 6 × 3 = 18. "
    "Grew from: 2021 Q49 (rectangles in a diagram) and 2021 Q26 (rhombuses). Rule for a grid of m columns and n rows: C(m+1, 2) × C(n+1, 2).",
    k="fig", a=3, f=F47)

def dots_in(fig, n, cx, cy):
    s = fig
    for i in range(n): s += dot(cx - (n - 1) * 5 + i * 10, cy, 2.6)
    return s
G48 = [
    lambda x, y: dots_in(ring(x, y, 21), 2, x, y),
    lambda x, y: dots_in(poly([(x - 18, y - 18), (x + 18, y - 18), (x + 18, y + 18), (x - 18, y + 18)]), 1, x, y),
    lambda x, y: dots_in(ngon(x, y, 22, 3, -90), 3, x, y + 6),
    lambda x, y: dots_in(ngon(x, y, 22, 6, 0), 3, x, y),
    lambda x, y: dots_in(poly([(x, y - 22), (x + 16, y), (x, y + 22), (x - 16, y)]), 1, x, y),
    lambda x, y: dots_in(ngon(x, y, 22, 5), 2, x, y + 2),
    lambda x, y: dots_in('<ellipse cx="%g" cy="%g" rx="23" ry="14"/>' % (x, y), 1, x, y),
    lambda x, y: dots_in(poly([(x - 22, y - 14), (x + 22, y - 14), (x + 22, y + 14), (x - 22, y + 14)]), 3, x, y),
    lambda x, y: dots_in(poly([(x - 12, y - 16), (x + 12, y - 16), (x + 22, y + 16), (x - 22, y + 16)]), 2, x, y + 2),
]
add("Grouping identical figures", "Divide the nine figures into three groups of three, each group sharing one common property.",
    ["2, 5, 7; 1, 6, 9; 3, 4, 8", "2, 5, 7; 1, 4, 9; 3, 6, 8", "2, 5, 9; 1, 6, 7; 3, 4, 8", "1, 5, 7; 2, 6, 9; 3, 4, 8"],
    "The outlines are all different, so the class must come from inside: the number of dots. One dot: 2, 5, 7. Two dots: 1, 6, 9. Three dots: 3, 4, 8. "
    "Grew from: 2025 Q11, Q22, Q23, Q46 (grouping). When the shapes cannot be split into three equal sets, look at what is inside them.",
    k="fig", a=0, f=nine(G48))

S0 = 120
b = rect(20, 12, S0, S0) + line(20, 12, 140, 132) + line(140, 12, 20, 132) + line(80, 12, 80, 132) + line(20, 72, 140, 72)
F49 = svg(160, 145, b)
add("Grouping identical figures", "A square is drawn with both its diagonals and both lines joining the midpoints of opposite sides. How many triangles are there in the figure?",
    ["16", "18", "20", "24"],
    "Small triangles round the centre: 8. Two small ones together make a triangle on each side of the square (centre and two corners): 4. "
    "Four small ones make a half of the square cut by a diagonal: 4. Total 8 + 4 + 4 = 16. "
    "Grew from: 2021 Q8 (triangles in a figure). Count by size, smallest first, and write the count for each size.",
    k="fig", a=0, f=F49)

# ---------------------------------------------------------------- Embedded figures (1)
def sq_with(x, y, lines):
    b = rect(x, y, 80, 80)
    for (x1, y1, x2, y2) in lines: b += line(x + x1, y + y1, x + x2, y + y2)
    return b
b = lab(160, 52, "(X)") + poly([(200, 30), (200, 70), (230, 70)])
b += line(10, 100, 510, 100, True)
emb = [[(80, 40, 50, 80), (50, 80, 0, 0)], [(0, 40, 40, 80), (40, 80, 80, 0)],
       [(0, 40, 30, 0), (30, 0, 80, 80)], [(0, 40, 30, 80), (30, 80, 80, 0)]]
for i, ls in enumerate(emb):
    x = 25 + i * 125
    b += sq_with(x, 118, ls) + lab(x + 40, 214, "(%d)" % (i + 1))
F50 = svg(520, 228, b)
add("Embedded figures", "Which answer figure contains the figure (X) as its part (same size, same way up)?",
    ["1", "2", "3", "4"],
    "(X) is a right triangle with the right angle at the bottom left, a vertical side of 40 and a base of 30 (in the drawing's units). "
    "In (4) the line from the middle of the left side to the bottom makes exactly that triangle with the left side and the bottom. "
    "(1) has it flipped (right angle at the bottom right), (2) has a base of 40 (wrong shape), (3) has it turned upside down. "
    "Grew from: 2025 Q12, Q13 (embedded figures, first asked in 2025). Check size, angle and the way it faces.",
    k="fig", a=3, f=F50)
