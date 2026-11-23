# English Mock 06 · full Paper III (English) on the 2025 layout, written with the aso-mock skill.
# Plan: python3 .claude/skills/aso-mock/scripts/draw.py english --n 100 --seed 584378
# First option is the right one unless a is given (then the options stay in the printed order).

META = dict(
    paper="english",
    title="ASO English Mock 06",
    hub_title="English Mock 06",
    masthead="English Mock 06",
    heading="English Paper III · Mock 06",
    tagline="100 questions drawn by probability<br>from the <b>2018, 2021 and 2025</b> papers, on the 2025 layout.",
    key="aso-english-mock-2027-6",
    code="M06",
    out="ASO-English-Mock-Test-2027-6.html",
    minutes=60,
    seed=20261123,
    order="given",
    date="23 Nov 2026",
    draw="python3 scripts/draw.py english --n 100 --seed 584378",
    intro=[
        "This is a full English paper on the 2025 layout: 69 fill-in-the-blank questions, 9 error questions, "
        "9 jumbled sentences, 3 jumbled paragraphs and two reading passages of five questions each. "
        "The topics and rules were drawn by how often the 2018, 2021 and 2025 papers asked them "
        "(2021 and 2025 count fully, 2018 counts half), and every question was then written by hand.",
        "Three questions are exact past questions, because OPSC repeats itself: 2025 Q13 (Had she known), "
        "2025 Q16 (selfish) and 2021 Q47 (sinister). One passage is on Odisha's Raja festival. "
        "Every explanation names the rule and the past question it grew from.",
    ],
)

Q = []
def add(s, q, o, e, k="one", n=False, c=False, a=None, **x):
    d = dict(s=s, q=q, o=o, e=e, k=k, n=n, c=c, a=a); d.update(x); Q.append(d)

V, T, SV, P, AD, AR, VB, ER, SY, AN, CO, RE = ("Vocabulary", "Tenses", "Subject–verb agreement", "Preposition", "Adverb",
    "Articles", "Verb", "Error spotting", "Synonyms", "Antonyms", "Comprehension", "Sentence rearrangement")
NA = "No article"

FILL = {V: [], T: [], SV: [], P: [], AD: [], AR: [], VB: [], SY: [], AN: []}
def f(s, q, o, e, **x):
    FILL[s].append(dict(s=s, q=q, o=o, e=e, k="one", n=False, c=False, a=x.pop("a", None), **x))

# ================================================================ Vocabulary (14)
f(V, "Unlike his talkative sister, Ravi was ____ and rarely spoke more than a few words at a time.",
  ["reticent", "garrulous", "eloquent", "boisterous"],
  "Reticent = quiet, not willing to say much. The clue is 'unlike his talkative sister': the blank must be the opposite of talkative. "
  "Garrulous = talking too much (the trap, it means the sister); eloquent = speaking well; boisterous = noisy. "
  "Grew from 2025 Q50, where 'unlike the pessimism of his brothers' pointed to 'optimistic'. The 'unlike …' clue always asks for the opposite.")
f(V, "The villagers were ____ of the stranger at first, but slowly began to trust him.",
  ["wary", "fond", "proud", "envious"],
  "Wary = careful because you do not trust someone. 'But slowly began to trust him' tells you they did not trust him at first. "
  "All four words take 'of', so grammar does not help; only the meaning does. This is the 2025 pattern (Q16, Q17): the second half of the sentence explains the blank.")
f(V, "The plan looked good on paper, but it was not ____ with the small budget we had.",
  ["feasible", "inevitable", "obligatory", "redundant"],
  "Feasible = possible to do. 'Looked good on paper, but … small budget' says it could not be done. "
  "Inevitable = sure to happen; obligatory = compulsory; redundant = not needed. Family: 2025 asked 'untenable hypothesis' (Q32) in the same 'idea versus reality' frame.")
f(V, "The manager praised Anita for her ____; she never gave up on the difficult project.",
  ["perseverance", "negligence", "hesitation", "arrogance"],
  "Perseverance = continuing to try in spite of difficulty. 'Never gave up' is its definition. "
  "2025 used 'tenacious' (holding on firmly); perseverance is the noun cousin of the same idea. Others: negligence = carelessness; hesitation = pausing from doubt; arrogance = pride.")
f(V, "The old man felt ____ whenever he spoke of his childhood days in the village.",
  ["nostalgic", "indifferent", "apprehensive", "furious"],
  "Nostalgic = longing for happy times in the past. 'Childhood days' is the clue. "
  "Indifferent = not caring; apprehensive = afraid of what may happen; furious = very angry. 2025 Q58 asked an emotion word from a clue in the sentence; this is the next one.")
f(V, "Water is ____ in the desert, so travellers carry it with great care.",
  ["scarce", "abundant", "plentiful", "surplus"],
  "Scarce = in short supply. 'Carry it with great care' only makes sense if there is little of it. "
  "Abundant and plentiful mean the opposite; surplus = more than needed. Remember the pair scarce / abundant, a favourite antonym pair.")
f(V, "The doctor's handwriting was so ____ that the chemist could not read the prescription.",
  ["illegible", "legible", "eligible", "ineligible"],
  "Illegible = cannot be read. Legible = can be read (opposite). Eligible / ineligible = allowed or not allowed to do something (eligible for a job). "
  "Look-alike words are the commonest trap in 2025-style vocabulary: 'so … that' tells you the result (could not read).")
f(V, "Her ____ nature made her popular; she was always ready to help anyone in need.",
  ["benevolent", "malevolent", "callous", "spiteful"],
  "Benevolent = kind and wanting to do good. 'Always ready to help' is the clue. "
  "Malevolent = wishing harm (its opposite, built on 'mal' = bad); callous = not caring about others' pain; spiteful = wanting to hurt. Prefixes help: bene = good, mal = bad.")
f(V, "The students were so ____ about the result that some of them could not sleep the night before.",
  ["anxious", "reluctant", "indifferent", "hesitant"],
  "Anxious = worried and nervous. 'Could not sleep' shows worry. "
  "Reluctant = unwilling (2021 Q48 had 'reluctant' as the answer); indifferent = not caring; hesitant = slow to act because unsure. None of those keeps someone awake.")
f(V, "His actions were seen as ____, while most expected him to be more considerate.",
  ["selfish", "compassionate", "polite", "generous"],
  "Selfish = thinking only of oneself. 'More considerate' (thinking of others) is the contrast clue, so the blank is its opposite. "
  "The other three are all kind words. The examiner repeats questions word for word, so past questions are worth learning exactly.",
  src="2025 Q16")
f(V, "He could not support his large family on his meagre salary. The word 'meagre' means:",
  ["very small", "regular", "monthly", "generous"],
  "Meagre = very small, not enough. 'Could not support his family' shows the salary was too little. "
  "Grew from the 2018 word-meaning questions (Q65, Q66, Q84, Q96), which gave a word in a sentence and asked its meaning. Synonyms: scanty, paltry. Opposite: ample.")
f(V, "The minister visited the area to allay the fears of the flood victims. The word 'allay' means:",
  ["to calm or lessen", "to increase", "to record", "to ignore"],
  "Allay = to make a fear, doubt or pain less strong. A minister visits victims to calm their fears. "
  "Do not mix it up with 'ally' (a friend or partner country). Same 2018 word-in-a-sentence family.")
f(V, "In which sentence is the word 'fair' used to mean 'just and honest'?",
  ["The judge gave a fair decision.", "She has fair hair and blue eyes.",
   "We bought toys at the village fair.", "The weather will be fair tomorrow."],
  "A fair decision is a just one. The other three use other meanings: fair hair = light in colour; a village fair = a mela; fair weather = bright and dry. "
  "The map's open angle for this family is 'a word with many meanings' (2018 asked 'bar'); fair, bear, bank, light and match are the usual ones.")
f(V, "We need a pragmatic approach to solve the water problem of the city. The word 'pragmatic' means:",
  ["practical and sensible", "dreamy and idealistic", "slow and careful", "angry and forceful"],
  "Pragmatic = dealing with problems in a practical way, based on what can really be done. "
  "Its opposite is idealistic (thinking of how things should be rather than how they are). Same 2018 word-meaning family.")

# ================================================================ Tenses (11)
f(T, "I wish I ____ more time to prepare for yesterday's interview.",
  ["had had", "have", "had", "would have"],
  "A wish about the PAST takes the past perfect: I wish I had had more time (yesterday). "
  "'I wish I had more time' would be a wish about NOW. This family came in 2018 twice and in 2025 Q1 ('I wish I had spent'). Rule: wish + past = present regret; wish + past perfect = past regret.")
f(T, "It is high time we ____ our habit of wasting food.",
  ["changed", "change", "will change", "have changed"],
  "'It is (high) time' + subject + PAST tense, though the meaning is present: It is high time we changed. "
  "This is the other half of the unreal-past family (with 'I wish' and 'I would rather'). The present 'change' is the trap.")
f(T, "India ____ the Cricket World Cup for the first time in 1983.",
  ["won", "has won", "had won", "was winning"],
  "A finished action at a stated past time ('in 1983') takes the simple past. The present perfect never goes with a past time word. "
  "2021 Q23 and Q32 asked the same rule; the map's open angle is 'a past year'.")
f(T, "Please do not disturb him now; he ____ for tomorrow's examination.",
  ["is studying", "studies", "studied", "has studied"],
  "'Now' shows an action going on at this moment, so the present continuous: is studying. "
  "Grew from 2021 Q75. The simple present (studies) is for habits: He studies every evening.")
f(T, "I ____ three letters since morning, but I have not posted any of them yet.",
  ["have written", "wrote", "had written", "write"],
  "'Since morning' + a result that matters now = present perfect: I have written. "
  "'Since' and 'for' with a period up to now need the perfect. 2018 Q15 and 2021 Q74 asked the present perfect; the simple past 'wrote' would need a finished time (at nine o'clock).")
f(T, "Light ____ much faster than sound.",
  ["travels", "is travelling", "travelled", "has travelled"],
  "Scientific facts and general truths take the simple present. "
  "2021 Q25 and Q82 and 2025 Q37 tested the simple present for habits; facts are the next angle of the same rule.")
f(T, "If it ____ tomorrow, the match will be cancelled.",
  ["rains", "will rain", "rained", "would rain"],
  "First conditional: If + simple present, … will + verb. Never put 'will' in the if-clause. "
  "2025 asked three conditionals (Q13, Q25, Q38); this mock carries 2025 Q13 (third conditional) too, so learn all three types: "
  "1) If it rains, I will stay. 2) If it rained, I would stay. 3) If it had rained, I would have stayed.")
f(T, "Had she known about the meeting, she ____ there on time.",
  ["would have been", "would be", "will be", "is"],
  "'Had she known' = If she had known (third conditional, with the 'if' dropped and the verb moved to the front). "
  "The result part must be would have + past participle. An exact repeat: the examiner reuses questions.",
  src="2025 Q13")
f(T, "How long ____ for the bus? I have been standing here for twenty minutes.",
  ["have you been waiting", "are you waiting", "did you wait", "do you wait"],
  "'How long' about an action that started in the past and is still going on takes the present perfect continuous: have been + -ing. "
  "The reply in the sentence uses the same tense. Grew from 2025 Q23 and 2018 Q3, Q14, Q61 ('has been living … for five years').")
f(T, "By the time we got the food ready, most of the guests ____.",
  ["had left", "have left", "leave", "are leaving"],
  "Two past actions: the guests left first, so it takes the past perfect (had left); the later action is in the simple past (got). 'By the time' + past is the signal. "
  "2025 Q10 and Q27 asked the same 'earlier of two past actions' rule (2025 Q27: 'had known each other … when they finally met').")
f(T, "By the time you reach home tonight, I ____ dinner.",
  ["will have cooked", "cook", "have cooked", "am cooking"],
  "An action that will be complete before a point in the future takes the future perfect: will have + past participle. "
  "'By the time' + present (you reach) is the signal. This is the map's open angle for the future family (2021 Q28, Q76, Q87).")

# ================================================================ Subject–verb agreement (8)
f(SV, "These spectacles ____ to my grandfather.",
  ["belong", "belongs", "is belonging", "has belonged"],
  "Trousers, jeans, scissors, spectacles and pliers are always plural, so: These spectacles belong. 'Belong' is a state verb, so no continuous form. But 'a pair of trousers IS', because the subject becomes 'pair'. "
  "2025 Q62 asked 'the pair of shoes'; this is its other half.")
f(SV, "Economics ____ my favourite subject in college.",
  ["is", "are", "were", "have been"],
  "Subjects ending in -ics (economics, physics, mathematics, politics) are singular when they name a subject of study, like news and measles. "
  "2021 Q84 and Q88 asked plural-looking nouns.")
f(SV, "The teacher, as well as the students, ____ excited about the trip.",
  ["is", "are", "were", "have been"],
  "With 'as well as', 'along with', 'together with' and 'with', the verb agrees with the FIRST subject. The first subject is 'the teacher' (singular), so: is. "
  "Asked in 2021 Q86 and 2025 Q9.")
f(SV, "Each of these old houses ____ a small garden at the back.",
  ["has", "have", "are having", "were having"],
  "'Each of + plural noun' takes a singular verb, because the real subject is 'each'. "
  "2021 Q24 and 2025 Q55 asked this family (each, every, everyone).")
f(SV, "Everyone in the two villages ____ about the new road.",
  ["knows", "know", "are knowing", "have known"],
  "Everyone, everybody, someone and nobody are singular, even when the phrase after them is plural ('the two villages'). "
  "'Know' is a state verb, so no continuous form. Same family as 2025 Q67 ('Everyone feel' was the error).")
f(SV, "The jury ____ given its verdict after two days.",
  ["has", "have", "are", "were"],
  "A collective noun acting as one unit takes a singular verb; 'its' in the sentence confirms the jury acts as one. "
  "If the members acted separately, it would be 'The jury have given their opinions'. 2021 Q89 and 2025 Q35, Q53 asked this.")
f(SV, "The number of tigers in Similipal ____ risen in recent years.",
  ["has", "have", "are", "were"],
  "'The number of' + plural noun takes a SINGULAR verb, because the subject is 'number': The number of tigers has risen. "
  "'A number of' means 'many' and takes a PLURAL verb. 2025 Q20 asked the 'A number of factors have' half; this is the other half.")
f(SV, "Neither the principal nor the teachers ____ present at the meeting.",
  ["were", "was", "is", "has been"],
  "With 'neither … nor' and 'either … or', the verb agrees with the NEARER subject. 'Teachers' is nearer and plural, so: were. "
  "2025 Q39 asked this; 2018 Q52 asked 'neither of'.")

# ================================================================ Preposition (11)
f(P, "My birthday falls ____ June.",
  ["in", "on", "at", "by"],
  "Months, years and seasons take 'in' (in June, in 2026, in winter). Days and dates take 'on' (on Monday, on 5 June). Clock times take 'at' (at 6 p.m.). "
  "2021 Q60 and Q62 asked time prepositions.")
f(P, "He has been working ____ Cuttack ____ six years and lives ____ a small flat near the river.",
  ["in, for, in", "at, since, on", "in, since, at", "on, for, by"],
  "In + a city; FOR + a length of time (six years), SINCE + a point of time (since 2020); live in a flat or a house. "
  "Only the first set is right in all three places. Grew from the multi-blank family (2018 Q62, Q78, Q86; 2021 Q7).")
f(P, "The novel was written ____ Fakir Mohan Senapati and later translated ____ English ____ a young scholar.",
  ["by, into, by", "from, in, by", "by, in, from", "with, to, of"],
  "The doer in a passive sentence takes 'by'; translate FROM one language INTO another. "
  "Fakir Mohan Senapati is the father of modern Odia prose (Chha Mana Atha Guntha). Multi-blank family.")
f(P, "The train arrived ____ the station ____ 6 p.m. ____ Monday.",
  ["at, at, on", "in, on, at", "on, in, at", "at, by, in"],
  "Arrive AT a small place (a station, an airport), arrive IN a city or country. At + clock time; on + day. "
  "2025 Q18 asked 'arrived at a decision'; this is the place use of the same verb.")
f(P, "Our car ____ on the way to Puri, so we reached very late.",
  ["broke down", "broke up", "broke out", "broke in"],
  "Break down = stop working (a machine or vehicle). Break up = end a relationship or meeting; break out = start suddenly (a fire, a war); break in = enter by force. "
  "Phrasal verbs came in 2021 (Q34, Q55) and 2025 (Q54, Q60); four options on one verb is the usual pattern.")
f(P, "The nurse ____ the patients in the ward day and night.",
  ["looks after", "looks into", "looks for", "looks up to"],
  "Look after = take care of. Look into = investigate; look for = search; look up to = respect. "
  "The map lists the 'look' set as an open angle of the phrasal-verb family.")
f(P, "The final was ____ because of the storm, and it will not be played at all this season.",
  ["called off", "put off", "set off", "taken off"],
  "Call off = cancel (it will not happen). 'Will not be played at all' is the clue. "
  "Put off = postpone (it will happen later): the trap. Set off = start a journey; take off = remove, or a plane leaving the ground.")
f(P, "Though younger in age, he is senior ____ me in service.",
  ["to", "than", "from", "over"],
  "Senior, junior, superior, inferior, prior and preferable take 'to', never 'than'. "
  "Adjective + preposition questions came word for word in 2018 and 2021 (Q53, Q54, Q56, Q61).")
f(P, "My grandmother is very fond ____ Odissi music.",
  ["of", "with", "for", "about"],
  "Fond OF = liking something. Same adjective + preposition family (afraid of, envious of, proud of, good at, eligible for).")
f(P, "The servant was accused ____ theft by his employer.",
  ["of", "for", "with", "about"],
  "Accuse someone OF a crime; charge someone WITH a crime. Do not mix the two. "
  "Verb + preposition family: 2025 Q14 (lies in), Q18 (arrived at), Q42, Q64.")
f(P, "Doctors advise patients with heart disease to abstain ____ smoking.",
  ["from", "of", "with", "to"],
  "Abstain FROM = keep yourself from doing something. Its cousins: refrain from, prevent from, desist from. Same verb + preposition family.")

# ================================================================ Adverb (8)
f(AD, "She was ____ tired to walk any further.",
  ["too", "very", "so", "much"],
  "Too + adjective + to-infinitive means 'so much that it is not possible': too tired to walk. "
  "'Very tired to walk' and 'so tired to walk' are wrong (so needs 'that': so tired that she could not walk). Grew from 2025 Q12 and Q61 (intensifiers).")
f(AD, "The water is not warm ____ for a bath.",
  ["enough", "too", "very", "much"],
  "'Enough' comes AFTER an adjective (warm enough) but BEFORE a noun (enough water). "
  "Same intensifier family as 2018 Q27 and 2025 Q12.")
f(AD, "Little ____ that he would become a famous writer one day.",
  ["did he know", "he knew", "he did know", "knew he"],
  "When 'Little' (meaning 'not at all') starts a sentence, the subject and helping verb swap places, as in a question: Little did he know. "
  "The same goes for never, seldom, rarely, not only and under no circumstances. "
  "2025 asked four inversion openers (Q8, Q11, Q21, Q40).")
f(AD, "Seldom ____ such a beautiful sunset over the Chilika lake.",
  ["have I seen", "I have seen", "I saw", "seen I have"],
  "Negative adverbs at the start (seldom, rarely, never, hardly, scarcely, little) need inversion: Seldom have I seen. "
  "2025 asked 'Rarely does one' and 'Never before had'; seldom is the next one on the same list.")
f(AD, "The flowers smell ____ after the rain.",
  ["sweet", "sweetly", "sweetness", "more sweetly"],
  "Smell, taste, feel, look, sound, seem and become are linking verbs: they describe the subject, so they take an ADJECTIVE (smell sweet). "
  "2025 asked four adjective-or-adverb questions (Q41, Q44, Q49, Q56); this is the linking-verb half.")
f(AD, "The children played ____ in the park all evening.",
  ["happily", "happy", "happiness", "happier"],
  "An action verb (played) is described by an ADVERB of manner: played happily. "
  "The other half of the same family (2025 Q41 'scrutinised carefully', Q44 'spoke diplomatically').")
f(AD, "The road was narrow and crowded; ____, the ambulance reached the hospital on time.",
  ["nevertheless", "therefore", "moreover", "consequently"],
  "Nevertheless = in spite of that. Reaching on time is the opposite of what a crowded road leads us to expect, so we need a contrast word. "
  "Therefore and consequently show a result; moreover adds a point. 2025 Q22, Q33 and Q52 asked these openers.")
f(AD, "Gold is ____ than silver.",
  ["costlier", "costliest", "more costlier", "most costly"],
  "With 'than' we need the comparative: costlier (or more costly). Never use 'more' and '-er' together (more costlier is a double comparative). "
  "2025 Q4 ('oldest but the smallest') and 2018 Q82 asked degrees of comparison.")

# ================================================================ Articles (6)
f(AR, "My elder sister has ____ MA degree in English.",
  ["an", "a", "the", NA],
  "A and an go by SOUND, not spelling. 'MA' is read 'em-ay', which starts with a vowel sound, so: an MA (like an MLA, an IAS officer). "
  "Five questions in 2021 and 2025 asked a/an by sound (Q69, Q72; Q31, Q57).")
f(AR, "India won the series by winning ____ one-day match at Cuttack.",
  ["a", "an", "the", NA],
  "'One' is spoken 'wun', with a consonant (w) sound, so it takes 'a': a one-day match, a one-rupee coin. The same goes for a university, a European (y sound). "
  "Same a/an-by-sound family.")
f(AR, "We usually have ____ dinner at nine o'clock.",
  [NA, "a", "the", "an"],
  "Names of meals (breakfast, lunch, dinner) take no article in general use: have dinner. "
  "But with an adjective they take one: We had a lovely dinner. 2021 Q66, Q70 and Q71 asked the zero article.")
f(AR, "____ iron is the most useful of all metals.",
  [NA, "The", "An", "A"],
  "Names of materials and abstract nouns used in a general sense take no article: Iron is useful; Honesty is the best policy. "
  "But with a particular meaning they take 'the': the iron in this bridge. Zero-article family.")
f(AR, "____ Himalayas protect India from the cold winds of Central Asia.",
  ["The", "A", "An", NA],
  "Names of rivers, seas, oceans, mountain ranges and deserts take 'the': the Mahanadi, the Bay of Bengal, the Himalayas, the Thar. "
  "But single mountains and lakes do not: Mount Everest, Chilika Lake. 2025 Q24 asked 'the Amazon rainforest'; 2021 Q63, Q65, Q68 asked 'the'.")
f(AR, "Mount Everest is ____ highest peak in the world.",
  ["the", "a", "an", NA],
  "Superlatives always take 'the': the highest, the best, the most beautiful. "
  "Same family as the rivers question above: 'the' for something particular or one of a kind.")

# ================================================================ Verb (5)
f(VB, "She finished ____ the report just before lunch.",
  ["writing", "to write", "write", "to writing"],
  "Avoid, enjoy, finish, mind, deny, suggest and practise are followed by the -ING form, not 'to'. "
  "2025 Q6, Q34 and Q48 asked gerund-or-infinitive ('denied having been', 'prevent from').")
f(VB, "Farmers are used to ____ up before sunrise.",
  ["getting", "get", "got", "be getting"],
  "In 'be used to', 'look forward to', 'object to' and 'with a view to', the word 'to' is a PREPOSITION, so the verb after it takes -ing: are used to getting up. "
  "Do not confuse it with 'used to + verb' for a past habit: He used to get up early. "
  "A favourite trap of the gerund family.")
f(VB, "Choose the correct passive form: The farmer will plough the field tomorrow.",
  ["The field will be ploughed by the farmer tomorrow.", "The field will be plough by the farmer tomorrow.",
   "The field would be ploughed by the farmer tomorrow.", "The field is ploughed by the farmer tomorrow."],
  "Simple future passive = will be + past participle. Keep the tense of the active (will), never change it to would or is. "
  "Voice was asked in 2018 Q50 and 2021 Q1, Q30, Q33; the map's open angle is the simple future.")
f(VB, "Choose the correct passive form: Who wrote this letter?",
  ["By whom was this letter written?", "Who was this letter written?",
   "By whom this letter was written?", "Whom was this letter written by him?"],
  "In the passive, 'Who' becomes 'By whom', and the question order stays: By whom + was + subject + past participle? "
  "Option 3 has no question order (was must come before 'this letter').")
f(VB, "Choose the correct passive form: They are building a new school in our village.",
  ["A new school is being built in our village.", "A new school is built in our village.",
   "A new school has been built in our village.", "A new school was being built in our village."],
  "Present continuous passive = is/are being + past participle. 'By them' can be dropped when the doer is not important. "
  "The other options change the tense.")

# ================================================================ Synonyms (4)
f(SY, "The leader gave an (eloquent) speech that moved the whole crowd. The word in the bracket means:",
  ["fluent and persuasive", "short and dull", "loud and angry", "long and boring"],
  "Eloquent = speaking well and in a way that moves people. 'Moved the whole crowd' is the clue. "
  "2021 Q41 and Q42 used exactly this format: a sentence with a bracketed word. Synonyms and antonyms are named in the syllabus but were missing in 2025.")
f(SY, "The (timid) child hid behind his mother when the guests arrived. The word in the bracket means:",
  ["shy and easily frightened", "brave", "naughty", "hungry"],
  "Timid = shy, lacking courage. Hiding behind his mother is the clue. Opposites: bold, brave, confident. Same 2021 bracket format.")
f(SY, "He left his government job for a (lucrative) business offer. The word in the bracket means:",
  ["profitable", "risky", "boring", "small"],
  "Lucrative = bringing in a lot of money. Someone leaves a safe job only for something that pays well. Synonyms: profitable, rewarding. Same 2021 bracket format.")
f(SY, "Choose the word most similar in meaning to OBSTINATE:",
  ["Stubborn", "Obedient", "Flexible", "Polite"],
  "Obstinate = refusing to change one's mind, stubborn. Obedient and flexible are near-opposites. "
  "2021 Q43 asked a synonym this way ('veracity'). Other members: adamant, headstrong, unyielding.")

# ================================================================ Antonyms (2)
f(AN, "Choose the word most opposite in meaning to ANCIENT:",
  ["Modern", "Antique", "Historic", "Aged"],
  "Ancient = very old. Its opposite is modern. Antique, historic and aged all mean old, so they are synonyms, not antonyms. "
  "2021 asked four antonyms in this exact wording (Q44 to Q47).")
f(AN, "Choose the word most opposite in meaning to SINISTER:",
  ["Good", "Evil", "Long", "Short"],
  "Sinister = evil, threatening harm. Its opposite here is 'good'. 'Evil' is a synonym: the trap. An exact past question.",
  src="2021 Q47")

# ---------------------------------------------------------------- order the fill block: no two neighbours with one label
def spread(groups):
    rest = {k: list(v) for k, v in groups.items()}
    out, last = [], None
    while any(rest.values()):
        cands = sorted((k for k in rest if rest[k] and k != last), key=lambda k: -len(rest[k]))
        if not cands: cands = [k for k in rest if rest[k]]
        k = cands[0]; out.append(rest[k].pop(0)); last = k
    return out
Q.extend(spread(FILL))

# ================================================================ Error questions (9)
SEG = "Identify the incorrect segment in the sentence below:\n"
add(ER, SEG + "[The list of] [selected candidates] [have been] [put up on the notice board.]",
    ["The list of", "selected candidates", "have been", "put up on the notice board."],
    "The subject is 'the list' (singular), not 'candidates', so: The list of selected candidates HAS been put up. "
    "A plural noun between the subject and the verb is the oldest agreement trap. 2025 Q68 ('rules has become') was an agreement error of the same kind.", a=2)
add(ER, SEG + "[He is] [one of the best players] [who has ever] [played for India.]",
    ["He is", "one of the best players", "who has ever", "played for India."],
    "'Who' refers to 'players' (plural), not to 'one', so the verb is plural: one of the best players who HAVE ever played. "
    "Compare 'One of my friends has gone', where 'one' is the subject. Agreement errors were the commonest kind in 2025 (Q67, Q68).", a=2)
add(ER, SEG + "[If I] [was you,] [I would accept] [the offer at once.]",
    ["If I", "was you,", "I would accept", "the offer at once."],
    "In an unreal present condition (second conditional) we use 'were' for every person: If I were you. "
    "The 2025 error row had a conditional mistake too (will/would). This mock also asks the first and third conditionals.", a=1)
add(ER, "Choose the best replacement for the part in brackets. If no change is needed, choose 'No improvement'.\n"
        "She (did not went) to the market yesterday.",
    ["did not go", "has not gone", "had not went", "No improvement"],
    "After did / does / do, the verb is always in its base form: did not go. 'Has not gone' clashes with 'yesterday'. "
    "2021 asked five sentence-improvement questions (Q12 to Q16) in this format.", a=0)
add(ER, "Choose the best replacement for the part in brackets. If no change is needed, choose 'No improvement'.\n"
        "One should keep (his) promises.",
    ["their", "one's", "your", "No improvement"],
    "When 'one' is the subject, the pronoun after it is 'one's' (or 'oneself'): One should keep one's promises. "
    "Same 2021 sentence-improvement family.", a=1)
add(ER, "Choose the best replacement for the part in brackets. If no change is needed, choose 'No improvement'.\n"
        "(Being a rainy day,) we stayed at home.",
    ["Having a rainy day,", "Been a rainy day,", "It being a rainy day,", "No improvement"],
    "As written, the sentence says 'we' were a rainy day: the opening phrase has no proper subject (a 'dangling' phrase). "
    "Adding 'It' gives the phrase its own subject: It being a rainy day, we stayed at home. Same 2021 family (Q13 'because of they dislike').", a=2)
add(ER, "Choose the grammatically correct sentence:",
    ["I have never seen such a big crowd.", "I have seen never such a big crowd.",
     "Never I have seen such a big crowd.", "I have never seen a such big crowd."],
    "'Never' goes between the helping verb and the main verb (have never seen), and 'such' comes before the article (such a big crowd). "
    "If 'Never' starts the sentence, it needs inversion (Never have I seen). 2021 Q37 to Q40 asked 'pick the correct sentence' and word order.")
add(ER, "Choose the INCORRECT sentence:",
    ["He gave me many advices.", "He gave me much advice.", "He gave me a piece of advice.", "He gave me some advice."],
    "Advice is uncountable: it has no plural (advices) and takes much, some or a piece of. "
    "The same is true of information, furniture, luggage and equipment. Same 2021 family, asked the other way round.")
add(ER, "Which of the following sentences is free from error?",
    ["Hardly anyone came to the meeting.", "Hardly no one came to the meeting.",
     "Hardly nobody came to the meeting.", "Hardly anyone did not come to the meeting."],
    "Hardly, scarcely and barely are already negative, so they must not be used with another negative (no one, nobody, not). "
    "'Hardly anyone' = almost nobody. Same 2021 family.")

# ================================================================ Rearrangement: parts of a sentence (9)
RS = "Rearrange the following parts to make a meaningful sentence:\n"
def rs(parts, right, wrong, e):
    t = RS + "\n".join("%s: %s" % (l, p) for l, p in zip("PQRS", parts))
    add(RE, t, [right] + wrong, e)

rs(["of a new medical college", "The Chief Minister", "at Kalahandi on Monday", "laid the foundation stone"],
   "QSPR", ["QPSR", "SQPR", "PQSR"],
   "The Chief Minister (Q) laid the foundation stone (S) of a new medical college (P) at Kalahandi on Monday (R). "
   "Method from 2025 Q81 to Q94: find the subject (Q), then its verb (S); 'of …' must follow the noun it belongs to; the place and time phrase comes last.")
rs(["gathered at Puri", "to watch the Rath Yatra", "Although it was raining heavily,", "thousands of devotees"],
   "RSPQ", ["RPSQ", "SRPQ", "RQSP"],
   "Although it was raining heavily, (R) thousands of devotees (S) gathered at Puri (P) to watch the Rath Yatra (Q). "
   "The part ending in a comma opens the sentence; 'to watch' (purpose) comes after the action it explains.")
rs(["the students", "before the end of the week", "The teacher asked", "to submit their projects"],
   "RPSQ", ["RSPQ", "PRSQ", "RQPS"],
   "The teacher asked (R) the students (P) to submit their projects (S) before the end of the week (Q). "
   "Pattern: ask + person + to-verb. The time phrase goes last.")
rs(["finish the work on time,", "Not only did he", "helped his colleagues", "but he also"],
   "QPSR", ["QSPR", "PQSR", "QRSP"],
   "Not only did he (Q) finish the work on time, (P) but he also (S) helped his colleagues (R). "
   "'Not only' is always answered by 'but also'; 'did he' needs a base verb (finish), and 'he also' needs a past verb (helped).")
rs(["and released in Similipal", "The tiger,", "was caught by forest officials", "which had strayed into the village,"],
   "QSRP", ["QRSP", "SQRP", "QSPR"],
   "The tiger, (Q) which had strayed into the village, (S) was caught by forest officials (R) and released in Similipal (P). "
   "A 'which' clause sits right after the noun it describes, between commas; 'and released' joins the second action to the first.")
rs(["The book", "and I have almost finished it", "that you lent me last week", "is very interesting"],
   "PRSQ", ["PSRQ", "RPSQ", "PRQS"],
   "The book (P) that you lent me last week (R) is very interesting (S) and I have almost finished it (Q). "
   "The 'that' clause follows its noun; the main verb (is) comes after the whole subject.")
rs(["for their living", "depend on fishing", "in the coastal villages", "Most people"],
   "SRQP", ["SQRP", "QSRP", "SRPQ"],
   "Most people (S) in the coastal villages (R) depend on fishing (Q) for their living (P). "
   "The phrase 'in the coastal villages' describes the people, so it stays next to them; 'depend on' needs its object (fishing) straight after it.")
rs(["were delighted", "who had worked hard", "When the results were announced,", "the students"],
   "RSQP", ["RQSP", "SQRP", "RSPQ"],
   "When the results were announced, (R) the students (S) who had worked hard (Q) were delighted (P). "
   "The opening time clause ends in a comma; 'who' must follow 'the students'.")
rs(["near the Moon's south pole", "the first country", "India became", "to land a spacecraft"],
   "RQSP", ["RSQP", "QRSP", "SRQP"],
   "India became (R) the first country (Q) to land a spacecraft (S) near the Moon's south pole (P). "
   "'The first … to + verb' is a fixed pattern. (Chandrayaan-3 landed there on 23 August 2023.)")

# ================================================================ Rearrangement: paragraphs (3)
RP = "Rearrange the following sentences to make a meaningful paragraph:\n"
def rp(sents, right, wrong, e):
    t = RP + "\n".join("%s: %s" % (l, p) for l, p in zip("PQRS", sents))
    add(RE, t, [right] + wrong, e)

rp(["She began playing with a bamboo stick at the age of eight.",
    "Today she trains young girls from her village in the same game.",
    "Sunita grew up in a small village in Sundargarh, where hockey is played in every field.",
    "Within a few years, she was selected for the state team."],
   "RPSQ", ["RSPQ", "PRSQ", "RPQS"],
   "R introduces Sunita and her village, P is how she began ('She' needs Sunita named first), S what followed ('Within a few years'), Q the present ('Today'). "
   "2025 Q87 to Q90 rewarded exactly this: a pronoun or a time word can never start a paragraph.")
rp(["It was built in the thirteenth century by King Narasimhadeva I.",
    "The Sun Temple at Konark is one of the finest monuments of Odisha.",
    "Today it is a UNESCO World Heritage Site and attracts visitors from all over the world.",
    "The whole temple is designed as a huge chariot with twelve pairs of wheels."],
   "QPSR", ["QSPR", "PQSR", "RQPS"],
   "Q names the topic, P says who built it ('It' needs the temple named first), S describes its design, R comes last with 'Today'. "
   "Paragraphs move from introduction to history to description to the present.")
rp(["Then he wrote down three small goals for every day.",
    "Ramesh found it hard to study for long hours.",
    "Within a month, he was finishing more work than ever before.",
    "So he decided to change the way he planned his day."],
   "QSPR", ["QPSR", "SQPR", "QSRP"],
   "Q is the problem, S the decision ('So'), P the first step ('Then'), R the result ('Within a month'). "
   "Time words (then, within a month) and 'So' fix the order of a story paragraph.")

# ================================================================ Comprehension (2 passages × 5)
P1 = (
"Raja is one of the most loved festivals of Odisha. It is celebrated for three days in the middle of June, when the first "
"monsoon showers arrive. The people of Odisha believe that during these days Mother Earth, like a woman, rests and prepares "
"herself for the new season of growth. So the festival honours both the earth and womanhood.\n\n"
"During Raja, all farm work stops. No one ploughs the fields or digs the soil, because the earth must not be disturbed while she "
"rests. Young girls are the centre of the celebration. They wear new clothes, put alta on their feet and do no household work. "
"They play games and enjoy themselves on swings tied to the branches of big trees. The songs they sing on these swings are full "
"of love, fun and the joy of the rain.\n\n"
"The first day is called Pahili Raja, the second Raja Sankranti, which marks the beginning of the solar month of Mithuna, and "
"the third Bhuin Daha or Basi Raja. Homes fill with the smell of poda pitha, a cake baked slowly over a fire, which is the "
"special dish of the festival. Friends and relatives visit each other, and villages come alive with games and music.\n\n"
"For a farming society, the festival has a clear meaning. The hot summer has ended, the rains have begun, and the fields will "
"soon be ready for sowing. By resting the earth and rejoicing at the same time, the people express their gratitude to nature "
"and their hope for a good harvest. In recent years Raja has also become popular in cities, where cultural programmes and "
"fairs keep the old tradition alive.")
PRE1 = "Read the passage on Raja and answer the question.\n"
add(CO, PRE1 + "According to the passage, why is ploughing stopped during Raja?",
    ["Because the earth must not be disturbed while she rests", "Because the fields are flooded by heavy rain",
     "Because farmers are busy baking poda pitha", "Because the government declares a holiday"],
    "Paragraph 2: 'No one ploughs the fields … because the earth must not be disturbed while she rests.' A detail question: the answer is a sentence of the passage in other words. "
    "2025 Q96 to Q100 (the Odisha hockey passage) were mostly detail questions.", p=P1, g="p1")
add(CO, PRE1 + "What is the second day of the festival called?",
    ["Raja Sankranti", "Pahili Raja", "Basi Raja", "Bhuin Daha"],
    "Paragraph 3: the first day is Pahili Raja, the second Raja Sankranti, the third Bhuin Daha or Basi Raja. "
    "Raja Sankranti begins the solar month of Mithuna.", p=P1, g="p1")
add(CO, PRE1 + "Which of the following can be inferred about the timing of the festival?",
    ["It is linked to the start of the farming season", "It is held after the harvest is gathered",
     "It marks the end of the monsoon", "It has no link with farming"],
    "The last paragraph says the rains have begun and the fields will soon be ready for sowing, so the festival comes just before the farming season starts. "
    "Inference questions ask what the passage suggests without saying it in one line (2025 Q94, Q99).", p=P1, g="p1")
add(CO, PRE1 + "Which is the most suitable title for the passage?",
    ["Raja: A Festival of the Earth and Womanhood", "The Monsoon in India",
     "How to Bake Poda Pitha", "Games Played by Young Girls"],
    "A title must cover the whole passage, not one detail. The passage is about what Raja celebrates, how and why. "
    "The other three are either too wide (monsoon in India) or only one detail. 2021 Q93 asked a title.", p=P1, g="p1")
add(CO, PRE1 + "The word 'gratitude', as used in the passage, means:",
    ["thankfulness", "sadness", "fear", "pride"],
    "Gratitude = the feeling of being thankful. People thank nature for the rain and hope for a good harvest. "
    "2021 Q94 asked the meaning of a word from the passage.", p=P1, g="p1")

P2 = (
"Not long ago, a child with a storybook was a common sight in every home. Today the same child is more likely to be holding a "
"mobile phone. Short videos, games and messages fill most of the free time that was once spent with books. Many teachers have "
"noticed that students now find it difficult to read a long chapter without losing interest.\n\n"
"This change matters because reading does more than pass the time. When we read a book, we have to build pictures in our own "
"minds, follow an argument from start to finish and remember what happened many pages earlier. These are skills of patience and "
"deep attention. A screen full of quick, bright images rarely asks for such effort; it rewards us for moving on to the next "
"thing as fast as we can.\n\n"
"Yet it would be wrong to blame technology alone. The same phone that distracts a student can also carry hundreds of books, free "
"newspapers and lectures by the best teachers in the country. The problem is not the tool but the way it is used. A knife can "
"cut vegetables or hurt a hand; what it does depends on the person holding it.\n\n"
"Some schools have found simple ways to bring back the reading habit. They keep the first twenty minutes of the day for silent "
"reading, in which the teachers also read their own books. Others run small class libraries where students choose what they "
"like rather than what they are told to read. Parents can help in the same way, by reading at home themselves. Children copy "
"what they see far more than what they hear.")
PRE2 = "Read the passage on reading and answer the question.\n"
add(CO, PRE2 + "What do some schools do in the first twenty minutes of the day?",
    ["Everyone, teachers included, reads silently", "Students watch short educational videos",
     "Teachers give lectures on good books", "Students write summaries of their books"],
    "Paragraph 4: the first twenty minutes are kept for silent reading, 'in which the teachers also read their own books'. A detail question.",
    p=P2, g="p2")
add(CO, PRE2 + "According to the passage, reading a book develops which of these?",
    ["Patience and deep attention", "Speed in moving from one thing to the next",
     "Skill in playing games", "The habit of watching short videos"],
    "Paragraph 2: building pictures, following an argument and remembering are 'skills of patience and deep attention'. "
    "Option 2 is what the screen rewards, the opposite.", p=P2, g="p2")
add(CO, PRE2 + "Why does the writer compare the mobile phone to a knife?",
    ["To show that its effect depends on how it is used", "To show that phones are dangerous and should be banned",
     "To show that phones are as cheap as knives", "To show that phones should be kept away from the kitchen"],
    "The sentence before says 'The problem is not the tool but the way it is used'; the knife can help or hurt depending on the user. "
    "The writer does not call for a ban, so option 2 goes too far: the usual trap in inference questions.", p=P2, g="p2")
add(CO, PRE2 + "Which is the most suitable title for the passage?",
    ["Reading in the Age of the Mobile Phone", "The History of Printed Books",
     "How to Make Short Videos", "Why Phones Must Be Banned in Schools"],
    "The passage is about the loss of the reading habit to phones and how to bring it back. "
    "The last option takes a side the writer rejects ('it would be wrong to blame technology alone').", p=P2, g="p2")
add(CO, PRE2 + "Which word is most nearly OPPOSITE in meaning to 'rarely' as used in the passage?",
    ["often", "seldom", "hardly", "scarcely"],
    "Rarely = not often. Its opposite is often (or frequently). Seldom, hardly and scarcely all mean nearly the same as rarely: the trap. "
    "Passage-word questions can ask the closest or the opposite meaning (2021 Q94).", p=P2, g="p2")
