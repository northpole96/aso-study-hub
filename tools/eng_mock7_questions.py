# English Mock 07 · full Paper III (English) on the 2021 layout, written with the aso-mock skill (24 Nov 2026).
# Plan: python3 .claude/skills/aso-mock/scripts/draw.py english --seed 724815
# User's changes: follow the 2021 paper (drills in blocks), rearrangement under 5, six direct parts-of-speech questions,
# moderate difficulty. First option is the right one unless a is given (then the options stay in the printed order).

META = dict(
    paper="english",
    title="ASO English Mock 07",
    hub_title="English Mock 07",
    masthead="English Mock 07",
    heading="English Paper III · Mock 07",
    tagline="100 questions drawn by probability<br>from the <b>2018, 2021 and 2025</b> papers, on the <b>2021 layout</b>.",
    key="aso-english-mock-2027-7",
    code="M07",
    out="ASO-English-Mock-Test-2027-7.html",
    minutes=45,
    seed=20261124,
    order="given",
    date="24 Nov 2026",
    draw="python3 scripts/draw.py english --seed 724815",
    intro=[
        "This full English paper (45 minutes) follows the 2021 booklet: a mixed grammar opener, then blocks of drills (six parts of speech, "
        "vocabulary, ten prepositions, ten articles, five tenses, ten agreement questions) and one reading passage. "
        "Sentence rearrangement is kept small (4 questions, as you asked), and the level is moderate: one clear rule per question. About a third of the questions are a little longer and wordier, like real exam sentences.",
        "Three questions are exact past questions, because OPSC repeats itself: 2025 Q2 (clear), 2025 Q51 (contrary) and "
        "2021 Q38 (She lives in an apartment). The passage is on Chilika Lake. Every explanation names the rule and the past question it grew from.",
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
add(VB, "Visitors who come to the city zoo on weekends ____ feed the animals, because the zoo staff say that outside food can make them seriously ill.",
    ["must not", "need not", "would", "might"],
    "'Must not' = a ban, as on a sign. 'Need not' means it is not necessary (the trap). Would and might do not give an order. "
    "Grew from 2021 Q2 (People ____ walk on grass = mustn't). Family: modals of duty and ban.")
add(P, "Many young children who sleep alone for the first time are afraid ____ the dark, and they often ask their parents to leave a small light on.",
    ["of", "from", "at", "with"],
    "Afraid of. Adjective + preposition pairs must be learnt as pairs. Grew from 2021 Q9 and Q54 ('Different from', 'Bored with'): same family, new adjective.")
add(ER, IMP + "Before the examination began, the teacher politely asked all the students (to not make) any noise in the library.",
    ["not to make", "don't to make", "to no make", "No improvement"],
    "The 'not' comes before 'to' in a negative infinitive: not to make. 'To not make' is a common slip. Grew from 2021 Q12–16 (sentence improvement, five questions).")
add(AD, "After the first shower of the monsoon, the flowers in our school garden smell ____ and attract many bees and butterflies.",
    ["sweet", "sweetly", "sweeten", "sweetness"],
    "After linking verbs (smell, taste, look, feel, sound) we use an adjective, not an adverb: smell sweet. "
    "2025 tested this adjective/adverb choice (felt tired, looked dull).")
add(VB, "Although his friends had offered to share the cost of the dinner, he insisted on ____ the bill himself.",
    ["paying", "to pay", "pay", "paid"],
    "A preposition (on) is followed by the -ing form: insisted on paying. Compare 2025 'prevent … from + -ing'. "
    "Same family: verb + preposition + gerund.")
add(T, "By the time the police arrived at the shop late at night, the thief ____ away with all the money.",
    ["had run", "has run", "ran", "was running"],
    "Two past actions: the one that happened first (running away) goes in the past perfect. 'By the time' + past tells you so. "
    "Grew from 2025 (past perfect: The train had left before she started).")
add(P, "The final match of the inter-school tournament was ____ because of the heavy rain that continued for the whole afternoon.",
    ["called off", "called on", "called up", "called at"],
    "Called off = cancelled. Called on = visited; called up = telephoned or ordered to join. Phrasal verbs are learnt as whole units. "
    "Grew from 2025 phrasal verbs (called for, look into, turned out).")
add(ER, IMP + "I (am knowing) him for ten years.",
    ["have known", "have been knowing", "was known", "No improvement"],
    "'For ten years' needs the present perfect. 'Know' is a state verb and is not used in the continuous form, so 'have known', not 'have been knowing'. "
    "Grew from 2021 Q13 ('never be' → 'had never been').")
add(VB, "Change into passive voice: The police will arrest the thief soon.\nThe thief ____ by the police soon.",
    ["will be arrested", "will arrested", "is arrested", "would arrest"],
    "Passive of the simple future: will + be + past participle. Grew from 2021 Q1 (will be cleaned): same form, a new verb (will be arrested).")
add(AD, "No sooner did the new teacher enter the noisy class on the first day of school ____ the noise stopped completely.",
    ["than", "when", "then", "that"],
    "No sooner … than; Hardly … when. The word order after 'No sooner' is inverted (did the teacher enter). "
    "Inversion openers were four questions in 2025.")
add(VB, "Since her school will close for two months in May, she is looking forward to ____ her grandparents in the village this summer.",
    ["meeting", "meet", "met", "to meet"],
    "In 'look forward to', the 'to' is a preposition, so the verb takes -ing: looking forward to meeting. The same trap works with 'object to' and 'be used to'. "
    "Grew from 2025 gerund/infinitive questions (seen going, denied having been).")
add(P, "According to her birth certificate, which her father showed at the school office, she was born ____ 15 August 1999.",
    ["on", "in", "at", "by"],
    "On + a date or a day (on Monday, on 15 August); in + month or year; at + a clock time. "
    "Grew from 2021 prepositions of time (Q53–62).")
add(ER, IMP + "Please do not worry about me; I will call you (when I will reach) home safely this evening.",
    ["when I reach", "when I reached", "when I would reach", "No improvement"],
    "After when, if, before, after, until, we do not use 'will' in the time clause: will call … when I reach. "
    "Same idea as the first conditional, which 2025 and 2018 asked.")
add(T, "My younger sister usually ____ tea with her breakfast in the morning, but today she is drinking coffee because we have run out of tea.",
    ["drinks", "drink", "is drinking", "drank"],
    "'Usually' shows a habit, so the simple present: drinks (third person -s). 'Today she is drinking' is the contrasting present continuous. "
    "Grew from 2021 Q25 and 2025 present-tense questions.")
add(VB, "She denied ____ the window.",
    ["breaking", "to break", "break", "broke"],
    "Deny, enjoy, avoid, finish, mind, suggest are followed by -ing, not 'to'. "
    "Grew from 2025 'denied having been'. Same family, simpler form.")
add(AD, "After walking for nearly six hours in the hot sun without any rest, she was ____ tired that she could not stand.",
    ["so", "such", "very", "too"],
    "So + adjective + that. 'Such' is used with a noun (such a tired girl). 'Too' has no 'that' clause after it. "
    "Intensifier family: 2018 Q27 and 2025 (very few … exceptionally).")
add(ER, IMP + "He is (senior than) me by two years.",
    ["senior to", "more senior than", "senior from", "No improvement"],
    "Senior, junior, superior, inferior, prefer: all take 'to', never 'than'. Grew from 2018 and 2021 'prefers … to' questions; also 2021 Q16 (comparison).")
add(P, "The shopkeeper was angry ____ the boy for breaking the glass.",
    ["with", "of", "to", "from"],
    "Angry with a person, angry at (or about) a thing. Grew from 2021 prepositions after adjectives (Q54–62).")
add(VB, "To prepare for the annual day programme, the teacher made all the students ____ the long poem by heart.",
    ["learn", "to learn", "learning", "learnt"],
    "After make, let, see, hear + object, the verb stays in its bare form (no 'to'): made the students learn. "
    "In the passive the 'to' returns: The students were made to learn. Grew from 2021 Q6 (seen going).")
add(ER, IMP + "My mother never drinks coffee in the evening because she prefers tea (than coffee) at that time.",
    ["to coffee", "from coffee", "than the coffee", "No improvement"],
    "Prefer X to Y. Never 'than'. Asked in the 2018 and 2021 papers in other words.")

# ================================================================ Block 2 · parts of speech (6)
POS = "Choose the correct part of speech for the word in bracket:\n"
add(PS, POS + "After checking his notes twice, he is (quite) sure about the answer.",
    ["Adverb", "Adjective", "Conjunction", "Preposition"],
    "'Quite' tells us how sure he is, so it modifies the adjective 'sure'. A word that modifies an adjective, verb or another adverb is an adverb. "
    "Grew from 2021 Q17–22 (direct part-of-speech questions).")
add(PS, POS + "The cat jumped (over) the wall.",
    ["Preposition", "Adverb", "Conjunction", "Adjective"],
    "'Over' stands before a noun phrase (the wall) and shows its place: a preposition. The same word is an adverb when nothing follows it (The plane flew over). "
    "2021 Q18 asked 'for' in the same way.")
add(PS, POS + "Although she was new in the school, she was (friendly) to everyone in the class.",
    ["Adjective", "Adverb", "Noun", "Verb"],
    "'Friendly' ends in -ly but describes 'she', so it is an adjective (the trap in 2021 Q19, 'costly'). "
    "Other -ly adjectives: lovely, lonely, silly, elderly.")
add(PS, POS + "(Swimming) is a good exercise.",
    ["Gerund", "Participle", "Infinitive", "Complement"],
    "An -ing word that works as a noun (here, the subject) is a gerund. An -ing word that describes a noun is a participle (2021 Q20, 'drowning man'). "
    "Grew from 2021 Q20 and Q22.")
add(PS, POS + "I will wait (until) you come back.",
    ["Conjunction", "Preposition", "Adverb", "Adjective"],
    "'Until' joins two clauses (I will wait / you come back), so it is a conjunction. Before a noun (until Monday) it would be a preposition. "
    "Grew from 2021 Q17 ('as well as' = conjunction).")
add(PS, POS + "(Everyone) was happy with the result.",
    ["Pronoun", "Noun", "Adjective", "Verb"],
    "'Everyone' stands in place of names of people, so it is an (indefinite) pronoun. Others: someone, anybody, nobody, each. "
    "2021 Q21 asked 'liar' = noun; here the same choice between noun and pronoun.")

# ================================================================ Block 3 · pick the correct sentence, spot the error (8)
add(ER, "Which sentence is correct?",
    ["She lives in an apartment.", "She lives to an apartment.", "She lives on an apartment.", "She live in apartment."],
    "Live IN a house or an apartment; an apartment needs 'an' (a vowel sound) and the verb 'lives' agrees with 'she'. "
    "Exact past question: 2021 Q38.", src="2021 Q38")
add(ER, "Pick the sentence that is grammatically correct:",
    ["She has been teaching here since 2015.", "She is teaching here since 2015.", "She teach here since 2015.", "She has teach here for 2015."],
    "'Since 2015' (a point of time) needs the present perfect continuous: has been teaching. 'Is teaching' cannot go with 'since'. "
    "Family: 2021 Q36–40 (pick the correct statement).")
add(ER, "Choose the correct sentence:",
    ["Each of the girls has won a prize.", "Each of the girls have won a prize.", "Each of girls has won prize.", "Each girls has won a prize."],
    "Each is singular, so it takes 'has'. Each is followed by 'of + plural noun with the' or by a singular noun (each girl). "
    "Grew from 2021 Q24 and 2025 'each of the buildings has'.")
add(ER, "Choose the correct word order:",
    ["Where did you go yesterday?", "Where you did go yesterday?", "Where did go you yesterday?", "Where yesterday you did go?"],
    "In a question, the helping verb comes before the subject: did you go. Grew from 2021 Q3 (Why did she leave so early?).")
add(ER, "Which of the following sentences is NOT correct?",
    ["I have lived here since five years.", "I have lived here for five years.", "I have lived here since 2020.", "I lived here five years ago."],
    "'Since' goes with a point of time (since 2020); 'for' goes with a length of time (for five years). The first sentence mixes them. "
    "Be careful: this question asks for the wrong sentence.")
add(ER, "Choose the sentence that is free from error:",
    ["The furniture in the room is old.", "The furniture in the room are old.", "The furnitures in the room are old.", "The furnitures in the room is old."],
    "Furniture is uncountable: no plural, and it takes a singular verb. Same group: information, advice, luggage, news. "
    "Grew from 2021 Q39 and the plural-noun family (news is, mathematics is).")
SEG = "Identify the incorrect segment in the sentence below:\n"
add(ER, SEG + "[If it will rain] [tomorrow, we] [shall cancel] [the picnic.]",
    ["If it will rain", "tomorrow, we", "shall cancel", "the picnic."],
    "In the first conditional, the 'if' part uses the simple present, not will: If it rains tomorrow, we shall cancel the picnic. "
    "2025 had a conditional (will/would) error in its error-spotting row.", a=0)
add(ER, SEG + "[Hardly had he] [reached the station] [when the train] [has left.]",
    ["Hardly had he", "reached the station", "when the train", "has left."],
    "Hardly had + past participle … when + simple past: when the train LEFT. 'Has left' breaks the past sequence. "
    "Grew from 2025 inversion (Hardly had … when).", a=3)

# ================================================================ Block 4 · mixed tenses, agreement, adverbs (6)
add(T, "If I ____ the answer, I would tell you.",
    ["knew", "know", "had known", "will know"],
    "'I would tell' = second conditional (unreal now), so the 'if' part takes the simple past: If I knew. "
    "Grew from 2025 conditionals (Had she known; If I had been you).")
add(SV, "A number of students ____ absent today.",
    ["are", "is", "was", "has been"],
    "A number of + plural noun takes a plural verb: A number of students ARE. 'The number of students IS' is singular. "
    "Number-of family from 2021 and 2025 agreement questions.")
add(AD, "The students listened ____ to the lecture.",
    ["carefully", "careful", "care", "carefulness"],
    "An adverb describes the verb 'listened': listened carefully. Grew from 2025 (scrutinised carefully, spoke diplomatically).")
add(T, "She told me that she ____ the film before.",
    ["had seen", "has seen", "saw", "sees"],
    "'Told' is past, and she saw the film even earlier, so the past perfect: had seen. "
    "Grew from 2025 past perfect (had known each other for a decade when …).")
add(SV, "Rice and curry ____ his favourite meal.",
    ["is", "are", "were", "have been"],
    "Two nouns that form one idea (rice and curry, bread and butter) take a singular verb. Compare 'The doctor and the nurse are' (two people). "
    "Grew from 2021 Q83–92 (agreement block).")
add(AD, "Of all the girls in the class, Meena is the ____.",
    ["tallest", "taller", "tall", "most tall"],
    "The + superlative (tallest) when we speak of one among many. 'Higher' compares only two. "
    "Grew from 2025 (oldest but the smallest) and 2018 degree questions.")

# ================================================================ Block 5 · vocabulary (16)
SYN = "Select the word that has the same meaning as the word in the bracket:\n"
ANT = "Choose the word most opposite in meaning to "
add(SY, SYN + "The retired judge spoke at the college function, and his (candid) remarks about the failures of the system surprised the audience.",
    ["frank", "rude", "loud", "careful"],
    "Candid = open and honest, even when it is not pleasant. Rude and loud describe manner, not honesty. "
    "Grew from 2021 Q41–42 (intrigue, fondling): the bracket word in a sentence.")
add(AN, ANT + "EXPAND:",
    ["contract", "extend", "spread", "enlarge"],
    "Expand = become bigger. Its opposite is contract (become smaller). The other three mean the same as expand. "
    "Grew from 2021 Q44–47 (military, embrace, subversion, sinister).")
add(V, "His explanation was so ____ that everyone understood the difficult concept.",
    ["clear", "complicated", "confusing", "vague"],
    "Everyone understood, so the explanation was clear. The other three words all say it was hard to follow. "
    "Exact past question: 2025 Q2.", src="2025 Q2")
add(SY, SYN + "At the birthday party, the magician's clever tricks (enthralled) the children, and nobody could look away from the stage.",
    ["fascinated", "bored", "frightened", "confused"],
    "Enthral = hold the attention completely, fascinate. Grew from 2021 Q41 (intrigue).")
add(AN, ANT + "SCARCE:",
    ["plentiful", "rare", "limited", "insufficient"],
    "Scarce = not enough, rare. Plentiful = in large amount. The other three are near synonyms of scarce, the usual trap in antonym questions.")
add(V, "We are unhappy because the results of the experiment are ____ to our expectations.",
    ["contrary", "consistent", "supportive", "expected"],
    "'Contrary to' = opposite to, which fits 'unhappy because'. Consistent, supportive and expected would make us happy. "
    "Exact past question: 2025 Q51.", src="2025 Q51")
add(SY, SYN + "The police officer spoke softly and tried to (pacify) the angry crowd that had gathered outside the factory gate.",
    ["calm", "excite", "warn", "ignore"],
    "Pacify = make calm and peaceful (from 'peace'). Its opposite is excite or anger. Same family as 2021 Q41–42.")
add(AN, ANT + "ARROGANT:",
    ["humble", "proud", "rude", "bold"],
    "Arrogant = too proud of oneself. Humble = modest. Proud is a near synonym, the trap. Same kind as 2021 Q47 (sinister).")
add(V, "The new teacher was so ____ that even the shyest student felt free to ask questions.",
    ["approachable", "aloof", "strict", "forgetful"],
    "Approachable = easy to talk to. 'Shyest student felt free' is the clue; aloof (cold, distant) is the opposite. "
    "2025 asked 'unlike the pessimism of his brothers' in the same way: the clue is inside the sentence.")
add(SY, SYN + "To protect the rivers and the sea, the government has announced a new rule that will (curb) the use of plastic bags.",
    ["restrict", "increase", "allow", "praise"],
    "Curb = control or limit (a curb on a road keeps traffic in). Increase and allow are opposites. "
    "Same family as 2021 Q41–42.")
add(AN, ANT + "TRANQUIL:",
    ["agitated", "peaceful", "silent", "gentle"],
    "Tranquil = calm and quiet. Agitated = disturbed, restless. Peaceful, silent and gentle are near synonyms. Grew from 2021 Q44–47.")
add(V, "In the sentence 'The teacher asked him to address the class', the word 'address' means:",
    ["speak to", "write a letter to", "find the place of", "greet with a bow"],
    "Address as a verb = speak formally to a group. The noun 'address' is the place where one lives. "
    "Grew from 2018 word-meaning questions (a word with many meanings).")
add(SY, SYN + "When the reporter asked about the date of the new bridge, the minister gave a (vague) reply and avoided naming any month.",
    ["unclear", "loud", "quick", "honest"],
    "Vague = not clear or exact. Honest is the opposite idea. Same family as 2021 Q41–42.")
add(AN, ANT + "HOSTILE:",
    ["friendly", "enemy", "angry", "strange"],
    "Hostile = unfriendly, showing enmity. Friendly is the opposite. 'Enemy' is a noun and is the trap. Grew from 2021 Q44–47.")
add(V, "Tell me the ____ of the story in two lines. (Choose the word that means 'the main idea'.)",
    ["gist", "plot", "moral", "scene"],
    "Gist = the main point. Plot is the order of events; moral is the lesson. Grew from 2018 word-meaning questions (hoard, lately).")
add(SY, "Select the pair of synonyms:\n(I) Brave  (II) Cowardly  (III) Fearless  (IV) Timid",
    ["(I) and (III)", "(I) and (II)", "(II) and (III)", "(III) and (IV)"],
    "Brave and fearless both mean 'without fear'. Cowardly and timid are the other pair. Grew from 2021 Q50–52 (pairs of synonyms).")

# ================================================================ Block 6 · prepositions (10)
add(P, "The success of the new bridge project in the district depends ____ teamwork, honest planning and good use of money.",
    ["on", "of", "at", "to"],
    "Depend on, never 'depend of'. Verb + preposition pairs are asked every year (2021 Q53–62; 2025 'lies in', 'focuses on').")
add(P, "Although she smiled at the party, she was secretly envious ____ her friend's success in the entrance examination.",
    ["of", "at", "about", "to"],
    "Envious of, jealous of. Grew from 2021 Q54 (adjective + preposition).")
add(P, "The meeting was held ____ the school hall ____ Monday. The principal congratulated the winners ____ their success.",
    ["in, on, on", "at, in, for", "on, at, of", "by, to, on"],
    "In the hall (inside a place), on Monday (day), congratulated on (success). "
    "Same style as 2021 Q7 and 2018 Q78 (three blanks in one passage, asked twice word for word).")
add(P, "____ the strong wind, the boat reached the shore safely.",
    ["Despite", "Although", "In spite", "Because"],
    "Despite + noun phrase. Although needs a clause; 'in spite' needs 'of'; 'because' gives a reason, not a contrast. "
    "Family: phrase prepositions (despite, in spite of, because of, in view of).")
add(P, "On the last day of the school year, the teacher divided the box of sweets ____ the children equally so that no one felt left out.",
    ["among", "between", "with", "by"],
    "Among = three or more things or people; between = two. Grew from 2021 Q53–62 (prepositions in sentences).")
add(P, "After reading both essays carefully, the teacher said that your idea is very similar ____ mine.",
    ["to", "with", "from", "than"],
    "Similar to, different from. Grew from 2018 Q87 and 2021 Q9 (According to, Different from, Based on).")
add(P, "I have been standing at the railway station gate waiting for you ____ two hours, and I am very tired now.",
    ["for", "since", "from", "by"],
    "For + a length of time; since + a point of time. Grew from 2021 prepositions of time (Q53–62).")
add(P, "She is married ____ a doctor and is very proud ____ him.",
    ["to, of", "with, at", "to, for", "by, about"],
    "Married to; proud of. Two blanks in one sentence, as in 2021 Q7.")
add(P, "The police, with the help of the villagers and a few dogs, are looking ____ the missing child near the forest.",
    ["for", "into", "after", "at"],
    "Look for = search. Look into = investigate; look after = take care of. 2025 asked 'look into'. Learn the phrasal verbs as a set.")
add(P, "She apologised ____ the teacher ____ being late.",
    ["to, for", "with, of", "for, to", "at, on"],
    "Apologise to a person for something. Verb + two prepositions. Grew from 2025 'confide in', 'suffer from'.")

# ================================================================ Block 7 · articles (10)
def art(q, o, e): add(AR, q, o, e)
art("Everyone in the village trusts her, because she is ____ honest girl who has never told a lie.", ["an", "a", "the", NA],
    "The rule is the SOUND, not the spelling: honest begins with a vowel sound (the h is silent), so 'an'. Grew from 2021 Q63–72 and 2025 (an honour).")
art("____ Indus flows through Ladakh.", ["The", "A", "An", NA],
    "The goes with rivers, seas, oceans and mountain ranges (the Indus, the Pacific, the Alps). Grew from 2021 and 2025 'the Amazon rainforest'.")
art("The stadium was full on Sunday because it was ____ one-day match between India and Australia.", ["a", "an", "the", NA],
    "'One' begins with the consonant sound 'w', so 'a one-day match'. Same sound rule as 'a unique', 'a European' (2021 and 2025).")
art("____ time is more valuable than money.", [NA, "The", "A", "An"],
    "No article before an abstract noun used in a general sense (time, honesty, beauty). Grew from 2021 zero-article questions.")
art("Among all the players who have joined our college cricket team this year, Rohit is ____ best batsman.", ["the", "a", "an", NA],
    "The goes with superlatives: the best, the tallest. Grew from 2021 and 2025 superlatives.")
art("He is ____ MP from Odisha.", ["an", "a", "the", NA],
    "MP is read 'em-pee', which starts with a vowel sound, so 'an MP'. Same as 'an MLA', 'an SI'. Grew from 2021 and 2025 a/an questions (an MLA).")
art("____ Himalayas are the highest mountain range in the world.", ["The", "A", "An", NA],
    "Mountain ranges and plural names take 'the' (the Himalayas, the Andes); a single peak does not (Mount Everest). Grew from 2021 article questions (Q63–72).")
art("In our hostel, the bell rings loudly at noon, and we have ____ lunch at one o'clock in the big dining hall.", [NA, "the", "a", "an"],
    "No article before meals (breakfast, lunch, dinner). Grew from 2021 zero-article questions.")
art("He is ____ European and ____ M.A. from Calcutta University.", ["a, an", "an, a", "a, a", "an, an"],
    "European begins with 'y' (consonant sound), so 'a'. M.A. begins with 'em' (vowel sound), so 'an'. Two blanks in one sentence; the sound trap from 2025.")
art("She plays ____ guitar in the school band.", ["the", "a", "an", NA],
    "The goes with musical instruments (the guitar, the violin). Grew from 2021 specific-article questions.")

# ================================================================ Block 8 · tenses (5)
add(T, "I have travelled to many hill stations with my family, but I have never ____ such a beautiful place.",
    ["seen", "saw", "see", "been seeing"],
    "Have + past participle: have never seen. 'Never … before' with no time named takes the present perfect. Grew from 2018 Q15 and 2025 'I have had no trouble so far'.")
add(T, "Sachin Tendulkar ____ his first Test century in 1990.",
    ["scored", "has scored", "scores", "had scored"],
    "A fixed past year (1983) takes the simple past: won. The present perfect never goes with a finished time. Grew from 2018 and 2025 (They won the Asia Cup in 1993).")
add(T, "By the time you reach home, I ____ dinner.",
    ["will have cooked", "will cook", "have cooked", "cooked"],
    "'By the time you reach' = a future deadline: the future perfect (will have + past participle). Grew from 2021 Q73–76 (future perfect).")
add(T, "It ____ since early morning without any break, so all the roads in the town are wet and muddy.",
    ["has been raining", "is raining", "rains", "had rained"],
    "'Since morning' + the action goes on up to now: present perfect continuous. Grew from 2018 and 2025 (has been living … for five years).")
add(T, "When ____ you last visit your village?",
    ["did", "have", "do", "had"],
    "'Last' points to a finished time, so the question uses did + base verb. 'Have you last visited' is wrong. Grew from the 2018 and 2021 past-simple questions.")

# ================================================================ Block 9 · rearrangement (4, under 5)
RS = "Rearrange the following parts to make a meaningful sentence:\n"
def rs(parts, right, wrong, e):
    t = RS + "\n".join("%s: %s" % (l, p) for l, p in zip("PQRS", parts))
    add(RE, t, [right] + wrong, e)
rs(["of the school", "has been postponed", "The annual sports day", "because of the heavy rain"],
   "RPQS", ["RQPS", "PRQS", "RPSQ"],
   "The annual sports day (R) of the school (P) has been postponed (Q) because of the heavy rain (S). Find the subject first (R), then the phrase that belongs to it (P), then the verb (Q); the reason comes last. Method from the 2025 rearrangement questions.")
rs(["who had won the first prize", "gave a speech", "The girl", "at the annual function"],
   "RPQS", ["RQPS", "PRQS", "RSQP"],
   "The girl (R) who had won the first prize (P) gave a speech (Q) at the annual function (S). 'Who' follows the noun it describes. Same method as 2025.")
rs(["he finished", "Although he was very tired,", "before midnight.", "the work"],
   "QPSR", ["PQSR", "QPRS", "SPQR"],
   "Although he was very tired, (Q) he finished (P) the work (S) before midnight. (R). A sentence that opens with 'Although' puts the comma part first; the time phrase goes last. Grew from 2025.")
RP = "Rearrange the following sentences to make a meaningful paragraph:\n"
add(RE, RP + "\n".join("%s: %s" % (l, p) for l, p in zip("PQRS", [
    "The owner thanked him with tears of joy.",
    "Gopal found a purse on the road.",
    "He went to the address and returned the purse.",
    "Inside, there was some money and an address card."])),
    ["QSRP", "QRSP", "SQRP", "QSPR"],
    "Start with the first event: Gopal found a purse (Q). 'Inside' (S) must follow it. He then returned it (R), and the owner's thanks (P) is the end. "
    "A story paragraph runs in the order of time. Grew from 2025 (rearranging a paragraph).")

# ================================================================ Block 10 · subject-verb agreement (10)
add(SV, "The captain, along with his players, ____ welcomed at the airport.",
    ["was", "were", "are", "have been"],
    "'Along with' does not make the subject plural. The verb agrees with the first subject (captain), so 'was'. Grew from 2021 and 2025 'as well as' questions.")
add(SV, "A rare collection of old coins from the Gupta and Mauryan periods ____ kept in the state museum.",
    ["is", "are", "were", "have been"],
    "The subject is 'collection' (one thing), not 'coins'. A plural noun after 'of' does not change the verb. Grew from 2021 and 2025 collective-noun questions.")
add(SV, "A pair of trousers ____ lying on the bed.",
    ["is", "are", "were", "have been"],
    "'A pair' is singular: a pair of trousers IS. Without 'pair', trousers is plural (The trousers are). Grew from the 2021 agreement block.")
add(SV, "Many a student in the final year of the course ____ failed in this subject because of weak practice.",
    ["has", "have", "are", "were"],
    "Many a + singular noun takes a singular verb, though the meaning is 'many'. Grew from 2021 Q83–92.")
add(SV, "The price of vegetables ____ risen sharply this month.",
    ["has", "have", "are", "were"],
    "The subject is 'price' (singular). 'Of vegetables' only describes it. The plural noun next to the verb is the trap. Grew from 2025 Q68 ('rules has become').")
add(SV, "Every boy and girl in this small village school ____ the national anthem very well.",
    ["knows", "know", "are knowing", "have known"],
    "Every + singular noun(s), even joined by 'and', takes a singular verb. Grew from 2021 Q24 and 2025 'everyone feels'.")
add(SV, "My spectacles ____ on the desk.",
    ["are", "is", "was", "has been"],
    "Scissors, trousers, spectacles and pants are plural in form and take a plural verb unless 'a pair of' is used. Compare the pair-of question above.")
add(SV, "Either Meera or her cousins ____ coming to the party.",
    ["are", "is", "was", "has been"],
    "With either … or and neither … nor, the verb agrees with the nearer subject: 'cousins' (plural) → are. Grew from 2025 neither/nor error-spotting question.")
add(SV, "One of the books on the shelf ____ missing.",
    ["is", "are", "were", "have been"],
    "The subject is 'one' (singular). 'Of the books' only tells which one. Grew from 2021 Q83–92.")
add(SV, "Doctors often warn that eating too many sweets and chocolates every day ____ bad for your teeth.",
    ["is", "are", "were", "have been"],
    "A gerund phrase as a subject is singular: Eating … IS. Grew from 2021 gerund-subject questions (public speaking is a skill).")

# ================================================================ Block 11 · comprehension (1 passage × 5)
P1 = (
"Chilika Lake in Odisha is the largest coastal lagoon in Asia. It lies along the Bay of Bengal and spreads over parts of three "
"districts: Puri, Khordha and Ganjam. A narrow strip of sand separates the lake from the sea, and a small channel lets sea water "
"flow in and out. Because of this, the water is salty in some parts of the lake and fresh in others.\n\n"
"Every winter, lakhs of birds fly to Chilika from far-off places such as Siberia and Central Asia. They travel thousands of "
"kilometres to escape the harsh cold of their homes. Nalabana, a small island in the lake, is the best place to watch them, and "
"it has been declared a bird sanctuary. The lake is also home to the rare Irrawaddy dolphin, which many tourists come to see in a boat.\n\n"
"For thousands of fishing families, the lake is the main source of food and income. Fish, prawn and crab caught here are sold in "
"many cities. However, the lake once faced serious trouble. Silt carried by rivers and illegal prawn farms had made it shallow and "
"polluted the water. In 1993, Chilika was placed on the list of wetlands in danger. In 2000, the Chilika Development Authority "
"opened a new mouth to the sea and removed the illegal farms. The water became cleaner and the fish catch rose. In 2002, the lake "
"was taken off the danger list, the first Asian wetland to be saved in this way.")
PRE1 = "Read the passage on Chilika Lake and answer the question.\n"
add(CO, PRE1 + "Which is the most suitable title for the passage?",
    ["Chilika Lake: Home of Birds and Fishermen", "The History of Odisha's Rivers",
     "How to Start a Prawn Farm", "A Journey to the Bay of Bengal"],
    "The passage covers the lake itself, its birds and dolphins, the fishing families and how the lake was saved. The first title covers all of these; the others are too narrow or about something else. "
    "Title questions grew from 2018 comprehension (Q67–70).", p=P1, g="p1")
add(CO, PRE1 + "According to the passage, why do birds fly to Chilika every winter?",
    ["To escape the harsh cold of their homes", "To find fish and prawn to eat", "To lay their eggs in the sand", "To meet the Irrawaddy dolphin"],
    "Paragraph 2: 'They travel thousands of kilometres to escape the harsh cold of their homes.' A detail question: the answer is a line of the passage in other words. "
    "2025 (the Odisha hockey passage) were mostly detail questions.", p=P1, g="p1")
add(CO, PRE1 + "What had made the lake shallow and polluted?",
    ["Silt from rivers and illegal prawn farms", "Heavy rain and floods", "Too many tourists and boats", "The sand strip near the sea"],
    "Paragraph 3: 'Silt carried by rivers and illegal prawn farms had made it shallow and polluted the water.' The other options are not mentioned as causes.", p=P1, g="p1")
add(CO, PRE1 + "What happened after the Chilika Development Authority opened a new mouth to the sea?",
    ["The water became cleaner and the fish catch rose", "The lake was added to the danger list",
     "The birds stopped coming to the lake", "The fishing families left the area"],
    "Paragraph 3: after the new mouth and the removal of illegal farms, 'the water became cleaner and the fish catch rose'. The danger-list entry came earlier (1993).", p=P1, g="p1")
add(CO, PRE1 + "Which of the following is TRUE according to the passage?",
    ["The water of the lake is salty in some parts and fresh in others", "The lake is fully separated from the sea",
     "Nalabana is a large city near the lake", "Chilika is the largest lake in the world"],
    "Paragraph 1: the channel lets sea water flow in, so the water is salty in some parts and fresh in others. 'Fully separated' is wrong (there is a channel) and 'largest in the world' goes beyond 'largest coastal lagoon in Asia'. "
    "A 'which is true' question checks each option against the text, as in 2025.", p=P1, g="p1")
