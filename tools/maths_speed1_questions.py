# Questions for the Speed, Trains, Races and Boats set (26 questions, 26 minutes), made 18 Nov 2026.
# Family weight: 6 of the 50 maths questions in 2025 (Q54 cycle, Q59 train, Q60 km race, Q64 car, Q65 100 m race, Q82 train).
# In every item the FIRST option is the right one (the builder shuffles options).
# s: the four parts of the family (shown on the page and in the report), id: name used by tools/check_maths_speed1.py,
# which recomputes every answer. None repeats a Maths Mock 01 question (its train, car and race items are other angles).

Q = []
def add(s, id, q, o, e, c=False):
    Q.append(dict(s=s, t=s, id=id, q=q, o=o, e=e, k="one", n=False, c=c, a=None))

SP, TR, RA, BO = "Speed & Time", "Trains", "Races", "Boats & Streams"

# ================================================================ SPEED AND TIME
add(SP, "conv",
    "A train runs at 72 km/h. How many metres does it cover in 15 seconds?",
    ["300 m", "1,080 m", "270 m", "400 m"],
    "Type: changing units. To turn km/h into metres per second, multiply by 5/18 (because 1 km = 1,000 m and 1 hour = 3,600 s, and 1000/3600 = 5/18). "
    "72 × 5/18 = 20 m/s. In 15 seconds: 20 × 15 = 300 m. "
    "Trap: 1,080 is 72 × 15, which mixes km/h with seconds. Rule: before you multiply speed by time, make the units match. Going back, m/s × 18/5 gives km/h.")
add(SP, "late",
    "Walking at 4/5 of his usual speed, a man reaches his office 10 minutes late. What is his usual time for the journey?",
    ["40 minutes", "50 minutes", "30 minutes", "45 minutes"],
    "Type: slower speed, late arrival. For a fixed distance, time goes the opposite way to speed. If speed becomes 4/5, time becomes 5/4 of the usual time. "
    "The extra time is 5/4 − 1 = 1/4 of the usual time, and that is 10 minutes. So the usual time is 4 × 10 = 40 minutes. "
    "Trap: 50 minutes is the NEW (slow) time. Likely next: 'at 6/7 of his speed he is 12 minutes late' (extra = 1/6 of usual, so usual = 72 minutes).")
add(SP, "lateEarly",
    "A boy walks to school at 5 km/h and reaches 6 minutes late. If he walks at 6 km/h, he reaches 4 minutes early. How far is the school?",
    ["5 km", "6 km", "4 km", "3 km"],
    "Type: late at one speed, early at another. The two times differ by 6 + 4 = 10 minutes = 1/6 hour (late and early ADD, because the right time sits between them). "
    "So d/5 − d/6 = 1/6. The left side is d/30, so d/30 = 1/6 and d = 5 km. "
    "Shortcut: distance = (product of speeds ÷ difference of speeds) × time difference = (30 ÷ 1) × 1/6 = 5 km. "
    "Trap: subtracting 6 − 4 = 2 minutes instead of adding gives 1 km, which is why you must check whether both times are late, or one late and one early.")
add(SP, "cycle",
    "Ravi cycles to a town. At 12 km/h he reaches at 3 p.m.; at 18 km/h he reaches at 1 p.m. At what speed must he cycle to reach at 2 p.m.?",
    ["14.4 km/h", "15 km/h", "14 km/h", "13.5 km/h"],
    "Type: the 2025 Q54 family (Robert on his cycle). The two times differ by 2 hours, so d/12 − d/18 = 2. That is d/36 = 2, so d = 72 km. "
    "At 12 km/h the ride takes 72/12 = 6 hours, so he starts at 9 a.m. To reach at 2 p.m. he has 5 hours: 72/5 = 14.4 km/h. "
    "Trap: 15 km/h is the average of 12 and 18. The answer is never the plain average, because time, not speed, is split evenly.")
add(SP, "newSpeed",
    "A car covers a distance in 6 hours at 60 km/h. What speed does it need to cover the same distance in 4 1/2 hours?",
    ["80 km/h", "75 km/h", "90 km/h", "70 km/h"],
    "Type: same distance, new time (the 2025 Q64 family, the car and its 715 km). Distance = 60 × 6 = 360 km. New speed = 360 ÷ 4.5 = 80 km/h. "
    "Shortcut: speed and time go opposite ways, so new speed = 60 × 6/4.5 = 60 × 4/3 = 80. "
    "Likely next: 'to cover it in 3/4 of the time, by how much must the speed rise?' (by 1/3, that is 33 1/3%).")
add(SP, "ratioTime",
    "The speeds of A and B are in the ratio 3 : 4. A takes 30 minutes more than B to reach a place. How long does A take?",
    ["2 hours", "1 1/2 hours", "1 hour", "2 1/2 hours"],
    "Type: ratio of speeds. For the same distance, times are in the opposite ratio, so A : B time = 4 : 3. "
    "The difference of 1 part is 30 minutes, so A takes 4 parts = 120 minutes = 2 hours (and B takes 1 1/2 hours). "
    "Trap: 1 1/2 hours is B's time. Read which person the question asks about.")
add(SP, "avg2",
    "A man drives from A to B at 40 km/h and returns at 60 km/h. What is his average speed for the whole journey?",
    ["48 km/h", "50 km/h", "45 km/h", "52 km/h"],
    "Type: average speed, same distance both ways. Average speed is total distance ÷ total time, NOT the average of the speeds. "
    "Formula for two equal distances: 2xy/(x + y) = 2 × 40 × 60/100 = 48 km/h. "
    "Check with a distance of 120 km: 3 hours going, 2 hours back, so 240 km in 5 hours = 48 km/h. "
    "Trap: 50 km/h is the plain average. He spends MORE time at the slower speed, so the answer is always below the plain average.")
add(SP, "avg3",
    "A man covers three equal distances at 10 km/h, 20 km/h and 60 km/h. What is his average speed for the whole journey?",
    ["18 km/h", "30 km/h", "20 km/h", "24 km/h"],
    "Type: average speed, three equal distances. Take each part as 60 km (the LCM of 10, 20 and 60). Times: 6 h, 3 h and 1 h, so 180 km in 10 hours = 18 km/h. "
    "Formula: 3xyz/(xy + yz + zx) = 3 × 12,000/(200 + 1,200 + 600) = 36,000/2,000 = 18. "
    "Trap: 30 km/h is the plain average of 10, 20 and 60.")
add(SP, "avgParts",
    "A man walks 60 km. He covers the first 24 km at 6 km/h and the rest at 12 km/h. What is his average speed?",
    ["8 4/7 km/h", "9 km/h", "8 km/h", "10 km/h"],
    "Type: average speed, unequal parts. Time for 24 km at 6 km/h = 4 h. The rest is 36 km at 12 km/h = 3 h. Total: 60 km in 7 hours = 60/7 = 8 4/7 km/h. "
    "Trap: 9 km/h is the plain average of 6 and 12. Always go back to total distance ÷ total time.")
add(SP, "stoppage",
    "Without stoppages a bus runs at 54 km/h. With stoppages its average speed is 45 km/h. For how many minutes does the bus stop each hour?",
    ["10 minutes", "9 minutes", "12 minutes", "15 minutes"],
    "Type: stoppages. In one hour the bus loses 54 − 45 = 9 km because of stops. At its running speed, 9 km takes 9/54 hour = 1/6 hour = 10 minutes. "
    "Formula: stop time per hour = (difference ÷ speed without stops) × 60. "
    "Trap: 9 minutes treats the lost kilometres as minutes.")
add(SP, "meet",
    "Two towns P and Q are 310 km apart. A car leaves P at 8 a.m. towards Q at 40 km/h. Another leaves Q at 9 a.m. towards P at 50 km/h. When do they meet?",
    ["12 noon", "11:30 a.m.", "11 a.m.", "12:30 p.m."],
    "Type: moving towards each other. By 9 a.m. the first car has gone 40 km, so 270 km is left between them. "
    "Moving towards each other, the gap closes at 40 + 50 = 90 km/h (speeds ADD). Time = 270/90 = 3 hours after 9 a.m., so they meet at 12 noon. "
    "Trap: forgetting the first car's head start gives 310/90 ≈ 3.4 hours after 8 a.m., about 11:27. Likely next: how far from P do they meet? 40 × 4 = 160 km.")
add(SP, "chase",
    "A thief is seen by a policeman 200 m away. The thief runs at 10 km/h and the policeman chases at 12 km/h. How far will the thief have run before he is caught?",
    ["1 km", "1.2 km", "800 m", "600 m"],
    "Type: a chase, same direction. Speeds SUBTRACT: the gap of 200 m closes at 12 − 10 = 2 km/h. Time = 0.2 km ÷ 2 km/h = 0.1 hour = 6 minutes. "
    "In that time the thief runs 10 × 0.1 = 1 km. "
    "Trap: 1.2 km is how far the POLICEMAN runs (the thief's 1 km plus the 200 m gap).")

# ================================================================ TRAINS
add(TR, "pole",
    "A train 240 m long passes a pole in 16 seconds. What is its speed in km/h?",
    ["54 km/h", "15 km/h", "60 km/h", "48 km/h"],
    "Type: train and a pole (or a man standing, a tree, a signal post). The pole has no length, so the train covers only its own length. "
    "Speed = 240/16 = 15 m/s. Into km/h: 15 × 18/5 = 54 km/h. "
    "Trap: 15 is the answer in m/s. Always check which unit the options use.")
add(TR, "platform",
    "A train 180 m long running at 54 km/h crosses a platform in 20 seconds. How long is the platform?",
    ["120 m", "300 m", "180 m", "150 m"],
    "Type: train and a platform (or a bridge, a tunnel). To cross a platform the train covers its own length PLUS the platform's length. "
    "54 km/h = 15 m/s. In 20 s it covers 15 × 20 = 300 m. Platform = 300 − 180 = 120 m. "
    "Trap: 300 m is train + platform together.")
add(TR, "poleAndPlatform",
    "A train passes a pole in 15 seconds and a 100 m long platform in 25 seconds. What is the length of the train?",
    ["150 m", "100 m", "200 m", "250 m"],
    "Type: pole and platform together. The extra 10 seconds are spent covering the 100 m platform, so the speed is 100/10 = 10 m/s. "
    "In 15 seconds at 10 m/s the train covers its own length: 150 m. "
    "Algebra check: L/15 = (L + 100)/25 gives 25L = 15L + 1,500, so L = 150.")
add(TR, "manSame",
    "A train 125 m long passes a man running at 5 km/h in the same direction in 10 seconds. What is the speed of the train?",
    ["50 km/h", "45 km/h", "40 km/h", "55 km/h"],
    "Type: train and a moving man. Same direction, so speeds SUBTRACT: relative speed = 125/10 = 12.5 m/s = 12.5 × 18/5 = 45 km/h. "
    "That is (train − man), so train = 45 + 5 = 50 km/h. "
    "Trap: 45 km/h is only the relative speed. If the man ran TOWARDS the train, the train would be 45 − 5 = 40 km/h, which is the other trap.")
add(TR, "opposite",
    "Two trains 140 m and 160 m long run at 60 km/h and 48 km/h in opposite directions on parallel tracks. How long do they take to cross each other?",
    ["10 seconds", "90 seconds", "9 seconds", "12 seconds"],
    "Type: two trains, opposite directions. Distance = both lengths = 140 + 160 = 300 m. Opposite directions, so speeds ADD: 108 km/h = 108 × 5/18 = 30 m/s. "
    "Time = 300/30 = 10 seconds. "
    "Trap: 90 seconds uses the difference of speeds (12 km/h), which is the same-direction rule.")
add(TR, "sameDir",
    "Two trains 100 m and 150 m long run in the same direction at 72 km/h and 54 km/h. How long does the faster train take to pass the slower one completely?",
    ["50 seconds", "7 1/7 seconds", "20 seconds", "30 seconds"],
    "Type: two trains, same direction (overtaking). Distance = both lengths = 250 m. Same direction, so speeds SUBTRACT: 72 − 54 = 18 km/h = 5 m/s. "
    "Time = 250/5 = 50 seconds. "
    "Trap: 7 1/7 seconds adds the speeds (126 km/h = 35 m/s), which is the opposite-direction rule.")
add(TR, "afterMeet",
    "Two trains start at the same time from P and Q towards each other. After they meet, they take 9 hours and 16 hours to reach Q and P respectively. What is the ratio of their speeds?",
    ["4 : 3", "3 : 4", "16 : 9", "9 : 16"],
    "Type: times after meeting. Rule: speed of first : speed of second = √(time of second after meeting) : √(time of first after meeting). "
    "Here: √16 : √9 = 4 : 3. "
    "Sense check: the train from P needs only 9 more hours, less than the other, so it must be the faster one. That rules out 3 : 4. "
    "Traps: 16 : 9 forgets the square root, and 9 : 16 forgets both the root and the swap.")

# ================================================================ RACES
add(RA, "chainBeat",
    "In a 1 km race, A beats B by 100 m, and B beats C by 100 m. By how many metres does A beat C?",
    ["190 m", "200 m", "180 m", "210 m"],
    "Type: one runner beats another, chained (the 2025 Q60 family, 'in a km race A beats B by...'). "
    "When A runs 1,000 m, B runs 900 m. When B runs 1,000 m, C runs 900 m, so when B runs 900 m, C runs 900 × 900/1,000 = 810 m. "
    "So when A finishes, C has run 810 m and A beats C by 190 m. "
    "Trap: 200 m just adds the two leads. The second lead shrinks because B has not finished when A does.")
add(RA, "startGiven",
    "A runs 1 2/3 times as fast as B. If A gives B a start of 80 m, how far from the start must the winning post be so that both reach it at the same time?",
    ["200 m", "160 m", "240 m", "120 m"],
    "Type: a start (head start) given. Speeds A : B = 5/3 : 1 = 5 : 3, so in the same time they cover distances in the ratio 5 : 3. "
    "A runs 80 m more than B, and the difference is 5 − 3 = 2 parts. So 1 part = 40 m and A runs 5 parts = 200 m. "
    "Trap: 120 m is how far B runs (3 parts).")
add(RA, "startBeat",
    "In a 200 m race, A runs at 18 km/h. A gives B a start of 20 m and still beats him by 5 seconds. What is B's speed?",
    ["14.4 km/h", "15 km/h", "16 km/h", "12 km/h"],
    "Type: start given AND a win by time (the 2025 Q65 family, the 100 m race at 8 km/h). 18 km/h = 5 m/s, so A finishes 200 m in 40 seconds. "
    "B runs only 180 m and takes 40 + 5 = 45 seconds. B's speed = 180/45 = 4 m/s = 4 × 18/5 = 14.4 km/h. "
    "Trap: forgetting the start gives 200/45 m/s = 16 km/h.")
add(RA, "circle",
    "A and B start running together from the same point on a 600 m circular track, at 5 m/s and 3 m/s, in the same direction. After how long do they first meet?",
    ["5 minutes", "75 seconds", "2 minutes", "10 minutes"],
    "Type: circular track. In the same direction they meet when the faster gains one full lap, 600 m, on the slower. It gains 5 − 3 = 2 m each second, so 600/2 = 300 seconds = 5 minutes. "
    "Trap: 75 seconds is the opposite-direction answer (speeds add: 600/8). "
    "Likely next: 'when will they next be together at the STARTING point?' A takes 120 s a lap and B 200 s, so the LCM: 600 s = 10 minutes.")

# ================================================================ BOATS AND STREAMS
add(BO, "boatBasic",
    "A boat goes 30 km downstream in 2 hours and 18 km upstream in 2 hours. What is the speed of the boat in still water?",
    ["12 km/h", "3 km/h", "15 km/h", "24 km/h"],
    "Type: boat basics. Downstream (with the water) speed = boat + stream = 30/2 = 15 km/h. Upstream (against the water) = boat − stream = 18/2 = 9 km/h. "
    "Boat = half the SUM = (15 + 9)/2 = 12 km/h. Stream = half the DIFFERENCE = (15 − 9)/2 = 3 km/h. "
    "Trap: 3 km/h is the stream's speed, and 15 km/h is the downstream speed.")
add(BO, "boatRatio",
    "A man takes twice as long to row a distance upstream as to row the same distance downstream. If the stream flows at 4 km/h, what is his speed in still water?",
    ["12 km/h", "8 km/h", "16 km/h", "6 km/h"],
    "Type: ratio of times. Twice the time upstream means downstream speed is twice the upstream speed: b + 4 = 2(b − 4). "
    "So b + 4 = 2b − 8, and b = 12 km/h. "
    "Shortcut: if upstream takes n times as long, boat : stream = (n + 1) : (n − 1) = 3 : 1 here, so the boat is 3 × 4 = 12. "
    "Trap: 8 km/h is the upstream speed.")
add(BO, "boatRound",
    "A boat's speed in still water is 10 km/h and the stream flows at 2 km/h. The boat goes to a place and comes back in 25 hours. How far is the place?",
    ["120 km", "125 km", "100 km", "150 km"],
    "Type: there and back. Downstream speed = 12 km/h and upstream = 8 km/h. So d/12 + d/8 = 25. "
    "Over 24: (2d + 3d)/24 = 25, so 5d = 600 and d = 120 km. "
    "Check: 10 hours going down, 15 hours coming up, 25 hours in all. "
    "Trap: 125 km uses the still-water speed both ways (25 × 10 ÷ 2).")

assert len(Q) == 26, len(Q)
