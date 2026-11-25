# English Mock 08 · full Paper III (English) on the 2021 layout, written with the aso-mock skill (25 Nov 2026).
# Plan: python3 .claude/skills/aso-mock/scripts/draw.py english --seed 318406 (families and exact repeats; counts changed on the user's word).
# User's changes (25 Nov 2026): add 4 voice-change and 3 direct/indirect speech questions; rearrangement 6 (4 sentence + 2 paragraph),
# written in lower case with no full stop so the first part gives no clue; level semi-moderate to hard.
# First option is the right one unless a is given (then the options stay in the printed order).

META = dict(
    paper="english",
    title="ASO English Mock 08",
    hub_title="English Mock 08",
    masthead="English Mock 08",
    heading="English Paper III · Mock 08",
    tagline="100 questions on the <b>2021 layout</b>,<br>with voice, speech and clue-free rearrangement.",
    key="aso-english-mock-2027-8",
    code="M08",
    out="ASO-English-Mock-Test-2027-8.html",
    minutes=45,
    seed=20261125,
    order="given",
    date="25 Nov 2026",
    draw="python3 scripts/draw.py english --seed 318406",
    intro=[
        "This full English paper (45 minutes) follows the 2021 booklet: a mixed grammar opener, then blocks of drills (six parts of speech, "
        "vocabulary, nine prepositions, eight articles, five tenses, ten agreement questions) and one reading passage. "
        "On your request it also has four voice-change and three direct-and-indirect-speech questions, and six rearrangement questions "
        "(four sentence parts, two paragraphs) written in small letters with no full stop, so the first part gives no clue.",
        "The level is semi-moderate to hard: many options are close, and some questions need two steps. Three questions are exact past questions: "
        "2025 Q58 (touching), 2021 Q55 (took it to heart) and 2021 Q64 (an ideal climate). Voice and speech are not named in the official syllabus list, "
        "so treat those seven as extra practice. The passage is on Sambalpuri ikat.",
    ],
)

Q = []
def add(s, q, o, e, k="one", n=False, c=False, a=None, **x):
    d = dict(s=s, q=q, o=o, e=e, k=k, n=n, c=c, a=a); d.update(x); Q.append(d)

V, T, SV, P, AD, AR, VB, ER, SY, AN, CO, RE, PS = ("Vocabulary", "Tenses", "Subject–verb agreement", "Preposition", "Adverb",
    "Articles", "Verb", "Error spotting", "Synonyms", "Antonyms", "Comprehension", "Sentence rearrangement", "Parts of speech")
NA = "No article"
IMP = "Choose how the part in brackets can be improved. If no change is needed, choose 'No improvement'.\n"

# ================================================================ Block 1 · mixed grammar opener (16)
add(VB, "The committee has decided ____ the annual meeting until the new chairman takes charge next month.",
    ["to postpone", "postponing", "postpone", "to postponing"],
    "'Decide' is followed by the to-infinitive: decided to postpone. Verbs like enjoy, avoid and finish take -ing; decide, plan, hope and refuse take to. "
    "Grew from 2025 and 2021 verb-form questions.")
add(VB, "She cannot help ____ whenever she hears that old film song, although she knows the words are quite silly.",
    ["laughing", "to laugh", "laugh", "to laughing"],
    "'Cannot help' means 'cannot stop oneself' and takes the -ing form: cannot help laughing. Same group: cannot bear, cannot stand, it is no use, it is worth. "
    "Grew from 2018 gerund questions.")
add(VB, "You ____ told me about the problem earlier; now it is too late for anyone to help.",
    ["should have", "must have", "can have", "need have"],
    "'Should have + past participle' blames a missed duty in the past. 'Must have' is a guess about something certain, not a blame. 'Can have' and 'need have' are not used this way. "
    "Grew from 2021 Q2 (modals).")
add(VB, "The match was cancelled, so he ____ have hurried to the ground in such heavy traffic.",
    ["needn't", "mustn't", "can't", "shan't"],
    "'Needn't have + past participle' means he did something that was not necessary. 'Mustn't have' is not used for the past. "
    "Grew from 2021 modals (need not and must not). Family: perfect modals.")
add(T, "The patient ____ for nearly two hours when the doctor finally arrived at the village clinic.",
    ["had been waiting", "has been waiting", "was waiting", "waited"],
    "An action that was going on for some time before another past action: past perfect continuous (had been waiting). 'Was waiting' does not show the two hours before the doctor came. "
    "Grew from 2025 tense questions.")
add(T, "I am sorry, I can't open the cupboard. I ____ my keys, and I do not know where to look for them.",
    ["have lost", "lost", "had lost", "was losing"],
    "A past action with a result now (no keys now): present perfect, have lost. 'Lost' would name a time in the past. "
    "Grew from the 2018 and 2021 present-perfect questions.")
add(AD, "Never before ____ such a huge crowd at the annual temple fair as we saw on the last day of the festival.",
    ["had I seen", "I had seen", "have I saw", "I did see"],
    "A negative opener (Never before, Hardly, Rarely) is followed by the auxiliary BEFORE the subject: Never before had I seen. Grew from 2025 inversion openers (Never before had, Rarely does).")
add(AD, "Of the two brothers, Ravi is the ____ careful, and so the family trusts him with the shop.",
    ["more", "most", "much", "very"],
    "Between two persons we use the comparative with 'the': the more careful. 'Most' is for three or more. Grew from 2025 degree questions.")
add(AD, "He did not prepare well for the interview; ____, he answered every question with confidence and won the job.",
    ["nevertheless", "therefore", "moreover", "hence"],
    "The second part goes against the first (no preparation, still did well), so the linker must show contrast: nevertheless. Therefore and hence show result; moreover adds. "
    "Grew from 2025 connector questions.")
add(P, "The Chief Minister laid special emphasis ____ the need for clean drinking water in every village of the district.",
    ["on", "for", "at", "over"],
    "Emphasis on, stress on, focus on. Noun + preposition pairs are learnt as pairs. Grew from 2021 and 2025 fixed-preposition questions.")
add(P, "Although the villagers were poor, they were deeply grateful ____ the young doctor ____ saving the child.",
    ["to … for", "at … for", "to … of", "with … on"],
    "Grateful TO a person FOR a thing. Two blanks make you check both pairs. Grew from 2021 Q56 (envious of) and 2025 multi-blank prepositions.")
add(P, "Because of the cyclone warning issued late in the evening, the school picnic was called ____.",
    ["off", "out", "away", "down"],
    "Call off = cancel. Call out = shout; call on = visit. Grew from 2021 and 2025 phrasal verbs.")
add(ER, IMP + "The report said that neither of the two answers (are) correct, and the examiner asked the student to try again.",
    ["is", "are being", "were", "No improvement"],
    "'Neither' with 'of the two' takes a singular verb: neither of the answers IS correct. Grew from 2021 agreement block and sentence improvement Q12–16.")
add(ER, IMP + "He is (more taller) than his elder brother, although he is three years younger than him.",
    ["taller", "most tall", "much more tall", "No improvement"],
    "A short adjective takes -er alone; 'more' + '-er' is a double comparative and wrong. Grew from 2021 sentence improvement.")
add(ER, IMP + "If it (will rain) tomorrow, the school will have to postpone the annual sports meet.",
    ["rains", "would rain", "is raining", "No improvement"],
    "In the first conditional, the 'if' part takes the simple present: If it rains. Never will after if. Grew from 2025 conditional error.")
add(ER, IMP + "The principal suggested (me to take) the prize on behalf of our class on the final day.",
    ["that I take", "me taking to", "me for take", "No improvement"],
    "'Suggest' does not take object + to. Use 'suggested that I take' (or 'suggested my taking'). A subtle trap that looks natural. Grew from 2021 improvement questions.")

# ================================================================ Block 2 · parts of speech (6)
POS = "Choose the correct part of speech for the word in bracket:\n"
add(PS, POS + "The rain stopped and the little boy walked (past) the shop without looking inside.",
    ["Preposition", "Adverb", "Adjective", "Noun"],
    "'Past' stands before a noun phrase (the shop) and shows where he went: a preposition. With nothing after it (He walked past) it would be an adverb. "
    "2021 Q18 asked 'for' in the same way.")
add(PS, POS + "In this country the (rich) are often asked to help the poor in times of trouble.",
    ["Noun", "Adjective", "Adverb", "Pronoun"],
    "'The' + adjective = a group of people. 'The rich' means rich people: it works as a plural noun. Grew from 2021 Q21 (noun) and the other 'the + adjective' forms.")
add(PS, POS + "He reached the station very (early) to catch the first train to the city.",
    ["Adverb", "Adjective", "Noun", "Conjunction"],
    "'Early' tells HOW (when) he reached, so it modifies a verb: an adverb. In 'the early bird' it is an adjective. Early, late, fast, hard are both. Grew from 2021 Q19 (costly).")
add(PS, POS + "(Walking) after dinner is a very good exercise for the heart.",
    ["Gerund", "Participle", "Infinitive", "Verb"],
    "An -ing word that works as a noun (here the subject) is a gerund. An -ing word that describes a noun is a participle. Grew from 2021 Q20 and Q22.")
add(PS, POS + "The (broken) window was repaired by the carpenter on the same morning.",
    ["Participle", "Gerund", "Infinitive", "Noun"],
    "'Broken' is the past participle and it describes the noun 'window'. An -ed or -en form used like an adjective is a participle (2021 Q20, 'drowning man').")
add(PS, POS + "(Since) he was ill, he did not attend the class on the last day of the term.",
    ["Conjunction", "Preposition", "Adverb", "Adjective"],
    "'Since' joins two clauses (he was ill / he did not attend) and gives a reason: a conjunction. Before a time word (since Monday) it is a preposition. "
    "Grew from 2021 Q17 ('as well as' = conjunction).")

# ================================================================ Block 3 · pick the correct sentence, spot the error (8)
PICK = "Choose the grammatically correct sentence:"
add(ER, PICK.strip(),
    ['He is senior to me in the office.', 'He is senior than me in the office.', 'He is more senior than me in the office.', 'He is seniorer to me in the office.'],
    "Senior, junior, superior, inferior, prior take 'to', not 'than'. Grew from 2021 Q38 and the 'Different from' family.")
add(ER, PICK.strip(),
    ['The furniture in the hall was very old.', 'The furnitures in the hall were very old.', 'The furniture in the hall were very old.', 'The furnitures in the hall was very old.'],
    "Furniture is uncountable: no -s, and the verb is singular. Grew from 2025 uncountable nouns.")
add(ER, PICK.strip(),
    ['I look forward to meeting you next week.', 'I look forward to meet you next week.', 'I am looking forward to meet you next week.', 'I look forward for meeting you next week.'],
    "In 'look forward to', 'to' is a preposition, so the -ing form follows: meeting. Grew from 2025 verb + preposition + gerund questions.")
add(ER, PICK.strip(),
    ['Each of the players has received a medal.', 'Each of the players have received a medal.', 'Each of the players are receiving a medal.', 'Each of the player has received a medal.'],
    "'Each' is singular (has), and 'of' takes a plural noun (players). 'Each of the player' breaks the second rule. Grew from 2021 agreement block.")
add(ER, PICK.strip(),
    ['Scarcely had I left the house when it began to rain.', 'Scarcely I had left the house when it began to rain.', 'Scarcely had I left the house than it began to rain.', 'Scarcely did I leave the house when it began to rain.'],
    "Scarcely/Hardly had + subject + past participle … WHEN. Than goes with no sooner. Grew from 2025 inversion openers.")
add(ER, PICK.strip(),
    ['If I had known the truth, I would have told you.', 'If I would have known the truth, I would have told you.', 'If I knew the truth, I would have told you.', 'If I have known the truth, I would tell you.'],
    "Third conditional (unreal past): If + had + past participle, would have + past participle. 'Would' never goes in the if-part. Grew from 2025 conditionals.")
SEG = "Identify the incorrect segment in the sentence below:\n"
add(ER, SEG + "[The teacher as well as] [the students were] [present in the hall] [when the bell rang.]",
    ["The teacher as well as", "the students were", "present in the hall", "when the bell rang."],
    "'As well as' does not join subjects, so the verb follows the first noun (teacher): was present. 'The students were' is the error. Grew from 2021 and 2025 'as well as' questions.", a=1)
add(ER, SEG + "[The news of] [the flood have] [shocked the] [whole country.]",
    ["The news of", "the flood have", "shocked the", "whole country."],
    "'News' is singular (like economics), so the verb must be 'has shocked'. The plural-looking noun next to the verb (the flood) is not the subject. Grew from 2021 and 2025 agreement questions.", a=1)
# ================================================================ Block 4 · mixed tenses, agreement, adverbs (6)
add(T, "I ____ a long letter to my friend when the telephone rang, so I had to leave it half finished.",
    ["was writing", "wrote", "had written", "am writing"],
    "A longer action in progress (past continuous) when a shorter one cut in (the phone rang). Grew from the 2018 and 2021 past-continuous questions.")
add(SV, "The Principal and Chairman of the trust, Mr Das, ____ present at the function and gave away the prizes.",
    ["was", "were", "are", "have been"],
    "Two titles for ONE person (one article before the first title only) take a singular verb: the Principal and Chairman WAS. Two persons would need 'the Principal and the Chairman were'. Grew from 2021 'and' agreement questions.")
add(AD, "Not only ____ the examination, but she also won a scholarship for higher studies.",
    ["did she pass", "she passed", "she did pass", "has she passed"],
    "'Not only' at the start of a sentence needs inversion: auxiliary before the subject (did she pass). Grew from 2025 inversion questions.")
add(T, "Honey never ____ bad if it is kept in a clean, tightly closed jar away from water.",
    ["goes", "went", "has gone", "is going"],
    "A general truth takes the simple present. Grew from 2021 and 2025 present-simple questions.")
add(SV, "Either of the two roads ____ good enough for the buses that bring the pilgrims to the temple.",
    ["is", "are", "were", "have been"],
    "'Either' and 'neither' are singular when used alone: either of the roads IS. Grew from the 2021 agreement block.")
add(AD, "He ran so ____ that nobody in the village could catch him before the bus left the stand.",
    ["fast", "fastly", "faster", "fastest"],
    "'Fast' is both an adjective and an adverb. There is no word 'fastly'. 'So … that' needs the plain form. Grew from 2025 adjective/adverb questions.")

# ================================================================ Block 5 · vocabulary (14)
add(SY, "Choose the word closest in meaning to the word in bracket:\nThe minister's reply to the reporters was (ambiguous), and nobody could tell whether he agreed or not.",
    ["unclear", "honest", "angry", "brief"],
    "Ambiguous = having two possible meanings, so unclear. The clue is 'nobody could tell'. Grew from 2021 synonym questions (11 asked).")
add(SY, "Choose the word closest in meaning to the word in bracket:\nThe villagers were (jubilant) when their small team won the district cup after twenty years.",
    ["delighted", "surprised", "tired", "silent"],
    "Jubilant = full of joy, delighted. Grew from 2021 synonym questions.")
add(SY, "Choose the word closest in meaning to the word in bracket:\nShe is a (frugal) woman who never wastes money on things she does not really need.",
    ["thrifty", "greedy", "poor", "generous"],
    "Frugal = careful with money, thrifty. 'Poor' is the trap: frugal is a habit, not a lack of money. Grew from 2021 synonym questions.")
add(SY, "Choose the word closest in meaning to the word in bracket:\nThe doctor gave a (candid) opinion about the condition of the patient, even though it was not pleasant to hear.",
    ["frank", "secret", "kind", "doubtful"],
    "Candid = honest and open, frank. Grew from 2021 synonym questions.")
add(SY, "Choose the word closest in meaning to the word in bracket:\nThe auditor is known for his (meticulous) checking of every page of the accounts.",
    ["thorough", "talented", "speedy", "modest"],
    "Meticulous = very careful about details, thorough. Grew from 2021 synonym questions.")
add(AN, "Choose the word opposite in meaning to the word in bracket:\nIn the dry months, fresh drinking water becomes (scarce) in many parts of the district.",
    ["abundant", "costly", "clean", "salty"],
    "Scarce = hard to find; opposite: abundant (plentiful). Grew from 2021 antonym questions (4 asked).")
add(AN, "Choose the word opposite in meaning to the word in bracket:\nAfter the dispute, the two neighbours were (hostile) to each other for many years.",
    ["friendly", "foreign", "famous", "formal"],
    "Hostile = unfriendly, like an enemy; opposite: friendly. Grew from 2021 antonym questions.")
add(AN, "Choose the word opposite in meaning to the word in bracket:\nThe young officer was (reluctant) to accept the transfer, though his seniors pressed him.",
    ["eager", "afraid", "angry", "slow"],
    "Reluctant = unwilling; opposite: eager (willing). Grew from 2021 antonym questions.")
add(AN, "Choose the word opposite in meaning to the word in bracket:\nA (prudent) investor does not put all his savings into a single risky scheme.",
    ["reckless", "wise", "thrifty", "cautious"],
    "Prudent = careful and sensible; opposite: reckless. Wise, thrifty and cautious are near-synonyms (the trap). Grew from 2021 antonym questions.")
add(V, "The concert was so ____ that many people were moved to tears.",
    ["touching", "chaotic", "dull", "loud"],
    "Moved to tears needs an emotional word: touching. Exact repeat of 2025 Q58 (key B in the paper).", src="2025 Q58")
add(V, "The speaker told such a ____ story of the flood that the audience listened in complete silence till the end.",
    ["gripping", "gripped", "grip", "gripper"],
    "Adjective needed before 'story': gripping (holding attention). Gripped is for a person (the audience was gripped). Grew from 2025 vocabulary fill-ins.")
add(V, "Because of the shortage of funds, the committee decided to ____ the plan for a new library until next year.",
    ["shelve", "shell", "shield", "shed"],
    "Shelve = put aside for later. The other three look alike but do not fit. Grew from 2025 context-word questions.")
add(V, "The heavy rain in September has badly ____ the standing paddy crop in the coastal districts.",
    ["affected", "effected", "afflicted", "infected"],
    "Affect = to have an influence on; effect (verb) = to bring about. 'Afflicted' is for a person suffering. A classic confusable pair. Grew from 2018 and 2025 vocabulary.")
add(V, "After a long trial, the judge ____ the accused of all the charges for lack of proof.",
    ["acquitted", "accused", "acquired", "admitted"],
    "Acquit = declare not guilty. 'Accused' is the word in the stem (the trap). Grew from 2025 context-word questions.")

# ================================================================ Block 6 · prepositions (9)
add(P, "The teacher divided the sweets ____ the twelve children of the class in equal shares.",
    ["among", "between", "with", "to"],
    "Among = more than two; between = two. Twelve children, so among. Grew from 2021 prepositions block.")
add(P, "The thief was caught ____ the act of breaking the lock of the shop, and the police took him away.",
    ["in", "at", "on", "by"],
    "Caught in the act (fixed phrase). Grew from 2021 prepositions block.")
add(P, "The teacher was very angry ____ the boy ____ breaking the glass window of the staff room.",
    ["with … for", "at … of", "to … for", "with … on"],
    "Angry WITH a person, angry AT/ABOUT a thing; blame or punish FOR the act. Two blanks make you check both pairs. Grew from 2021 Q56 (envious of) and 2025 multi-blank prepositions.")
add(P, "The delegates from all the states arrived ____ Delhi late at night, after the long delay of their flight.",
    ["in", "at", "to", "on"],
    "Arrive IN a city or country; arrive AT a small place (a station, an airport, the shop). Never 'arrive to'. Grew from 2021 prepositions block.")
add(P, "The little boy takes ____ his father in looks and in his way of speaking, say his neighbours.",
    ["after", "up", "over", "to"],
    "Take after = look or behave like an older relative. Grew from 2021 and 2025 phrasal verbs.")
add(P, "Many girls in the remote area were deprived ____ their share of the family property for years.",
    ["of", "from", "with", "to"],
    "Deprive somebody OF something. Grew from the 2021 prepositions (envious of).")
add(P, "He looks upset; I think he took the criticism ____ heart.",
    ["to", "about", "in", "of"],
    "Take something to heart = feel it deeply. Exact repeat of 2021 Q55.", src="2021 Q55")
add(P, "The new road bridge over the river is still ____ construction, so people use the old ferry.",
    ["under", "in", "on", "at"],
    "Under construction, under repair, under way, under review. Grew from 2021 prepositions block.")
add(P, "Why was he absent ____ the final class of the term when the results were announced?",
    ["from", "of", "to", "at"],
    "Absent FROM. Grew from 2021 adjective + preposition questions.")

# ================================================================ Block 7 · articles (8)
add(AR, "She has ____ MBA degree from a reputed university in the state, and she now works in a bank.",
    ["an", "a", "the", NA],
    "MBA starts with the sound 'em', a vowel SOUND, so 'an'. The sound decides, not the letter. Grew from 2021 and 2025 a/an sound questions.")
add(AR, "____ Ganga is the longest river of India, and it is held sacred by millions of people.",
    ["The", "A", "An", NA],
    "Names of rivers take 'the'. Grew from 2021 articles block (the Himalayas, the Ganga).")
add(AR, "He decided to study in ____ university in Odisha because his elder brother had studied there.",
    ["a", "an", "the", NA],
    "'University' starts with 'yoo', a consonant sound: a university. Grew from 2025 Q31 (a unique perspective).")
add(AR, "My uncle plays ____ guitar very well, and he often performs at weddings in our village.",
    ["the", "a", "an", NA],
    "Musical instruments take 'the' when we speak of playing them: play the guitar. Grew from 2021 articles block.")
add(AR, "Los Angeles has ____ ideal climate.",
    ["an", "the", NA, "a"],
    "'Ideal' begins with a vowel sound, so an. Exact repeat of 2021 Q64 (key D).", src="2021 Q64")
add(AR, "The new teacher is ____ European, but she speaks Odia with a very sweet accent.",
    ["a", "an", "the", NA],
    "'European' starts with the sound 'yoo': a European. Same trap as university, one, useful. Grew from 2025 Q31.")
add(AR, "On weekdays, my younger sister goes to ____ bed at ten o'clock and wakes up at five.",
    [NA, "the", "a", "an"],
    "Go to bed, go to school, go to church: no article when we mean the usual purpose. Grew from 2021 zero-article questions.")
add(AR, "The doctor told the old man to wait for ____ hour before he took the second tablet.",
    ["an", "a", "the", NA],
    "'Hour' has a silent h: the first sound is a vowel, so an hour. Grew from 2021 and 2025 a/an sound questions.")

# ================================================================ Block 8 · tenses (5)
add(T, "If the rain had stopped an hour earlier, we ____ the match in the school ground.",
    ["would have played", "would play", "had played", "will have played"],
    "Third conditional: If + had + past participle … would have + past participle. Grew from 2025 conditionals (Had she known).")
add(T, "The driver ____ the truck at a high speed when the front tyre burst and the truck hit a tree.",
    ["was driving", "drove", "had driven", "has driven"],
    "A long action in progress when another cut in: past continuous. Grew from 2018 and 2021 past-continuous questions.")
add(T, "I ____ this novel for two weeks, but I have not finished even half of it yet.",
    ["have been reading", "am reading", "had read", "read"],
    "Action that began in the past and is still going on, with a length of time (two weeks): present perfect continuous. Grew from 2018 and 2025 (has been living … for five years).")
add(T, "By this time next year, my sister ____ her engineering degree and started working in Pune.",
    ["will have completed", "will complete", "has completed", "completed"],
    "'By this time next year' = a point in the future by which something is finished: future perfect. Grew from 2021 Q73–76 (future perfect).")
add(T, "I wish I ____ a car of my own; then I could drive to the office instead of waiting for the crowded bus every morning.",
    ["had", "have", "would have", "will have"],
    "After 'wish' about a present unreal situation, the verb takes the simple past: I wish I HAD a car (but I do not). 'Have' and 'will have' are the trap. Grew from 2025 conditional and wish items.")

# ================================================================ Block 9 · voice change (4) [extra practice, not in the printed syllabus list]
VO = "Choose the correct passive form of the sentence (or the correct active form, if the sentence is passive):\n"
add(VB, VO + "The villagers built a small bridge over the stream last year.",
    ["A small bridge was built over the stream by the villagers last year.",
     "A small bridge is built over the stream by the villagers last year.",
     "A small bridge was being built over the stream by the villagers last year.",
     "A small bridge had been built over the stream by the villagers last year."],
    "Simple past active (built) → was/were + past participle (was built). The tense stays the same. 'Was being built' is the continuous form, and 'had been built' is the past perfect: both change the tense.")
add(VB, VO + "You must complete the form before Friday.",
    ["The form must be completed by you before Friday.",
     "The form must complete by you before Friday.",
     "The form must have been completed by you before Friday.",
     "The form must be complete by you before Friday."],
    "Modal active → modal + be + past participle: must be completed. A common slip is leaving out 'be' or using the base verb.")
add(VB, VO + "Why did the manager reject the application?",
    ["Why was the application rejected by the manager?",
     "Why the application was rejected by the manager?",
     "Why did the application be rejected by the manager?",
     "Why has the application been rejected by the manager?"],
    "A past-simple question with 'did' becomes 'was/were + past participle' in the passive, and 'did' disappears. The question order stays (Why was …?). 'Why the application was …' loses the inversion; 'did … be rejected' is not English.")
add(VB, VO + "The thief was being chased by the police through the narrow lanes.",
    ["The police were chasing the thief through the narrow lanes.",
     "The police was chasing the thief through the narrow lanes.",
     "The police chased the thief through the narrow lanes.",
     "The police had chased the thief through the narrow lanes."],
    "Passive continuous (was being chased) → active past continuous (were chasing). 'Police' takes a plural verb (were), a small trap. Keep the tense.")

# ================================================================ Block 10 · direct and indirect speech (3) [extra practice]
SP = "Choose the correct indirect (reported) form of the sentence:\n"
add(VB, SP + "He said, \"I will help you tomorrow.\"",
    ["He said that he would help me the next day.",
     "He said that he will help you tomorrow.",
     "He said that he would help you the next day.",
     "He said that he would help me tomorrow."],
    "Reporting verb in the past: will → would; I → he; you → me; tomorrow → the next day. Four changes, so check each. '… would help me tomorrow' forgets to change 'tomorrow'.")
add(VB, SP + "She asked me, \"Where do you live?\"",
    ["She asked me where I lived.",
     "She asked me where did I live.",
     "She asked me where do I live.",
     "She asked me that where I lived."],
    "A question becomes a statement order in reported speech (no 'do/did'), and the tense moves back: do live → lived. No 'that' with a question word.")
add(VB, SP + "The teacher said to the boys, \"Do not make a noise.\"",
    ["The teacher ordered the boys not to make a noise.",
     "The teacher ordered the boys do not make a noise.",
     "The teacher told the boys that they do not make a noise.",
     "The teacher asked the boys not making a noise."],
    "A command becomes 'ordered/told + object + (not) to + verb'. A negative command uses 'not to'. 'ordered the boys do not' and 'asked … not making' break the infinitive.")

# ================================================================ Block 11 · rearrangement (6): small letters, no full stops, no clue from the first letter
RS = "Rearrange the following parts to make a meaningful sentence:\n"
def rs(parts, right, wrong, e):
    t = RS + "\n".join("%s: %s" % (l, p) for l, p in zip("PQRS", parts))
    add(RE, t, [right] + wrong, e)
rs(["will be opened next month", "over the river", "the new bridge", "by the chief minister"],
   "RQPS", ["RPQS", "QRPS", "SRQP"],
   "the new bridge (R) over the river (Q) will be opened next month (P) by the chief minister (S). Find the subject first (R), then the phrase that belongs to it (Q), then the verb (P); the doer (by …) comes last. Method from the 2025 rearrangement questions.")
rs(["the students rushed out", "of the hall", "when the examination ended", "with great relief"],
   "RPQS", ["RQPS", "PRQS", "RPSQ"],
   "when the examination ended (R) the students rushed out (P) of the hall (Q) with great relief (S). The time clause opens; 'out' must be followed by 'of the hall'. Same method as 2025.")
rs(["who had waited patiently", "the old man", "was finally given", "a seat by the conductor"],
   "QPRS", ["QRPS", "PQRS", "SQPR"],
   "the old man (Q) who had waited patiently (P) was finally given (R) a seat by the conductor (S). 'Who' follows the noun it describes; the verb comes next. Grew from 2025.")
rs(["but also extremely wise", "the soldier was", "in his decisions", "not only brave"],
   "QSPR", ["QPSR", "SQPR", "QSRP"],
   "the soldier was (Q) not only brave (S) but also extremely wise (P) in his decisions (R). 'Not only' comes before 'but also'; the phrase 'in his decisions' ends the sentence. Grew from 2021 and 2025.")
RP = "Rearrange the following sentences to make a meaningful paragraph:\n"
add(RE, RP + "\n".join("%s: %s" % (l, p) for l, p in zip("PQRS", [
    "he watered it daily and protected it from the goats",
    "after some years the tree bore its first sweet fruits",
    "a farmer planted a small mango seed near his hut",
    "the whole village then came to taste them"])),
    ["RPQS", "RQPS", "PRQS", "RPSQ"],
    "Start with the first event: a farmer planted a seed (R). 'It' in P points back to the seed, so P follows R. The fruits (Q) come after the years, and 'them' in S points to the fruits, so S is last. "
    "Grew from 2025 paragraph rearrangement.")
add(RE, RP + "\n".join("%s: %s" % (l, p) for l, p in zip("PQRS", [
    "this is why farmers in Odisha wait anxiously for it every June",
    "the monsoon winds blow from the south-west",
    "they carry moisture from the Indian Ocean",
    "when they meet the hills the moisture falls as rain"])),
    ["QRSP", "QSRP", "RQSP", "QRPS"],
    "Start with the topic: the monsoon winds (Q). 'They' in R refers to the winds, so R is second. Then the rain (S). 'This is why …' (P) sums up and closes the paragraph. "
    "Words like 'they' and 'this' always point back; they cannot open a paragraph. Grew from 2025.")

# ================================================================ Block 12 · subject-verb agreement (10)
add(SV, "Either the principal or the two vice-principals ____ to sign the letter before it goes to the Director.",
    ["have", "has", "is", "was"],
    "Either…or: the verb agrees with the NEAREST subject, vice-principals (plural): have. Grew from 2021 and 2025 neither-nor / either-or questions.")
add(SV, "The number of unemployed youths in the district ____ increasing every year, say the officials.",
    ["is", "are", "were", "have been"],
    "'The number of' = singular (the number is). 'A number of' = plural. Grew from 2021 agreement block.")
add(SV, "A number of unemployed youths ____ gathered outside the office to ask for jobs.",
    ["have", "has", "is", "was"],
    "'A number of' means 'many', so the verb is plural: have. The pair 'the number / a number' is a favourite of the examiner.")
add(SV, "Each of the girls in the hostel ____ a separate cupboard for her books and clothes.",
    ["has", "have", "are having", "were"],
    "'Each' is singular: each has. The plural noun after 'of' is the trap. Grew from 2021 Q83–92.")
add(SV, "Mathematics ____ my favourite subject, but physics is the one that I find difficult.",
    ["is", "are", "were", "have been"],
    "Names of subjects ending in -s (mathematics, physics, economics, politics) take a singular verb. Grew from 2021 agreement block.")
add(SV, "The Arabian Nights ____ a famous collection of stories that has been read by children for centuries.",
    ["is", "are", "were", "have been"],
    "The title of a book, film or newspaper is ONE thing, so the verb is singular, even if the title looks plural (Gulliver's Travels is). Grew from 2021 and 2025 agreement questions.")
add(SV, "Ten thousand rupees ____ a big amount for a student to pay as a deposit for a hostel room.",
    ["is", "are", "were", "have been"],
    "A sum of money, a distance or a period of time is seen as ONE amount: singular. Grew from the 2021 agreement block (the 'number + unit' idea, Rule 6 in the Guide).")
add(SV, "More than one candidate ____ failed in the test, so the board decided to hold a re-test.",
    ["has", "have", "are", "were"],
    "'More than one' takes a singular noun and a singular verb, though it means many. (Many a student has, More than one has.) Grew from 2021 'many a' questions.")
add(SV, "Half of the mangoes in the basket ____ rotten, and the shopkeeper took them away.",
    ["were", "was", "is", "has been"],
    "With 'half of / some of / most of', the verb agrees with the noun after 'of': mangoes (plural), so were. 'Half of the cake was.' Grew from 2021 and 2025 'of'-phrase questions.")
add(SV, "One of the boys who ____ late for the morning assembly was punished by the headmaster.",
    ["were", "was", "is", "has been"],
    "'Who' refers to 'boys' (plural), so the verb in the 'who' clause is were. The main verb 'was punished' goes with 'one'. A two-step question. Grew from 2025 'one of the … who' items.")

# ================================================================ Block 13 · comprehension (5)
P1 = (
"Sambalpuri ikat is one of the best-known handloom traditions of Odisha. It takes its name from Sambalpur in the western part of the state, "
"but weavers in Bargarh, Bolangir and Sonepur also practise it. The word 'ikat' means 'to tie'. Before any cloth is woven, the threads are tied "
"tightly in small bundles and dipped in dye. The tied parts do not take the colour, and when the ties are removed, a pattern appears on the "
"thread itself.\n\n"
"This work needs great patience. A weaver must plan the whole design in advance, because the threads are dyed in the order in which they will "
"be woven. If one thread is out of place, the design on the finished cloth looks broken. A single saree can take several weeks, and sometimes "
"months, to complete. The motifs, such as the shell, the wheel and the flower, are taken from temples and from everyday village life.\n\n"
"In recent years, cheap power-loom copies have hurt the weavers. The machine-made cloth sells at a lower price, though it lacks the soft blur at "
"the edges of each pattern that marks true ikat. To help the craft, several cooperatives now train young people and sell directly to buyers in "
"cities. Many weavers say that the demand for handmade cloth is growing again, but they feel that buyers must learn to look for the original.")
PRE1 = "Read the passage on Sambalpuri ikat and answer the question.\n"
add(CO, PRE1 + "Which is the most suitable title for the passage?",
    ["Sambalpuri Ikat: A Patient Craft of Odisha", "The Rise of Power Looms in India", "Temple Art of Western Odisha", "How Colours Are Made from Plants"],
    "The passage explains what ikat is, how it is made, and the trouble from machine copies. The first title covers all of it; the others are too narrow or not mentioned. Title questions grew from 2018 comprehension.",
    p=P1, g="p1")
add(CO, PRE1 + "According to the passage, what happens when the ties on the threads are removed?",
    ["A pattern appears on the thread", "The cloth becomes soft", "The colour fades away", "The thread breaks into small pieces"],
    "Paragraph 1: 'when the ties are removed, a pattern appears on the thread itself.' A detail question: the answer is a line of the passage in other words. 2025 had mostly detail questions.",
    p=P1, g="p1")
add(CO, PRE1 + "Why must a weaver plan the whole design in advance?",
    ["Because the threads are dyed in the order in which they will be woven", "Because the cloth must be sold quickly",
     "Because buyers ask for new motifs every month", "Because machines copy the design"],
    "Paragraph 2: 'the threads are dyed in the order in which they will be woven.' An inference-in-detail question: the reason is given in the text.",
    p=P1, g="p1")
add(CO, PRE1 + "The word 'motifs' in paragraph 2 means:",
    ["repeated designs", "tools of a weaver", "colours of dye", "names of villages"],
    "Motifs = designs or patterns (the shell, the wheel, the flower). The examples after the word give the meaning. Vocabulary-in-context questions grew from 2018 and 2025 comprehension.",
    p=P1, g="p1")
add(CO, PRE1 + "Which of the following is NOT true according to the passage?",
    ["Power-loom cloth shows the soft blur at the edges of the pattern", "Ikat is also woven in Bargarh and Sonepur",
     "A single saree may take months to complete", "Cooperatives train young people in the craft"],
    "Paragraph 3 says machine-made cloth LACKS the soft blur, so the first statement is false; the other three are in the passage (paragraphs 1, 2 and 3). A 'NOT true' question: check each option against the text.",
    p=P1, g="p1")
