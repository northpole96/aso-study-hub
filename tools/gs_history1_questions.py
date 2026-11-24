# GS Modern History Mock 01: 50 questions on syllabus topic (c) British rule and freedom struggle (24 Nov 2026).
# The first 20 are the "highest probability" list the user approved in chat; the other 30 were drawn from the same
# families (plan: python3 .claude/skills/aso-mock/scripts/draw.py ga --topics his --n 30 --seed 241899).
# First option is right unless a is given.

S12 = ["Only 1", "Only 2", "Both 1 and 2", "Neither 1 nor 2"]
S3 = ["Only 1 and 2", "Only 2 and 3", "Only 1 and 3", "1, 2 and 3"]
def M(a, b, c, d):
    return "a-%d, b-%d, c-%d, d-%d" % (a, b, c, d)

META = dict(
    paper="ga",
    title="ASO GS Modern History Mock 01",
    hub_title="Modern History 50 · GS Mock 01",
    link_title="Modern History 50 mock",
    masthead="GS History 01",
    heading="General Studies Paper I · Modern History Mock 01",
    tagline="50 questions on<br><b>British rule and the freedom struggle</b><br>picked for the highest chance.",
    key="aso-gs-history-1",
    code="HIS1",
    out="ASO-GS-Mock-Modern-History-1.html",
    minutes=45,
    seed=241124,
    order="mixed",
    topic="his",
    date="24 Nov 2026",
    draw="python3 .claude/skills/aso-mock/scripts/draw.py ga --topics his --n 30 --seed 241899 (plus 20 hand-picked)",
    intro=[
        "This mock covers syllabus topic (c), British rule and the freedom struggle. It has 50 questions. Twenty are the ones judged most likely to come, chosen from the families the 2018, 2021 and 2025 papers keep using: the press and books, the Acts, the Viceroys, the Congress sessions, the labour and left groups, 1857, education and Odisha. The other thirty come from the same families and from the drawn plan.",
        "Every question is the next angle of a family the examiner has already used. One question, the date of Poorna Swaraj, is an exact repeat of 2025 Q54. There is no official key, so the answers come from standard textbooks. Read each explanation: it names the question it grew from and the facts of the family that are likely to come next. Answers that are not fully settled carry a CHECK tag.",
    ],
)

Q = []
def add(s, q, o, e, k="one", n=False, c=False, a=None, **x):
    d = dict(s=s, q=q, o=o, e=e, k=k, n=n, c=c, a=a); d.update(x); Q.append(d)

H = "Modern History"

# ================================================================ the 20 chosen in chat

# 1 press: pairs
add(H, "Which one of the following pairs of newspaper and founder or editor is NOT correct?",
    ["Bande Mataram – Surendranath Banerjee", "Kesari – Bal Gangadhar Tilak", "Comrade – Muhammad Ali Jauhar", "Mooknayak – B. R. Ambedkar"],
    "Why: Bande Mataram (1906) was started by Bipin Chandra Pal, and Aurobindo Ghose edited it later. Surendranath Banerjee ran The Bengalee. The other three pairs are right: Kesari (Marathi) was Tilak's paper, Comrade was Muhammad Ali's English weekly, and Mooknayak (1920) was Ambedkar's first paper. "
    "Grew from: 2021 Q28 (Pratap, Hind Swaraj, National Herald) and 2025 Q64 (Hindu, Young India, Bombay Times, Amrita Bazar Patrika). "
    "Family: Mahratta (Tilak, English), Al-Hilal (Abul Kalam Azad), Yugantar (Barindra Ghosh), Indian Opinion (Gandhi, South Africa), New India and Commonweal (Annie Besant), Harijan (Gandhi), Utkal Dipika (Odisha, 1866).",
    k="not")

# 2 press: Metcalfe
add(H, "Who removed the restrictions on the Indian press in 1835 and is called the 'Liberator of the Indian Press'?",
    ["Charles Metcalfe", "Lord Wellesley", "Lord Ripon", "Lord William Bentinck"],
    "Why: Charles Metcalfe, acting Governor-General, repealed the 1823 licensing rules in 1835. Bentinck was the Governor-General before him and Metcalfe took over, so Bentinck is the trap. "
    "Grew from: 2025 Q30 asked who brought the Censorship of the Press Act in 1799 (Wellesley). "
    "Family: 1799 Wellesley's censorship; 1823 Adam's licensing rules; 1835 Metcalfe; 1857 Licensing Act; 1878 Vernacular Press Act (Lytton), repealed in 1882 (Ripon); 1908 and 1910 Press Acts (Minto).")

# 3 books: pairs
add(H, "Which one of the following pairs of book and author is NOT correct?",
    ["Neel Darpan – Rabindranath Tagore", "Gita Rahasya – Bal Gangadhar Tilak", "Discovery of India – Jawaharlal Nehru", "Anandamath – Bankim Chandra Chatterjee"],
    "Why: Neel Darpan (1860) was written by Dinabandhu Mitra. It showed how indigo planters treated the farmers of Bengal. Tagore wrote Gora and Gitanjali. Tilak wrote Gita Rahasya in Mandalay jail, Nehru wrote Discovery of India in Ahmednagar Fort, and Anandamath carried the song Vande Mataram. "
    "Grew from: 2021 Q28 (Hind Swaraj by Gandhi) and 2018 Q25 (a book on Gandhi by Ramachandra Guha). "
    "Family: India Wins Freedom (Azad), The Indian War of Independence 1857 (Savarkar), Hind Swaraj (Gandhi, 1909), Poverty and Un-British Rule in India (Naoroji), An Autobiography (Nehru), Unhappy India (Lajpat Rai).",
    k="not")

# 4 economic impact: Naoroji
add(H, "'Poverty and Un-British Rule in India', which explained the Drain of Wealth, was written by:",
    ["Dadabhai Naoroji", "R. C. Dutt", "G. K. Gokhale", "M. G. Ranade"],
    "Why: Dadabhai Naoroji, the 'Grand Old Man of India', argued that part of India's wealth went to Britain every year without return. R. C. Dutt wrote 'The Economic History of India', which is the trap. "
    "Grew from: 2021 Q27 (deindustrialisation). "
    "Family: Naoroji was the first Asian elected to the British House of Commons (1892), founded the East India Association (1866) and was Congress president three times (1886, 1893, 1906).")

# 5 acts: diarchy
add(H, "Which Act introduced diarchy in the provinces?",
    ["Government of India Act, 1919", "Government of India Act, 1935", "Indian Councils Act, 1909", "Indian Councils Act, 1892"],
    "Why: diarchy means dual rule. In the provinces, 'transferred' subjects such as education and health went to elected Indian ministers, and 'reserved' subjects such as police and finance stayed with the Governor. It came from the Montagu-Chelmsford reforms of 1919. "
    "Grew from: 2025 Q38 (provincial autonomy and federal court: 1935) and 2018 Q28 (elections: 1909). "
    "Family: 1909 Morley-Minto (separate electorates), 1919 (bicameral Centre, Public Service Commission, a Statutory Commission after ten years), 1935 (provincial autonomy, Federal Court, All-India Federation never began).")

# 6 acts: wrong pair
add(H, "Which one of the following Acts is NOT correctly matched with what it brought?",
    ["Indian Councils Act, 1892 – separate electorates for Muslims", "Regulating Act, 1773 – Supreme Court at Calcutta", "Pitt's India Act, 1784 – Board of Control", "Charter Act, 1833 – Governor-General of India"],
    "Why: separate electorates came with the Indian Councils Act of 1909 (Morley-Minto), not the Act of 1892. The 1892 Act brought indirect election and the right to ask questions. The other three pairs are right. "
    "Grew from: 2025 Q76 (a wrongly matched Act and year) and 2018 Q28 (the principle of elections). "
    "Family: 1813 ended the Company's trade monopoly in India; 1833 made the Governor-General of Bengal the Governor-General of India (Bentinck was the first); 1853 started open competition for the civil service; 1858 passed rule to the Crown.",
    k="not")

# 7 viceroys: Curzon
add(H, "The Partition of Bengal in 1905 was made during the time of which Viceroy?",
    ["Lord Curzon", "Lord Lytton", "Lord Ripon", "Lord Minto"],
    "Why: Curzon divided Bengal on 16 October 1905 and said it was for better administration. The Swadeshi and boycott movement grew out of this. Minto came after him, and the partition was undone in 1911 under Hardinge. "
    "Grew from: 2018 Q86 and 2025 Q10 (Ripon and the Ilbert Bill). "
    "Family: Curzon also passed the Universities Act of 1904 and set up the Archaeological Survey; Ripon gave local self-government (1882); Lytton held the Delhi Durbar of 1877; Dalhousie started railways and the Doctrine of Lapse; Bentinck banned sati.")

# 8 land revenue: Permanent Settlement
add(H, "The Permanent Settlement of 1793 in Bengal and Bihar was introduced by:",
    ["Lord Cornwallis", "Thomas Munro", "Holt Mackenzie", "Lord Wellesley"],
    "Why: Cornwallis fixed the land revenue of Bengal and Bihar for ever and made the zamindars the owners of the land. "
    "Grew from: 2025 Q88 (Ryotwari: Madras and Bombay). "
    "Family: Ryotwari (Thomas Munro and Alexander Reed), Mahalwari (Holt Mackenzie, North-West Provinces, 1822). Trap: Munro is the Ryotwari name, Mackenzie is the Mahalwari name.")

# 9 education: Wood's Despatch
add(H, "Which document is called the 'Magna Carta of English Education in India'?",
    ["Wood's Despatch, 1854", "Macaulay's Minute, 1835", "Hunter Commission, 1882", "Sadler Commission, 1917"],
    "Why: Charles Wood's Despatch of 1854 set up universities at Calcutta, Bombay and Madras (1857), a department of education in each province, and grants-in-aid. This is why it is called the Magna Carta. "
    "Grew from: 2025 Q81 (put Hartog, Hunter, Sadler and Kothari in order) and 2021 Q23 (Charter Act of 1813). "
    "Family: 1813 one lakh rupees for education; 1835 Macaulay's Minute for English; 1854 Wood; 1882 Hunter (primary and secondary); 1902 Raleigh; 1917 Sadler; 1929 Hartog; 1944 Sargent; 1948 Radhakrishnan; 1964 Kothari.")

# 10 firsts: Canning
add(H, "Who was the first Viceroy of India?",
    ["Lord Canning", "Lord Dalhousie", "Lord Bentinck", "Lord Cornwallis"],
    "Why: after the Government of India Act 1858, the Governor-General also got the title Viceroy. Lord Canning was the first to hold both. "
    "Grew from: 2025 Q45 (a 'NOT correct' question on firsts). "
    "Family: Warren Hastings was the first Governor-General of Bengal; William Bentinck was the first Governor-General of India (1833); Macaulay was the first Law Member; Satyendranath Tagore was the first Indian in the ICS (1863); S. P. Sinha was the first Indian in the Viceroy's Executive Council (1909).")

# 11 INC: Sarojini Naidu
add(H, "Who was the first Indian woman President of the Indian National Congress?",
    ["Sarojini Naidu", "Annie Besant", "Vijayalakshmi Pandit", "Aruna Asaf Ali"],
    "Why: Sarojini Naidu presided at Kanpur in 1925. Annie Besant, who was Irish, was the first woman president (Calcutta, 1917), so 'Indian' in the question is the key. "
    "Grew from: 2018 Q88 (the only Congress session Gandhi presided over: Belgaum, 1924) and 2025 Q31 (Karachi, 1931). "
    "Family: W. C. Bonnerjee (1885) was the first president; Badruddin Tyabji the first Muslim president (1887); George Yule the first English president (1888).")

# 12 INC: Lahore
add(H, "Who presided over the Lahore session of the Indian National Congress in 1929, which set Poorna Swaraj as the goal?",
    ["Jawaharlal Nehru", "Motilal Nehru", "Sardar Vallabhbhai Patel", "Subhas Chandra Bose"],
    "Why: Jawaharlal Nehru was elected president at Lahore (December 1929) when he was only 40. Motilal Nehru presided in 1928 at Calcutta, which is the trap. Patel presided over Karachi in 1931. "
    "Grew from: 2025 Q54 (the date of Poorna Swaraj) and 2025 Q31 (Karachi). "
    "Family: Lahore adopted the Poorna Swaraj resolution on the banks of the Ravi, and the Congress boycotted the Round Table Conferences and planned civil disobedience.")

# 13 organisations: Servants of India Society
add(H, "The Servants of India Society (1905) was founded by:",
    ["Gopal Krishna Gokhale", "Lala Lajpat Rai", "N. M. Joshi", "Bal Gangadhar Tilak"],
    "Why: Gokhale started it in Pune to train workers for public service. Lajpat Rai's body, the Servants of the People Society (1921), has a similar name, and this is the trap that 2025 Q58 used. N. M. Joshi was a member of Gokhale's society. "
    "Grew from: 2025 Q58 (match of leaders with bodies) and 2025 Q57 (Central National Mohammedan Association). "
    "Family: Gokhale was called Gandhi's political guru; Indian Association (1876, Surendranath Banerjee); Poona Sarvajanik Sabha (1870, Ranade); Madras Mahajana Sabha (1884); Muslim League (1906, Dhaka).")

# 14 labour: AITUC
add(H, "Who was the first president of the All India Trade Union Congress (AITUC), formed in 1920?",
    ["Lala Lajpat Rai", "N. M. Joshi", "V. V. Giri", "Dewan Chaman Lall"],
    "Why: the AITUC was formed in Bombay on 31 October 1920 and Lala Lajpat Rai was its first president. Dewan Chaman Lall was its first general secretary, so he is the trap. "
    "Grew from: 2025 Q58 and Q97 (CPI, the Labour Swaraj Party and trade-union leaders) and 2018 Q67 (Gandhi and the Ahmedabad Textile Labour Association). "
    "Family: the Madras Labour Union (1918, B. P. Wadia); the Meerut Conspiracy Case (1929); the Congress Socialist Party (1934); the All India Kisan Sabha (1936, Swami Sahajanand).")

# 15 Gandhi: order
add(H, "Arrange the following in the correct chronological order:\n(i) Non-Cooperation Movement\n(ii) Dandi March\n(iii) Quit India Movement\n(iv) Rowlatt Satyagraha",
    ["iv, i, ii, iii", "i, ii, iii, iv", "iv, ii, i, iii", "i, iv, ii, iii"],
    "Why: Rowlatt Satyagraha 1919, Non-Cooperation 1920–22, Dandi March 12 March to 6 April 1930, Quit India 8 August 1942. "
    "Grew from: 2018 Q87 (a similar four-movement order) and 2018 Q32 (Dandi date). "
    "Family: Champaran 1917, Ahmedabad mill strike and Kheda 1918, Jallianwala Bagh 1919, Chauri Chaura 1922, Simon Commission 1928, Civil Disobedience 1930, Gandhi-Irwin Pact 1931, Poona Pact 1932.",
    k="order")

# 16 Poona Pact
add(H, "The Poona Pact (1932) between Gandhi and Ambedkar gave the depressed classes:",
    ["Reserved seats inside the general electorate", "Separate electorates", "Dominion status", "Provincial autonomy"],
    "Why: the Communal Award of Ramsay MacDonald (August 1932) gave separate electorates to the depressed classes. Gandhi fasted in Yerwada jail. The Poona Pact (24 September 1932) gave them more reserved seats, but inside the general electorate. "
    "Grew from: 2018 Q87 (order of movements) and 2025 Q31 (Karachi 1931, Gandhi at the Second Round Table Conference). "
    "Family: Gandhi-Irwin Pact (March 1931), Second Round Table Conference (1931), Communal Award (1932), Poona Pact (1932), Harijan Sevak Sangh (1932).")

# 17 revolutionaries: Chittagong
add(H, "Who led the Chittagong Armoury Raid of April 1930?",
    ["Surya Sen", "Chandrashekhar Azad", "Ram Prasad Bismil", "Rash Behari Bose"],
    "Why: Surya Sen, known as 'Masterda', led the raid on the police and auxiliary armouries of Chittagong on 18 April 1930. Azad and Bismil belong to the north Indian HRA and HSRA, and Rash Behari Bose to the Ghadar and INA story. "
    "Grew from: 2018 Q30 (headquarters of the Ghadar Party: San Francisco). "
    "Family: Anushilan Samiti, Alipore bomb case (1908), India House (London), Kakori (1925), Bhagat Singh and the Assembly bomb (1929), Komagata Maru (1914).")

# 18 1857: Bareilly
add(H, "Who led the revolt of 1857 at Bareilly?",
    ["Khan Bahadur Khan", "Bakht Khan", "Ahmadullah Shah", "Liaquat Ali"],
    "Why: Khan Bahadur Khan, a descendant of Hafiz Rahmat Khan, declared himself ruler at Bareilly. Bakht Khan led at Delhi, Ahmadullah Shah at Faizabad and Liaquat Ali at Allahabad. "
    "Grew from: 2025 Q75 (a wrongly matched storm-centre) and 2018 Q29 (where it began: Meerut). "
    "Family: Kanpur: Nana Sahib and Tantia Tope; Lucknow: Begum Hazrat Mahal; Jhansi: Rani Lakshmibai; Jagdishpur: Kunwar Singh; Delhi: Bahadur Shah Zafar and Bakht Khan; Sambalpur: Surendra Sai.")

# 19 Odisha 1857
add(H, "Who led the revolt of 1857 in Sambalpur, Odisha?",
    ["Surendra Sai", "Bakshi Jagabandhu", "Chakra Bisoyi", "Madhusudan Das"],
    "Why: Surendra Sai of Sambalpur fought the British for years and was jailed in Asirgarh fort, where he died in 1884. Bakshi Jagabandhu led the Paika Rebellion of 1817 and Chakra Bisoyi led the Kandha rising in Ghumsur, so both are traps. "
    "Grew from: 2025 Q75 (storm-centres of 1857). "
    "Family: Odisha came under British rule in 1803 (Treaty of Deogaon); the province of Odisha was created on 1 April 1936 (Utkal Divas).")

# 20 Odisha: Utkal Sammilani
add(H, "The Utkal Sammilani (1903), which worked for the unity of Odia-speaking areas, was led by:",
    ["Madhusudan Das", "Gopabandhu Das", "Fakir Mohan Senapati", "Harekrushna Mahtab"],
    "Why: Madhusudan Das, known as 'Utkal Gourav', was the leader of the Sammilani. Its first session was held at Cuttack in 1903. Gopabandhu Das ('Utkalmani') came later and ran the Satyabadi school. "
    "Grew from: the Odisha lines of the syllabus; Odisha history is asked often because of Utkal Divas (1 April 1936). "
    "Family: Utkal Dipika (1866); Utkal Union Conference; Odisha province under the Government of India Act 1935; Krushna Chandra Gajapati as the first Prime Minister of Odisha.",
    c=True)

# ================================================================ the 30 drawn and added

# 21 expansion: Allahabad
add(H, "By which treaty did the East India Company get the Diwani (the right to collect revenue) of Bengal, Bihar and Orissa in 1765?",
    ["Treaty of Allahabad", "Treaty of Bassein", "Treaty of Srirangapatna", "Treaty of Salbai"],
    "Why: after winning the Battle of Buxar (1764), Robert Clive signed the Treaty of Allahabad with Shah Alam II and Shuja-ud-Daula. The Diwani made the Company the real ruler of three provinces. "
    "Grew from: 2018 Q26 (the French defeated at Wandiwash) and 2018 Q71 (the Treaty of Bassein, 1802). "
    "Family: Plassey 1757, Buxar 1764, Salbai 1782, Srirangapatna 1792 (Tipu Sultan), Bassein 1802 (Baji Rao II), Deogaon 1803 (Odisha).")

# 22 expansion: order of treaties
add(H, "Arrange these treaties in the correct order of date:\n(i) Treaty of Salbai\n(ii) Treaty of Bassein\n(iii) Treaty of Srirangapatna\n(iv) Treaty of Allahabad",
    ["iv, i, iii, ii", "i, iv, iii, ii", "iv, iii, i, ii", "iv, i, ii, iii"],
    "Why: Allahabad 1765, Salbai 1782, Srirangapatna 1792, Bassein 1802. Remember them as 65, 82, 92, 02. "
    "Grew from: 2018 Q71 (the Treaty of Bassein, signed by Baji Rao II) and 2018 Q26. "
    "Family: Salbai ended the First Anglo-Maratha War; Srirangapatna ended the Third Anglo-Mysore War; Bassein began the Second Anglo-Maratha War.",
    k="order")

# 23 Indian states: first subsidiary
add(H, "Which was the first Indian state to accept the Subsidiary Alliance of Lord Wellesley (1798)?",
    ["Hyderabad", "Mysore", "Awadh", "Gwalior"],
    "Why: the Nizam of Hyderabad accepted it in 1798. In this system the ruler kept British troops, paid for them and took no other European into service. Mysore under Tipu Sultan did not accept it and was crushed in 1799. "
    "Grew from: 2021 Q21, Q22 and Q25 (three questions on rulers and states). "
    "Family: Hyderabad 1798, Mysore 1799 (after Tipu), Tanjore 1799, Awadh 1801, Peshwa 1802 (Bassein), Scindia 1804.")

# 24 Indian states: lapse
add(H, "Which of the following states was NOT annexed by Dalhousie under the Doctrine of Lapse?",
    ["Awadh", "Satara", "Jhansi", "Nagpur"],
    "Why: Awadh was taken in 1856 on the charge of misrule, not by lapse. The Doctrine of Lapse applied where a ruler died without a natural heir: Satara 1848, Sambalpur 1849, Jhansi 1853, Nagpur 1854. "
    "Grew from: 2021 Q21 and Q22 (two 'not a matched pair' questions on states). "
    "Family: the annexation of Awadh hurt the sepoys of Bengal, who came from there; Dalhousie also started railways (1853) and the telegraph.",
    k="not")

# 25 Gandhi: Champaran
add(H, "Gandhi's first Satyagraha in India (Champaran, 1917) was against the forced growing of which crop?",
    ["Indigo", "Cotton", "Opium", "Tea"],
    "Why: under the 'tinkathia' system, farmers had to grow indigo on three-twentieths of their land for the planters. Gandhi went to Champaran in Bihar at the call of Rajkumar Shukla. "
    "Grew from: 2018 Q87 and Q32 (Gandhi's movements and Dandi). "
    "Family: Champaran (1917), the Ahmedabad mill strike and Kheda (1918), then Rowlatt (1919). Neel Darpan (1860) was the earlier play about indigo.")

# 26 Gandhi-Irwin
add(H, "Which agreement of 1931 led the Congress to take part in the Second Round Table Conference?",
    ["Gandhi–Irwin Pact", "Poona Pact", "Lucknow Pact", "Cripps Proposals"],
    "Why: in the Gandhi-Irwin Pact (5 March 1931) the Congress suspended Civil Disobedience, and the Government freed political prisoners. Gandhi then went to London as the Congress's only representative. "
    "Grew from: 2018 Q87 and 2025 Q31 (Karachi session, 1931, endorsed the Pact). "
    "Family: the Poona Pact is 1932; the Lucknow Pact is 1916; the Cripps Mission came in 1942.")

# 27 Gandhi: Chauri Chaura
add(H, "Which incident made Gandhi call off the Non-Cooperation Movement in February 1922?",
    ["Chauri Chaura", "Jallianwala Bagh", "Kakori", "Moplah rising"],
    "Why: on 5 February 1922 a mob burnt a police station at Chauri Chaura (Gorakhpur) and killed 22 policemen. Gandhi believed the country was not yet ready for non-violence. "
    "Grew from: 2018 Q87 (order of movements). "
    "Family: Jallianwala Bagh 1919 (General Dyer, Amritsar); the Khilafat Movement; the Swaraj Party (1923, C. R. Das and Motilal Nehru) was formed after the movement ended.")

# 28 Gandhi: Quit India place
add(H, "The Quit India resolution was passed in August 1942 at which place?",
    ["Bombay (Gowalia Tank)", "Wardha", "Allahabad", "Lahore"],
    "Why: the All India Congress Committee passed it at Gowalia Tank Maidan, Bombay, on 8 August 1942. Gandhi gave the call 'Do or Die'. Gandhi and the leaders were arrested the next morning. "
    "Grew from: 2018 Q87 (Quit India in an order question). "
    "Family: the Wardha meeting (July 1942) first approved the idea; Jayaprakash Narayan, Aruna Asaf Ali and Ram Manohar Lohia ran the underground; the Cripps Mission (March 1942) came before.")

# 29 INC: first president
add(H, "Who presided over the first session of the Indian National Congress in 1885 at Bombay?",
    ["W. C. Bonnerjee", "Dadabhai Naoroji", "A. O. Hume", "Surendranath Banerjee"],
    "Why: Womesh Chunder Bonnerjee was the first president, and 72 delegates came. A. O. Hume, who had helped to found the Congress, was its first general secretary, not its president. "
    "Grew from: 2018 Q88 and 2025 Q31, Q54 (sessions and presidents). "
    "Family: Naoroji presided in 1886, 1893 and 1906; Badruddin Tyabji was the first Muslim president (1887); Gandhi presided only in 1924 at Belgaum.")

# 30 INC: Lucknow 1916
add(H, "The Lucknow Pact of 1916 joined the Congress and the Muslim League and brought the Extremists back. Who presided over that Congress session?",
    ["Ambika Charan Mazumdar", "Annie Besant", "Bal Gangadhar Tilak", "Motilal Nehru"],
    "Why: Ambika Charan Mazumdar presided at Lucknow in 1916. Tilak and Jinnah worked out the Pact, and the Congress accepted separate electorates for Muslims, which is why people remember it. "
    "Grew from: 2025 Q31 and Q54 (Karachi and Lahore sessions). "
    "Family: Surat split 1907 (Rash Behari Ghosh); Annie Besant presided in 1917; Gandhi in 1924 (Belgaum); Sarojini Naidu in 1925; Nehru in 1929 (Lahore); Patel in 1931 (Karachi).")

# 31 INC: Tripuri
add(H, "Who defeated Pattabhi Sitaramayya to be elected Congress President in 1939 and then resigned?",
    ["Subhas Chandra Bose", "Jawaharlal Nehru", "Maulana Abul Kalam Azad", "Rajendra Prasad"],
    "Why: Bose beat Gandhi's candidate Pattabhi Sitaramayya in January 1939. At the Tripuri session in March he faced a block, and he resigned and founded the Forward Bloc in May. Rajendra Prasad took his place. "
    "Grew from: 2018 Q33 (Bose's Provisional Government in Singapore). "
    "Family: Bose was also president at Haripura (1938). Azad presided in 1923 and again in 1940 (Ramgarh), the longest term, to 1946.")

# 32 REPEAT: Poorna Swaraj date
add(H, "On which date was 'Poorna Swaraj' declared as the goal of the Indian National Congress?",
    ["26 January 1930", "12 March 1930", "9 August 1942", "15 August 1947"],
    "Why: the Lahore session of December 1929 passed the Poorna Swaraj resolution, and 26 January 1930 was fixed as the first Independence Day. The date was then observed every year until 1947, and in 1950 the Constitution came into force on the same day. The other dates are the Dandi March (12 March 1930), Quit India (9 August 1942, the day after the resolution) and Independence (15 August 1947). "
    "Grew from: 2025 Q54, repeated word for word. "
    "Family: the Lahore session (Nehru, 1929); the Karachi resolution on Fundamental Rights (1931).",
    src="2025 Q54")

# 33 leaders: titles
add(H, "Which one of the following titles is NOT correctly matched with its leader?",
    ["Utkal Gourav – Gopabandhu Das", "Punjab Kesari – Lala Lajpat Rai", "Frontier Gandhi – Khan Abdul Ghaffar Khan", "Deshbandhu – C. R. Das"],
    "Why: 'Utkal Gourav' was Madhusudan Das, and Gopabandhu Das was 'Utkalmani'. The other three are right. "
    "Grew from: 2025 Q96 (statements about Lala Lajpat Rai). "
    "Family: Lokmanya – Tilak; Netaji – Subhas Bose; Sardar – Vallabhbhai Patel; Deshbandhu – C. R. Das; Bapu – Gandhi; Gurudev – Tagore.",
    k="not")

# 34 leaders: Bose statements
add(H, "Consider the following statements about Subhas Chandra Bose:\n1. He founded the Forward Bloc in 1939.\n2. He gave the call 'Delhi Chalo' to the Indian National Army.\n3. He gave the slogan 'Do or Die'.\nWhich of the statements given above is/are correct?",
    S3,
    "Why: Bose founded the Forward Bloc after leaving the Congress (statement 1 is right), and 'Delhi Chalo' was the INA's marching call (statement 2 is right). 'Do or Die' was Gandhi's slogan in the Quit India call of 1942, so statement 3 is false. "
    "Grew from: 2018 Q33 (Bose's Provisional Government, Singapore) and 2025 Q96 (statements about one leader). "
    "Family: 'Give me blood and I will give you freedom'; 'Jai Hind'; Azad Hind Fauj under Rash Behari Bose and Mohan Singh before Bose took over in 1943.",
    k="stmt", a=0)

# 35 leaders: Tilak statements
add(H, "Consider the following statements about Bal Gangadhar Tilak:\n1. He said 'Swaraj is my birthright and I shall have it'.\n2. He founded the Servants of India Society.\n3. He started the newspapers Kesari and Mahratta.\nWhich of the statements given above is/are correct?",
    S3,
    "Why: statements 1 and 3 are right. The Servants of India Society was founded by Gokhale in 1905, so statement 2 is false. Tilak and Gokhale are often swapped in questions. "
    "Grew from: 2025 Q58 (Servants of the People Society, Lajpat Rai) and 2025 Q96 (statements about one leader). "
    "Family: Tilak started the Ganapati and Shivaji festivals, set up the Home Rule League at Poona in 1916 and led the Extremists at Surat (1907); Annie Besant's league was at Adyar.",
    k="stmt", a=2)

# 36 firsts: match
add(H, "Match List I with List II:\nList I\na. Satyendranath Tagore\nb. Macaulay\nc. S. P. Sinha\nd. W. C. Bonnerjee\nList II\n1. First Law Member of the Governor-General's Council\n2. First Indian to enter the Indian Civil Service\n3. First President of the Indian National Congress\n4. First Indian member of the Viceroy's Executive Council",
    [M(2, 1, 4, 3), M(1, 2, 4, 3), M(2, 1, 3, 4), M(2, 4, 1, 3)],
    "Why: Satyendranath Tagore (elder brother of Rabindranath) joined the ICS in 1863. Macaulay was the first Law Member (1834). S. P. Sinha joined the Viceroy's Executive Council in 1909 and Bonnerjee was the first president of the Congress. "
    "Grew from: 2025 Q45 (a 'NOT correct' question on firsts). "
    "Family: Warren Hastings (first Governor-General of Bengal), Bentinck (first Governor-General of India), Canning (first Viceroy), Mountbatten (last Viceroy), C. Rajagopalachari (first Indian Governor-General).",
    k="match", a=0)

# 37 economic: famine commission
add(H, "The first Famine Commission (1880), after the great famine of 1876–78, was headed by:",
    ["Sir Richard Strachey", "Sir James Lyall", "Sir Antony MacDonnell", "Lord Lytton"],
    "Why: the Famine Commission of 1880 under Sir Richard Strachey laid down the 'Famine Code'. Lyall (1898) and MacDonnell (1901) led the later commissions. Lord Lytton was Viceroy during the famine, and he is the trap. "
    "Grew from: 2021 Q27 (the effects of British economic policy). "
    "Family: Orissa famine 1866 (Na-anka Durbhiksha) killed about a third of the people of Odisha; the Great Bengal Famine of 1943. Some books name a different head for the 1880 body, so this carries CHECK.",
    c=True)

# 38 judicial: IPC
add(H, "The Indian Penal Code was drafted by the First Law Commission under the chairmanship of:",
    ["Lord Macaulay", "Lord Cornwallis", "Warren Hastings", "Lord Dalhousie"],
    "Why: Macaulay headed the First Law Commission (1834), which drafted the code. It came into force in 1862. Cornwallis is linked to the Cornwallis Code of 1793, which is the trap. "
    "Grew from: 2021 Q24 (the order of colonial courts and laws). "
    "Family: Supreme Court at Calcutta (1774); Sadr Diwani and Nizamat Adalat; High Courts Act 1861 (Calcutta, Bombay, Madras); Elijah Impey was the first Chief Justice of the Supreme Court.")

# 39 social reform: pairs
add(H, "Which one of the following social reform bodies is NOT correctly matched with its founder or leader?",
    ["Prarthana Samaj – Keshab Chandra Sen", "Arya Samaj – Dayananda Saraswati", "Satyashodhak Samaj – Jyotirao Phule", "Ramakrishna Mission – Swami Vivekananda"],
    "Why: the Prarthana Samaj (1867) was founded in Bombay by Atmaram Pandurang, with M. G. Ranade among its leaders. Keshab Chandra Sen led the Brahmo Samaj of India. The other three pairs are right. "
    "Grew from: the syllabus line on social reform (never yet asked as a separate question, so it is a gap in the three papers). "
    "Family: Brahmo Samaj 1828 (Ram Mohan Roy); Arya Samaj 1875 (Bombay); Satyashodhak Samaj 1873 (Pune); Ramakrishna Mission 1897.",
    k="not")

# 40 social reform: Vidyasagar
add(H, "The Hindu Widows' Remarriage Act of 1856 was passed mainly because of the efforts of:",
    ["Ishwar Chandra Vidyasagar", "Raja Ram Mohan Roy", "Dayananda Saraswati", "Jyotirao Phule"],
    "Why: Vidyasagar sent petitions with thousands of signatures, and the Act was passed in July 1856 (Dalhousie had prepared it; Canning signed it). Ram Mohan Roy worked against sati, which is the trap. "
    "Grew from: the syllabus line on social reform. "
    "Family: sati banned in 1829 under Bentinck; Female Infanticide Act 1870; Age of Consent Act 1891; Sarda Act 1929 (child marriage).")

# 41 organisations: Indian Association
add(H, "The Indian Association (1876), a forerunner of the Congress, was founded by:",
    ["Surendranath Banerjee", "Dadabhai Naoroji", "A. O. Hume", "Pherozeshah Mehta"],
    "Why: Surendranath Banerjee and Ananda Mohan Bose founded it in Calcutta in 1876. Naoroji's body was the East India Association (London, 1866), and Hume founded the Congress with others in 1885. "
    "Grew from: 2025 Q57 (founder of the Central National Mohammedan Association, 1877–78). "
    "Family: Poona Sarvajanik Sabha (1870); Madras Mahajana Sabha (1884); Bombay Presidency Association (1885); British Indian Association (1851); Muslim League (Dhaka, 1906).")

# 42 1857: Hugh Rose
add(H, "Which British general defeated Rani Lakshmibai of Jhansi at Gwalior in June 1858?",
    ["Sir Hugh Rose", "Sir Colin Campbell", "John Nicholson", "Henry Havelock"],
    "Why: Sir Hugh Rose took Jhansi (April 1858) and then Gwalior, where Lakshmibai died fighting in June. Campbell took Lucknow, Nicholson was at Delhi and Havelock at Kanpur. "
    "Grew from: 2025 Q75 (storm-centres and leaders of 1857). "
    "Family: Delhi fell in September 1857 (John Nicholson was killed, Hodson captured Bahadur Shah Zafar); Lucknow (Campbell); Kanpur (Nana Sahib, Tantia Tope); Bihar (Kunwar Singh).")

# 43 1857: Savarkar
add(H, "Who first called the Revolt of 1857 the 'First War of Indian Independence' in a book?",
    ["V. D. Savarkar", "Bipin Chandra Pal", "Lala Lajpat Rai", "Vincent Smith"],
    "Why: Savarkar wrote 'The Indian War of Independence, 1857' (1909). British writers called it the Sepoy Mutiny. "
    "Grew from: 2021 Q28 (Savarkar and the Free India Society) and 2018 Q29 (where the revolt began). "
    "Family: Savarkar founded the Free India Society in London; R. C. Majumdar said it was neither first, nor national, nor a war of independence; S. N. Sen called it a war of independence.")

# 44 revolutionaries: Komagata Maru
add(H, "The Komagata Maru incident of 1914 involved Indian passengers who were refused entry into:",
    ["Canada", "Australia", "South Africa", "Malaya"],
    "Why: the ship carried about 376 Sikh and Punjabi passengers to Vancouver. Canada's rules sent them back, and a clash with police followed at Budge Budge near Calcutta. "
    "Grew from: 2018 Q30 (the Ghadar Party at San Francisco). "
    "Family: Ghadar Party 1913 (Lala Har Dayal and Sohan Singh Bhakna); India House (London); Anushilan Samiti; Kakori 1925.")

# 45 revolutionaries: Kakori
add(H, "The Kakori Train Robbery of 1925 was planned by which revolutionary body?",
    ["Hindustan Republican Association", "Ghadar Party", "Anushilan Samiti", "India House"],
    "Why: Ram Prasad Bismil and the Hindustan Republican Association took the government's money from a train near Kakori (Lucknow) in August 1925. Bismil, Ashfaqulla Khan and others were hanged. "
    "Grew from: 2018 Q30 (Ghadar headquarters). "
    "Family: HRA became the HSRA in 1928 (Bhagat Singh, Chandrashekhar Azad); Assembly bomb 1929; Lahore Conspiracy Case; Saunders killing 1928.")

# 46 press laws: order
add(H, "Arrange these press laws and events in order of time:\n(i) Vernacular Press Act\n(ii) Metcalfe removes the curbs on the press\n(iii) Censorship of the Press Act of 1799\n(iv) Indian Press Act of 1910",
    ["iii, ii, i, iv", "ii, iii, i, iv", "iii, i, ii, iv", "iii, ii, iv, i"],
    "Why: 1799 (Wellesley), 1835 (Metcalfe), 1878 (Lytton), 1910 (Minto). The Vernacular Press Act was repealed in 1882 under Ripon. "
    "Grew from: 2025 Q30 (the 1799 Act) and 2021 Q28 (the press in a combination question). "
    "Family: 1823 licensing rules (John Adam); 1857 Licensing Act; 1908 Newspapers (Incitement to Offences) Act; 1931 Indian Press (Emergency Powers) Act.",
    k="order")

# 47 acts: 1858
add(H, "Which Act ended the rule of the East India Company and passed the government of India to the British Crown?",
    ["Government of India Act, 1858", "Regulating Act, 1773", "Charter Act, 1853", "Indian Councils Act, 1861"],
    "Why: after the Revolt of 1857, this Act abolished the Company and the Board of Control, and set up the Secretary of State for India and his Council. Queen Victoria's Proclamation of 1 November 1858 announced it. "
    "Grew from: 2018 Q28 and 2025 Q38, Q76 (Acts in three papers). "
    "Family: the Governor-General became Viceroy (Canning); the 1861 Act brought Indians into the Viceroy's Council as nominated members.")

# 48 acts: 1935 Odisha
add(H, "The separate province of Orissa (now Odisha) was formed on 1 April 1936 under which Act?",
    ["Government of India Act, 1935", "Government of India Act, 1919", "Indian Councils Act, 1909", "Indian Independence Act, 1947"],
    "Why: the Government of India Act 1935 created two new provinces, Orissa and Sind. 1 April is now celebrated as Utkal Divas (Odisha Day). "
    "Grew from: 2025 Q38 (provincial autonomy and federal court, also 1935). "
    "Family: Sir John Hubback was the first Governor and Krushna Chandra Gajapati the first Prime Minister of Odisha; Madhusudan Das and the Utkal Sammilani led the demand.")

# 49 viceroys: Ripon NOT
add(H, "Which one of the following is NOT associated with the time of Lord Ripon?",
    ["The Delhi Durbar of 1877", "The Ilbert Bill controversy", "The repeal of the Vernacular Press Act", "The Local Self-Government resolution of 1882"],
    "Why: the Delhi Durbar of 1877, where Queen Victoria was proclaimed Empress of India, was held under Lord Lytton. The other three belong to Ripon, called the 'Father of Local Self-Government in India'. "
    "Grew from: 2018 Q86 and 2025 Q10 (the Ilbert Bill and Ripon, asked twice). "
    "Family: Lytton (Vernacular Press Act 1878, Arms Act 1878, Second Afghan War); Ripon (Hunter Commission 1882, First Factory Act 1881); Curzon (Partition of Bengal).",
    k="not")

# 50 education: Sadler
add(H, "Which commission, set up in 1917, studied the problems of the Calcutta University and made suggestions for the whole country?",
    ["Sadler Commission", "Hunter Commission", "Hartog Committee", "Raleigh Commission"],
    "Why: the Calcutta University Commission under Michael Sadler (1917–19) suggested a separate Intermediate stage and a new type of university. "
    "Grew from: 2025 Q81 (the order of Hartog, Hunter, Sadler and Kothari). "
    "Family: Hunter 1882 (primary and secondary), Raleigh 1902 (universities, then the Universities Act of 1904), Sadler 1917, Hartog 1929 (primary), Sargent 1944, Radhakrishnan 1948 (university), Kothari 1964.")
