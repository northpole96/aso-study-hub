# Number Series set 01 (22 Nov 2026): a 30-question practice set for the Number Series Guide.
# Every pattern of the guide (gaps, gaps of gaps, alternating signs, two series mixed, multiplying,
# powers, two before, letters, positions and counting) with its twists, mostly in the wrong-term style
# that the 2021 and 2025 papers use. Three past questions word for word. Order is given (patterns mixed by hand).
# Build: python3 .claude/skills/aso-mock/scripts/build.py tools/reasoning_series1_questions.py
# First option is right.

META = dict(
    paper="reasoning",
    title="ASO Number Series Set 01",
    hub_title="Number Series Set 01",
    masthead="Series 01",
    heading="Paper II (A) · Reasoning · Number and alphabet series",
    tagline="30 questions on <b>every series pattern</b><br>and its twists, set to the 2018, 2021 and 2025 papers.",
    key="aso-reasoning-series-1",
    code="SER1",
    out="ASO-Reasoning-Series-1.html",
    minutes=30,
    seed=20261124,
    order="given",
    date="22 Nov 2026",
    draw="hand-made from the Number Series Guide chapters (no draw)",
    topic="rser",
    intro=[
        "This set goes with the Number Series Guide. It has thirty questions, one minute each, and it covers every "
        "pattern in the guide: gaps and gaps of gaps, alternating signs, two series mixed, multiplying, squares and "
        "cubes, the two terms before, letter series, and the 2018-style position and counting questions. The patterns "
        "are mixed, so the first job in every question is to run the checking order and spot the type.",
        "Half the questions ask for the wrong term, because that is what the 2021 and 2025 papers ask most. Three are "
        "real past questions word for word (2025 Q49, 2025 Q1 and 2018 Q15). 2025 Q49 has no official key, so its "
        "answer carries CHECK. Press Copy answers at the end and paste the report into the chat for a redo set.",
    ],
)

Q = []
def add(s, q, o, e, k="one", n=False, c=False, a=None, **x):
    d = dict(s=s, q=q, o=o, e=e, k=k, n=n, c=c, a=a); d.update(x); Q.append(d)

S = "Number series"
W = "One term in the following number series is wrong. Find out the wrong term.\n"

add(S, W + "11, 14, 20, 29, 41, 57",
    ["57", "41", "29", "20"],
    "Gaps: 3, 6, 9, 12, 16. They are multiples of 3, so the last gap should be 15 and the last term 41 + 15 = 56. "
    "Only the last gap misfits, so the last term is wrong. Pattern: check 1, gaps growing by a fixed step, like 2021 Q32.")

add(S, "Find the missing term: 3, 4, 9, 8, 27, 12, ?",
    ["81", "16", "54", "36"],
    "The numbers go up and down, so split them. Odd places: 3, 9, 27, multiplying by 3, so the blank (7th place, odd) is 81. "
    "Even places: 4, 8, 12, adding 4. Trap: 16 is the next even-place term. Pattern: check 3, two series mixed, like 2025 Q15.")

add(S, W + "40, 44, 38, 46, 36, 48, 33",
    ["33", "48", "38", "46"],
    "Gaps: +4, −6, +8, −10, +12, −15. The signs alternate and the sizes grow by 2, so the last gap should be −14 "
    "and the last term 48 − 14 = 34. Pattern: check 2, alternating signs, like 2025 Q48.")

add(S, "Find the missing letter: D, H, M, S, ?",
    ["Z", "Y", "X", "W"],
    "As numbers: D = 4, H = 8, M = 13, S = 19. Gaps: 4, 5, 6, so the next gap is 7 and 19 + 7 = 26 = Z. "
    "Pattern: check 7, letters with a growing skip, the next angle of 2025 Q1.")

add(S, "Find the missing term: 3, 8, 18, 38, 78, ?",
    ["158", "156", "160", "118"],
    "Each term is double the one before, plus 2: 3 × 2 + 2 = 8, 8 × 2 + 2 = 18, and 78 × 2 + 2 = 158. "
    "The gaps 5, 10, 20, 40 double too, which is another way to see it (next gap 80). Pattern: check 4, multiply then add.")

add(S, W + "1, 3, 12, 25, 48", ["25", "3", "12", "48"],
    "Exact past question (2021 Q30 and 2025 Q49, word for word). No official key has been published. The best rule: "
    "3, 12, 27, 48 are 3 × 1², 3 × 2², 3 × 3², 3 × 4², so 25 should be 27 and 25 is wrong. The quick sign is that "
    "25 is the only option that is not a multiple of 3. Another reading (×2 + 1 and ×3 + 3 in turn) would make 48 "
    "wrong, which is why this answer carries CHECK.", c=True, src="2025 Q49")

add(S, "Find the missing term: 1, 2, 2, 4, 8, 32, ?",
    ["256", "64", "128", "40"],
    "Each term is the product of the two before it: 1 × 2 = 2, 2 × 2 = 4, 2 × 4 = 8, 4 × 8 = 32, so the next is "
    "8 × 32 = 256. Trap: 64 (doubling 32) fits only the look of the end. Pattern: check 6, like 2025 Q50.")

add(S, W + "2, 9, 28, 65, 125, 217",
    ["125", "65", "217", "28"],
    "These are n³ + 1: 1 + 1 = 2, 8 + 1 = 9, 27 + 1 = 28, 64 + 1 = 65, 125 + 1 = 126, 216 + 1 = 217. "
    "So 125 should be 126. The trap: 125 looks right because it is a perfect cube, but every other term is a cube plus one. "
    "Pattern: check 5, near-cubes.")

add(S, "Find the missing term: 1, 4, 10, 20, 35, ?",
    ["56", "54", "50", "55"],
    "First gaps: 3, 6, 10, 15. Second gaps: 3, 4, 5. The next second gap is 6, so the next first gap is 21 and the "
    "next term is 35 + 21 = 56. Pattern: check 1, gaps of the gaps.")

add(S, "Find the missing letter pair: BY, DW, FU, ?",
    ["HS", "GT", "HT", "IS"],
    "First letters B, D, F skip one: next H. Second letters are their opposites (B–Y, D–W, F–U add to 27), "
    "so the opposite of H (8) is 27 − 8 = 19 = S. Trap: GT is the opposite pair of G, not H. Pattern: letter pairs.")

add(S, "Find the missing term: 5040, 720, 120, 24, ?, 2",
    ["6", "8", "4", "12"],
    "Divide by 7, 6, 5, 4, 3, 2 in turn: 5040 ÷ 7 = 720, 720 ÷ 6 = 120, 120 ÷ 5 = 24, 24 ÷ 4 = 6, 6 ÷ 3 = 2. "
    "Pattern: check 4, a falling multiplier (these are 7!, 6!, 5!, 4!, 3!, 2!).")

add(S, W + "2, 3, 5, 8, 13, 22, 34",
    ["22", "13", "34", "8"],
    "Each term is the sum of the two before it: 2 + 3 = 5, 3 + 5 = 8, 5 + 8 = 13, 8 + 13 = 21. So 22 is wrong, and "
    "13 + 21 = 34 confirms it. Here the wrong term is not at the end, so its next term (34) fits only the corrected "
    "value. Pattern: check 6.")

add(S, "Find the missing term: 2, 6, 3, 9, 6, 18, ?",
    ["15", "54", "12", "21"],
    "Two steps take turns: ×3, −3, ×3, −3, ×3, so the next step is −3: 18 − 3 = 15. "
    "Trap: 54 continues ×3 and ignores the turn-taking. Pattern: two operations in turn.")

add(S, "In the English alphabet, which letter is 4th to the left of the 10th letter from the right?",
    ["M", "N", "L", "U"],
    "10th from the right = 27 − 10 = 17 = Q. 4th to the left means minus 4: 13 = M. Work from the end of the sentence "
    "backwards; left = subtract, right = add. Trap: U (17 + 4) goes the wrong way. Family: 2018 Q6.")

add(S, W + "4, 9, 25, 49, 121, 168",
    ["168", "121", "49", "25"],
    "These are the squares of the primes: 2², 3², 5², 7², 11², 13². 13² = 169, so 168 is wrong. "
    "Sign: a square never ends in 8. Pattern: check 5, and check 1's prime list.")

add(S, "Find the missing term: 3, 2, 2, 3, 8, ?",
    ["35", "40", "30", "32"],
    "Multiply by 1, 2, 3, 4, 5 and subtract the same number: 3 × 1 − 1 = 2, 2 × 2 − 2 = 2, 2 × 3 − 3 = 3, "
    "3 × 4 − 4 = 8, so 8 × 5 − 5 = 35. Trap: 40 forgets the − 5. This is the minus twin of the ×n + n type.")

add(S, "Choose the most appropriate option to complete the following series.\nV, R, N, _, F, B",
    ["J", "K", "H", "P"],
    "Exact past question (2025 Q1). V = 22, R = 18, N = 14, F = 6, B = 2: the series falls by 4, so the blank is "
    "14 − 4 = 10 = J. The options K and H are one step either side of the trap of miscounting.", src="2025 Q1")

add(S, W + "3, 4, 6, 10, 18, 34, 68",
    ["68", "34", "18", "10"],
    "Gaps: 1, 2, 4, 8, 16, 34. They double, so the last gap should be 32 and the last term 34 + 32 = 66. "
    "Trap: 68 looks like doubling 34. Pattern: check 1, doubling gaps.")

add(S, "Find the missing term: 3, 6, 11, 18, 27, ?",
    ["38", "36", "37", "40"],
    "These are n² + 2: 1 + 2, 4 + 2, 9 + 2, 16 + 2, 25 + 2, and 36 + 2 = 38. The gaps 3, 5, 7, 9 (next 11) give the same "
    "answer. Two ways to see a series is normal; use whichever you see first.")

add(S, "How many 8s in the following string are immediately preceded by 3 or 5?\n3 8 5 8 1 8 3 8 6 8 5 8",
    ["4", "3", "5", "6"],
    "Underline every 8 and look one step left. The 8s are preceded by 3, 5, 1, 3, 6 and 5. Four of them (3, 5, 3, 5) "
    "count. 'Immediately preceded' means the digit just before. Family: 2018 Q3.")

add(S, W + "1, 1, 2, 6, 24, 100, 720",
    ["100", "24", "720", "6"],
    "Multiply by 1, 2, 3, 4, 5, 6: 1, 1, 2, 6, 24, 120, 720. So 100 should be 120. Two gaps around 100 are spoiled "
    "(×4.17 and ×7.2), and the right value 120 fixes both. Pattern: check 4, growing multiplier.")

add(S, "Find the missing term: B3, E9, H27, ?",
    ["K81", "J81", "K54", "L81"],
    "Letters: B, E, H skip two each time (2, 5, 8), so the next is 11 = K. Numbers: 3, 9, 27 multiply by 3, so 81. "
    "Answer K81. Pattern: letters and numbers together; solve each part on its own.")

add(S, "Find the missing term: 1, 2, 3, 10, ?, 9802",
    ["99", "199", "101", "999"],
    "Exact past question (2018 Q15; option C is unreadable in the scan and was rebuilt). Square each term and add or "
    "subtract 1 in turn: 1² + 1 = 2, 2² − 1 = 3, 3² + 1 = 10, 10² − 1 = 99, 99² + 1 = 9802. "
    "Trap: 101 uses + 1 every time.", src="2018 Q15")

add(S, W + "2, 10, 4, 20, 8, 30, 16, 41",
    ["41", "30", "16", "20"],
    "Split the series. Odd places: 2, 4, 8, 16, doubling. Even places: 10, 20, 30, then 40, adding 10. "
    "So 41 is wrong. Pattern: check 3 in the wrong-term style.")

add(S, "Find the missing term: 64, 96, 144, 216, ?",
    ["324", "288", "432", "300"],
    "Each term is 1.5 times the one before: 64 × 1.5 = 96, 96 × 1.5 = 144, 144 × 1.5 = 216, 216 × 1.5 = 324. "
    "Ratios can be fractions; divide the second term by the first to find it. Pattern: check 4.")

add(S, "In the word PRACTICE, the first four letters are written in reverse order, and so are the last four. "
    "Which letter is now 6th from the left?",
    ["C", "I", "E", "T"],
    "PRAC becomes CARP and TICE becomes ECIT, so the new word is CARPECIT. The 6th letter from the left is C. "
    "Write the new word down before you count. Family: 2018 Q25 and 2018 Q50.")

add(S, W + "10, 12, 15, 20, 27, 39, 51",
    ["39", "27", "51", "20"],
    "Gaps: 2, 3, 5, 7, 12, 12. Primes: 2, 3, 5, 7, 11, 13. Two gaps side by side are spoiled (12 and 12), "
    "and the term between them, 39, is wrong. It should be 27 + 11 = 38, and then 38 + 13 = 51 fits. "
    "Pattern: one wrong term spoils two neighbouring gaps.")

add(S, "Find the missing term: 7, 26, 63, 124, ?",
    ["215", "216", "217", "210"],
    "These are n³ − 1: 8 − 1, 27 − 1, 64 − 1, 125 − 1, and 6³ − 1 = 215. Trap: 216 is the cube itself, and 217 is "
    "n³ + 1. Pattern: check 5, near-cubes.")

add(S, W + "Z, X, U, R, L, F".replace("number series", "letter series"),
    ["R", "U", "L", "F"],
    "As numbers: Z = 26, X = 24, U = 21, R = 18, L = 12, F = 6. The gaps should be 2, 3, 4, 5, 6: 26, 24, 21, 17, 12, 6. "
    "So R (18) should be Q (17). Both gaps around R (3 and 6) are spoiled, which points to it. Pattern: letters, wrong term.")

add(S, "Find the missing term: 2, 3, 4, 9, 16, 29, ?",
    ["54", "45", "58", "52"],
    "Each term is the sum of the three before it: 2 + 3 + 4 = 9, 3 + 4 + 9 = 16, 4 + 9 + 16 = 29, so the next is "
    "9 + 16 + 29 = 54. Trap: 45 adds only the last two (16 + 29). Pattern: check 6.")
