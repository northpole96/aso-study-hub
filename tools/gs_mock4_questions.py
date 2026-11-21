# Questions for GS Mock 04. In every item the FIRST option is the right one,
# unless "a" is given (then the options stay in the written order).
# k: one | stmt | match | not | order.  n: needs 2025-26 news.  c: Check tag.
# Every question is a next angle of a family from the 2018, 2021 and 2025 papers,
# and none repeats a question of GS Mock 01, 02, 03, GA Mock 1, the GA Full Test or Defence Mock 01.

S12 = ["Only 1", "Only 2", "Both 1 and 2", "Neither 1 nor 2"]
S3 = ["Only 1 and 2", "Only 2 and 3", "Only 1 and 3", "1, 2 and 3"]
def M(a, b, c, d):  # match answer text
    return "a-%d, b-%d, c-%d, d-%d" % (a, b, c, d)

Q = []
def add(s, q, o, e, k="one", n=False, c=False, a=None):
    Q.append(dict(s=s, q=q, o=o, e=e, k=k, n=n, c=c, a=a))

# ------------------------------------------------------------------ POLITY (17)
P = "Polity"
add(P, "Fundamental Duties are contained in which Part of the Constitution?",
    ["Part IV-A (Article 51A)", "Part IV (Article 36 to 51)", "Part III (Article 12 to 35)", "Part V (Article 52 to 151)"],
    "Part IV-A has only one Article, 51A. It was added by the 42nd Amendment (1976), and the 86th Amendment (2002) added the eleventh duty (a parent's duty to send a child of 6 to 14 to school). Duties can not be enforced by a court. Do not mix this with Part IV, which holds the Directive Principles (asked in 2025: which one was added in 1976). Part III is Fundamental Rights.")
add(P, "Consider the following statements:\n1. The President nominates 12 members to the Rajya Sabha.\n2. The nominated members can vote in the election of the President.\nWhich of the statements given above is/are correct?",
    S12,
    "Statement 1 is correct (Article 80). Statement 2 is wrong: only the elected members of Parliament and of the State Assemblies vote for the President (Article 54). Nominated members can, however, vote in the Vice-President election and in the impeachment of the President. The 2025 paper asked where the nominated-member idea came from (Ireland). Also learn: the 12 come from literature, science, art and social service.",
    k="stmt", a=0)
add(P, "Who described the Prime Minister as the 'keystone of the cabinet arch'?",
    ["Lord Morley", "Sir William Harcourt", "Ivor Jennings", "Harold Laski"],
    "Lord Morley used these words. Sir William Harcourt called the Prime Minister 'the sun around which the planets revolve'. The idea of 'first among equals' (primus inter pares) is also linked to the Prime Minister. The 2025 paper had a four-statement question on the Prime Minister and the Council of Ministers, and Mock 01 asked the 'horoscope' quote for the Preamble, so famous remarks about an office are a live family.")
add(P, "Which of the following is NOT mentioned in the Rules of Procedure of Parliament, but has grown as a practice?",
    ["Zero Hour", "Question Hour", "Adjournment Motion", "Calling Attention Notice"],
    "Zero Hour began in the Lok Sabha in 1962. It is the time just after Question Hour when members raise urgent matters without notice. It is an Indian practice and has no place in the written rules. Question Hour, Adjournment Motion and Calling Attention are all in the rules. The 2025 paper asked what happens to Rajya Sabha amendments to a Money Bill, so how Parliament works is a steady family.", k="not")
add(P, "Which one of the following pairs is NOT correctly matched?",
    ["Tenth Schedule – Powers and duties of Panchayats",
     "Seventh Schedule – Union, State and Concurrent Lists",
     "Ninth Schedule – Laws protected from challenge in court, mainly land reform laws",
     "Eighth Schedule – Languages recognised by the Constitution"],
    "The Tenth Schedule is the anti-defection law (52nd Amendment, 1985). The powers of Panchayats are in the Eleventh Schedule, and those of Municipalities in the Twelfth. The Ninth Schedule was added by the First Amendment (1951) to protect land reform laws. The 2025 paper asked the same 'not matched' style on Schedules (First, Second, Fourth, Fifth). The Fourth Schedule gives the seats of each State in the Rajya Sabha.", k="not")
add(P, "Article 27 says that no person shall be forced to pay any tax:",
    ["for the promotion of any particular religion", "for running a school", "for the upkeep of a temple built by the State", "on income from agriculture"],
    "Article 27 protects the secular character of the State. The 2025 paper asked which Articles cover the Right to Religion (25 to 28). Article 25: freedom to practise and spread religion. Article 26: manage religious affairs. Article 27: no tax for a religion. Article 28: no religious teaching in a school kept wholly by the State. Articles 29 and 30 protect minorities and are in a different group (Cultural and Educational Rights).")
add(P, "Constitution Day (Samvidhan Divas) is observed on 26 November because on that day in 1949:",
    ["the Constituent Assembly adopted the Constitution", "the Constitution came into force", "the Drafting Committee was set up", "Dr B. R. Ambedkar was born"],
    "The Assembly adopted the Constitution on 26 November 1949, and it came into force on 26 January 1950 (Republic Day). The Government began to mark 26 November as Constitution Day in 2015. The Drafting Committee was set up on 29 August 1947. Ambedkar was born on 14 April 1891. Dates and days are a family in every paper: 2025 asked Water Day, Consumer Rights Day, TB Day and Voters' Day.")
add(P, "The Model Code of Conduct for elections comes into force from the date on which:",
    ["the Election Commission announces the election schedule", "a Bill on the election is passed", "the President dissolves the House", "the nominations close"],
    "The Model Code is a set of rules agreed by the political parties and enforced by the Election Commission under its Article 324 powers. It starts the day the schedule is announced and lasts until the results. It has no direct force of law, but the Commission can act against breaches. The 2025 paper asked about Article 324 and the Commission's powers, and Mock 03 asked about its composition.")
add(P, "Which Article of the Directive Principles asks the State to secure a Uniform Civil Code for citizens?",
    ["Article 44", "Article 43", "Article 45", "Article 48"],
    "Article 44 is in Part IV, so it is not enforceable by a court. In 2025 the Uniform Civil Code was a wrong option in the question on the Directive Principle added in 1976 (the right answer was free legal aid, Article 39A); Article 40 (Village Panchayats) and Article 48 (cow slaughter) were the other options. Neighbours: Article 43 – living wage; Article 45 – early childhood care (changed by the 86th Amendment); Article 47 – public health and prohibition; Article 48A – environment (added in 1976).")
add(P, "Which of the following is NOT a member of the Selection Committee for the Chairperson of the Lokpal?",
    ["Home Minister", "Prime Minister", "Speaker of the Lok Sabha", "Leader of the Opposition in the Lok Sabha"],
    "The Lokpal and Lokayuktas Act, 2013 names a five-part committee: the Prime Minister (chair), the Speaker, the Leader of the Opposition in the Lok Sabha, the Chief Justice of India (or a judge named by the CJI) and one eminent jurist. The Home Minister is not in it. The 2025 paper asked who is NOT in the NHRC committee (the Deputy Speaker), so 'who is not in the committee' is the exam's favourite twist.", k="not")
add(P, "Consider the following statements about the impeachment of the President:\n1. The resolution must be passed by a simple majority of the members present.\n2. A notice of 14 days, signed by at least one-fourth of the members of the House, is needed.\n3. Nominated members of the Rajya Sabha can take part in it.\nWhich of the statements given above are correct?",
    S3,
    "Statement 1 is wrong: Article 61 needs a two-thirds majority of the total membership of the House. Statements 2 and 3 are right. The charge can start in either House, the other House then investigates, and the President may appear or be represented. No President has ever been impeached. The 2025 paper asked about the Council of Ministers being collectively responsible to the Lok Sabha, so how offices are held and ended is a live family.",
    k="stmt", a=1)
add(P, "A writ of Mandamus, which means 'we command', is issued by a court to:",
    ["order a public official to do a duty he has failed to do", "free a person who is illegally detained", "stop a lower court from going beyond its power", "ask a person by what authority he holds an office"],
    "Mandamus compels a public authority to perform a legal duty. It cannot be issued against a private person, the President or a Governor. The other three: Habeas Corpus ('have the body') frees the detained, Prohibition stops a lower court, and Quo Warranto ('by what authority') asks about a public office. Mock 01 asked Prohibition and Mock 02 Quo Warranto, so Mandamus and Certiorari ('to be certified') complete the five writs of Article 32.")
add(P, "Match List I (Feature of the Indian Constitution) with List II (Country from which it was borrowed):\nList I: a. Concurrent List  b. Residuary powers with the Centre  c. Ideals of liberty, equality and fraternity  d. Election of Rajya Sabha members\nList II: 1. Canada  2. France  3. Australia  4. South Africa",
    [M(3, 1, 2, 4), M(1, 3, 2, 4), M(3, 1, 4, 2), M(3, 2, 1, 4)],
    "The Concurrent List comes from Australia; a strong Centre and residuary powers from Canada; the ideals of the Preamble from the French Revolution; the way of electing the Rajya Sabha (and the amendment procedure) from South Africa. The 2021 and 2025 papers each asked a 'borrowed from' question (2025: Rajya Sabha nominations from Ireland), and Mock 02 asked the Emergency (Germany). Fundamental Duties come from the USSR.", k="match")
add(P, "Consider the following statements about the State Legislative Council:\n1. Parliament can create or abolish it if the Assembly passes a resolution by a special majority.\n2. Its strength cannot be more than one-third of the Assembly, and not less than 40.\n3. It is a permanent House and is not dissolved.\nWhich of the statements given above are correct?",
    S3,
    "All three are correct (Articles 169 and 171). One-third of the members retire every two years. The 2025 paper asked the minimum age for the Council (30 years), and Mock 02 asked which State has no Council (Odisha). Learn the six States that have one: Andhra Pradesh, Telangana, Bihar, Karnataka, Maharashtra and Uttar Pradesh. A Council has no say in a Money Bill, and the Assembly can override its advice on other Bills.",
    k="stmt", a=3)
add(P, "A member of a State Public Service Commission can be removed from office only by:",
    ["the President, after an inquiry by the Supreme Court", "the Governor, after an inquiry by the High Court", "the Chief Minister, with the Assembly's approval", "the State Legislature, by a simple majority"],
    "A member of the OPSC is appointed by the Governor but removed by the President (Article 317), and only for misbehaviour proved by the Supreme Court, or for reasons like insolvency or taking paid work. The 2025 paper asked who can set up a Joint Commission (an Act of Parliament), and Mock 02 asked the age limit (62 years). The Governor can suspend a member while the inquiry goes on.")
add(P, "In which case did the Supreme Court hold that the 'procedure established by law' in Article 21 must be just, fair and reasonable?",
    ["Maneka Gandhi v. Union of India (1978)", "A. K. Gopalan v. State of Madras (1950)", "Golaknath v. State of Punjab (1967)", "Minerva Mills v. Union of India (1980)"],
    "Maneka Gandhi's passport was impounded, and the Court read Articles 14, 19 and 21 together. Gopalan (1950) had said that any law passed by the legislature was enough. This case opened the way for the rights read into Article 21: privacy (asked in 2018), the right to livelihood, and maternity leave (asked in 2025). Minerva Mills (1980) said that harmony between Fundamental Rights and Directive Principles is part of the basic structure.", n=False)
add(P, "The Right to Property was removed from the list of Fundamental Rights by the:",
    ["44th Amendment Act, 1978", "42nd Amendment Act, 1976", "25th Amendment Act, 1971", "1st Amendment Act, 1951"],
    "The 44th Amendment deleted Articles 19(1)(f) and 31 and put a new Article 300A in Part XII: no person shall be deprived of property except by law. It is now a legal right, not a Fundamental Right. The same Amendment (Mock 01) changed 'internal disturbance' to 'armed rebellion' for an Emergency and added a Directive Principle on reducing inequality. The 1st Amendment (1951) added the Ninth Schedule.")

# ------------------------------------------------------------------ MODERN HISTORY (14)
H = "Modern History"
add(H, "The Hindu Widow Remarriage Act, 1856 was passed mainly through the efforts of:",
    ["Ishwar Chandra Vidyasagar", "Raja Ram Mohan Roy", "Dayanand Saraswati", "Jyotirao Phule"],
    "Vidyasagar, the Bengal reformer, collected thousands of signatures and wrote a book on the subject. The Bill was drafted in Lord Dalhousie's time, and the Act was passed in 1856 under Lord Canning. Raja Ram Mohan Roy worked against sati (banned in 1829 by Bentinck). The Sarda Act (1929) was on child marriage. The 2025 paper asked who founded newspapers and who edited journals, so reformers and their causes are in the same family as Mock 03's 'founder of an organisation' match.")
add(H, "The Gagging Act of 1857, which required a licence for printing presses, was passed during the time of:",
    ["Lord Canning", "Lord Dalhousie", "Lord Lytton", "Lord Ripon"],
    "It was passed just after the Revolt began and it stayed in force for a year. The press laws go in this order: Censorship of the Press Act 1799 (Wellesley), Licensing Regulations 1823 (John Adam), the 1835 law that freed the press (Metcalfe), the Gagging Act 1857 (Canning), the Vernacular Press Act 1878 (Lytton), and its repeal in 1882 (Ripon). The 2025 paper asked three questions from this chain.")
add(H, "Which of the following pairs (newspaper – person) is NOT correctly matched?",
    ["Bahishkrit Bharat – Jyotirao Phule", "Mooknayak – B. R. Ambedkar", "Pratap – Ganesh Shankar Vidyarthi", "Bombay Chronicle – Pherozeshah Mehta"],
    "Ambedkar started Mooknayak (1920) and Bahishkrit Bharat (1927). Phule's group worked through Satyashodhak Samaj and the paper Deenbandhu. Pratap was published from Kanpur by Vidyarthi. The Bombay Chronicle (1910) was started by Pherozeshah Mehta, and Horniman edited it. The 2025 paper's wrong pair mixed founders ('Bombay Times' by Sanjibani). Mock 01 matched Kesari, The Bengalee and Al-Hilal.", k="not")
add(H, "The Communist Party of India was first formed abroad in 1920 at:",
    ["Tashkent", "Moscow", "Berlin", "Kanpur"],
    "M. N. Roy and others formed it at Tashkent in October 1920. In India, the first All-India Communist Conference was at Kanpur in December 1925 (asked in Mock 03). The Labour Swaraj Party was formed in 1925 in Bengal by Muzaffar Ahmed, Qazi Nazrul Islam, Hemanta Kumar Sarkar and others (asked twice in 2025). The Meerut Conspiracy Case came in 1929 (Mock 02).")
add(H, "Who became the first woman Governor of a State in independent India?",
    ["Sarojini Naidu", "Vijaya Lakshmi Pandit", "Padmaja Naidu", "Sucheta Kripalani"],
    "Sarojini Naidu became Governor of the United Provinces in 1947. She had been the first Indian woman President of the Congress (Kanpur, 1925; asked in GA Mock 1). Vijaya Lakshmi Pandit was Governor of Maharashtra and Padmaja Naidu of West Bengal. Sucheta Kripalani was the first woman Chief Minister (Uttar Pradesh, 1963). Annie Besant, who was British, had presided over the Congress in 1917.")
add(H, "The Wardha Scheme of Basic Education (1937) was worked out by a committee headed by:",
    ["Zakir Husain", "B. G. Kher", "Abul Kalam Azad", "Sadler"],
    "It was Gandhi's idea of 'Nai Talim': free and compulsory education in the mother tongue for seven years, built around a craft. Zakir Husain's committee made the plan at the Wardha conference. The 2025 paper asked the order of four education bodies (Hunter 1882, Sadler 1917, Hartog 1929, Kothari 1964), and Mock 03 asked the order of Sargent, Raleigh and others. Wood's Despatch (1854) was the 'Magna Carta' (Mock 02).")
add(H, "Who was the Commander-in-Chief of the rebel army at Delhi during the Revolt of 1857?",
    ["Bakht Khan", "Tantia Tope", "Azimullah Khan", "Khan Bahadur Khan"],
    "Bakht Khan came from Bareilly with his soldiers and took charge at Delhi under Bahadur Shah Zafar. Tantia Tope was Nana Sahib's general at Kanpur and later Jhansi. Khan Bahadur Khan led at Bareilly (asked in Mock 01). The 2025 paper asked a 'wrongly matched' list of centres (Kanpur, Jagdishpur, Faizabad, Jhansi), and Mock 03 asked who led at Faizabad (Maulvi Ahmadullah).")
add(H, "Which one of the following pairs (Viceroy or Governor-General – event) is NOT correct?",
    ["Lord Lytton – the Ilbert Bill controversy", "Lord Ripon – the 1882 Resolution on local self-government", "Lord Curzon – the Partition of Bengal", "Lord Dalhousie – the Doctrine of Lapse"],
    "The Ilbert Bill (1883) belongs to Lord Ripon's time. It would have let Indian judges try Europeans, and the European protest forced a compromise (asked in 2018 and 2025). Lytton is remembered for the Vernacular Press Act, the Arms Act (both 1878) and the Delhi Durbar of 1877. Ripon is called the 'Father of Local Self-Government' (Mock 02). Curzon divided Bengal in 1905, and Hardinge cancelled it in 1911.", k="not")
add(H, "The principle of election (indirect) was first brought into the legislative councils by the:",
    ["Indian Councils Act, 1892", "Indian Councils Act, 1861", "Indian Councils Act, 1909", "Government of India Act, 1919"],
    "The 1892 Act let the Viceroy and Governors nominate some members on the 'recommendation' of local bodies, universities and chambers of commerce. It also allowed members to discuss the budget. The 1861 Act brought Indians into the council by nomination. The 1909 Act (Morley–Minto) brought separate electorates. The 1919 Act began dyarchy in the provinces. The 2025 paper asked what the 1935 Act brought (provincial autonomy).")
add(H, "The Rowlatt Act of 1919 was officially called the:",
    ["Anarchical and Revolutionary Crimes Act", "Press and Sedition Act", "Defence of India Act", "Public Safety Act"],
    "It let the Government jail people for two years without trial and try them without a jury. Indians called it the 'Black Act'. It led to the hartal of 6 April 1919, the Jallianwala Bagh firing on 13 April and the Hunter Committee (asked in the Full Test). Gandhi launched his first all-India satyagraha against it. Dr Satyapal and Dr Saifuddin Kitchlew were arrested in Amritsar.")
add(H, "Match List I (Book) with List II (Author):\nList I: a. Poverty and Un-British Rule in India  b. The Economic History of India  c. Hind Swaraj  d. The Discovery of India\nList II: 1. Jawaharlal Nehru  2. M. K. Gandhi  3. R. C. Dutt  4. Dadabhai Naoroji",
    [M(4, 3, 2, 1), M(3, 4, 2, 1), M(4, 3, 1, 2), M(4, 2, 3, 1)],
    "Naoroji's 'drain of wealth' theory came in Poverty and Un-British Rule in India (1901). R. C. Dutt wrote the Economic History of India (1901–03). Gandhi wrote Hind Swaraj in 1909, on the ship home from London. Nehru wrote The Discovery of India in Ahmednagar Fort jail (1944). The 2025 paper asked who edited papers and journals (Lajpat Rai and the Poona Sarvajanik Sabha), so authors and works are a safe family.", k="match")
add(H, "The title 'Sardar' was given to Vallabhbhai Patel after the success of the:",
    ["Bardoli Satyagraha (1928)", "Kheda Satyagraha (1918)", "Champaran Satyagraha (1917)", "Salt Satyagraha (1930)"],
    "Peasants of Bardoli in Gujarat refused to pay a raised land tax in 1928. Patel led them and the Government cancelled the increase. The women of Bardoli gave him the title. Patel also presided over the Karachi Session (1931), the one the 2025 paper asked about as a statement question (it was not Motilal Nehru). Kheda (1918) was Gandhi's first peasant struggle, and Champaran (1917) was against indigo planting.")
add(H, "Arrange the following events in the order in which they took place (earliest first):\n1. Poona Pact\n2. Dandi March\n3. Communal Award\n4. Second Round Table Conference",
    ["2, 4, 3, 1", "2, 3, 4, 1", "4, 2, 3, 1", "2, 4, 1, 3"],
    "Dandi March: March–April 1930. Second Round Table Conference: September to December 1931, where Gandhi was the Congress's only representative. Communal Award: August 1932, giving separate electorates to the Depressed Classes. Poona Pact: September 1932, between Gandhi and Ambedkar, which gave reserved seats in the general electorate instead. Mock 03 asked a similar order that began with the Gandhi–Irwin Pact (March 1931).", k="order")
add(H, "Consider the following statements about Lord Dalhousie:\n1. The first telegraph line in India was laid in his time.\n2. The Post Office Act of 1854 was passed in his time.\n3. He abolished the practice of sati.\nWhich of the statements given above are correct?",
    S3,
    "Statement 3 is wrong: Bentinck banned sati in 1829. Dalhousie (1848–56) opened the first telegraph line (Calcutta to Diamond Harbour, 1851), began the railway (Bombay to Thane, 1853), reformed the post with a uniform rate in 1854, and used the Doctrine of Lapse (Satara was the first State, 1848; asked in Mock 01). Wood's Despatch also came in his time (1854).",
    k="stmt", a=0)

# ------------------------------------------------------------------ DEFENCE (10)
D = "Defence"
add(D, "Match List I (Exercise) with List II (Partner country of India):\nList I: a. Surya Kiran  b. Ajeya Warrior  c. Mitra Shakti  d. Sampriti\nList II: 1. Sri Lanka  2. United Kingdom  3. Bangladesh  4. Nepal",
    [M(4, 2, 1, 3), M(2, 4, 1, 3), M(4, 2, 3, 1), M(4, 1, 2, 3)],
    "Surya Kiran is the army exercise with Nepal; Ajeya Warrior with the UK; Mitra Shakti with Sri Lanka; Sampriti with Bangladesh. The 2025 paper asked the 17th India–Mongolia exercise (Nomadic Elephant), Dharma Guardian (Japan) and Desert Flag (UAE), and Mock 01 and Mock 03 matched other partners. Every neighbour has its own exercise, so learn them by country: Maitree (Thailand), Ekuverin (Maldives), Harimau Shakti (Malaysia).", k="match", n=True)
add(D, "'Operation Trident', carried out by the Indian Navy on 4 December 1971, was an attack on:",
    ["Karachi harbour", "Chittagong port", "Gwadar port", "Colombo harbour"],
    "Missile boats sank or damaged Pakistani ships and set the oil tanks of Karachi on fire. Operation Python followed on 8–9 December. Navy Day, 4 December, remembers the attack. The 2025 paper asked four operation names (Jindagi, Keller, Olivia, Zero Line), and Mock 03 matched Meghdoot, Polo, Cactus and Vijay. Operation Trident is the Navy's famous war name, as Meghdoot is the Army's on Siachen.")
add(D, "Operation Urja Suraksha, run by the Indian Navy in 2026, was linked to:",
    ["escorting ships that carried oil and gas through the Strait of Hormuz", "rescuing Indians from Iran", "relief after a cyclone in Sri Lanka", "patrols against pirates off Somalia"],
    "The US–Israel strikes on Iran began on 28 February 2026, and shipping in the Strait of Hormuz became unsafe. 'Urja' means energy. Much of India's oil and gas comes through that strait. Operation Sindhu (2025) was the earlier rescue of Indians from Iran (Mock 02). The 2025 paper asked operation names like Jindagi (Varunavat landslide) and Zero Line, so purposes of operations are asked.", n=True)
add(D, "In the Indian Air Force, which rank is equal to a Brigadier in the Army?",
    ["Air Commodore", "Group Captain", "Air Vice Marshal", "Wing Commander"],
    "The Air Force ranks, from the bottom of the senior group: Wing Commander (Lieutenant Colonel), Group Captain (Colonel), Air Commodore (Brigadier), Air Vice Marshal (Major General), Air Marshal (Lieutenant General), Air Chief Marshal (General). In the Navy: Commander, Captain, Commodore, Rear Admiral, Vice Admiral, Admiral. Mock 01 and Mock 02 asked the Navy side (Commodore, Captain). GA Mock 1 asked the Air Force equal of a Major.")
add(D, "Consider the following statements about the Andaman and Nicobar Command:\n1. It was set up in 1999.\n2. It is a joint (tri-service) command with its headquarters at Port Blair.\n3. Its Commander-in-Chief is chosen in turn from the Army, Navy and Air Force.\nWhich of the statements given above are correct?",
    S3,
    "Statement 1 is wrong: it was set up in October 2001, after the Kargil Review Committee asked for better joint command. It was India's first joint command, and the Strategic Forces Command (2003) came later. The post goes in turn to officers of the three Services. The theatre commands that the new CDS, General N. S. Raja Subramani, is to set up (Mock 02) follow the same thought. The 2025 paper had three-statement questions on a force, a missile and a ship.",
    k="stmt", a=1)
add(D, "Which is the second-highest gallantry award of India in wartime?",
    ["Maha Vir Chakra", "Vir Chakra", "Kirti Chakra", "Shaurya Chakra"],
    "In wartime the order is Param Vir Chakra, Maha Vir Chakra and Vir Chakra. In peacetime it is Ashoka Chakra (asked in Mock 02), Kirti Chakra and Shaurya Chakra. Savitri Khanolkar designed the Param Vir Chakra (Mock 01). These awards started in 1950 and apply from 15 August 1947. Defence is the biggest news-linked topic of 2025 (12 questions), so awards and ranks are safe.")
add(D, "Arrange the following events in the order in which they took place (earliest first):\nA. Operation Sindoor\nB. Kargil War\nC. Pokhran-II nuclear tests\nD. Balakot air strike",
    ["C, B, D, A", "B, C, D, A", "C, B, A, D", "B, C, A, D"],
    "Pokhran-II: May 1998 (Operation Shakti). Kargil: May to July 1999. Balakot: 26 February 2019, after the Pulwama attack. Operation Sindoor: 7 May 2025, after the Pahalgam attack of 22 April 2025. The 2021 paper asked 'the present Chief of Air Staff' and 2025 had 12 defence questions, many on recent strikes and operations, so a sequence of conflicts is a good test.", k="order")
add(D, "The Defence Acquisition Council, which approves large purchases for the armed forces, is headed by:",
    ["the Defence Minister", "the Prime Minister", "the Chief of Defence Staff", "the Defence Secretary"],
    "The DAC was set up in 2001, after the Kargil Review Committee, and it clears 'Acceptance of Necessity' for big buys. The Defence Secretary and the Service chiefs are members. The CDS (Mock 01 and the Defence mock) is the Principal Military Adviser, not the head of the DAC. Policies of 2020 raised foreign investment in defence to 74% by the automatic route (Defence mock). Make in India in defence is a steady topic.")
add(D, "The Arjun, India's main battle tank, was designed by:",
    ["DRDO's Combat Vehicles Research and Development Establishment, Avadi", "Hindustan Aeronautics Limited, Bengaluru", "Bharat Electronics Limited, Bengaluru", "Mazagon Dock, Mumbai"],
    "The Arjun was developed by CVRDE at Avadi near Chennai, and the heavy vehicles factory at Avadi builds it. HAL makes aircraft and helicopters (Tejas, Dhruv). BEL makes electronics and radars. Mazagon Dock builds warships and submarines (the Scorpene submarines asked in the Defence mock). Learn which agency builds what: the 2025 paper asked who developed the Pralay (DRDO).")
add(D, "Which of the following long-range air defence missile systems did India buy from Russia?",
    ["S-400 Triumf", "Iron Dome", "Barak-8", "Patriot"],
    "The S-400 deal was signed in 2018 and the squadrons are in the Indian Air Force. Iron Dome and Barak-8 are Israeli. Patriot is American. The 2025 paper asked who announced the 'Golden Dome' (the USA), and the Defence mock asked which is NOT Israeli (THAAD). Mission Sudarshan Chakra, announced on 15 August 2025, is India's own plan for a national air shield.")

# ------------------------------------------------------------------ ENVIRONMENT (9)
E = "Environment"
add(E, "Under the Paris Agreement, the climate plans that each country submits are called:",
    ["Nationally Determined Contributions", "Clean Development Mechanisms", "Certified Emission Reductions", "National Adaptation Funds"],
    "The Paris Agreement (2015) asks each country to set its own NDC and renew it every five years. Its goal is to keep warming well below 2°C and aim for 1.5°C. Clean Development Mechanism and Certified Emission Reductions belong to the Kyoto Protocol (asked in 2025 as the date of adoption, 11 December 1997, and in Mock 03). India's targets at COP26 included net zero by 2070.")
add(E, "What was the theme of Earth Day 2025 (22 April)?",
    ["Our Power, Our Planet", "Planet vs. Plastics", "Invest in Our Planet", "Restore Our Earth"],
    "The 2025 theme was 'Our Power, Our Planet', which called for a switch to clean power. 'Planet vs. Plastics' was the 2024 theme (the 2025 paper asked 2024), 'Invest in Our Planet' was 2022 and 'Restore Our Earth' was 2021. Earth Day is run by EARTHDAY.ORG. Careful: our manual and Mock 01 give the same line for 2026, but that rests on one report, so keep the 2025 answer as the safe one.",
    n=True, c=True)
add(E, "Plant and animal species that are brought into a region from outside, usually by human action, are called:",
    ["exotic (alien) species", "endemic species", "keystone species", "edge species"],
    "Exotic species are not native. If they spread and harm local life they are called invasive (water hyacinth, lantana). The 2025 paper asked the word for species found only in one region (endemic) and what 'edge species' means (those that live in the ecotone). Mock 01 asked 'keystone'. The opposite of exotic is native or indigenous.")
add(E, "Which of the following is NOT a Biosphere Reserve of India?",
    ["Kaziranga", "Nilgiri", "Sundarbans", "Similipal"],
    "Kaziranga (Assam) is a National Park, a Tiger Reserve and a World Heritage Site, but not a Biosphere Reserve. Nilgiri (1986) was the first; Sundarbans (1989); Similipal (Odisha, UNESCO network in 2009). Assam's Biosphere Reserves are Manas and Dibru-Saikhowa. The 2025 paper asked the Biogeographical Regions of India in a four-part match, so protected-area types are a live family.", k="not")
add(E, "India's first Biosphere Reserve, set up in 1986, is the:",
    ["Nilgiri Biosphere Reserve", "Sundarbans Biosphere Reserve", "Nanda Devi Biosphere Reserve", "Gulf of Mannar Biosphere Reserve"],
    "It covers parts of Tamil Nadu, Kerala and Karnataka, and holds Mudumalai, Bandipur, Nagarhole and Silent Valley. Nanda Devi (Uttarakhand) came in 1988 and Gulf of Mannar (Tamil Nadu, 1989) was the first marine one. Biosphere Reserves have a core, a buffer and a transition zone. The 2025 paper asked which hills are closest to Kanyakumari, and the Nilgiri answer in Mock 02 was where the Ghats meet.")
add(E, "Which is the largest tiger reserve of India by area?",
    ["Nagarjunsagar–Srisailam, Andhra Pradesh and Telangana", "Sundarbans, West Bengal", "Similipal, Odisha", "Manas, Assam"],
    "The Nagarjunsagar–Srisailam reserve covers more than 3,000 sq km as a core area. Similipal is the biggest in Odisha (and Odisha's second national park since 2025). India has 58 tiger reserves since Madhav (Madhya Pradesh) was added in March 2025 (asked in Mock 02). The sixth All India Tiger Estimation report is due in 2027, and the 2022 count was 3,682 tigers.", n=True)
add(E, "Under the Wildlife (Protection) Act, 1972, animals that get the highest legal protection are placed in:",
    ["Schedule I", "Schedule II", "Schedule IV", "Schedule V"],
    "Schedule I (and Part II of Schedule II) carry the strictest punishment for hunting: tiger, elephant, snow leopard, and the olive ridley turtle (listed as Vulnerable by the IUCN, Mock 03). The Act made national parks and tiger reserves possible. A change in 2022 cut the schedules from six to four: I and II for animals, III for protected plants and IV for species listed under CITES.")
add(E, "Consider the following statements:\n1. El Niño is a cooling of the surface water of the central and eastern Pacific Ocean.\n2. El Niño years are often linked to a weak monsoon in India.\n3. La Niña years are often linked to a good monsoon in India.\nWhich of the statements given above are correct?",
    S3,
    "Statement 1 is wrong: El Niño is a warming of the water, and La Niña is the cooling. In an El Niño year the air pressure pattern over the Pacific (the Southern Oscillation) weakens the monsoon winds, so rain is often poor, as in 2009 and 2023. La Niña usually helps the monsoon. The 2025 paper asked a two-statement question on the Indian Ocean Dipole, and Mock 02 on its positive phase. IOD, El Niño and La Niña form one family.",
    k="stmt", a=1)
add(E, "The National Biodiversity Authority, set up under the Biological Diversity Act, 2002, has its headquarters at:",
    ["Chennai", "New Delhi", "Bhopal", "Dehradun"],
    "The Act put India's Convention on Biological Diversity duties into law: it controls the use of biological resources by foreign firms and ensures sharing of benefits with local people. States have Biodiversity Boards and villages have Biodiversity Management Committees. Dehradun holds the Forest Survey of India, which publishes the ISFR every two years (asked in 2025, Mock 01 and Mock 03). Bhopal has the Indian Institute of Forest Management.")

# ------------------------------------------------------------------ ECONOMY (8)
EC = "Economy"
add(EC, "Which of the following is NOT a revenue receipt of the Government of India?",
    ["Recovery of loans given earlier", "Corporation tax", "Interest received on loans", "Dividends from public sector companies"],
    "A revenue receipt does not create a debt or reduce an asset. Taxes, interest and dividends are revenue. A capital receipt either creates a liability (borrowing) or reduces an asset (recovery of loans, sale of shares in a PSU). The 2025 paper asked what is NOT part of the fiscal deficit (monetary deficit), and Mock 02 asked the effective revenue deficit. Revenue deficit = revenue expenditure minus revenue receipts.", k="not")
add(EC, "Gross Value Added (GVA) at basic prices is obtained from GDP at market prices by:",
    ["subtracting product taxes and adding product subsidies", "adding product taxes and subtracting product subsidies", "subtracting depreciation", "adding net factor income from abroad"],
    "GDP at market prices = GVA at basic prices + product taxes − product subsidies. So GVA = GDP − taxes + subsidies. India moved to GVA as the main output measure in 2015, with the base year 2011–12. The new GDP series released on 27 February 2026 uses 2022-23 (Mock 02). The 2025 paper asked which sector gives the most to GDP (services).")
add(EC, "The first nationalisation of 14 major commercial banks in India took place in:",
    ["1969", "1955", "1980", "1991"],
    "On 19 July 1969 the Government of Indira Gandhi took over 14 banks with deposits above ₹50 crore. Six more were nationalised in 1980. The Imperial Bank became the State Bank of India in 1955, and the RBI was nationalised in 1949 (GA Mock 1). The 2025 paper asked what is NOT a function of the RBI (regulating stock exchanges, which is SEBI's job). Reform of banks is a steady family: Narasimham, Malhotra (Mock 02).")
add(EC, "Consider the following statements about the Fiscal Responsibility and Budget Management (FRBM) Act:\n1. It was passed in 2003.\n2. It allows the RBI to lend to the Government without limit.\n3. Its original target was a fiscal deficit of 3 per cent of GDP.\nWhich of the statements given above are correct?",
    S3,
    "Statement 2 is wrong: the Act banned the RBI from buying Government bonds in the primary market (from 2006), so the Government cannot be funded by printing money. Statements 1 and 3 are right. The N. K. Singh Committee (2016–17) reviewed it (asked in Mock 01) and suggested a debt-to-GDP goal. Budget 2026-27 set the fiscal deficit target at 4.3% of GDP. The 2025 paper asked about deficits.",
    k="stmt", a=2)
add(EC, "A situation of high inflation together with slow growth and high unemployment is called:",
    ["stagflation", "deflation", "disinflation", "reflation"],
    "Stagflation joins 'stagnation' and 'inflation'. It was seen in the 1970s after the oil price shocks. Deflation is a fall in the general price level. Disinflation is a fall in the rate of inflation, while prices still rise. Reflation is a push to raise prices after deflation. Mock 03 asked the cost-push and demand-pull types of inflation, and Mock 02 asked the RBI's 4% target.")
add(EC, "The Cash Reserve Ratio (CRR) is the share of a bank's deposits that the bank must keep:",
    ["with the Reserve Bank of India, in cash, without interest", "in Government securities", "as gold", "as loans to farmers"],
    "CRR is a quantitative tool of credit control: if the RBI raises it, banks have less to lend. The SLR (Statutory Liquidity Ratio) is the share kept in the bank's own vault as cash, gold or Government bonds. Moral suasion is a qualitative tool (Mock 01). The 2025 paper asked what is NOT a function of the RBI. In October 2026 the RBI raised the repo rate by 0.25 point (a CHECK item in our manual).")
add(EC, "Which was the last Five Year Plan of India?",
    ["Twelfth Plan (2012–17)", "Eleventh Plan (2007–12)", "Tenth Plan (2002–07)", "Thirteenth Plan"],
    "After the Twelfth Plan, the Planning Commission was replaced by NITI Aayog on 1 January 2015, and the Plan system ended in 2017. The theme was 'faster, more inclusive and sustainable growth'. The Eleventh Plan said 'inclusive growth'. The 2018, 2021 and 2025 papers each asked the Rolling Plan (1978–80) or its Plan, and Mock 01 and Mock 03 asked who gave the idea and which Plan it replaced.")
add(EC, "'No tax shall be levied or collected except by authority of law.' This is stated in Article:",
    ["265", "112", "266", "280"],
    "Article 265 sits in the Part on Finance. Article 112 is the Annual Financial Statement, Article 266 the Consolidated and Public Accounts of the States and the Union (Mock 03 matched the Funds), and Article 280 the Finance Commission. The 16th Finance Commission (chair Arvind Panagariya) covers 2026–31 and kept the States' share at 41% (Mock 02). GST is Article 246A and 279A (Mock 03).")

# ------------------------------------------------------------------ GOVERNANCE (6)
G = "Governance"
add(G, "The Prevention of Corruption Act, which replaced the Act of 1947, was passed in:",
    ["1988", "1964", "2003", "2013"],
    "The 1988 Act covers public servants who take bribes or hold unexplained wealth. It was changed in 2018 so that giving a bribe is also an offence. The CVC became statutory in 2003 (Mock 03). The Lokpal and Lokayuktas Act was passed in 2013 (the Lokpal itself began work in 2019). The 2021 and 2025 papers both asked the Santhanam Committee on corruption (1962), so the rest of the anti-corruption chain is the next angle.")
add(G, "The Vohra Committee (1993) looked into:",
    ["the links between criminals, politicians and officials", "the reform of police training", "the pay of civil servants", "the rights of State Governors"],
    "N. N. Vohra's report described a nexus between criminal gangs, politicians and bureaucrats. It was a wrong option in the 2025 question on Governors (the right one was the 2nd Administrative Reforms Commission, which said appointments should be non-partisan). The 2025 paper listed four committees (B. R. Mehta, Yugandhar, Yoginder K. Alagh and Hota) in which one was NOT on civil services.")
add(G, "The State Administrative Training Institute of Odisha, in Bhubaneswar, is called:",
    ["Gopabandhu Academy of Administration", "Nabakrushna Choudhury Centre for Development Studies", "Utkal Institute of Public Administration", "Harekrushna Mahtab Academy"],
    "The Gopabandhu Academy trains Odisha's State services and gives orientation to IAS officers. Nabakrushna Choudhury Centre for Development Studies is a research centre. The 2025 paper asked where the NIRDPR is (Hyderabad) and when the IIPA was set up (1954). Mock 02 asked about LBSNAA. The Odisha Government is putting ₹585 crore into Suando, Gopabandhu Das's birthplace in Puri district (2026).")
add(G, "The institution of the Ombudsman, on which the Lokpal is modelled, first began in:",
    ["Sweden", "the United Kingdom", "New Zealand", "Denmark"],
    "Sweden created the post in 1809. New Zealand was the first Commonwealth country to adopt it (1962). The Citizen's Charter idea came from the UK (1991). The word 'Lokpal' was coined by L. M. Singhvi in 1963 (Mock 01). The First ARC (1966) suggested the Lokpal and Lokayuktas. Odisha was the first State to pass a Lokayukta law, in 1970 (CHECK before the exam).", c=True)
add(G, "Consider the following statements about the Comptroller and Auditor General (CAG) of India:\n1. He is appointed by the President.\n2. He can be removed by the President at will.\n3. His reports on the Union accounts go to the President, who places them before Parliament.\nWhich of the statements given above are correct?",
    S3,
    "Statement 2 is wrong: the CAG is removed like a Supreme Court judge, by Parliament on a special majority for proved misbehaviour or incapacity (Article 148). Statement 3 is Article 151. The CAG is the 'friend, philosopher and guide' of the Public Accounts Committee (asked in Mock 02). The present CAG is K. Sanjay Murthy. The 2025 paper asked how the Chief Election Commissioner is removed (like a judge).",
    k="stmt", a=2)
add(G, "Which Commission on Centre–State relations, set up in 2007, was headed by Justice M. M. Punchhi?",
    ["Punchhi Commission", "Sarkaria Commission", "Rajamannar Committee", "Venkatachaliah Commission"],
    "It gave its report in 2010. It said that the Governor's term should be fixed and that he can be removed only by impeachment-like steps. The Sarkaria Commission (1983) led to the Inter-State Council in 1990 (Mock 01). The Rajamannar Committee (1969) was set up by Tamil Nadu. The Venkatachaliah Commission (2000–02) reviewed the working of the Constitution. The 2025 paper asked which body said Governors should be non-partisan.")

# ------------------------------------------------------------------ ODISHA (7)
O = "Odisha"
add(O, "Which river of Odisha was called the 'Sorrow of Odisha' because of its floods?",
    ["Mahanadi", "Brahmani", "Baitarani", "Subarnarekha"],
    "The Mahanadi brings floods to the delta every monsoon and was called this before the Hirakud Dam (dedicated in 1957) helped control them. The 2025 paper asked which Odisha river saw 6.98 lakh olive ridleys nest (Rushikulya) and what 'Hexadeltaic' means (six rivers' deltas). The Mahanadi's name means 'great river'. Cuttack stands at the head of its delta, and the Bali Jatra of Kartika Purnima is held on its bank (Mock 01).")
add(O, "Chilika Lake in Odisha is the largest ____ in Asia.",
    ["brackish water lagoon", "freshwater lake", "oxbow lake", "salt lake in a desert"],
    "Chilika lies on the coast of Puri, Khordha and Ganjam districts, and joins the Bay of Bengal by a narrow mouth. Its water is part fresh, part salty. It is the winter home of migratory birds (Nalabana is the bird sanctuary) and has the Irrawaddy dolphin. Mock 01 asked the largest freshwater lake of Odisha (Ansupa, in Cuttack). Odisha has six Ramsar sites (Mock 02 and 03).")
add(O, "Match List I (Place) with List II (Mineral for which it is known):\nList I: a. Sukinda (Jajpur)  b. Talcher (Angul)  c. Joda–Barbil (Keonjhar)  d. Gandhamardan (Bargarh)\nList II: 1. Bauxite  2. Iron ore  3. Coal  4. Chromite",
    [M(4, 3, 2, 1), M(3, 4, 2, 1), M(4, 3, 1, 2), M(4, 2, 3, 1)],
    "Sukinda has almost all of India's chromite. Talcher is the coalfield of the Brahmani valley (Mock 01). Joda and Barbil are the iron ore and manganese centres. Gandhamardan, between Bargarh and Bolangir, has bauxite. The 2025 paper asked a place–mineral match (Baula-Nuasahi, Kesarpur, Chhatrapur, Sunki), and Mock 02 asked Panchpatmali (bauxite). Odisha has most of India's chromite, bauxite and a large part of its iron ore.", k="match")
add(O, "Consider the following statements about recent cyclones of the Bay of Bengal:\n1. Cyclone Montha (October 2025) was named by Thailand.\n2. Cyclone Senyar (November 2025) was named by the UAE.\n3. Cyclone Ditwah (2025), which hit Sri Lanka, was named by Bangladesh.\nWhich of the statements given above are correct?",
    S3,
    "Statement 3 is wrong: Ditwah was named by Yemen. Names for cyclones in the North Indian Ocean are given in turn by the countries of the WMO/ESCAP panel, in a fixed list. Bangladesh gave 'Arnab', and our manual says the next on the list is 'Murasu' (CHECK). Odisha is hit by these storms often, and the 2025 paper asked about Operation Jindagi and the Olivia nesting, so Odisha's coastal hazards are a live family.",
    k="stmt", a=0, n=True)
add(O, "Which is the most populous Scheduled Tribe of Odisha?",
    ["Kondh (Kandha)", "Santal", "Gond", "Munda"],
    "In the 2011 Census the Kondh had about 16 lakh people, ahead of the Santal and Gond (each about 9 lakh). Odisha has 62 Scheduled Tribes and 13 Particularly Vulnerable Tribal Groups (Bonda, Didayi, Juang and others). The Kondhs live in Kandhamal, Rayagada and Kalahandi. The Gopabandhu Jan Arogya and Samrudha Krushaka schemes are among the Odisha news of 2026, and the 2026 scheme MMJJM 2.0 is for tribal livelihoods (Mock 02).")
add(O, "Odisha Day (Utkal Divas), 1 April 2026, marked how many years since the formation of the Odisha province in 1936?",
    ["90 years", "75 years", "80 years", "100 years"],
    "Odisha became a separate province on a language basis on 1 April 1936, the first in India, with Sir John Austen Hubback as Governor and Krishna Chandra Gajapati as the first Prime Minister. Harekrushna Mahtab was the Premier when India became free in 1947 (Mock 01). The Utkal Sammilani of Madhusudan Das began the demand (1903). 'Utkal Gaurav' is Madhusudan Das.", n=True, c=True)
add(O, "Which district of Odisha is called the 'rice bowl' of the State?",
    ["Bargarh", "Cuttack", "Balasore", "Ganjam"],
    "Bargarh, in the Hirakud command area, is known for its large paddy crop. The Hirakud dam's canals feed Bargarh, Sambalpur, Bolangir and Sonepur (the 2025 paper asked which districts get irrigation from Hirakud and the Mahanadi canal). The Dhanu Jatra of Bargarh is its famous festival, said to be the world's largest open-air theatre (CHECK).", c=True)

# ------------------------------------------------------------------ INSTITUTIONS (6)
I = "Institutions"
add(I, "Which two Indian works were inscribed on UNESCO's Memory of the World Register in April 2025?",
    ["The Bhagavad Gita and Natyashastra", "The Ramayana and Mahabharata", "The Arthashastra and Kamasutra", "The Rigveda and Upanishads"],
    "The Memory of the World Register protects documents and manuscripts (the 2025 paper asked its aim). It is different from the World Heritage List (sites) and the Intangible Heritage List (traditions, such as Deepavali, added in December 2025). The Rigveda manuscripts were inscribed earlier, in 2007. Check this with the manual before the exam, as it rests on one source.",
    n=True, c=True)
add(I, "The headquarters of the International Atomic Energy Agency (IAEA) is at:",
    ["Vienna, Austria", "Geneva, Switzerland", "New York, USA", "The Hague, Netherlands"],
    "The 2025 paper put 'Vienna' as a wrong HQ of the World Meteorological Organization (WMO is at Geneva). The IAEA, an independent body linked to the UN, is at Vienna. The ICJ is at The Hague. The UN Headquarters is in New York, and UNEP is in Nairobi. Mock 01 matched WMO and others with their HQs and Mock 03 did the banks, so another set of seats is the next angle.")
add(I, "The Swachh Survekshan, the national survey of the cleanliness of cities, is conducted by the:",
    ["Ministry of Housing and Urban Affairs", "Ministry of Jal Shakti", "Ministry of Environment, Forest and Climate Change", "Ministry of Rural Development"],
    "It is the main part of the Swachh Bharat Mission (Urban). The 2025–26 results said that Puri was first among clean coastal towns (CHECK). Swachh Bharat (Gramin) is run by Jal Shakti. The 2025 paper asked which ministry hosted the Purple Fest and which launched Bharat Ranbhoomi Darshan, so 'which ministry' is a steady question type.", c=True)
add(I, "The United Nations Environment Programme (UNEP), which leads World Environment Day, has its headquarters at:",
    ["Nairobi, Kenya", "Geneva, Switzerland", "Paris, France", "New York, USA"],
    "UNEP is the only major UN body with its main office in the developing world. World Environment Day (5 June) is run by UNEP with a host country (Azerbaijan in 2026, Republic of Korea in 2025; Mocks 01 and 03). UNESCO is at Paris. The World Water Day theme is set by UN-Water, and Earth Day by EARTHDAY.ORG, so know who sets which day.")
add(I, "United Nations Day is observed on:",
    ["24 October", "26 June", "10 December", "1 January"],
    "The UN Charter came into force on 24 October 1945. The UN turned 80 in 2025. 26 June is the day the Charter was signed (1945). 10 December is Human Rights Day. The 2025 paper asked what a 'Goodwill Ambassador' of the UN is, and the 2018 paper asked about a non-UN body (the Red Cross). The UN General Assembly has 193 members.")
add(I, "The Food Safety and Standards Authority of India (FSSAI) works under the:",
    ["Ministry of Health and Family Welfare", "Ministry of Consumer Affairs", "Ministry of Agriculture", "Ministry of Commerce and Industry"],
    "FSSAI was set up under the Food Safety and Standards Act, 2006 and has its headquarters in Delhi. The Bureau of Indian Standards (BIS) comes under Consumer Affairs, Food and Public Distribution. Agmark is under Agriculture. The 2025 paper asked which Union Ministry hosted the Purple Fest (Social Justice and Empowerment), so match each body to its ministry.")

# ------------------------------------------------------------------ GENERAL NEWS (6)
N = "General News"
add(N, "What was the theme of World Consumer Rights Day (15 March) in 2025?",
    ["A Just Transition to Sustainable Lifestyles", "Fair and Responsible AI for Consumers", "Empowering Consumers through Clean Energy Transitions", "Tackling Plastic Pollution Together"],
    "The 2025 theme was 'A Just Transition to Sustainable Lifestyles'. The 2024 theme was 'Fair and Responsible AI for Consumers' and the 2023 theme was clean energy. In India, National Consumer Day is on 24 December (Mock 03), when the Consumer Protection Act of 1986 got the President's assent. The 2025 paper asked the date of World Consumer Rights Day, so the previous-year theme is the next angle.", n=True)
add(N, "The main national event of the International Day of Yoga 2025 (21 June), led by the Prime Minister, was held at:",
    ["Visakhapatnam", "Srinagar", "Ranchi", "Mysuru"],
    "The 2025 theme was 'Yoga for One Earth, One Health', and the event at Visakhapatnam (Andhra Pradesh) had a record number of people. Srinagar was the venue in 2024, Mysuru in 2022 and Ranchi in 2019. The 2026 Yoga Day was the 12th; its theme in our manual is 'Yoga for Healthy Ageing' (CHECK). The 2025 paper asked four days: Water, Consumer Rights, TB and Voters'.", n=True)
add(N, "Consider the following statements about the UN Security Council:\n1. Five non-permanent members are elected every year.\n2. Non-permanent members have the power of veto.\n3. A non-permanent member serves for two years.\nWhich of the statements given above are correct?",
    S3,
    "Statement 2 is wrong: only the five permanent members (the USA, UK, France, Russia and China) can veto. The General Assembly elects five of the ten non-permanent members each year, by a two-thirds vote. In June 2026 Kyrgyzstan was elected for the first time for 2027–28 (Mock 02), and Germany lost its bid. The 2018 paper asked the Council twice and 2021 asked the June election.",
    k="stmt", a=2, n=True)
add(N, "Who became the first woman Prime Minister of Japan in October 2025?",
    ["Sanae Takaichi", "Yuriko Koike", "Shigeru Ishiba", "Mizuho Fukushima"],
    "Takaichi took over from Shigeru Ishiba. She belongs to the Liberal Democratic Party. Pope Leo XIV (Robert Prevost, elected in May 2025) is the first Pope from the USA. Other new heads in the news: Balendra Shah (Nepal, March 2026) and Tarique Rahman (Bangladesh, February 2026), both asked in earlier mocks. The 2025 paper asked who is the new head of a country or body, so a list of new leaders is useful.", n=True)
add(N, "The first G20 Leaders' Summit held on African soil, in November 2025, took place in:",
    ["Johannesburg", "Cape Town", "Nairobi", "Cairo"],
    "South Africa held the G20 presidency in 2025. India hosted in 2023 (New Delhi, where the African Union became a permanent member) and Brazil in 2024 (Rio). The USA holds the presidency in 2026 and the summit is planned at Miami. The 2025 paper asked the host of the BIMSTEC Youth Summit, and Mock 03 asked the host of the BIMSTEC summit (Bangkok, 2025) and the 52nd G7 (Évian, France, 2026).", n=True)
add(N, "María Corina Machado, who won the Nobel Peace Prize in 2025, is a leader from:",
    ["Venezuela", "Colombia", "Argentina", "Brazil"],
    "The Nobel Committee honoured her for her work to bring democracy to Venezuela. The 2026 Peace Prize went to Navi Pillay of South Africa (Mock 03). The 2021 paper asked the Nobel of 2019 and the 2025 paper asked the Earth Day theme of the year before, so the previous year's winner is a typical question. László Krasznahorkai (Hungary) won Literature in 2025, and Chemistry 2025 was for metal–organic frameworks (Mock 02).", n=True)

# ------------------------------------------------------------------ WORLD GEOGRAPHY (6)
W = "World Geography"
add(W, "Arrange the gases of the atmosphere in the decreasing order of their share by volume:\n1. Argon\n2. Carbon dioxide\n3. Nitrogen\n4. Oxygen",
    ["3, 4, 1, 2", "3, 4, 2, 1", "4, 3, 1, 2", "3, 1, 4, 2"],
    "Nitrogen is about 78%, oxygen about 21%, argon about 0.93% and carbon dioxide about 0.04%. The 2025 paper matched the same gases (oxygen 21%, nitrogen 78%, ozone, water vapour) in a four-part list. Water vapour varies from near zero to 4%. Ozone is a very small part and sits mostly in the stratosphere. Carbon dioxide is small but it is the main gas behind the warming asked in each paper.", k="order")
add(W, "Mount Etna, one of the most active volcanoes in the world, is in:",
    ["Italy", "Japan", "Iceland", "Indonesia"],
    "Etna is on the island of Sicily. The 2025 paper asked where Mount Lewotobi Laki-Laki erupts (Indonesia). Other volcanoes: Vesuvius (Italy), Fuji (Japan), Krakatoa (Indonesia), Mauna Loa (Hawaii) and Barren Island (India's only active one, Andaman Sea; Mock 03). Most of the world's volcanoes lie on the 'Ring of Fire' around the Pacific (Mock 03).")
add(W, "Victoria Falls, one of the largest waterfalls in the world, is on the river:",
    ["Zambezi", "Congo", "Orange", "Limpopo"],
    "The Zambezi forms the falls on the border of Zambia and Zimbabwe. It then flows into the Indian Ocean in Mozambique. The 2025 paper asked which river crosses the Equator twice (Congo) and Mock 02 asked the one that crosses the Tropic of Capricorn twice (Limpopo). The Orange River flows west into the Atlantic. Kariba and Cahora Bassa dams are on the Zambezi.")
add(W, "The highest navigable lake in the world is:",
    ["Lake Titicaca", "Lake Baikal", "Lake Victoria", "Lake Tanganyika"],
    "Titicaca lies at about 3,800 m in the Andes, on the border of Peru and Bolivia. Baikal in Russia is the deepest lake (Mock 01). Victoria is the largest in Africa and the largest tropical lake. Tanganyika is the longest freshwater lake and second deepest. The Caspian Sea is the largest inland water body. The 2025 paper asked the deepest part of the ocean (Challenger Deep).")
add(W, "The Bab-el-Mandeb strait connects the Red Sea with the:",
    ["Gulf of Aden", "Persian Gulf", "Mediterranean Sea", "Gulf of Oman"],
    "Bab-el-Mandeb lies between Yemen and Djibouti and Eritrea. The Suez Canal links the Red Sea with the Mediterranean, so ships to Europe pass both. The Strait of Hormuz joins the Persian Gulf and the Gulf of Oman (Mock 01), and it was in the 2026 news after the Iran war (Operation Urja Suraksha). The Malacca Strait joins the Indian Ocean and the South China Sea.")
add(W, "Match List I (Grassland) with List II (Region):\nList I: a. Pampas  b. Prairies  c. Steppes  d. Canterbury\nList II: 1. North America  2. New Zealand  3. Argentina  4. Eurasia",
    [M(3, 1, 4, 2), M(1, 3, 4, 2), M(3, 1, 2, 4), M(3, 4, 1, 2)],
    "Pampas are in Argentina and Uruguay, the Prairies in the USA and Canada, the Steppes across Eurasia, and the Canterbury Plains in New Zealand. The 2025 paper asked what 'savannas' are (tropical grasslands) and the 2021 paper had a grasslands question. Mock 01 matched Downs, Veld, Llanos and Puszta, and Mock 03 asked Campos (Brazil). Temperate grasslands are the 'granary' of the world.", k="match")

# ------------------------------------------------------------------ INDIA GEOGRAPHY (5)
IG = "India Geography"
add(IG, "Which State shares international borders with Bangladesh, Bhutan and Nepal?",
    ["West Bengal", "Sikkim", "Assam", "Meghalaya"],
    "West Bengal touches all three: Bangladesh (the longest border), Nepal (a short stretch in Darjeeling) and Bhutan. Sikkim has Nepal, Bhutan and China. Assam has Bhutan and Bangladesh. Meghalaya has only Bangladesh. The 2025 paper asked a four-part match of States with Bhutan–Bangladesh, China–Nepal, China and Pakistan borders. Mock 01 asked the State with the most neighbouring States (Uttar Pradesh), and Mock 02 asked the State without a Myanmar border (Tripura).")
add(IG, "Nathu La, a pass through which India has traded with China, is in:",
    ["Sikkim", "Arunachal Pradesh", "Uttarakhand", "Himachal Pradesh"],
    "Nathu La (about 4,300 m) is in Sikkim, on the old Silk Route. Trade through it began in 2006. Lipulekh is in Uttarakhand and Shipki La in Himachal Pradesh (the Sutlej enters India there; Mock 01). Our manual says border trade through Nathu La resumed on 1 August 2026 after six years (CHECK). The 2025 paper had a question on State borders, and Mock 02 matched passes (Zoji La, Rohtang, Lipulekh).", c=True, n=True)
add(IG, "Match List I (Peak) with List II (State):\nList I: a. Doddabetta  b. Kalsubai  c. Mahendragiri  d. Guru Shikhar\nList II: 1. Odisha  2. Rajasthan  3. Tamil Nadu  4. Maharashtra",
    [M(3, 4, 1, 2), M(4, 3, 1, 2), M(3, 4, 2, 1), M(3, 1, 4, 2)],
    "Doddabetta (Nilgiris) is the highest peak of the Nilgiris. Kalsubai is the highest peak of Maharashtra, in the Sahyadri. Mahendragiri is in the Eastern Ghats of Gajapati district, Odisha. Guru Shikhar (Mount Abu) is the highest peak of the Aravallis. The 2025 paper asked the hills near Kanyakumari and an order of Odisha's hills north to south, and Mock 02 matched Odisha's peaks with districts.", k="match")
add(IG, "Which river is called the 'Sorrow of Bihar' because of its frequent floods and shifting course?",
    ["Kosi", "Gandak", "Sone", "Ghaghara"],
    "The Kosi rises in Nepal and carries a very heavy load of silt, so it changes its course. The 2008 flood was one of the worst. The Mahanadi was the 'Sorrow of Odisha', the Damodar the 'Sorrow of Bengal' and the Brahmaputra the 'Sorrow of Assam'. The Sutlej enters India at Shipki La, and the Brahmaputra is the Siang in Arunachal Pradesh (Mock 03).")
add(IG, "The Coromandel Coast lies mainly along the coast of:",
    ["Tamil Nadu", "Odisha", "Kerala", "Maharashtra"],
    "It is the southern part of the Eastern Coastal Plain, between Kanyakumari and the Krishna delta (Tamil Nadu and the south of Andhra Pradesh). The northern part is the Northern Circars. The west coast has the Konkan (Maharashtra and Goa), Kannada coast and Malabar (Kerala). The 2025 paper asked the name 'Hexadeltaic region' for Odisha's coast, and Mock 02 asked which river is not among the six.")

# ------------------------------------------------------------------ SCIENCE & TECH (6)
S = "Science & Tech"
add(S, "Which of the following diseases is caused by a virus?",
    ["Measles", "Tuberculosis", "Cholera", "Leprosy"],
    "Measles, like mumps (asked in 2025 as a contagious airborne viral disease), is caused by a virus. Tuberculosis and leprosy are caused by bacteria (Mycobacterium). Cholera is a waterborne bacterial disease (Mock 02). Vaccines exist for measles (MMR), but not for leprosy. World TB Day is on 24 March, the day Robert Koch announced the TB bacterium in 1882 (asked in 2025).")
add(S, "The landing site of Chandrayaan-3 near the Moon's south pole was named:",
    ["Shiv Shakti Point", "Tiranga Point", "Jawahar Point", "Vikram Point"],
    "The Prime Minister gave the name 'Shiv Shakti' on 26 August 2023. The place where Chandrayaan-2's lander crashed in 2019 is 'Tiranga Point'. Chandrayaan-1's impact probe (2008) fell at 'Jawahar Point'. 23 August is observed as National Space Day. Mock 02 asked about the PSLV-C62 failure of 12 January 2026, and the 2025 paper asked which orbit EOS-09 was meant for (sun-synchronous).")
add(S, "The AI Impact Summit of February 2026 was held at:",
    ["Bharat Mandapam, New Delhi", "Bletchley Park, UK", "Seoul, South Korea", "Paris, France"],
    "India hosted the fourth in a line of global AI summits. Bletchley Park (2023) was the AI Safety Summit, Seoul followed in 2024 and Paris in February 2025. The 2025 paper asked which country first criminalised AI-generated child abuse material (the UK). Earlier mocks asked the 2026 news of space and tech (Gaganyaan, NISAR, Artemis II). Learn who hosted what, and when.", n=True)
add(S, "Match List I (Vitamin) with List II (Chemical name):\nList I: a. Vitamin A  b. Vitamin B1  c. Vitamin C  d. Vitamin D\nList II: 1. Thiamine  2. Ascorbic acid  3. Retinol  4. Calciferol",
    [M(3, 1, 2, 4), M(1, 3, 2, 4), M(3, 1, 4, 2), M(3, 2, 1, 4)],
    "Vitamin A is retinol (night blindness when short). B1 is thiamine (beri-beri). C is ascorbic acid (scurvy). D is calciferol (rickets), made in the skin in sunlight (Mock 01). Vitamin K is for blood clotting and E is an antioxidant. The 2025 paper had one question on a disease (mumps) and one on air gases, so everyday science has a steady two or three questions.", k="match")
add(S, "Which of the following diseases is NOT spread by mosquitoes?",
    ["Typhoid", "Malaria", "Dengue", "Chikungunya"],
    "Typhoid is caused by the bacterium Salmonella typhi and spreads through dirty food and water. Malaria spreads by the female Anopheles mosquito (the parasite is Plasmodium), dengue by the Aedes mosquito (Mock 03), and chikungunya also by Aedes. Mumps (2025) spreads by air. Cholera spreads by water (Mock 02). Keep the three groups: water, air and insects.", k="not")
add(S, "The India Semiconductor Mission, launched in 2021, is run under the:",
    ["Ministry of Electronics and Information Technology", "Ministry of Commerce and Industry", "Department of Science and Technology", "Ministry of Heavy Industries"],
    "The Mission was approved with an outlay of ₹76,000 crore, and India Semiconductor Mission 2.0 was cleared in July 2026 with about ₹1.27 lakh crore (CHECK). In Odisha, Info Valley, Bhubaneswar will host a 3D-glass chip-packaging unit (June 2026 MoU with Intel and 3D Glass Solutions). The 2025 paper asked where SpaceX is headquartered and which ISRO satellite went on PSLV-C61, so tech and space come with a place.",
    n=True, c=True)
