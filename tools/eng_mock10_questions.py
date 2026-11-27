# English Mock 10 · redo set after English Mock 09 (27 Nov 2026), 2021 layout, level hard.
# The user pasted the Mock 09 Copy answers report (Net 70.00: 75 right, 20 wrong, 5 skipped).
# 25 redo questions (every wrong and skipped one, options reshuffled, "Redo · M09 Qn" in the explanation),
# 25 same-rule twins ("Same rule · M09 Qn"), each kept apart from its redo, and 50 new questions
# drawn with: python3 .claude/skills/aso-mock/scripts/draw.py english --n 100 --seed 489289
# (its exact repeats 2025 Q10, 2021 Q5 and 2021 Q12 are kept).
# First option is the right one unless a is given (then the options stay in the printed order).
import os, runpy

META = dict(
    paper="english",
    title="ASO English Mock 10",
    hub_title="English Mock 10 · redo",
    masthead="English Mock 10",
    heading="English Paper III · Mock 10 (redo set)",
    tagline="Your 25 missed questions from Mock 09,<br>25 <b>same-rule twins</b> and 50 new ones.",
    key="aso-english-mock-2027-10",
    code="M10",
    out="ASO-English-Mock-Test-2027-10.html",
    minutes=45,
    seed=20261128,
    order="given",
    date="27 Nov 2026",
    draw="python3 .claude/skills/aso-mock/scripts/draw.py english --n 100 --seed 489289 (50 new slots; 25 redo and 25 twins from the Mock 09 report)",
    intro=[
        "This is the redo set for English Mock 09 (you scored 70.00). Every question you got wrong or skipped is back, "
        "with its options in a new order, and each one has a new twin that tests the same rule in a fresh sentence. "
        "The explanation of a redo question starts with 'Redo · M09' and says what you picked last time; a twin starts with 'Same rule · M09'. "
        "The other 50 questions are new and drawn by probability.",
        "The paper keeps the 2021 layout and the hard level of Mock 09. Three are exact past questions: 2021 Q12 (because of they dislike him), "
        "2021 Q5 (With regard to) and 2025 Q10 (The train had left). The passage is about learning in the home language first. "
        "Read Weak Spots Guide 2 before or after this mock: it explains every rule you missed.",
    ],
)

Q = []
def add(s, q, o, e, k="one", n=False, c=False, a=None, **x):
    d = dict(s=s, q=q, o=o, e=e, k=k, n=n, c=c, a=a); d.update(x); Q.append(d)

V, T, SV, P, AD, AR, VB, ER, SY, AN, CO, RE, PS = ("Vocabulary", "Tenses", "Subject–verb agreement", "Preposition", "Adverb",
    "Articles", "Verb", "Error spotting", "Synonyms", "Antonyms", "Comprehension", "Sentence rearrangement", "Parts of speech")
NA = "No article"
IMP = "Choose how the part in brackets can be improved. If no change is needed, choose 'No improvement'.\n"
POS = "Choose the correct part of speech for the word in bracket:\n"
PICK = "Choose the grammatically correct sentence:"
SEG = "Identify the incorrect segment in the sentence below:\n"

# ---------------------------------------------------------------- redo helper: M09 is in booklet order, so M09 Qn = its Q[n-1]
M9 = runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), "eng_mock9_questions.py"))["Q"]
PICKED = {3: "would have felt", 4: "we saw", 10: "less nervous you will feel", 12: "not mention", 14: "was because",
          19: "to be", 22: "Preposition", 28: "the 'whom' sentence", 31: "He is as tall, if not taller than, his brother.",
          32: "The boy resembles with his father in every way.", 34: "the Koraput hills", 36: "are", 43: "false",
          45: "(II) and (IV)", 47: "Clarity", 51: "Anger", 54: "eloquent", 63: "away", 77: "wins", 81: "is"}
def redo(n, order=None):
    q = dict(M9[n - 1])
    right = q["o"][q["a"] if q.get("a") is not None else 0]
    was = ("Last time you chose '%s'. " % PICKED[n]) if n in PICKED else "Last time you skipped it. "
    q["e"] = "Redo · M09 Q%d. %s%s" % (n, was, q["e"])
    if order is not None:                      # new printed order for fixed-order questions
        q["o"] = order; q["a"] = order.index(right)
    Q.append(q)

# ================================================================ Block 1 · mixed grammar opener (20)
redo(12)
add(P, "The prize-giving was held ____ the big hall ____ the first floor ____ ten o'clock in the morning.",
    ["in, on, at", "at, in, on", "on, at, in", "in, at, on"],
    "Inside a room or hall: in. A floor or level of a building: on. An exact clock time: at. Grew from the multi-blank prepositions of 2018 and 2021.")
redo(3)
add(AD, "The new phone is ____ too expensive for a student like me to buy.",
    ["much", "very", "so", "more"],
    "'Too' + adjective is made stronger with 'much' or 'far' (much too expensive), not with 'very'. 'Very too' is never used. Grew from 2025 adverb questions (intensifiers).")
redo(10)
redo(19)
redo(18)
redo(4)
add(ER, "Choose from the options how the sentence can be improved: They could not admire his bright performance (because of they dislike him).",
    ["because of their disliking of him", "because of their dislike him", "because they dislike him", "No correction required"],
    "'Because of' is followed by a noun or pronoun; 'because' is followed by a full clause (subject + verb): because they dislike him. "
    "Same family as M09 Q14 ('the reason is that').", a=2, src="2021 Q12")
add(VB, "Speak softly in the ward lest you ____ the sleeping patients.",
    ["should disturb", "will disturb", "may not disturb", "should not disturb"],
    "Same rule · M09 Q29 (lest). 'Lest' already means 'so that … not', so it is followed by 'should' and never by another 'not'. 'Will' is not used after lest.")
redo(81)
add(AD, "He felt ____ about leaving his old parents alone in the village, but the new job was in Delhi.",
    ["bad", "badly", "worse than", "baddest"],
    "'Feel' here is a linking verb (it describes his state), so it takes an adjective: felt bad. 'Felt badly' would describe how he used his sense of touch. "
    "Grew from 2025 adjective-or-adverb questions (felt tired).")
redo(63)
add(ER, IMP + "The officer (whom everyone believed) was honest was later caught taking a bribe.",
    ["who everyone believed", "whom everyone believed it", "that everyone believed him", "No improvement"],
    "Same rule · M09 Q28. Take out the inserted clause 'everyone believed': 'The officer who was honest'. The relative word is the subject of 'was', so it is 'who', not 'whom'.", a=0)
add(VB, "Choose the correct passive form: Somebody should have told me about the change of venue.",
    ["I should have been told about the change of venue.", "I should be told about the change of venue.",
     "I should have told about the change of venue.", "I should have being told about the change of venue."],
    "Modal perfect in the passive: should have + been + past participle. 'Should be told' changes the time to the present or future; 'have being' is never used. "
    "Grew from the voice questions of 2018 and 2021.")
add(P, "We reached the station ____ time for the train, with five minutes to spare.",
    ["in", "on", "at", "by"],
    "In time = early enough, with some time left (the clue: five minutes to spare). On time = exactly at the fixed time. Grew from the 2021 and 2025 time prepositions.")
add(ER, IMP + "Our village school is (as good, if not better than,) the private school in town.",
    ["as good as, if not better than,", "as good, if not better,", "good as, if not better than,", "No improvement"],
    "Same rule · M09 Q31. Each half must stand on its own: 'as good as the school' and 'better than the school'. Only the first option keeps both 'as … as' and 'than'.", a=0)
add(VB, "My father would rather I ____ a job in Odisha than move to a big city far away.",
    ["took", "take", "taken", "had to take"],
    "Same rule · M09 Q12. 'Would rather' + another person + past simple, for the present or future: would rather I took. The past form here does not mean past time.")
redo(14, order=["is that", "was because", "is due to", "No improvement"])
add(VB, "After a long talk with the manager, the clerk admitted ____ the files home without permission.",
    ["having taken", "to have taken", "to take", "have taken"],
    "Same rule · M09 Q19 (denied having been). Admit, deny, avoid, mind, regret take the -ing form, never to. For an earlier act, the perfect gerund 'having taken' is best.")

# ================================================================ Block 2 · parts of speech (6)
redo(22)
add(PS, POS + "Nobody (but) the old watchman knew the way to the cave.",
    ["Preposition", "Conjunction", "Adverb", "Adjective"],
    "Same rule · M09 Q25. 'But' means 'except' and stands before a noun (the old watchman), so it is a preposition. It is a conjunction only when it joins two clauses or words of equal rank.")
redo(26)
add(PS, POS + "I met him at the fair in 2019, but I have not seen him (since).",
    ["Adverb", "Preposition", "Conjunction", "Adjective"],
    "Same rule · M09 Q22 (before). With nothing after it, 'since' tells when and modifies the verb: an adverb. 'Since 2019' would make it a preposition, 'since he left' a conjunction.")
redo(25)
add(PS, POS + "(Tired) of waiting in the hot sun, the villagers went back to their homes.",
    ["Participle", "Gerund", "Infinitive", "Noun"],
    "Same rule · M09 Q26 (Seeing). 'Tired of waiting' describes the villagers, so it works like an adjective: a past participle. A participle phrase at the start of a sentence describes the subject that follows.")

# ================================================================ Block 3 · pick the correct sentence, spot the error (8)
add(ER, SEG + "[The machinery in] [the old rice mill] [have been] [sold as scrap.]",
    ["The machinery in", "the old rice mill", "have been", "sold as scrap."],
    "Same rule · M09 Q34 (scenery). 'Machinery' is uncountable (like scenery, furniture, luggage), so it takes a singular verb: has been sold.", a=2)
redo(28)
add(ER, PICK,
    ["The higher you climb, the colder it becomes.", "The higher you climb, colder it becomes.",
     "Higher you climb, the colder it becomes.", "The higher you climb, the more colder it becomes."],
    "Same rule · M09 Q10. 'The + comparative …, the + comparative …': 'the' is needed in both halves, and a short adjective takes -er alone (never 'more colder').")
redo(29)
add(ER, PICK,
    ["The reason for his absence is that he was ill.", "The reason for his absence is because he was ill.",
     "The reason for his absence is due to he was ill.", "The reason for his absence is because of he was ill."],
    "Same rule · M09 Q14. After 'the reason … is', use 'that' + clause. 'Because' repeats the idea of reason; 'due to' and 'because of' cannot take a clause.")
redo(31)
redo(32)
redo(34)

# ================================================================ Block 4 · mixed tenses, agreement, adverbs (6)
add(T, "If she had not missed the last bus last night, she ____ so tired at the office now.",
    ["would not be", "would not have been", "will not be", "had not been"],
    "Same rule · M09 Q3. Mixed conditional: the condition is past (last night), the result is present (now), so use would + base verb. 'Would not have been' would be a past result.")
add(SV, "The pair of gold earrings that she lost at the wedding ____ found under the stage the next morning.",
    ["was", "were", "have been", "are"],
    "Same rule · M09 Q36. The subject is 'pair', which is singular. 'Earrings' alone would take a plural verb. The words in between do not change it.")
add(AD, "Only by working late every night ____ to finish the report on time.",
    ["was she able", "she was able", "she could be able", "able she was"],
    "Same rule · M09 Q4. 'Only' + a phrase or clause at the start (only by, only when, only after) puts the helping verb before the subject: was she able.")
add(T, "It is the first time I ____ such a long journey on my own.",
    ["have made", "made", "had made", "make"],
    "Same rule · M09 Q77. 'It is (this is) the first time' is followed by the present perfect: have made. With 'It was the first time', use the past perfect.")
add(SV, "The team ____ selected its new captain for the coming season.",
    ["has", "have", "are", "were"],
    "A collective noun acting as one unit takes a singular verb, and the pronoun 'its' confirms it. 'Their' would show the members acting separately. "
    "Grew from 2021 and 2025 collective-noun questions.")
add(AD, "Start for the station at once; ____, you will miss the last train to Puri.",
    ["otherwise", "however", "therefore", "besides"],
    "'Otherwise' means 'if not': if you do not start now, you will miss the train. 'However' shows contrast, 'therefore' result, 'besides' addition. "
    "Grew from 2025 connector questions.")

# ================================================================ Block 5 · vocabulary (16)
redo(43)
add(SY, "Choose the word most similar in meaning to ALLEVIATE:",
    ["Relieve", "Aggravate", "Elevate", "Allocate"],
    "Same rule · M09 Q44 (ameliorate). Alleviate = make pain or trouble less severe (alleviate poverty). Aggravate is its opposite; elevate and allocate only sound alike.")
redo(45)
add(SY, "Choose the word closest in meaning to the word in bracket:\nThe two brothers stopped speaking to each other over a (petty) quarrel about a mango tree.",
    ["unimportant", "angry", "frequent", "bitter"],
    "Same rule · M09 Q43 (frivolous). Petty = small and unimportant. 'Angry' and 'bitter' describe a quarrel too, but they are not what 'petty' means.")
redo(44)
add(SY, "Select the pair of synonyms:\n(I) Meagre (II) Ample (III) Scanty (IV) Costly",
    ["(I) and (III)", "(II) and (IV)", "(I) and (II)", "(II) and (III)"],
    "Same rule · M09 Q45. Meagre and scanty both mean too little. Ample means more than enough, the opposite of both; costly is about price.")
redo(47)
add(AN, "Choose the word most opposite in meaning to ARDOUR:",
    ["Indifference", "Passion", "Heat", "Courage"],
    "Same rule · M09 Q51 (zeal). Ardour = great eagerness or warmth of feeling. Its opposite is indifference, a lack of interest. Passion and heat are synonyms.")
add(AN, "Choose the word most opposite in meaning to OBSCURE (as in 'an obscure village poet'):",
    ["Famous", "Hidden", "Humble", "Unknown"],
    "Obscure here means little known. Its opposite is famous. Hidden and unknown are close to synonyms. Grew from the four antonyms of 2021.")
add(AN, "Choose the word most opposite in meaning to DEFIANCE:",
    ["Obedience", "Rebellion", "Confidence", "Silence"],
    "Same rule · M09 Q47 (subversion). Defiance = open refusal to obey. Its opposite is obedience. Rebellion is a synonym.")
redo(51)
redo(54)
add(V, "The new medicine gave only ____ relief; within an hour the pain came back as bad as before.",
    ["momentary", "lasting", "complete", "permanent"],
    "Momentary = lasting a very short time. The clue is 'within an hour the pain came back'. Grew from the 2025 one-blank vocabulary questions.")
add(V, "The witness was so ____ that he changed his story three times in one hour, and the judge refused to believe him.",
    ["inconsistent", "reliable", "truthful", "confident"],
    "Inconsistent = not staying the same. Changing the story three times is the clue; reliable and truthful are the opposite. Grew from the 2025 one-blank vocabulary questions.")
add(V, "In which sentence is the word 'fine' used to mean 'money paid as a punishment'?",
    ["He had to pay a fine for driving without a helmet.", "The weather was fine all week.",
     "She wrote with a fine pen.", "I am fine, thank you."],
    "A fine is money paid for breaking a rule. The other sentences use 'fine' as an adjective: pleasant, thin, well. Grew from 2018 word-meaning questions (a word with many meanings: bar).")
add(V, "His report was ____: just two pages, yet it said everything the committee needed to know.",
    ["crisp", "lengthy", "eloquent", "vague"],
    "Same rule · M09 Q54 (succinct). Crisp = short and clear. 'Eloquent' (moving, well spoken) is again the trap; the clue is length (two pages) and clarity.")

# ================================================================ Block 6 · prepositions (10)
add(P, "____ his principles, he has to be very careful.",
    ["With regard of", "With regard on", "With regard to", "None of these"],
    "The fixed phrase is 'with regard to' (= about, concerning), like 'in regard to' and 'as regards'. Family: phrase prepositions (according to, based on).", a=2, src="2021 Q5")
add(P, "The small hospital could not cope ____ the rush of patients after the bus accident.",
    ["with", "up", "for", "by"],
    "Same rule · M09 Q18 (dispense with). Cope with = deal with a difficulty. Verb + preposition pairs are fixed and must be learnt as pairs.")
add(P, "She takes ____ her mother; she has the same eyes and the same loud laugh.",
    ["after", "to", "up", "on"],
    "Take after = look or behave like an older family member. Take to = begin to like; take up = start a hobby; take on = accept work. Grew from 2021 and 2025 phrasal verbs.")
add(P, "The success of the whole plan hinges ____ the support of the villagers.",
    ["on", "in", "at", "with"],
    "Hinge on (or upon) = depend on. Grew from the verb + preposition family (lies in, focuses on).")
add(P, "The factory was fined for failing to dispose ____ its waste safely.",
    ["of", "off", "with", "from"],
    "Same rule · M09 Q63 (part with). Dispose of = get rid of. 'Off' is the sound-alike trap. Fixed verb + preposition.")
add(P, "Being a quiet man, he was always averse ____ long speeches and big functions.",
    ["to", "from", "of", "against"],
    "Averse to = not liking something (like opposed to). Grew from the 2018 and 2021 adjective + preposition pairs.")
add(P, "The rescue team ____ the flooded village only after the water went down.",
    ["reached", "reached at", "reached to", "reached in"],
    "Same rule · M09 Q32 (resemble). 'Reach' takes its object directly, with no preposition: reached the village. Compare 'arrived at the village'.")
add(P, "We sat ____ the shade of a big banyan tree and ate our lunch.",
    ["in", "under", "below", "on"],
    "We sit 'in the shade' (inside the shaded area) but 'under the tree'. 'Under the shade' is a common mistake. Grew from 2021 and 2025 place prepositions.")
add(P, "____ the absence of the Principal, the senior-most teacher took the morning assembly.",
    ["In", "On", "At", "For"],
    "The fixed phrase is 'in the absence of' (also 'in the presence of'). Grew from 2021 phrase prepositions.")
add(P, "A fierce quarrel ____ between the two families over the boundary of a small field.",
    ["broke out", "broke up", "broke in", "broke off"],
    "Break out = start suddenly (a fire, a war, a quarrel). Break up = end; break in = enter by force; break off = stop suddenly. Grew from 2021 and 2025 phrasal verbs.")

# ================================================================ Block 7 · articles (10)
add(AR, "He bought ____ umbrella and ____ raincoat, but forgot to collect ____ boots he had ordered last week.",
    ["an, a, the", "a, a, the", "an, a, a", "an, the, the"],
    "Umbrella begins with a vowel sound (an); raincoat with a consonant sound (a); the boots are particular ones he had ordered (the). Grew from 2021 multi-blank article questions.")
add(AR, "There is ____ eucalyptus tree at the gate of our school.",
    ["a", "an", "the", NA],
    "Eucalyptus is said 'yoo-ka-lip-tus', which begins with a consonant sound (y), so 'a eucalyptus'. 'There is' introduces something new, so it takes a/an, not the. The spelling begins with a vowel, but the sound decides. "
    "Grew from 2021 and 2025 a/an questions (a unique, a European).")
add(AR, "Every family in the village now cooks on ____ LPG stove.",
    ["an", "a", "the", NA],
    "L is read 'el', which begins with a vowel sound, so 'an LPG stove'. Grew from the a/an family (an MLA).")
add(AR, "He was sworn in as ____ Union minister at the age of forty-two.",
    ["a", "an", "the", NA],
    "'Union' is said 'yoon-yun', which begins with the consonant sound y, so 'a Union minister'. Grew from the a/an family (a unique).")
add(AR, "The stranded fishermen sent ____ SOS message from their boat.",
    ["an", "a", "the", NA],
    "S is read 'es', a vowel sound, so 'an SOS'. Grew from the a/an family.")
add(AR, "The chief guest gave ____ hour-long speech on clean villages.",
    ["an", "a", "the", NA],
    "The 'h' of 'hour' is silent, so 'hour-long' begins with a vowel sound: an hour-long speech. Grew from the a/an family (an honour).")
add(AR, "After the vote, Meena was elected ____ captain of the school hockey team.",
    [NA, "a", "the", "an"],
    "After elect, appoint, make or crown, a post held by one person takes no article: elected captain, appointed Principal. Grew from the zero-article family of 2021 and 2025.")
add(AR, "In our village most people travel to Bhubaneswar by ____ train.",
    [NA, "a", "the", "an"],
    "'By' + a means of transport takes no article: by train, by bus, by air. With a particular train, use the article: on the morning train. Grew from the zero-article family.")
add(AR, "Many ships carrying oil from the Gulf cross ____ Indian Ocean every day.",
    ["the", "a", "an", NA],
    "Names of oceans, seas and rivers take 'the': the Indian Ocean, the Bay of Bengal, the Mahanadi. Grew from the 'the' family of 2021 and 2025.")
add(AR, "____ Lingaraj Temple in Bhubaneswar draws thousands of pilgrims every day.",
    ["The", "A", "An", NA],
    "Names of famous buildings and temples take 'the': the Lingaraj Temple, the Taj Mahal, the Sun Temple. Grew from the 'the' family.")

# ================================================================ Block 8 · tenses (5)
add(T, "The train ____ before she started from home.",
    ["had left", "left", "has left", "will leave"],
    "Two past actions: the earlier one (the train leaving) takes the past perfect. Family: past perfect (M09 Q11).", src="2025 Q10")
redo(77)
add(T, "Please don't phone at eight o'clock; we ____ dinner then.",
    ["will be having", "will have had", "have", "had"],
    "An action that will be going on at a future moment takes the future continuous: will be having. 'Will have had' would mean dinner is over, so phoning would be fine. "
    "Grew from 2025 future-tense questions.")
add(T, "He talks as though he ____ everything about farming, but he has never worked in a field.",
    ["knew", "knows", "has known", "will know"],
    "Same rule · M09 Q81 (as if she were). 'As if' and 'as though' for something untrue take the past form: as though he knew. The last part shows it is untrue.")
add(T, "I ____ him at the bus stand yesterday, but he did not see me.",
    ["saw", "have seen", "had seen", "was seeing"],
    "A finished action at a stated past time (yesterday) takes the past simple. 'See' is a state verb and is not used in -ing forms. Grew from 2018 and 2021 past-simple questions.")

# ================================================================ Block 9 · rearrangement (4)
RS = "Rearrange the following parts to make a meaningful sentence:\n"
def rs(parts, right, wrong, e):
    add(RE, RS + "\n".join("%s: %s" % (l, p) for l, p in zip("PQRS", parts)), [right] + wrong, e)
rs(["was rushed to the hospital", "the old man", "who had collapsed", "on the platform"],
   "QRSP", ["QPRS", "RSQP", "QRPS"],
   "the old man (Q) who had collapsed (R) on the platform (S) was rushed to the hospital (P). 'Who' follows the noun it describes, and the main verb comes after the whole subject. Method from 2025.")
rs(["than to make excuses", "it is better", "and correct it", "to admit a mistake"],
   "QSRP", ["QPSR", "SRQP", "QSPR"],
   "it is better (Q) to admit a mistake (S) and correct it (R) than to make excuses (P). 'Better … than' compares two infinitives; 'it' in R needs 'a mistake' before it. Same method as 2025.")
rs(["neither", "nor his brother", "came to the meeting", "Ramesh"],
   "PSQR", ["SPQR", "PQSR", "SRPQ"],
   "neither (P) Ramesh (S) nor his brother (Q) came to the meeting (R). 'Neither' stands just before the first of the two persons and 'nor' before the second. Grew from 2025 rearrangement.")
add(RE, "Rearrange the following sentences to make a meaningful paragraph:\n" + "\n".join("%s: %s" % (l, p) for l, p in zip("PQRS", [
    "the trees held the rain and let it flow slowly into the river",
    "as a result the river now floods the low fields every monsoon",
    "for centuries the hills above the village were covered with thick forest",
    "in the last thirty years however most of that forest has been cut down"])),
    ["RPSQ", "RSPQ", "PRSQ", "RPQS"],
    "R opens with the time and the forest. P ('the trees') follows it. S turns the story with 'however'. Q ('as a result') gives the effect and closes. "
    "Linkers such as however and as a result point back, so they never open a paragraph. Grew from 2025 paragraph rearrangement.")

# ================================================================ Block 10 · subject-verb agreement (10)
add(SV, "The Minister, with his two secretaries, ____ arrived for the review meeting.",
    ["has", "have", "are", "were"],
    "'With', 'along with', 'as well as' do not join subjects; the verb agrees with the first noun (Minister). Grew from 2021 and 2025 'as well as' questions.")
add(SV, "Not the players but the coach ____ to blame for the team's poor show.",
    ["is", "are", "were", "have been"],
    "In 'not X but Y', the verb agrees with Y, the one that is really meant: the coach is to blame. Grew from the 'as well as' family.")
add(SV, "Time and tide ____ for no man.",
    ["wait", "waits", "is waiting", "has waited"],
    "Two different things joined by 'and' take a plural verb: time and tide wait. (When the two make one idea, like 'bread and butter', the verb is singular.) "
    "Grew from 2021 and 2025 'and' questions.")
add(SV, "The Secretary and the Treasurer of the club ____ been asked to resign.",
    ["have", "has", "is", "was"],
    "'The' is repeated before each title, so they are two different people: plural verb, have been asked. 'The Secretary and Treasurer' (one 'the') would be one person. "
    "Grew from the 'and' family.")
redo(36)
add(SV, "Either my brothers or I ____ going to meet you at the railway station tomorrow.",
    ["am", "are", "is", "were"],
    "With either … or and neither … nor, the verb agrees with the nearer subject. Here that is 'I', so the verb is 'am'. Grew from 2025 error spotting (neither … nor).")
add(SV, "Few of the old poet's songs ____ been translated into English so far.",
    ["have", "has", "is", "was"],
    "'Few' and 'a few' are plural, so 'few of' + a plural noun takes a plural verb: have been translated. (Some of + an uncountable noun is singular: some of the milk was.) Grew from the few/some family.")
add(SV, "Collecting old stamps and coins ____ been his hobby since he was a child.",
    ["has", "have", "were", "are"],
    "A gerund phrase as the subject is singular, even with plural nouns (stamps and coins) inside it. Grew from 2021 gerund-subject questions.")
add(SV, "Each student in the three sections ____ been given a separate roll number.",
    ["has", "have", "are", "were"],
    "'Each' + singular noun takes a singular verb, whatever plural words come later (sections). Grew from 2021 and 2025 each/every questions.")
add(SV, "Hindi and Odia ____ taught in every class of this school.",
    ["are", "is", "was", "has been"],
    "Two subjects joined by 'and' that are clearly two things take a plural verb. Grew from 2021 and 2025 'and' questions.")

# ================================================================ Block 11 · comprehension (5)
P1 = (
"Many parents in India today are eager for their children to learn English as early as possible. They believe, with good reason, that English "
"opens doors to higher education and better jobs. Some families have even stopped speaking their own language at home, hoping that the child "
"will pick up English faster. Teachers who work with young children, however, warn that this hope may be misplaced.\n\n"
"A child does not learn only words; she learns to think. Her first ideas about number, time, fairness and kindness come to her in the language "
"she hears at home. When school suddenly replaces that language with one she barely understands, the child may learn to repeat sentences "
"without grasping what they mean. Studies in many countries suggest that children who first learn to read in their mother tongue later learn a "
"second language more easily, not less, because the skill of reading carries over from one language to the other.\n\n"
"None of this means that English should be pushed aside. The point is one of order. A strong base in the home language makes the second storey, "
"English, steadier. Children who switch too early may end up comfortable in neither language: they cannot discuss a science lesson in Odia, and "
"they cannot talk about their feelings in English.\n\n"
"The best schools now try to build a bridge. In the early classes they teach mainly in the child's own language and bring in English slowly, "
"through songs, stories and conversation. By the middle classes the child moves easily between the two. Parents, too, have a part to play. "
"Speaking the home language with pride, and reading to the child in it, is not a step backward. It is the first and surest step forward.")
PRE1 = "Read the passage on the home language and answer the question.\n"
add(CO, PRE1 + "According to the passage, why have some families stopped speaking their own language at home?",
    ["They hope the child will pick up English faster", "Their children refuse to speak it",
     "Schools have asked them to stop", "They think the home language is difficult"],
    "Paragraph 1: 'hoping that the child will pick up English faster'. A detail question: the answer is a line of the passage in other words. 2025 had mostly detail questions.",
    p=P1, g="p1")
add(CO, PRE1 + "In paragraph 1, the word 'misplaced' means:",
    ["mistaken", "lost", "hidden", "delayed"],
    "A hope that is misplaced is put in the wrong place, that is, mistaken. 'Lost' is the everyday meaning of a misplaced object, the trap. Word-in-passage questions grew from 2025.",
    p=P1, g="p1")
add(CO, PRE1 + "According to the passage, what may happen to children who switch to English too early?",
    ["They may be comfortable in neither language", "They will learn English faster than others",
     "They will forget English when they grow up", "They will stop going to school"],
    "Paragraph 3: they 'may end up comfortable in neither language'. The second option is the hope the passage questions. Grew from the 2025 detail questions.",
    p=P1, g="p1")
add(CO, PRE1 + "What, according to the passage, do the best schools do in the early classes?",
    ["Teach mainly in the child's own language and bring in English slowly", "Teach only in English from the first day",
     "Teach English and Odia for equal hours from the start", "Leave all language teaching to the parents"],
    "Paragraph 4: 'In the early classes they teach mainly in the child's own language and bring in English slowly'. Grew from the 2025 detail questions.",
    p=P1, g="p1")
add(CO, PRE1 + "Which is the most suitable title for the passage?",
    ["The Home Language First, English Next", "Why English Should Be Pushed Aside",
     "Science Lessons in Odia", "How Parents Choose a School"],
    "The writer argues for an order: the home language first, then English. The second title says the opposite of paragraph 3; the others are small parts. "
    "Title questions grew from 2018 comprehension.",
    p=P1, g="p1")
