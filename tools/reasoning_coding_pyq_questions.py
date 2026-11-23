# Past questions of the coding-decoding section, every one, word for word (22 Nov 2026, user asked "make a coding decoding
# all 3 years pyq as a mock, exact questions"). 17 questions: 2018 Q17, 20, 21, 22, 49; 2021 Q2, 15, 17, 21,
# 34, 35, 44; 2025 Q2, 18, 30, 42, 43. Options are kept in the printed order (a = the right letter), and the
# questions in paper order. Text from pyq/OPSC-ASO-2021-Reasoning-Maths-Paper-II.md and the 2018 and 2025 OCR;
# only OCR slips were fixed. No official key exists: every answer is worked out below.
# Build: python3 .claude/skills/aso-mock/scripts/build.py tools/reasoning_coding_pyq_questions.py

META = dict(
    paper="reasoning",
    title="ASO Coding-Decoding Past Questions",
    hub_title="Coding-Decoding · all past questions",
    masthead="Coding PYQ",
    heading="Paper II (A) · Reasoning · Coding and decoding · 2018, 2021, 2025",
    tagline="All <b>17 coding questions</b> from the<br>2018, 2021 and 2025 papers, word for word.",
    key="aso-reasoning-coding-pyq",
    code="CODP",
    out="ASO-Reasoning-Coding-PYQ.html",
    minutes=17,
    seed=20261126,
    order="given",
    date="22 Nov 2026",
    draw="every coding question of the three papers (no draw)",
    topic="rcod",
    intro=[
        "These are all seventeen coding and decoding questions the examiner has set in Paper II: five from 2018, seven "
        "from 2021 and five from 2025. They are word for word and in paper order, with the options in the order "
        "they were printed. Coding is one of the steadiest sections, at five to seven questions every year.",
        "There is no official answer key, so every answer was worked out letter by letter and the working is shown. "
        "The three kinds to watch are letter shifts, letters turned into numbers and added, and coded sentences. "
        "A few option letters were unreadable in the 2018 scan and are rebuilt; the explanation says where.",
    ],
)

Q = []
def add(s, q, o, e, k="one", n=False, c=False, a=None, **x):
    d = dict(s=s, q=q, o=o, e=e, k=k, n=n, c=c, a=a); d.update(x); Q.append(d)

C = "Coding and decoding"

# ---------------------------------------------------------------- 2018
add(C, "In a certain code language '134' means 'good and tasty', '478' means 'see good pictures' and '729' means "
    "'pictures are faint'. Which of the following digits stands for 'see'?",
    ["9", "2", "1", "8"],
    "'good' is in the first two sentences, and the only digit in both codes is 4, so good = 4. 'pictures' is in the "
    "second and third, and the shared digit is 7, so pictures = 7. In '478' (see good pictures) the digit left over "
    "is 8, so see = 8. Method: find the word two sentences share, then the code they share. (Option D reads '÷8' in the scan.)",
    a=3, src="2018 Q17")

add(C, "If FRIEND is coded as HUMJTK, how is CANDLE written in that code?",
    ["EDRIRL", "DCQHQK", "ESJFME", "DEQJOM"],
    "Each letter moves forward by a growing step: F +2 = H, R +3 = U, I +4 = M, E +5 = J, N +6 = T, D +7 = K. "
    "CANDLE: C +2 = E, A +3 = D, N +4 = R, D +5 = I, L +6 = R, E +7 = L, giving EDRIRL.",
    a=0, src="2018 Q20")

add(C, "In a certain code language COMPUTER is written as RFUVQNPC. How will MEDICINE be written in that code language?",
    ["MFEDJJOE", "EOJDEJFM", "MFEJDJOE", "EOJDJEFM"],
    "Write COMPUTER backwards: RETUPMOC. Compare with RFUVQNPC: the first and last letters (R, C) stay, and every "
    "letter between moves one step forward (E→F, T→U, U→V, P→Q, M→N, O→P). MEDICINE backwards is ENICIDEM; keep E "
    "and M, move the middle six forward: N→O, I→J, C→D, I→J, D→E, E→F. Answer EOJDJEFM. Trap: B (EOJDEJFM) swaps two letters.",
    a=3, src="2018 Q21")

add(C, "If ROSE is coded as 6821, CHAIR is coded as 73456 and PREACH is coded as 961473, what will be the code for SEARCH?",
    ["246173", "214673", "214763", "216473"],
    "Each letter has a fixed digit. ROSE: R 6, O 8, S 2, E 1. CHAIR: C 7, H 3, A 4, I 5, R 6. PREACH: P 9 (the rest "
    "agree). SEARCH: S 2, E 1, A 4, R 6, C 7, H 3 = 214673. The options differ in one or two places, so check digit by digit.",
    a=1, src="2018 Q22")

add(C, "If Z = 52 and ACT = 48, then BAT will be equal to:",
    ["39", "41", "44", "46"],
    "Z is the 26th letter, and 26 × 2 = 52. ACT: 1 + 3 + 20 = 24, and 24 × 2 = 48. So the code is twice the sum of the "
    "letter places. BAT: 2 + 1 + 20 = 23, and 23 × 2 = 46. (Only option D is readable in the scan; A to C are rebuilt.) "
    "The same rule came back in 2025 Q42 and Q43.",
    a=3, src="2018 Q49")

# ---------------------------------------------------------------- 2021
add(C, "In a certain code language, 'VIRTUE' is coded as '201' and 'TRAGEDY' is coded as '218'. How will 'PROFANE' "
    "be coded in that language?",
    ["570", "342", "432", "456"],
    "Number each letter from the back (Z = 1, A = 26; that is 27 minus its place) and add them, then multiply by "
    "the number of vowels. VIRTUE: 5 + 18 + 9 + 7 + 6 + 22 = 67; vowels I, U, E = 3; 67 × 3 = 201. TRAGEDY: 109 × 2 "
    "(A, E) = 218. PROFANE: 11 + 9 + 12 + 21 + 26 + 13 + 22 = 114; vowels O, A, E = 3; 114 × 3 = 342. "
    "The hardest coding question of the three papers: if it does not open in a minute, skip it.",
    a=1, src="2021 Q2")

add(C, "How is 'sure' written in a code language?\nI. 'he is sure' is written as 'ja ha ma' in that code language.\n"
    "II. 'is she sure' is written as 'ka ja ma' in that code language.",
    ["Ja", "Ja or ma", "Ma", "Ha"],
    "'is' and 'sure' are in both sentences, and 'ja' and 'ma' are in both codes. So 'sure' is ja or ma, and the two "
    "sentences cannot tell which. When two words share the same two codes, the answer is 'either'.",
    a=1, src="2021 Q15")

add(C, "If ZIP = 198 and ZAP = 246, then how will you code VIP?",
    ["174", "222", "888", "990"],
    "Number the letters from the back (Z = 1, A = 26), add them, add the number of letters, and multiply by 6. "
    "ZIP: 1 + 18 + 11 = 30, plus 3 = 33, × 6 = 198. ZAP: 1 + 26 + 11 = 38, plus 3 = 41, × 6 = 246. "
    "VIP: 5 + 18 + 11 = 34, plus 3 = 37, × 6 = 222. Shortcut: ZIP and ZAP differ only in I/A (18 vs 26, 8 apart) and "
    "the codes differ by 48 = 8 × 6, so each step of a letter is worth 6. VIP differs from ZIP by V/Z (5 vs 1, 4 apart): "
    "198 + 24 = 222.",
    a=1, src="2021 Q17")

add(C, "In a certain code, MOTHER is written as ONHURF. How will ANSWER be written in that code?",
    ["NBXSSE", "NBWRRF", "MAVSPE", "NBWTRF"],
    "Swap each pair of letters (MO TH ER → OM HT RE), then leave the first of each pair and move the second one step "
    "forward: O, M+1 = N, H, T+1 = U, R, E+1 = F, giving ONHURF. ANSWER: AN SW ER → NA WS RE → N, B, W, T, R, F = NBWTRF.",
    a=3, src="2021 Q21")

add(C, "In a certain code language, \"GOAT\" is written as \"45\" and \"COAT\" is written as \"41\". How is \"BOAT\" "
    "written in that code language?",
    ["40", "41", "42", "43"],
    "Add the letter places and add 2. GOAT: 7 + 15 + 1 + 20 = 43, plus 2 = 45. COAT: 39 + 2 = 41. BOAT: 38 + 2 = 40. "
    "Shortcut: only the first letter changes; G to C is 4 steps and the code drops 4, so B (one before C) gives 40.",
    a=0, src="2021 Q34")

add(C, "In a certain code language, TUTORIAL is written as DODNGLCF and DANCE is written as YCJMZ. How is EDUCATION "
    "written in that code?",
    ["ZYMODCLNJ", "ZYOMCDLNJ", "ZYOMDCLNJ", "ZYOTNLCMD"],
    "Each letter has its own fixed code (no shifting rule). From the two words: T = D, U = O, O = N, R = G, I = L, "
    "A = C, L = F, D = Y, N = J, C = M, E = Z. EDUCATION: E Z, D Y, U O, C M, A C, T D, I L, O N, N J = ZYOMCDLNJ. "
    "The options differ only in the middle, so decode just those letters (U C A T).",
    a=1, src="2021 Q35")

add(C, "If REQUEST is written as S2R52TU, then how will ACID be written?",
    ["1394", "IC94", "BDJE", "1D3E"],
    "Consonants move one letter forward (R → S, Q → R, S → T, T → U). Vowels become their place among the vowels: "
    "A = 1, E = 2, I = 3, O = 4, U = 5. ACID: A = 1, C → D, I = 3, D → E, giving 1D3E. (In the scan the 1 of option "
    "D looks like a capital I.)",
    a=3, src="2021 Q44")

# ---------------------------------------------------------------- 2025
add(C, "In a certain code language, STRAIGHT is written as TSARGITH. How will THURSDAY be written as in that language?",
    ["AYSDURTH", "HTRUDSYA", "UHTDRSYA", "HTRUDSAY"],
    "Split the word into pairs and swap each pair: ST RA IG HT → TS AR GI TH. THURSDAY: TH UR SD AY → HT RU DS YA = "
    "HTRUDSYA. Trap: D (HTRUDSAY) forgets to swap the last pair.",
    a=1, src="2025 Q2")

add(C, "In a certain code language, 'cool drinks available here' is written as 'bhu man juk lop', 'available lost "
    "objects here' is written as 'gan bhu nut juk', 'be cool search objects' is written as 'vax der man nut', and "
    "'available drinks desert search' is written as 'but juk der lop'. How will 'lost drinks' be written in that language?",
    ["gan lop", "nut gan", "lop bhu", "juk gan"],
    "'available' is in sentences 1, 2 and 4; the only code in all three is juk. 'here' is in 1 and 2: bhu and juk are "
    "shared, juk is taken, so here = bhu. 'drinks' is in 1 and 4: shared lop and juk, so drinks = lop. 'objects' (2 "
    "and 3) = nut. In sentence 2 the code left for 'lost' is gan. So 'lost drinks' = gan lop.",
    a=0, src="2025 Q18")

add(C, "In a certain code language, 'first of all' is written as 'kan dan san', 'who is first' is written as 'zan kan "
    "ven', and 'this is pale' is written as 'ven gen len'. How will 'who' be written in that language?",
    ["kan", "gen", "zan", "ven"],
    "'first' is in sentences 1 and 2, sharing kan, so first = kan. 'is' is in sentences 2 and 3, sharing ven, so "
    "is = ven. In 'who is first' (zan kan ven) the code left is zan, so who = zan.",
    a=2, src="2025 Q30")

add(C, "In a certain code language, 'MOST' is written as '134' and 'FUR' is written as '90'. How will 'SUCCESS' be "
    "written in that language?",
    ["89", "175", "215", "178"],
    "Twice the sum of the letter places. MOST: 13 + 15 + 19 + 20 = 67, × 2 = 134. FUR: 6 + 21 + 18 = 45, × 2 = 90. "
    "SUCCESS: 19 + 21 + 3 + 3 + 5 + 19 + 19 = 89, × 2 = 178. Trap: 89 is the sum before doubling. Same rule as 2018 Q49.",
    a=3, src="2025 Q42")

add(C, "If N = 28 and ORE = 76, then how will you code PALE?",
    ["68", "72", "76", "19"],
    "N is the 14th letter and 14 × 2 = 28. ORE: 15 + 18 + 5 = 38, × 2 = 76. PALE: 16 + 1 + 12 + 5 = 34, × 2 = 68. "
    "This rule (twice the sum) came three times: 2018 Q49, 2025 Q42 and here. Learn EJOTY (E 5, J 10, O 15, T 20, Y 25) "
    "to add fast.",
    a=0, src="2025 Q43")
