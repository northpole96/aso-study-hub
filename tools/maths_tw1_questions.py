# Questions for the Time and Work set (14 questions, 15 minutes), made 18 Nov 2026 from the user's own list of
# 13 practice questions in 11 types (question 3 has two parts, so it becomes two questions).
# In every item the FIRST option is the right one (the builder shuffles options).
# t: the type number (used only to keep neighbours apart), id: name used by tools/check_maths_tw1.py,
# which recomputes every answer.
# Method used everywhere: work = 1 whole job; a person who takes n days does 1/n of the job a day.

Q = []
def add(t, id, q, o, e, c=False):
    Q.append(dict(s="Time & Work", t=t, id=id, q=q, o=o, e=e, k="one", n=False, c=c, a=None))

# ---------------------------------------------------------------- Type 1: working together
add(1, "together",
    "A can do a work in 12 days and B in 18 days. In how many days can they finish it together?",
    ["7 1/5 days", "15 days", "7 1/2 days", "6 days"],
    "Type 1 · Working together. In one day A does 1/12 of the work and B does 1/18. Together they do 1/12 + 1/18 = 3/36 + 2/36 = 5/36 of the work a day. "
    "So the whole work takes 36/5 = 7 1/5 days. "
    "Shortcut: together = (a × b)/(a + b) = (12 × 18)/30 = 7.2 days. "
    "Trap: 15 days is the average of 12 and 18. Two people working together must be faster than the faster one alone, so the answer must be less than 12.")
add(1, "bAlone",
    "A and B together finish a work in 10 days. A alone takes 15 days. How long will B alone take?",
    ["30 days", "5 days", "25 days", "12 1/2 days"],
    "Type 1 · Working together, turned round. Together they do 1/10 a day and A does 1/15. So B does 1/10 − 1/15 = 3/30 − 2/30 = 1/30 a day, and B alone takes 30 days. "
    "Shortcut: B = (a × t)/(a − t) = (15 × 10)/5 = 30. "
    "Trap: 5 days comes from 15 − 10. You can never subtract days; subtract the one-day work (the fractions).")

# ---------------------------------------------------------------- Type 2: pairs given
add(2, "pairsAll",
    "A and B can do a work in 12 days, B and C in 15 days, and C and A in 20 days. How long will A, B and C take working together?",
    ["10 days", "5 days", "15 2/3 days", "12 days"],
    "Type 2 · Pairs given. Add the three pairs: 1/12 + 1/15 + 1/20 = 5/60 + 4/60 + 3/60 = 12/60 = 1/5. "
    "Each person is counted twice in this sum (A is in A+B and in C+A), so 1/5 is the work of 2(A + B + C). "
    "Then A + B + C = 1/10 a day, and all three take 10 days. "
    "Trap: 5 days. That forgets to halve, which is the most common mistake in this type.")
add(2, "pairsA",
    "A and B can do a work in 12 days, B and C in 15 days, and C and A in 20 days. How long will A alone take?",
    ["30 days", "60 days", "20 days", "24 days"],
    "Type 2 · Pairs given, one person alone. First find all three together: (1/12 + 1/15 + 1/20) ÷ 2 = 1/10 a day. "
    "A alone = (all three) − (B and C) = 1/10 − 1/15 = 3/30 − 2/30 = 1/30. So A takes 30 days. "
    "Likely next: B alone = 1/10 − 1/20 = 1/20 (20 days) and C alone = 1/10 − 1/12 = 1/60 (60 days). That is why 20 and 60 sit in the options.")

# ---------------------------------------------------------------- Type 3: someone leaves
add(3, "leavesAfter",
    "A can do a work in 20 days and B in 30 days. They start together, but A leaves after 6 days. B finishes the rest. How many days does the whole work take?",
    ["21 days", "15 days", "18 days", "24 days"],
    "Type 3 · Someone leaves after some days. Together they do 1/20 + 1/30 = 5/60 = 1/12 a day. In 6 days they do 6/12 = 1/2 of the work. "
    "B does the other 1/2 alone at 1/30 a day, which takes 15 days. Whole work = 6 + 15 = 21 days. "
    "Trap: 15 days is only B's part. Read the question: it asks for the WHOLE work, so add the 6 days.")
add(3, "leavesBefore",
    "A can do a work in 10 days and B in 15 days. They start together, but A leaves 5 days before the work is finished. How many days does the work take in all?",
    ["9 days", "8 days", "11 days", "6 days"],
    "Type 3 · Someone leaves before the end. Here you do not know when A left, so call the whole time T days. "
    "B works all T days and does T/15. A works only (T − 5) days and does (T − 5)/10. Together they make the whole work: (T − 5)/10 + T/15 = 1. "
    "Multiply by 30: 3(T − 5) + 2T = 30, so 5T = 45 and T = 9 days. "
    "Easy trick: pretend A had stayed for those last 5 days. A would have done 5/10 = 1/2 more, so the two together would have done 1 + 1/2 = 3/2 work at 1/10 + 1/15 = 1/6 a day. Time = (3/2) ÷ (1/6) = 9 days.")

# ---------------------------------------------------------------- Type 4: efficiency
add(4, "efficient",
    "A is twice as efficient as B. Together they finish a work in 14 days. How long will A alone take?",
    ["21 days", "42 days", "28 days", "7 days"],
    "Type 4 · Efficiency. 'Twice as efficient' means A does twice as much work in a day as B. Give B 1 unit a day and A 2 units. Together they do 3 units a day. "
    "In 14 days they do 14 × 3 = 42 units, so the whole work is 42 units. A alone, at 2 units a day, takes 42/2 = 21 days. "
    "Trap: 42 days is B alone. And 28 = 2 × 14 doubles the wrong person. The more efficient worker always takes FEWER days.")

# ---------------------------------------------------------------- Type 5: alternate days
add(5, "alternate",
    "A can do a work in 10 days and B in 15 days. They work on alternate days, with A starting. In how many days is the work finished?",
    ["12 days", "6 days", "11 1/2 days", "13 days"],
    "Type 5 · Alternate days. Take the work as 30 units (the LCM of 10 and 15). A does 3 units a day and B does 2. "
    "One pair of days (A then B) does 5 units. 5 pairs = 10 days = 25 units, leaving 5. Day 11 is A's: 3 units, leaving 2. Day 12 is B's: exactly 2 units. Done in 12 days. "
    "Trap: 6 days is the time when both work together every day (30 ÷ 5). Always check the last part day by day; here it ends exactly at the end of day 12, so there is no half day.")

# ---------------------------------------------------------------- Type 6: sharing wages
add(6, "wages",
    "A can do a work in 6 days and B in 8 days. They are paid Rs. 3,200 for the job. With C's help, they finish it in 3 days. What is C's share?",
    ["Rs. 400", "Rs. 1,600", "Rs. 1,200", "Rs. 800"],
    "Type 6 · Sharing wages. Money is shared in the ratio of WORK DONE. In 3 days A does 3/6 = 1/2 of the work and B does 3/8. "
    "So C did 1 − 1/2 − 3/8 = 8/8 − 4/8 − 3/8 = 1/8 of the work, and C gets 1/8 of Rs. 3,200 = Rs. 400. "
    "Check: A gets Rs. 1,600 and B gets Rs. 1,200, and 1,600 + 1,200 + 400 = 3,200. "
    "Traps: Rs. 1,600 and Rs. 1,200 are A's and B's shares. Do not share by days taken; a faster worker earns more.")

# ---------------------------------------------------------------- Type 7: men and women
add(7, "menWomen",
    "4 men and 6 women finish a work in 8 days. 3 men and 7 women finish it in 10 days. How long will 10 women take to finish it?",
    ["40 days", "35 days", "50 days", "32 days"],
    "Type 7 · Men and women (two equations). Total work is the same both times, so 8(4m + 6w) = 10(3m + 7w), where m and w are one man's and one woman's day's work. "
    "That gives 32m + 48w = 30m + 70w, so 2m = 22w and 1 man = 11 women. "
    "Now change everyone into women: 4 men + 6 women = 44 + 6 = 50 women, who take 8 days. Work = 50 × 8 = 400 woman-days. 10 women take 400/10 = 40 days. "
    "Likely next: the same pair asking 'how long will 10 men take?' 10 men = 110 women, so 400/110 = 3 7/11 days.")

# ---------------------------------------------------------------- Type 8: men, hours, days
add(8, "mhd",
    "15 men working 8 hours a day dig a 120 m trench in 20 days. In how many days will 10 men working 6 hours a day dig a 60 m trench?",
    ["20 days", "10 days", "40 days", "15 days"],
    "Type 8 · Men, hours, days and amount of work. Use the formula (M₁ × H₁ × D₁)/W₁ = (M₂ × H₂ × D₂)/W₂. "
    "(15 × 8 × 20)/120 = (10 × 6 × D)/60, so 20 = D. The answer is 20 days. "
    "In words: fewer men and fewer hours make the job slower (×15/10 × 8/6 = 2 times longer), but the trench is half as long (× 1/2), so the two cancel. "
    "Trap: 40 days forgets that the trench is shorter; 10 days uses the length the wrong way up.")

# ---------------------------------------------------------------- Type 9: extra men to finish on time
add(9, "extraMen",
    "A contract must be finished in 40 days, and 60 men start work. After 25 days, only half the work is done. How many more men must be added to finish on time?",
    ["40", "100", "60", "30"],
    "Type 9 · Extra men to finish on time (the family of 2025 Q53). Half the work took 60 × 25 = 1,500 man-days, so the other half also needs 1,500 man-days. "
    "Only 40 − 25 = 15 days are left, so 1,500/15 = 100 men are needed. 60 are already there, so 40 MORE men must be added. "
    "Trap: 100 is the total needed, not the number to add. Read whether the question asks 'how many men' or 'how many more men'.")

# ---------------------------------------------------------------- Type 10: part done, then a helper joins
add(10, "helperJoins",
    "A does 3/5 of a work in 12 days. Then B joins him, and together they finish the rest in 3 days. How long would B alone take for the whole work?",
    ["12 days", "20 days", "15 days", "7 1/2 days"],
    "Type 10 · Part done, then a helper joins. A does 3/5 in 12 days, so A alone needs 12 × 5/3 = 20 days for the whole work (1/20 a day). "
    "The rest is 2/5, done by A and B in 3 days, so together they do 2/5 ÷ 3 = 2/15 a day. "
    "B alone = 2/15 − 1/20 = 8/60 − 3/60 = 5/60 = 1/12, so B takes 12 days. "
    "Trap: 20 days is A's time, and 7 1/2 days is A and B together.")

# ---------------------------------------------------------------- Type 11: pipe and leak
add(11, "pipeLeak",
    "Pipe A fills a tank in 12 hours. Pipe B empties it in 18 hours. Both are opened when the tank is half full. How long until the tank is full?",
    ["18 hours", "36 hours", "7 1/5 hours", "9 hours"],
    "Type 11 · Pipe and leak. An emptying pipe is a 'negative worker'. Each hour A fills 1/12 and B empties 1/18, so the net filling is 1/12 − 1/18 = 3/36 − 2/36 = 1/36 of the tank. "
    "Only half the tank is left to fill: (1/2) ÷ (1/36) = 18 hours. "
    "Traps: 36 hours fills the whole tank (it was already half full). 7 1/5 hours adds the pipes as if both were filling.")

assert len(Q) == 14, len(Q)
