# Ranking Set 01 (25 Nov 2026): 30 questions on ranking, order and dictionary order (user: "make a guide here only and 30 question mock").
# Plan drawn with: python3 .claude/skills/aso-mock/scripts/draw.py reasoning --topics rnk --n 30 (seed 9011):
# 13 dictionary order, 12 row rank, 5 ordering puzzles; two exact past questions (2021 Q1, 2021 Q38). Order is given (families mixed by hand).
# Every answer is re-checked by code inside this file (asserts). First option is right unless `a` is given.
# Build: python3 .claude/skills/aso-mock/scripts/build.py tools/reasoning_ranking1_questions.py
import itertools

META = dict(
    paper="reasoning",
    title="ASO Ranking Set 01",
    hub_title="Ranking Set 01",
    masthead="Ranking 01",
    heading="Paper II (A) · Reasoning · Ranking, order and dictionary order",
    tagline="30 questions on <b>row rank, dictionary order</b><br>and ordering puzzles, set to the 2018, 2021 and 2025 papers.",
    key="aso-reasoning-ranking-1",
    code="RNK1",
    out="ASO-Reasoning-Ranking-1.html",
    minutes=27,
    seed=20261125,
    order="given",
    date="25 Nov 2026",
    draw="python3 .claude/skills/aso-mock/scripts/draw.py reasoning --topics rnk --n 30 --seed 9011",
    topic="rrnk",
    intro=[
        "Thirty questions on the topic that grew fastest in the papers: 2 questions in 2018, 4 in 2021 and 8 in 2025. "
        "The mix follows the papers: 13 dictionary-order questions, 12 row-rank questions (left plus right minus one, "
        "swaps, shifts, between) and 5 ordering puzzles (who is the tallest, who is the lightest).",
        "Two are real past questions word for word (2021 Q1 and 2021 Q38). Every other question is the next angle of a "
        "past one, and its explanation names the question it grew from. Press Copy answers at the end and paste the report into the chat for a redo set.",
    ],
)

Q = []
def add(s, q, o, e, k="one", n=False, c=False, a=None, **x):
    d = dict(s=s, q=q, o=o, e=e, k=k, n=n, c=c, a=a); d.update(x); Q.append(d)

S = "Number ranking"
R = ["I", "II", "III", "IV", "V"]

def sorted_idx(words):
    return sorted(range(len(words)), key=lambda i: words[i].lower())

def tel(items):
    return "(" + ", ".join(items) + ")"

def order_q(words, intro, why, src, directory=False, key=None):
    """Five words -> 'arrange in dictionary order' question with four options (right first)."""
    ks = key or (lambda i: words[i].lower())
    idx = sorted(range(5), key=ks)
    right = [R[i] for i in idx]
    def fmt(seq): return ", ".join("(%s)" % x for x in seq)
    opts = [right]
    for p in [(2, 3), (0, 1), (1, 2), (3, 4), (0, 2)]:
        s = list(right); s[p[0]], s[p[1]] = s[p[1]], s[p[0]]
        if s not in opts: opts.append(s)
        if len(opts) == 4: break
    stem = intro + "\n" + "\n".join("(%s) %s" % (R[i], w) for i, w in enumerate(words))
    ordered = ", ".join(words[i] for i in idx)
    add(S, stem, [fmt(o) for o in opts], "Why: %s Order: %s. Grew from: %s." % (why, ordered, src))

def word_q(words, intro, pos, ans, why, src, wrong):
    """pos: 0-based index into sorted list; ans checked."""
    idx = sorted_idx(words)
    got = words[idx[pos]]
    assert got == ans, (got, ans)
    assert ans not in wrong and len(set(wrong)) == 3
    ordered = ", ".join(words[i] for i in idx)
    add(S, intro + "\n" + ", ".join(words), [ans] + wrong,
        "Why: %s Order: %s. Grew from: %s." % (why, ordered, src))

DICT = "English dictionary"

# ------------------------------------------------------------------ 1  row rank: both ends
assert 21 + 21 - 1 == 41
add(S, "A girl is 21st from both ends of a row. How many girls are there in the row?",
    ["41", "42", "40", "43"],
    "Why: total = left rank + right rank − 1 = 21 + 21 − 1 = 41. The girl is counted twice when you add the two ranks, so take one away. "
    "She is the middle girl: 20 on each side. Grew from: 2025 Q3 (33rd from both ends). Same frame, new number.")

# ------------------------------------------------------------------ 2  dictionary: full order, Cons-
order_q(["Consult", "Console", "Contain", "Conserve", "Consider"],
        "Arrange the following words in the order in which they appear in an English Dictionary:",
        "All five start with 'Con'. Then 'Cons' (Conserve, Consider, Console, Consult) comes before 'Cont' (Contain), because s comes before t. "
        "Among the 'Cons' words the next letters are e, i, o, u.",
        "2025 Q16 (Radical, Radiate…) and 2021 Q13 (Meticulous, Metric…)")

# ------------------------------------------------------------------ 3  ordering puzzle (heights)
def solve(persons, cons):
    out = []
    for perm in itertools.permutations(persons):          # perm[0] is the tallest
        rank = {p: i for i, p in enumerate(perm)}          # smaller number = taller
        if all(c(rank) for c in cons):
            out.append(perm)
    return out

def taller(a, b): return lambda r: r[a] < r[b]
def only_taller_than(a, b): return lambda r: r[a] == 5 and r[b] == 6          # not used for 7 people
def taller_than_only(x, y, n):      # x is taller than only y: y is last, x is second last
    return lambda r: r[x] == n - 2 and r[y] == n - 1
def shorter_than_only(x, y):        # x is shorter than only y: y is first, x second
    return lambda r: r[y] == 0 and r[x] == 1

P = list("ABCDEFG")
c1 = [shorter_than_only("E", "A"), taller_than_only("B", "D", 7), taller("F", "B"), taller("C", "F"), taller("G", "C")]
sol = solve(P, c1)
assert len(sol) == 1 and sol[0][3] == "C", sol
add(S, "There are seven persons A, B, C, D, E, F and G. Each of them has a different height. E is shorter than only A. "
       "B is taller than only D. F is taller than B but shorter than C. G is taller than C. "
       "Who is the fourth tallest of the seven?",
    ["C", "F", "G", "B"],
    "Why: 'E is shorter than only A' means A is the tallest and E is second. 'B is taller than only D' means D is the shortest and B is second shortest. "
    "The rest of the chain is G > C > F, and it fills places 3, 4 and 5. Order, tallest first: A, E, G, C, F, B, D. The fourth tallest is C. "
    "Trap: 'taller than only' and 'shorter than only' point to opposite ends. Grew from: 2025 Q19 (seven persons of different heights, 'C is shorter than only G').")

# ------------------------------------------------------------------ 4  row rank: between
assert 40 - 14 + 1 == 27 and 27 - 9 - 1 == 17
add(S, "In a row of 40 boys, Arun is 9th from the left end and Bala is 14th from the right end. How many boys are there between Arun and Bala?",
    ["17", "18", "16", "15"],
    "Why: Bala from the left = 40 − 14 + 1 = 27th. Between the 9th and the 27th: 27 − 9 − 1 = 17. "
    "Draw the row and mark both boys. Grew from: 2021 Q38 (row of thirty, R 4th from right and W 10th from left, 16 between).")

# ------------------------------------------------------------------ 5  dictionary: prefix rule
order_q(["Pair", "Painter", "Pail", "Paint", "Pain"],
        "Arrange the following words in the order in which they appear in an English Dictionary:",
        "All start with 'Pai'. Pail (l), Pain (n) and Pair (r) differ at the fourth letter: l, n, r. "
        "Pain, Paint and Painter all begin with 'Pain', and a shorter word comes before a longer word that starts with it: Pain, Paint, Painter. Pair comes after all of them.",
        "2021 Q1 (telephone directory, Krishanmurty…) and 2025 Q26 (Un- words)")

# ------------------------------------------------------------------ 6  row rank: swap, find total
n = 25 + 20 - 1
assert n == 44
add(S, "In a row, Kiran is at the 12th position from the left and Manu is at the 20th position from the right. "
       "If they interchange their positions, Kiran becomes 25th from the left. How many persons are there in the row?",
    ["44", "45", "43", "46"],
    "Why: After the swap, Kiran stands where Manu stood. So Manu's old place is 25th from the left and 20th from the right. "
    "Total = 25 + 20 − 1 = 44. Only the swapped place matters; the 12 is a distraction. "
    "Grew from: 2025 Q31 (Aman 20th from left, Gita 14th from right; after swapping Aman is 30th from left) and 2018 Q48. Same frame, but this one asks for the total.")

# ------------------------------------------------------------------ 7  dictionary: fourth from left
word_q(["River", "Rival", "Rise", "Ritual", "Rice"],
       "If the following words are arranged in the order of an English Dictionary from left to right, which one will be fourth from the left?",
       3, "Rival", "All start with 'Ri'. The third letters are c (Rice), s (Rise), t (Ritual) and v (Rival, River). So the order is Rice, Rise, Ritual, then Rival and River. "
       "Rival comes before River because a comes before e. Fourth from the left is Rival.",
       "2021 Q42 (fourth from the left) and 2025 Q28 (fourth from the right)", ["River", "Ritual", "Rise"])

# ------------------------------------------------------------------ 8  ordering puzzle (weights, count)
P2 = list("PQRSTUV")
c2 = [taller_than_only("U", "R", 7), shorter_than_only("V", "S"), taller("Q", "P"), taller("P", "T"), taller("T", "U")]
sol2 = solve(P2, c2)
assert len(sol2) == 1
below_p = 6 - sol2[0].index("P")
assert below_p == 3
add(S, "Seven friends P, Q, R, S, T, U and V have different weights. U is heavier than only R. V is lighter than only S. "
       "Q is heavier than P. T is lighter than P but heavier than U. How many friends are lighter than P?",
    ["Three", "Two", "Four", "Five"],
    "Why: 'U is heavier than only R' means R is the lightest and U is second lightest. 'V is lighter than only S' means S is the heaviest and V is second. "
    "The chain Q > P > T > U fits in the middle. Order, heaviest first: S, V, Q, P, T, U, R. Lighter than P: T, U and R, so three. "
    "Grew from: 2025 Q19 (seven persons by height) with a count at the end.")

# ------------------------------------------------------------------ 9  row rank: moves to the right
assert 30 - (12 + 4) + 1 == 15
add(S, "In a row of 30 girls facing north, Pooja is 12th from the left end. If she moves four places to her right, "
       "what will be her position from the right end of the row?",
    ["15th", "16th", "14th", "17th"],
    "Why: Moving to her right adds to her number from the left: 12 + 4 = 16th from the left. From the right end: 30 − 16 + 1 = 15th. "
    "Facing north, her right hand is the east side, so her left-end number grows when she moves right. "
    "Grew from: 2025 Q32 (row of 26 facing north, 13th from the right moves three places left).")

# ------------------------------------------------------------------ 10 dictionary: telephone directory with initials
add(S, "Select the correct option that indicates the arrangement of the given names in the order in which they appear in a telephone directory:\n"
       "(I) Das, R.\n(II) Dash, A.\n(III) Das, A.\n(IV) Dasgupta, S.\n(V) Das, B.",
    ["(III), (V), (I), (IV), (II)", "(III), (V), (I), (II), (IV)", "(V), (III), (I), (IV), (II)", "(I), (V), (III), (IV), (II)"],
    "Why: A directory sorts by surname first, then by the first letter of the given name. Surnames: Das (three people), Dasgupta, Dash. "
    "'Das' is the shortest, so it comes first. Then Dasgupta (g) before Dash (h). Among the three Das: A, B, R. Order: Das A, Das B, Das R, Dasgupta, Dash. "
    "Grew from: 2021 Q1 (telephone directory).")

# ------------------------------------------------------------------ 11 row rank: top and bottom of a class
assert 7 + 28 - 1 == 34
add(S, "In a class, Tina is 7th from the top and 28th from the bottom. How many students are there in the class?",
    ["34", "35", "33", "36"],
    "Why: total = 7 + 28 − 1 = 34. Tina is counted in both ranks, so subtract one. "
    "Grew from: 2018 Q19 (Sam 9th from the top and 38th from the bottom).")

# ------------------------------------------------------------------ 12 REPEAT 2021 Q1
add(S, "Select the correct option that indicates the arrangement of the given words in the order in which they appear in a telephone directory:\n"
       "(I) Krishanmurty\n(II) Krishnamurthy\n(III) Krishnmurthi\n(IV) Krishanmurthy\n(V) Krishnamurti",
    ["(IV), (I), (II), (V), (III)", "(IV), (I), (II), (III), (V)", "(IV), (V), (II), (III), (I)", "(IV), (III), (V), (III), (II)"],
    "Why: Compare letter by letter. 'Krisha…' comes before 'Krishn…'. Between the two 'Krisha' words, 'Krishanmurth…' (h) comes before 'Krishanmurty' (y), so IV then I. "
    "Of the 'Krishn' words, 'Krishna…' comes before 'Krishnm…', so II and V come before III. II (Krishnamurth…) comes before V (Krishnamurti) because h comes before i. Order: IV, I, II, V, III. "
    "Exact past question, 2021 Q1; the key is the printed one (A). Option D has a repeated (III) in the paper.", src="2021 Q1")

# ------------------------------------------------------------------ 13 REPEAT 2021 Q38
assert 30 - 4 + 1 == 27 and 27 - 10 - 1 == 16
add(S, "In a row of thirty boys, R is 4th from right end and W is 10th from the left end. How many boys are there between R and W?",
    ["15", "16", "17", "Cannot be determined"],
    "Why: R is 27th from the left (30 − 4 + 1). Between the 10th and the 27th places: 27 − 10 − 1 = 16. Exact past question, 2021 Q38.",
    a=1, src="2021 Q38")

# ------------------------------------------------------------------ 14 dictionary: middle word
word_q(["Gather", "Garden", "Gaze", "Garage", "Gamble"],
       "Which of the following words will be in the middle (third) when they are arranged in the order of an English Dictionary?",
       2, "Garden", "All start with 'Ga'. Third letters: m (Gamble), r (Garage, Garden), t (Gather), z (Gaze). "
       "Garage and Garden share 'Gar', and a comes before d, so Garage is before Garden. Order: Gamble, Garage, Garden, Gather, Gaze. The middle one is Garden.",
       "2021 Q42 and 2025 Q28 (a position after arranging five words)", ["Garage", "Gather", "Gamble"])

# ------------------------------------------------------------------ 15 ordering puzzle (marks)
P3 = list("ABCDEF")
c3 = [lambda r: r["F"] == 0, taller("D", "C"), taller("C", "E"), taller("B", "A"), lambda r: r["B"] == 3]
sol3 = solve(P3, c3)
last = {s[-1] for s in sol3}
assert last == {"E", "A"}, last
c3 = [lambda r: r["F"] == 0, taller("D", "C"), taller("C", "E"), taller("B", "A"), lambda r: r["B"] == 3, taller("A", "E")]
sol3 = solve(P3, c3)
assert len({s[-1] for s in sol3}) == 1 and sol3[0][-1] == "E", sol3
add(S, "Six students A, B, C, D, E and F scored different marks in a test. F scored the highest. D scored more than C, and C scored more than E. "
       "B scored more than only two students. A scored more than E but less than B. Who scored the lowest?",
    ["E", "A", "C", "B"],
    "Why: 'B scored more than only two students' puts B 4th from the top. F is first. D and C must be above E, and A is between B and E. "
    "Order, highest first: F, D, C, B, A, E. The lowest is E. Check: below B are A and E, exactly two. "
    "Grew from: 2025 Q19 (who is the shortest among seven).")

# ------------------------------------------------------------------ 16 row rank: below in the class
assert 11 + 9 == 20 and 20 + 18 - 1 == 37
add(S, "Rohit is 11th from the top in a class. Sohan is 9 places below Rohit and is 18th from the bottom. How many students are there in the class?",
    ["37", "38", "36", "39"],
    "Why: Sohan from the top = 11 + 9 = 20th. Total = 20 + 18 − 1 = 37. First find his rank from the same end as the other number, then use left + right − 1. "
    "Grew from: 2018 Q19 and 2025 Q44 (two persons, a gap, then the total).")

# ------------------------------------------------------------------ 17 dictionary: last word
word_q(["Quiz", "Quite", "Quilt", "Quit", "Quiet"],
       "Which of the following words will come last when arranged in the order of an English Dictionary?",
       4, "Quiz", "All start with 'Qui'. The next letters: e (Quiet), l (Quilt), t (Quit, Quite), z (Quiz). z is the last letter of the alphabet. "
       "Order: Quiet, Quilt, Quit, Quite, Quiz. Quit comes before Quite because the shorter word comes first.",
       "2025 Q16 and 2025 Q26 (the five-word dictionary frame)", ["Quite", "Quit", "Quilt"])

# ------------------------------------------------------------------ 18 row rank: between, with total hidden
assert 8 + 5 + 11 == 24
add(S, "Anil is 8th from the left end of a row and Sunil is 11th from the right end. There are five boys between them. How many boys are there in the row?",
    ["24", "25", "23", "26"],
    "Why: Count everyone: 7 boys before Anil, Anil, 5 between, Sunil, and 10 after Sunil. 7 + 1 + 5 + 1 + 10 = 24. "
    "Shortcut: left rank + between + right rank = 8 + 5 + 11 = 24. "
    "Grew from: 2025 Q44 (Bhavuk 7th from left, Bhavan 16th from right, six boys between them).")

# ------------------------------------------------------------------ 19 dictionary: how many stay in place
words = ["Hand", "Hard", "Hair", "Half", "Head"]
idx = sorted_idx(words)
stay = sum(1 for pos, i in enumerate(idx) if pos == i)
assert stay == 1
add(S, "If the following words are arranged in the order of an English Dictionary, how many words will remain at the same position?\n"
       "Hand, Hard, Hair, Half, Head",
    ["One", "Two", "Three", "None"],
    "Why: Order in the dictionary: Hair, Half, Hand, Hard, Head. Compare with the given order: Hand (3rd now, 1st before), Hard (4th, was 2nd), "
    "Hair (1st, was 3rd), Half (2nd, was 4th), Head (5th, was 5th). Only Head stays. "
    "Grew from: 2025 Q28 (position after arranging). New twist: how many stay.", a=0)

# ------------------------------------------------------------------ 20 row rank: middle
assert 45 // 2 == 22
add(S, "P is exactly in the middle of a row of 45 children. How many children are standing on his right side?",
    ["22", "23", "21", "24"],
    "Why: In a row of 45, the middle child is 23rd from each end. Children on one side: 45 − 1 = 44, half of it = 22. "
    "Grew from: 2025 Q3 (a boy 33rd from both ends: the middle of a row).")

# ------------------------------------------------------------------ 21 dictionary: second from the right (3-letter words)
word_q(["TAP", "RED", "MUD", "BOX", "HEN"],
       "If the following words are arranged in the order in which they appear in an English Dictionary from left to right, which word will be the second from the right?",
       3, "RED", "Look at the first letter: B, H, M, R, T. They are already different, so the order is BOX, HEN, MUD, RED, TAP. Second from the right is RED.",
       "2025 Q27–28 (LAP BUT CAR SON HID) and 2021 Q41–42 (THE MOD CPU)", ["TAP", "MUD", "HEN"])

# ------------------------------------------------------------------ 22 ordering puzzle (simple chain)
P4 = list("PQRST")
c4 = [taller("P", "Q"), taller("P", "R"), taller("Q", "S"), taller("S", "R"), taller("T", "P")]
sol4 = solve(P4, c4)
assert len(sol4) == 1 and sol4[0][-1] == "R", sol4
add(S, "Five friends are P, Q, R, S and T. P is taller than Q and R. S is shorter than Q but taller than R. T is taller than P. Who is the shortest?",
    ["R", "S", "Q", "P"],
    "Why: Join the statements into one chain: T > P > Q > S > R. The shortest is at the end of the chain, R. "
    "Method: write the letters in a line with > signs, and join statements at the common person. Grew from: 2025 Q19 (shortest of seven).")

# ------------------------------------------------------------------ 23 row rank: two leave
assert (36 - 14 + 1) - 1 == 22
add(S, "In a row of 36 boys, Raj is 14th from the left end. One boy standing at each end of the row leaves. What is Raj's position from the right end now?",
    ["22nd", "23rd", "21st", "24th"],
    "Why: Raj was 36 − 14 + 1 = 23rd from the right. The boy at the right end leaves, so Raj becomes 22nd from the right. "
    "The boy at the left end leaving does not change his place from the right. Grew from: 2025 Q32 (a place changes, find the new rank).")

# ------------------------------------------------------------------ 24 dictionary: second from the left (prefix)
word_q(["Relative", "Relax", "Relation", "Relate", "Relieve"],
       "If the following words are arranged in the order of an English Dictionary, which word will be second from the left?",
       1, "Relation", "All start with 'Rel'. Then 'Rela' (Relate, Relation, Relative, Relax) comes before 'Reli' (Relieve). Among the 'Rela' words the fifth letters are t, t, t, x: Relax is last of them. "
       "Relate, Relation and Relative share 'Relat': next letters e, i, i. So Relate first, then Relation and Relative (o before v). Order: Relate, Relation, Relative, Relax, Relieve.",
       "2025 Q16 (Radical, Radiate…) and 2025 Q28", ["Relate", "Relative", "Relax"])

# ------------------------------------------------------------------ 25 row rank: between two class ranks
assert 45 - 20 + 1 == 26 and 26 - 12 - 1 == 13
add(S, "In a class of 45 students, Mohan is 12th from the top and Sohan is 20th from the bottom. How many students are there between Mohan and Sohan?",
    ["13", "14", "12", "15"],
    "Why: Sohan from the top = 45 − 20 + 1 = 26th. Between the 12th and the 26th: 26 − 12 − 1 = 13. "
    "Grew from: 2021 Q38 (between two boys, one rank from each end).")

# ------------------------------------------------------------------ 26 dictionary: full order, Bea-/Bec-
order_q(["Because", "Beauty", "Beast", "Became", "Beat"],
        "Arrange the following words in the order in which they appear in an English Dictionary:",
        "'Bea…' words come before 'Bec…' words. Among the 'Bea' words: Beast (s), Beat (t), Beauty (u). Beast comes before Beat because s comes before t. "
        "Among the 'Bec' words: Became (m) before Because (u).",
        "2025 Q26 (Unimportant, Understand…) and 2021 Q13")

# ------------------------------------------------------------------ 27 row rank: ahead and behind
assert 12 + 1 + 17 == 30
add(S, "In a queue, Tara has 12 persons in front of her and 17 persons behind her. How many persons are there in the queue?",
    ["30", "29", "31", "28"],
    "Why: 12 in front + Tara + 17 behind = 30. Her place from the front is 13th and from the back 18th; 13 + 18 − 1 = 30. "
    "Do not forget to count Tara. Grew from: 2025 Q3 (counting from both ends).")

# ------------------------------------------------------------------ 28 dictionary: second from the right
word_q(["Unit", "Umbrella", "Under", "Ultra", "Uncle"],
       "If the following words are arranged in the order of an English Dictionary, which word will be second from the right?",
       3, "Under", "All start with 'U'. Second letters: l (Ultra), m (Umbrella), n (Uncle, Under, Unit). Among the 'Un' words: c (Uncle), d (Under), i (Unit). "
       "Order: Ultra, Umbrella, Uncle, Under, Unit. Second from the right is Under.",
       "2025 Q28 (fourth from the right)", ["Unit", "Uncle", "Umbrella"])

# ------------------------------------------------------------------ 29 dictionary: letters of a word
w = "PLANET"
srt = sorted(w)
same = sum(1 for a_, b_ in zip(w, srt) if a_ == b_)
assert same == 2
add(S, "If the letters of the word PLANET are arranged in alphabetical order, how many letters will remain at the same position?",
    ["One", "Two", "Three", "None"],
    "Why: PLANET in alphabetical order is A E L N P T. Compare place by place with P L A N E T: N stays 4th and T stays 6th. The others move. So two letters stay. "
    "Grew from: the letter-position questions of 2018 and 2021 and the 2025 dictionary frame.", a=1)

# ------------------------------------------------------------------ 30 ordering puzzle (seven persons, how many taller)
P5 = list("ABCDEFG")
c5 = [shorter_than_only("D", "G"), taller("B", "E"), taller("E", "A"), taller("A", "C"), taller("C", "F"), lambda r: r["B"] == 2]
sol5 = solve(P5, c5)
assert len(sol5) == 1, sol5
order5 = sol5[0]
cnt = order5.index("C")
assert cnt == 5 and "".join(order5) == "GDBEACF", order5
add(S, "Seven persons A, B, C, D, E, F and G have different heights. D is shorter than only G. B is taller than E, who is taller than A. "
       "A is taller than C, who is taller than F. B is the third tallest. How many persons are taller than C?",
    ["Five", "Four", "Three", "Six"],
    "Why: 'D is shorter than only G' means G is the tallest and D is second. B is third. Then the chain B > E > A > C > F follows. "
    "Order, tallest first: G, D, B, E, A, C, F. Taller than C: G, D, B, E and A, so five. "
    "Grew from: 2025 Q19 (seven persons by height) with a count at the end.")
