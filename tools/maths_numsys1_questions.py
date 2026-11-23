# Number System set 01 (23 Nov 2026): 30 questions for the number-system chapters (7 to 12) of the Arithmetic Guide.
# Divisibility, remainders, successive division, last digits, HCF and LCM (with the remainder and fraction types),
# number facts and decimals, each with a twist. Three past questions word for word (2025 Q71 = 2021 Q93, 2025 Q100, 2018 Q82).
# Build: python3 .claude/skills/aso-mock/scripts/build.py tools/maths_numsys1_questions.py   (calc re-checks every answer)
# First option is right. Order is given: types mixed by hand, each repeat kept apart from its twin.

META = dict(
    paper="maths",
    title="ASO Number System Set 01",
    hub_title="Number System Set 01",
    masthead="Numbers 01",
    heading="Paper II (B) · Arithmetic · Number system",
    tagline="30 questions on <b>divisibility, remainders, HCF, LCM</b><br>and decimals, set to the 2018, 2021 and 2025 papers.",
    key="aso-maths-numsys-1",
    code="NUM1",
    out="ASO-Maths-Number-System-1.html",
    minutes=30,
    seed=20261123,
    order="given",
    date="23 Nov 2026",
    draw="hand-made from the Arithmetic Guide, chapters 7 to 12 (no draw)",
    topic="ari",
    intro=[
        "This set goes with the number-system chapters of the Arithmetic Guide. It has thirty questions, one minute each, "
        "and covers every type in those chapters: divisibility with unknown digits, least number to add or take away, "
        "counting multiples, successive division, last digits of powers, HCF and LCM in all their remainder forms, "
        "fractions, consecutive numbers, two-digit numbers, factors and decimals.",
        "Each type comes with a twist the papers have not used yet, so you cannot answer from memory. Three questions are "
        "real past questions word for word (2025 Q71, which was also 2021 Q93; 2025 Q100; 2018 Q82). Press Copy answers at "
        "the end and paste the report into the chat for a redo set.",
    ],
)

Q = []
def add(s, q, o, e, k="one", n=False, c=False, a=None, **x):
    d = dict(s=s, q=q, o=o, e=e, k=k, n=n, c=c, a=a); d.update(x); Q.append(d)

A = "Arithmetic"

add(A, "What least number must be subtracted from 8961 so that the result is exactly divisible by 23?",
    ["14", "9", "23", "5"],
    "Type: least number to take away. 8961 = 23 × 389 + 14, so take away the remainder, 14 (8947 = 23 × 389). "
    "Trap: 9 is the number to ADD (23 − 14). Grew from 2025 Q56.", calc="8961 % 23")

add(A, "Two numbers are in the ratio 4 : 5 and their L.C.M. is 180. What is the sum of the numbers?",
    ["81", "90", "72", "99"],
    "Type: numbers from a ratio and the LCM. Write them as 4x and 5x. 4 and 5 share no factor, so the LCM is 20x = 180 and x = 9. "
    "The numbers are 36 and 45; their sum is 81. Twin of 2025 Q79, which gave the HCF instead.", calc="4*9 + 5*9")

add(A, "If the number 85x47 is divisible by 11, then the value of x is:",
    ["5", "6", "4", "3"],
    "Type: divisibility by 11. Digits in the odd places (from the left): 8 + x + 7 = 15 + x. Even places: 5 + 4 = 9. "
    "The difference 6 + x must be 0 or a multiple of 11, so x = 5. Check: 85547 = 11 × 7777. The 11 test is the next angle of 2025 Q100.",
    calc="(85547 % 11 == 0) * 5")

add(A, "Three bells toll at intervals of 9, 12 and 15 seconds. They start tolling together. How many times will they toll together in 30 minutes, including the first time?",
    ["11", "10", "12", "9"],
    "Type: together again (LCM), with a count. LCM of 9, 12, 15 = 180 seconds = 3 minutes. In 30 minutes: 30 ÷ 3 = 10 more times, "
    "plus the start = 11. Trap: 10 forgets the first toll. Grew from 2025 Q61 (beeping devices).", calc="30*60 // 180 + 1")

add(A, "A number when divided by 357 leaves a remainder 39. What will be the remainder when the same number is divided by 17?",
    ["5", "39", "22", "3"],
    "Type: reusing a remainder. 357 = 17 × 21, so the number is (a multiple of 17) + 39. 39 ÷ 17 leaves 5. "
    "This only works because 17 is a factor of 357.", calc="39 % 17")

add(A, "How many numbers between 100 and 300 are exactly divisible by 7?",
    ["28", "29", "27", "30"],
    "Type: counting multiples. The first is 105 and the last is 294. Count = (294 − 105) ÷ 7 + 1 = 27 + 1 = 28. "
    "Trap: 27 forgets the + 1. Next angle of 2021 Q82.", calc="(294 - 105) // 7 + 1")

add(A, "What is the sum of two consecutive even numbers, the difference of whose squares is 84?",
    ["42", "34", "38", "46"],
    "Exact past question (2025 Q71, and word for word 2021 Q93). Shortcut: for consecutive even numbers the difference of squares is "
    "twice their sum, so the sum is 84 ÷ 2 = 42 (the numbers are 20 and 22).", calc="84 // 2", src="2025 Q71")

add(A, "The H.C.F. of two numbers is 12 and their L.C.M. is 336. If one number is 48, the other number is:",
    ["84", "96", "72", "112"],
    "Type: HCF × LCM = product of the two numbers. 12 × 336 = 4032, and 4032 ÷ 48 = 84. Check: HCF(48, 84) = 12 and LCM = 336.",
    calc="12*336 // 48")

add(A, "The unit digit of 7⁹⁵ is:",
    ["3", "7", "9", "1"],
    "Type: last digit of a power. Powers of 7 end in 7, 9, 3, 1 and repeat every 4. 95 ÷ 4 leaves 3, so take the 3rd: 3.",
    calc="7**95 % 10")

add(A, "What least number must be added to 5000 so that the sum is exactly divisible by 47?",
    ["29", "18", "47", "22"],
    "Type: least number to add. 5000 = 47 × 106 + 18. Add 47 − 18 = 29 (5029 = 47 × 107). "
    "Trap: 18 is the number to take away.", calc="47 - 5000 % 47")

add(A, "If 0.006 × 0.25 is written in standard form, it is:",
    ["1.5 × 10⁻³", "1.5 × 10⁻⁴", "1.5 × 10⁻²", "15 × 10⁻⁵"],
    "Type: multiplying decimals. 6 × 25 = 150, with 3 + 2 = 5 decimal places: 0.00150 = 1.5 × 10⁻³. "
    "Trap: 15 × 10⁻⁵ is the same value but not standard form (one digit before the point). Grew from 2018 Q54 and 2021 Q54.",
    nocalc=True)

add(A, "Three containers hold 156 litres, 234 litres and 390 litres of oil. Using the largest measure that measures all three exactly, how many measures are needed in all?",
    ["10", "78", "12", "15"],
    "Type: largest measure (HCF), with a count. HCF of 156, 234, 390 = 78 litres. Measures: 156 ÷ 78 + 234 ÷ 78 + 390 ÷ 78 = 2 + 3 + 5 = 10. "
    "Trap: 78 is the size of the measure, not the number of measures. Next angle of 2025 Q84.", calc="(156 + 234 + 390) // 78")

add(A, "A number when divided successively by 3, 5 and 8 leaves remainders 2, 1 and 4 respectively. Which of the following can be the number?",
    ["65", "97", "75", "53"],
    "Type: successive division. Work backwards: 4 × 5 + 1 = 21, then 21 × 3 + 2 = 65. Check: 65 ÷ 3 = 21 r 2; 21 ÷ 5 = 4 r 1; 4 ÷ 8 = 0 r 4. "
    "Any 65 + 120k also works (120 = 3 × 5 × 8), as in 2025 Q70 (214 = 94 + 120).", calc="(4*5 + 1)*3 + 2")

add(A, "The least number which, when divided by 12, 15, 20 and 54, leaves a remainder of 8 in each case is:",
    ["548", "540", "532", "1088"],
    "Type: same remainder in every case: LCM + remainder. LCM of 12, 15, 20, 54 = 540. Answer 540 + 8 = 548. "
    "Trap: 532 takes the remainder away.", calc="540 + 8")

add(A, "0.444… + 0.3737… (both recurring) = ?",
    ["0.8181…", "0.8118…", "0.7181…", "0.81"],
    "Type: adding recurring decimals. Turn them into fractions: 0.444… = 4/9 = 44/99, and 0.3737… = 37/99. "
    "The sum is 81/99 = 0.8181… Adding digit by digit (0.44 + 0.37 = 0.81) loses the repeat. Next angle of 2021 Q56.", nocalc=True)

add(A, "The least number which, when divided by 5, 6, 7 and 8, leaves remainders 3, 4, 5 and 6 respectively is:",
    ["838", "842", "840", "836"],
    "Type: remainders each the same amount short of the divisors. 5 − 3 = 6 − 4 = 7 − 5 = 8 − 6 = 2. So the number is LCM − 2. "
    "LCM of 5, 6, 7, 8 = 840, and 840 − 2 = 838.", calc="840 - 2")

add(A, "How many factors does 360 have?",
    ["24", "20", "18", "36"],
    "Type: number of factors. 360 = 2³ × 3² × 5. Add 1 to each power and multiply: (3 + 1)(2 + 1)(1 + 1) = 24.",
    calc="4*3*2")

add(A, "If the number 653xy is divisible by 90, then (x + y) = ?",
    ["4", "2", "3", "6"],
    "Exact past question (2025 Q100). 90 = 9 × 10. Divisible by 10, so y = 0. Divisible by 9, so 6 + 5 + 3 + x = 14 + x is a multiple of 9: x = 4. "
    "x + y = 4.", calc="4 + 0", src="2025 Q100")

add(A, "The greatest number which divides 1305, 4665 and 6905 leaving the same remainder in each case is:",
    ["1120", "1305", "560", "280"],
    "Type: same remainder, greatest divisor: the HCF of the differences. 4665 − 1305 = 3360 and 6905 − 4665 = 2240. "
    "HCF(3360, 2240) = 1120. (Each number leaves 185.)", calc="math.gcd(4665 - 1305, 6905 - 4665)")

add(A, "The H.C.F. of 2/3, 8/9, 16/81 and 10/27 is:",
    ["2/81", "2/3", "160/3", "1/81"],
    "Type: HCF of fractions = HCF of the tops ÷ LCM of the bottoms. HCF(2, 8, 16, 10) = 2; LCM(3, 9, 81, 27) = 81. Answer 2/81. "
    "Trap: 160/3 is the LCM rule. Next angle of 2021 Q53 and 2018 Q53.", calc="2/81")

add(A, "What is the largest 4-digit number exactly divisible by 88?",
    ["9944", "9988", "9900", "9856"],
    "Type: largest multiple below a limit. 9999 = 88 × 113 + 55. Take away the remainder: 9999 − 55 = 9944. "
    "Next angle of 2018 Q52 (least five-digit multiple).", calc="9999 - 9999 % 88")

add(A, "The difference of the squares of two consecutive odd numbers is 64. The larger of the two numbers is:",
    ["17", "15", "19", "33"],
    "Type: consecutive odd numbers. The difference of squares is twice the sum, so the sum is 32 and the numbers are 15 and 17. "
    "Larger 17. Twin of 2025 Q71 (even numbers, 84).", calc="64 // 2 // 2 + 1")

add(A, "The least number which should be added to 2497 so that the sum is exactly divisible by 5, 6, 4 and 3 is:",
    ["23", "3", "13", "33"],
    "Exact past question (2018 Q82). LCM of 5, 6, 4, 3 = 60. 2497 = 60 × 41 + 37, so add 60 − 37 = 23 (2520 = 60 × 42).",
    calc="60 - 2497 % 60", src="2018 Q82")

add(A, "The value of √0.000064 is:",
    ["0.008", "0.08", "0.0008", "0.8"],
    "Type: square root of a decimal. 64 = 8². Six decimal places become three, so 0.008. Check: 0.008 × 0.008 = 0.000064. "
    "Next angle of 2021 Q63 (√1.5625).", calc="0.008")

add(A, "A two-digit number is 4 times the sum of its digits. If 27 is added to the number, its digits are reversed. The number is:",
    ["36", "63", "24", "48"],
    "Type: two-digit number and its reverse. 10a + b = 4(a + b) gives b = 2a. Adding 27 reverses it, so 9(b − a) = 27 and b − a = 3. "
    "So a = 3, b = 6: the number is 36. Trap: 63 is the reverse.", calc="36")

add(A, "If 653xy is divisible by 72 and y = 4, then the value of x is:",
    ["0", "4", "8", "9"],
    "Type: unknown digit with 72 = 8 × 9. The last three digits 3x4 must divide by 8: x = 0, 4 or 8. The digit sum 18 + x must divide by 9: "
    "x = 0 or 9. Only x = 0 passes both (65304 = 72 × 907). The 72 twin of 2025 Q100.", calc="0")

add(A, "The largest number that divides 1657 and 2037 leaving remainders 6 and 5 respectively is:",
    ["127", "123", "235", "305"],
    "Type: greatest divisor with given remainders. Take each remainder away: 1657 − 6 = 1651 and 2037 − 5 = 2032. "
    "HCF(1651, 2032) = 127 (1651 = 13 × 127, 2032 = 16 × 127).", calc="math.gcd(1651, 2032)")

add(A, "0.3666… (6 recurring) expressed as a fraction is:",
    ["11/30", "4/11", "33/100", "11/36"],
    "Type: mixed recurring decimal. (All the digits − the part that does not repeat) over one 9 and one 0: (36 − 3)/90 = 33/90 = 11/30. "
    "Trap: 4/11 = 36/99 is 0.3636…", calc="11/30")

add(A, "The L.C.M. of 1/3, 5/6, 2/9 and 4/27 is:",
    ["20/3", "1/54", "20/27", "10/3"],
    "Type: LCM of fractions = LCM of the tops ÷ HCF of the bottoms. LCM(1, 5, 2, 4) = 20; HCF(3, 6, 9, 27) = 3. Answer 20/3. "
    "Trap: 1/54 uses the HCF rule.", calc="20/3")

add(A, "The unit digit of 2³⁵ × 3²² is:",
    ["2", "8", "9", "4"],
    "Type: last digit of a product of powers. 2 cycles 2, 4, 8, 6: 35 ÷ 4 leaves 3, so 8. 3 cycles 3, 9, 7, 1: 22 ÷ 4 leaves 2, so 9. "
    "8 × 9 = 72, last digit 2. Find each last digit, then multiply only the last digits.", calc="(2**35 * 3**22) % 10")
