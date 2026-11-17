# Questions for GS Mock 02. In every item the FIRST option is the right one,
# unless "a" is given (then the options stay in the written order).
# k: one | stmt | match | not | order.  n: needs 2025-26 news.  c: Check tag.

S12 = ["Only 1", "Only 2", "Both 1 and 2", "Neither 1 nor 2"]
def M(a, b, c, d):  # match answer text
    return "a-%d, b-%d, c-%d, d-%d" % (a, b, c, d)

Q = []
def add(s, q, o, e, k="one", n=False, c=False, a=None):
    Q.append(dict(s=s, q=q, o=o, e=e, k=k, n=n, c=c, a=a))

# ------------------------------------------------------------------ POLITY (16)
P = "Polity"
add(P, "The provision for suspending Fundamental Rights during an Emergency was borrowed from the constitution of:",
    ["Germany (Weimar Constitution)", "Canada", "Australia", "Ireland"],
    "The Weimar Constitution of Germany gave the idea. Past papers asked single citizenship (Britain, 2021) and nomination of Rajya Sabha members (Ireland, 2025), so another 'borrowed from' question is likely. Also learn: Concurrent List and joint sitting from Australia; strong Centre and residuary powers from Canada; Fundamental Duties from the USSR; amendment procedure from South Africa; Directive Principles and the method of electing the President from Ireland.")
add(P, "Consider the following statements about the Preamble:\n1. In the Berubari Union case (1960), the Supreme Court said the Preamble is not a part of the Constitution.\n2. In the Kesavananda Bharati case (1973), the Supreme Court said the Preamble is a part of the Constitution.\n3. The Preamble has been amended only once so far.\nWhich of the statements given above are correct?",
    ["Only 1 and 2", "Only 2 and 3", "Only 1 and 3", "1, 2 and 3"],
    "All three are correct. The Court changed its view in 1973: the Preamble is a part of the Constitution and can be amended, but its basic features cannot be destroyed. It was amended once, by the 42nd Amendment (1976), which added 'Socialist', 'Secular' and 'Integrity'. The Preamble cannot be enforced in a court. The Preamble was asked in 2018 and twice in 2025.",
    k="stmt", a=3)
add(P, "The Rajya Sabha must return a Money Bill to the Lok Sabha, with or without its recommendations, within:",
    ["14 days", "30 days", "six weeks", "six months"],
    "Article 109 gives the Rajya Sabha only 14 days. The Lok Sabha may accept or reject its recommendations (asked in 2025). Article 110 defines a Money Bill and the Speaker's decision on it is final. A Money Bill starts only in the Lok Sabha, needs the President's recommendation, and there is no joint sitting on it.")
add(P, "Match List I (Office) with List II (Minimum age):\nList I: a. Member of a Panchayat  b. Member of the Lok Sabha  c. Member of a Legislative Council  d. Governor\nList II: 1. 35 years  2. 21 years  3. 30 years  4. 25 years",
    [M(2, 4, 3, 1), M(2, 3, 4, 1), M(4, 2, 3, 1), M(2, 4, 1, 3)],
    "Panchayat or Municipality member 21; Lok Sabha and Legislative Assembly 25; Rajya Sabha and Legislative Council 30; President, Vice-President and Governor 35. The 2025 paper asked the Legislative Council age (30).", k="match")
add(P, "Consider the following statements about the Governor of a State:\n1. The Governor is appointed by the President.\n2. The Governor holds office during the pleasure of the President.\n3. The Governor can be removed by the State Legislature through impeachment.\n4. The same person can be appointed Governor of two or more States.\nWhich of the statements given above are correct?",
    ["Only 1 and 2", "Only 1, 2 and 4", "Only 2, 3 and 4", "1, 2, 3 and 4"],
    "Statement 3 is wrong: there is no impeachment of a Governor. The President appoints (Article 155) and can remove the Governor at any time (Article 156). The 7th Amendment (1956) allowed one person to be Governor of two or more States. Minimum age is 35. The 2025 paper asked which commission wanted non-partisan Governors (Sarkaria). Odisha: Braj Mohan Ram was named Governor in October 2026, after Hari Babu Kambhampati.",
    k="stmt", a=1)
add(P, "The Comptroller and Auditor General of India is called the 'friend, philosopher and guide' of the:",
    ["Public Accounts Committee", "Estimates Committee", "Finance Commission", "NITI Aayog"],
    "The CAG's audit reports are examined by the Public Accounts Committee (22 members: 15 from the Lok Sabha and 7 from the Rajya Sabha; its chairman is usually from the Opposition). The CAG is appointed by the President (asked in 2021) under Article 148, serves six years or till the age of 65, and gives the reports to the President (Article 151). The present CAG is K. Sanjay Murthy.")
add(P, "Which Schedule of the Constitution contains the forms of oaths and affirmations?",
    ["Third Schedule", "Second Schedule", "Fourth Schedule", "Seventh Schedule"],
    "The 2025 paper used this as a trap by pairing oaths with the Second Schedule. Second = salaries and allowances; Third = oaths; Fourth = seats in the Rajya Sabha; Fifth = Scheduled Areas; Sixth = tribal areas of Assam, Meghalaya, Tripura and Mizoram; Seventh = the three lists; Eighth = 22 languages; Ninth = laws kept away from court review (added by the 1st Amendment, 1951); Tenth = defection; Eleventh = Panchayats; Twelfth = Municipalities.")
add(P, "Which Article of the Constitution asks the State to separate the judiciary from the executive?",
    ["Article 50", "Article 48", "Article 44", "Article 40"],
    "Article 50 was one of the wrong options in the 2025 question on foreign policy (Article 51), so it is a likely next question. Learn the Directive Principles by number: 39A free legal aid (added in 1976, asked in 2025), 40 village panchayats, 44 uniform civil code, 45 early childhood care, 47 nutrition and prohibition, 48 agriculture and cow protection, 48A environment, 51 international peace.")
add(P, "The voting age in India was lowered from 21 years to 18 years by the:",
    ["61st Amendment Act, 1988", "44th Amendment Act, 1978", "73rd Amendment Act, 1992", "86th Amendment Act, 2002"],
    "The 61st Amendment changed Article 326. It was passed in 1988 and came into force in 1989. Amendments asked so far: 42nd (2025), 44th and 99th (2021), 69th (2018), 91st (2025). Others to learn: 52nd anti-defection, 73rd Panchayats, 74th Municipalities, 86th Right to Education, 101st GST, 103rd EWS quota, 106th women's reservation.")
add(P, "The name of Kerala was changed to 'Keralam' in 2026. Under which Article can Parliament change the name of a State by an ordinary law?",
    ["Article 3", "Article 368", "Article 356", "Article 1"],
    "Under Article 3, Parliament can form new States and change the area, boundary or name of a State by a simple majority. The Bill needs the President's recommendation, and the President first sends it to the State Legislature for its views, which are not binding. Article 4 says such a law is not an amendment under Article 368. Orissa became Odisha in 2011. The 2025 paper listed 'altering the boundary of States' as an option.",
    n=True)
add(P, "Which writ is issued by a court to ask a person by what authority he or she holds a public office?",
    ["Quo Warranto", "Mandamus", "Certiorari", "Habeas Corpus"],
    "Quo Warranto means 'by what warrant'. Mandamus ('we command', asked in 2018) orders an official to do a public duty. Habeas Corpus frees a person held illegally. Prohibition stops a lower court from going on with a case. Certiorari quashes an order already passed by a lower court. The Supreme Court issues writs under Article 32 and the High Courts under Article 226.")
add(P, "Which of the following Fundamental Rights is available only to citizens of India and not to foreigners?",
    ["The six freedoms under Article 19", "Equality before law under Article 14", "Protection of life and personal liberty under Article 21", "Freedom of religion under Article 25"],
    "Five Articles are for citizens only: 15, 16, 19, 29 and 30. All others, such as Articles 14, 20, 21, 21A and 25 to 28, are for every person in India. The 2025 paper asked the Articles on religion (25 to 28) and the 2021 paper asked Article 21A.")
add(P, "In January 2026 the Supreme Court held that menstrual health and hygiene is a part of the right to life and dignity. This right flows from:",
    ["Article 21", "Article 14", "Article 19", "Article 32"],
    "Both earlier court questions in this exam were also about Article 21: the right to privacy (2018) and maternity leave (2025). Rights read into Article 21 include privacy, livelihood, clean environment, speedy trial, sleep, and health. This item rests on news reports, so confirm it once before the exam.",
    n=True, c=True)
add(P, "Which of the following States does NOT have a Legislative Council?",
    ["Odisha", "Bihar", "Karnataka", "Telangana"],
    "Only six States have a Legislative Council: Andhra Pradesh, Telangana, Uttar Pradesh, Bihar, Maharashtra and Karnataka. Under Article 169, Parliament can create or abolish a Council by an ordinary law after the State Assembly passes a resolution by a special majority (asked in 2021). A Council member must be 30 years old (asked in 2025). Its size cannot be more than one-third of the Assembly or less than 40.", k="not")
add(P, "A member of a State Public Service Commission, such as the OPSC, holds office for six years or until the age of:",
    ["62 years", "60 years", "65 years", "70 years"],
    "State PSC: six years or 62. UPSC: six years or 65. The Governor appoints the chairman and members of a State PSC, but only the President can remove them. Articles 315 to 323 deal with the Commissions. A Joint State PSC is created by Parliament (asked in 2025). The 2021 paper asked which jobs a former member can take.")
add(P, "Consider the following statements about the National Human Rights Commission:\n1. A former Chief Justice of India or a former Judge of the Supreme Court can be its Chairperson.\n2. The Chairperson holds office for five years or until the age of 70.\n3. It was set up under the Protection of Human Rights Act, 1993.\nWhich of the statements given above are correct?",
    ["Only 1 and 2", "Only 2 and 3", "Only 1 and 3", "1, 2 and 3"],
    "Statement 2 is wrong. The 2019 amendment cut the term from five years to three years (or the age of 70) and also allowed a former Supreme Court Judge to be Chairperson. The NHRC was asked in 2018 (who can be chairman), 2021 (first chairman: Ranganath Misra) and 2025 (selection committee). The present Chairperson is Justice V. Ramasubramanian.",
    k="stmt", a=2)

# ---------------------------------------------------------- MODERN HISTORY (13)
H = "Modern History"
add(H, "Consider the following statements about the Permanent Settlement:\n1. It was introduced by Lord Cornwallis in 1793.\n2. It made the zamindars the owners of the land.\n3. Under it, the land revenue was revised every thirty years.\nWhich of the statements given above are correct?",
    ["Only 1", "Only 1 and 2", "Only 2 and 3", "1, 2 and 3"],
    "Statement 3 is wrong: the revenue was fixed for ever, which is why it is called 'permanent'. It covered Bengal, Bihar and Orissa. The 2025 paper asked the Ryotwari system (Madras and Bombay; Thomas Munro and Alexander Read; revenue taken straight from the ryot). The third system is Mahalwari (Holt Mackenzie, 1822; North-Western Provinces and Punjab; settled with the village).",
    k="stmt", a=1)
add(H, "Open competition for recruitment to the civil services in India was introduced by the:",
    ["Charter Act of 1853", "Charter Act of 1833", "Indian Councils Act, 1861", "Government of India Act, 1858"],
    "The Charter Act of 1853 ended the Company's power to nominate civil servants. The Macaulay Committee (1854) then framed the exam, and Satyendranath Tagore became the first Indian ICS officer in 1863. Charter Act 1813: ₹1 lakh for education (asked in 2021). Charter Act 1833: Governor-General of India, and Macaulay as the first Law Member (asked in 2025).")
add(H, "The office of the Secretary of State for India was created by the:",
    ["Government of India Act, 1858", "Regulating Act, 1773", "Pitt's India Act, 1784", "Indian Councils Act, 1892"],
    "After the Revolt of 1857, the 1858 Act moved power from the Company to the Crown. The Secretary of State, helped by a 15-member Council of India, sat in London, and the Governor-General also became the Viceroy (Lord Canning, asked in 2025). Regulating Act 1773: Governor-General of Bengal and a Supreme Court at Calcutta. Pitt's India Act 1784: Board of Control. 1892: a start of elections (asked in 2018). 1935: provincial autonomy and a federal court (asked in 2025).")
add(H, "Who is called the 'Father of Local Self-Government' in India?",
    ["Lord Ripon", "Lord Mayo", "Lord Lytton", "Lord Curzon"],
    "Ripon's Resolution of 1882 set up local boards with elected members. He also repealed the Vernacular Press Act, passed the first Factory Act (1881), set up the Hunter Education Commission (1882) and faced the Ilbert Bill row (asked in 2018 and 2025). Lytton: Vernacular Press Act, Arms Act and the Delhi Durbar of 1877. Dufferin: the Congress was founded in his time (1885). Curzon: Partition of Bengal (1905).")
add(H, "Which of the following pairs is NOT correctly matched?",
    ["Comrade – Abul Kalam Azad", "Utkal Dipika – Gourishankar Ray", "The Samaja – Gopabandhu Das", "New India – Annie Besant"],
    "Comrade (1911) was started by Maulana Mohammad Ali. Azad ran Al-Hilal. Utkal Dipika (1866) was the first Odia newspaper and The Samaja (1919) was started by Utkalmani Gopabandhu Das. Newspaper questions came in 2021 and twice in 2025. More pairs: Sambad Kaumudi – Rammohan Roy; Rast Goftar – Dadabhai Naoroji; Mook Nayak – B. R. Ambedkar; Hindu – G. Subramania Iyer; Amrita Bazar Patrika – Sisir Kumar Ghosh.", k="not")
add(H, "In March 1929, communist and trade union leaders such as Muzaffar Ahmed, S. A. Dange and P. C. Joshi were arrested and tried in the:",
    ["Meerut Conspiracy Case", "Kakori Conspiracy Case", "Lahore Conspiracy Case", "Alipore Bomb Case"],
    "The Meerut Conspiracy Case (1929–33) was the government's attack on the labour movement. The 2025 paper asked two questions on the Labour Swaraj Party (1925), whose leaders included Muzaffar Ahmed and Qazi Nazrul Islam, so this family is live. Earlier, Dange and Muzaffar Ahmed were also tried in the Kanpur Bolshevik Conspiracy Case (1924). Kakori (1925) was a train robbery by the HRA; the Lahore case was against Bhagat Singh; Alipore (1908) was against Aurobindo Ghosh.")
add(H, "Who presided over the Karachi Session of the Indian National Congress (1931), which passed the resolution on Fundamental Rights and the National Economic Programme?",
    ["Sardar Vallabhbhai Patel", "Motilal Nehru", "Jawaharlal Nehru", "Subhas Chandra Bose"],
    "The 2025 paper gave 'Motilal Nehru presided' as a false statement, so the true name is the natural next question. The session was held a few days after Bhagat Singh was hanged, and it approved the Gandhi–Irwin Pact. Other sessions: Belgaum 1924, the only one under Gandhi (asked in 2018); Lahore 1929, Purna Swaraj under Jawaharlal Nehru; Faizpur 1936, the first in a village; Tripuri 1939, Bose beat Pattabhi Sitaramayya.")
add(H, "Arrange Gandhiji's early struggles in India in the order in which they took place (earliest first):\n1. Kheda Satyagraha\n2. Rowlatt Satyagraha\n3. Champaran Satyagraha\n4. Ahmedabad Mill Strike",
    ["3, 4, 1, 2", "3, 1, 4, 2", "4, 3, 1, 2", "3, 4, 2, 1"],
    "Champaran (1917, indigo farmers) → Ahmedabad Mill Strike (early 1918, his first hunger strike) → Kheda (1918, no-tax struggle) → Rowlatt Satyagraha (1919). The 2018 paper asked the order of the later movements: Rowlatt (1919), Simon boycott (1928), Civil Disobedience (1930), Quit India (1942). Gandhi also founded the Ahmedabad Textile Labour Association (asked in 2018).", k="order")
add(H, "Match List I (Organisation) with List II (Founder):\nList I: a. Indian Association (1876)  b. Poona Sarvajanik Sabha (1870)  c. East India Association (1866)  d. Mohammedan Literary Society (1863)\nList II: 1. Dadabhai Naoroji  2. Abdul Latif  3. Surendranath Banerjea  4. M. G. Ranade",
    [M(3, 4, 1, 2), M(3, 1, 4, 2), M(4, 3, 1, 2), M(3, 4, 2, 1)],
    "These are the bodies that came before the Congress. The 2025 paper asked the Central National Mohammedan Association (Syed Amir Ali) with Abdul Latif as a wrong option, and mentioned the journal of the Poona Sarvajanik Sabha. Also learn: Madras Mahajan Sabha (1884), Bombay Presidency Association (1885, Pherozeshah Mehta), British Indian Association (1851).", k="match")
add(H, "Which document is known as the 'Magna Carta of English Education in India'?",
    ["Wood's Despatch, 1854", "Macaulay's Minute, 1835", "Hunter Commission Report, 1882", "Sargent Plan, 1944"],
    "Charles Wood's Despatch asked for a full system from primary school to university. The universities of Calcutta, Bombay and Madras followed in 1857. The order of education bodies was asked in 2025: Hunter (1882) → Raleigh (1902) → Sadler (1917) → Hartog (1929) → Wardha scheme (1937) → Sargent (1944) → Radhakrishnan (1948) → Kothari (1964).")
add(H, "Who called Bal Gangadhar Tilak the 'Father of Indian Unrest'?",
    ["Valentine Chirol", "Lord Curzon", "Lord Minto", "Annie Besant"],
    "Valentine Chirol, a British journalist, wrote this in his book 'Indian Unrest' (1910). Tilak ran Kesari (Marathi) and Mahratta (English) and said 'Swaraj is my birthright'. The 2025 paper had a statement question on Lala Lajpat Rai (Punjab Kesari; he founded 'The Punjabee'), so the other two of Lal–Bal–Pal are likely. Bipin Chandra Pal edited New India and Bande Mataram.")
add(H, "The Indian National Army (INA) was first formed in 1942 by:",
    ["Captain Mohan Singh", "Subhas Chandra Bose", "Rash Behari Bose", "Shah Nawaz Khan"],
    "Mohan Singh raised the first INA from Indian prisoners of war in Malaya and Singapore. Rash Behari Bose led the Indian Independence League. Subhas Chandra Bose took charge in 1943 and set up the Provisional Government of Free India at Singapore on 21 October 1943 (asked in 2018). The INA trials were held at the Red Fort in 1945.")
add(H, "Which of the following was NOT part of the alliance defeated by the British at the Battle of Buxar (1764)?",
    ["Siraj-ud-Daulah", "Mir Qasim", "Shuja-ud-Daulah", "Shah Alam II"],
    "Siraj-ud-Daulah was defeated earlier, at Plassey (1757). At Buxar, Hector Munro beat Mir Qasim of Bengal, Shuja-ud-Daulah of Awadh and the Mughal emperor Shah Alam II. The Treaty of Allahabad (1765) then gave the Company the Diwani (right to collect revenue) of Bengal, Bihar and Orissa. Wandiwash (1760), which ended the French challenge, was asked in 2018.", k="not")

# ------------------------------------------------------------------ DEFENCE (10)
D = "Defence"
add(D, "Who took over as India's third Chief of Defence Staff on 31 May 2026?",
    ["General N. S. Raja Subramani", "General Anil Chauhan", "General Upendra Dwivedi", "Admiral Dinesh K. Tripathi"],
    "The 2021 paper asked 'the present Chief of Air Staff', and all four top posts changed in 2026. CDS: General N. S. Raja Subramani (after Anil Chauhan; the first CDS was Bipin Rawat). Army: General Dhiraj Seth, from 30 June 2026. Navy: Admiral Krishna Swaminathan, from 31 May 2026. Air Force: Air Chief Marshal Ashutosh Dixit, from 31 October 2026.",
    n=True)
add(D, "Match List I (Military exercise) with List II (Partner country):\nList I: a. KHANJAR  b. DUSTLIK  c. KAZIND  d. Garuda Shakti\nList II: 1. Uzbekistan  2. Indonesia  3. Kyrgyzstan  4. Kazakhstan",
    [M(3, 1, 4, 2), M(1, 3, 4, 2), M(3, 4, 1, 2), M(4, 1, 3, 2)],
    "The three Central Asian names are the trap. KHANJAR is with Kyrgyzstan (2026: Misamari, Assam). DUSTLIK is with Uzbekistan (2026: in Uzbekistan). KAZIND is with Kazakhstan. Garuda Shakti is the special forces exercise with Indonesia. Asked before: Dharma Guardian with Japan (2021 and 2025; the 7th edition was in Uttarakhand in 2026) and Nomadic Elephant with Mongolia (2025). Also: Yudh Abhyas – USA, Shakti – France, AUSTRAHIND – Australia, Surya Kiran – Nepal, Sampriti – Bangladesh.",
    k="match", n=True)
add(D, "Consider the following statements:\n1. MILAN is a bilateral naval exercise held only between India and Japan.\n2. In February 2026, MILAN and the International Fleet Review were held off Visakhapatnam.\nWhich of the statements given above is/are correct?",
    S12,
    "MILAN is a multilateral exercise hosted by the Indian Navy every two years. It began in 1995 in the Andaman and Nicobar Islands and later moved to Visakhapatnam, the base of the Eastern Naval Command. The India–Japan naval exercise is JIMEX. The 2025 paper had the same kind of statement question on TROPEX-25. Confirm the 2026 dates once before the exam.",
    k="stmt", n=True, c=True, a=1)
add(D, "Which of the following countries is NOT a participant in the naval exercise 'Malabar'?",
    ["France", "Japan", "Australia", "United States"],
    "Malabar began in 1992 between India and the USA. Japan became a permanent member in 2015 and Australia joined in 2020. The same four countries form the Quad (asked in 2021). India's naval exercise with France is Varuna. The 2025 paper asked this 'who did not take part' style on Exercise Sea Dragon.", k="not")
add(D, "Consider the following statements:\n1. Agni-5 is a surface-to-surface ballistic missile with a range of more than 5,000 km.\n2. BrahMos is a subsonic cruise missile developed by India and Israel.\n3. Akash is a surface-to-air missile.\nWhich of the statements given above are correct?",
    ["Only 1 and 2", "Only 2 and 3", "Only 1 and 3", "1, 2 and 3"],
    "BrahMos is a supersonic cruise missile made by India and Russia (the name joins the Brahmaputra and the Moskva). The 2025 paper used the same trick on Pralay, which is a surface-to-surface quasi-ballistic missile with a range of about 150 to 500 km. Others: Prithvi – short-range surface-to-surface; Astra – air-to-air; Nag – anti-tank; Nirbhay – subsonic cruise; S-400 – bought from Russia (asked in 2021).",
    k="stmt", a=2)
add(D, "Consider the following statements about the Border Security Force (BSF):\n1. It was raised in 1965.\n2. It guards India's borders with Pakistan and Bangladesh.\n3. It works under the Ministry of Defence.\nWhich of the statements given above are correct?",
    ["Only 1 and 2", "Only 2 and 3", "Only 1 and 3", "1, 2 and 3"],
    "All the Central Armed Police Forces work under the Ministry of Home Affairs. The 2025 paper had a three-statement question on the ITBP (raised in 1962, China border), so another force is likely. SSB (1963): Nepal and Bhutan. Assam Rifles (1835, the oldest): Myanmar. CISF (1969): airports and industries. CRPF (1939): internal security. The Coast Guard (1978) is under the Ministry of Defence.",
    k="stmt", a=0)
add(D, "Which of the following pairs is NOT correctly matched?",
    ["Officers Training Academy – Pune", "Indian Military Academy – Dehradun", "Indian Naval Academy – Ezhimala", "Air Force Academy – Dundigal"],
    "The Officers Training Academy is at Chennai (a second one is at Gaya). Pune has the National Defence Academy at Khadakwasla. The Indian National Defence University at Binola, Haryana was asked in 2018 and 2021. Others: National Defence College – New Delhi; Defence Services Staff College – Wellington; College of Defence Management – Secunderabad; Sardar Vallabhbhai Patel National Police Academy – Hyderabad (asked in 2025).", k="not")
add(D, "A Captain in the Indian Navy is equal in rank to a ____ in the Indian Army.",
    ["Colonel", "Captain", "Major", "Brigadier"],
    "A Navy Captain is much senior to an Army Captain. Equal ranks (Army / Navy / Air Force): Major / Lt Commander / Squadron Leader (asked in 2021); Lt Colonel / Commander / Wing Commander; Colonel / Captain / Group Captain; Brigadier / Commodore / Air Commodore; Major General / Rear Admiral / Air Vice Marshal; General / Admiral / Air Chief Marshal.")
add(D, "Which is India's highest gallantry award given in peacetime?",
    ["Ashoka Chakra", "Param Vir Chakra", "Kirti Chakra", "Maha Vir Chakra"],
    "Peacetime: Ashoka Chakra → Kirti Chakra → Shaurya Chakra. Wartime: Param Vir Chakra → Maha Vir Chakra → Vir Chakra. The 2021 paper asked the only Air Force officer with the Param Vir Chakra (Flying Officer Nirmal Jit Singh Sekhon, 1971). The first Param Vir Chakra went to Major Somnath Sharma (1947).")
add(D, "Match List I (Operation) with List II (Purpose):\nList I: a. Operation Brahma  b. Operation Sindhu  c. Operation Sagar Bandhu  d. Operation Sindoor\nList II: 1. Bringing Indians home from Iran  2. Strikes on terror camps after the Pahalgam attack  3. Earthquake relief to Myanmar  4. Cyclone relief to Sri Lanka",
    [M(3, 1, 4, 2), M(3, 4, 1, 2), M(1, 3, 4, 2), M(4, 1, 3, 2)],
    "All four are from 2025. Brahma: help to Myanmar after the March earthquake. Sindoor: 7 May, after the Pahalgam attack of 22 April. Sindhu: June, evacuation from Iran. Sagar Bandhu: help to Sri Lanka after Cyclone Ditwah. The 2025 paper asked three operation names (Jindagi, Keller, Olivia). From 2026 learn Operation Urja Suraksha, in which the Navy escorted oil and gas ships during the Strait of Hormuz crisis.",
    k="match", n=True)

# -------------------------------------------------------------- ENVIRONMENT (9)
E = "Environment"
add(E, "The '10 per cent law' of energy transfer from one trophic level to the next was given by:",
    ["Raymond Lindeman", "Eugene Odum", "Charles Elton", "A. G. Tansley"],
    "Lindeman (1942) said only about 10% of the energy passes to the next level; the rest is lost as heat. That is why the pyramid of energy is always upright. Tansley coined 'ecosystem' (1935), Elton gave the pyramid of numbers, and Ernst Haeckel coined 'ecology'. Ecology terms came in every paper: plankton (2018), hemiparasites and assimilation efficiency (2021), edge species and endemic species (2025).")
add(E, "The change in the kinds of species from one habitat or community to another is called:",
    ["Beta diversity", "Alpha diversity", "Gamma diversity", "Genetic diversity"],
    "Alpha = diversity inside one community. Beta = change between communities. Gamma = total diversity of the whole region (asked in 2021). R. H. Whittaker gave these three terms. An ecotone is the zone where two communities meet, and species found mostly there are edge species (asked in 2025).")
add(E, "The Stockholm Convention (2001) deals with:",
    ["persistent organic pollutants", "mercury", "movement of hazardous waste across borders", "trade in endangered species"],
    "Persistent organic pollutants (POPs) are poisons such as DDT that stay in nature for years. Minamata Convention – mercury (asked in 2021). Basel – hazardous waste. Rotterdam – prior consent for trade in dangerous chemicals. CITES – trade in endangered species. Montreal Protocol – ozone. Do not confuse it with the Stockholm Conference of 1972, the first UN meeting on the environment.")
add(E, "The United Nations Framework Convention on Climate Change (UNFCCC) was opened for signature at the:",
    ["Rio Earth Summit, 1992", "Stockholm Conference, 1972", "Kyoto Conference, 1997", "Paris Conference, 2015"],
    "The Rio Earth Summit also gave the Convention on Biological Diversity and Agenda 21. The idea of 'common but differentiated responsibilities' (asked in 2021) comes from it. The Kyoto Protocol was adopted on 11 December 1997 (asked in 2025) and came into force in 2005. The Paris Agreement came at COP21 in 2015. COP30 was at Belém, Brazil (2025) and COP31 at Antalya, Türkiye (2026).")
add(E, "Consider the following statements about the India State of Forest Report (ISFR) 2023:\n1. Madhya Pradesh has the largest forest cover in area.\n2. Odisha is among the top four States in the increase of forest and tree cover.\nWhich of the statements given above is/are correct?",
    S12,
    "By area: Madhya Pradesh, then Arunachal Pradesh, then Chhattisgarh. By share of its own area: Lakshadweep is first, and Mizoram is first among the States. The top four in increase of forest and tree cover are Chhattisgarh, Uttar Pradesh, Odisha and Rajasthan (asked in 2025). India's forest and tree cover is 25.17% of its area. The Forest Survey of India, Dehradun brings out the report every two years.",
    k="stmt", a=2)
add(E, "Match List I (Protected area) with List II (Animal it is best known for):\nList I: a. Keibul Lamjao  b. Dachigam  c. Gir  d. Kaziranga\nList II: 1. Asiatic lion  2. One-horned rhinoceros  3. Sangai (brow-antlered deer)  4. Hangul (Kashmir stag)",
    [M(3, 4, 1, 2), M(4, 3, 1, 2), M(3, 4, 2, 1), M(3, 1, 4, 2)],
    "Keibul Lamjao in Manipur floats on Loktak Lake and is the only home of the Sangai. Dachigam is near Srinagar. Gir in Gujarat has all the Asiatic lions (891 in the 2025 count). Kaziranga in Assam has the one-horned rhino. The 2018 paper asked about Manas in Assam. In Odisha: Bhitarkanika – saltwater crocodile; Chilika – Irrawaddy dolphin; Similipal – black (melanistic) tigers.", k="match")
add(E, "Which became India's 58th tiger reserve in March 2025?",
    ["Madhav, Madhya Pradesh", "Ratapani, Madhya Pradesh", "Guru Ghasidas–Tamor Pingla, Chhattisgarh", "Similipal, Odisha"],
    "56th: Guru Ghasidas–Tamor Pingla. 57th: Ratapani. 58th: Madhav, which gave Madhya Pradesh nine tiger reserves, the most of any State. Project Tiger began in 1973. The 2022 count found 3,682 tigers, and the next count is due in 2027. Odisha has two tiger reserves: Similipal and Satkosia.",
    n=True)
add(E, "The Central Pollution Control Board (CPCB) was set up in 1974 under the:",
    ["Water (Prevention and Control of Pollution) Act, 1974", "Air (Prevention and Control of Pollution) Act, 1981", "Environment (Protection) Act, 1986", "Wild Life (Protection) Act, 1972"],
    "The CPCB was born under the Water Act and got its air duties later, under the Air Act of 1981. Asked before: it measures pollutants twice a week under the National Air Quality Monitoring Programme (2021) and made the Comprehensive Environmental Pollution Index with IIT Delhi (2025). The Environment (Protection) Act of 1986 came after the Bhopal gas leak. The National Green Tribunal was set up in 2010.")
add(E, "To be called a 'biodiversity hotspot', a region must have at least 1,500 endemic species of vascular plants and must have lost at least ____ of its original vegetation.",
    ["70%", "30%", "50%", "90%"],
    "Norman Myers gave the hotspot idea in 1988 (asked in 2021). 'Endemic' means found only in that region (asked in 2025). There are 36 hotspots in the world. Four touch India: the Himalaya, Indo-Burma, the Western Ghats and Sri Lanka, and Sundaland (the Nicobar Islands).")

# ------------------------------------------------------------------ ECONOMY (8)
EC = "Economy"
add(EC, "Effective Revenue Deficit is equal to the revenue deficit minus:",
    ["grants given to States for creating capital assets", "interest payments", "capital expenditure", "market borrowings"],
    "The 2025 paper asked which term is not a real deficit ('Monetary Deficit'), with Effective Revenue Deficit as an option. Revenue deficit = revenue spending − revenue receipts. Fiscal deficit = total spending − total receipts other than borrowings. Primary deficit = fiscal deficit − interest payments. Budget 2026-27 targets a fiscal deficit of 4.3% of GDP.")
add(EC, "Match List I (Committee) with List II (Subject):\nList I: a. Narasimham Committee  b. Malhotra Committee  c. Tendulkar Committee  d. Urjit Patel Committee\nList II: 1. Poverty line  2. Inflation targeting and monetary policy  3. Banking sector reforms  4. Insurance sector reforms",
    [M(3, 4, 1, 2), M(4, 3, 1, 2), M(3, 4, 2, 1), M(3, 1, 4, 2)],
    "The 2025 paper asked the Pherwani Committee (National Stock Exchange), with Narasimham, Rangarajan and Abid Hussain as the other options. Rangarajan also worked on the poverty line (2014) and on disinvestment. Abid Hussain: small industries. Kelkar and Chelliah: tax reforms. N. K. Singh: review of the FRBM law.", k="match")
add(EC, "The National Multidimensional Poverty Index of NITI Aayog measures poverty in three dimensions using how many indicators?",
    ["12", "10", "8", "17"],
    "The global index of the UNDP and Oxford uses 10 indicators. India's index adds two more, maternal health and a bank account, to make 12. The three dimensions are health, education and standard of living, each with equal weight. The data comes from the National Family Health Survey (asked in 2025). NITI Aayog is in charge of measuring poverty (asked in 2021).")
add(EC, "Consider the following statements:\n1. The RBI's inflation target is 4 per cent, with a band of 2 per cent on either side.\n2. This target is measured by the Wholesale Price Index (WPI).\nWhich of the statements given above is/are correct?",
    S12,
    "The target uses the Consumer Price Index (CPI-Combined), brought out by the National Statistics Office. The WPI comes from the Office of the Economic Adviser in the commerce ministry. The Government fixes the target after talking to the RBI, and the six-member Monetary Policy Committee sets the repo rate to meet it. Inflation is named in the syllabus. The CPI got a new base year, 2024, in 2026.",
    k="stmt", a=0)
add(EC, "The 'People's Plan' (1945) for the economic development of India was prepared by:",
    ["M. N. Roy", "Shriman Narayan Agarwal", "Jayaprakash Narayan", "a group of industrialists led by J. R. D. Tata and G. D. Birla"],
    "Bombay Plan (1944): eight industrialists. Gandhian Plan (1944): Shriman Narayan Agarwal. People's Plan (1945): M. N. Roy. Sarvodaya Plan (1950): Jayaprakash Narayan. The Planning Commission was set up on 15 March 1950. The Rolling Plan has been asked three times (2018, 2021, 2025): the Janata government of Morarji Desai used it in 1978–80, the idea came from Gunnar Myrdal, and it was not part of any Five Year Plan.")
add(EC, "The Viksit Bharat – Guarantee for Rozgar and Ajeevika Mission (Gramin) Act, which replaced MGNREGA, promises a rural household how many days of wage work in a year?",
    ["125 days", "100 days", "150 days", "200 days"],
    "Parliament passed the new law (short name VB–G RAM G) in December 2025. MGNREGA, passed in 2005, had promised 100 days. Employment and poverty alleviation are named in the syllabus, so learn this change well.",
    n=True)
add(EC, "The 16th Finance Commission, whose award covers 2026–31, kept the States' share in the divisible pool of central taxes at:",
    ["41%", "42%", "32%", "50%"],
    "The 14th Commission gave 42%. The 15th cut it to 41% after Jammu and Kashmir became a Union Territory, and the 16th (chairman Arvind Panagariya) kept 41%. The Finance Commission is set up by the President under Article 280 every five years and has a chairman and four other members (asked in 2021). Budget 2026-27 was the first under the 16th Commission.",
    n=True)
add(EC, "The new series of India's GDP, released in February 2026, uses which base year?",
    ["2022-23", "2011-12", "2017-18", "2024-25"],
    "The base year is the year whose prices are used to compare other years. It moved from 2011-12 to 2022-23. The National Statistics Office under the Ministry of Statistics brings out the GDP numbers. The services sector gives the largest share of GDP (asked in 2025).",
    n=True)

# --------------------------------------------------------------- GOVERNANCE (7)
G = "Governance"
add(G, "Which of the following is NOT one of the three modules of the 'Sevottam' model?",
    ["Performance-linked pay for employees", "Citizen's Charter", "Public Grievance Redress", "Service Delivery Capability"],
    "Sevottam (Seva + Uttam, 'excellent service') is a quality management system for public services (asked in 2025). The Department of Administrative Reforms and Public Grievances made it in 2006. Its three parts are a Citizen's Charter, a grievance redress system and the capability to deliver services. The Citizen's Charter idea came from the United Kingdom (1991) and India adopted it in 1997.", k="not")
add(G, "Match List I (Committee) with List II (What it is known for):\nList I: a. Balwant Rai Mehta Committee  b. Ashok Mehta Committee  c. G. V. K. Rao Committee  d. L. M. Singhvi Committee\nList II: 1. Constitutional status for Panchayats  2. Three-tier Panchayati Raj  3. Two-tier Panchayati Raj  4. Called Panchayati Raj 'grass without roots'",
    [M(2, 3, 4, 1), M(3, 2, 4, 1), M(2, 3, 1, 4), M(2, 4, 3, 1)],
    "Balwant Rai Mehta (1957): three tiers; Rajasthan was the first State to start, at Nagaur in 1959. Ashok Mehta (1977): two tiers. G. V. K. Rao (1985): the district as the main unit of planning. L. M. Singhvi (1986): constitutional status, which came with the 73rd Amendment (1992). The 2025 paper named the 'B. R. Mehta Committee' as the one not linked to the civil services.", k="match")
add(G, "Arrange the following in the order in which they were set up (earliest first):\n1. Lee Commission\n2. Aitchison Commission\n3. Macaulay Committee\n4. Islington Commission",
    ["3, 2, 4, 1", "2, 3, 4, 1", "3, 2, 1, 4", "3, 4, 2, 1"],
    "Macaulay Committee 1854 (open exam) → Aitchison Commission 1886 (Imperial, Provincial and Subordinate services) → Islington Commission 1912 → Lee Commission 1923. The Lee Commission is the 'Royal Commission on Superior Civil Services' (asked in 2025); on its advice the first Public Service Commission was set up in 1926. After independence: Kothari (1976), Satish Chandra (1989), Alagh (2001), Hota (2004).", k="order")
add(G, "Which of the following statements about the Lal Bahadur Shastri National Academy of Administration (LBSNAA) is NOT correct?",
    ["It works under the Ministry of Home Affairs", "It is located at Mussoorie in Uttarakhand", "It trains officers of the Indian Administrative Service", "It was set up in 1959"],
    "LBSNAA is under the Department of Personnel and Training. The 2025 paper asked this same style on the Sardar Vallabhbhai Patel National Police Academy (Hyderabad, set up in 1948, under the Home Ministry). Also asked in 2025: Indian Institute of Public Administration, New Delhi (1954) and NIRDPR, Hyderabad. Odisha's own training centre is the Gopabandhu Academy of Administration, Bhubaneswar.", k="not")
add(G, "Consider the following statements about the Lokpal:\n1. It has a Chairperson and not more than eight Members.\n2. Half of the Members must be judicial Members.\n3. The Prime Minister is fully outside its jurisdiction.\nWhich of the statements given above are correct?",
    ["Only 1 and 2", "Only 2 and 3", "Only 1 and 3", "1, 2 and 3"],
    "The Prime Minister is covered, but not on matters of foreign relations, security, public order, atomic energy and space. The Lokpal and Lokayuktas Act was passed in 2013 and came into force in January 2014. The first Chairperson was Justice Pinaki Chandra Ghose (2019); the present one is Justice A. M. Khanwilkar. Corruption bodies keep coming: the Santhanam Committee was asked in 2021 and 2025.",
    k="stmt", a=0)
add(G, "CPGRAMS, run by the Department of Administrative Reforms and Public Grievances, is an online system for:",
    ["lodging and tracking public grievances", "filing RTI applications", "buying goods and services for government offices", "training civil servants online"],
    "CPGRAMS is the Centralised Public Grievance Redress and Monitoring System. RTI applications go to the RTI Online portal. Government buying is done on GeM. Online training is on iGOT Karmayogi. E-governance is named in the syllabus and was asked in 2018. Others: UMANG (many services in one app), DigiLocker (documents), PRAGATI (the Prime Minister's review of projects).")
add(G, "Which Article of the Constitution says that a civil servant cannot be dismissed by an authority lower than the one that appointed him, and not without an inquiry?",
    ["Article 311", "Article 309", "Article 312", "Article 323A"],
    "Article 309: rules of recruitment and service. Article 310: civil servants hold office during the pleasure of the President or Governor. Article 311: the two safeguards against that pleasure. Article 312: All India Services, created by Parliament after a Rajya Sabha resolution (asked in 2021 and 2025). Article 315: Public Service Commissions. Article 323A: administrative tribunals.")

# ------------------------------------------------------------------- ODISHA (7)
O = "Odisha"
add(O, "The coastal plain of Odisha is called the 'Hexadeltaic region' because it is built by the deltas of six rivers. Which of the following is NOT one of the six?",
    ["Indravati", "Subarnarekha", "Budhabalanga", "Rushikulya"],
    "The six, from north to south: Subarnarekha, Budhabalanga, Baitarani, Brahmani, Mahanadi and Rushikulya. The 2025 paper asked why the region has this name. The Indravati flows the other way, through Kalahandi, Nabarangpur and Koraput into the Godavari. The 2021 paper asked which rivers add most to the coastal plain.", k="not")
add(O, "The Brahmani river is formed by the meeting of which two rivers at Vedavyas near Rourkela?",
    ["Sankh and Koel", "Ib and Tel", "Sabari and Sileru", "Ong and Jira"],
    "The Sankh and the South Koel come down from the Chota Nagpur plateau and join at Vedavyas. The 2021 paper matched the Rajgangpur–Panposh uplands with these two rivers. The Rengali Dam is on the Brahmani. Ib, Tel, Ong and Jira are tributaries of the Mahanadi. Sabari and Sileru in Malkangiri flow to the Godavari. Baitarani rises at Gonasika in Keonjhar; Rushikulya rises in the Rushimala hills and has no delta.")
add(O, "Match List I (Peak) with List II (District):\nList I: a. Mahendragiri  b. Malayagiri  c. Meghasani  d. Gandhamardan\nList II: 1. Mayurbhanj  2. Bargarh–Balangir border  3. Gajapati  4. Angul",
    [M(3, 4, 1, 2), M(4, 3, 1, 2), M(3, 4, 2, 1), M(3, 1, 4, 2)],
    "The 2025 paper asked for these hills in north-to-south order, so the districts are the next step. Meghasani is in the Similipal hills. Malayagiri is near Pallahara. Gandhamardan has bauxite and the Nrusinghanath and Harishankar temples. Mahendragiri is in the Eastern Ghats. Deomali in Koraput (1,672 m) is the highest peak of Odisha.", k="match")
add(O, "Panchpatmali in Koraput district, mined by NALCO, has one of the largest deposits of:",
    ["bauxite", "chromite", "iron ore", "manganese"],
    "Bauxite is the ore of aluminium; NALCO's refinery is at Damanjodi. The 2025 paper matched places with minerals (Baula-Nuasahi – chromite; Chhatrapur – monazite). Others: Sukinda in Jajpur – chromite; Joda–Barbil in Keonjhar and Gorumahisani in Mayurbhanj – iron ore; Talcher and Ib valley – coal; Gandhamardan – bauxite.")
add(O, "Who led the long fight against the British in the Sambalpur region during and after the Revolt of 1857?",
    ["Veer Surendra Sai", "Buxi Jagabandhu", "Chakhi Khuntia", "Laxman Naik"],
    "Surendra Sai fought on until 1862 and died in Asirgarh fort in 1884. Buxi Jagabandhu led the Paika Rebellion of 1817. Chakhi Khuntia, a priest of Puri, helped the rebels of 1857. Laxman Naik of Koraput was hanged in 1943 for the Quit India Movement. The 2018 paper asked two Odisha history questions (the British conquest of 1803 and Gandhi at Cuttack in 1921), and the 1857 revolt was asked in 2018 and 2025.")
add(O, "The great Odisha famine of 1866, in which about one-third of the people of the coastal districts died, is known as the:",
    ["Na'anka famine", "Chalisa famine", "Doji Bara famine", "Chhappania famine"],
    "'Na'anka' means the ninth regnal year of the Gajapati king of Puri. T. E. Ravenshaw was the Commissioner. The famine woke up Odia public life: Utkal Dipika started the same year, and the demand for a separate Odia province grew from it. Chalisa (1783) was in north India, Doji Bara (1791) in the Deccan and Chhappania (1899) in Rajasthan.")
add(O, "Which became Odisha's second national park in April 2025?",
    ["Similipal", "Bhitarkanika", "Satkosia", "Chandaka"],
    "Similipal in Mayurbhanj became India's 107th national park, with about 846 sq km. Bhitarkanika (1998) was Odisha's first. Similipal is also a tiger reserve and a UNESCO biosphere reserve, and is known for black tigers. Olive ridley turtles were asked in 2018 and 2025: in 2026 Rushikulya had mass nesting but Gahirmatha did not.",
    n=True)

# ---------------------------------------------------------- WORLD GEOGRAPHY (6)
W = "World Geography"
add(W, "Which river crosses the Tropic of Capricorn twice?",
    ["Limpopo", "Congo", "Zambezi", "Orange"],
    "The Limpopo of southern Africa bends north and then south-east, cutting the Tropic of Capricorn twice. The Congo crosses the Equator twice (asked in 2025). In India the Mahi crosses the Tropic of Cancer twice. The Nile is the longest river and the Amazon carries the most water.")
add(W, "Arrange the layers of the atmosphere from the Earth's surface upward:\n1. Stratosphere\n2. Thermosphere\n3. Troposphere\n4. Mesosphere",
    ["3, 1, 4, 2", "3, 4, 1, 2", "1, 3, 4, 2", "3, 1, 2, 4"],
    "Troposphere (weather) → Stratosphere (ozone layer; jets fly here) → Mesosphere (coldest; meteors burn up) → Thermosphere (holds the ionosphere, which reflects radio waves) → Exosphere. The gases of the atmosphere were asked in 2018 (nitrogen is the largest) and 2025 (nitrogen 78%, oxygen 21%).", k="order")
add(W, "The boundary between the Earth's crust and the mantle is called the:",
    ["Mohorovičić (Moho) discontinuity", "Gutenberg discontinuity", "Lehmann discontinuity", "Conrad discontinuity"],
    "Conrad: between the upper and lower crust. Moho: crust and mantle. Gutenberg: mantle and outer core. Lehmann: outer core and inner core. The 2018 paper asked about earthquakes: the focus is the point underground where it starts, and the epicentre is the point on the surface just above it. P waves pass through solids and liquids; S waves pass only through solids.")
add(W, "The rich fishing ground of the Grand Banks, off Newfoundland, lies where which two ocean currents meet?",
    ["Gulf Stream and Labrador Current", "Kuroshio and Oyashio", "Brazil and Falkland Currents", "Benguela and Agulhas Currents"],
    "Where a warm current meets a cold one, fog forms and plankton grows, so fish gather. The warm Gulf Stream meets the cold Labrador Current at the Grand Banks. The warm Kuroshio meets the cold Oyashio off Japan. The 2021 paper asked which current is in the southern hemisphere (West Wind Drift).")
add(W, "Which warm, dry wind of the Rocky Mountains is called the 'Snow Eater'?",
    ["Chinook", "Foehn", "Sirocco", "Mistral"],
    "The Chinook blows down the eastern side of the Rockies and melts snow quickly. The Foehn is the same kind of wind in the Alps. The Sirocco is a hot wind from the Sahara to southern Europe. The Mistral is a cold wind in France, Bora blows on the Adriatic coast and Khamsin in Egypt (all three were in the 2021 question). Loo is the hot summer wind of north India.")
add(W, "Match List I (Landform) with List II (Agent that makes it):\nList I: a. Moraine  b. Barchan  c. Stalactite  d. Oxbow lake\nList II: 1. River  2. Wind  3. Glacier  4. Underground water",
    [M(3, 2, 4, 1), M(2, 3, 4, 1), M(3, 2, 1, 4), M(3, 4, 2, 1)],
    "Glacier: moraine, cirque, drumlin, U-shaped valley. Wind: barchan (a crescent sand dune), mushroom rock, loess. Underground water in limestone: stalactite (hangs from the roof), stalagmite (grows from the floor), sinkhole. River: meander, oxbow lake, delta, V-shaped valley. The 2021 paper asked the bird-foot delta (Mississippi) and types of mountains.", k="match")

# ---------------------------------------------------------- INDIA GEOGRAPHY (5)
I = "India Geography"
add(I, "Match List I (Pass) with List II (State or Union Territory):\nList I: a. Zoji La  b. Rohtang  c. Lipulekh  d. Bomdi La\nList II: 1. Uttarakhand  2. Arunachal Pradesh  3. Ladakh  4. Himachal Pradesh",
    [M(3, 4, 1, 2), M(4, 3, 1, 2), M(3, 4, 2, 1), M(3, 1, 4, 2)],
    "Zoji La is on the Srinagar–Leh road. Rohtang links Kullu with Lahaul and Spiti. Lipulekh is on the way to Kailash Mansarovar. Bomdi La is in western Arunachal, near the Sela Tunnel (asked in 2021). The 2021 paper asked a wrong pair: Jelep La is in Sikkim, like Nathu La. Shipki La and Bara Lacha La are in Himachal; Mana and Niti are in Uttarakhand.", k="match")
add(I, "Which of the following States does NOT share a border with Myanmar?",
    ["Tripura", "Mizoram", "Manipur", "Nagaland"],
    "Four States touch Myanmar: Arunachal Pradesh, Nagaland, Manipur and Mizoram. Tripura has Bangladesh on three sides. The 2025 paper matched States with neighbour countries. Sikkim touches three countries (China, Nepal, Bhutan) and so does West Bengal (Bangladesh, Nepal, Bhutan). India's longest land border is with Bangladesh.", k="not")
add(I, "The river Kaveri rises at Talakaveri in the:",
    ["Brahmagiri hills of Kodagu, Karnataka", "Nilgiri hills of Tamil Nadu", "Mahabaleshwar hills of Maharashtra", "Amarkantak plateau of Madhya Pradesh"],
    "Krishna rises at Mahabaleshwar and Godavari at Trimbak near Nashik. Narmada and Son rise at Amarkantak in the Maikal range; Tapi does not, it rises at Multai (asked in 2021). Mahanadi rises at Sihawa in Chhattisgarh. Kaveri is the longest river of Tamil Nadu (used in a 2018 statement).")
add(I, "Consider the following statements:\n1. In a positive Indian Ocean Dipole, the western Indian Ocean is warmer than the eastern part.\n2. A positive Indian Ocean Dipole usually weakens the Indian monsoon.\nWhich of the statements given above is/are correct?",
    S12,
    "A positive dipole usually helps the monsoon; a negative one hurts it. The Indian Ocean Dipole is also called the 'Indian Niño' and works like El Niño (asked in 2025). El Niño is the warming of the Pacific off Peru and usually means a weak monsoon in India. La Niña is the cooling of the same waters and usually means good rain.",
    k="stmt", a=0)
add(I, "The Western Ghats and the Eastern Ghats meet at the:",
    ["Nilgiri hills", "Cardamom hills", "Anamalai hills", "Shevaroy hills"],
    "The same four hills were the options in 2025, when the answer was the Cardamom hills (closest to Kanyakumari). Doddabetta is the highest peak of the Nilgiris. The Palghat Gap lies between the Nilgiris and the Anamalai hills. Anamudi in the Anamalai hills is the highest peak of south India. The Shevaroy hills are in the Eastern Ghats of Tamil Nadu.")

# ------------------------------------------------------------- INSTITUTIONS (7)
N = "Institutions"
add(N, "Which of the following countries was elected in June 2026 as a non-permanent member of the UN Security Council for 2027–28?",
    ["Kyrgyzstan", "Germany", "Philippines", "Pakistan"],
    "The 2021 paper asked this same question for the June 2022 election. The five new members for 2027–28 are Austria, Kyrgyzstan, Portugal, Trinidad and Tobago, and Zimbabwe. Kyrgyzstan beat the Philippines and won a seat for the first time; Germany lost. Pakistan's term ends in December 2026. There are 10 non-permanent members, five are elected each year, and the term is two years (asked in 2021).",
    n=True)
add(N, "Consider the following statements about BRICS:\n1. India chaired BRICS in 2026 and hosted its 18th summit.\n2. The New Development Bank of BRICS has its headquarters in New Delhi.\n3. Indonesia became a full member in January 2025.\nWhich of the statements given above are correct?",
    ["Only 1 and 2", "Only 2 and 3", "Only 1 and 3", "1, 2 and 3"],
    "The New Development Bank is in Shanghai. The 18th summit was held in New Delhi in September 2026 and ended with the New Delhi Declaration. The 17th summit was at Rio de Janeiro in 2025. The first five members were Brazil, Russia, India, China and South Africa; Egypt, Ethiopia, Iran and the UAE joined in 2024. The 2021 and 2025 papers asked the hosts of SCO and BIMSTEC meetings.",
    k="stmt", n=True, a=2)
add(N, "Which country hosted the 2026 summit of the Shanghai Cooperation Organisation (SCO), held in the group's 25th year?",
    ["Kyrgyzstan", "China", "Kazakhstan", "Russia"],
    "The summit was at Bishkek. The 2025 summit was at Tianjin, China. The SCO was founded at Shanghai in 2001, its secretariat is in Beijing and its anti-terror body (RATS) is at Tashkent. India and Pakistan joined in 2017, Iran in 2023 and Belarus in 2024. The 2021 paper asked who hosted the 20th SCO meeting.",
    n=True)
add(N, "The headquarters of the International Maritime Organization (IMO) is in:",
    ["London", "Geneva", "Hamburg", "New York"],
    "The IMO is the only UN specialised agency based in the United Kingdom. Geneva: WHO, ILO, WTO, WMO (the 2025 paper gave 'Vienna' as a false statement for WMO). Vienna: IAEA, UNIDO. Rome: FAO. Paris: UNESCO. Bern: Universal Postal Union. Montreal: ICAO. Nairobi: UNEP. Gurugram: International Solar Alliance (asked in 2021). Brussels: NATO (asked in 2021).")
add(N, "Match List I (Report) with List II (Publisher):\nList I: a. Emissions Gap Report  b. World Investment Report  c. Global Innovation Index  d. Human Development Report\nList II: 1. UNDP  2. WIPO  3. UNEP  4. UNCTAD",
    [M(3, 4, 2, 1), M(4, 3, 2, 1), M(3, 4, 1, 2), M(3, 2, 4, 1)],
    "The 2021 paper asked who publishes 'South Asia Economic Focus' (World Bank) and the World Giving Index (Charities Aid Foundation). More: World Economic Outlook – IMF; Global Gender Gap – World Economic Forum; Global Hunger Index – Concern Worldwide and Welthungerhilfe; World Press Freedom Index – Reporters Without Borders; Global Peace Index – Institute for Economics and Peace. In 2026 India was 38th in the Global Innovation Index.", k="match")
add(N, "The Secretary-General of the United Nations is appointed by the:",
    ["General Assembly, on the recommendation of the Security Council", "Security Council alone", "International Court of Justice", "General Assembly, on the recommendation of the Economic and Social Council"],
    "This is likely because António Guterres's second term ends on 31 December 2026 and a new Secretary-General starts on 1 January 2027. Learn the new name before the exam. The term is five years. Any permanent member can veto a name in the Security Council. The UN was founded on 24 October 1945 and has 193 members.")
add(N, "Which country holds the presidency of the G20 in 2026?",
    ["United States", "South Africa", "Brazil", "United Kingdom"],
    "India (New Delhi, 2023) → Brazil (Rio de Janeiro, 2024) → South Africa (Johannesburg, 2025, the first summit in Africa) → United States (2026). The African Union became a member at the New Delhi summit. The G20 has no permanent secretariat; a 'troika' of the past, present and next presidents runs it.",
    n=True)

# ----------------------------------------------------------- SCIENCE & TECH (5)
SC = "Science & Tech"
add(SC, "Cholera is a:",
    ["waterborne bacterial disease", "waterborne viral disease", "airborne bacterial disease", "airborne viral disease"],
    "The 2025 paper asked the same thing about mumps (an airborne viral disease). Cholera is caused by the bacterium Vibrio cholerae and spreads through dirty water. Bacteria: cholera, typhoid, tuberculosis (airborne), plague. Virus: mumps, measles, polio, dengue, hepatitis, rabies. Protozoa: malaria, kala-azar. Fungus: ringworm.")
add(SC, "ISRO's PSLV-C62 mission failed on 12 January 2026 after a problem in its third stage. Which main satellite was lost?",
    ["EOS-N1 (Anvesha)", "EOS-09", "NISAR", "CMS-03"],
    "EOS-N1 'Anvesha' was a DRDO satellite for watching the seas. It was the PSLV's second failure in a row: PSLV-C61 with EOS-09 failed in May 2025, and the 2025 paper asked the orbit meant for EOS-09 (Sun-synchronous polar orbit). NISAR, the NASA–ISRO radar satellite, went up on a GSLV in July 2025.",
    n=True)
add(SC, "Consider the following statements about the Artemis II mission:\n1. It was a crewed NASA mission that flew around the Moon in April 2026.\n2. Its astronauts landed near the Moon's south pole.\nWhich of the statements given above is/are correct?",
    S12,
    "Artemis II did not land. Four astronauts (three Americans and Jeremy Hansen of Canada) flew around the Moon in the Orion capsule, launched on the SLS rocket. It was the first crewed trip to the Moon since Apollo 17 in 1972. The 2021 paper had a statement question on China's Chang'e-5 Moon mission, and the 2025 paper asked about SpaceX.",
    k="stmt", n=True, a=0)
add(SC, "Galvanisation protects iron from rusting by coating it with a thin layer of:",
    ["zinc", "tin", "copper", "chromium"],
    "'Use of science in everyday life' is in the syllabus; the 2018 paper asked what non-stick pans are coated with (Teflon). Food cans are coated with tin. Stainless steel is iron with chromium and nickel. LPG gets its smell from ethyl mercaptan. Dry ice is solid carbon dioxide. Vinegar is acetic acid. Baking soda is sodium bicarbonate.")
add(SC, "The Nobel Prize in Chemistry 2025 was given to Susumu Kitagawa, Richard Robson and Omar Yaghi for developing:",
    ["metal–organic frameworks", "lithium-ion batteries", "CRISPR gene editing", "quantum dots"],
    "Metal–organic frameworks are crystals full of tiny holes that can trap gases or pull water from desert air. The 2021 paper asked the 2019 Chemistry prize (lithium-ion batteries), so an older year can come too. 2020: CRISPR gene editing. 2023: quantum dots. 2024: protein design. The Nobel Peace Prize 2025 went to María Corina Machado of Venezuela.",
    n=True)

# ------------------------------------------------------------ GENERAL NEWS (7)
GN = "General News"
add(GN, "The United Nations has declared 2026 as the International Year of:",
    ["the Woman Farmer", "Millets", "Cooperatives", "Quantum Science and Technology"],
    "2026 is the International Year of the Woman Farmer, and also of Rangelands and Pastoralists. 2025 was the year of Cooperatives, of Quantum Science and Technology, and of Glaciers' Preservation. 2023 was the year of Millets, on India's proposal.",
    n=True)
add(GN, "What was the theme of World Water Day 2026 (22 March)?",
    ["Water and Gender", "Glacier Preservation", "Water for Peace", "Accelerating Change"],
    "2023: Accelerating Change. 2024: Water for Peace. 2025: Glacier Preservation. 2026: Water and Gender. The 2025 paper asked the date of World Water Day, and themes of days come every year (Earth Day in 2018, 2021 and 2025; World TB Day and National Voters' Day in 2025). Note that the 2025 paper asked the Earth Day theme of the year before, so learn two years of themes.",
    n=True)
add(GN, "Match List I (State) with List II (Chief Minister who took office after the Assembly elections of 2026):\nList I: a. West Bengal  b. Tamil Nadu  c. Kerala  d. Assam\nList II: 1. V. D. Satheesan  2. Himanta Biswa Sarma  3. Suvendu Adhikari  4. Vijay",
    [M(3, 4, 1, 2), M(4, 3, 1, 2), M(3, 4, 2, 1), M(3, 1, 4, 2)],
    "The results came on 4 May 2026. West Bengal got its first BJP government under Suvendu Adhikari. In Tamil Nadu the actor Vijay's party, TVK, won. In Kerala the Congress-led UDF came back under V. D. Satheesan. In Assam Himanta Biswa Sarma won a second term. Odisha's Chief Minister is Mohan Charan Majhi (since June 2024).",
    k="match", n=True)
add(GN, "Which site became India's 45th UNESCO World Heritage Site in July 2026?",
    ["Ancient Buddhist Site of Sarnath", "Maratha Military Landscapes", "Moidams of the Ahom Dynasty", "Santiniketan"],
    "Sarnath, near Varanasi, is where the Buddha gave his first sermon. It was added at the Busan session. 44th: Maratha Military Landscapes (2025). 43rd: Moidams of Assam (2024). Santiniketan and the Hoysala temples came in 2023. Odisha has one World Heritage Site, the Sun Temple at Konark. The 2025 paper asked about UNESCO's Memory of the World Register, which is for documents.",
    n=True)
add(GN, "A year-long celebration of 150 years of 'Vande Mataram' began on 7 November 2025. Who wrote the song?",
    ["Bankim Chandra Chatterjee", "Rabindranath Tagore", "Sarat Chandra Chattopadhyay", "Dwijendralal Roy"],
    "Bankim Chandra wrote it in 1875 and later placed it in his novel Anandamath (1882). Rabindranath Tagore first sang it at the Calcutta session of the Congress in 1896. It was made the National Song on 24 January 1950. Tagore wrote the National Anthem, Jana Gana Mana.",
    n=True)
add(GN, "Which Indian festival was added to UNESCO's Representative List of the Intangible Cultural Heritage of Humanity in December 2025?",
    ["Deepavali", "Holi", "Chhath", "Raja Parba"],
    "It was added at a session held in New Delhi. Earlier Indian entries include Durga Puja of Kolkata (2021) and Garba of Gujarat (2023). Keep three UNESCO lists apart: World Heritage Sites (places), Intangible Cultural Heritage (living traditions) and the Memory of the World Register (documents, asked in 2025).",
    n=True)
add(GN, "Who became the Prime Minister of Bangladesh in February 2026?",
    ["Tarique Rahman", "Muhammad Yunus", "Sheikh Hasina", "Khaleda Zia"],
    "Tarique Rahman of the BNP took office on 17 February 2026 after the election of 12 February. Muhammad Yunus had led the interim government since August 2024, when Sheikh Hasina left the country. In Nepal, Balendra Shah became Prime Minister in March 2026. In Japan, Sanae Takaichi became the first woman Prime Minister in October 2025.",
    n=True)
