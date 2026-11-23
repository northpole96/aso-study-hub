# Number Series set 02 (22 Nov 2026): 30 more questions for the Number Series Guide (user asked "30 more questions").
# No repeats of Set 02, the guide's worked examples or Reasoning Mock 01.
# Every pattern of the guide (gaps, gaps of gaps, alternating signs, two series mixed, multiplying,
# powers, two before, letters, positions and counting) with its twists, mostly in the wrong-term style
# that the 2021 and 2025 papers use. Two past questions word for word (2021 Q31, 2018 Q14). Order is given (patterns mixed by hand).
# Build: python3 .claude/skills/aso-mock/scripts/build.py tools/reasoning_series2_questions.py
# First option is right.

META = dict(
    paper="reasoning",
    title="ASO Number Series Set 02",
    hub_title="Number Series Set 02",
    masthead="Series 02",
    heading="Paper II (A) · Reasoning · Number and alphabet series",
    tagline="30 questions on <b>every series pattern</b><br>and its twists, set to the 2018, 2021 and 2025 papers.",
    key="aso-reasoning-series-2",
    code="SER2",
    out="ASO-Reasoning-Series-2.html",
    minutes=30,
    seed=20261125,
    order="given",
    date="22 Nov 2026",
    draw="hand-made from the Number Series Guide chapters (no draw)",
    topic="rser",
    intro=[
        "Thirty more questions for the Number Series Guide, all new: none repeats Set 01, the guide's worked examples "
        "or Reasoning Mock 01. Every pattern comes again with a new twist: digit reversal, products of primes, "
        "alphabetical order, fractions, falling gaps of gaps and letter-number pairs.",
        "A third of the questions ask for the wrong term. Two are real past questions word for word (2021 Q31 and "
        "2018 Q14). Press Copy answers at the end and paste the report into the chat for a redo set.",
    ],
)

Q = []
def add(s, q, o, e, k="one", n=False, c=False, a=None, **x):
    d = dict(s=s, q=q, o=o, e=e, k=k, n=n, c=c, a=a); d.update(x); Q.append(d)

S = "Number series"
W = "One term in the following number series is wrong. Find out the wrong term.\n"

add(S, W + "5, 7, 12, 19, 31, 51, 81",
    ["51", "31", "81", "19"],
    "Each term is the sum of the two before it: 5 + 7 = 12, 7 + 12 = 19, 12 + 19 = 31, 19 + 31 = 50. So 51 is wrong, "
    "and 31 + 50 = 81 confirms it. Pattern: check 6 in the wrong-term style.")

add(S, "Find the missing term: 6, 11, 21, 41, 81, ?",
    ["161", "162", "121", "160"],
    "Double and subtract 1: 6 × 2 − 1 = 11, 11 × 2 − 1 = 21, and 81 × 2 − 1 = 161. The gaps 5, 10, 20, 40 double too "
    "(next 80). Trap: 162 forgets the − 1. Pattern: check 4, multiply then add.")

add(S, "Find the missing letter: A, C, F, J, O, ?",
    ["U", "T", "V", "S"],
    "As numbers: 1, 3, 6, 10, 15. Gaps 2, 3, 4, 5, so the next gap is 6: 15 + 6 = 21 = U. "
    "Anchor: O = 15 (EJOTY), so U is six after it. Pattern: check 7, growing skip.")

add(S, W + "1, 9, 25, 49, 81, 120",
    ["120", "81", "49", "25"],
    "These are the squares of the odd numbers: 1², 3², 5², 7², 9², 11² = 121. So 120 is wrong. "
    "Quick sign: an odd number squared is odd, and 120 is even. Pattern: check 5.")

add(S, "Find the missing term: 1, 10, 3, 9, 5, 8, 7, ?",
    ["7", "9", "6", "11"],
    "The blank is in the 8th place, an even place. Even places: 10, 9, 8, so the next is 7. Odd places: 1, 3, 5, 7. "
    "Trap: 9 continues the odd-place series. Pattern: check 3, two series mixed.")

add(S, "Find the missing term: 2, 10, 30, 68, 130, ?",
    ["222", "216", "210", "220"],
    "These are n³ + n: 1 + 1, 8 + 2, 27 + 3, 64 + 4, 125 + 5, and 216 + 6 = 222. "
    "Trap: 216 (the cube alone) and 210 (n³ − n). Pattern: check 5.")

add(S, W + "64, 32, 96, 48, 144, 72, 210",
    ["210", "144", "96", "72"],
    "Two steps take turns: ÷2, ×3, ÷2, ×3, ÷2, ×3. So the last term should be 72 × 3 = 216, and 210 is wrong. "
    "Pattern: two operations in turn, wrong-term style.")

add(S, "Find the missing term: 2, 12, 36, 80, 150, ?",
    ["252", "216", "240", "256"],
    "These are n³ + n² = n²(n + 1): 1 × 2, 4 × 3, 9 × 4, 16 × 5, 25 × 6, and 36 × 7 = 252. "
    "This is the twin of 2018 Q13 (n³ − n²). Pattern: check 5.")

add(S, "Find the missing term: Z1, X3, V5, ?",
    ["T7", "U7", "T6", "S7"],
    "Letters go back by 2: Z, X, V, T. Numbers go up by 2: 1, 3, 5, 7. Answer T7. "
    "Solve the letter part and the number part separately.")

add(S, W + "2, 4, 8, 14, 22, 32, 45",
    ["45", "32", "22", "14"],
    "Gaps: 2, 4, 6, 8, 10, 13. They are the even numbers, so the last gap should be 12 and the last term 32 + 12 = 44. "
    "Only the last gap misfits, so the last term is wrong. Pattern: check 1.")

add(S, "Find the missing term: 6, 15, 35, 77, ?",
    ["143", "121", "133", "156"],
    "Each term is the product of two primes in a row: 2 × 3, 3 × 5, 5 × 7, 7 × 11, so the next is 11 × 13 = 143. "
    "Trap: 121 = 11 × 11 repeats a prime. This needs the prime list from the last-week sheet.")

add(S, "In the English alphabet, which letter is exactly midway between the 5th letter from the left and the 8th letter from the right?",
    ["L", "M", "K", "N"],
    "5th from the left = E = 5. 8th from the right = 27 − 8 = 19 = S. Midway = (5 + 19) ÷ 2 = 12 = L. "
    "Family: 2018 Q6, letter positions; kth from the right is 27 − k.")

add(S, "Find the missing term: 1, 2, 6, 30, 210, ?",
    ["2310", "1890", "2100", "2520"],
    "Multiply by the primes in turn: ×2, ×3, ×5, ×7, so the next is ×11: 210 × 11 = 2310. "
    "Trap: 1890 (×9) and 2520 (×12) follow 'growing multipliers' but skip the prime rule.")

add(S, W + "3, 6, 18, 72, 360, 2150",
    ["2150", "360", "72", "18"],
    "Multiply by 2, 3, 4, 5, 6: 3, 6, 18, 72, 360, 2160. So 2150 is wrong. "
    "The examiner keeps the wrong term close to the right one. Pattern: check 4.")

add(S, W + "105, 85, 60, 30, 0, −45, −90",
    ["0", "105", "60", "−45"],
    "Exact past question (2021 Q31). The gaps should be −20, −25, −30, −35, −40, −45, giving 105, 85, 60, 30, −5, −45, −90. "
    "The gaps around 0 (−30 and −45) are both spoiled, so 0 is wrong; it should be −5.", src="2021 Q31")

add(S, "Find the missing term: 1, 8, 9, 64, 25, 216, ?",
    ["49", "343", "36", "81"],
    "The blank is in the 7th place, an odd place. Odd places: 1, 9, 25 are 1², 3², 5², so the next is 7² = 49. "
    "Even places: 8, 64, 216 are 2³, 4³, 6³. Trap: 343 = 7³ uses the wrong half's rule.")

add(S, "In the following string, how many 7s are immediately followed by 5 or 9?\n2 7 5 9 7 2 5 7 9 2 7 5",
    ["3", "2", "4", "5"],
    "Underline every 7 and look one step right. The four 7s are followed by 5, 2, 9 and 5, so three count. "
    "'Immediately followed' means the digit just after. Family: 2018 Q3.")

add(S, "If the letters of the word BRIGHTEN are arranged in alphabetical order, which letter will be 3rd from the right?",
    ["N", "R", "I", "H"],
    "In alphabetical order: B, E, G, H, I, N, R, T. From the right: T, R, N, so the 3rd is N. "
    "Write the new order down before counting. Family: 2018 Q25 and Q50 (rearranged words).")

add(S, "Find the missing letter pair: AB, DE, HI, MN, ?",
    ["ST", "RS", "TU", "SU"],
    "The first letters A, D, H, M are 1, 4, 8, 13: gaps 3, 4, 5, so the next gap is 6 and 19 = S. "
    "Each pair is two letters in a row, so ST. Pattern: letter pairs with a growing skip.")

add(S, "Find the missing term: 1, 5, 13, 29, 61, ?",
    ["125", "121", "123", "127"],
    "Double and add 3: 1 × 2 + 3 = 5, 5 × 2 + 3 = 13, and 61 × 2 + 3 = 125. "
    "The gaps 4, 8, 16, 32 double too, which gives the same answer (next 64). Pattern: check 4.")

add(S, W + "1, 3, 3, 9, 27, 234, 6561",
    ["234", "27", "9", "6561"],
    "Each term is the product of the two before it: 1 × 3 = 3, 3 × 3 = 9, 3 × 9 = 27, 9 × 27 = 243, and 27 × 243 = 6561. "
    "So 234 should be 243: the digits were swapped to make the trap. Pattern: check 6.")

add(S, "Find the missing term: 200, 190, 172, 144, 104, ?",
    ["50", "54", "60", "44"],
    "First gaps: 10, 18, 28, 40. Second gaps: 8, 10, 12, so the next second gap is 14 and the next first gap is 54. "
    "104 − 54 = 50. Trap: 54 is the gap, not the term. Pattern: gaps of the gaps, in a falling series.")

add(S, "5, 5, 19, 7, 41, 9, ?",
    ["71", "61", "79", "69"],
    "Exact past question (2018 Q14; options A and C are garbled in the scan and were rebuilt). Odd places: 5, 19, 41 "
    "with gaps 14, 22, growing by 8, so the next gap is 30 and the answer is 71. Even places: 5, 7, 9. "
    "Pattern: check 3.", src="2018 Q14")

add(S, W + "7, 9, 13, 21, 37, 69, 132",
    ["132", "69", "37", "21"],
    "Gaps: 2, 4, 8, 16, 32, 63. They double, so the last gap should be 64 and the last term 69 + 64 = 133. "
    "Another way: each term is double the one before, minus 5 (9 × 2 − 5 = 13). Pattern: check 1.")

add(S, "Find the missing term: 3, 4.5, 6.75, ?",
    ["10.125", "9", "10.5", "9.75"],
    "Each term is 1.5 times the one before: 3 × 1.5 = 4.5, 4.5 × 1.5 = 6.75, 6.75 × 1.5 = 10.125. "
    "Trap: 9 adds a fixed 2.25; but the gaps (1.5, 2.25) grow, so it is a ratio. Pattern: check 4.")

add(S, "One term in the following letter series is wrong. Find out the wrong term.\nB, E, H, K, M, Q",
    ["M", "K", "Q", "H"],
    "As numbers: 2, 5, 8, 11, 13, 17. The gaps should all be 3: 2, 5, 8, 11, 14, 17. So M (13) should be N (14). "
    "Both gaps around M (2 and 4) are spoiled, which points to it.")

add(S, "Find the missing term: 13, 31, 24, 42, 35, ?",
    ["53", "28", "44", "62"],
    "Two steps take turns: reverse the digits, then subtract 7. 13 → 31, 31 − 7 = 24, 24 → 42, 42 − 7 = 35, "
    "and the next step reverses 35 → 53. Trap: 28 (35 − 7) skips the turn. A new twist: digit reversal.")

add(S, "Find the missing term: 1, 4, 13, 40, 121, ?",
    ["364", "363", "365", "242"],
    "Multiply by 3 and add 1: 1 × 3 + 1 = 4, 4 × 3 + 1 = 13, and 121 × 3 + 1 = 364. "
    "The gaps 3, 9, 27, 81 are powers of 3 (next 243), which gives the same answer.")

add(S, W + "2, 7, 14, 23, 34, 46, 62",
    ["46", "34", "62", "23"],
    "These are n² − 2: 4 − 2, 9 − 2, 16 − 2, 25 − 2, 36 − 2, 49 − 2 = 47, 64 − 2. So 46 is wrong. "
    "The gaps show it too: 5, 7, 9, 11, 12, 16 should be 5, 7, 9, 11, 13, 15.")

add(S, "Find the missing term: 11, 13, 17, 19, 23, 29, ?",
    ["31", "33", "37", "35"],
    "These are the primes in a row from 11. After 29 the next prime is 31. "
    "Trap: 33 (3 × 11) and 35 (5 × 7) are odd but not prime. Know the primes up to 100.")
