S12 = ["Only 1", "Only 2", "Both 1 and 2", "Neither 1 nor 2"]
S3 = ["Only 1 and 2", "Only 2 and 3", "Only 1 and 3", "1, 2 and 3"]
def M(a, b, c, d):
    return "a-%d, b-%d, c-%d, d-%d" % (a, b, c, d)

META = dict(
    paper="ga",
    title="ASO GS Mock 05",
    hub_title="GS Mock 05",
    masthead="GS Mock 05",
    heading="General Studies Paper I · Mock 05",
    tagline="100 questions drawn by probability<br>from the <b>2018, 2021 and 2025</b> papers.",
    key="aso-gs-mock-2027-5",
    code="GS05",
    out="ASO-GS-Mock-Test-2027-5.html",
    minutes=90,
    seed=20261125,
    order="mixed",
    date="25 Nov 2026",
    draw="python3 .claude/skills/aso-mock/scripts/draw.py ga --n 100 --seed 791149",
    intro=[
        "This is a full General Awareness paper of 100 questions in 90 minutes, with +1 for a right answer and −0.25 for a wrong one. It was drawn by probability from the 2018, 2021 and 2025 papers (2018 counts half) and from the official syllabus, so likely families such as Polity, Modern History, Defence and Environment come up most. Every question is the next angle of a family the examiner has already used.",
        "Four questions are exact repeats of past questions (2025 Q75, 2025 Q17, 2021 Q35, 2021 Q49). About a quarter is 2026 news, always tied to a fact that stays true. Every explanation names the past question it grew from and the neighbouring facts that may come next.",
    ],
)

Q = []
def add(s, q, o, e, k="one", n=False, c=False, a=None, **x):
    d = dict(s=s, q=q, o=o, e=e, k=k, n=n, c=c, a=a); d.update(x); Q.append(d)

# ---------------- (a)(b) General News
add("General News", "Which of the following operations is NOT correctly matched with its purpose?",
    ["Operation Brahma – evacuation of Indians from Sudan", "Operation Dost – relief for the Türkiye–Syria earthquake", "Operation Ganga – evacuation of Indians from Ukraine", "Operation Ajay – evacuation of Indians from Israel"],
    "Why: Operation Brahma was India's relief help to Myanmar after the March 2025 earthquake. The Sudan evacuation was Operation Kaveri (2023). Grew from: 2025 Q11 (Operation Jindagi) and 2021 Q4 (Operation Sajag). Family: Operation Sindhu (evacuation from Iran, 2025) and Operation Urja Suraksha (Hormuz, 2026) come next.",
    k="not", n=True)
add("General News", "Which of the following statements is NOT correct?",
    ["Viktor Orbán won a fifth straight term in Hungary's election of April 2026.", "Tarique Rahman, leader of the BNP, became Prime Minister of Bangladesh in February 2026.", "Balendra Shah, a former mayor of Kathmandu, became Prime Minister of Nepal in March 2026.", "Sushila Karki headed Nepal's interim government before the 2026 election."],
    "Why: Orbán lost on 12 April 2026 to Péter Magyar's Tisza party after 16 years in power. The other three statements are true. Grew from: 2021 Q17 and 2021 Q12 (country news as a NOT-correct statement). Family: new leaders of 2025-26 (Takaichi in Japan, Pope Leo XIV, Lula in Brazil).",
    k="not", n=True)
add("General News", "Consider the following statements:\n1. Pope Leo XIV is the first Pope from the United States.\n2. Sanae Takaichi is the first woman Prime Minister of Japan.\n3. The Strait of Hormuz lies between Iran and Saudi Arabia.\nWhich of the statements given above are correct?",
    S3, "Why: Robert Prevost (Leo XIV) was chosen in May 2025 and Takaichi took office in October 2025, so 1 and 2 are right. The Strait of Hormuz lies between Iran and Oman, so 3 is false. Family: it links the Persian Gulf to the Gulf of Oman, and the 2026 Iran war closed it.",
    k="stmt", n=True, a=0)
add("General News", "Lula da Silva, re-elected in October 2026, begins which term as President of Brazil?",
    ["Fourth", "Third", "Second", "Fifth"],
    "Why: Lula won in 2002, 2006 and 2022, and again on 25 October 2026, so this is his fourth term. Grew from: 2018 Q7 (new Prime Minister of Italy), the 'new head of government' family. Family: Magyar (Hungary), Shah (Nepal), Rahman (Bangladesh).",
    n=True)
add("General News", "A pumped-storage hydropower plant, such as the Upper Indravati project in Odisha, is used to",
    ["store energy by pumping water uphill when power is cheap and release it to make power when demand is high", "make power only from the sea tides", "store natural gas underground for use in winter", "make power from the heat of the earth's crust"],
    "Why: A pumped-storage plant works like a giant water battery. It lifts water to an upper reservoir with spare power and runs it down through turbines at peak hours. Grew from: 2018 Q55 (what a new product is used for). Family: green hydrogen, battery storage and floating solar are the other storage and clean-power ideas in the news.",
    n=True)
add("General News", "Which of the following is NOT correctly matched?",
    ["Villages of Excellence programme – Japan", "Net Zero Vision for Bhubaneswar – United Kingdom", "Comprehensive Strategic Partnership of 2026 (Tashkent visit) – Uzbekistan", "3rd India–Australia Annual Summit of 2026 – Melbourne"],
    "Why: India's 'Villages of Excellence' plan (150 villages) was with Israel, not Japan. Grew from: 2021 Q3 (Israel) and 2025 Q25 (Net Zero Vision with the UK). Family: the partner country of an Indian programme or the venue of a bilateral summit in 2026.",
    k="not", n=True)
add("General News", "'Ambaji Mohanthal', which got a Geographical Indication (GI) tag in October 2026, is a traditional sweet of which State?",
    ["Gujarat", "Rajasthan", "Odisha", "Maharashtra"],
    "Why: Mohanthal is a gram-flour sweet offered at the Ambaji temple in Gujarat. A GI tag protects a product's name and says that it comes from one place. Grew from: 2021 Q6 (State and its dance, culture match). Family: GI tags in the news, festivals and their States, UNESCO lists (Sarnath became the 45th World Heritage Site in July 2026).",
    n=True)
add("General News", "In October 2026 the President gave assent to the Uniform Civil Code Bill of which State, after Uttarakhand became the first State with such a code?",
    ["Gujarat", "Assam", "Madhya Pradesh", "Rajasthan"],
    "Why: Gujarat's Bill got the President's assent in October 2026. Goa is not the first because it follows the old Portuguese Civil Code, which is a legacy law, not a new State UCC. Grew from: 2021 Q2 (which State presented a Child Budget). Family: State laws and name changes in the news (Kerala became Keralam by a simple Parliament law).",
    n=True)
add("General News", "The PM Viksit Gram Swaraj Yojana, approved in October 2026, aims to strengthen which institutions?",
    ["Panchayati Raj Institutions", "Cooperative banks", "Urban local bodies", "Self-help groups"],
    "Why: It is a centrally sponsored scheme for 2026-27 to 2030-31 that backs village councils (Panchayats). Grew from: 2018 Q20 (POSHAN Abhiyaan month). Family: the aim, Ministry or month of a scheme launched in 2025-26.",
    n=True)
add("General News", "Which writer won the Booker Prize 2026 at the age of 81, becoming its oldest winner?",
    ["M. John Harrison", "David Szalay", "Kiran Desai", "Banu Mushtaq"],
    "Why: M. John Harrison won in 2026 and is also the first Booker winner from science fiction. David Szalay won in 2025 for 'Flesh'. Banu Mushtaq won the International Booker 2025 for 'Heart Lamp' (Kannada). Grew from: 2018 Q21 (Magsaysay) and 2021 Q19 (a medal). Family: Magsaysay 2026 had no Indian winner (Tommy Koh, Runa Khan, Bo Kyi).",
    n=True)
add("General News", "The Human Development Index is published every year by",
    ["UNDP", "World Bank", "International Monetary Fund", "UNICEF"],
    "Why: The UNDP (United Nations Development Programme) publishes the Human Development Report with the HDI, which mixes health, education and income. Grew from: 2018 Q8 (Global Peace Index) and 2021 Q18 (World Giving Index). Family: ask who publishes a report before you learn India's rank: WEF (Gender Gap), IMF (World Economic Outlook).")
add("General News", "Which country brokered the two-week US–Iran ceasefire that began on 8 April 2026?",
    ["Pakistan", "Qatar", "Oman", "Türkiye"],
    "Why: Pakistan brought the two sides together and the truce began on 8 April 2026, about six weeks after the strikes of 28 February 2026. A US–Iran framework to end the war followed in June 2026. Grew from: 2021 Q12 and 2018 Q22 (country facts tied to news). Family: Pakistan also joined the Mecca Joint Defence Agreement (August 2026) with Saudi Arabia and Türkiye.",
    n=True)

# ---------------- (c) Modern History
add("Modern History", "Match List I with List II.\nList I\na. All India Trade Union Congress (1920)\nb. All India Kisan Sabha (1936)\nc. Swaraj Party (1923)\nd. Labour Swaraj Party (1925)\nList II\n1. Lala Lajpat Rai, first president\n2. Swami Sahajanand Saraswati, first president\n3. C. R. Das, president\n4. Kazi Nazrul Islam, founder member",
    [M(1,2,3,4), M(2,1,3,4), M(1,2,4,3), M(3,2,1,4)],
    "Why: Lajpat Rai led the AITUC at its first session in 1920, Sahajanand led the Kisan Sabha, C. R. Das and Motilal Nehru founded the Swaraj Party, and Nazrul Islam was a founder of the Labour Swaraj Party. The trap is the two similar party names. Grew from: 2025 Q58 and 2025 Q97 (Labour Swaraj Party) and 2018 Q67. Family: CPI Kanpur 1925, Meerut Conspiracy Case 1929.",
    k="match")
add("Modern History", "Which of the following Sikh misl chiefs is NOT correctly matched with his misl?",
    ["Ranjit Singh – Bhangi misl", "Jassa Singh Ahluwalia – Ahluwalia misl", "Charat Singh – Sukerchakia misl", "Hari Singh – Bhangi misl"],
    "Why: Ranjit Singh came from the Sukerchakia misl (his grandfather Charat Singh built it) and later joined all the misls into one Sikh State. Hari Singh led the Bhangi misl. Grew from: 2021 Q25 (the Bhangi clan). Family: Ahluwalia, Kanhaiya, Ramgarhia misls; Lahore (1799).",
    k="not")
add("Modern History", "Which man started 'Bengal Gazette' in 1780, the first newspaper of India?",
    ["James Augustus Hicky", "Raja Ram Mohan Roy", "Surendranath Banerjea", "Bal Gangadhar Tilak"],
    "Why: Hicky's weekly of Calcutta was the first newspaper and was soon shut for attacking the Company's officials. Roy started 'Sambad Kaumudi' (1821), Banerjea 'The Bengalee' and Tilak 'Kesari' and 'Mahratta'. Grew from: 2025 Q30 (Censorship of the Press Act 1799). Family: press laws in order, the founder of a paper.")
add("Modern History", "The Sadler Commission (1917) was set up to study the problems of",
    ["Calcutta University and university education", "Primary education in villages", "Education of women", "Technical education"],
    "Why: Michael Sadler studied Calcutta University and recommended separate intermediate colleges after Class 10 and a three-year degree course. Grew from: 2025 Q81 (order of the Hartog and Hunter commissions). Family: Wood 1854, Hunter 1882 (primary), Raleigh 1902 (universities), Hartog 1929, Sargent 1944.")
add("Modern History", "The first railway line of India, from Bombay to Thane (1853), was opened under which Governor-General?",
    ["Lord Dalhousie", "Lord William Bentinck", "Lord Canning", "Lord Ripon"],
    "Why: Dalhousie (1848-56) started railways, the telegraph and the postal system, and also used the Doctrine of Lapse. Bentinck banned sati (1829). Canning led the 1857 revolt years. Grew from: 2025 Q10 and 2018 Q86 (Ripon and the Ilbert Bill). Family: Lytton, Curzon, Mayo and what each is known for.")
add("Modern History", "Which Act made the Governor-General of Bengal the Governor-General of India?",
    ["Charter Act, 1833", "Regulating Act, 1773", "Pitt's India Act, 1784", "Charter Act, 1813"],
    "Why: The Charter Act of 1833 gave one law-making authority to the whole country and ended the Company's trade. William Bentinck became the first Governor-General of India. Grew from: 2018 Q28 (principle of elections), 2025 Q38 and Q76. Family: 1773, 1784, 1813, 1853, 1858, 1861, 1892, 1909, 1919, 1935.")
add("Modern History", "Arrange the following events of the British legal system in the order of time, earliest first:\n1. The Supreme Court at Calcutta\n2. The Cornwallis Code\n3. The Indian Penal Code enacted\n4. The Indian High Courts Act",
    ["1, 2, 3, 4", "2, 1, 3, 4", "1, 2, 4, 3", "1, 3, 2, 4"],
    "Why: Supreme Court at Calcutta 1774, Cornwallis Code 1793, Indian Penal Code (drafted by Macaulay) 1860, Indian High Courts Act 1861. Grew from: 2021 Q24 (order of colonial courts). Family: Sadr Diwani and Nizamat Adalat, the Regulating Act of 1773, the Law Commission.",
    k="order")
add("Modern History", "Who among the following was NOT a founder of the Congress Socialist Party (1934)?",
    ["Sardar Vallabhbhai Patel", "Jayaprakash Narayan", "Acharya Narendra Dev", "Ram Manohar Lohia"],
    "Why: The CSP was set up by young socialists inside the Congress at Patna in 1934, led by Narendra Dev (president) and J. P. Narayan (secretary). Patel stood with the Congress right wing and did not support it. Grew from: 2025 Q97 and 2025 Q58. Family: Meerut Conspiracy Case, Kisan Sabha 1936, Forward Bloc 1939.",
    k="not")
add("Modern History", "Which one of the following storm-centres of the Revolt of 1857 is wrongly matched?",
    ["Revolt at Faizabad - Hazrat Mahal", "Revolt at Kanpur - Nana Sahib", "Revolt at Jagdishpur - Kunwar Singh", "Revolt at Jhansi - Rani Lakshmibai"],
    "Why: At Faizabad the leader was Maulvi Ahmadullah Shah. Begum Hazrat Mahal led the revolt at Lucknow. Grew from: 2025 Q75 (asked word for word) and 2018 Q29. Family: Bakht Khan (Delhi), Khan Bahadur (Bareilly), Surendra Sai (Sambalpur).",
    k="not", src="2025 Q75")
add("Modern History", "The Haripura session of the Indian National Congress (1938) was presided over by",
    ["Subhas Chandra Bose", "Jawaharlal Nehru", "Rajendra Prasad", "Maulana Abul Kalam Azad"],
    "Why: Bose presided over Haripura in 1938 and was re-elected at Tripuri in 1939, defeating Pattabhi Sitaramayya, then quit the post. Grew from: 2018 Q88 (Gandhi at Belgaum), 2025 Q31 (Karachi) and 2025 Q54 (Poorna Swaraj, Lahore 1929). Family: presidents of key sessions (Bonnerjee 1885, Surat 1907, Lucknow 1916, Nagpur 1920).")
add("Modern History", "Consider the following statements:\n1. Bal Gangadhar Tilak is known as 'Lokmanya'.\n2. Madhusudan Das is known as 'Utkalmani'.\n3. Khan Abdul Ghaffar Khan is known as the 'Frontier Gandhi'.\nWhich of the statements given above are correct?",
    S3, "Why: Madhusudan Das is 'Utkal Gourav'; the title 'Utkalmani' belongs to Gopabandhu Das. The other two titles are right. Grew from: 2025 Q96 (Lala Lajpat Rai's titles). Family: Punjab Kesari, Deshbandhu, Netaji, Mahatma, Deenbandhu.",
    k="stmt", a=2)

# ---------------- (d) Polity
add("Polity", "The 'None of the Above' (NOTA) option was introduced in Indian elections after a Supreme Court judgment of 2013 in",
    ["PUCL v. Union of India", "Kesavananda Bharati v. State of Kerala", "Minerva Mills v. Union of India", "S. R. Bommai v. Union of India"],
    "Why: In PUCL v. Union of India (2013) the Court said voters have the right to reject all candidates. The other three are famous for the basic structure and Article 356. Grew from: 2025 Q83 (election method for the Lok Sabha). Family: voting age 18 (61st Amendment), delimitation, reserved seats.")
add("Polity", "After the 2019 amendment of the Protection of Human Rights Act, the term of the Chairperson and members of the NHRC is",
    ["3 years or till the age of 70, whichever is earlier", "5 years or till the age of 70, whichever is earlier", "5 years or till the age of 65, whichever is earlier", "6 years or till the age of 65, whichever is earlier"],
    "Why: The 2019 amendment cut the term from five years to three, and members can be reappointed. The 65 and 6-year form belongs to the CAG and Election Commission. Grew from: 2018 Q65, 2021 Q51 and 2025 Q87 (NHRC every year). Family: State Human Rights Commissions, removal by the President after a Supreme Court inquiry.")
add("Polity", "From which of the following countries was the provision of the nomination of Rajya Sabha members borrowed?",
    ["Ireland", "Australia", "United Kingdom", "USA"],
    "Why: The Irish Constitution lets the head of state nominate members of its upper house, and India took the idea. Ireland also gave the Directive Principles and the method of electing the President. Grew from: 2025 Q17 (asked word for word). Family: UK (parliamentary system), USA (Fundamental Rights), Canada (strong Centre), Australia (Concurrent List).",
    src="2025 Q17")
add("Polity", "Who / Which of the following can abolish a State Legislative Council?",
    ["Parliament", "Governor", "President", "State Assembly"],
    "Why: Under Article 169 Parliament abolishes or creates a Council by a law, after the State Assembly passes a resolution by a special majority. The Assembly alone cannot do it. Grew from: 2021 Q35 (asked word for word) and 2025 Q33 (minimum age 30). Family: six States have a Council, one-third retire every two years.",
    src="2021 Q35")
add("Polity", "Under the 44th Amendment, which Articles of the Constitution cannot be suspended even during a National Emergency?",
    ["Articles 20 and 21", "Articles 14 and 19", "Articles 19 and 21", "Articles 21 and 32"],
    "Why: Right against conviction without law (20) and Right to life and personal liberty (21) stay alive in any Emergency. Article 19 stops only during a war or external aggression Emergency. Grew from: 2018 Q16 (privacy) and 2025 Q6 (maternity leave), both Article 21. Family: Article 359 and the 44th Amendment (1978).")
add("Polity", "The idea of Fundamental Duties in the Indian Constitution was borrowed from the Constitution of",
    ["The USSR", "Japan", "South Africa", "France"],
    "Why: The USSR Constitution listed duties of citizens, and India added Part IV-A (Article 51A) by the 42nd Amendment in 1976. Japan gave 'procedure established by law' and South Africa the amendment procedure. Grew from: 2021 Q31 (single citizenship) and 2025 Q17 (Rajya Sabha nominations). Family: the source country of each feature.")
add("Polity", "Article 24 of the Constitution prohibits the employment of children below which age in factories, mines and other hazardous work?",
    ["14 years", "12 years", "16 years", "18 years"],
    "Why: Article 24 (Right against Exploitation) bars child labour below 14 in dangerous work. Article 23 bans forced labour and trafficking. Grew from: 2021 Q32 and Q33 (Article 21A) and 2025 Q82 (Articles on religion). Family: Article 17 (untouchability), 21A (education for ages 6 to 14), 25 to 28 (religion).")
add("Polity", "The Attorney General of India is appointed by the President under which Article?",
    ["Article 76", "Article 148", "Article 165", "Article 124"],
    "Why: Article 76 creates the Attorney General, who must be fit to be a Supreme Court judge. Article 148 is the CAG, 165 the Advocate General of a State and 124 the Supreme Court. Grew from: 2021 Q40 (who appoints the CAG). Family: the AG may speak in Parliament but cannot vote.")
add("Polity", "Which of the following is NOT a right recognised by the Supreme Court as part of Article 21?",
    ["Right to strike", "Right to privacy", "Right to livelihood", "Right to menstrual health"],
    "Why: The Court has held that there is no Fundamental Right to strike. Privacy (Puttaswamy, 2017), livelihood (Olga Tellis) and menstrual health (January 2026) were all read into Article 21. Grew from: 2018 Q16 and 2025 Q6. Family: clean environment, speedy trial, shelter, dignified death (2018).",
    k="not", n=True)
add("Polity", "Arrange the following provisions in the order in which they appear in the Constitution of India, from the lowest Article number:\n1. The right to vote\n2. The right to education\n3. Equality before law\n4. Protection of property by law",
    ["3, 2, 4, 1", "3, 4, 2, 1", "2, 3, 4, 1", "3, 2, 1, 4"],
    "Why: Equality before law is Article 14, the Right to Education is Article 21A, protection of property is Article 300A and the right to vote is Article 326. Voting and property are legal rights, not Fundamental Rights. Grew from: 2021 Q34 (which right deals with voting). Family: the 44th Amendment moved property out of Part III.",
    k="order")
add("Polity", "Which of the following Constitutional Amendments is NOT correctly matched with its subject?",
    ["74th Amendment – Panchayati Raj institutions", "61st Amendment – voting age lowered to 18", "86th Amendment – Right to Education", "42nd Amendment – addition of the word 'Socialist' to the Preamble"],
    "Why: The 73rd Amendment deals with Panchayats; the 74th deals with urban local bodies (Municipalities). Grew from: 2018 Q75, 2021 Q37, Q39 and 2025 Q91. Family: 1st, 7th, 24th, 44th, 52nd, 69th, 91st, 97th, 101st, 103rd, 104th, 106th.",
    k="not")
add("Polity", "Which of the following is NOT correctly matched?",
    ["Ernest Barker – 'identity card of the Constitution'", "K. M. Munshi – 'political horoscope of the Constitution'", "N. A. Palkhivala – 'identity card of the Constitution'", "Thakur Das Bhargava – 'soul of the Constitution'"],
    "Why: Ernest Barker called the Preamble the 'keynote' of the Constitution. The 'identity card' phrase is Palkhivala's. Grew from: 2025 Q35 (Barker's keynote), 2025 Q32 and 2018 Q34. Family: Objectives Resolution (Nehru, 13 December 1946), Berubari, Kesavananda.",
    k="not")
add("Polity", "Free legal aid to the poor is directed by which Article of the Constitution?",
    ["Article 39A", "Article 38", "Article 41", "Article 46"],
    "Why: Article 39A was added to the Directive Principles by the 42nd Amendment (1976). Article 41 is the right to work and education, and 46 is the interest of weaker sections. Grew from: 2025 Q78 (Article 51) and 2025 Q98 (a DPSP added in 1976). Family: 40 (panchayats), 44 (UCC), 45, 48, 48A, 50.")
add("Polity", "The Goods and Services Tax (GST) was introduced by which Constitutional Amendment?",
    ["101st Amendment, 2016", "103rd Amendment, 2019", "104th Amendment, 2020", "106th Amendment, 2023"],
    "Why: The 101st Amendment inserted Article 279A (GST Council) and GST began on 1 July 2017. The 103rd gave the EWS quota, the 104th ended Anglo-Indian seats and the 106th reserved a third of the seats for women. Grew from: 2021 Q37 and 2025 Q91 (amendment and its year). Family: the Article behind each amendment.")

# ---------------- (e) World geography
add("World Geography", "Match List I (name of tropical storm) with List II (region).\nList I\na. Hurricane\nb. Typhoon\nc. Willy-willy\nd. Cyclone\nList II\n1. Indian Ocean\n2. North-western Australia\n3. China Sea and Western Pacific\n4. Atlantic Ocean and Caribbean",
    [M(4,3,2,1), M(3,4,2,1), M(4,3,1,2), M(2,3,4,1)],
    "Why: All four are the same kind of storm named differently by region. Hurricanes form over the Atlantic and Caribbean, typhoons over the China Sea, willy-willies off north-west Australia, and cyclones over the Indian Ocean. Grew from: 2021 Q68 (match cyclone and region). Family: Baguio (Philippines), Coriolis force, cyclone naming (Montha, Senyar).",
    k="match")
add("World Geography", "Which of the following temperate or tropical grassland and country pairs is NOT correctly matched?",
    ["Downs – South Africa", "Llanos – Venezuela", "Campos – Brazil", "Veldt – South Africa"],
    "Why: The Downs are grasslands of south-eastern Australia. The Veldt is the grassland of South Africa. Llanos lie along the Orinoco in Venezuela and Colombia, and Campos are in Brazil. Grew from: 2021 Q63 (not correctly matched) and 2025 Q53 (savannas). Family: Prairies, Pampas, Steppes, Savanna.",
    k="not")
add("World Geography", "The temperate grasslands of Argentina and Uruguay are called",
    ["Pampas", "Prairies", "Veldt", "Downs"],
    "Why: The Pampas lie in southern South America. The Prairies are in North America. Grew from: 2021 Q63 and 2025 Q53. Family: Llanos and Campos are tropical grasslands of South America, the Steppes lie in Eurasia.")
add("World Geography", "The deepest point of the Atlantic Ocean lies in the",
    ["Puerto Rico Trench", "Sunda (Java) Trench", "Tonga Trench", "Mariana Trench"],
    "Why: The Puerto Rico Trench is the deepest part of the Atlantic. The Mariana Trench (Challenger Deep) is the deepest in the world, in the Pacific. The Java Trench is the deepest in the Indian Ocean. Grew from: 2025 Q70 (deepest part of the ocean) and 2018 Q80 (Ninety East Ridge). Family: Mid-Atlantic Ridge, Sargasso Sea, Dead Sea salinity.")
add("World Geography", "The Steppes are temperate grasslands found mainly in",
    ["Eurasia", "North America", "South America", "Australia"],
    "Why: Steppes cover Central Asia and eastern Europe, from Ukraine to Mongolia. Prairies are in North America and Pampas in South America. Grew from: 2021 Q63 (grassland pairs) and 2025 Q53. Family: continent and temperate or tropical for each grassland.")
add("World Geography", "Consider the following statements:\n1. The Madden–Julian Oscillation is a pulse of tropical rain that moves eastwards in about 30 to 60 days.\n2. The Southern Oscillation is a see-saw of air pressure over the Pacific Ocean.\n3. La Niña is a warming of the central Pacific Ocean.\nWhich of the statements given above are correct?",
    S3, "Why: La Niña is a cooling of the central and eastern Pacific, so 3 is false. The other two are right, and El Niño with the Southern Oscillation is together called ENSO. Grew from: 2025 Q39 (Indian Ocean Dipole and El Niño). Family: the effect of each on the Indian monsoon.",
    k="stmt", a=0)
add("World Geography", "Which one of the following is a warm ocean current?",
    ["Gulf Stream", "Labrador Current", "Benguela Current", "Peru (Humboldt) Current"],
    "Why: The Gulf Stream carries warm water from the Gulf of Mexico towards Europe. The other three are cold currents. Grew from: 2021 Q62 (a current of the southern hemisphere). Family: Kuroshio (warm), Canary and California (cold), West Wind Drift.")
add("World Geography", "In Köppen's scheme, the climate symbol 'Af' stands for",
    ["Tropical rainforest climate", "Tropical savanna climate", "Hot desert climate", "Humid subtropical climate"],
    "Why: 'A' is a hot tropical group and 'f' means wet in all months, so Af is the rainforest. 'Aw' is savanna, 'BWh' hot desert and 'Cfa' humid subtropical. Grew from: 2021 Q69 (match Köppen symbol and climate). Family: Mediterranean (Cs), tundra (ET).")

# ---------------- (f) India
add("India Geography", "Which of the following is NOT correct about the Indian monsoon and seasons?",
    ["'Loo' is a cold, moist winter wind of the Himalayan foothills.", "Mango showers are pre-monsoon showers of Kerala and Karnataka.", "Kal Baisakhi is a pre-monsoon storm of West Bengal and the north-east.", "The retreating monsoon brings rain to the Tamil Nadu coast in October and November."],
    "Why: Loo is a hot, dry wind of the northern plains in May and June. The other three statements are right. Grew from: 2021 Q75 (scholars of climatic regions) and 2021 Q79 (monsoon fluctuation). Family: ITCZ and jet streams, Mawsynram, Köppen, Stamp, Trewartha.",
    k="not")
add("India Geography", "Consider the following statements:\n1. Shipki La lies in Himachal Pradesh.\n2. Bomdi La lies in Arunachal Pradesh.\n3. Jelep La lies in Sikkim.\nWhich of the statements given above are correct?",
    S3, "Why: Shipki La (Sutlej valley) is in Himachal Pradesh, Bomdi La near Tawang is in Arunachal Pradesh, and Jelep La, like Nathu La, is in Sikkim. All three are correct. Grew from: 2021 Q80 (pass that does not belong to the State). Family: Zoji La, Banihal, Rohtang, Lipulekh, Nathu La.",
    k="stmt", a=3)
add("India Geography", "Which of the following is NOT correct about Indian soils?",
    ["Red soil gets its colour from calcium carbonate.", "Black soil is formed from volcanic lava and holds moisture well.", "Laterite soil is formed by heavy rain leaching and is found in Odisha and the Western Ghats.", "Alluvial soil is formed by river deposits and is the most widespread soil of India."],
    "Why: Red soil is red because of iron oxide. Black soil (regur) comes from Deccan lava and suits cotton. Grew from: 2021 Q73 (largest forest type). Family: tropical deciduous forest is the largest; mangroves at the Sundarbans and Bhitarkanika.",
    k="not")
add("India Geography", "The Indravati river is a tributary of which major river?",
    ["Godavari", "Mahanadi", "Krishna", "Kaveri"],
    "Why: The Indravati rises in Kalahandi (Odisha) and joins the Godavari after crossing Chhattisgarh. The Upper Indravati project is in Odisha. Grew from: 2021 Q72 (rivers of the Maikal range). Family: Narmada and Son start at Amarkantak; the Mahanadi starts near Sihawa in Chhattisgarh.")
add("India Geography", "The Lipulekh Pass, a route to Kailash Mansarovar, lies in which State?",
    ["Uttarakhand", "Sikkim", "Himachal Pradesh", "Arunachal Pradesh"],
    "Why: Lipulekh is on the border of Uttarakhand with Tibet and Nepal. The other Kailash route is through Nathu La in Sikkim. Shipki La is in Himachal Pradesh. Grew from: 2021 Q80 (pass and State). Family: Rohtang (Himachal), Banihal (J&K), Zoji La (Ladakh).")

# ---------------- Odisha
add("Odisha", "Arrange the following rivers of Odisha from north to south, along the coast:\n1. Mahanadi\n2. Subarnarekha\n3. Rushikulya\n4. Brahmani",
    ["2, 4, 1, 3", "2, 1, 4, 3", "4, 2, 1, 3", "2, 4, 3, 1"],
    "Why: The Subarnarekha is in the far north (Balasore), then the Brahmani, the Mahanadi and, in the south, the Rushikulya in Ganjam. Grew from: 2021 Q76 and 2025 Q94 (Hirakud and the Mahanadi canal). Family: Baitarani, Budhabalanga, Vansadhara.",
    k="order")
add("Odisha", "Which of the following is NOT correct?",
    ["The Paika Rebellion of 1817 was led by Veer Surendra Sai.", "Odisha became a separate province on 1 April 1936.", "The Treaty of Deogaon (1803) with the Bhonsle ruler of Nagpur brought Odisha under British rule.", "Veer Surendra Sai of Sambalpur fought the British in the 1850s and 1860s."],
    "Why: The Paika Rebellion was led by Bakshi Jagabandhu Bidyadhar. Surendra Sai fought in the 1857 period at Sambalpur. Grew from: 2018 Q27 (Odisha history NOT correct). Family: Utkal Divas 1 April (90th year in 2026), Utkal Sammilani 1903, Madhusudan Das.",
    k="not")
add("Odisha", "The Barehipani waterfall, one of the highest in India, lies in which protected area of Odisha?",
    ["Similipal National Park", "Bhitarkanika National Park", "Satkosia Tiger Reserve", "Chilika Lake"],
    "Why: Barehipani (about 399 m) and Joranda are the two big falls of Similipal in Mayurbhanj district. Bhitarkanika is the mangrove park of Kendrapara. Grew from: 2025 Q16 (Hexadeltaic region) and 2025 Q79 (Odisha's mineral places). Family: regions, hills in order, rivers and the projects built on them.")
add("Odisha", "The Rengali multipurpose project is built on which river?",
    ["Brahmani", "Mahanadi", "Baitarani", "Rushikulya"],
    "Why: Rengali dam, in Angul district, is on the Brahmani. Hirakud is on the Mahanadi. Grew from: 2025 Q94 (Hirakud's irrigation). Family: Upper Indravati (Kalahandi), Balimela (Machkund), Salandi (Baitarani basin).")

# ---------------- (g) Governance
add("Governance", "Where is the Lal Bahadur Shastri National Academy of Administration (LBSNAA), which trains IAS officers, located?",
    ["Mussoorie", "Hyderabad", "Dehradun", "Mount Abu"],
    "Why: LBSNAA is in Mussoorie, Uttarakhand. The National Police Academy and NIRDPR are in Hyderabad. Grew from: 2025 Q15, Q37 and Q71. Family: IIPA (New Delhi, 1954), SVPNPA (1948 at Mount Abu, Hyderabad since 1975), Gopabandhu Academy (Bhubaneswar).")
add("Governance", "Which of the following training institutes is NOT correctly matched with its place?",
    ["Sardar Vallabhbhai Patel National Police Academy – Mussoorie", "Indian Institute of Public Administration – New Delhi", "Gopabandhu Academy of Administration – Bhubaneswar", "National Academy of Direct Taxes – Nagpur"],
    "Why: The Police Academy was started at Mount Abu in 1948 and has been in Hyderabad since 1975. Mussoorie hosts LBSNAA. Grew from: 2025 Q37 (SVPNPA statements). Family: NIRDPR in Hyderabad, ISTM, Gopabandhu Academy of Administration in Bhubaneswar.",
    k="not")
add("Governance", "Who described the Indian Civil Service as the 'steel frame' of British rule in India?",
    ["David Lloyd George", "Lord Cornwallis", "Lord Macaulay", "Lord Lee"],
    "Why: Lloyd George, the British Prime Minister, used the phrase in 1922. Cornwallis is called the Father of the Civil Services in India. Grew from: 2025 Q95 (Lee Commission). Family: Islington Commission (1912), Aitchison Commission (1886), Public Service Commission (1926).")
add("Governance", "Which of the following is a form of judicial control over the administration?",
    ["A writ of mandamus issued by a High Court", "Discussion of the budget in Parliament", "Transfer of an officer by the Cabinet Secretary", "Audit report of the CAG"],
    "Why: Courts control the administration through writs, review of orders and damages. Budget discussion and audit are legislative controls and transfer is an executive control. Grew from: 2018 Q49 (executive control) and 2021 Q44 (citizens' control). Family: the Lokpal, Lokayuktas and the Right to Information Act.")
add("Governance", "Which of the following is NOT correct about the Citizen's Charter?",
    ["It is legally enforceable in a court of law.", "It tells citizens what service standards to expect from an office.", "The idea began in the United Kingdom in 1991.", "India's Sevottam model was introduced in 2006."],
    "Why: A Citizen's Charter is a promise, not a law, so it cannot be enforced in a court. Grew from: 2025 Q1 (Sevottam). Family: CPGRAMS, Right to Services laws (Madhya Pradesh 2010), the 1997 Chief Ministers' conference.",
    k="not")
add("Governance", "Which of the following is NOT associated with reforms of the civil services in India?",
    ["Sarkaria Commission", "Kothari Committee", "Satish Chandra Committee", "Hota Committee"],
    "Why: The Sarkaria Commission (1983) studied Centre–State relations. Kothari (1976) shaped the UPSC exam, Satish Chandra (1989) revised it and Hota (2004) studied civil services reform. Grew from: 2025 Q41 and 2021 Q46. Family: Baswan (2016), Yugandhar (training), Alagh (2001).",
    k="not")

# ---------------- (g) Economy
add("Economy", "The Consumer Price Index (CPI) of India is released by",
    ["National Statistical Office (MoSPI)", "Office of the Economic Adviser, DPIIT", "Reserve Bank of India", "NITI Aayog"],
    "Why: The NSO under the Ministry of Statistics publishes the CPI. The Wholesale Price Index comes from the Office of the Economic Adviser in the Commerce Ministry. Family: the RBI's target is 4 per cent, within a band of 2 to 6 per cent; cost-push, demand-pull and stagflation. Grew from: syllabus line on inflation, never asked yet.")
add("Economy", "Consider the following statements:\n1. Narasimham Committee dealt with banking sector reforms.\n2. Chelliah Committee recommended inflation targeting.\n3. Urjit Patel Committee recommended CPI as the anchor for inflation.\nWhich of the statements given above are correct?",
    S3, "Why: Chelliah's committee (1991) was about tax reform, so 2 is false. The Urjit Patel Committee (2014) moved the RBI to CPI-based inflation targeting. Grew from: 2025 Q61 (Pherwani Committee and NSE). Family: Kelkar (tax), Rangarajan (poverty, disinvestment).",
    k="stmt", a=2)
add("Economy", "The Deendayal Antyodaya Yojana–National Rural Livelihoods Mission (DAY-NRLM) is run by which Ministry?",
    ["Ministry of Rural Development", "Ministry of Skill Development", "Ministry of Housing and Urban Affairs", "Ministry of Panchayati Raj"],
    "Why: DAY-NRLM builds women's self-help groups in villages; it is a Rural Development scheme. Grew from: 2018 Q54 (skill development scheme for youth). Family: PMKVY, SANKALP (Skill Development), DAY-NULM (Housing and Urban Affairs).")
add("Economy", "Consider the following statements:\n1. Revenue deficit is revenue expenditure minus revenue receipts.\n2. Primary deficit is the fiscal deficit minus interest payments.\n3. The FRBM Act was passed in 2013.\nWhich of the statements given above are correct?",
    S3, "Why: Statements 1 and 2 are right. The FRBM Act was passed in 2003, so 3 is false. Grew from: 2025 Q65 (what is NOT a part of the fiscal deficit). Family: effective revenue deficit, fiscal deficit target, the 2018 FRBM review.",
    k="stmt", a=0)
add("Economy", "How many members does the Monetary Policy Committee (MPC) of the RBI have?",
    ["Six", "Five", "Seven", "Nine"],
    "Why: Three members come from the RBI, including the Governor, and three are named by the Government, so there are six. The Governor has a casting vote. Grew from: 2018 Q76 (repo rate) and 2025 Q68 (what the RBI does not do). Family: repo, reverse repo, CRR, SLR, RBI founded 1935 and nationalised 1949.")
add("Economy", "Who among the following had adopted the strategy of 'Rolling Plan'?",
    ["Morarji Desai", "Jawaharlal Nehru", "Rajiv Gandhi", "Narendra Modi"],
    "Why: The Janata government under Morarji Desai adopted the Rolling Plan (1978-80), an idea of Gunnar Myrdal. Each year the plan is reviewed and a new year is added. Grew from: 2021 Q49 (asked word for word), 2018 Q51 and 2025 Q40. Family: Plan holiday 1966-69, Mahalanobis (2nd Plan), NITI Aayog 2015.",
    src="2021 Q49")

# ---------------- (h) Defence
add("Defence", "India's Army exercise DUSTLIK is held with which country?",
    ["Uzbekistan", "Kazakhstan", "Kyrgyzstan", "Tajikistan"],
    "Why: DUSTLIK is with Uzbekistan (the 2026 edition was the 7th, April 2026). KAZIND is with Kazakhstan and KHANJAR with Kyrgyzstan. Grew from: 2021 Q20 and 2025 Q90 (Dharma Guardian), 2025 Q55 (Nomadic Elephant). Family: Yudh Abhyas (USA), Shakti (France), Mitra Shakti (Sri Lanka), AUSTRAHIND (Australia).",
    n=True)
add("Defence", "The Light Combat Helicopter 'Prachand' is made by",
    ["Hindustan Aeronautics Limited", "Bharat Electronics Limited", "Bharat Dynamics Limited", "Mazagon Dock Shipbuilders"],
    "Why: HAL makes the LCH Prachand, the ALH Dhruv and the Tejas. BEL makes radars, BDL missiles and Mazagon ships. Grew from: 2018 Q56 and Q57, 2021 Q85 and Q87. Family: where each system came from: Rafale (France), S-400 (Russia), Apache (USA).")
add("Defence", "Which Central Armed Police Force is known as the 'Sentinels of the North-East'?",
    ["Assam Rifles", "Border Security Force", "Indo-Tibetan Border Police", "Central Reserve Police Force"],
    "Why: Assam Rifles, raised in 1835 as the Cachar Levy, guards the Myanmar border and fights insurgency in the North-East. It is under the Home Ministry but run by the Army. Grew from: 2025 Q29 (ITBP). Family: ITBP (1962), SSB (Nepal, Bhutan), BSF (1965).",
    n=True)
add("Defence", "Consider the following statements:\n1. The CISF provides security to airports and nuclear plants.\n2. The CRPF was raised in 1939 as the Crown Representative's Police.\n3. The National Security Guard (NSG) works under the Ministry of Defence.\nWhich of the statements given above are correct?",
    S3, "Why: The NSG, the Black Cat commando force, comes under the Ministry of Home Affairs, so 3 is false. Grew from: 2025 Q29 (ITBP statements). Family: CAPFs all work under the Home Ministry; raising year and duty of each.",
    k="stmt", n=True, a=0)
add("Defence", "Which of the following is a five-star rank of the Indian Air Force?",
    ["Marshal of the Air Force", "Air Chief Marshal", "Air Marshal", "Air Vice Marshal"],
    "Why: The five-star ranks are Field Marshal (Army), Admiral of the Fleet (Navy) and Marshal of the Air Force. Arjan Singh got the last in 2002. Air Chief Marshal is the four-star rank of the Chief. Grew from: 2021 Q90 (Squadron Leader equals Major). Family: equal ranks across the three Services.")
add("Defence", "The Chief of Defence Staff is also the head of which department of the Ministry of Defence?",
    ["Department of Military Affairs", "Department of Defence Production", "Department of Defence Research and Development", "Department of Ex-servicemen Welfare"],
    "Why: The CDS is a permanent chairman of the Chiefs of Staff Committee and Secretary of the Department of Military Affairs, created in 2019. The 2026 task of the new CDS, N. S. Raja Subramani, is to set up theatre commands. Grew from: 2021 Q82 (Chief of Air Staff). Family: the 2026 changes of the three chiefs.",
    n=True)
add("Defence", "Consider the following statements about missile technology:\n1. Hypersonic speed means a speed above Mach 1.\n2. A ramjet engine has no rotating compressor.\n3. The LRAShM tested by DRDO is a hypersonic anti-ship glide vehicle.\nWhich of the statements given above are correct?",
    S3, "Why: Hypersonic means above Mach 5, not Mach 1, so 1 is false. A ramjet squeezes air by the speed of the vehicle itself. LRAShM is the Long-Range Anti-Ship Missile. Grew from: 2025 Q51 (scramjet). Family: Pralay (RCI, quasi-ballistic, 350-500 km) and the AD-1 interceptor.",
    k="stmt", n=True, a=1)
add("Defence", "The Pinaka multi-barrel rocket launcher system of the Indian Army was designed by",
    ["DRDO", "Hindustan Aeronautics Limited", "Bharat Electronics Limited", "Mazagon Dock Shipbuilders"],
    "Why: DRDO's Armament Research and Development Establishment, Pune, designed Pinaka, and a long-range version was tested from Chandipur, Odisha, in 2026. HAL makes aircraft and BEL radars. Grew from: 2021 Q84 (Missile Woman) and 2018 Q56 (first indigenous tank, Arjun). Family: what DRDO, HAL, BEL and BDL each make.",
    n=True)
add("Defence", "The National Defence Academy (NDA), which trains cadets of all three Services, is located at",
    ["Khadakwasla, Pune", "Dehradun", "Ezhimala", "Wellington"],
    "Why: NDA is at Khadakwasla near Pune. The IMA is in Dehradun, the Naval Academy at Ezhimala and the Defence Services Staff College at Wellington. Grew from: 2018 Q58 and 2021 Q81 (INDU at Binola). Family: AFA Dundigal, National Defence College (New Delhi), CDM Secunderabad.")
add("Defence", "Consider the following statements:\n1. SIMBEX is a naval exercise between India and Singapore.\n2. Varuna is a naval exercise between India and Germany.\n3. IBSAMAR is held among India, Brazil and South Africa.\nWhich of the statements given above are correct?",
    S3, "Why: Varuna is with France, so 2 is false. SIMBEX-2026 was the 33rd edition at Visakhapatnam, and IBSAMAR IX ended at Simon's Town in October 2026. Grew from: 2025 Q4 (TROPEX-25). Family: Malabar (Japan, 2026), KONKAN (UK), Milan.",
    k="stmt", n=True, a=2)
add("Defence", "The headquarters of the Eastern Naval Command of the Indian Navy is at",
    ["Visakhapatnam", "Mumbai", "Kochi", "Karwar"],
    "Why: Eastern Command is in Visakhapatnam, Western in Mumbai and Southern in Kochi. Karwar hosts the large Project Seabird base. Grew from: 2025 Q14 (military places and new names) and 2021 Q85 (naval induction). Family: the International Fleet Review and MILAN 2026 were held off Visakhapatnam.",
    n=True)
add("Defence", "Consider the following statements:\n1. Red Flag is an air exercise hosted by France.\n2. Tarang Shakti is a multinational air exercise hosted by India.\n3. Desert Flag is hosted by the United Arab Emirates.\nWhich of the statements given above are correct?",
    S3, "Why: Red Flag is held by the United States Air Force, so 1 is false. Grew from: 2025 Q73 (Desert Flag-10). Family: Pitch Black (Australia), Garuda (France), Udara Shakti (Malaysia).",
    k="stmt", n=True, a=1)
add("Science & Tech", "Tuberculosis is caused by",
    ["A bacterium", "A virus", "A protozoan", "A fungus"],
    "Why: TB is caused by Mycobacterium tuberculosis and spreads through the air by coughing. Mumps is a viral airborne disease. Malaria is protozoan. Grew from: 2025 Q24 (Mumps). Family: vector and type of each disease, vaccines (BCG for TB).")
add("Science & Tech", "The 2025 Nobel Prize in Physics honoured work on",
    ["Quantum tunnelling in an electrical circuit large enough to be held in the hand", "The discovery of the Higgs boson", "The detection of gravitational waves", "Pulses of light lasting attoseconds"],
    "Why: John Clarke, Michel Devoret and John Martinis won in 2025 for showing quantum behaviour in a circuit you can see. Higgs (2013), gravitational waves (2017) and attosecond light (2023) are earlier prizes. Grew from: 2021 Q91 (the 2019 Chemistry prize). Family: ask the year before too.",
    n=True)
add("Environment", "The gradual process by which one plant community replaces another in the same area over time is called",
    ["Ecological succession", "Adaptation", "Migration", "Speciation"],
    "Why: Succession starts with pioneer species on bare rock and ends in a stable climax community. Grew from: 2025 Q23 and Q84 (endemic and edge species). Family: niche, biome, food web, ecotone.")
add("Environment", "Match List I with List II.\nList I (Biogeographic zone of India)\na. Trans-Himalaya\nb. Desert\nc. Western Ghats\nd. Gangetic Plain\nList II (Typical animal)\n1. Great Indian Bustard\n2. Snow leopard\n3. Gangetic dolphin\n4. Lion-tailed macaque",
    [M(2,1,4,3), M(1,2,4,3), M(2,1,3,4), M(4,1,2,3)],
    "Why: The snow leopard lives in the cold Trans-Himalaya, the Great Indian Bustard in the Thar and nearby dry lands, the lion-tailed macaque in the Western Ghats rainforest and the dolphin in the Ganga. Grew from: 2025 Q93 (match the biogeographic regions). Family: India has ten zones, including Semi-arid, Deccan, North-East, Coasts and Islands.",
    k="match")
add("Environment", "Match List I with List II.\nList I\na. IPCC set up\nb. UNFCCC adopted\nc. Paris Agreement\nd. India's net-zero target year\nList II\n1. 1988\n2. 1992\n3. 2015\n4. 2070",
    [M(1,2,3,4), M(2,1,3,4), M(1,2,4,3), M(3,2,1,4)],
    "Why: The IPCC was set up by the WMO and UNEP in 1988, the UNFCCC came from the 1992 Earth Summit at Rio, the Paris Agreement is of 2015 and India promised net-zero by 2070. Grew from: 2025 Q66 (evidence of global warming) and 2021 Q99. Family: glacier retreat, carbon sinks, COP31 (Antalya, November 2026).",
    k="match")
add("Environment", "Which is India's first National Park?",
    ["Jim Corbett National Park", "Kaziranga National Park", "Gir National Park", "Kanha National Park"],
    "Why: Corbett, in Uttarakhand, was set up in 1936 as Hailey National Park. Kaziranga (Assam) is famous for the one-horned rhino and Gir for the Asiatic lion. Grew from: 2018 Q70 (Manas) and 2021 Q92 (Jaypore). Family: tiger reserves (58 with Madhav, MP) and new Ramsar sites.")
add("Environment", "The PM Surya Sarovar Yojana, approved in July 2026, supports which kind of project?",
    ["Floating solar power plants", "Offshore wind farms", "Green hydrogen hubs", "Rooftop solar for homes"],
    "Why: The scheme backs 5,000 MW of floating solar with storage, with an outlay of ₹5,070 crore. Rooftop solar is PM Surya Ghar. Grew from: 2021 Q98 (largest solar park). Family: Bhadla and Khavda solar parks, the National Green Hydrogen Mission.",
    n=True)
add("Environment", "Which of the following belongs to the nekton of an ocean?",
    ["Tuna", "Diatoms", "Copepods", "Jellyfish"],
    "Why: Nekton are animals that swim actively against the current, like fish and whales. Plankton drift: diatoms (plants) and copepods (animals). Jellyfish are weak swimmers and count as plankton. Grew from: 2018 Q13 (the upper part of an aquatic ecosystem). Family: the 10 per cent law, assimilation efficiency (2021 Q100).")
add("Environment", "Which of the following ecological pyramids is always upright?",
    ["Pyramid of energy", "Pyramid of numbers", "Pyramid of biomass", "Pyramid of biomass in a sea"],
    "Why: Energy is lost at each level, so the pyramid of energy is always upright. The pyramids of numbers and biomass can be inverted, for example in a pond. Grew from: 2018 Q13 and 2021 Q100. Family: food chain and food web, trophic levels.")
add("Environment", "How many of the world's biodiversity hotspots lie, wholly or partly, in India?",
    ["Four", "Two", "Six", "Eight"],
    "Why: India has four: the Himalaya, Indo-Burma, the Western Ghats and Sri Lanka, and Sundaland (Nicobar Islands). Norman Myers gave the hotspot idea. Grew from: 2021 Q94 and Q97. Family: alpha, beta and gamma diversity, in-situ and ex-situ conservation.")
add("Environment", "The Forest Survey of India, which publishes the India State of Forest Report, has its headquarters at",
    ["Dehradun", "New Delhi", "Bhopal", "Kolkata"],
    "Why: FSI is in Dehradun, and it publishes the ISFR every two years. Madhya Pradesh has the largest forest area and Mizoram the highest percentage. Grew from: 2018 Q48 and 2025 Q92 (forest cover by State). Family: mangrove cover (West Bengal leads), India's total forest and tree cover.")
add("Environment", "In which IUCN Red List category is the Great Indian Bustard placed?",
    ["Critically Endangered", "Endangered", "Vulnerable", "Near Threatened"],
    "Why: Only a small number of the birds are left, mostly in Rajasthan, so it is Critically Endangered. In October 2026 captive-bred birds were released at Desert National Park, Jaisalmer. Grew from: 2025 Q100 (first mammal extinct from climate change). Family: gharial, vultures, Asiatic lions (891 in 2025).",
    n=True)
add("Environment", "The Basel Convention deals with",
    ["The movement of hazardous wastes across borders", "Trade in endangered animals and plants", "Wetlands of international importance", "Protection of the ozone layer"],
    "Why: The Basel Convention (1989) controls the export of hazardous waste. CITES covers wildlife trade, Ramsar wetlands and Montreal the ozone layer. Grew from: 2018 Q63, 2021 Q16 and Q60, 2025 Q69 (Kyoto). Family: Rotterdam, Stockholm and Minamata (mercury).")
add("Environment", "Which of the following is NOT correct about Olive Ridley turtles in Odisha?",
    ["The Gahirmatha beach lies in Ganjam district.", "Rushikulya is a mass-nesting beach in Ganjam district.", "Mass nesting is called 'arribada'.", "Operation Olivia is run by the Indian Coast Guard."],
    "Why: Gahirmatha is in Kendrapara district, in Bhitarkanika. Rushikulya is the beach in Ganjam. Grew from: 2018 Q62 (NOT correct about Olive Ridleys) and 2025 Q27 (Rushikulya nesting). Family: the Devi river mouth, IUCN Vulnerable.",
    k="not")

# ---------------- (j) Institutions
add("Institutions", "The 'World Economic Outlook' report is published by",
    ["International Monetary Fund", "World Bank", "World Economic Forum", "UNCTAD"],
    "Why: The IMF issues it twice a year. The World Bank publishes South Asia Economic Focus (asked in 2021) and the WEF the Global Gender Gap Report. Grew from: 2021 Q15. Family: Human Development Report (UNDP), Global Hunger Index.",
    n=True)
add("Institutions", "The International Court of Justice (ICJ) has its seat at",
    ["The Hague", "Geneva", "New York", "Brussels"],
    "Why: The ICJ, the UN's main court, sits in The Hague. The Permanent Court of Arbitration, which gave an award on the Indus Waters Treaty on 31 August 2026 (India rejected it), is also at The Hague. Grew from: 2021 Q55 (NATO's HQ) and 2025 Q8 (SpaceX). Family: WTO Geneva, IMO London, ISA Gurugram.")
add("Institutions", "Which city hosted the Heads of State summit of the Shanghai Cooperation Organisation in 2026?",
    ["Bishkek", "Tianjin", "Astana", "Dushanbe"],
    "Why: The 2026 SCO summit was in Bishkek, Kyrgyzstan (31 August - 1 September), ending in the Bishkek Declaration. Tianjin hosted in 2025. Dushanbe hosted only the Heads of Government meeting in October 2026. Grew from: 2021 Q53 (virtual SCO summit) and 2025 Q44 (BIMSTEC Youth Summit). Family: BRICS (New Delhi, September 2026), G20 (Miami, December 2026).",
    n=True)
add("Institutions", "The headquarters of the Food and Agriculture Organization (FAO) is at",
    ["Rome", "Geneva", "Paris", "Vienna"],
    "Why: FAO is in Rome. WMO and ILO are in Geneva, UNESCO in Paris and the IAEA in Vienna. Grew from: 2018 Q97 (not a UN agency) and 2025 Q5 (WMO). Family: ICRC, which is not a UN agency, and the 2025 Q74 title of Goodwill Ambassador.")
add("Institutions", "The 'Gujral Doctrine' is associated with India's policy towards",
    ["Neighbouring countries", "The United States", "The Soviet Union", "Gulf countries"],
    "Why: I. K. Gujral's doctrine of 1996-97 said India should help smaller neighbours without asking for the same in return. Panchsheel (1954) was with China. Grew from: 2021 Q30 (Panchsheel). Family: Look East, Act East, Neighbourhood First.")
add("Institutions", "Match List I with List II.\nList I\na. International Solar Alliance\nb. Coalition for Disaster Resilient Infrastructure (CDRI)\nc. Global Biofuels Alliance\nd. One Sun One World One Grid\nList II\n1. Launched at COP21, Paris, 2015\n2. Launched at the UN Climate Action Summit, 2019\n3. Launched at the G20 Summit, New Delhi, 2023\n4. Announced at COP26, Glasgow, 2021",
    [M(1,2,3,4), M(2,1,3,4), M(1,2,4,3), M(3,2,1,4)],
    "Why: The ISA (HQ Gurugram) came with France in 2015. CDRI was launched in 2019, the Global Biofuels Alliance at the 2023 G20 and OSOWOG at COP26. Grew from: 2021 Q52 (ISA's HQ) and 2021 Q59 (One Sun One World One Grid). Family: the Bahamas became the 116th ISA member in 2026.",
    k="match")
add("Institutions", "Which of the following was NOT one of the five founding leaders of the Non-Aligned Movement?",
    ["Fidel Castro", "Jawaharlal Nehru", "Gamal Abdel Nasser", "Josip Broz Tito"],
    "Why: The NAM was started in 1961 at Belgrade by Nehru, Nasser (Egypt), Tito (Yugoslavia), Sukarno (Indonesia) and Nkrumah (Ghana). Castro joined later as the leader of Cuba. Grew from: 2018 Q64 (whose concept was NAM), 2021 Q13 and Q54. Family: members of SAARC, NATO, BIMSTEC, SCO, BRICS.",
    k="not")
add("Institutions", "MINURSO, the UN mission that ended in 2026 after 35 years, worked in",
    ["Western Sahara", "Cyprus", "Kosovo", "Lebanon"],
    "Why: MINURSO (UN Mission for the Referendum in Western Sahara) began in 1991 in north-west Africa. UNFICYP is in Cyprus and UNIFIL in Lebanon. Grew from: 2018 Q97 and 2025 Q5 (UN bodies). Family: the UN Security Council (five new members elected each year for two years).",
    n=True)


