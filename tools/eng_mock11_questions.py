# English Mock 11 · full Paper III (English) on the 2021 layout, written with the aso-mock skill (28 Nov 2026).
# User: "/aso-mock english full hard".
# Plan: python3 .claude/skills/aso-mock/scripts/draw.py english --n 100 --seed 89729884 (families, counts and the exact repeats).
# Level: hard (close options, traps that look natural, a few 'No improvement' answers), still one rule per question.
# The plan's third repeat (2025 Q91) is a question on a 2025 passage and cannot stand alone, so the passage here is new
# and that slot is a new detail question; the other two repeats (2025 Q68, 2021 Q41) are kept word for word.
# First option is the right one unless a is given (then the options stay in the printed order).

META = dict(
    paper="english",
    title="ASO English Mock 11",
    hub_title="English Mock 11",
    masthead="English Mock 11",
    heading="English Paper III · Mock 11",
    tagline="100 <b>hard</b> questions on the <b>2021 layout</b>,<br>with close options and natural-looking traps.",
    key="aso-english-mock-2027-11",
    code="M11",
    out="ASO-English-Mock-Test-2027-11.html",
    minutes=45,
    seed=20261128,
    order="given",
    date="28 Nov 2026",
    draw="python3 .claude/skills/aso-mock/scripts/draw.py english --n 100 --seed 89729884",
    intro=[
        "This full English paper (45 minutes) follows the 2021 booklet. It opens with a mixed grammar block of twenty, "
        "then six parts of speech, eight pick-the-correct-sentence and spot-the-error questions, six mixed questions, "
        "sixteen vocabulary questions, ten prepositions, ten articles, five tenses, four rearrangements, "
        "ten agreement questions and one reading passage.",
        "The level is hard. Options are close, some sentences need no change at all, and several traps look like "
        "ordinary English (needn't have, worth visiting, the children as well as their mother, the statistics are). "
        "Each question still tests one rule. Two are exact past questions: 2025 Q68 (immigration rules has become) and "
        "2021 Q41 (intrigue). The passage is about the painters' village of Raghurajpur near Puri.",
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
add(VB, "We ____ a taxi from the station, because when we came out, Ramesh was already waiting for us with his car.",
    ["needn't have hired", "mustn't have hired", "couldn't have hired", "shouldn't hire"],
    "We did hire a taxi, and it turned out to be of no use, because Ramesh had come with a car. A past action that was done but was not necessary takes "
    "'needn't have + past participle'. 'Didn't need to hire' would mean we did not hire one. 'Mustn't have' is not used for the past. "
    "Grew from the modals of 2021 Q2 (duty and need).")
add(P, "The villagers could not ____ the dust and noise of the stone-crushing unit any longer, so they went together to the Collector.",
    ["put up with", "put up to", "put on with", "put off with"],
    "'Put up with' means tolerate or bear. 'Put off' means postpone and 'put on' means wear; neither takes 'with' here. "
    "Grew from the phrasal verbs of 2021 and 2025 (turned out, take to heart, called for).")
add(T, "____ I in your place, I would not sign any paper at the bank without reading every line of it.",
    ["Were", "If", "Had", "Should"],
    "A type 2 condition can drop 'if' and put 'were' first: Were I in your place = If I were in your place. 'If I in your place' has no verb, "
    "and 'Had I' would need a past participle (Had I been). Grew from 2025 conditionals (Q13, Q25, Q38).")
add(AD, "So loudly ____ at the wedding procession that the old people in the street had to shut their windows.",
    ["did the band play", "the band played", "played the band", "the band did play"],
    "When 'so' + an adverb (or adjective) opens the sentence, the helping verb comes before the subject: So loudly did the band play. "
    "'The band played so loudly that…' is the normal order; once 'so loudly' moves to the front, the order must turn round. "
    "'Played the band' moves the main verb, which English does not allow. Grew from the 2025 inversion openers (the map lists 'So + adverb').")
add(ER, IMP + "I (am having) two brothers and a sister, and all of them are older than me.",
    ["have", "am had", "have been having", "No improvement"],
    "'Have' meaning 'own' or 'possess' is a state verb, so it does not take the -ing form: I have two brothers. "
    "'I am having lunch' is fine, because there 'have' means eat. Grew from the 2021 sentence improvement block (Q12–16).", a=0)
add(VB, "After ten years of night duty at the hospital, the nurse has at last got used to ____ during the day.",
    ["sleeping", "sleep", "slept", "be sleeping"],
    "In 'be used to' and 'get used to' the word 'to' is a preposition, so the -ing form follows: got used to sleeping. "
    "'Used to sleep' (no be or get) is a past habit and takes the base verb. Grew from 2025 gerund-or-infinitive questions.")
add(P, "My younger brother is good ____ mathematics, weak ____ English and very keen ____ music.",
    ["at, in, on", "in, at, in", "at, at, about", "on, in, at"],
    "Good at a subject or skill, weak in a subject, keen on a hobby. Each adjective has its own preposition, so learn them as pairs. "
    "One sentence, three pairs: the 2018 and 2021 multi-blank style ('in his honour … invited to it').")
add(AD, "You may borrow my bicycle for the day ____ you bring it back before it gets dark.",
    ["provided", "unless", "lest", "although"],
    "'Provided' (or 'provided that') means 'only if': you may borrow it only if you return it. 'Unless' would turn the meaning round, "
    "'lest' means 'for fear that', and 'although' shows a contrast. Grew from the 2025 connector questions.")
add(ER, IMP + "The old wooden bridge over the canal (has collapsed) during the storm last night.",
    ["collapsed", "had collapsed", "was collapsing", "No improvement"],
    "'Last night' is a finished past time, and the present perfect (has collapsed) cannot go with a finished time. "
    "The simple past is needed: collapsed. 'Had collapsed' needs a second, later past action. Grew from 2021 sentence improvement.", a=0)
add(VB, "Choose the correct passive form: They will have completed the new railway bridge by next March.",
    ["The new railway bridge will have been completed by next March.", "The new railway bridge will be completed by next March.",
     "The new railway bridge will have completed by next March.", "The new railway bridge would have been completed by next March."],
    "Future perfect active (will have completed) becomes future perfect passive: will have been + past participle. "
    "'Will be completed' drops the perfect sense, and 'will have completed' has no 'been', so it is still active. Grew from the 2018 and 2021 voice questions.")
add(T, "I recognised my old school friend at once at the wedding, although I ____ her for nearly twenty years.",
    ["had not seen", "have not seen", "did not see", "was not seeing"],
    "Two times in the past: the twenty years without meeting came before the moment of recognising at the wedding. "
    "The earlier stretch takes the past perfect: had not seen. 'Have not seen' would reach up to now, not up to the wedding. "
    "Grew from 2025 past-perfect questions (Q10, Q27).")
add(P, "The results of the recruitment test will be put up ____ the end of this month, so please do not keep calling the office.",
    ["at", "in", "on", "into"],
    "'At the end of' a period (at the end of the month) names a point of time. 'In the end' means 'finally' and is not followed by 'of the month'. "
    "Grew from the time prepositions of 2021 (at, on, in with times and dates).")
add(ER, IMP + "Between you and (me), the new timetable will not last more than a month.",
    ["I", "myself", "mine", "No improvement"],
    "The sentence is correct. 'Between' is a preposition, and a pronoun after a preposition is in the object form: between you and me. "
    "'Between you and I' sounds polite to many people but is wrong. A hard paper always has a few sentences that need no change.", a=3)
add(VB, "The old Shiva temple on the hill is small and hard to reach, but it is well worth ____ for the view of the river at sunset.",
    ["visiting", "to visit", "visit", "to be visited"],
    "'Worth' is followed by the -ing form, and that -ing form is active even when the meaning is passive: worth visiting, worth reading, worth seeing. "
    "'Worth to be visited' is a common mistake. Grew from 2025 gerund-or-infinitive questions.")
add(AD, "Nowhere else ____ such a peaceful sunrise as the one on the beach at Chandrabhaga.",
    ["have I seen", "I have seen", "I saw", "saw I"],
    "'Nowhere' at the start of a sentence is a negative word, so the helping verb comes before the subject: Nowhere else have I seen. "
    "Grew from the 2025 inversion openers (Never before had, Rarely does).")
add(P, "The retired judge presided ____ the meeting, and after listening ____ both sides, he ruled ____ favour of the farmers.",
    ["over, to, in", "on, to, in", "on, at, on", "over, for, with"],
    "Preside over a meeting, listen to someone, in favour of. Only the first blank separates the first two options: one presides over (or at) a meeting, never on it. "
    "The 2018 and 2021 multi-blank style.")
add(VB, "Choose the correct passive form: Let him open the door of the strong room.",
    ["Let the door of the strong room be opened by him.", "Let the door of the strong room is opened by him.",
     "Let the door of the strong room be open by him.", "The door of the strong room is let opened by him."],
    "A sentence with 'Let + object + verb' becomes 'Let + new subject + be + past participle': Let the door be opened by him. "
    "'Be open' uses the adjective, not the participle. Grew from the 2018 and 2021 voice questions.")
add(ER, IMP + "My younger sister has (less friends) than me, but she is much closer to each of them.",
    ["fewer friends", "lesser friends", "little friends", "No improvement"],
    "'Fewer' is used with things we can count (fewer friends, fewer books); 'less' with things we cannot count (less water, less time). "
    "'Lesser' means 'smaller in importance' (a lesser poet). Grew from the 2021 sentence improvement block.", a=0)
add(VB, "The ground is wet and the roads are full of puddles; it ____ heavily during the night.",
    ["must have rained", "should have rained", "ought to have rained", "would have rained"],
    "'Must have + past participle' is a sure guess about the past from what we see now (wet ground, puddles). 'Should have' and 'ought to have' speak of a duty "
    "that was missed, which makes no sense for rain. Grew from the 2021 modals (Q2).")
add(ER, IMP + "The doctor advised my grandfather (to not eat) sweets after his sugar test.",
    ["not to eat", "to don't eat", "for not eating", "No improvement"],
    "'Not' goes before the to-infinitive: advised him not to eat. 'To not eat' splits the infinitive and is marked wrong in Indian exams. "
    "Grew from 2021 sentence improvement.", a=0)

# ================================================================ Block 2 · parts of speech (6)
POS = "Choose the correct part of speech for the word in bracket:\n"
add(PS, POS + "After a week in hospital, the old man is quite (well) now and has gone back to his farm.",
    ["Adjective", "Adverb", "Noun", "Verb"],
    "Here 'well' means 'in good health' and describes the man after 'is', so it is an adjective (like 'fit'). In 'She sings well' it tells how and is an adverb. "
    "The trap is that 'well' is usually learnt as an adverb. Grew from 2021 Q17–22 (costly looks like an adverb but is an adjective).")
add(PS, POS + "My grandfather goes for a long walk along the river bank (daily).",
    ["Adverb", "Adjective", "Noun", "Preposition"],
    "'Daily' tells how often he goes, so it modifies the verb: an adverb. In 'a daily newspaper' it stands before a noun and is an adjective. "
    "Same pairs: weekly, early, fast, hard. Grew from 2021 Q17–22.")
add(PS, POS + "My cousin's only ambition in life is (to become) a doctor in her own village.",
    ["Infinitive", "Gerund", "Participle", "Adverb"],
    "'To' + base verb is an infinitive. Here it names the ambition, so it works like a noun after 'is'. Grew from 2021 Q17–22 ('eat to live' = infinitive).")
add(PS, POS + "(Alas)! The old banyan tree that stood at the village gate has fallen in the storm.",
    ["Interjection", "Adverb", "Conjunction", "Adjective"],
    "A word that shows a sudden feeling (sorrow here) and stands apart from the sentence, often with an exclamation mark, is an interjection: alas, hurrah, oh, bravo. "
    "Grew from 2021 Q17–22; the interjection is a part of speech the papers have not asked yet.")
add(PS, POS + "Even as a small boy, he was very fond of (reading) adventure stories late at night.",
    ["Gerund", "Participle", "Infinitive", "Verb"],
    "After a preposition (of) the -ing form works as a noun, so it is a gerund: fond of reading. A participle works as an adjective ('the boy reading a book' is a participle). Grew from 2021 Q17–22 (drowning man = participle, eating is fun = gerund).")
add(PS, POS + "The road was long and the sun was hot, (yet) the pilgrims kept walking towards the temple.",
    ["Conjunction", "Adverb", "Preposition", "Pronoun"],
    "Here 'yet' joins two full clauses and shows a contrast, like 'but', so it is a conjunction. In 'He has not come yet' it is an adverb of time. "
    "Grew from 2021 Q17–22 (as well as = conjunction).")

# ================================================================ Block 3 · pick the correct sentence, spot the error (8)
PICK = "Choose the grammatically correct sentence:"
add(ER, PICK,
    ["The tired dog lay under the tree all afternoon.", "The tired dog laid under the tree all afternoon.",
     "The tired dog lied under the tree all afternoon.", "The tired dog was laying under the tree all afternoon."],
    "'Lie' (rest) has the past 'lay'; 'lay' (put something down) has the past 'laid' and needs an object; 'lie' (tell a lie) has 'lied'. "
    "The dog rested, so: lay. Grew from 2021 pick-the-correct-sentence questions.")
add(ER, PICK,
    ["He was so tired that he could not walk any further.", "He was so tired to walk any further.",
     "He was too tired that he could not walk any further.", "He was very tired that he could not walk any further."],
    "The pairs are fixed: 'so … that' + a clause, or 'too … to' + a verb (too tired to walk). Mixing them (too … that, so … to) is wrong, "
    "and 'very' cannot start a 'that' clause of result. Grew from 2021 pick-correct questions.")
add(ER, PICK,
    ["My friend and I went to the Rath Yatra together.", "I and my friend went to the Rath Yatra together.",
     "Me and my friend went to the Rath Yatra together.", "My friend and me went to the Rath Yatra together."],
    "The subject needs 'I', not 'me', and politeness puts the first person last: My friend and I. Grew from 2021 pick-correct questions.")
add(ER, PICK,
    ["It is ten years since he left the village.", "It is ten years since he has left the village.",
     "It is ten years when he left the village.", "It is ten years since he had left the village."],
    "In 'It is + time + since', the 'since' part names a past point and takes the simple past: since he left. "
    "Grew from 2021 pick-correct questions and the since/for family.")
add(ER, PICK,
    ["Please explain the new rule to me.", "Please explain me the new rule.",
     "Please explain me about the new rule.", "Please explain to me about the new rule."],
    "'Explain' cannot take the person straight after it: explain something to someone. 'About' is not needed either, "
    "because 'explain' already takes its object directly (like 'discuss'). Grew from 2021 pick-correct questions.")
add(ER, PICK,
    ["Rohan is taller than any other boy in his class.", "Rohan is taller than any boy in his class.",
     "Rohan is the taller than any other boy in his class.", "Rohan is tallest than any other boy in his class."],
    "When we compare one member with the rest of his own group, we need 'any other': taller than any other boy. "
    "'Than any boy' would compare him with himself too. Grew from 2021 pick-correct questions.")
SEG = "Identify the incorrect segment in the sentence below:\n"
add(ER, SEG + "[If I] [would have known] [about the strike,] [I would not have come.]",
    ["If I", "would have known", "about the strike,", "I would not have come."],
    "A type 3 condition takes the past perfect in the 'if' part, never 'would have': If I had known. 'Would have' belongs only to the result part. "
    "Grew from 2025 Q66 (the conditional error-spotting row).", a=1)
add(ER, SEG + "Immigration rules [has become] so stringent [that] visa verification [happens] at multiple levels before a passenger [is given] entry.",
    ["has become", "that", "happens", "is given"],
    "Exact past question (2025 Q68). The subject 'rules' is plural, so the verb must be 'have become'. 'So … that' is right, "
    "'verification happens' is singular with a singular subject, and 'is given' agrees with 'a passenger'.", a=0, src="2025 Q68")

# ================================================================ Block 4 · mixed tenses, agreement, adverbs (6)
add(T, "Only after all the guests ____ home did the tired family sit down to eat what was left of the feast.",
    ["had gone", "have gone", "were going", "go"],
    "Two past actions: the guests left first, and the family ate after that. The earlier one takes the past perfect: had gone. "
    "'Have gone' reaches up to now, and 'were going' does not show that they had already left. Grew from 2025 past-perfect questions (the earlier of two past actions).")
add(SV, "Neither my sister nor I ____ ever been to Delhi, although our father worked there for two years.",
    ["have", "has", "are", "is"],
    "With 'neither … nor', the verb agrees with the nearer subject. The nearer one is 'I', so: have. 'Has' would suit 'my sister' if she came second. "
    "Grew from 2018 Q52 and 2025 Q39 (neither … nor).")
add(AD, "After two days of rest and medicine, she is feeling ____ better today than she was on Monday.",
    ["much", "very", "more", "too"],
    "A comparative (better) is made stronger with 'much', 'far' or 'a lot', not with 'very' (very good, but much better). "
    "'More better' is a double comparative. Grew from the 2025 adverb-of-degree questions.")
add(T, "You look very tired and your eyes are red. How long ____ in this queue for the ration?",
    ["have you been standing", "are you standing", "did you stand", "you have been standing"],
    "'How long' with an action that began in the past and is still going on takes the present perfect continuous: have you been standing. "
    "In a question the helping verb comes before 'you'. Grew from 2018 Q3, Q14 and 2025 Q23.")
add(SV, "The statistics in this report ____ not correct, so the officer has sent it back to the block office.",
    ["are", "is", "was", "has been"],
    "'Statistics' as a subject of study takes a singular verb (Statistics is a branch of maths). But here it means figures or numbers, "
    "which are plural: the statistics are. Grew from 2021 Q84 and Q88 (measles is, news is).")
add(AD, "The new manager of the mill treats every worker ____, whether he joined last week or thirty years ago.",
    ["fairly", "fair", "fairness", "fairer"],
    "'Treats' is an action verb, and the word tells how he treats them, so it must be an adverb: fairly. 'Fair' is the adjective (a fair manager), "
    "and 'fairness' is a noun. Grew from 2025 adjective-or-adverb questions.")

# ================================================================ Block 5 · vocabulary (16): synonyms 6, antonyms 5, words in a sentence 5
add(SY, "Choose the word most similar in meaning to SAGACIOUS:",
    ["Wise", "Sad", "Talkative", "Brave"],
    "Sagacious means having or showing good judgement: wise, shrewd. 'Sad' is a sound trap. Grew from 2021 Q43 (synonym of veracity).")
add(SY, "Choose the word closest in meaning to the word in bracket: The committee took a (unanimous) decision to build the new library.",
    ["agreed by everyone", "quickly made", "wise and fair", "final and fixed"],
    "Unanimous means that every member agreed, with no one against it (uni = one, animus = mind). Grew from 2021 Q41–42 (meaning of the bracketed word).")
add(SY, "Choose the word closest in meaning to the word in bracket: After the drought, the small farmers were in a (precarious) position, with no grain and no savings.",
    ["unsafe and uncertain", "hopeless and sad", "humble and simple", "crowded and noisy"],
    "Precarious means not safe or steady, likely to get worse or fall at any time. 'Hopeless' is close but means no hope at all, which the word does not say. "
    "Grew from 2021 Q41–42.")
add(SY, "Choose the word most similar in meaning to DISCERN:",
    ["Perceive", "Discard", "Disturb", "Decide"],
    "Discern means to see or notice something that is not easy to see: perceive, make out. The other three are sound traps that start with 'dis' or 'de'. "
    "Grew from 2021 Q43.")
add(SY, "Doesn't it (intrigue) you? The word in the bracket means:",
    ["Arouse interest", "Pleases", "Offends", "Tiredness"],
    "Exact past question (2021 Q41). To intrigue is to make someone curious, to arouse their interest. 'Intrigue' as a noun means a secret plot, but here it is a verb.",
    src="2021 Q41")
add(SY, "Choose the word most similar in meaning to IMPECCABLE:",
    ["Flawless", "Impressive", "Unforgivable", "Delicate"],
    "Impeccable means without any fault: flawless, perfect (an impeccable record). 'Impressive' looks like it but only means making a strong effect. "
    "Grew from 2021 Q43.")
add(AN, "Choose the word most opposite in meaning to LOQUACIOUS:",
    ["Reserved", "Talkative", "Rude", "Clever"],
    "Loquacious means talking a great deal. Its opposite is a person who says little: reserved, quiet, taciturn. 'Talkative' is the synonym trap. "
    "Grew from 2021 Q44–47 (antonyms).")
add(AN, "Choose the word most opposite in meaning to LENIENT:",
    ["Strict", "Gentle", "Lazy", "Tolerant"],
    "Lenient means mild in punishing, not strict (a lenient teacher). The opposite is strict or severe. 'Gentle' and 'tolerant' are near synonyms. "
    "Grew from 2021 Q44–47.")
add(AN, "Choose the word most opposite in meaning to GREGARIOUS:",
    ["Unsociable", "Friendly", "Greedy", "Noisy"],
    "Gregarious means fond of company (from Latin grex, a flock). The opposite is unsociable. 'Greedy' is a sound trap. Grew from 2021 Q44–47.")
add(AN, "Choose the word most opposite in meaning to MAGNANIMOUS:",
    ["Petty", "Generous", "Noble", "Proud"],
    "Magnanimous means generous in forgiving, big-hearted (magna = great). The opposite is petty or mean-minded. 'Generous' and 'noble' are near synonyms. "
    "Grew from 2021 Q44–47.")
add(AN, "Choose the word most opposite in meaning to OPAQUE:",
    ["Transparent", "Dark", "Thick", "Solid"],
    "Opaque means that light cannot pass through it (frosted glass, a wall). The opposite is transparent. Grew from 2021 Q44–47.")
add(V, "The minister's ____ remarks about the flood victims angered the whole state, and he had to apologise the very next day.",
    ["insensitive", "compassionate", "tactful", "cautious"],
    "The clue is 'angered the whole state' and 'had to apologise': the remarks showed no care for others' feelings. "
    "Compassionate, tactful and cautious remarks would not need an apology. Grew from the 2025 context-word questions (21 in 2025).")
add(V, "Although the evidence against the trader was ____, the jury still found him not guilty, which surprised everyone in the court.",
    ["overwhelming", "flimsy", "scanty", "doubtful"],
    "'Although' and 'surprised everyone' show a contrast: the evidence was very strong, yet he was freed. Flimsy, scanty and doubtful evidence would make "
    "the verdict no surprise at all. Grew from the 2025 context-word questions ('unlike the pessimism').")
add(V, "In the sentence 'The chief guest's speech was full of platitudes', the word 'platitudes' means:",
    ["dull remarks said too often", "promises for the future", "clever and funny jokes", "angry words of blame"],
    "A platitude is a remark that has been used so often that it has no force or interest left ('Hard work always pays'). "
    "Grew from 2018 Q65–66 (meaning of a word in a sentence).")
add(V, "The doctor's ____ voice calmed the frightened child at once, and she stopped crying.",
    ["soothing", "abrasive", "stern", "brusque"],
    "Soothing means gently calming. The clue is 'calmed … stopped crying'. Abrasive, stern and brusque voices are harsh or rough. "
    "Grew from the 2025 context-word questions.")
add(V, "In which sentence is the word 'bear' used to mean 'to put up with'?",
    ["I cannot bear the noise of the loudspeakers any longer.", "These mango trees bear fruit in May.",
     "The old bridge cannot bear the weight of heavy trucks.", "A bear came out of the forest near the village."],
    "'Cannot bear the noise' = cannot tolerate it. To bear fruit is to produce it, to bear a weight is to carry or support it, and the last one is the animal. "
    "Grew from 2018 Q84 (a word with many meanings, such as 'bar').")

# ================================================================ Block 6 · prepositions (10)
add(P, "Passengers are requested to refrain ____ smoking inside the station building.",
    ["from", "of", "to", "against"],
    "'Refrain from' means hold yourself back from doing something. Same group: abstain from, desist from. Grew from 2025 Q42 and the verb + preposition family.")
add(P, "Every member of the cooperative society must adhere ____ the rules that were passed at the general meeting.",
    ["to", "by", "with", "on"],
    "'Adhere to' means follow or stick to (rules, a plan). 'Abide by' is a different pair with the same sense, which is why 'by' tempts. "
    "Grew from 2018 and 2021 fixed prepositions.")
add(P, "The clerk was given two days' leave ____ the Sunday he had worked during the election.",
    ["in lieu of", "in view of", "in spite of", "in place to"],
    "'In lieu of' means 'instead of' or 'in return for': leave in place of the Sunday he worked. 'In view of' means 'because of'. "
    "Grew from 2018 and 2021 phrase prepositions (according to, different from, based on).")
add(P, "The Collector has ordered an officer to look ____ the complaints of the villagers about the new ration cards.",
    ["into", "after", "for", "upon"],
    "'Look into' means examine or enquire into. 'Look after' is take care of, and 'look for' is search. Grew from the 2021 and 2025 phrasal verbs.")
add(P, "He holds a high post in the society ____ his long service, not because of his wealth.",
    ["by virtue of", "by means to", "by way to", "by dint to"],
    "'By virtue of' means 'because of' or 'on the strength of'. The other three break fixed forms (by means of, by way of, by dint of all need 'of'). "
    "Grew from 2018 and 2021 phrase prepositions.")
add(P, "The old fort stands empty now, completely devoid ____ the life and noise it once knew.",
    ["of", "from", "with", "in"],
    "'Devoid of' means without or lacking. Same group: bereft of, short of, free of. Grew from the 2025 adjective + preposition questions.")
add(P, "The weaver could not account ____ the missing bundles of silk thread, so the society asked him to pay for them.",
    ["for", "of", "to", "on"],
    "'Account for' means give a reason or explanation for something. 'On account of' is a different phrase (because of). "
    "Grew from 2021 fixed prepositions.")
add(P, "People who sleep very little at night are more prone ____ headaches and anger.",
    ["to", "for", "of", "with"],
    "'Prone to' means likely to suffer from or do something (prone to floods, prone to anger). Same group: liable to, subject to. "
    "Grew from the 2025 adjective + preposition questions.")
add(P, "The flight was cancelled ____ the thick fog that covered the airport from early morning.",
    ["on account of", "in spite of", "instead of", "in case of"],
    "'On account of' means because of. The fog caused the cancelling. 'In spite of' would mean the flight went ahead anyway. "
    "Grew from 2018 and 2021 phrase prepositions.")
add(P, "In his farewell speech, the retiring headmaster did not dwell ____ his own work but spoke only about his students.",
    ["on", "in", "at", "over"],
    "'Dwell on' (or 'dwell upon') means think or speak about something for a long time. 'Dwell in' means live in a place. "
    "Grew from 2018 and 2021 fixed prepositions.")

# ================================================================ Block 7 · articles (10)
AO = ["a", "an", "the", NA]
def art(q, right, e):
    o = [right] + [x for x in AO if x.lower() != right.lower()]
    add(AR, q, o, e)
art("The young prince was declared ____ heir to the throne when he was only ten.", "an",
    "'Heir' begins with a silent h, so the first sound is a vowel sound (air): an heir. Same: an hour, an honest man. Grew from 2021 Q63–72 (a/an by sound).")
art("Every student of the school must come in ____ uniform on Republic Day.", "a",
    "'Uniform' begins with the letter u but the sound 'you' (a consonant sound), so: a uniform. Same: a university, a useful book. Grew from 2021 Q63–72.")
art("My grandmother speaks ____ Odia, Bengali and Hindi with equal ease.", NA,
    "Names of languages take no article: she speaks Odia. 'The Odia language' would need 'the' because of the word 'language'. "
    "Grew from the zero-article family of 2021.")
art("The young lawyer filed ____ RTI application to find out why the road had not been built.", "an",
    "We say the letters: R is read 'ar', which starts with a vowel sound, so: an RTI application. Same: an MLA, an FIR. Grew from 2021 Q63–72.")
art("____ Mount Kilimanjaro, the highest peak in Africa, stands in Tanzania.", NA,
    "Single mountains take no article (Mount Everest, Mount Kilimanjaro), but ranges do (the Himalayas, the Alps). Grew from the zero-article family.")
art("The police caught the young man near the bank, and after a short trial he was sent to ____ prison for three years.", NA,
    "Prison, school, hospital and church take no article when we speak of their main use: he went to prison as a prisoner. "
    "'He went to the prison to meet his brother' takes 'the', because he is a visitor. Grew from the zero-article family (2021).")
art("Our neighbour has ____ eleven-year-old son who plays the flute beautifully.", "an",
    "'Eleven' starts with a vowel sound, so: an eleven-year-old son. The number decides by its sound, not by how it is written (an 11-year-old). "
    "Grew from 2021 Q63–72.")
art("____ Sahara is the largest hot desert in the world.", "The",
    "Names of deserts take 'the' (the Sahara, the Thar), like oceans, rivers and mountain ranges. Grew from the 2021 'the' with special names family.")
add(AR, "After ____ hour's drive from Puri we reached ____ Konark, where we saw ____ Sun Temple.",
    ["an, no article, the", "a, the, the", "an, the, a", "the, no article, a"],
    "An hour (silent h); no article before the name of a town (Konark); the Sun Temple (one famous building). "
    "Grew from the multi-blank article questions of 2018.")
art("____ French are known for their love of good food and fine wine.", "The",
    "'The' + a nationality word ending in -ch, -sh or -ese means the whole people: the French, the Japanese. "
    "Grew from 2021 'the' questions (the rich, the poor: a whole class).")

# ================================================================ Block 8 · tenses (5)
add(T, "Your bag looks very heavy for a small girl. Wait, I ____ it to the bus stop for you.",
    ["will carry", "am carrying", "carry", "shall be carrying"],
    "An offer or a decision made at the moment of speaking takes 'will': I'll carry it for you. 'Am carrying' is a plan already made. "
    "Grew from 2018 Q88 and 2021 Q28 (future).")
add(T, "India's first satellite, Aryabhata, ____ in 1975 with the help of the Soviet Union.",
    ["was launched", "has been launched", "had been launched", "is launched"],
    "A finished past date (in 1975) takes the simple past, here in the passive: was launched. The present perfect cannot go with a past year. "
    "Grew from 2021 Q23 and Q32 (a past year with the simple past).")
add(T, "Look at your clothes! You ____ in the mud again, haven't you?",
    ["have been playing", "are playing", "will play", "had played"],
    "The present result (dirty clothes) of an action that has just been going on takes the present perfect continuous: have been playing. "
    "The tag 'haven't you' also asks for 'have'. Grew from 2018 Q3, Q14 and 2025 Q23.")
add(T, "Every year, the Rath Yatra of Lord Jagannath ____ in the month of Ashadha.",
    ["takes place", "is taking place", "took place", "has taken place"],
    "'Every year' shows a regular, repeated event, which takes the simple present: takes place. Grew from 2021 Q25 and Q82 (habits and facts).")
add(T, "When ____ the letter? I have been waiting for it all week and it has still not come.",
    ["did you post", "have you posted", "had you posted", "you posted"],
    "A question with 'when' asks about a point in the past, so it takes the simple past: When did you post? 'When have you posted' is wrong. "
    "Grew from 2021 Q23 and 2025 Q63 (simple past).")

# ================================================================ Block 9 · rearrangement (4): small letters, no full stops, no clue from the first letter
RS = "Rearrange the following parts to make a meaningful sentence:\n"
def rs(parts, right, wrong, e):
    t = RS + "\n".join("%s: %s" % (l, p) for l, p in zip("PQRS", parts))
    add(RE, t, [right] + wrong, e)
rs(["to the families who lost their homes", "the state government announced", "in the floods of last August", "a special grant"],
   "QSPR", ["QPSR", "SQPR", "PRQS"],
   "the state government announced (Q) a special grant (S) to the families who lost their homes (P) in the floods of last August (R). "
   "'Announced' needs its object (a grant) first; 'to the families' says who gets it; 'in the floods' says how they lost their homes. "
   "Method from the 2025 sentence-part questions.")
rs(["that he forgot", "so busy with the harvest", "the farmer was", "to collect his new ration card"],
   "RQPS", ["QRPS", "RQSP", "RPQS"],
   "the farmer was (R) so busy with the harvest (Q) that he forgot (P) to collect his new ration card (S). 'So … that' must come in that order, "
   "and 'forgot' needs what he forgot right after it. Grew from 2025 rearrangement.")
rs(["but also to keep simple accounts", "taught the old weavers", "the evening school in our village", "not only to read and write"],
   "RQSP", ["RSQP", "QRSP", "RQPS"],
   "the evening school in our village (R) taught the old weavers (Q) not only to read and write (S) but also to keep simple accounts (P). "
   "'Not only' must come before 'but also', and both parts follow the verb 'taught'. Grew from 2025 rearrangement.")
RP = "Rearrange the following sentences to make a meaningful paragraph:\n"
add(RE, RP + "\n".join("%s: %s" % (l, p) for l, p in zip("PQRS", [
    "within a year the number of girls in the high school went up by half",
    "many girls in the hill villages left school after Class 7 because the high school was ten kilometres away",
    "the government then gave every girl in Class 8 a bicycle",
    "seeing this, other districts began the same scheme"])),
    ["QRPS", "QPRS", "RQPS", "QRSP"],
    "Q opens: it states the problem. R ('then') gives the answer to it. P gives the result, and S ('seeing this') points back to that result. "
    "Openers like then, this and such always point back. Grew from 2025 paragraph rearrangement.")

# ================================================================ Block 10 · subject-verb agreement (10)
add(SV, "To err ____ human, to forgive divine.",
    ["is", "are", "were", "have been"],
    "An infinitive (to err) as the subject is singular, like a gerund (Swimming is good exercise). Grew from 2021 Q92 (a gerund subject).")
add(SV, "Each of us ____ a duty to keep the village pond clean.",
    ["has", "have", "are having", "were having"],
    "'Each' is the subject and it is singular; 'of us' does not change that: Each of us has. Grew from 2021 Q24 and 2025 Q55 (each, every).")
add(SV, "The temple and the tank beside it ____ more than four hundred years old.",
    ["are", "is", "was", "has been"],
    "Two separate things joined by 'and' make a plural subject: are. (Only when the two make one idea, such as 'bread and butter', is the verb singular.) "
    "Grew from 2021 Q83.")
add(SV, "The Cabinet ____ approved the new policy for the handloom weavers at its meeting yesterday.",
    ["has", "have", "are", "were"],
    "A collective noun acting as one body takes a singular verb: The Cabinet has approved (its meeting shows it acts as one). "
    "Grew from 2021 Q89 and 2025 Q35, Q53 (the committee, a group of).")
add(SV, "Many a brave soldier ____ laid down his life to guard this border.",
    ["has", "have", "were", "are"],
    "'Many a' is followed by a singular noun and a singular verb (and 'his', not 'their'): Many a soldier has. Grew from 2021 Q85.")
add(SV, "The number of women in the state assembly ____ grown slowly over the last fifty years.",
    ["has", "have", "are", "were"],
    "'The number of' is singular, because the subject is 'the number': has grown. 'A number of' means 'many' and takes a plural verb. "
    "Grew from 2025 Q20.")
add(SV, "Some of the passengers on the overturned bus ____ badly hurt, but nobody died.",
    ["were", "was", "is", "has been"],
    "'Some of' takes its number from the noun after 'of': some of the passengers (plural) were; some of the milk (uncountable) is. "
    "Grew from 2021 Q90 and Q91.")
add(SV, "Not everyone who came to the gram sabha last Sunday ____ with the new plan for the canal.",
    ["agrees", "agree", "are agreeing", "have agreed"],
    "'Everyone' is singular, and 'not' and the 'who' clause do not change that: Not everyone agrees. Grew from 2021 Q24 and 2025 Q55.")
add(SV, "Plenty of rice ____ left over after the wedding feast, so it was given to the orphanage.",
    ["was", "were", "are", "have been"],
    "Quantity words such as plenty of, a lot of and most of take their number from the noun: rice is uncountable, so 'was'. "
    "(Plenty of chairs were left.) Grew from 2021 Q90 and Q91 (some of the rice is).")
add(SV, "The children, as well as their mother, ____ down with fever this week.",
    ["are", "is", "has", "was"],
    "With 'as well as', the verb agrees with the first subject. Here the first subject is 'the children', which is plural, so: are. "
    "The usual examples have a singular first subject, which is why 'is' tempts. Grew from 2021 Q86 and 2025 Q9 (as well as, along with).")

# ================================================================ Block 11 · comprehension (5)
P1 = (
"Raghurajpur is a small village of about a hundred and forty houses among coconut and mango groves, a short drive from Puri. "
"Walk down its single street and you will see that almost every house is also a workshop. On the walls and verandas, men, women "
"and children sit bent over pieces of cloth, painting gods, birds and flowers in fine, bright lines. This is pattachitra, one of "
"the oldest painting traditions of Odisha, and in Raghurajpur it is still the work of whole families.\n\n"
"The painting begins long before a brush touches the cloth. Old cotton cloth is coated with a paste of chalk and gum made from "
"tamarind seeds, and then rubbed with a smooth stone until it is firm and shining. Only then can it take paint. The colours too are "
"made at home: white from powdered conch shells, black from the soot of an oil lamp, yellow and red from soft stones. The brushes "
"are often made from the hair of a squirrel or a mouse tied to a small stick.\n\n"
"Most paintings tell stories of Lord Jagannath, of Krishna, or from the Ramayana. A large one can take a painter several weeks, "
"because every border and every jewel is drawn by hand.\n\n"
"A generation ago, the craft seemed to be dying. Painters earned very little, and many young people left for jobs in the cities. "
"Things changed slowly when the village began to be known as a heritage crafts village. Visitors came from Puri, painters were "
"invited to fairs in Delhi and abroad, and today many families also sell their work on the internet. More young people now stay "
"and learn from their parents, though they often paint smaller and quicker pieces for tourists as well as the large traditional ones.")
PRE1 = "Read the passage on Raghurajpur and answer the question.\n"
add(CO, PRE1 + "What can be inferred from the last paragraph about why more young people now stay in Raghurajpur?",
    ["The craft can now give them a fair living", "The government has stopped them from leaving",
     "There are no jobs left in the cities", "Large traditional paintings now sell faster than small ones"],
    "The paragraph says painters once earned little and the young left; after visitors, fairs and online sales came, more young people stay. "
    "The link is that painting now pays. Nothing says the cities have no jobs, and small pieces are the quicker ones. "
    "An inference question: pick what the lines show. Grew from the 2025 passage questions.",
    p=P1, g="p1")
add(CO, PRE1 + "According to the passage, how is the cloth made ready for painting?",
    ["It is coated with chalk and tamarind-seed gum and rubbed with a stone", "It is dipped in the juice of coconut and mango leaves",
     "It is dyed yellow and red with powdered stones", "It is dried in the sun for several weeks"],
    "Paragraph 2: the cloth 'is coated with a paste of chalk and gum made from tamarind seeds, and then rubbed with a smooth stone'. "
    "Stones give the colours, not the coating, and 'several weeks' is how long a large painting takes. A detail question, as in 2025.",
    p=P1, g="p1")
add(CO, PRE1 + "According to the passage, where does the black colour come from?",
    ["The soot of an oil lamp", "Powdered conch shells", "Soft black stones", "The hair of a squirrel"],
    "Paragraph 2: 'black from the soot of an oil lamp'. Conch shells give white, stones give yellow and red, and squirrel hair is for brushes. "
    "Grew from the 2025 detail questions.",
    p=P1, g="p1")
add(CO, PRE1 + "In the passage, the phrase 'the craft seemed to be dying' means that:",
    ["fewer and fewer people were doing the work", "the old painters were falling ill",
     "the paintings were losing their colour", "the government had banned the craft"],
    "A craft 'dies' when people stop practising it. The next sentence explains: painters earned little and the young left. "
    "A word-meaning question from the passage, as in 2025.",
    p=P1, g="p1")
add(CO, PRE1 + "According to the passage, which of these is NOT given as a way the village's work now reaches buyers?",
    ["Shops opened by the painters in Puri", "Visitors who come to the village",
     "Fairs in Delhi and abroad", "Sales on the internet"],
    "The last paragraph names visitors from Puri, fairs in Delhi and abroad, and the internet. It never says the painters opened shops in Puri. "
    "A detail question in the NOT form; read every option against the lines.",
    p=P1, g="p1")
