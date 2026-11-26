S12 = ["Only 1", "Only 2", "Both 1 and 2", "Neither 1 nor 2"]
S3 = ["Only 1 and 2", "Only 2 and 3", "Only 1 and 3", "1, 2 and 3"]
def M(a, b, c, d):
    return "a-%d, b-%d, c-%d, d-%d" % (a, b, c, d)

META = dict(
    paper="ga",
    title="ASO GS Mock 06",
    hub_title="GS Mock 06",
    masthead="GS Mock 06",
    heading="General Studies Paper I · Mock 06",
    tagline="100 questions drawn by probability<br>from the <b>2018, 2021 and 2025</b> papers.",
    key="aso-gs-mock-2027-6",
    code="GS06",
    out="ASO-GS-Mock-Test-2027-6.html",
    minutes=90,
    seed=20261126,
    order="mixed",
    date="26 Nov 2026",
    draw="python3 .claude/skills/aso-mock/scripts/draw.py ga --n 100 --seed 208328444",
    intro=[
        "This is a full General Awareness paper of 100 questions in 90 minutes, with +1 for a right answer and −0.25 for a wrong one. The plan was drawn by probability from the 2018, 2021 and 2025 papers (2018 counts half) and the official syllabus, so Polity, Modern History, Defence and Environment come up most. Every question is the next angle of a family the examiner has already used, and none repeats a question of the earlier GS mocks.",
        "Four questions are exact past questions (2025 Q33, 2025 Q82, 2025 Q1 and 2025 Q40). About a quarter is news from 2025 and 2026, always tied to a fact that stays true. Every explanation says why the answer is right, which past question it grew from, and the neighbouring facts that may come next.",
    ],
)

Q = []
def add(s, q, o, e, k="one", n=False, c=False, a=None, **x):
    d = dict(s=s, q=q, o=o, e=e, k=k, n=n, c=c, a=a); d.update(x); Q.append(d)

GN, HIS, POL, WG, IG, OD, GOV, ECO, DEF, SCI, ENV, INS = ("General News", "Modern History", "Polity", "World Geography",
    "India Geography", "Odisha", "Governance", "Economy", "Defence", "Science & Tech", "Environment", "Institutions")

# ---------------------------------------------------------------- (a)(b) General News (11)
add(GN, "The Chenab Rail Bridge, opened in June 2025 as the world's highest railway arch bridge, is part of which rail project?",
    ["Udhampur–Srinagar–Baramulla Rail Link", "Mumbai–Ahmedabad High Speed Rail", "Western Dedicated Freight Corridor", "Bilaspur–Manali–Leh rail line"],
    "Why: The Chenab bridge stands about 359 m above the river in Reasi district of Jammu and Kashmir. It is the key bridge of the Udhampur–Srinagar–Baramulla Rail Link (USBRL), which gave the Kashmir valley a rail link to the rest of India in 2025. Grew from: 2018 Q17 (the two ends of the first bullet train, Mumbai and Ahmedabad). Family: big projects with their place: Anji Khad (India's first cable-stayed rail bridge, also on USBRL), New Pamban Bridge (first vertical-lift sea bridge, Tamil Nadu), Atal Setu (Mumbai sea link).")

add(GN, "Which one of the following national schemes is NOT correctly matched with the place where it was launched?",
    ["PM-KISAN – Varanasi, Uttar Pradesh (2019)", "Beti Bachao, Beti Padhao – Panipat, Haryana (2015)", "Pradhan Mantri Ujjwala Yojana – Ballia, Uttar Pradesh (2016)", "POSHAN Abhiyaan – Jhunjhunu, Rajasthan (2018)"],
    "Why: PM-KISAN (₹6,000 a year to farmer families in three instalments) was launched at Gorakhpur, Uttar Pradesh, on 24 February 2019, not at Varanasi. The other three pairs are right. Grew from: 2025 Q3 (the district where the '100 Din Beti Bachao, Beti Padhao' campaign was launched). Family: Ayushman Bharat PM-JAY was launched at Ranchi (2018), Swachh Bharat in New Delhi (2 October 2014); the examiner likes the launch place and the ministry.",
    k="not")

add(GN, "'Samudra Manthan', approved by the Union Cabinet in 2026, is a national scheme for",
    ["exploration of India's offshore areas", "cleaning rivers that flow into the sea", "deep-sea fishing by coastal villages", "building new major ports"],
    "Why: Samudra Manthan is the National Offshore Exploration Scheme, meant to search India's sea areas for oil, gas and minerals (about ₹84,000 crore in its first phase). The name comes from the churning of the ocean in the Puranas. Grew from: 2018 Q20 (the aim of a central scheme). Family: other schemes of 2026: PM Surya Sarovar Yojana (floating solar), India Semiconductor Mission 2.0, and the VB–G RAM G Act that replaced MGNREGA.",
    n=True)

add(GN, "Which country became the first in the world to bar children under 16 from having social media accounts, from 10 December 2025?",
    ["Australia", "France", "Denmark", "United Kingdom"],
    "Why: Australia's law made platforms such as Instagram, TikTok and YouTube block accounts of children under 16 from 10 December 2025. France followed in July 2026 as the first European Union country with a legal age limit (under 15). Grew from: 2025 Q49 (the first country to make AI-made child abuse material a crime). Family: 'first country to pass a law or ban': the examiner asks the country, then the age or the date.",
    n=True)

add(GN, "In August 2026 a Court of Arbitration at The Hague held that the Indus Waters Treaty is still fully in force, and India rejected the award. The treaty of 1960 was signed with the help of",
    ["the World Bank", "the United Nations Security Council", "the Soviet Union", "the Commonwealth"],
    "Why: The Indus Waters Treaty was signed at Karachi on 19 September 1960 by Jawaharlal Nehru and Ayub Khan, with the World Bank as the go-between and a signatory. It gave the eastern rivers (Ravi, Beas, Sutlej) to India and the western rivers (Indus, Jhelum, Chenab) mostly to Pakistan. India put it 'in abeyance' after the Pahalgam attack of April 2025. Trap: the Soviet Union helped with the Tashkent Declaration of 1966, not this treaty. Grew from: 2021 Q17 and 2018 Q22 (country news). Family: Simla Agreement 1972, Tashkent 1966.",
    n=True)

add(GN, "National Handloom Day is observed on 7 August because on that day in 1905",
    ["the Swadeshi Movement was launched", "the Partition of Bengal came into force", "the Indian National Congress was founded", "Gandhiji began spinning khadi at Sabarmati"],
    "Why: On 7 August 1905 a meeting at the Calcutta Town Hall began the Swadeshi Movement, a boycott of British goods and a call to use Indian cloth, as a protest against the Partition of Bengal. The first National Handloom Day was held in 2015. Trap: the Partition itself came into force on 16 October 1905. Grew from: 2025 Q22 and Q28 (dates of days) and 2025 Q99 (a national day of India). Family: National Sports Day 29 August (Dhyan Chand), National Unity Day 31 October (Patel), National Education Day 11 November (Azad).",
    k="one")

add(GN, "Police Commemoration Day (21 October) remembers ten policemen who were killed on that day in 1959 by Chinese troops at",
    ["Hot Springs, Ladakh", "Galwan valley, Ladakh", "Nathu La, Sikkim", "Tawang, Arunachal Pradesh"],
    "Why: On 21 October 1959 a CRPF patrol was ambushed by Chinese troops at Hot Springs in Ladakh and ten men died. Every year on 21 October all police forces of India honour their dead; the National Police Memorial in New Delhi opened in 2018. Trap: Galwan was the clash of June 2020. Grew from: 2025 Q22, Q28 and Q72 (dates and meaning of days). Family: Army Day 15 January, Air Force Day 8 October, Navy Day 4 December (Operation Trident, 1971).")

add(GN, "Consider the following statements about Ayushman Bharat – Pradhan Mantri Jan Arogya Yojana (PM-JAY):\n1. It gives a health cover of up to ₹5 lakh per family per year.\n2. It is fully paid for by the Union Government, and the States pay nothing.\n3. Since October 2024 all citizens aged 70 and above are covered, whatever their income.\nWhich of the statements given above are correct?",
    S3,
    "Why: 1 is right: the cover is ₹5 lakh per family per year for hospital care. 2 is wrong: the cost is shared, usually 60:40 between the Union and a State (90:10 in the North-East and Himalayan States). 3 is right: from 29 October 2024 every person aged 70 or more can get the Ayushman Vay Vandana card. Grew from: 2018 Q20 (POSHAN Abhiyaan). Family: PM-JAY began at Ranchi on 23 September 2018 and is run by the National Health Authority under the Health Ministry.",
    k="stmt", a=2)

add(GN, "After United States forces captured President Nicolás Maduro in Caracas on 3 January 2026, who became the acting President of Venezuela?",
    ["Delcy Rodríguez", "María Corina Machado", "Edmundo González Urrutia", "Diosdado Cabello"],
    "Why: Delcy Rodríguez, who was Maduro's Vice President, took over as acting president. Trap: María Corina Machado is the opposition leader who won the Nobel Peace Prize 2025, and Edmundo González was the opposition candidate of 2024. Grew from: 2018 Q7 (the new Prime Minister of Italy). Family: new leaders of 2026: Tarique Rahman (Bangladesh), Balendra Shah (Nepal), Péter Magyar (Hungary), Lula's fourth term (Brazil). Capital of Venezuela: Caracas.",
    n=True)

add(GN, "In April 2026 India signed a free trade agreement that kept dairy products out of its scope. With which country was it signed?",
    ["New Zealand", "Oman", "United Kingdom", "Australia"],
    "Why: The India–New Zealand FTA was signed on 27 April 2026 and came into force on 20 October 2026. India kept dairy out to protect its milk farmers, since New Zealand is a big dairy exporter. Grew from: 2021 Q3 (partner country of an Indian programme, Israel). Family: India–UK trade agreement (signed July 2025, in force July 2026), India–Oman CEPA (Muscat, December 2025), India–Australia ECTA (2022), India–EU talks concluded in January 2026.",
    n=True)

add(GN, "Deepavali joined UNESCO's list of the Intangible Cultural Heritage of Humanity in December 2025. Match List I (another element of India on the same list) with List II (State):\nList I: a. Garba  b. Ramman  c. Mudiyettu  d. Sankirtana\nList II: 1. Manipur  2. Kerala  3. Uttarakhand  4. Gujarat",
    [M(4, 3, 2, 1), M(4, 2, 3, 1), M(3, 4, 2, 1), M(4, 3, 1, 2)],
    "Why: Garba is the circle dance of Gujarat (listed 2023). Ramman is a religious festival and masked ritual theatre of Garhwal, Uttarakhand (2009). Mudiyettu is a ritual dance drama of Kerala about the goddess Kali (2010). Sankirtana is the ritual singing, drumming and dancing of Manipur (2013). Grew from: 2021 Q6 (State and its folk dance). Family: other Indian entries: Kumbh Mela (2017), Durga Puja in Kolkata (2021), Yoga (2016), Chhau (2010), Kalbelia of Rajasthan (2010), Navroz (2016).",
    k="match", n=True)

# ---------------------------------------------------------------- (c) Modern History (12)
add(HIS, "The 'portfolio system', begun by Lord Canning, was given legal recognition by which Act?",
    ["Indian Councils Act, 1861", "Government of India Act, 1858", "Charter Act, 1853", "Indian Councils Act, 1892"],
    "Why: The Indian Councils Act of 1861 recognised Canning's portfolio system, in which each member of the Viceroy's council looked after one department. It also brought Indians into the law-making council as nominated members and let the Viceroy issue ordinances. Grew from: 2018 Q28 (Act that brought elections, 1892) and 2025 Q38 (provincial autonomy, 1935). Family: what each Act first did: 1773 Supreme Court at Calcutta, 1784 Board of Control, 1833 Governor-General of India, 1853 open competition, 1909 separate electorates, 1919 diarchy, 1935 federal court.")

add(HIS, "Match List I (Viceroy) with List II (event in his time):\nList I: a. Lord Dufferin  b. Lord Lansdowne  c. Lord Minto II  d. Lord Chelmsford\nList II: 1. Founding of the Muslim League  2. First session of the Indian National Congress  3. Rowlatt Act and the Jallianwala Bagh massacre  4. Drawing of the Durand Line",
    [M(2, 4, 1, 3), M(4, 2, 1, 3), M(2, 4, 3, 1), M(2, 1, 4, 3)],
    "Why: Dufferin was Viceroy when the Congress first met at Bombay in 1885. Lansdowne's time saw the Indian Councils Act 1892 and the Durand Line with Afghanistan (1893). Minto II saw the Muslim League founded at Dacca (1906) and the Morley–Minto reforms (1909). Chelmsford saw the Rowlatt Act and Jallianwala Bagh (1919). Grew from: 2018 Q86 and 2025 Q10 (Ilbert Bill under Ripon). Family: Lytton – Vernacular Press Act and Delhi Durbar (1877); Curzon – Partition of Bengal (1905); Hardinge II – capital to Delhi (1911).",
    k="match")

add(HIS, "Which one of the following pairs (centre of the Revolt of 1857 – British officer who recaptured it) is NOT correct?",
    ["Kanpur – Sir Hugh Rose", "Delhi – John Nicholson", "Lucknow – Sir Colin Campbell", "Jagdishpur (Arrah) – William Taylor and Vincent Eyre"],
    "Why: Kanpur was recovered by Henry Havelock and later held by Sir Colin Campbell. Sir Hugh Rose led the Central India campaign and took Jhansi and Gwalior from Rani Lakshmibai. The other pairs are right: Nicholson fell while storming Delhi in September 1857, and Campbell retook Lucknow in March 1858. Grew from: 2025 Q75 (centres and Indian leaders, wrongly matched). Family: Indian leaders: Bakht Khan (Delhi), Nana Sahib (Kanpur), Begum Hazrat Mahal (Lucknow), Kunwar Singh (Jagdishpur), Surendra Sai (Sambalpur, Odisha).",
    k="not")

add(HIS, "The Hartog Committee (1929) is best known for pointing out",
    ["wastage and stagnation in primary education", "the need for a teaching university at Calcutta", "the need for basic education through a craft", "a 10+2+3 pattern of school and college"],
    "Why: The Hartog Committee, set up by the Simon Commission, found that many children left primary school early (wastage) or failed to move up (stagnation), so it asked for better quality rather than more schools. Trap: the Calcutta University study was the Sadler Commission (1917); basic education through craft was the Wardha scheme (1937); 10+2+3 came from the Kothari Commission (1964–66). Grew from: 2025 Q81 (order of Hartog, Hunter, Sadler, Sargent) and 2021 Q23 (Charter Act 1813).")

add(HIS, "Who introduced the Ryotwari system in the Madras Presidency, as its Governor from 1820?",
    ["Thomas Munro", "Lord Cornwallis", "John Shore", "Lord Wellesley"],
    "Why: In the Ryotwari system the government settled revenue directly with each cultivator (ryot), with no zamindar in between. Alexander Read first tried it in the Baramahal area in 1792 and Thomas Munro spread it across Madras; it later went to Bombay. Grew from: 2025 Q88 (the region of Ryotwari: Madras and Bombay). Family: Permanent Settlement 1793 (Cornwallis, Bengal and Bihar, with zamindars); Mahalwari 1822 (Holt Mackenzie, North-West, with the village as a whole).")

add(HIS, "The Landholders' Society (1838), often called the first political association of modern India, was set up at",
    ["Calcutta", "Bombay", "Madras", "Poona"],
    "Why: The Landholders' Society was formed in Calcutta in 1838 by Dwarkanath Tagore, Prasanna Kumar Tagore, Radhakanta Deb and others to protect the interests of the zamindars. It joined the Bengal British India Society in 1851 to form the British Indian Association. Grew from: 2025 Q57 (founder of the Central National Mohammedan Association). Family: Indian Association 1876 (Surendranath Banerjee and Ananda Mohan Bose), East India Association 1866 (Dadabhai Naoroji, London), Poona Sarvajanik Sabha 1870 (M. G. Ranade), Madras Mahajana Sabha 1884.")

add(HIS, "Which one of the following pairs (ruler – state he founded or ruled in the 18th century) is NOT correctly matched?",
    ["Saadat Khan Burhan-ul-Mulk – Hyderabad", "Ranjit Singh – Punjab", "Haidar Ali – Mysore", "Murshid Quli Khan – Bengal"],
    "Why: Saadat Khan Burhan-ul-Mulk founded the state of Awadh (1722). Hyderabad was founded by Nizam-ul-Mulk Asaf Jah (1724). The other pairs are right. Grew from: 2021 Q21 and Q22 (rulers and their states) and 2021 Q25 (the Bhangi misl of Punjab). Family: these 'successor states' rose as the Mughal empire weakened; Wellesley's Subsidiary Alliance (1798) was first accepted by Hyderabad, and Dalhousie took Awadh in 1856 on the ground of misrule.",
    k="not")

add(HIS, "Who among the following was NOT among the founders of the Communist Party of India at Tashkent in October 1920?",
    ["S. A. Dange", "M. N. Roy", "Abani Mukherji", "M. P. T. Acharya"],
    "Why: The émigré CPI was formed at Tashkent on 17 October 1920 by M. N. Roy, Evelyn Trent-Roy, Abani Mukherji, Rosa Fitingof, M. P. T. Acharya, Mohammad Ali and Mohammad Shafiq. S. A. Dange worked in Bombay; he was an accused in the Kanpur Bolshevik Conspiracy Case (1924) and the Meerut Conspiracy Case (1929). Grew from: 2025 Q97 (who was NOT in the Labour Swaraj Party) and 2025 Q58 (left bodies and people). Family: CPI conference at Kanpur 1925, AITUC 1920 (Lala Lajpat Rai), Congress Socialist Party 1934, All India Kisan Sabha 1936.",
    k="not")

add(HIS, "In December 1943 Subhas Chandra Bose hoisted the national flag at Port Blair and renamed the Andaman and Nicobar Islands as",
    ["Shaheed and Swaraj Islands", "Azad and Hind Islands", "Netaji and Jai Hind Islands", "Vijay and Bharat Islands"],
    "Why: The Japanese handed the islands to Bose's Azad Hind Government, and on 30 December 1943 he raised the tricolour at Port Blair and named the Andamans 'Shaheed' (martyr) and the Nicobars 'Swaraj' (self-rule). In December 2018 Ross Island, Neil Island and Havelock Island were renamed Netaji Subhash Chandra Bose Dweep, Shaheed Dweep and Swaraj Dweep. Grew from: 2018 Q33 (Azad Hind Government at Singapore, 21 October 1943). Family: first INA by Mohan Singh (1942), 'Delhi Chalo', Red Fort trials (1945).")

add(HIS, "The motto 'Satyameva Jayate', written below the national emblem, is taken from the",
    ["Mundaka Upanishad", "Rig Veda", "Katha Upanishad", "Bhagavad Gita"],
    "Why: 'Satyameva Jayate' (truth alone triumphs) is a line of the Mundaka Upanishad. It was adopted with the State Emblem, which is based on the Lion Capital of Ashoka at Sarnath, on 26 January 1950. Grew from: 2021 Q26 ('ekam sat, vipraha bahudha vadanti' comes from the Rig Veda) and 2018 Q82 (Meru as the centre of the universe). Family: 'Vasudhaiva Kutumbakam' is from the Maha Upanishad; the Gayatri Mantra is from the Rig Veda; 'Asato ma sadgamaya' is from the Brihadaranyaka Upanishad.")

add(HIS, "The Satyabadi Bana Vidyalaya, an open-air school started in 1909 at Sakhigopal near Puri, was founded by",
    ["Gopabandhu Das", "Madhusudan Das", "Fakir Mohan Senapati", "Harekrushna Mahtab"],
    "Why: Utkalmani Gopabandhu Das set up the school in 1909 on the lines of the ancient gurukula, under trees, to build national feeling and service. Teachers such as Nilakantha Das, Godavarish Mishra and Krupasindhu Mishra made it the 'Satyabadi school' of Odia writing. He also started the paper 'The Samaja' (1919). Grew from: 2025 Q96 (statements about Lala Lajpat Rai) and the titles family. Family: Madhusudan Das (Utkal Gourav, Utkal Sammilani 1903), Fakir Mohan Senapati (father of modern Odia prose).")

add(HIS, "The Mahalwari system of land revenue, in which revenue was settled with the village as a whole, was proposed in 1822 by",
    ["Holt Mackenzie", "Thomas Munro", "Alexander Read", "Lord Cornwallis"],
    "Why: Holt Mackenzie's plan (Regulation VII of 1822) settled revenue with the 'mahal' (village or estate) through its headmen, in the North-Western Provinces, parts of Central India and Punjab. R. M. Bird and James Thomason later revised it (1833). Grew from: 2025 Q88 (Ryotwari region). Family: three systems, three men: Permanent Settlement – Cornwallis (1793); Ryotwari – Read and Munro (Madras, Bombay); Mahalwari – Holt Mackenzie. The examiner may ask any pair as NOT correctly matched.")

# ---------------------------------------------------------------- (d) Polity (14)
add(POL, "Match List I (part of a State Legislative Council) with List II (share or number):\nList I: a. Members elected by local bodies  b. Members elected by graduates  c. Members nominated by the Governor  d. Least total strength of a Council\nList II: 1. One-third  2. One-twelfth  3. 40  4. One-sixth",
    [M(1, 2, 4, 3), M(2, 1, 4, 3), M(1, 4, 2, 3), M(1, 2, 3, 4)],
    "Why: Under Article 171, one-third of a Council is elected by local bodies, one-third by the MLAs, one-twelfth by graduates, one-twelfth by teachers, and one-sixth is nominated by the Governor. A Council may not be smaller than 40 or larger than one-third of the Assembly. Grew from: 2021 Q35 (who can abolish a Council: Parliament) and 2025 Q33 (minimum age 30). Family: six States have one (Andhra Pradesh, Telangana, Uttar Pradesh, Bihar, Maharashtra, Karnataka); one-third retire every two years; Article 169 for creating or abolishing.",
    k="match")

add(POL, "What is the minimum age limit prescribed for the membership of the State Legislative Council?",
    ["30 years", "21 years", "25 years", "35 years"],
    "Why: Article 173 sets 30 years for the Legislative Council and 25 years for the Legislative Assembly. This is the exact 2025 question. Family: 25 for the Lok Sabha, 30 for the Rajya Sabha, 35 for President and Vice-President, 21 for a panchayat member; Parliament (Article 169) creates or abolishes a Council when the Assembly asks by a special majority (asked in 2021 Q35).",
    src="2025 Q33")

add(POL, "Which of the following Articles are related to the Right to Religion?",
    ["Articles 25 to 28", "Articles 14 to 18", "Articles 19 to 22", "Articles 29 and 30"],
    "Why: Articles 25 to 28 give freedom of religion: conscience and practice (25), managing religious affairs (26), no tax for promoting a religion (27), and no religious instruction in schools run wholly by the State (28). This is the exact 2025 question. Family: 14–18 equality, 19–22 freedom, 23–24 against exploitation, 29–30 cultural and educational rights of minorities, 32 constitutional remedies.",
    src="2025 Q82")

add(POL, "Which one of the following pairs (right read into Article 21 – Supreme Court case) is NOT correctly matched?",
    ["Right to die with dignity (passive euthanasia) – Maneka Gandhi (1978)", "Right to privacy – K. S. Puttaswamy (2017)", "Right to livelihood – Olga Tellis (1985)", "Right to speedy trial – Hussainara Khatoon (1979)"],
    "Why: Passive euthanasia and living wills were allowed in Common Cause v. Union of India (2018). The Maneka Gandhi case (1978) said a law that takes away life or liberty must be 'just, fair and reasonable'. The other pairs are right. Grew from: 2018 Q16 (privacy judgment) and 2025 Q6 (maternity leave read as part of Article 21). Family: rights to shelter, clean environment, education (now Article 21A), and in 2026 menstrual health and hygiene; Articles 20 and 21 cannot be suspended in an Emergency.",
    k="not")

add(POL, "Under which Article can a High Court issue writs not only to enforce Fundamental Rights but also 'for any other purpose'?",
    ["Article 226", "Article 32", "Article 227", "Article 136"],
    "Why: Article 226 lets a High Court issue writs for Fundamental Rights and also for other legal rights ('for any other purpose'), so its writ power is wider than the Supreme Court's. Article 32 is only for Fundamental Rights, but it is itself a Fundamental Right. Trap: Article 227 is the High Court's power of superintendence over lower courts; Article 136 is special leave to appeal. Grew from: 2018 Q38 (mandamus). Family: the five writs: habeas corpus, mandamus, prohibition, certiorari, quo warranto.")

add(POL, "Which one of the following statements about the National Human Rights Commission (NHRC) is NOT correct?",
    ["It can itself punish a person found guilty of violating human rights.", "It was set up under the Protection of Human Rights Act, 1993.", "Its Chairperson must have been a Chief Justice of India or a judge of the Supreme Court.", "Members of a State Human Rights Commission are appointed by the Governor."],
    "Why: The NHRC can inquire, visit jails and recommend compensation or action, but it cannot punish anyone; its advice is not binding. The other three are right: it is a statutory body of 1993, the 2019 amendment allows a former CJI or a former Supreme Court judge as Chairperson, and the Governor appoints a State commission after a committee led by the Chief Minister recommends. Grew from: 2018 Q65, 2021 Q51 and 2025 Q87 (eligibility, first chairman, selection committee). Family: term 3 years or 70 years; first chairman Ranganath Misra.",
    k="not")

add(POL, "Which one of the following statements about the Public Service Commissions is NOT correct?",
    ["The UPSC presents its annual report to the Prime Minister.", "Members of the UPSC are appointed by the President.", "Members of a State Public Service Commission are appointed by the Governor.", "A member of a State Public Service Commission can be removed only by the President."],
    "Why: Under Article 323 the UPSC gives its annual report to the President, who lays it before Parliament (a State PSC reports to the Governor). The rest are right: the Governor appoints State PSC members but only the President can remove them, after a Supreme Court inquiry for misbehaviour. Grew from: 2021 Q38 (bar on later jobs) and 2025 Q56 (Joint State PSC by an Act of Parliament). Family: Articles 315–323; term six years or 65 (UPSC) and 62 (State PSC).",
    k="not")

add(POL, "Article 45 of the Constitution, as changed by the 86th Amendment (2002), now directs the State to provide",
    ["early childhood care and education for all children until they are six", "free and compulsory education for children aged 6 to 14", "free legal aid to the poor", "a uniform civil code for all citizens"],
    "Why: The 86th Amendment moved free and compulsory education for ages 6 to 14 into the Fundamental Rights as Article 21A, and rewrote Article 45 (a Directive Principle) for early childhood care and education below six. It also added a Fundamental Duty on parents (Article 51A(k)). Trap: free legal aid is Article 39A and the uniform civil code is Article 44. Grew from: 2025 Q78 (Article 51, foreign policy) and 2025 Q98 (a principle added in 1976). Family: Article 40 panchayats, 48A environment, 50 separation of judiciary from executive.")

add(POL, "Which of the following subjects was NOT moved from the State List to the Concurrent List by the 42nd Amendment (1976)?",
    ["Agriculture", "Education", "Forests", "Weights and measures"],
    "Why: The 42nd Amendment moved five subjects to the Concurrent List: education, forests, weights and measures, protection of wild animals and birds, and administration of justice (except the Supreme Court and High Courts). Agriculture is still in the State List. Grew from: 2018 Q39 (which subject was moved: education) and 2021 Q50 (economic planning is in the Concurrent List). Family: residuary powers lie with the Union (Article 248); Article 249 lets the Rajya Sabha allow Parliament to make a law on a State subject.",
    k="not")

add(POL, "Which Article of the Constitution defines a Money Bill?",
    ["Article 110", "Article 109", "Article 112", "Article 117"],
    "Why: Article 110 lists what makes a Bill a Money Bill (taxes, borrowing, the Consolidated Fund and so on), and says the Speaker's decision on it is final. Article 109 gives the special procedure (only in the Lok Sabha, 14 days for the Rajya Sabha). Article 112 is the annual financial statement (budget) and Article 117 covers Financial Bills. Grew from: 2025 Q19 (Rajya Sabha's suggestions on a Money Bill) and 2018 Q37 (vote on account). Family: no joint sitting on a Money Bill; it needs the President's recommendation to be introduced.")

add(POL, "The Advocate General of a State is appointed by the Governor under which Article?",
    ["Article 165", "Article 76", "Article 148", "Article 124"],
    "Why: Article 165 provides for the Advocate General, the State's top law officer, who must be qualified to be a High Court judge and holds office during the Governor's pleasure. Like the Attorney General, he can speak in the State Legislature but cannot vote. Trap: Article 76 is the Attorney General of India, Article 148 the CAG, Article 124 the Supreme Court. Grew from: 2021 Q40 (who appoints the CAG: the President). Family: CAG term six years or 65, removed like a Supreme Court judge; AG of India: qualified as a Supreme Court judge.")

add(POL, "Which of the following is NOT an All India Service?",
    ["Indian Foreign Service", "Indian Administrative Service", "Indian Police Service", "Indian Forest Service"],
    "Why: There are three All India Services: IAS, IPS and the Indian Forest Service (1966). Their officers are recruited by the Union but serve in the States. The Indian Foreign Service is a Central Service (Group A) that serves only the Union. Grew from: 2021 Q45 (a new All India Service is created after a Rajya Sabha resolution under Article 312). Family: Article 312 needs two-thirds of the Rajya Sabha members present and voting; Article 311 protects civil servants; Sardar Patel is the father of the All India Services.")

add(POL, "Article 23 of the Constitution prohibits",
    ["traffic in human beings and begar (forced labour)", "untouchability in any form", "employment of children below 14 in factories and mines", "titles, except military and academic distinctions"],
    "Why: Article 23 bans buying and selling of people and 'begar', work taken without pay. Articles 23 and 24 form the Right against Exploitation. Trap: untouchability is Article 17, titles Article 18, child labour Article 24. Grew from: 2021 Q33 (Article 21A) and 2025 Q82 (Articles of the Right to Religion). Family: rights only for citizens (15, 16, 19, 29, 30); Article 20 and 21 cannot be suspended in an Emergency; Right to Property moved to Article 300A by the 44th Amendment.")

add(POL, "The procedure for amending the Constitution was borrowed from the Constitution of",
    ["South Africa", "the USA", "Ireland", "Canada"],
    "Why: The idea of an amendment procedure, and the election of Rajya Sabha members, came from South Africa. Grew from: 2021 Q31 (single citizenship from Britain) and 2025 Q17 (nomination of Rajya Sabha members from Ireland). Family: USA – Fundamental Rights, judicial review, removal of judges; Ireland – Directive Principles, way of electing the President; Canada – federation with a strong Centre, residuary powers; Australia – Concurrent List, joint sitting; Germany (Weimar) – suspension of rights in an Emergency; USSR – Fundamental Duties; Japan – procedure established by law; France – liberty, equality, fraternity.")

# ---------------------------------------------------------------- (e) World Geography (8)
add(WG, "Match List I (climate type) with List II (region where it is found):\nList I: a. Mediterranean  b. Equatorial  c. Tropical monsoon  d. Temperate steppe\nList II: 1. Bangladesh  2. Kazakhstan  3. Central Chile  4. Congo basin",
    [M(3, 4, 1, 2), M(4, 3, 1, 2), M(3, 4, 2, 1), M(3, 1, 4, 2)],
    "Why: Mediterranean climate (dry summers, rainy winters) is found on the west sides of continents near 30°–40°, as in central Chile, California and the Mediterranean lands. Equatorial climate (hot and wet all year) covers the Congo and Amazon basins. Tropical monsoon climate covers South Asia, including Bangladesh. Temperate grassland (steppe) climate covers the dry interior of Eurasia such as Kazakhstan. Grew from: 2021 Q69 (Köppen symbols matched with climates). Family: Köppen letters: A tropical, B dry, C warm temperate, D cold, E polar.",
    k="match")

add(WG, "Which of the following seas has the lowest salinity?",
    ["Baltic Sea", "Red Sea", "Mediterranean Sea", "Arabian Sea"],
    "Why: The Baltic Sea gets a lot of fresh water from rivers and melting snow, loses little to evaporation in its cool climate, and is almost shut off from the open ocean, so its water is only slightly salty. The Red Sea is the saltiest open sea (heat, little rain, no big rivers). Grew from: 2018 Q83 (the sea with no coastline: Sargasso) and 2025 Q70 (the deepest part: Challenger Deep). Family: the Dead Sea and Lake Van are far saltier lakes; average ocean salinity is about 35 parts per thousand.")

add(WG, "In Köppen's classification of climates, the symbol 'ET' stands for",
    ["Tundra climate", "Ice cap climate", "Taiga climate", "Steppe climate"],
    "Why: In Köppen's scheme 'E' is the polar group. 'ET' is tundra, where the warmest month is between 0 °C and 10 °C, so only mosses, lichens and small shrubs grow. Trap: 'EF' is the ice cap (no month above 0 °C); taiga is a 'D' cold climate (Dfc) and steppe is 'BS'. Grew from: 2021 Q69 (BWk, BWh, BSh, BSk). Family: 'Af' tropical rainforest, 'Aw' savanna, 'Cs' Mediterranean, 'Cwg' the Ganga plain.")

add(WG, "Match List I (layer of the atmosphere) with List II (its feature):\nList I: a. Troposphere  b. Stratosphere  c. Mesosphere  d. Ionosphere\nList II: 1. Almost all weather happens here  2. Reflects radio waves back to the Earth  3. Meteors burn up here  4. Calm air, good for flying jet aircraft",
    [M(1, 4, 3, 2), M(4, 1, 3, 2), M(1, 4, 2, 3), M(1, 3, 4, 2)],
    "Why: The troposphere, the lowest layer, holds most water vapour and dust, so clouds, rain and storms happen there. The stratosphere above it has calm air and the ozone layer, so jets fly in its lower part. Meteors burn up in the mesosphere, the coldest layer. The ionosphere, in the thermosphere, has charged particles that bounce radio waves back. Grew from: 2018 Q41 (largest gas, nitrogen) and 2025 Q85 (composition of the air). Family: order from the ground: troposphere, stratosphere, mesosphere, thermosphere, exosphere.",
    k="match")

add(WG, "The Volga, the longest river of Europe, flows into the",
    ["Caspian Sea", "Black Sea", "Baltic Sea", "White Sea"],
    "Why: The Volga rises in the Valdai Hills north-west of Moscow, flows about 3,500 km across Russia and ends in a large delta in the Caspian Sea, which has no outlet to the ocean. Trap: the Danube and the Dnieper flow into the Black Sea. Grew from: 2025 Q80 (the Congo crosses the Equator twice) and 2021 Q66 (Mississippi's bird-foot delta). Family: Limpopo crosses the Tropic of Capricorn twice; the Nile is the longest river; the Amazon has the largest basin; the Danube flows through four capitals.")

add(WG, "The Great Barrier Reef, the largest coral reef system in the world, lies in which sea?",
    ["Coral Sea", "Tasman Sea", "Arafura Sea", "Timor Sea"],
    "Why: The Great Barrier Reef runs for about 2,300 km off the coast of Queensland, north-east Australia, in the Coral Sea. Corals grow in warm, clear, shallow sea water, and warmer seas cause coral bleaching. Trap: the Tasman Sea lies between Australia and New Zealand. Grew from: 2018 Q80 (Ninety East Ridge) and 2021 Q70 (widest continental shelf). Family: India's coral areas: Gulf of Mannar, Gulf of Kachchh, Lakshadweep (atolls), Andaman and Nicobar.")

add(WG, "Which type of volcano has gentle slopes built from runny basalt lava, like Mauna Loa in Hawaii?",
    ["Shield volcano", "Composite (strato) volcano", "Cinder cone", "Caldera"],
    "Why: Runny (basic) basalt lava flows far before it cools, so it builds a wide, low dome like a warrior's shield; Mauna Loa and Kilauea in Hawaii are examples. Composite volcanoes such as Fuji and Vesuvius are steep cones of layers of thick lava and ash, and erupt violently. Grew from: 2021 Q65 (region with most active volcanoes) and 2025 Q43 (Lewotobi Laki-Laki, Indonesia). Family: Ring of Fire around the Pacific; Barren Island (Andaman) is India's only active volcano.")

add(WG, "Kanlaon, a volcano that erupted several times in 2026, is on Negros island in",
    ["Philippines", "Indonesia", "Japan", "Papua New Guinea"],
    "Why: Kanlaon (Canlaon) is one of the most active volcanoes of the Philippines, on Negros island, and part of the Pacific Ring of Fire. It erupted in February, March, July and October 2026. Grew from: 2025 Q43 (Mount Lewotobi Laki-Laki, an active volcano of Indonesia). Family: volcanoes in the news and their country: Taal and Mayon (Philippines), Etna (Italy), Merapi (Indonesia), Sakurajima (Japan); the Venezuela twin earthquakes of June 2026.",
    n=True)

# ---------------------------------------------------------------- (f) India Geography (5)
add(IG, "Which one of the following mountain passes is NOT correctly matched with its State or Union Territory?",
    ["Niti Pass – Himachal Pradesh", "Banihal – Jammu and Kashmir", "Khardung La – Ladakh", "Bum La – Arunachal Pradesh"],
    "Why: Niti Pass is in Chamoli district of Uttarakhand, on the route to Tibet. Banihal crosses the Pir Panjal range between Jammu and the Kashmir valley; Khardung La is north of Leh on the road to the Nubra valley; Bum La is near Tawang on the China border. Grew from: 2021 Q80 (pass that does not belong to its State). Family: Shipki La (Himachal, Sutlej enters India), Nathu La and Jelep La (Sikkim), Lipulekh and Mana (Uttarakhand), Zoji La (Ladakh), Rohtang (Himachal).",
    k="not")

add(IG, "Which of the following rivers is a tributary of the Krishna?",
    ["Tungabhadra", "Wainganga", "Hasdeo", "Hemavati"],
    "Why: The Tungabhadra, formed by the Tunga and the Bhadra in Karnataka, joins the Krishna near Kurnool; the Bhima is another tributary of the Krishna. Trap: the Wainganga joins the Godavari (through the Pranhita), the Hasdeo joins the Mahanadi, and the Hemavati joins the Kaveri. Grew from: 2021 Q72 (rivers rising in the Maikal range: Narmada, Son, not Tapi). Family: the Mahanadi rises near Sihawa (Chhattisgarh); the Godavari at Trimbakeshwar; the Krishna near Mahabaleshwar; the Kaveri at Talakaveri.")

add(IG, "Which one of the following pairs (place – rainfall feature) is NOT correct?",
    ["Jaisalmer (Rajasthan) – more than 200 cm of rain a year", "Mawsynram (Meghalaya) – one of the wettest places on Earth", "Leh (Ladakh) – very little rain; a cold desert", "Chennai – gets most of its rain from October to December"],
    "Why: Western Rajasthan, around Jaisalmer, gets only about 20 cm of rain a year, because the monsoon winds there are dry and the Aravallis run parallel to them. The other pairs are right: Mawsynram lies on the funnel-shaped south slopes of the Khasi hills; Leh sits in the rain shadow of the Himalaya; Tamil Nadu's coast gets its main rain from the retreating (north-east) monsoon. Grew from: 2021 Q75 and Q79 (climatic regions and monsoon fluctuation). Family: mango showers (Kerala, Karnataka), kal baisakhi (West Bengal), loo (northern plains).",
    k="not")

add(IG, "Match List I (State) with List II (the only country it shares a border with):\nList I: a. Himachal Pradesh  b. Bihar  c. Meghalaya  d. Nagaland\nList II: 1. Nepal  2. Myanmar  3. China  4. Bangladesh",
    [M(3, 1, 4, 2), M(1, 3, 4, 2), M(3, 1, 2, 4), M(3, 4, 1, 2)],
    "Why: Himachal Pradesh touches only China (Tibet), Bihar only Nepal, Meghalaya only Bangladesh, and Nagaland only Myanmar. Grew from: 2025 Q67 (States on international borders: West Bengal with Bhutan and Bangladesh, Uttarakhand with China and Nepal, Gujarat with Pakistan). Family: the longest border is with Bangladesh (about 4,096 km, touched by West Bengal, Assam, Meghalaya, Tripura, Mizoram); Sikkim touches China, Nepal and Bhutan; Arunachal touches Bhutan, China and Myanmar.",
    k="match")

add(IG, "Which one of the following pairs (tree – forest type in which it is found) is NOT correctly matched?",
    ["Ebony and mahogany – thorn forest", "Teak and sal – tropical deciduous forest", "Sundari – mangrove (tidal) forest", "Deodar – Himalayan (montane) forest"],
    "Why: Ebony, mahogany and rosewood grow in tropical evergreen forests of heavy-rain areas such as the Western Ghats and the North-East. Thorn forests (Rajasthan, Gujarat) have acacia, babool and khair. The other pairs are right: teak and sal are the main trees of the monsoon (deciduous) forests, sundari gives the Sundarbans their name, and deodar is a Himalayan conifer. Grew from: 2021 Q73 (tropical deciduous forests cover the largest area). Family: Bhitarkanika in Odisha is India's second-largest mangrove forest.",
    k="not")

# ---------------------------------------------------------------- (f) Odisha (4)
add(OD, "The coastal plain of Odisha forms which part of India's Eastern Coastal Plain?",
    ["Utkal Plain", "Northern Circars", "Coromandel Coast", "Konkan Coast"],
    "Why: The Eastern Coastal Plain is divided into the Utkal Plain (Odisha), the Northern Circars (Andhra Pradesh) and the Coromandel Coast (Tamil Nadu). The Utkal Plain includes the deltas of the Mahanadi, Brahmani and Baitarani and the Chilika lake. Trap: the Konkan is on the west coast. Grew from: 2025 Q16 (the Hexadeltaic region) and 2025 Q60 (hill ranges from north to south). Family: Odisha's four physical regions: coastal plain, central tableland, northern plateau and the Eastern Ghats; highest peak Deomali (Koraput).")

add(OD, "Which one of the following schemes in Odisha's Budget 2026-27 is NOT correctly matched with its aim?",
    ["Mission PoWaR – ports and waterways", "Subhadra – women", "Samrudha Krushaka – farmers", "Gopabandhu Jan Arogya Yojana – health cover"],
    "Why: Mission PoWaR stands for Power, Water and Roads, to reach every revenue village. The other pairs are right: Subhadra gives money to women, Samrudha Krushaka supports farmers, and Gopabandhu Jan Arogya Yojana is the State's health cover. The budget (about ₹3.10 lakh crore) was presented on 20 February 2026 by Chief Minister Mohan Charan Majhi, who holds Finance. Grew from: 2025 Q25 (Net Zero Vision for Bhubaneswar with the UK). Family: the semiconductor MoU with Intel and 3D Glass Solutions (Info Valley, June 2026), the Upper Indravati pumped storage project (Kalahandi).",
    k="not", n=True)

add(OD, "In Odisha, saline and saline-alkaline soils are found mainly in",
    ["the coastal districts such as Balasore, Bhadrak, Kendrapara and Jagatsinghpur", "the western districts such as Bargarh and Balangir", "the Eastern Ghats districts such as Koraput and Rayagada", "the northern plateau districts such as Mayurbhanj and Keonjhar"],
    "Why: Sea water floods the low coastal belt during cyclones and high tides, and salt also rises from shallow salty groundwater, so the coastal districts have saline soils. Red and laterite soils cover most of the uplands. Grew from: 2021 Q78 (Ranga Mati and Rugidia belong to the laterite group). Family: red soil covers the largest area of Odisha; deltaic alluvial soil lies on the coast; black soil occurs in patches in the west and south.")

add(OD, "Match List I (place in Odisha) with List II (mineral it is known for):\nList I: a. Chhatrapur (Ganjam)  b. Daitari (Keonjhar)  c. Biramitrapur (Sundargarh)  d. Titlagarh (Balangir)\nList II: 1. Graphite  2. Iron ore  3. Beach-sand minerals such as ilmenite and monazite  4. Limestone and dolomite",
    [M(3, 2, 4, 1), M(2, 3, 4, 1), M(3, 2, 1, 4), M(3, 4, 2, 1)],
    "Why: The beach sands of Chhatrapur in Ganjam are mined by IREL (OSCOM) for ilmenite, rutile, zircon and monazite. Daitari in Keonjhar has iron ore; Biramitrapur in Sundargarh supplies limestone and dolomite for steel and cement; Titlagarh in Balangir has graphite. Grew from: 2025 Q79 (monazite, chromite, limestone and copper with their places). Family: Sukinda (Jajpur) – chromite and nickel; Panchpatmali (Koraput) – bauxite; Talcher (Angul) – coal; Joda–Barbil (Keonjhar) – iron and manganese.",
    k="match")

# ---------------------------------------------------------------- (g) Governance (4)
add(GOV, "Consider the following statements:\n1. The Central Vigilance Commission was set up in 1964 on the advice of the Santhanam Committee.\n2. The First Administrative Reforms Commission (1966) recommended only a Lokpal for the Centre, and not Lokayuktas in the States.\n3. The Lokpal can inquire into the Prime Minister, with some exceptions such as national security.\nWhich of the statements given above are correct?",
    S3,
    "Why: 1 is right: the Santhanam Committee (1962–64) led to the CVC in 1964, and the CVC became statutory in 2003. 2 is wrong: the First ARC, under Morarji Desai, recommended both a Lokpal for the Centre and Lokayuktas for the States. 3 is right: under the Lokpal and Lokayuktas Act, 2013, the PM is covered, except for matters of international relations, security, public order, atomic energy and space. Grew from: 2025 Q47 (year of the Santhanam Committee) and 2021 Q42 (27 modes of corruption). Family: first Lokpal chairperson P. C. Ghose (2019).",
    k="stmt", a=2)

add(GOV, "SEVOTTAM is a",
    ["Quality Management System", "Qualified Management System", "Performance Management System", "Quantity Management System"],
    "Why: Sevottam (seva + uttam, 'excellent service') is a service-delivery quality model brought in by the Department of Administrative Reforms and Public Grievances in 2006. Its three parts are the Citizen's Charter, the grievance redress system and service delivery capability. This is the exact 2025 question. Family: Citizen's Charter in India from 1997 (not enforceable in court), CPGRAMS for online grievances, Right to Services laws (Madhya Pradesh first, 2010).",
    src="2025 Q1")

add(GOV, "Under the MGNREGA (2005), the social audit of all works in a village had to be carried out by the",
    ["Gram Sabha", "Comptroller and Auditor General", "Block Development Officer", "State Election Commission"],
    "Why: Section 17 of the Act made the Gram Sabha check all works, records and payments in its village through a social audit, so that the people themselves hold the officials to account. Social audit is a form of citizen's control over administration. Grew from: 2021 Q44 (most effective means of citizen's control) and 2018 Q49 (a tool of executive control). Family: legislative control (Question Hour, Public Accounts Committee, CAG audit), executive control (appointment and removal, budget), judicial control (writs, judicial review); MGNREGA was replaced by the VB–G RAM G Act in 2025.")

add(GOV, "Who is called the 'Father of the Civil Services in India'?",
    ["Lord Cornwallis", "Lord Macaulay", "Warren Hastings", "Lord Wellesley"],
    "Why: Cornwallis (Governor-General 1786–93) raised the pay of the Company's servants, stopped their private trade and bribes, and built a regular, well-paid civil service. Trap: Wellesley set up Fort William College (1800) to train them; Macaulay's 1854 report brought open competition, started in 1855. Grew from: 2025 Q95 (the Lee Commission, Royal Commission on the Superior Civil Services). Family: Aitchison Commission 1886, Islington 1912, Lee 1923–24 (led to the Public Service Commission of 1926); Lloyd George called the ICS the 'steel frame'.")

# ---------------------------------------------------------------- (g) Economy (7)
add(ECO, "In October 2026 the RBI raised the repo rate from 5.25% to 5.50%. What does a rise in the repo rate usually do?",
    ["It makes bank loans costlier, which helps to control inflation", "It makes bank loans cheaper, which helps to boost growth", "It increases the amount of money in the economy", "It directly lowers the government's fiscal deficit"],
    "Why: The repo rate is the rate at which the RBI lends short-term money to banks against government securities. When it rises, banks pay more for money and raise their own lending rates, so people and firms borrow and spend less, and price rises slow down. The October 2026 hike was the first of this cycle, with retail inflation above the 6% upper limit. Grew from: 2018 Q76 (the repo rate) and 2025 Q68 (what the RBI does not do). Family: reverse repo, SDF (the floor), MSF and Bank Rate, CRR, SLR; the six-member Monetary Policy Committee decides the repo rate.",
    n=True)

add(ECO, "The Reserve Bank of India was set up in 1935 on the recommendation of the",
    ["Hilton Young Commission", "Chamberlain Commission", "Babington Smith Committee", "Lee Commission"],
    "Why: The Hilton Young Commission (Royal Commission on Indian Currency and Finance, 1926) advised a central bank for India; the RBI Act of 1934 followed, and the RBI opened on 1 April 1935 in Calcutta, moving to Bombay in 1937. It was nationalised on 1 January 1949. Trap: the Chamberlain Commission (1913) and Babington Smith Committee (1919) also studied Indian currency. Grew from: 2025 Q68 (functions of the RBI). Family: first Governor Osborne Smith, first Indian Governor C. D. Deshmukh; the RBI does not regulate stock markets (SEBI does).")

add(ECO, "The Planning Commission of India was set up in March 1950 by",
    ["a resolution of the Union Cabinet", "an Article of the Constitution", "an Act of Parliament", "an order of the President under Article 263"],
    "Why: The Planning Commission was not a constitutional or statutory body; it was created by a Cabinet resolution on 15 March 1950, with Jawaharlal Nehru as its first chairman. NITI Aayog, which replaced it on 1 January 2015, was also set up by a Cabinet resolution. Grew from: 2018 Q51, 2021 Q49 and 2025 Q40 (the Rolling Plan, asked three times). Family: the First Plan (1951–56, Harrod–Domar), the Second Plan (Mahalanobis), Plan holiday 1966–69, financial inclusion in the Eleventh Plan, the last plan the Twelfth (2012–17).")

add(ECO, "Which of the following is a direct tax?",
    ["Corporation tax", "Goods and Services Tax", "Customs duty", "Excise duty"],
    "Why: A direct tax is paid by the person or company on whom it is levied and cannot be passed on, such as income tax and corporation tax (tax on company profits). GST, customs duty and excise duty are indirect taxes, collected from sellers but paid in the end by buyers in the price. Grew from: 2025 Q62 (GST unified many indirect taxes). Family: GST came by the 101st Amendment on 1 July 2017, GST Council under Article 279A, GST 2.0 from 22 September 2025 with two main rates (5% and 18%); cess and surcharge are not shared with the States.")

add(ECO, "Consider the following statements about NITI Aayog:\n1. It publishes the SDG India Index.\n2. It publishes the Export Preparedness Index.\n3. It publishes the Global Innovation Index.\nWhich of the statements given above are correct?",
    S3,
    "Why: 1 and 2 are right: NITI Aayog brings out the SDG India Index (first in 2018), the Export Preparedness Index, the India Innovation Index and the National Multidimensional Poverty Index. 3 is wrong: the Global Innovation Index is published by WIPO (the World Intellectual Property Organization). Grew from: 2025 Q52 (aim and set-up of NITI Aayog) and 2021 Q48 (NITI Aayog assesses poverty). Family: NITI was set up on 1 January 2015 by a Cabinet resolution; the PM is its chairperson; its Governing Council has all Chief Ministers.",
    k="stmt", a=0)

add(ECO, "Consider the following statements:\n1. Net National Product is Gross National Product plus depreciation.\n2. Gross National Product is Gross Domestic Product plus net factor income from abroad.\n3. GDP counts the output produced within the country's borders, by residents and foreigners alike.\nWhich of the statements given above are correct?",
    S3,
    "Why: 1 is wrong: NNP is GNP minus depreciation (the wear of machines and buildings). 2 is right: GNP adds what Indians earn abroad and takes away what foreigners earn in India. 3 is right: GDP is about place, not nationality. Grew from: 2018 Q52 (best measure of economic growth) and 2025 Q21 (services give the largest share of GDP). Family: per capita income = national income ÷ population; GDP is released by the National Statistics Office (MoSPI); the new GDP series of February 2026 uses base year 2022-23.",
    k="stmt", a=1)

add(ECO, "Which Five Year Plan introduced the concept of 'Rolling Plan' in India?",
    ["First Plan", "Second Plan", "Third Plan", "None of the above"],
    "Why: The Rolling Plan was not part of any Five Year Plan as first framed. The Janata government ended the Fifth Plan a year early and ran a Rolling Plan for 1978–80, on the idea of Gunnar Myrdal; Indira Gandhi's government dropped it in 1980. So the answer is 'None of the above'. This is the exact 2025 question. Family: asked three times from different sides: what it is (2018 Q51, a plan revised every year), who adopted it (2021 Q49, Morarji Desai), which plan (2025 Q40).",
    src="2025 Q40", a=3)

# ---------------------------------------------------------------- (h) Defence (12)
add(DEF, "IBSAMAR IX, a naval exercise held at Simon's Town in 2026, brings the Indian Navy together with the navies of",
    ["Brazil and South Africa", "Indonesia and Singapore", "Bangladesh and Sri Lanka", "Japan and Australia"],
    "Why: IBSAMAR is the maritime exercise of the IBSA group: India, Brazil and South Africa. Simon's Town is South Africa's main naval base, near Cape Town. Grew from: 2021 Q20 and 2025 Q90 (Dharma Guardian with Japan) and 2025 Q55 (Nomadic Elephant with Mongolia). Family: partner of each exercise: Varuna (France), KONKAN (UK), SIMBEX (Singapore), SLINEX (Sri Lanka), JIMEX (Japan), AUSINDEX (Australia), Malabar (USA, Japan, Australia), SAMPRITI (Bangladesh).",
    n=True)

add(DEF, "The Shinku La tunnel, being built by the Border Roads Organisation, will link the Lahaul valley of Himachal Pradesh with the",
    ["Zanskar valley of Ladakh", "Kashmir valley", "Chumbi valley of Tibet", "Kinnaur valley of Himachal Pradesh"],
    "Why: The Shinku La tunnel, at about 15,800 feet, will give an all-weather road from Lahaul (Himachal) to Padum in the Zanskar valley (Ladakh); when ready it is expected to be the world's highest tunnel. Work began in 2024. Grew from: 2021 Q89 (Sela Tunnel, Arunachal Pradesh). Family: BRO was set up in 1960 and works under the Ministry of Defence; Atal Tunnel (under Rohtang, Himachal, 2020), Sela Tunnel (Arunachal, 2024), Zojila tunnel (Kashmir–Ladakh, being built).")

add(DEF, "The LRLACM, flight-tested by DRDO in June 2026, is a",
    ["long-range land-attack cruise missile", "long-range surface-to-air missile", "submarine-launched ballistic missile", "anti-tank guided missile"],
    "Why: LRLACM stands for Long-Range Land Attack Cruise Missile; its lead lab is DRDO's Aeronautical Development Establishment (ADE), Bengaluru. A cruise missile flies low like an aircraft all the way, while a ballistic missile goes high and falls on its target. Trap: the long-range surface-to-air missile is Project Kusha. Grew from: 2018 Q56 (first indigenous tank, Arjun) and 2025 Q36 (Pralay). Family: 2026 tests: Agni-5 with MIRV (8 May), Pralay user trial (5 November), Kusha first flight (July), Agni-4 (August).",
    n=True)

add(DEF, "Admiral Krishna Swaminathan, who became the Chief of the Naval Staff on 31 May 2026, was earlier the head of which command?",
    ["Western Naval Command, Mumbai", "Eastern Naval Command, Visakhapatnam", "Southern Naval Command, Kochi", "Andaman and Nicobar Command, Port Blair"],
    "Why: Admiral Swaminathan headed the Western Naval Command at Mumbai before he took over from Admiral Dinesh K. Tripathi. The new CDS, General N. S. Raja Subramani, took office on the same day. Grew from: 2021 Q82 (the present Chief of the Air Staff). Family: 2026 changes: CDS Raja Subramani (3rd CDS, 31 May), Army Chief General Dhiraj Seth (30 June), Air Chief Ashutosh Dixit (31 October); Eastern Naval Command at Visakhapatnam, Southern at Kochi (training).",
    n=True)

add(DEF, "'Operation Rahat' (2015) of India's armed forces was carried out to evacuate Indians from",
    ["Yemen", "Sudan", "Ukraine", "Israel"],
    "Why: In April 2015, during the war in Yemen, the Navy, the Air Force and Air India brought out about 4,600 Indians and about 950 foreigners through Aden and Sanaa, with Djibouti as the base. Trap: Sudan was Operation Kaveri (2023), Ukraine Operation Ganga (2022), Israel Operation Ajay (2023). Grew from: 2025 Q20 (Operation Zero Line) and 2025 Q50 (Operation Keller). Family: Operation Sindhu (Iran, 2025), Operation Brahma (Myanmar earthquake relief, 2025), Operation Sindoor (7 May 2025), Operation Urja Suraksha (Hormuz, 2026).")

add(DEF, "The Barak-8 (MR-SAM) air-defence missile has been developed jointly by India and",
    ["Israel", "Russia", "France", "the United States"],
    "Why: Barak-8, called MR-SAM (medium-range surface-to-air missile) in India, was made by DRDO with Israel Aerospace Industries, and arms the Navy's destroyers and the Army and Air Force. Grew from: 2025 Q9 (Golden Dome of the USA) and 2021 Q87 (S-400 from Russia). Family: air-defence shields and their country: Iron Dome, Arrow and David's Sling (Israel), THAAD and Patriot (USA), S-400 Triumf (Russia), Akash (India); BrahMos was made with Russia.")

add(DEF, "In February 2026 the Army dropped 246 colonial-era names. Delhi Cantonment's Mall Road was renamed after which Param Vir Chakra awardee?",
    ["Second Lieutenant Arun Khetrapal", "Havildar Abdul Hamid", "Lance Naik Albert Ekka", "Major Hoshiar Singh"],
    "Why: Mall Road became Arun Khetrapal Marg, after the 21-year-old tank officer who won the PVC at Basantar in the 1971 war; Kirby Place became Kenuguruse Vihar. All four options are PVC awardees. Grew from: 2025 Q14 (renamed structures: Fort William to Vijay Durg, Kitchener House to Manekshaw House). Family: other 2026 renamings: Queens Line Road (Jaipur) to Sundar Singh Marg, New Birdwood Line (Bareilly) to Thimayya Colony.",
    n=True)

add(DEF, "Who became the first Indian woman to fly a fighter aircraft solo, a MiG-21 'Bison', in February 2018?",
    ["Flying Officer Avani Chaturvedi", "Flying Officer Bhawana Kanth", "Flying Officer Mohana Singh", "Flight Lieutenant Shivangi Singh"],
    "Why: Avani Chaturvedi flew a MiG-21 Bison alone from Jamnagar on 19 February 2018. She, Bhawana Kanth and Mohana Singh were the first three women commissioned as fighter pilots in June 2016. Trap: Shivangi Singh was the first woman to fly the Rafale. Grew from: 2021 Q84 (Missile Woman of India, Tessy Thomas). Family: first Field Marshal Sam Manekshaw (1973), only Marshal of the Air Force Arjan Singh, first CDS Bipin Rawat (2020), women in the NDA from 2022.")

add(DEF, "Who is called the 'Father of the Indian Navy'?",
    ["Chhatrapati Shivaji Maharaj", "Kanhoji Angre", "Raja Raja Chola I", "Admiral R. D. Katari"],
    "Why: Shivaji built a strong navy in the 17th century, with sea forts such as Sindhudurg, to guard the Konkan coast; the Navy's ensign of 2022 draws on his royal seal. Trap: Kanhoji Angre was the great Maratha admiral of the 18th century, and Vice Admiral R. D. Katari was the first Indian to head the Navy (1958). Grew from: 2021 Q84 (Missile Woman, Tessy Thomas). Family: Missile Man A. P. J. Abdul Kalam; Navy Day 4 December; INS Vikrant was commissioned in 2022.")

add(DEF, "The Army War College, which trains senior officers in tactics and leadership, is located at",
    ["Mhow, Madhya Pradesh", "Wellington, Tamil Nadu", "Secunderabad, Telangana", "Dehradun, Uttarakhand"],
    "Why: The Army War College is at Mhow (Dr Ambedkar Nagar), near Indore. Trap: Wellington has the Defence Services Staff College, Secunderabad the College of Defence Management, Dehradun the Indian Military Academy. Grew from: 2018 Q58 and 2021 Q81 (Indian National Defence University at Binola, Gurugram). Family: NDA Khadakwasla (Pune), Naval Academy Ezhimala (Kerala), Air Force Academy Dundigal (Hyderabad), National Defence College New Delhi, Officers Training Academy Chennai and Gaya.")

add(DEF, "Consider the following statements:\n1. The Border Security Force was raised in 1965.\n2. The Indo-Tibetan Border Police guards India's border with Nepal.\nWhich of the statements given above is/are correct?",
    S12,
    "Why: 1 is right: the BSF was raised on 1 December 1965, after the war with Pakistan; it guards the Pakistan and Bangladesh borders. 2 is wrong: the ITBP (1962) guards the border with China; the Nepal and Bhutan borders are guarded by the Sashastra Seema Bal. Grew from: 2025 Q29 (three statements about the ITBP). Family: Assam Rifles (1835, Myanmar border), CRPF (1939), CISF (1969, airports and industries), NSG (1984, 'Black Cats'); all the CAPFs work under the Home Ministry.",
    k="stmt", a=0)

add(DEF, "How many times has the Param Vir Chakra, India's highest wartime gallantry award, been awarded so far?",
    ["21", "14", "18", "30"],
    "Why: The PVC has been given 21 times since 1947–50; 14 of these awards were made after the soldier's death. The first went to Major Somnath Sharma (Kashmir, 1947) and the last ones to soldiers of the Kargil war (1999). Trap: 14 is the number of posthumous awards. Grew from: 2021 Q86 (the only Air Force officer with the PVC, Nirmal Jit Singh Sekhon). Family: wartime order: PVC, Maha Vir Chakra, Vir Chakra; peacetime: Ashoka Chakra, Kirti Chakra, Shaurya Chakra; the PVC was designed by Savitri Khanolkar.")

# ---------------------------------------------------------------- (i) Science & Tech (3)
add(SCI, "Aditya-L1, India's mission to study the Sun, is placed in a halo orbit around the Lagrange point L1. About how far is L1 from the Earth?",
    ["1.5 million km", "3.84 lakh km", "36,000 km", "15 million km"],
    "Why: L1 lies about 1.5 million km from the Earth towards the Sun, about one-hundredth of the Earth–Sun distance. There the pulls of the Sun and the Earth balance, so a craft can watch the Sun all the time without being hidden by the Earth. Trap: 3.84 lakh km is the Moon's distance, and 36,000 km is the height of a geostationary orbit. Grew from: 2025 Q48 (the orbit of EOS-09) and 2018 Q59 (lander of Chandrayaan-2). Family: Aditya-L1 was launched by PSLV-C57 in September 2023; Chandrayaan-3's lander Vikram and rover Pragyan; Gaganyaan G1 carries Vyommitra.")

add(SCI, "The Nobel Prize in Physiology or Medicine 2025 was awarded for discoveries about",
    ["peripheral immune tolerance, which stops the immune system from attacking the body", "optogenetics, the control of nerve cells with light", "microRNA and how it controls genes", "mRNA vaccines against COVID-19"],
    "Why: Mary Brunkow, Fred Ramsdell and Shimon Sakaguchi won it in 2025 for finding regulatory T cells, the 'security guards' that keep the immune system from attacking the body's own tissues. Trap: optogenetics was the 2026 prize, microRNA 2024 and mRNA vaccines 2023. Grew from: 2021 Q91 (Chemistry 2019 for lithium-ion batteries: the examiner asks the year before). Family: 2025 Chemistry – metal–organic frameworks; 2025 Physics – quantum tunnelling in a circuit; 2025 Peace – María Corina Machado.",
    n=True)

add(SCI, "Kala-azar (visceral leishmaniasis) is spread by the bite of the",
    ["sandfly", "Aedes mosquito", "Culex mosquito", "tsetse fly"],
    "Why: Kala-azar is caused by a protozoan, Leishmania donovani, and carried by the female sandfly; India has been close to eliminating it in Bihar, Jharkhand, West Bengal and Uttar Pradesh. Trap: Aedes spreads dengue, chikungunya and Zika; Culex spreads Japanese encephalitis and filaria; the tsetse fly spreads sleeping sickness in Africa. Grew from: 2025 Q24 (mumps is an airborne viral disease). Family: malaria by the female Anopheles (protozoan), TB and cholera are bacterial, measles and chickenpox are viral.")

# ---------------------------------------------------------------- (i) Environment (12)
add(ENV, "A well-known, much-loved species, such as the tiger or the giant panda, that is used to win public support for conservation is called a",
    ["flagship species", "keystone species", "indicator species", "endemic species"],
    "Why: A flagship species is chosen for its appeal, so that saving it also saves its forest; Project Tiger (1973) is the Indian example. A keystone species has a much larger effect on its ecosystem than its numbers suggest; an indicator species shows the health of the environment (lichens for air pollution); an endemic species lives only in one region. Grew from: 2025 Q23 (endemic) and 2025 Q84 (edge species). Family: umbrella species (protecting it protects many others), ecotone, niche, succession.")

add(ENV, "Bhitarkanika National Park in Odisha is best known for its",
    ["saltwater crocodiles and mangroves", "gharials of the Mahanadi gorge", "tigers and elephants in sal forest", "migratory birds of a brackish lagoon"],
    "Why: Bhitarkanika, in Kendrapara district, has the largest population of saltwater (estuarine) crocodiles in India and India's second-largest mangrove forest; it is a Ramsar site (2002) and was Odisha's first national park. Trap: gharials live in Satkosia gorge, tigers and elephants in Similipal, and migratory birds come to Chilika (Nalabana). Grew from: 2018 Q70 (what the Manas Sanctuary is known for) and 2021 Q92 (Jaypore forest made a national park). Family: Kaziranga – one-horned rhino, Gir – Asiatic lion, Keibul Lamjao – sangai deer.")

add(ENV, "A detritus food chain begins with",
    ["dead organic matter", "green plants", "herbivores", "carnivores"],
    "Why: In a detritus food chain, decomposers and detritivores such as fungi, bacteria and earthworms feed first on dead leaves, dead animals and waste, and are then eaten by others. A grazing food chain starts with green plants (producers). Grew from: 2018 Q13 (plankton in the upper part of the sea) and 2021 Q100 (high assimilation efficiency). Family: energy flows one way and only about 10% passes up each level (Lindeman); ecological pyramids of number, biomass and energy; producers, consumers and decomposers.")

add(ENV, "The India State of Forest Report 2023, released by the Forest Survey of India in December 2024, is which edition of the report?",
    ["18th", "16th", "17th", "20th"],
    "Why: The Forest Survey of India (Dehradun) has published the report every two years since 1987, so ISFR 2023 is the 18th (ISFR 2021 was the 17th). It put India's forest and tree cover at about 25.17% of its area. Grew from: 2018 Q48 (highest forest percentage) and 2025 Q92 (top States for increase in cover). Family: largest forest cover by area: Madhya Pradesh; highest share among States: Mizoram; largest mangrove cover: West Bengal; the edition number is an examiner habit.",
    n=True)

add(ENV, "After COP31 at Antalya, Türkiye, ended in November 2026, the next UN climate conference, COP32 (2027), is to be held in",
    ["Ethiopia", "Brazil", "Australia", "India"],
    "Why: COP32 is to be held at Addis Ababa, Ethiopia, in November 2027. COP31 at Antalya (9–22 November 2026) was hosted by Türkiye while Australia's Chris Bowen led the talks, and it ended without a main agreement. Trap: Brazil hosted COP30 at Belém (2025); India has offered to host COP33 in 2028. Grew from: 2021 Q14 (where the 15th World Forestry Congress was held). Family: COP29 Baku, COP28 Dubai; CBD COP17 at Yerevan, Armenia; the Kyoto Protocol (1997) and the Paris Agreement (2015).",
    n=True)

add(ENV, "India is one of how many 'megadiverse' countries of the world?",
    ["17", "12", "25", "36"],
    "Why: Seventeen countries, including India, Brazil, China, Indonesia and Australia, hold most of the world's species and are called megadiverse; the list was made by Conservation International. India has about 2.4% of the world's land but 7–8% of its recorded species. Trap: 36 is the number of global biodiversity hotspots. Grew from: 2021 Q94 (Norman Myers gave the hotspot idea) and 2021 Q97 (gamma diversity). Family: India's four hotspots: Himalaya, Indo-Burma, Western Ghats–Sri Lanka, Sundaland (Nicobar).")

add(ENV, "Match List I (programme) with List II (its aim):\nList I: a. Jal Jeevan Mission  b. Atal Bhujal Yojana  c. Namami Gange  d. AMRUT\nList II: 1. Water supply and sewerage in cities  2. Cleaning and protecting the Ganga  3. A tap water connection for every rural home  4. Groundwater management led by communities",
    [M(3, 4, 2, 1), M(4, 3, 2, 1), M(3, 4, 1, 2), M(3, 2, 4, 1)],
    "Why: Jal Jeevan Mission (2019) aims at a working tap connection ('Har Ghar Jal') for every rural home. Atal Bhujal Yojana (2019, World Bank-aided) helps villages in seven States manage groundwater. Namami Gange (2014) cleans the Ganga. AMRUT (2015) is about water supply, sewerage and parks in cities. Grew from: 2025 Q46 (statements on groundwater: India is the largest user). Family: Jal Shakti Ministry (2019), Catch the Rain campaign, Water quality index.",
    k="match")

add(ENV, "Earth Day was first observed on 22 April 1970 in the United States at the call of",
    ["Senator Gaylord Nelson", "Rachel Carson", "Al Gore", "John Muir"],
    "Why: US Senator Gaylord Nelson called for a nationwide 'teach-in' on the environment, and about 20 million Americans joined the first Earth Day on 22 April 1970; it went global in 1990. Trap: Rachel Carson wrote 'Silent Spring' (1962) and Al Gore made 'An Inconvenient Truth'. Grew from: 2018 Q61, 2021 Q10 and 2025 Q2 (the Earth Day theme, asked in all three papers). Family: Earth Day themes 2024 'Planet vs. Plastics', 2025 and 2026 'Our Power, Our Planet'; World Environment Day 5 June (host 2025 Republic of Korea, 2026 Azerbaijan).",
    k="one")

add(ENV, "Which of the following is an example of ex-situ conservation?",
    ["A seed bank", "A national park", "A biosphere reserve", "A sacred grove"],
    "Why: Ex-situ conservation saves a species outside its natural home, as in seed banks, gene banks, zoos and botanical gardens; the Svalbard Global Seed Vault in Norway is the best-known seed bank. National parks, biosphere reserves and sacred groves protect species in their own habitat (in-situ). Grew from: 2021 Q94 and Q97 (hotspots, gamma diversity). Family: India's first biosphere reserve Nilgiri (1986); Similipal is in UNESCO's network (2009); cryopreservation at −196 °C in liquid nitrogen.")

add(ENV, "According to the India State of Forest Report 2023, which State has the largest share of its area under forest?",
    ["Mizoram", "Arunachal Pradesh", "Meghalaya", "Madhya Pradesh"],
    "Why: Mizoram has about 85% of its area under forest, the highest among the States; among Union Territories Lakshadweep is higher still. Trap: Madhya Pradesh has the largest forest cover by area, not by share. Grew from: 2018 Q48 (highest percentage as per the 2018 report) and 2025 Q92 (top four States for increase). Family: largest mangrove cover – West Bengal (Sundarbans); total forest and tree cover about 25.17% of India; the National Forest Policy (1988) aims at one-third of the area under forest.",
    n=True)

add(ENV, "Match List I (programme or index) with List II (year it began):\nList I: a. Comprehensive Environmental Pollution Index (CEPI)  b. SAFAR air-quality forecasting  c. National Air Quality Index  d. National Clean Air Programme\nList II: 1. 2009  2. 2019  3. 2010  4. 2014",
    [M(1, 3, 4, 2), M(3, 1, 4, 2), M(1, 3, 2, 4), M(1, 4, 3, 2)],
    "Why: CEPI was made by the CPCB with IIT Delhi in 2009 to rank industrial clusters. SAFAR (System of Air Quality and Weather Forecasting and Research), run by IITM Pune, began in 2010 for the Delhi Commonwealth Games. The National AQI was launched in October 2014 under Swachh Bharat. The National Clean Air Programme began in January 2019. Grew from: 2025 Q26 (CEPI with IIT Delhi) and 2021 Q96 (NAMP monitors twice a week). Family: CPCB was set up in 1974 under the Water Act; the AQI uses eight pollutants.",
    k="match")

add(ENV, "Paddy fields, cattle and wetlands are major sources of which greenhouse gas?",
    ["Methane", "Nitrous oxide", "Sulphur hexafluoride", "Ozone"],
    "Why: Methane is made by microbes that break down matter without oxygen, as in flooded rice fields, the stomachs of cattle (enteric fermentation), wetlands and landfills. It traps about 80 times more heat than carbon dioxide over 20 years. Trap: nitrous oxide comes mainly from nitrogen fertilisers; sulphur hexafluoride from electrical equipment. Grew from: 2018 Q14 (greenhouse effect) and 2021 Q93 (a gas that is NOT a greenhouse gas). Family: the six Kyoto gases (CO2, CH4, N2O, HFCs, PFCs, SF6); the Global Methane Pledge (2021), which India has not joined.")

# ---------------------------------------------------------------- (j) Institutions (8)
add(INS, "The 'Living Planet Report', which tracks the fall in wildlife populations since 1970, is published by",
    ["WWF (World Wide Fund for Nature)", "UNEP", "IUCN", "the World Bank"],
    "Why: The Living Planet Report is brought out every two years by WWF with the Zoological Society of London; it uses the Living Planet Index of monitored populations of animals with backbones. Trap: IUCN publishes the Red List of threatened species, UNEP the Emissions Gap Report. Grew from: 2021 Q15 (South Asia Economic Focus by the World Bank). Family: report and publisher: World Economic Outlook – IMF; Global Gender Gap – World Economic Forum; Human Development Report – UNDP; Global Innovation Index – WIPO; World Press Freedom Index – Reporters Without Borders.")

add(INS, "Which Indian city joined UNESCO's Creative Cities Network in 2023 as a 'City of Gastronomy'?",
    ["Lucknow", "Gwalior", "Srinagar", "Jaipur"],
    "Why: Lucknow, known for Awadhi food, was named a City of Gastronomy in October 2023, while Gwalior was named a City of Music the same year. Hyderabad became a City of Gastronomy in 2019. Trap: Srinagar (2021) and Jaipur (2015) are Cities of Crafts and Folk Art. Grew from: 2025 Q86 (aim of the Memory of the World Register). Family: UNESCO lists: World Heritage (Sarnath became India's 45th site in July 2026), Intangible Cultural Heritage (Deepavali, 2025), Memory of the World (Bhagavad Gita and Natyashastra, 2025), Creative Cities.")

add(INS, "India's 'Look East Policy' was launched in 1991 under which Prime Minister?",
    ["P. V. Narasimha Rao", "I. K. Gujral", "Atal Bihari Vajpayee", "Manmohan Singh"],
    "Why: Narasimha Rao's government began the Look East Policy in 1991 to build trade and ties with South-East Asia (ASEAN) after the Cold War. In 2014 it was raised to the 'Act East Policy' under Narendra Modi, with more weight on security and the North-East. Trap: the Gujral Doctrine (1996–97) was about generous ties with neighbours. Grew from: 2021 Q30 (Panchsheel restates the UN Charter). Family: Panchsheel (1954, India and China), Non-Alignment (Nehru), Neighbourhood First (2014), SAGAR (2015), MAHASAGAR (2025).")

add(INS, "Match List I (initiative) with List II (its aim):\nList I: a. One Sun One World One Grid  b. Mission LiFE  c. International Big Cat Alliance  d. Green Credit Programme\nList II: 1. Rewards for green actions such as tree planting  2. A grid to share solar power across borders  3. Everyday lifestyle choices that protect the environment  4. Saving the seven big cat species",
    [M(2, 3, 4, 1), M(3, 2, 4, 1), M(2, 3, 1, 4), M(2, 4, 3, 1)],
    "Why: One Sun One World One Grid (OSOWOG) was proposed by India in 2018 and is carried forward through the International Solar Alliance. Mission LiFE (Lifestyle for Environment) was launched at Kevadia, Gujarat, in October 2022. The International Big Cat Alliance was launched at Mysuru in April 2023, 50 years after Project Tiger, for the tiger, lion, leopard, snow leopard, puma, jaguar and cheetah. The Green Credit Programme (2023) gives tradable credits for green actions. Grew from: 2021 Q52 (ISA headquarters at Gurugram) and 2021 Q59 (OSOWOG).",
    k="match")

add(INS, "Which country became the tenth full member of the Shanghai Cooperation Organisation (SCO) in July 2024?",
    ["Belarus", "Iran", "Türkiye", "Azerbaijan"],
    "Why: Belarus joined at the Astana summit of July 2024, a year after Iran (2023) became the ninth member. India and Pakistan joined in 2017. The SCO was founded in 2001 at Shanghai, so 2026 was its 25th year, marked at the Bishkek summit. Trap: Türkiye and Azerbaijan are dialogue partners. Grew from: 2021 Q13 (not a SAARC member) and 2021 Q54 (number of NATO members). Family: BRICS has 11 members (Indonesia joined in 2025, India chaired it in 2026); NATO's newest members are Finland (2023) and Sweden (2024).")

add(INS, "The International Criminal Court at The Hague, which tries people for genocide and war crimes, was set up under the",
    ["Rome Statute", "Geneva Conventions", "UN Charter", "Treaty of Versailles"],
    "Why: The Rome Statute was adopted in 1998 and came into force on 1 July 2002, creating the ICC to try individuals for genocide, crimes against humanity, war crimes and aggression. India, the USA and China are not members. Trap: the International Court of Justice, also at The Hague, was set up by the UN Charter and settles disputes between countries. Grew from: 2018 Q98 (Nagendra Singh, the Indian President of the ICJ). Family: ICJ has 15 judges elected for nine years; Dalveer Bhandari is an Indian judge of the ICJ.")

add(INS, "In June 2026 Kyrgyzstan and four other countries were elected to the UN Security Council for 2027–28. Which one of the following statements about the Council is NOT correct?",
    ["A retiring non-permanent member can be re-elected at once for the next term.", "The Council has 15 members.", "A non-permanent member serves for two years.", "Five non-permanent members are elected every year."],
    "Why: Article 23 of the UN Charter says a retiring non-permanent member is not eligible for immediate re-election, so a country must sit out at least one term. The rest are right: 5 permanent and 10 non-permanent members; half of the ten are elected each year by the General Assembly for two-year terms. Grew from: 2021 Q57 and Q58 (an elected member, and the two-year term) and 2018 Q99 (the permanent members). Family: elected for 2027–28: Austria, Kyrgyzstan, Portugal, Trinidad and Tobago, Zimbabwe; India has served eight terms, the last in 2021–22.",
    k="not", n=True)

add(INS, "The headquarters of the International Labour Organization (ILO) is at",
    ["Geneva", "Rome", "Paris", "Vienna"],
    "Why: The ILO, founded in 1919 under the Treaty of Versailles and the oldest UN specialised agency, is based in Geneva; it brings governments, employers and workers together. Trap: Rome has the FAO, Paris UNESCO, Vienna the IAEA and UNIDO. Grew from: 2025 Q5 (WMO statements) and 2018 Q97 (the Red Cross is not a UN agency). Family: Geneva also has the WHO, WMO, WTO and ITU; Nairobi has UNEP; Washington the IMF and World Bank; the ILO won the Nobel Peace Prize in 1969.")
