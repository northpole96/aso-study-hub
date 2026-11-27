# English Mock 09 · full Paper III (English) on the 2021 layout, written with the aso-mock skill (27 Nov 2026).
# User: "english full paper mock 100 question hard".
# Plan: python3 .claude/skills/aso-mock/scripts/draw.py english --n 100 --seed 577244 (families, counts and the three exact repeats).
# Level: hard (close options, two-way words such as look/hard/enough/but/before, traps that look natural), still one rule per question.
# First option is the right one unless a is given (then the options stay in the printed order).

META = dict(
    paper="english",
    title="ASO English Mock 09",
    hub_title="English Mock 09",
    masthead="English Mock 09",
    heading="English Paper III · Mock 09",
    tagline="100 <b>hard</b> questions on the <b>2021 layout</b>,<br>with close options and natural-looking traps.",
    key="aso-english-mock-2027-9",
    code="M09",
    out="ASO-English-Mock-Test-2027-9.html",
    minutes=45,
    seed=20261127,
    order="given",
    date="27 Nov 2026",
    draw="python3 .claude/skills/aso-mock/scripts/draw.py english --n 100 --seed 577244",
    intro=[
        "This full English paper (45 minutes) follows the 2021 booklet. It opens with a mixed grammar block of twenty, "
        "then six parts of speech, eight pick-the-correct-sentence and spot-the-error questions, six mixed questions, "
        "sixteen vocabulary questions, ten prepositions, ten articles, five tenses, four rearrangements, "
        "ten agreement questions and one reading passage.",
        "The level is hard. Many options are close, and several words change their part of speech with their place "
        "(look, hard, enough, but, before). Each question still tests one rule. Three are exact past questions: "
        "2021 Q13 (had never been), 2021 Q46 (SUBVERSION) and 2025 Q42 (focuses on). The passage is about the sea "
        "taking the coastal villages of Satabhaya in Kendrapara.",
    ],
)

Q = []
def add(s, q, o, e, k="one", n=False, c=False, a=None, **x):
    d = dict(s=s, q=q, o=o, e=e, k=k, n=n, c=c, a=a); d.update(x); Q.append(d)

V, T, SV, P, AD, AR, VB, ER, SY, AN, CO, RE, PS = ("Vocabulary", "Tenses", "Subject–verb agreement", "Preposition", "Adverb",
    "Articles", "Verb", "Error spotting", "Synonyms", "Antonyms", "Comprehension", "Sentence rearrangement", "Parts of speech")
NA = "No article"
IMP = "Choose how the part in brackets can be improved. If no change is needed, choose 'No improvement'.\n"

# ================================================================ Block 1 · mixed grammar opener (20)
add(VB, "Looking back on his life, the old clerk deeply regretted ____ school after Class 8, because he could never rise to a better post.",
    ["leaving", "to leave", "leave", "to leaving"],
    "Regret + -ing means being sorry about something already done (he left school long ago). Regret + to-infinitive is for something you are about to say or do: "
    "'We regret to inform you that…'. The clue is 'looking back'. Grew from the 2025 verb-form questions (gerund or infinitive after a verb).")
add(P, "The new government has promised to ____ the old system of paper permits and issue every licence online.",
    ["do away with", "do away from", "do away of", "do up with"],
    "'Do away with' means abolish or put an end to. The phrasal verb has two particles, 'away' and 'with', and neither can be changed. "
    "Grew from 2021 and 2025 phrasal verbs (turned out, take to heart, called for).")
add(T, "If you had taken the medicine on time yesterday, you ____ much better today.",
    ["would feel", "would have felt", "will feel", "had felt"],
    "A mixed conditional: the condition is in the past (had taken … yesterday) but the result is in the present (today), so the result takes would + base verb. "
    "'Would have felt' is for a result in the past. The time words decide. Grew from 2025 conditionals (type 2 and type 3).")
add(AD, "Only when the lights came back on ____ how much damage the storm had done to the hall.",
    ["did we see", "we saw", "we did see", "saw we"],
    "A sentence that opens with 'Only when', 'Only after', 'Not until' or 'Never' puts the helping verb before the subject in the main clause: did we see. "
    "'Saw we' moves the main verb, which English does not allow. Grew from the four inversion openers of 2025 (Rarely does, Never before had).")
add(ER, "Choose how the sentence can be improved: She was uneasy because she (never be) on a plane before.",
    ["had never been", "never been", "is never been", "No improvement"],
    "Exact past question (2021 Q13). Her experience up to that past moment needs the past perfect: had never been. 'Before' and 'was uneasy' place it in the past. "
    "The family: earlier of two past times takes had + past participle.", a=0, src="2021 Q13")
add(VB, "Choose the correct passive form: People say that the old banyan tree is three hundred years old.",
    ["The old banyan tree is said to be three hundred years old.", "The old banyan tree is said to have been three hundred years old.",
     "The old banyan tree was said that it is three hundred years old.", "It is said by people the old banyan tree is three hundred years old."],
    "'People say that X is …' becomes 'X is said to be …'. The present 'is' becomes the present infinitive 'to be'; 'to have been' would put the age in the past. "
    "Grew from the voice questions of 2018 and 2021 ('everyone understands English').")
add(AD, "The night guard looked ____ at the stranger who was standing near the bank's locked gate at midnight.",
    ["suspiciously", "suspicious", "suspicion", "more suspicious"],
    "'Look at' is an action (using the eyes), so it takes an adverb: looked suspiciously at him. 'He looked suspicious' (he seemed so) would take an adjective, "
    "because there 'look' is a linking verb like seem. The word 'at' shows the action. Grew from 2025 adjective-or-adverb questions.")
add(P, "The new rule on late fees is not applicable ____ students who have already paid for the whole year.",
    ["to", "for", "on", "with"],
    "We say 'applicable to', 'relevant to', 'suitable for'. 'Applicable for' is a common mistake. Adjective + preposition pairs are learnt as pairs. "
    "Grew from the 2018 and 2021 fixed prepositions (different from, according to, based on).")
add(VB, "You ____ to have told the police at once; by keeping quiet you only made matters worse.",
    ["ought", "should", "must", "had better"],
    "Only 'ought' is followed by 'to'. 'Should have told', 'must have told' and 'had better tell' take no 'to'. 'Ought to have + past participle' blames a missed duty in the past. "
    "Grew from 2021 Q2 (modals of duty).")
add(ER, IMP + "The more you practise speaking in public, (the less nervous you will feel) on the stage.",
    ["less nervous you will feel", "the lesser nervous you will feel", "the less nervous will you feel", "No improvement"],
    "The sentence is correct. 'The more …, the less …' needs 'the' in both halves, the plain comparative 'less' (not 'lesser'), and normal word order (you will feel). "
    "A hard paper always has a few sentences that need no change. Grew from the 2021 sentence improvement block (Q12–16).", a=3)
add(T, "When we returned from the fair late at night, we found that our house ____ into by thieves.",
    ["had been broken", "was broken", "has been broken", "had broken"],
    "Two past actions: the thieves broke in first, we found it later. The earlier one takes the past perfect, and the house did not do the breaking, so it is passive: had been broken into. "
    "'Had broken' is active and wrong. Grew from the 2025 past-perfect questions.")
add(VB, "I would rather you ____ this matter to anyone until the enquiry is over.",
    ["did not mention", "do not mention", "not mention", "had not mentioned"],
    "'Would rather' + another person + past simple speaks of the present or future: I would rather you did not mention it. "
    "'Had not mentioned' would be a regret about the past, but 'until the enquiry is over' points to the future. Grew from the would-rather family (2018).")
add(P, "The young officer was blamed ____ the delay, although he was not responsible ____ it, and the enquiry later cleared him ____ all charges.",
    ["for, for, of", "of, for, from", "for, to, of", "on, with, from"],
    "Blamed for a fault, responsible for a thing, cleared of a charge (also accused of, acquitted of). One sentence, three pairs: the 2018 and 2021 multi-blank style ('in his honour … invited to it').")
add(ER, IMP + "The reason why he failed the test (is because) he did not read the questions carefully.",
    ["was because", "is that", "is due to", "No improvement"],
    "'The reason … is because' says the same thing twice. After 'the reason' use 'that': The reason is that he did not read. "
    "'Is due to' cannot be followed by a full clause (he did not read). Grew from 2021 sentence improvement ('because of they dislike').", a=1)
add(VB, "Halfway up the steep hill, the old pilgrim stopped ____ his breath, and then walked on slowly to the temple.",
    ["to catch", "catching", "catch", "to catching"],
    "Stop + to-infinitive = stop in order to do something (he stopped so that he could rest). Stop + -ing = no longer do it. "
    "'Stopped catching his breath' would mean he gave up breathing. Grew from 2025 gerund-or-infinitive questions.")
add(AD, "The farmers worked ____ all through the summer, so no one was surprised when they had a rich harvest.",
    ["hard", "hardly", "hardily", "hardness"],
    "'Hard' is both an adjective and an adverb (work hard). 'Hardly' means 'almost not', which is the opposite of the sense here. "
    "Same trap: late / lately, near / nearly, high / highly. Grew from 2025 adjective-or-adverb questions.")
add(ER, IMP + "(Though he is poor, but) he never takes help from anyone in the village.",
    ["Although he is poor, but", "Despite he is poor,", "Though he is poor,", "No improvement"],
    "'Though' and 'but' both join the two parts, so using both is a double joining. Keep one: Though he is poor, he never takes help. "
    "'Despite' must be followed by a noun or -ing (despite being poor). Grew from 2021 sentence improvement.", a=2)
add(P, "As the chief guest was in a hurry, the organisers decided to dispense ____ the usual speeches and began the prize distribution at once.",
    ["with", "of", "off", "from"],
    "'Dispense with' means do without or leave out. Verb + preposition pairs like this (part with, dispense with, comply with) are fixed. "
    "Grew from 2025 Q42 and the verb + preposition family.")
add(VB, "The accused denied ____ anywhere near the bank on the night of the robbery.",
    ["having been", "to have been", "to be", "have been"],
    "'Deny' is followed by the -ing form, never by to. Since the act was in the past, the perfect gerund 'having been' is the best choice. "
    "Same group: admit, avoid, mind, risk. Grew from 2025 verb-form questions (denied having been is an open angle).")
add(ER, IMP + "(Unless you do not apply) before Friday, you will lose your seat in the hostel.",
    ["Unless you apply", "If you apply", "Unless you will apply", "No improvement"],
    "'Unless' already means 'if not', so 'unless … not' is a double negative. 'If you apply' turns the meaning round (you would lose the seat by applying). "
    "No 'will' after unless or if. Grew from 2021 sentence improvement and the 2025 conditional row.", a=0)

# ================================================================ Block 2 · parts of speech (6)
POS = "Choose the correct part of speech for the word in bracket:\n"
add(PS, POS + "Please put (that) bag on the top shelf before the guests arrive.",
    ["Adjective", "Pronoun", "Conjunction", "Adverb"],
    "'That' stands before a noun (bag) and points it out, so it is a demonstrative adjective. In 'That is my bag' it stands alone and is a pronoun; "
    "in 'He said that he was late' it joins and is a conjunction. Grew from 2021 Q17–22.")
add(PS, POS + "I am sure I have met this gentleman somewhere (before).",
    ["Adverb", "Preposition", "Conjunction", "Adjective"],
    "With nothing after it, 'before' tells when and modifies the verb (have met): an adverb. 'Before lunch' would make it a preposition; "
    "'before he came' a conjunction. Grew from 2021 Q18 ('for' as preposition).")
add(PS, POS + "In summer the farmers (water) their fields twice a week.",
    ["Verb", "Noun", "Adjective", "Adverb"],
    "Here 'water' is the action the farmers do, so it is a verb. A word's job in the sentence decides its part of speech, not the word itself. "
    "Grew from 2021 Q21 (liar = noun) and the 'noun used as a verb' angle.")
add(PS, POS + "The boy is not tall (enough) to reach the top shelf.",
    ["Adverb", "Adjective", "Noun", "Pronoun"],
    "'Enough' after an adjective (tall enough) tells how tall, so it modifies the adjective: an adverb. Before a noun (enough money) it is an adjective. "
    "Grew from 2021 Q19 (costly looks like an adverb but is an adjective).")
add(PS, POS + "All (but) one of the students passed the final examination.",
    ["Preposition", "Conjunction", "Adverb", "Adjective"],
    "Here 'but' means 'except' and stands before 'one', so it is a preposition. In 'He is poor but honest' it joins two words and is a conjunction. "
    "Grew from 2021 Q17 (as well as = conjunction).")
add(PS, POS + "(Seeing) the police at the gate, the thief ran out through the back door.",
    ["Participle", "Gerund", "Infinitive", "Verb"],
    "'Seeing the police' describes the thief (the thief, seeing the police, ran), so it works like an adjective: a participle. "
    "An -ing word that works as a noun ('Seeing is believing') is a gerund. Grew from 2021 Q20 (drowning man).")

# ================================================================ Block 3 · pick the correct sentence, spot the error (8)
PICK = "Choose the grammatically correct sentence:"
add(ER, PICK,
    ["The climate of Puri is milder than that of Bhubaneswar.", "The climate of Puri is milder than Bhubaneswar.",
     "The climate of Puri is milder than those of Bhubaneswar.", "The climate of Puri is more milder than that of Bhubaneswar."],
    "We compare climate with climate, not climate with a city, so 'that of Bhubaneswar' is needed ('those of' for a plural). 'More milder' is a double comparative. "
    "Grew from 2021 pick-the-correct-sentence questions.")
add(ER, PICK,
    ["The man who I thought was honest cheated me.", "The man whom I thought was honest cheated me.",
     "The man which I thought was honest cheated me.", "The man who I thought he was honest cheated me."],
    "'I thought' is only a small inserted clause. Take it out: 'The man who was honest'. The relative word is the subject of 'was', so it must be 'who', not 'whom'. "
    "A classic hard trap. Grew from 2021 pick-correct questions.")
add(ER, PICK,
    ["Walk carefully lest you should fall.", "Walk carefully lest you should not fall.",
     "Walk carefully lest you will fall.", "Walk carefully lest you may not fall."],
    "'Lest' means 'so that … not', so it never takes another 'not', and it is followed by 'should'. Grew from 2021 pick-correct questions.")
add(ER, PICK,
    ["She is both clever and hardworking.", "She is both clever as well as hardworking.",
     "She is both clever and also hardworking.", "She is clever both and hardworking."],
    "'Both' pairs only with 'and', and 'both' stands just before the first of the two words. 'Both … as well as' mixes two joiners. "
    "Grew from 2021 pick-correct questions and 2018 Q7 (as well as).")
add(ER, PICK,
    ["He is as tall as, if not taller than, his brother.", "He is as tall, if not taller than, his brother.",
     "He is as tall as, if not taller, his brother.", "He is tall as, if not taller than, his brother."],
    "Each half must be complete on its own: 'as tall as his brother' and 'taller than his brother'. Only the first sentence keeps both 'as … as' and 'than'. "
    "Grew from 2021 pick-correct questions and the degree family of 2025.")
add(ER, PICK,
    ["The boy resembles his father in every way.", "The boy resembles with his father in every way.",
     "The boy is resembling his father in every way.", "The boy resembles to his father in every way."],
    "'Resemble' takes its object directly, with no preposition (like discuss, reach, enter). It is a state verb, so it is not used in the continuous form. "
    "Grew from 2021 pick-correct questions.")
SEG = "Identify the incorrect segment in the sentence below:\n"
add(ER, SEG + "[Not only did he] [lost his money] [but also] [his good name.]",
    ["Not only did he", "lost his money", "but also", "his good name."],
    "After 'did', the verb goes back to its base form: did he lose, not did he lost. The inversion after 'Not only' is right. "
    "Grew from 2025 error spotting ('Not only does … made').", a=1)
add(ER, SEG + "[The scenery of] [the Koraput hills] [are charming] [during the monsoon.]",
    ["The scenery of", "the Koraput hills", "are charming", "during the monsoon."],
    "The subject is 'scenery', an uncountable noun that takes a singular verb: is charming. The plural 'hills' after 'of' does not change the verb. "
    "Grew from the 2025 error-spotting rows ('rules has', 'committee are').", a=2)

# ================================================================ Block 4 · mixed tenses, agreement, adverbs (6)
add(T, "Ravi and Sunil ____ each other for ten years when they decided to start a business together.",
    ["had known", "have known", "knew", "were knowing"],
    "The knowing ran up to a past moment (when they decided), so it takes the past perfect: had known … for ten years. 'Know' is a state verb and is not used in -ing forms. "
    "Grew from 2025 past-perfect questions ('had known each other for a decade').")
add(SV, "The pair of shoes that I bought at the fair last week ____ already too tight for me.",
    ["is", "are", "were", "have been"],
    "The subject is 'pair', which is singular: the pair … is. 'Shoes' alone would take 'are'. The words in between (that I bought…) do not change it. "
    "Grew from 2021 agreement questions (pair of).")
add(AD, "We need ____ information about the scheme before we can fill in the form.",
    ["further", "farther", "more far", "furthest"],
    "'Further' means more or additional (further information, further help). 'Farther' is only for real distance. 'More far' is not used. "
    "Grew from 2025 degree questions (irregular comparisons).")
add(T, "By the time you receive this letter, I ____ for Mumbai.",
    ["will have left", "will leave", "would have left", "have left"],
    "'By the time' + a future event: the other action will be complete before it, so use the future perfect, will have left. "
    "'By the time you receive' is present in form but future in meaning. Grew from 2025 future-tense questions.")
add(SV, "Each and every member of the two clubs ____ a right to vote at the meeting.",
    ["has", "have", "are having", "were having"],
    "'Each and every' takes a singular verb, even when a plural noun (clubs) comes later. 'Have' in the sense of own is a state verb and has no -ing form here. "
    "Grew from 2021 and 2025 each/every questions.")
add(AD, "The milk had turned ____ because it was left outside in the heat all afternoon.",
    ["sour", "sourly", "sourness", "soured"],
    "'Turn' here means 'become', a linking verb, so it is followed by an adjective that describes the milk: turned sour. Same with grow, become, seem, look. "
    "Grew from 2025 adjective-or-adverb questions (felt tired, looked dull).")

# ================================================================ Block 5 · vocabulary (16): synonyms 6, antonyms 5, words in a sentence 5
SYB = "Choose the word closest in meaning to the word in bracket:\n"
add(SY, SYB + "The minister's (cryptic) reply left the reporters wondering what he really meant.",
    ["mysterious", "angry", "polite", "honest"],
    "Cryptic = having a hidden or puzzling meaning, so mysterious. The clue is 'wondering what he really meant'. Grew from 2021 Q41–42 (word in bracket).")
add(SY, SYB + "The (incessant) rain of the last three days has flooded the low-lying parts of the town.",
    ["unceasing", "heavy", "sudden", "seasonal"],
    "Incessant = going on without stopping. 'Heavy' is tempting, but the word is about time (three days without a break), not strength. Grew from 2021 Q41–42.")
add(SY, SYB + "The court said that it would not waste its time on such (frivolous) complaints.",
    ["trivial", "serious", "false", "angry"],
    "Frivolous = not serious, silly or trivial. 'False' is tempting, but a frivolous complaint may be true and still not worth the court's time. Grew from 2021 Q41–42.")
add(SY, "Choose the word most similar in meaning to AMELIORATE:",
    ["Improve", "Worsen", "Measure", "Accept"],
    "Ameliorate = make a bad situation better (ameliorate the condition of the poor). 'Worsen' is its opposite. Grew from 2021 Q43 (veracity).")
add(SY, "Select the pair of synonyms:\n(I) Diligent (II) Careless (III) Industrious (IV) Idle",
    ["(I) and (III)", "(II) and (IV)", "(I) and (II)", "(III) and (IV)"],
    "Diligent and industrious both mean hardworking. Careless and idle are both faults, but they do not mean the same thing (one is about attention, the other about work). "
    "Grew from the 2021 pick-the-pair question.")
add(SY, "Choose the word most similar in meaning to AUDACIOUS:",
    ["Bold", "Loud", "Clever", "Cruel"],
    "Audacious = daring, bold, ready to take risks (an audacious plan). It has nothing to do with noise. Grew from 2021 Q43.")
add(AN, "Choose the word most opposite in meaning to SUBVERSION:",
    ["Compliance", "Destabilisation", "Clarity", "Sanity"],
    "Exact past question (2021 Q46). Subversion is the undermining of authority; its opposite is obeying it: compliance. Destabilisation is close to a synonym.",
    src="2021 Q46")
add(AN, "Choose the word most opposite in meaning to ADVERSITY:",
    ["Prosperity", "Misfortune", "Hardship", "Courage"],
    "Adversity = hard times, misfortune. Its opposite is prosperity (good fortune). Misfortune and hardship are synonyms, the usual trap. "
    "Grew from the four antonyms of 2021 (military, embrace, subversion, sinister).")
add(AN, "Choose the word most opposite in meaning to AFFLUENT:",
    ["Impoverished", "Prosperous", "Influential", "Generous"],
    "Affluent = rich. Impoverished = made poor. 'Influential' sounds like 'affluent' but means powerful. Grew from the 2021 antonyms.")
add(AN, "Choose the word most opposite in meaning to PROFOUND:",
    ["Superficial", "Deep", "Serious", "Difficult"],
    "Profound = deep (profound knowledge, profound sorrow). Its opposite is superficial, which means only on the surface. Grew from the 2021 antonyms.")
add(AN, "Choose the word most opposite in meaning to ZEAL:",
    ["Apathy", "Passion", "Anger", "Courage"],
    "Zeal = great energy and eagerness for a cause. Apathy = lack of interest or feeling. Passion is a synonym. Grew from the 2021 antonyms.")
add(V, "The stranger's ____ manner (whispering, glancing around and hiding his face) made the shopkeeper call the police.",
    ["furtive", "candid", "cheerful", "careless"],
    "Furtive = secret and sly, as if hiding something. The clues in the brackets all point to hiding. Grew from the 2025 one-blank vocabulary questions (unwelcoming air → sullen).")
add(V, "The old fort, once full of soldiers and traders, now stands ____; only bats and pigeons live in its empty halls.",
    ["desolate", "crowded", "renovated", "festive"],
    "Desolate = empty and lonely. 'Once full … now' sets up a contrast, and 'empty halls' confirms it. Grew from the 2025 one-blank vocabulary questions.")
add(V, "The speech was so ____ that the listeners, who had expected a long lecture, were pleased when the speaker finished in five minutes.",
    ["succinct", "verbose", "eloquent", "hesitant"],
    "Succinct = brief and clear. 'Eloquent' (fluent and moving) is tempting, but the clue is the five minutes, which is about length. "
    "Verbose is the opposite. Grew from the 2025 one-blank vocabulary questions (lucid, meticulously).")
add(V, "Unlike his ____ elder brother, who never asked a single question in class, Rahul wanted to know the reason behind everything.",
    ["incurious", "inquisitive", "argumentative", "ambitious"],
    "'Unlike' signals a contrast. Rahul is curious, so the brother must be the opposite: incurious. 'Inquisitive' describes Rahul, not the brother. "
    "Grew from the 2025 contrast-clue question ('unlike the pessimism of his brothers' → optimistic).")
add(V, "In which sentence is the word 'board' used to mean 'a group of people who manage an organisation'?",
    ["The board of the bank met to choose a new chairman.", "The teacher wrote the date on the board.",
     "We went on board the ship at Paradip.", "The hostel charges for room and board."],
    "A board of directors is a group that manages. 'On the board' is a flat surface, 'on board' means on a ship, and 'room and board' means meals. "
    "Grew from 2018 word-meaning questions (a word with many meanings: bar).")

# ================================================================ Block 6 · prepositions (10)
add(P, "The study focuses ____ the relationship between diet and mental health.",
    ["on", "in", "at", "with"],
    "Exact past question (2025 Q42). Focus on, concentrate on, emphasis on. Family: verb + preposition (lies in, arrived at, confide in).", src="2025 Q42")
add(P, "____ the coming elections, the government has cancelled the leave of all its officers.",
    ["In view of", "In spite of", "Instead of", "In place of"],
    "'In view of' = because of something expected or present. The officers are needed for the elections, so their leave is cancelled. 'In spite of' would need a contrast. "
    "Grew from 2021 phrase prepositions (according to, based on).")
add(P, "He was born ____ the morning of 2 October in a small village near Cuttack.",
    ["on", "in", "at", "by"],
    "We say 'in the morning', but 'on the morning of' a particular date, because a date takes 'on'. Grew from the time prepositions of 2021 and 2025 (in June, on Monday).")
add(P, "She is very proficient ____ Sanskrit as well as Odia, and often translates old texts for the museum.",
    ["in", "at", "with", "on"],
    "Proficient in (a skill or language), like skilled in. 'Good at' takes 'at', which is why 'at' is the trap. Grew from the 2018 and 2021 adjective + preposition pairs.")
add(P, "Because orders have fallen, the factory has had to ____ fifty of its workers until the new season.",
    ["lay off", "lay out", "lay down", "lay by"],
    "Lay off = stop employing workers for a time because there is no work. Lay out = arrange or spend; lay down = put down or make a rule. "
    "Grew from 2021 and 2025 phrasal verbs.")
add(P, "The match was postponed ____ the heavy rain that had flooded the ground since morning.",
    ["owing to", "in spite of", "instead of", "on behalf of"],
    "'Owing to' gives the cause (because of). 'In spite of' would mean the match went ahead. Grew from 2021 phrase prepositions.")
add(P, "The rich merchant refused to part ____ even a single coin for the repair of the village temple.",
    ["with", "from", "off", "away"],
    "Part with = give away something you own. Part from = leave a person ('She parted from her friends'). Grew from the verb + preposition family (2025 Q42).")
add(P, "The shop will stay open ____ nine o'clock tonight; after that the owner will lock it and go home.",
    ["until", "by", "since", "for"],
    "'Until' shows that an action goes on up to a time (stay open until nine). 'By' means 'not later than' and suits one finished act (finish it by nine). "
    "Grew from 2021 time prepositions (wait until Saturday).")
add(P, "The officer was accused of being partial ____ his own relatives when he gave out the contracts.",
    ["to", "for", "with", "on"],
    "Partial to = favouring someone unfairly. Grew from the 2018 and 2021 adjective + preposition pairs.")
add(P, "The frightened child clung ____ his mother's saree and would not let go.",
    ["to", "on", "with", "at"],
    "Cling to (past: clung to) = hold tightly. Same as stick to, hold on to. Grew from the verb + preposition family.")

# ================================================================ Block 7 · articles (10)
add(AR, "In recognition of his service, he was made ____ honorary member of the club.",
    ["an", "a", "the", NA],
    "The 'h' in 'honorary' is silent, so the word begins with a vowel sound: an honorary. Same with hour, honest, heir. Grew from the 2021 and 2025 a/an questions (an honour).")
add(AR, "The victim lodged ____ FIR at the nearest police station the same night.",
    ["an", "a", "the", NA],
    "F is read 'ef', which begins with a vowel sound, so 'an FIR'. Letters F, H, L, M, N, R, S, X take 'an' (an MP, an SP). Grew from 2021 and 2025 a/an questions (an MLA).")
add(AR, "The driver took ____ U-turn in the middle of the busy road and was fined by the traffic police.",
    ["a", "an", "the", NA],
    "U is read 'you', which begins with a consonant sound (y), so 'a U-turn', like a university, a union. Grew from the 2021 and 2025 a/an questions (a unique).")
add(AR, "The doctor asked for ____ X-ray of the injured man's chest before the operation.",
    ["an", "a", "the", NA],
    "X is read 'eks', a vowel sound, so 'an X-ray'. The spelling begins with a consonant letter, but the sound decides. Grew from the a/an family.")
add(AR, "My grandfather reads ____ Samaja every morning with his first cup of tea.",
    ["the", "a", "an", NA],
    "Names of newspapers take 'the': the Samaja, the Hindu, the Times of India. Grew from the 2021 and 2025 'the' questions (rivers, forests, the police).")
add(AR, "Amsterdam is the capital of ____ Netherlands.",
    ["the", "a", "an", NA],
    "Most country names take no article, but a few plural or 'group' names take 'the': the Netherlands, the Philippines, the United States. "
    "Grew from the 'the' family of 2021 and 2025.")
add(AR, "The government runs special schools for ____ blind in every district.",
    ["the", "a", "an", NA],
    "The + adjective names a whole group of people: the blind, the poor, the old. It takes a plural verb. Grew from the 'the' family.")
add(AR, "Rina is ____ only girl from our village who has played hockey for the state.",
    ["the", "a", "an", NA],
    "'Only' (like 'same' and the superlatives) points to one particular person, so it takes 'the': the only girl. Grew from the 'the' family (superlatives).")
add(AR, "____ man is the only animal that cooks its food.",
    [NA, "The", "A", "An"],
    "'Man' meaning all human beings takes no article: Man is mortal. Grew from the zero-article family of 2021 and 2025 (general plurals, meals, languages).")
add(AR, "The old watchman goes to ____ school every day, not to study but to guard its gate.",
    ["the", "a", "an", NA],
    "Go to school (no article) means going there to study. When someone goes to the building for another purpose, use 'the': goes to the school to guard it. "
    "Same with church, hospital, prison. Grew from the zero-article family.")

# ================================================================ Block 8 · tenses (5)
add(T, "This is the third time she ____ the state-level debate competition.",
    ["has won", "won", "had won", "wins"],
    "'This is the first (second, third) time' is followed by the present perfect: has won. Grew from the 2018 and 2021 present-perfect questions.")
add(T, "'When ____ from Delhi?' 'Only last night.'",
    ["did you return", "have you returned", "had you returned", "do you return"],
    "A question with 'When' asks for a point of time in the past, so it takes the past simple. The present perfect is never used with 'When…?' "
    "Grew from 2018 and 2021 past-simple questions.")
add(T, "It was in 1936 that Odisha ____ a separate province, after a long movement led by leaders such as Madhusudan Das.",
    ["became", "has become", "had become", "was becoming"],
    "A finished event at a stated past time (in 1936) takes the past simple. The 'after' phrase does not need the past perfect, because the order is already clear. "
    "Grew from the past-year question (They won the Asia Cup in 1993).")
add(T, "'You look very tired.' 'Yes, I ____ in the garden since early morning.'",
    ["have been working", "am working", "worked", "had been working"],
    "An action that began in the past and is still going on (or has just stopped, with a result now: tired) takes the present perfect continuous with since. "
    "Grew from 2025 perfect-continuous questions.")
add(T, "She gives orders to everyone as if she ____ the owner of the house.",
    ["were", "is", "has been", "will be"],
    "'As if' and 'as though' describe something that is not true (she is not the owner), so they take the past subjunctive 'were' for every person. "
    "Grew from the wish and unreal-past family (I wish I had spent, 2018 and 2025).")

# ================================================================ Block 9 · rearrangement (4): small letters, no full stops, no clue from the first letter
RS = "Rearrange the following parts to make a meaningful sentence:\n"
def rs(parts, right, wrong, e):
    t = RS + "\n".join("%s: %s" % (l, p) for l, p in zip("PQRS", parts))
    add(RE, t, [right] + wrong, e)
rs(["that the old bridge", "the engineers warned", "was no longer safe", "the district officials"],
   "QSPR", ["SQPR", "QPRS", "QSRP"],
   "the engineers warned (Q) the district officials (S) that the old bridge (P) was no longer safe (R). 'Warned' needs its object (who was warned) before the 'that' clause; "
   "'was no longer safe' needs the bridge as its subject. Method from the 2025 sentence-part questions.")
rs(["has been chosen", "who scored the highest marks", "the student", "for the state scholarship"],
   "RQPS", ["RPQS", "QRPS", "RQSP"],
   "the student (R) who scored the highest marks (Q) has been chosen (P) for the state scholarship (S). 'Who' must come right after the noun it describes; "
   "'chosen for' joins the verb to its phrase. Same method as 2025.")
rs(["hardly had", "when the guests", "the bride's party reached the hall", "began to leave"],
   "PRQS", ["PQRS", "RPQS", "PRSQ"],
   "hardly had (P) the bride's party reached the hall (R) when the guests (Q) began to leave (S). 'Hardly had' + subject + past participle, then 'when' + the second action. "
   "Grew from 2025 rearrangement and the inversion openers.")
RP = "Rearrange the following sentences to make a meaningful paragraph:\n"
add(RE, RP + "\n".join("%s: %s" % (l, p) for l, p in zip("PQRS", [
    "but within a few years most of them had stopped working",
    "the reason was that no one in the villages knew how to repair them",
    "some years ago hundreds of hand pumps were set up in the dry villages of the district",
    "so the new scheme trains one young person in every village as a mechanic"])),
    ["RPQS", "RQPS", "PRQS", "RPSQ"],
    "R opens: it names the hand pumps. 'But … them' (P) needs the pumps already named. Q gives the reason they stopped, and 'so' (S) gives the answer to that reason. "
    "Openers like but, so and 'the reason' always point back. Grew from 2025 paragraph rearrangement.")

# ================================================================ Block 10 · subject-verb agreement (10)
add(SV, "The Governor, accompanied by his wife and two senior officers, ____ expected to visit the flood relief camp tomorrow.",
    ["is", "are", "were", "have been"],
    "'Accompanied by', 'together with', 'along with' and 'as well as' do not join subjects; the verb agrees with the first noun (Governor): is. Grew from 2021 and 2025 'as well as' questions.")
add(SV, "Measles ____ a dangerous disease for small children who have not been vaccinated.",
    ["is", "are", "were", "have been"],
    "Names of diseases that end in -s (measles, mumps, rickets) are singular. Same with news, physics, mathematics. Grew from 2021 plural-looking nouns.")
add(SV, "There is many a student in this school who ____ the answer but is too shy to speak.",
    ["knows", "know", "are knowing", "have known"],
    "'Many a' + singular noun takes a singular verb, and so does the 'who' clause that describes it: many a student who knows. The second verb 'is' confirms it. "
    "Grew from 2021 'many a' questions.")
add(SV, "A bunch of keys ____ found near the temple gate by the cleaner this morning.",
    ["was", "were", "have been", "are"],
    "'A bunch of', 'a set of', 'a collection of' is one unit, so the verb is singular: a bunch of keys was found. Grew from 2021 and 2025 collective-noun questions.")
add(SV, "Either you or he ____ to blame for the loss of the file.",
    ["is", "are", "am", "were"],
    "With either … or and neither … nor, the verb agrees with the nearer subject (he): is to blame. Grew from 2025 error spotting (neither … nor).")
add(SV, "The Principal, and not the teachers, ____ responsible for the new timetable.",
    ["is", "are", "were", "have been"],
    "In 'X, and not Y', the verb agrees with X, the subject that is really meant. 'Not the teachers' is only added in commas. Grew from the 'as well as' family (2021, 2025).")
add(SV, "To find honest and hardworking helpers ____ not easy these days.",
    ["is", "are", "were", "have"],
    "An infinitive phrase (to find …) as the subject is singular, even if a plural noun (helpers) stands next to the verb. Same with gerunds: Taking walks is good. "
    "Grew from 2021 gerund-subject questions (to err is human).")
add(SV, "Everybody in the two neighbouring villages ____ invited to the wedding feast of the headman's son.",
    ["was", "were", "have been", "are"],
    "Everybody, everyone, each and every are singular, even when a plural noun (villages) follows. Grew from 2021 and 2025 each/every questions (everyone at the party was).")
add(SV, "Many a girl in these villages ____ to give up her studies after Class 10.",
    ["has had", "have had", "were having", "are having"],
    "'Many a' takes a singular noun and a singular verb (has had), and 'her studies' agrees with it. 'Many girls' would take 'have'. Grew from 2021 'many a' questions.")
add(SV, "The cost of the new school buses ____ been shared by the panchayat and the parents.",
    ["has", "have", "were", "are"],
    "The subject is 'cost' (singular); 'of the new school buses' only describes it. Grew from 2021 agreement questions (the headmaster wants; a plural noun after 'of' does not change the verb).")

# ================================================================ Block 11 · comprehension (5)
P1 = (
"For many years the people of Satabhaya, a group of fishing villages on the coast of Kendrapara district, have watched the sea come closer. "
"Old men still remember a temple, a school and a row of coconut trees that stood where the waves now break. Each year the sea takes a little "
"more land, and in some years, after a strong cyclone, it takes a great deal at once.\n\n"
"Scientists say that several things are at work. The sea is rising slowly as the earth grows warmer. Strong storms push the waves further "
"inland. In many places, mangrove forests, which once broke the force of the waves and held the soil together with their roots, have been "
"cut down for firewood or for fish ponds. Without them, the coast has little to protect it.\n\n"
"For a long time the villagers refused to leave. Their boats, their nets and the graves of their parents were here, and they feared that "
"life inland would have no place for fishermen. But as their houses fell one by one into the sea, most families finally agreed to move to "
"a new colony built for them further from the coast. There they were given land, a house and electricity.\n\n"
"The move has not been easy. The new colony is far from the sea, so some fishermen must travel a long way each day to reach their boats. "
"Younger people have begun to look for work in factories and shops. Many of the old, however, still walk back to the empty shore in the "
"evening and sit where their homes once stood. For them, the sea that took their land is still the centre of their lives.")
PRE1 = "Read the passage on Satabhaya and answer the question.\n"
add(CO, PRE1 + "According to the passage, what did the mangrove forests once do for the coast?",
    ["They broke the force of the waves and held the soil", "They gave the villagers land for fish ponds",
     "They supplied the wood for building boats", "They stopped the level of the sea from rising"],
    "Paragraph 2: mangroves 'once broke the force of the waves and held the soil together with their roots'. Fish ponds and firewood are why they were cut, not what they did. "
    "A detail question; 2025 had mostly detail questions (Odisha hockey passage).",
    p=P1, g="p1")
add(CO, PRE1 + "Why did the villagers refuse to leave for a long time?",
    ["They feared there would be no place for fishermen inland", "The new colony had no electricity",
     "The government did not offer them any land", "They believed the sea would go back"],
    "Paragraph 3: 'they feared that life inland would have no place for fishermen'. The colony did have land and electricity, so two options contradict the passage. "
    "Grew from the 2025 detail questions.",
    p=P1, g="p1")
add(CO, PRE1 + "What can be inferred about the older villagers from the last paragraph?",
    ["They remain deeply attached to the sea and their old home", "They plan to return and rebuild the old village",
     "They are angry with the government for moving them", "They have found new work in factories and shops"],
    "They walk back each evening and sit where their homes stood, and the sea is 'still the centre of their lives': attachment. Nothing says they plan to rebuild or are angry, "
    "and the factory work is about the younger people. An inference question: pick what the lines show, not what they might lead to. Grew from 2025 Q-passage inference.",
    p=P1, g="p1")
add(CO, PRE1 + "According to the passage, what problem do some fishermen face in the new colony?",
    ["They must travel far each day to reach their boats", "They have no houses of their own",
     "They are not allowed to fish in the sea", "Their nets were lost during the move"],
    "Paragraph 4: 'some fishermen must travel a long way each day to reach their boats'. The colony gave them houses. Grew from the 2025 detail questions.",
    p=P1, g="p1")
add(CO, PRE1 + "Which is the most suitable title for the passage?",
    ["The Rising Sea and the People of Satabhaya", "Why Mangroves Must Be Saved",
     "A New Colony for Fishermen", "Cyclones on the Odisha Coast"],
    "The passage tells of the sea taking the villages, its causes, the move and the life after it. The first title covers all four paragraphs; "
    "mangroves, the colony and cyclones are only parts. Title questions grew from 2018 comprehension.",
    p=P1, g="p1")
