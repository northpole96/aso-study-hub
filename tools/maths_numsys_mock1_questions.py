# Number System Mock 01 (23 Nov 2026): 50 questions, 45 minutes, on the number-system chapters (7 to 14) of the
# Arithmetic Guide. User asked "make a 50 question number system mock". No question repeats Number System Set 01
# or the guide's worked examples and cards, except six exact past questions (2025 Q56, Q61, Q70, Q84; 2021 Q53, Q54).
# Build: python3 .claude/skills/aso-mock/scripts/build.py tools/maths_numsys_mock1_questions.py  (calc re-checks every answer)
# First option is right. Order is given: types mixed by hand, each past question kept apart from its twin.

META = dict(
    paper="maths",
    title="ASO Number System Mock 01",
    hub_title="Number System Mock 01",
    masthead="Numbers M01",
    heading="Paper II (B) · Arithmetic · Number system mock",
    tagline="50 questions on the <b>whole number system</b>,<br>set to the 2018, 2021 and 2025 papers.",
    key="aso-maths-numsys-mock-1",
    code="NUMM1",
    out="ASO-Maths-Number-System-Mock-1.html",
    minutes=45,
    seed=20261124,
    order="given",
    date="23 Nov 2026",
    draw="hand-made from the Arithmetic Guide, chapters 7 to 14 (no draw)",
    topic="ari",
    intro=[
        "This is a full mock on the number system alone: fifty questions in forty-five minutes, the pace of the real "
        "paper. It covers every type in chapters 7 to 14 of the Arithmetic Guide in the weight the papers give them: "
        "divisibility, remainders and successive division, last digits, HCF and LCM in all their word-problem and "
        "remainder forms, fractions, number facts and decimals.",
        "Six questions are real past questions word for word (2025 Q56, Q61, Q70 and Q84; 2021 Q53 and Q54). Every "
        "other question is new and is not in Number System Set 01. Each answer names its type and the guide chapter "
        "that explains it. Press Copy answers at the end and paste the report into the chat for a redo set.",
    ],
)

Q = []
def add(s, q, o, e, k="one", n=False, c=False, a=None, **x):
    d = dict(s=s, q=q, o=o, e=e, k=k, n=n, c=c, a=a); d.update(x); Q.append(d)

A = "Arithmetic"

add(A, "Which of the following numbers is exactly divisible by 36?",
    ["5796", "5786", "6246", "7434"],
    "Type: big divisor, break into co-prime parts (chapter 8). 36 = 4 × 9. 5796: last two digits 96 divide by 4, and the digit sum "
    "5 + 7 + 9 + 6 = 27 divides by 9. Both pass (5796 = 36 × 161). 5786 has digit sum 26; 6246 and 7434 fail the 4 test (46, 34).",
    calc="5796 * (5796 % 36 == 0)")

add(A, "What least number must be added to 7894 so that the sum is exactly divisible by 13?",
    ["10", "3", "13", "7"],
    "Type: least number to add (chapter 9). 13 × 607 = 7891, so 7894 leaves 3. Add 13 − 3 = 10 (7904 = 13 × 608). "
    "Trap: 3 is the number to take away.", calc="13 - 7894 % 13")

add(A, "The H.C.F. of 84, 126 and 210 is:",
    ["42", "21", "14", "84"],
    "Type: HCF by prime factors (chapter 10). 84 = 2² × 3 × 7, 126 = 2 × 3² × 7, 210 = 2 × 3 × 5 × 7. Lowest power of each common prime: "
    "2 × 3 × 7 = 42.", calc="math.gcd(math.gcd(84, 126), 210)")

add(A, "The unit digit of 8⁶³ is:",
    ["2", "8", "4", "6"],
    "Type: last digit of a power (chapter 9). Powers of 8 end in 8, 4, 2, 6. 63 ÷ 4 leaves 3, so take the 3rd: 2.",
    calc="8**63 % 10")

add(A, "The sum of three consecutive odd numbers is 159. The smallest of them is:",
    ["51", "53", "49", "55"],
    "Type: three consecutive numbers (chapter 12). The sum is 3 × the middle one, so the middle is 159 ÷ 3 = 53. "
    "Consecutive odd numbers are 2 apart: 51, 53, 55. Trap: 53 is the middle one.", calc="159 // 3 - 2")

add(A, "Three traffic lights change after every 48 seconds, 72 seconds and 108 seconds. If they change together at 8:20:00 a.m., "
    "they will next change together at:",
    ["8:27:12 a.m.", "8:27:24 a.m.", "8:26:12 a.m.", "8:28:12 a.m."],
    "Type: together again, LCM (chapter 11). 48 = 2⁴ × 3, 72 = 2³ × 3², 108 = 2² × 3³. LCM = 2⁴ × 3³ = 432 seconds = 7 minutes 12 seconds. "
    "8:20:00 + 7 min 12 s = 8:27:12 a.m. Next angle of 2025 Q61.", nocalc=True)

add(A, "0.0025 × 0.04 is equal to:",
    ["1 × 10⁻⁴", "1 × 10⁻³", "1 × 10⁻⁵", "1 × 10⁻⁶"],
    "Type: multiplying decimals (chapter 13). 25 × 4 = 100. Decimal places: 4 + 2 = 6, so 0.000100 = 0.0001 = 1 × 10⁻⁴. "
    "Trap: 10⁻⁶ counts the places but forgets that 100 has two zeros.", nocalc=True)

add(A, "If the number 63x419 is divisible by 11, then the value of x is:",
    ["9", "7", "2", "0"],
    "Type: divisibility by 11 (chapter 8). From the right the digits are 9, 1, 4, x, 3, 6. Odd places: 9 + 4 + 3 = 16. "
    "Even places: 1 + x + 6 = 7 + x. The difference 16 − (7 + x) = 9 − x must be 0 or ±11, so x = 9 (639419 = 11 × 58129).",
    calc="9 * (639419 % 11 == 0)")

add(A, "A number is divided successively by 2, 3 and 5, leaving remainders 1, 2 and 3 respectively. The smallest such number is:",
    ["23", "41", "35", "29"],
    "Type: successive division (chapter 9). Work backwards: 3 × 3 + 2 = 11, then 11 × 2 + 1 = 23. Check: 23 ÷ 2 = 11 r 1; "
    "11 ÷ 3 = 3 r 2; 3 ÷ 5 = 0 r 3. The next answers are 23 + 30 = 53, 83… (30 = 2 × 3 × 5).", calc="(3*3 + 2)*2 + 1")

add(A, "Two numbers are in the ratio 5 : 7 and their L.C.M. is 315. The larger number is:",
    ["63", "45", "105", "35"],
    "Type: numbers from a ratio and the LCM (chapter 11). The numbers are 5x and 7x, and their LCM is 35x = 315, so x = 9. "
    "The numbers are 45 and 63. Larger: 63.", calc="7 * (315 // 35)")

add(A, "What least number must be subtracted from 1672 to obtain a number which is completely divisible by 17?",
    ["6", "7", "8", "4"],
    "Exact past question (2025 Q56). 17 × 98 = 1666, so 1672 leaves 6. Take away the remainder: 6 (chapter 9).",
    calc="1672 % 17", src="2025 Q56")

add(A, "How many three-digit numbers are exactly divisible by 9?",
    ["100", "99", "101", "111"],
    "Type: counting multiples (chapter 9). The first three-digit multiple of 9 is 108, the last is 999. "
    "(999 − 108) ÷ 9 + 1 = 99 + 1 = 100. Trap: 99 forgets the + 1.", calc="(999 - 108) // 9 + 1")

add(A, "The H.C.F. of 4/5, 6/25 and 8/15 is:",
    ["2/75", "2/5", "24/5", "1/75"],
    "Type: HCF of fractions (chapter 11). HCF of the tops 4, 6, 8 = 2. LCM of the bottoms 5, 25, 15 = 75. Answer 2/75. "
    "Trap: 24/5 is the LCM rule (LCM of tops ÷ HCF of bottoms).", calc="2/75")

add(A, "0.2727… (27 recurring) expressed as a fraction in its lowest terms is:",
    ["3/11", "27/100", "27/90", "2/7"],
    "Type: recurring decimal (chapter 13). Both digits repeat, so put them over two 9s: 27/99 = 3/11. "
    "Trap: 27/100 is the plain decimal 0.27.", calc="3/11")

add(A, "The least three-digit number which, when divided by 8, 12 and 16, leaves a remainder of 5 in each case is:",
    ["101", "53", "149", "96"],
    "Type: same remainder every time, LCM + remainder (chapter 11). LCM of 8, 12, 16 = 48. Numbers that leave 5 are 48k + 5: "
    "53, 101, 149… The least three-digit one is 101. Trap: 53 has two digits.", calc="2*48 + 5")

add(A, "A number when divided by 342 leaves a remainder 47. What will be the remainder when the same number is divided by 18?",
    ["11", "47", "29", "5"],
    "Type: reusing a remainder (chapter 9). 342 = 18 × 19, so 18 is a factor of 342. Only the 47 matters: 47 = 18 × 2 + 11. Remainder 11.",
    calc="47 % 18")

add(A, "Four different electronic devices make a beep after every 30 minutes, 1 hour, 1½ hour and 1 hour 45 minutes respectively. "
    "All the devices beeped together at 12 noon. They will again beep together at:",
    ["9 a.m.", "12 mid night", "3 a.m.", "6 a.m."],
    "Exact past question (2025 Q61). In minutes: 30, 60, 90, 105. LCM = 2² × 3² × 5 × 7 = 1260 minutes = 21 hours. "
    "12 noon + 21 hours = 9 a.m. (chapter 11).", nocalc=True, src="2025 Q61")

add(A, "How many factors does 1000 have?",
    ["16", "12", "9", "20"],
    "Type: number of factors (chapter 12). 1000 = 2³ × 5³. Add 1 to each power and multiply: (3 + 1)(3 + 1) = 16.",
    calc="4*4")

add(A, "If the number 57x2 is divisible by 8, the smallest possible value of x is:",
    ["1", "5", "9", "3"],
    "Type: divisibility by 8 (chapter 8). The last three digits 7x2 must divide by 8. 702 ÷ 8 leaves 6; 712 = 8 × 89. So the smallest x is 1. "
    "(752 and 792 also work, so 5 and 9 are possible but not the smallest.)", calc="1 * (712 % 8 == 0)")

add(A, "The product of two numbers is 2160 and their H.C.F. is 12. Their L.C.M. is:",
    ["180", "120", "240", "216"],
    "Type: HCF × LCM = product of two numbers (chapter 10). LCM = 2160 ÷ 12 = 180.", calc="2160 // 12")

add(A, "A room is 8 m 16 cm long and 6 m 72 cm wide. What is the least number of square tiles of equal size needed to cover its floor exactly?",
    ["238", "48", "204", "252"],
    "Type: largest measure, HCF, with a count (chapter 11). In cm: 816 and 672. HCF(816, 672) = 48, so the biggest tile is 48 cm. "
    "Tiles: (816 ÷ 48) × (672 ÷ 48) = 17 × 14 = 238. Trap: 48 is the tile size, not the number of tiles.",
    calc="(816 // math.gcd(816, 672)) * (672 // math.gcd(816, 672))")

add(A, "The value of √0.000441 is:",
    ["0.021", "0.21", "0.0021", "0.00021"],
    "Type: square root of a decimal (chapter 13). 441 = 21². Six decimal places become three: 0.021. Check: 0.021 × 0.021 = 0.000441.",
    calc="0.021")

add(A, "The least number which, when divided by 6, 7, 8, 9 and 10, leaves remainders 4, 5, 6, 7 and 8 respectively is:",
    ["2518", "2520", "2522", "1258"],
    "Type: each remainder the same amount short (chapter 11). Every remainder is 2 less than its divisor, so the answer is LCM − 2. "
    "LCM of 6, 7, 8, 9, 10 = 2520. 2520 − 2 = 2518.", calc="2520 - 2")

add(A, "What is the remainder when 8465 is divided by 11?",
    ["6", "5", "4", "0"],
    "Type: remainder by 11 (chapter 8). From the right the digits are 5, 6, 4, 8. Odd places: 5 + 4 = 9. Even places: 6 + 8 = 14. "
    "9 − 14 = −5; add 11 to get 6. Check: 11 × 769 = 8459, and 8465 − 8459 = 6. Trap: counting from the left gives 5.",
    calc="8465 % 11")

add(A, "The sum of the digits of a two-digit number is 11. The number obtained by reversing its digits is 45 less than the number. The number is:",
    ["83", "38", "74", "92"],
    "Type: two-digit number and its reverse (chapter 12). number − reverse = 9 × (a − b) = 45, so a − b = 5. With a + b = 11: "
    "a = 8, b = 3. The number is 83. Trap: 38 is the reverse.", calc="83")

add(A, "The largest five-digit number exactly divisible by 99 is:",
    ["99990", "99999", "99900", "99891"],
    "Type: largest number with given digits (chapter 9). 99999 = 99 × 1010 + 9. Take away 9: 99990.", calc="99999 - 99999 % 99")

add(A, "If the number 47x234 is divisible by 9, then the value of x is:",
    ["7", "6", "9", "2"],
    "Type: divisibility by 9 (chapter 8). Digit sum 4 + 7 + x + 2 + 3 + 4 = 20 + x. The next multiple of 9 is 27, so x = 7.",
    calc="27 - 20")

add(A, "The greatest number which divides 77, 147 and 252 leaving the same remainder in each case is:",
    ["35", "7", "70", "105"],
    "Type: same remainder, greatest divisor: HCF of the differences (chapter 11). 147 − 77 = 70 and 252 − 147 = 105. "
    "HCF(70, 105) = 35. Each number leaves 7.", calc="math.gcd(147 - 77, 252 - 147)")

add(A, "A number when divided by 6 leaves a remainder 4. What remainder will twice the number leave when divided by 6?",
    ["2", "4", "8", "0"],
    "Type: remainders (chapter 9). The number is 6k + 4, so twice it is 12k + 8. 12k divides by 6, and 8 leaves 2. "
    "Trap: 8 is bigger than the divisor, so it cannot be a remainder.", calc="(2 * 4) % 6")

add(A, "0.333… + 0.666… (both recurring) is equal to:",
    ["1", "0.9", "0.99", "1.01"],
    "Type: adding recurring decimals (chapter 13). 0.333… = 3/9 = 1/3 and 0.666… = 6/9 = 2/3. 1/3 + 2/3 = 1. "
    "Adding the digits gives 0.999…, which is exactly 1.", calc="1")

add(A, "A number was divided successively in order by 4, 5 and 6. The remainders were respectively 2, 3 and 4. The number is:",
    ["214", "476", "954", "1908"],
    "Exact past question (2025 Q70). Check 214: 214 ÷ 4 = 53 r 2; 53 ÷ 5 = 10 r 3; 10 ÷ 6 = 1 r 4. The smallest such number is 94, "
    "and 214 = 94 + 120 (chapter 9).", calc="214", src="2025 Q70")

add(A, "The L.C.M. of 3/4, 5/6 and 7/12 is:",
    ["105/2", "1/12", "105/12", "35/2"],
    "Type: LCM of fractions (chapter 11). LCM of the tops 3, 5, 7 = 105. HCF of the bottoms 4, 6, 12 = 2. Answer 105/2. "
    "Trap: 1/12 is the HCF rule.", calc="105/2")

add(A, "The product of two consecutive natural numbers is 462. Their sum is:",
    ["43", "41", "45", "42"],
    "Type: consecutive numbers (chapter 12). 462 is close to 21² = 441, and 21 × 22 = 462. The sum is 21 + 22 = 43.",
    calc="21 + 22")

add(A, "A number divisible by both 4 and 6 must be divisible by:",
    ["12", "24", "18", "36"],
    "Type: LCM idea (chapters 8 and 10). A number divisible by 4 and by 6 is a multiple of their LCM, which is 12. "
    "Trap: 24 = 4 × 6, but 12 itself divides by 4 and 6 and not by 24. 4 and 6 are not co-prime, so you cannot just multiply them.",
    calc="12")

add(A, "The unit digit of 3⁶⁵ × 6⁵⁹ × 7⁷¹ is:",
    ["4", "6", "2", "8"],
    "Type: last digit of a product of powers (chapter 9). 3⁶⁵: 65 ÷ 4 leaves 1, so 3. 6⁵⁹ always ends in 6. 7⁷¹: 71 ÷ 4 leaves 3, so 3. "
    "3 × 6 × 3 = 54, last digit 4.", calc="(3**65 * 6**59 * 7**71) % 10")

add(A, "The L.C.M. of 24, 36 and 40 is:",
    ["360", "720", "120", "1440"],
    "Type: LCM by prime factors (chapter 10). 24 = 2³ × 3, 36 = 2² × 3², 40 = 2³ × 5. Highest powers: 2³ × 3² × 5 = 360.",
    calc="360 * (360 % 24 == 0 and 360 % 36 == 0 and 360 % 40 == 0)")

add(A, "Three different containers contain 496 litres, 403 litres and 713 litres of mixtures of milk and water respectively. "
    "What biggest measure can measure all the different quantities exactly?",
    ["31 litres", "1 litre", "7 litres", "41 litres"],
    "Exact past question (2025 Q84). 496 = 31 × 16, 403 = 31 × 13, 713 = 31 × 23. The HCF is 31 litres (chapter 11).",
    calc="math.gcd(math.gcd(496, 403), 713)", src="2025 Q84")

add(A, "The least four-digit number which is exactly divisible by each of 15, 25, 40 and 75 is:",
    ["1200", "1000", "1800", "1600"],
    "Type: LCM and the least number with given digits (chapters 9 and 11). LCM of 15, 25, 40, 75 = 600. Its multiples are 600, 1200… "
    "The least four-digit one is 1200. Trap: 1000 is the least four-digit number, but 1000 ÷ 15 is not whole.",
    calc="2 * 600")

add(A, "0.03 × 0.0165 is equal to:",
    ["4.95 × 10⁻⁴", "4.95 × 10⁻³", "4.95 × 10⁻⁵", "4.95 × 10⁻⁶"],
    "Exact past question (2021 Q54). 3 × 165 = 495; decimal places 2 + 4 = 6, so 0.000495 = 4.95 × 10⁻⁴ (chapter 13).",
    nocalc=True, src="2021 Q54")

add(A, "The sum of two numbers is 216 and their H.C.F. is 27. How many such pairs of numbers are there?",
    ["2 pairs", "1 pair", "3 pairs", "4 pairs"],
    "Type: numbers from the HCF (chapter 11). Write the numbers as 27a and 27b, where a and b are co-prime. 27(a + b) = 216, so a + b = 8. "
    "Co-prime pairs adding to 8: (1, 7) and (3, 5). (2, 6) and (4, 4) share a factor. So 2 pairs: 27 and 189, 81 and 135.",
    calc="2")

add(A, "The sum of all two-digit numbers which are exactly divisible by 5 is:",
    ["945", "950", "900", "1045"],
    "Type: adding a run of multiples (chapters 9 and 12). The numbers are 10, 15, …, 95: (95 − 10) ÷ 5 + 1 = 18 of them. "
    "Sum = number of terms × (first + last) ÷ 2 = 18 × 105 ÷ 2 = 945.", calc="18 * (10 + 95) // 2")

add(A, "A number when divided by 5 leaves a remainder 3. What is the remainder when the square of the number is divided by 5?",
    ["4", "3", "9", "1"],
    "Type: remainders (chapter 9). The number is 5k + 3. Its square leaves the same remainder as 3² = 9, and 9 ÷ 5 leaves 4. "
    "Trap: 9 is bigger than the divisor.", calc="(3 * 3) % 5")

add(A, "Four bells toll at intervals of 6, 8, 12 and 18 seconds. They start tolling together. How many times will they toll together in one hour, "
    "including the first time?",
    ["51", "50", "49", "60"],
    "Type: together again, with a count (chapter 11). LCM of 6, 8, 12, 18 = 72 seconds. One hour = 3600 seconds. 3600 ÷ 72 = 50 times "
    "after the start, plus the start = 51.", calc="3600 // 72 + 1")

add(A, "The greatest number which divides 285 and 1249 leaving remainders 9 and 7 respectively is:",
    ["138", "69", "276", "46"],
    "Type: greatest number with given remainders (chapter 11). Take the remainders away: 285 − 9 = 276 and 1249 − 7 = 1242. "
    "HCF(276, 1242) = 138 (276 = 2 × 138, 1242 = 9 × 138).", calc="math.gcd(285 - 9, 1249 - 7)")

add(A, "0.4555… (only the 5 recurring) expressed as a fraction is:",
    ["41/90", "45/99", "41/99", "5/11"],
    "Type: mixed recurring decimal (chapter 13). All the digits once: 45. Take away the part that does not repeat: 45 − 4 = 41. "
    "Underneath: one 9 (one repeating digit) and one 0 (one non-repeating digit) = 90. Answer 41/90.", calc="41/90")

add(A, "The squares of two consecutive natural numbers differ by 35. The larger number is:",
    ["18", "17", "35", "19"],
    "Type: difference of squares (chapter 12). For consecutive numbers the difference of squares equals their sum, so the sum is 35. "
    "Two consecutive numbers adding to 35 are 17 and 18. Larger: 18.", calc="(35 + 1) // 2")

add(A, "What is the smallest digit x for which the number 63x4 is divisible by 12?",
    ["2", "0", "5", "8"],
    "Type: big divisor, co-prime parts (chapter 8). 12 = 3 × 4. The 4 test: x4 must divide by 4, so x is even (04, 24, 44, 64, 84). "
    "The 3 test: digit sum 13 + x must divide by 3, so x is 2, 5 or 8. Even and in the list: 2 (6324 = 12 × 527). "
    "Trap: 0 passes the 4 test but not the 3 test.", calc="2 * (6324 % 12 == 0)")

add(A, "What is the H.C.F. of 1/5, 2/7 and 3/11?",
    ["1/385", "6", "1/35", "5/77"],
    "Exact past question (2021 Q53). HCF of the tops 1, 2, 3 = 1; LCM of the bottoms 5, 7, 11 = 385. Answer 1/385 (chapter 11).",
    calc="1/385", src="2021 Q53")

add(A, "How many numbers from 1 to 200 are exactly divisible by both 4 and 6?",
    ["16", "33", "50", "17"],
    "Type: counting multiples of the LCM (chapters 9 and 10). Divisible by both 4 and 6 means divisible by their LCM, 12. "
    "200 ÷ 12 = 16 (remainder 8), so 16 numbers. Trap: 33 counts multiples of 6 only; 50 counts multiples of 4 only.",
    calc="200 // 12")

add(A, "The value of (0.008 × 0.15) ÷ 0.0004 is:",
    ["3", "0.3", "30", "0.03"],
    "Type: decimals (chapter 13). 0.008 × 0.15 = 0.0012 (8 × 15 = 120, five places). 0.0012 ÷ 0.0004 = 12 ÷ 4 = 3 "
    "(both have four decimal places, so they cancel).", calc="3")
