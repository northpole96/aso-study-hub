# GS Modern History Mock 02: 100 sibling questions on syllabus topic (c) (24 Nov 2026).
# User's brief: not 2 questions per original; each Mock 01 question gets as many neighbours as it truly has
# (Dandi date -> Quit India date, NCM date ...), quality over count. Same question shape, another member of the family.
# First option is right unless a is given.

S12 = ["Only 1", "Only 2", "Both 1 and 2", "Neither 1 nor 2"]
S3 = ["Only 1 and 2", "Only 2 and 3", "Only 1 and 3", "1, 2 and 3"]
def M(a, b, c, d):
    return "a-%d, b-%d, c-%d, d-%d" % (a, b, c, d)

META = dict(
    paper="ga",
    title="ASO GS Modern History Mock 02",
    hub_title="Modern History 100 · GS Mock 02",
    link_title="Modern History 100 mock",
    masthead="GS History 02",
    heading="General Studies Paper I · Modern History Mock 02",
    tagline="100 sibling questions on<br><b>British rule and the freedom struggle</b><br>neighbours of Mock 01.",
    key="aso-gs-history-2",
    code="HIS2",
    out="ASO-GS-Mock-Modern-History-2.html",
    minutes=90,
    seed=241125,
    order="mixed",
    topic="his",
    date="24 Nov 2026",
    draw="hand-built siblings of Modern History Mock 01 (families from draw.py ga --topics his)",
    intro=[
        "This mock is the sibling set of Modern History Mock 01. If Mock 01 asked when the Dandi March began, this mock asks about the movements next to it: the Non-Cooperation Movement, the Rowlatt Satyagraha, the Cripps Mission. Each question has the same shape as its original but tests a different member of the same family. The examiner often does this: the Ilbert Bill came in 2018 and again in 2025, and the 2025 paper asked three Congress-session questions on three different sessions.",
        "No original got a fixed number of siblings. A family with many well-known neighbours (the Congress sessions, the newspapers, the Viceroys, the 1857 centres) got many questions. A family with no real neighbours got none. No answer here repeats a Mock 01 answer. The key is from standard textbooks, as there is no official key. Three questions carry CHECK.",
    ],
)

Q = []
def add(s, q, o, e, k="one", n=False, c=False, a=None, **x):
    d = dict(s=s, q=q, o=o, e=e, k=k, n=n, c=c, a=a); d.update(x); Q.append(d)

H = "Modern History"

# ================================================================ A. Gandhi era, war years and the end of British rule
# (neighbours of: Dandi date, Chauri Chaura, Champaran, Gandhi-Irwin, Quit India)

add(H, "The Dandi March of March 1930 began from which place?",
    ["Sabarmati Ashram, Ahmedabad", "Sevagram, Wardha", "Champaran, Bihar", "Bardoli, Gujarat"],
    "Why: Gandhi and 78 followers left the Sabarmati Ashram on 12 March 1930 and walked about 240 miles to Dandi, where he broke the salt law on 6 April. Sevagram came later (1936) and Bardoli is linked to the 1928 farmers' satyagraha. "
    "Sibling of: the date of the Dandi March (2018 Q32). "
    "Family: salt tax, Civil Disobedience Movement 1930, Gandhi-Irwin Pact 1931; in Odisha the salt law was broken at Inchudi.")

add(H, "The Non-Cooperation Movement was formally launched on:",
    ["1 August 1920", "13 April 1919", "12 March 1930", "8 August 1942"],
    "Why: the movement began on 1 August 1920, the day Tilak died. Gandhi gave back his Kaiser-i-Hind medal that day. The Congress approved it at the special Calcutta session in September 1920 and confirmed it at Nagpur in December. "
    "Sibling of: the Dandi date (2018 Q32) and the order of movements (2018 Q87). "
    "Family: 13 April 1919 is Jallianwala Bagh; 12 March 1930 is Dandi; 8 August 1942 is the Quit India resolution.")

add(H, "The Hunter Committee (1919) was appointed to inquire into which event?",
    ["The Jallianwala Bagh massacre", "The Chauri Chaura violence", "The Moplah rebellion", "The Rowlatt Satyagraha"],
    "Why: after General Dyer's firing at Amritsar on 13 April 1919, the Government named the Hunter Committee. The Congress set up its own committee under Motilal Nehru, and Gandhi was on it. The 'Hunter Commission' of 1882 on education is the trap. "
    "Sibling of: Chauri Chaura, the other violent event that shaped Gandhi's movements. "
    "Family: Tagore gave up his knighthood and Gandhi his Kaiser-i-Hind medal after it.")

add(H, "The Rowlatt Act of 1919 allowed the Government to:",
    ["Jail a person without trial for up to two years", "Ban all newspapers in Indian languages", "Collect extra land revenue in war time", "Appoint only British judges in the High Courts"],
    "Why: the Act (Anarchical and Revolutionary Crimes Act) let the Government hold suspects without trial, which gave the slogan 'No dalil, no vakil, no appeal'. Gandhi began the Rowlatt Satyagraha against it in April 1919. "
    "Sibling of: Chauri Chaura (the end of Non-Cooperation) and the Gandhi movements in an order question (2018 Q87). "
    "Family: Rowlatt 1919, Jallianwala Bagh 1919, Non-Cooperation 1920.")

add(H, "Gandhi first used a fast as a weapon in India during which struggle?",
    ["The Ahmedabad mill strike (1918)", "The Champaran satyagraha (1917)", "The Kheda satyagraha (1918)", "The Dandi March (1930)"],
    "Why: in the Ahmedabad mill strike, workers wanted a 35 per cent rise, and Gandhi fasted to keep them firm. The mill-owners gave in. The three early struggles are often mixed up, so remember Champaran as indigo, Ahmedabad as the fast and Kheda as the tax. "
    "Sibling of: Champaran and indigo. "
    "Family: Ahmedabad Textile Labour Association (Gandhi, 2018 Q67); Kheda in Gujarat.")

add(H, "The Kheda Satyagraha of 1918 was a protest for:",
    ["Remission of land revenue after a failed crop", "Wages for mill workers", "Freedom of the press", "The end of the indigo system"],
    "Why: the crops in Kheda (Gujarat) failed, but the Government still asked for the revenue. Gandhi and Sardar Patel led the farmers to refuse to pay until it was waived for the poor. "
    "Sibling of: Champaran, where the issue was indigo. "
    "Family: Champaran 1917 (indigo), Ahmedabad 1918 (wages), Kheda 1918 (revenue), Bardoli 1928 (revenue, Patel gained the name 'Sardar').")

add(H, "The Cripps Mission of 1942 offered India:",
    ["Dominion status after the war and a Constituent Assembly", "Complete independence at once", "Provincial autonomy only", "A single federal Parliament with no princes"],
    "Why: Sir Stafford Cripps came in March 1942 as Japan neared India. The offer was Dominion status once the war ended and a Constituent Assembly, and each province could stay out. Gandhi called it a 'post-dated cheque on a failing bank'. "
    "Sibling of: the Quit India resolution (August 1942), which followed its failure. "
    "Family: August Offer 1940, Cripps 1942, Quit India 1942, Wavell Plan 1945, Cabinet Mission 1946.")

add(H, "Who was chosen as the first individual satyagrahi in 1940?",
    ["Vinoba Bhave", "Jawaharlal Nehru", "Rajendra Prasad", "Maulana Azad"],
    "Why: after the August Offer was rejected, Gandhi chose select people to protest one by one. Vinoba Bhave (at Paunar) was the first and Nehru the second. "
    "Sibling of: the Quit India movement (the mass movement that followed in 1942). "
    "Family: the August Offer by Linlithgow (1940), Individual Satyagraha (1940–41), Cripps (1942).")

add(H, "Which of the following was NOT a member of the Cabinet Mission of 1946?",
    ["Lord Wavell", "Lord Pethick-Lawrence", "Sir Stafford Cripps", "A. V. Alexander"],
    "Why: the Cabinet Mission had three British Cabinet ministers: Pethick-Lawrence (Secretary of State), Cripps and A. V. Alexander. Lord Wavell was the Viceroy at the time, and he met the Mission but was not a member. "
    "Sibling of: the Cripps Mission (1942), because Cripps came twice. "
    "Family: the Mission proposed a three-tier Union with groups A, B and C, a Constituent Assembly and an Interim Government.",
    k="not")

add(H, "On which day did the Muslim League observe 'Direct Action Day' in 1946?",
    ["16 August 1946", "9 August 1946", "26 January 1946", "14 August 1947"],
    "Why: the League withdrew its acceptance of the Cabinet Mission plan and called for Direct Action on 16 August 1946. Riots broke out in Calcutta. "
    "Sibling of: the Cabinet Mission and the 1946 timeline. "
    "Family: Interim Government (September 1946, Nehru as Vice-President of the Viceroy's Council); Mountbatten Plan (3 June 1947).")

add(H, "Who headed the Boundary Commission that drew the line between India and Pakistan in 1947?",
    ["Cyril Radcliffe", "Lord Mountbatten", "Lord Wavell", "Sir Stafford Cripps"],
    "Why: Cyril Radcliffe, a British lawyer, was named chairman of the two Boundary Commissions (Punjab and Bengal). The 'Radcliffe Line' was made public on 17 August 1947, two days after independence. "
    "Sibling of: the Poona Pact and Gandhi–Irwin Pact on the 'pact or plan' side of the freedom story. "
    "Family: Mountbatten Plan (3 June 1947); Indian Independence Act (18 July 1947 by royal assent).")

add(H, "Who announced in February 1947 that Britain would leave India by June 1948?",
    ["Clement Attlee", "Winston Churchill", "Ramsay MacDonald", "Lord Mountbatten"],
    "Why: the British Prime Minister Clement Attlee gave this in the House of Commons on 20 February 1947 and named Mountbatten as the new Viceroy. Mountbatten then moved the date forward to 15 August 1947. "
    "Sibling of: the Cripps Mission and Cabinet Mission, other British moves of the war and post-war years. "
    "Family: Ramsay MacDonald announced the Communal Award in 1932, and Churchill was the wartime Prime Minister.")

add(H, "Who among the following was NOT tried in the first Red Fort INA trials (1945–46)?",
    ["Mohan Singh", "Shah Nawaz Khan", "P. K. Sahgal", "Gurbaksh Singh Dhillon"],
    "Why: the first trial held a Muslim (Shah Nawaz Khan), a Hindu (Sahgal) and a Sikh (Dhillon) together, so the country stood united behind them. Mohan Singh had formed the first INA in 1942 and was not in this trial. "
    "Sibling of: Bose and the INA (2018 Q33, the Provisional Government in Singapore). "
    "Family: Bhulabhai Desai led the defence; Nehru put on his lawyer's gown for the first time in years.",
    k="not")

add(H, "The Royal Indian Navy mutiny of February 1946 began on which ship, at which port?",
    ["HMIS Talwar, Bombay", "HMIS Hindustan, Madras", "HMIS Bahadur, Karachi", "HMIS Godavari, Calcutta"],
    "Why: ratings on HMIS Talwar in Bombay struck on 18 February 1946 over food and racial treatment. The revolt spread to many ports. It shook the British, who saw that even the forces could no longer be relied on. "
    "Sibling of: the INA trials of the same winter. "
    "Family: the trials, the naval mutiny and the Cabinet Mission together pushed the date of independence closer.",
    c=True)

add(H, "The Irwin Declaration of October 1929 stated that:",
    ["Dominion status was the goal of British policy for India", "India would be given complete independence in one year", "The Simon Commission would be dissolved", "Separate electorates would end"],
    "Why: Lord Irwin said on 31 October 1929 that the natural issue of India's progress was Dominion status. A Round Table Conference would follow. The Congress answered at Lahore with Poorna Swaraj. "
    "Sibling of: the Poorna Swaraj date (2025 Q54) and the Gandhi–Irwin Pact. "
    "Family: Nehru Report (1928); Simon Commission (1927); Round Table Conferences (1930–32).")

# ================================================================ B. Congress, sessions and parties
# (neighbours of: Lahore president, Lucknow 1916, Tripuri 1939, Poorna Swaraj, first Indian woman president)

add(H, "The Congress split into the Moderates and the Extremists at Surat in 1907. Who presided over that session?",
    ["Rash Behari Ghosh", "Dadabhai Naoroji", "Lala Lajpat Rai", "Surendranath Banerjee"],
    "Why: the Extremists wanted Lala Lajpat Rai as president, the Moderates wanted Rash Behari Ghosh, and the session ended in a clash. Tilak was shut out of the Congress until 1916. "
    "Sibling of: the Lucknow 1916 president (Ambika Charan Mazumdar), which brought them back. "
    "Family: Naoroji's 1906 Calcutta address first named 'swaraj' as the goal.")

add(H, "The special session of the Congress at Calcutta in September 1920 that approved Non-Cooperation was presided over by:",
    ["Lala Lajpat Rai", "C. Vijayaraghavachariar", "Motilal Nehru", "C. R. Das"],
    "Why: Lajpat Rai presided over the special Calcutta session where Gandhi's resolution on Non-Cooperation was passed. The Nagpur session in December 1920 under C. Vijayaraghavachariar confirmed it. "
    "Sibling of: Lahore 1929 (Nehru) and Lucknow 1916 (Mazumdar). "
    "Family: C. R. Das first opposed the plan at Calcutta, then supported it at Nagpur.")

add(H, "Who presided over the Karachi session of the Congress in 1931?",
    ["Sardar Vallabhbhai Patel", "Jawaharlal Nehru", "Motilal Nehru", "Madan Mohan Malaviya"],
    "Why: Patel presided in March 1931, days after the Gandhi-Irwin Pact, and the session endorsed the Pact. The Fundamental Rights and Economic Programme resolution was also passed there. 2025's Q31 had 'Motilal Nehru' as the false option (he had died in 1931). "
    "Sibling of: the Lahore president (2025 Q54, 2025 Q31). "
    "Family: this was the only Congress session Patel presided over.")

add(H, "Who was the first Muslim President of the Indian National Congress (1887)?",
    ["Badruddin Tyabji", "Rahimtulla Sayani", "Muhammad Ali Jinnah", "Sir Syed Ahmad Khan"],
    "Why: Badruddin Tyabji presided at Madras in 1887. Sir Syed Ahmad Khan opposed the Congress and told Muslims to stay away. "
    "Sibling of: the first woman and first Indian woman president (Annie Besant and Sarojini Naidu). "
    "Family: Rahimtulla Sayani presided in 1896 and Maulana Azad in 1923 (youngest) and 1940–46.")

add(H, "Who was the first woman President of the Indian National Congress?",
    ["Annie Besant", "Sarojini Naidu", "Nellie Sengupta", "Sucheta Kripalani"],
    "Why: Annie Besant presided at Calcutta in 1917, soon after she started her Home Rule League. Sarojini Naidu was the first Indian woman (1925), and Nellie Sengupta (1933) was the first Indian-born woman after her. "
    "Sibling of: the first Indian woman president (Sarojini Naidu). "
    "Family: Besant was Irish and a leader of the Theosophical Society; she was jailed in 1917.")

add(H, "Which Congress session of December 1927 first passed a resolution for 'complete independence', and who presided over it?",
    ["M. A. Ansari at Madras", "Motilal Nehru at Calcutta", "Jawaharlal Nehru at Lahore", "Gandhi at Belgaum"],
    "Why: the Madras session of 1927 under Dr M. A. Ansari first passed a resolution for complete independence, and also decided to boycott the Simon Commission. Poorna Swaraj in 1929 only made it formal. "
    "Sibling of: the Poorna Swaraj date (2025 Q54) and the Lahore president. "
    "Family: Calcutta 1928 (Motilal) gave the Government one year to accept Dominion status.")

add(H, "The Nehru Report of 1928 was drawn up by a committee headed by:",
    ["Motilal Nehru", "Jawaharlal Nehru", "Tej Bahadur Sapru", "C. R. Das"],
    "Why: an All Parties Conference chose Motilal Nehru to chair the committee, which answered Lord Birkenhead's challenge to frame a Constitution. The report demanded Dominion status and no separate electorates. "
    "Sibling of: the Simon Commission, which it replied to. "
    "Family: Jinnah's Fourteen Points (1929) answered it; the Congress at Calcutta 1928 accepted it.")

add(H, "Jinnah's Fourteen Points of 1929 were presented in reply to:",
    ["The Nehru Report", "The Cripps Proposals", "The Communal Award", "The Simon Commission Report"],
    "Why: the Nehru Report gave up separate electorates, which the League opposed. Jinnah put his demands as fourteen points in March 1929. "
    "Sibling of: the Nehru Report. "
    "Family: the League's Lahore Resolution (1940) and Iqbal's Allahabad address (1930).")

add(H, "Which was the first session of the Congress to be held in a village?",
    ["Faizpur, 1936", "Haripura, 1938", "Ramgarh, 1940", "Tripuri, 1939"],
    "Why: the Faizpur session (Maharashtra), presided over by Nehru, was in a village. Gandhi wanted the Congress to go closer to the farmers. Haripura (1938) was also rural, but Faizpur came first. "
    "Sibling of: Tripuri 1939 (Bose defeated Pattabhi Sitaramayya). "
    "Family: the 1936–37 elections under the 1935 Act; Nehru's agrarian programme.")

add(H, "Annie Besant started her Home Rule League in 1916 at:",
    ["Adyar, Madras", "Poona", "Calcutta", "Lucknow"],
    "Why: Besant's League began in September 1916 at Adyar (Madras). Tilak's League began at Belgaum/Poona in April 1916. Both asked for self-government within the Empire during the First World War. "
    "Sibling of: the Lucknow 1916 session, which saw Moderates and Extremists meet again. "
    "Family: Besant's paper New India; Tilak's slogan 'Swaraj is my birthright'.")

add(H, "The Swaraj Party (1923), formed to contest the Councils, was founded by:",
    ["C. R. Das and Motilal Nehru", "Gandhi and Patel", "Tilak and Gokhale", "Jinnah and Ali brothers"],
    "Why: after Non-Cooperation ended, a group inside the Congress led by C. R. Das and Motilal Nehru, called the 'Pro-Changers', wanted to enter the Legislative Councils to fight the Government from within. Gandhi's group, the 'No-Changers', opposed it. "
    "Sibling of: Chauri Chaura (which ended Non-Cooperation). "
    "Family: the Swaraj Party won seats in the 1923 elections; Vithalbhai Patel became Speaker of the Central Assembly.")

add(H, "Lala Lajpat Rai was fatally injured in a lathi-charge in 1928 while leading a protest against:",
    ["The Simon Commission", "The Rowlatt Act", "The Partition of Bengal", "The Salt Tax"],
    "Why: the Simon Commission had no Indian member. At Lahore, the police beat Lajpat Rai and he died on 17 November 1928. Bhagat Singh and others then killed Saunders in revenge. "
    "Sibling of: 2025 Q96 (statements about Lala Lajpat Rai). "
    "Family: 'The day of my death will be the last day of British rule' is attributed to him; the slogan 'Simon Go Back'.")

add(H, "The Communal Award of 1932 was announced by:",
    ["Ramsay MacDonald", "Lord Willingdon", "Clement Attlee", "Winston Churchill"],
    "Why: the British Prime Minister Ramsay MacDonald gave separate electorates to the depressed classes, Muslims and others. Gandhi fasted against it and the Poona Pact followed. "
    "Sibling of: the Poona Pact, the move that undid it. "
    "Family: the Third Round Table Conference (1932); the Government of India Act 1935.")

add(H, "The August Offer of 1940, which promised a Constituent body after the war, was made by Viceroy:",
    ["Lord Linlithgow", "Lord Wavell", "Lord Irwin", "Lord Willingdon"],
    "Why: Linlithgow made the offer on 8 August 1940. The Congress rejected it, and the Individual Satyagraha followed. "
    "Sibling of: the Cripps Mission (1942) and Quit India (August 1942). "
    "Family: Linlithgow was Viceroy 1936–43; Wavell 1943–47; Mountbatten 1947.")

# ================================================================ C. Newspapers, books and writers (the user's first family)
# (neighbours of: Pratap, Hindu, Young India, Bombay Times, Amrita Bazar Patrika, Hind Swaraj, Gita Rahasya)

add(H, "Maulana Abul Kalam Azad started which Urdu weekly in 1912?",
    ["Al-Hilal", "Comrade", "Hamdard", "Zamindar"],
    "Why: Al-Hilal, in Calcutta, spoke against British rule and was banned by the Government in 1914. Azad then started Al-Balagh. Comrade (English) and Hamdard (Urdu) were Muhammad Ali's papers. "
    "Sibling of: the Bande Mataram, Comrade and Mooknayak pairs in the NOT-correct press question. "
    "Family: Azad wrote 'India Wins Freedom' and became Congress president in 1923 at 35.")

add(H, "Tilak's papers Kesari and Mahratta were published in which languages?",
    ["Marathi and English", "English and Marathi", "Hindi and English", "Marathi and Gujarati"],
    "Why: Kesari (1881) was the Marathi paper and Mahratta the English paper. Tilak and Agarkar began them together, and later Tilak ran them alone. They were the basis of his case for sedition. "
    "Sibling of: Kesari – Tilak, a pair from the press question. "
    "Family: Tilak was jailed in 1897 and sent to Mandalay in 1908.")

add(H, "Yugantar (1906), the Bengali revolutionary weekly, was started by:",
    ["Barindra Kumar Ghosh and Bhupendranath Datta", "Bipin Chandra Pal", "Surendranath Banerjee", "Aurobindo Ghose alone"],
    "Why: Barindra Kumar Ghosh, Aurobindo's brother, and Bhupendranath Datta, Vivekananda's brother, began Yugantar in Calcutta. It taught revolutionary ideas and led to the Alipore bomb case of 1908. "
    "Sibling of: Bande Mataram (Bipin Chandra Pal and Aurobindo). "
    "Family: Anushilan Samiti; Sandhya (Brahmabandhab Upadhyay).")

add(H, "Gandhi began his journal 'Indian Opinion' in 1903 in which country?",
    ["South Africa", "India", "England", "Burma"],
    "Why: Gandhi started Indian Opinion at Durban to tell the Indian community's story. He later edited Young India and Navajivan in India, and Harijan from 1933. "
    "Sibling of: 'Young India was published by Gandhi' (2025 Q64). "
    "Family: Gandhi's books: Hind Swaraj (1909), My Experiments with Truth, Satyagraha in South Africa.")

add(H, "'Amrita Bazar Patrika' changed from a Bengali to an English paper in 1878 to avoid which law?",
    ["The Vernacular Press Act", "The Indian Press Act of 1910", "The Rowlatt Act", "The Arms Act"],
    "Why: the Vernacular Press Act (1878) only controlled Indian-language papers, so the Ghosh brothers (Sisir Kumar and Motilal) turned their paper into an English one overnight. "
    "Sibling of: 'Amrita Bazar Patrika was founded by Sisir Kumar Ghosh' (2025 Q64) and the Vernacular Press Act. "
    "Family: the Act was passed by Lytton and repealed by Ripon in 1882.")

add(H, "'The Hindu' was started in 1878 at:",
    ["Madras", "Calcutta", "Bombay", "Poona"],
    "Why: it began as a weekly at Madras, and G. Subramania Iyer and others were among its founders. It later became a daily. Iyer also started the Tamil paper Swadesamitran. "
    "Sibling of: 'Hindu was founded by G. Subramania Iyer' (2025 Q64). "
    "Family: Madras Mahajana Sabha (1884); The Hindu's early support for Moderate causes.")

add(H, "The 'Bombay Chronicle' (1910), a nationalist paper, was started by:",
    ["Pherozeshah Mehta", "Dadabhai Naoroji", "G. K. Gokhale", "Tilak"],
    "Why: Mehta started it and it was edited by B. G. Horniman, an Englishman who backed Indian freedom. The Government deported Horniman during the First World War. "
    "Sibling of: 'Bombay Times was founded by...' (2025 Q64). Bombay Times was a British paper and became the Times of India. "
    "Family: Pherozeshah Mehta, 'Lion of Bombay', was one of the founders of the Congress.")

add(H, "Motilal Nehru started which English daily at Allahabad in 1919?",
    ["The Independent", "The Leader", "National Herald", "The Pioneer"],
    "Why: The Independent was Motilal's paper, started in 1919. The Leader was started by Madan Mohan Malaviya (1909) at Allahabad, and the Pioneer was a British paper. Nehru started the National Herald in 1938. "
    "Sibling of: 'Nehru founded the National Herald' (2021 Q28). "
    "Family: Hindustan Times (1924); Pratap (Ganesh Shankar Vidyarthi, Kanpur).")

add(H, "Raja Ram Mohan Roy's Bengali weekly (1821) was:",
    ["Sambad Kaumudi", "Mirat-ul-Akhbar", "Bengal Gazette", "Dig-Darshan"],
    "Why: Sambad Kaumudi was a Bengali weekly. His Persian paper was Mirat-ul-Akhbar. James Hicky's Bengal Gazette (1780) was the first newspaper in India. "
    "Sibling of: the press and press-law family (1799, 1823, 1835). "
    "Family: Roy stopped Mirat-ul-Akhbar in 1823 in protest against the licensing ordinance.")

add(H, "Utkal Dipika, an early Odia weekly (1866), was started at:",
    ["Cuttack", "Balasore", "Puri", "Sambalpur"],
    "Why: it began at Cuttack in 1866 under the leadership of Gauri Shankar Ray, and helped to spread the idea of a united Odisha. Bodhadayini (1861, Balasore) is often called the first Odia paper. "
    "Sibling of: Utkal Dipika in the press family (Kesari, Mahratta, Bengalee, Al-Hilal). "
    "Family: Madhusudan Das and the Utkal Sammilani later used it.",
    c=True)

add(H, "'India Wins Freedom', an account of the last years of British rule, was written by:",
    ["Maulana Abul Kalam Azad", "Jawaharlal Nehru", "Sardar Patel", "Rajendra Prasad"],
    "Why: Azad wrote it with Humayun Kabir's help and kept thirty pages sealed until 1988. Nehru's 'Discovery of India' was a different book. "
    "Sibling of: 'Discovery of India – Nehru' in the book pairs. "
    "Family: Nehru's 'An Autobiography'; Rajendra Prasad's 'India Divided'.")

add(H, "Match the books with their authors:\nList I\na. India Divided\nb. Unhappy India\nc. The Indian Struggle\nd. The Life Divine\nList II\n1. Aurobindo Ghose\n2. Lala Lajpat Rai\n3. Rajendra Prasad\n4. Subhas Chandra Bose",
    [M(3, 2, 4, 1), M(2, 3, 4, 1), M(3, 2, 1, 4), M(3, 4, 2, 1)],
    "Why: Rajendra Prasad wrote 'India Divided' (1946); Lajpat Rai wrote 'Unhappy India' as a reply to Katherine Mayo's 'Mother India'; Bose wrote 'The Indian Struggle' and Aurobindo wrote 'The Life Divine'. "
    "Sibling of: the book and author pairs in 2021 Q28 and 2018 Q25. "
    "Family: Gandhi's 'Hind Swaraj'; Savarkar's 'The Indian War of Independence'; Tilak's 'Gita Rahasya'.",
    k="match", a=0)

add(H, "Rabindranath Tagore gave up his knighthood in 1919 as a protest against:",
    ["The Jallianwala Bagh massacre", "The Partition of Bengal", "The Rowlatt Act", "The Simon Commission"],
    "Why: Tagore wrote to the Viceroy saying he wished to stand 'shorn of all special distinctions' with his countrymen after the Amritsar firing. He had won the Nobel Prize in 1913 for Gitanjali. "
    "Sibling of: Anandamath and Neel Darpan (Bengali writings of the freedom struggle). "
    "Family: Tagore wrote the national anthem and the song 'Amar Sonar Bangla'.")

add(H, "'The Economic History of India', a work that criticised British economic policy, was written by:",
    ["R. C. Dutt", "Dadabhai Naoroji", "G. K. Gokhale", "Justice Ranade"],
    "Why: Romesh Chunder Dutt wrote it in 1901–03 and used British records to show how the Drain of Wealth and heavy revenue ruined the farmers. He presided over the Congress in 1899. "
    "Sibling of: Naoroji's 'Poverty and Un-British Rule in India', the other great work on the drain. "
    "Family: the Drain of Wealth theory; the Famine Commissions of 1880, 1898 and 1901.")

add(H, "The Vernacular Press Act of 1878 was repealed in 1882 under:",
    ["Lord Ripon", "Lord Lytton", "Lord Curzon", "Lord Canning"],
    "Why: Lytton passed it to control the papers in Indian languages. Ripon repealed it and gave local self-government (1882). This is the same Ripon as in the Ilbert Bill question. "
    "Sibling of: the Censorship Act of 1799 (2025 Q30) and Metcalfe's 1835 act. "
    "Family: Lytton: Delhi Durbar 1877, Arms Act 1878.")

add(H, "Bal Gangadhar Tilak was sent to the Mandalay jail in 1908 for writings in his paper:",
    ["Kesari", "Mahratta", "Indian Mirror", "Bande Mataram"],
    "Why: Tilak's articles in Kesari on the Muzaffarpur bomb were called seditious, and he got six years in Mandalay (Burma). In 1897 he had first been jailed for sedition too. "
    "Sibling of: the Kesari – Tilak pair and the Censorship and Press Acts. "
    "Family: in Mandalay he wrote Gita Rahasya.")

# ================================================================ D. Acts and Viceroys
# (neighbours of: Ilbert Bill and Ripon, Partition of Bengal and Curzon, diarchy 1919, Acts wrongly matched)

add(H, "Queen Victoria was proclaimed Empress of India at the Delhi Durbar of 1877 under:",
    ["Lord Lytton", "Lord Ripon", "Lord Curzon", "Lord Dufferin"],
    "Why: Lytton held the Durbar while a famine was killing millions. Curzon held his own Durbar in 1903 for Edward VII. "
    "Sibling of: the Ilbert Bill question (Ripon, 2018 Q86 and 2025 Q10). "
    "Family: Lytton passed the Vernacular Press Act and the Arms Act in 1878.")

add(H, "The first railway line in India (1853) ran between:",
    ["Bombay and Thane", "Calcutta and Hooghly", "Madras and Arakkonam", "Delhi and Agra"],
    "Why: the 34 km line from Bombay (Bori Bunder) to Thane opened on 16 April 1853 under Dalhousie. He is also called the 'Father of Indian Railways'. "
    "Sibling of: Doctrine of Lapse (Dalhousie). "
    "Family: telegraph (1851), Post Office Act 1854, Wood's Despatch 1854.")

add(H, "Sati was made illegal in 1829 under the Governor-General:",
    ["Lord William Bentinck", "Lord Cornwallis", "Lord Dalhousie", "Lord Canning"],
    "Why: Bentinck passed the Regulation XVII of 1829 with Ram Mohan Roy's support. He also suppressed thagi and used English in higher education. "
    "Sibling of: the Widow Remarriage Act (Vidyasagar, 1856). "
    "Family: Bentinck was the first Governor-General of India (1833).")

add(H, "In 1911, the announcement that the capital would move from Calcutta to Delhi was made at a Durbar under Viceroy:",
    ["Lord Hardinge", "Lord Curzon", "Lord Minto", "Lord Chelmsford"],
    "Why: King George V announced it at the Delhi Durbar of December 1911. The partition of Bengal was undone in the same announcement. A bomb was thrown at Hardinge in 1912. "
    "Sibling of: Partition of Bengal (Curzon). "
    "Family: New Delhi was built by Lutyens and Baker and inaugurated in 1931.")

add(H, "Who was the first Indian to hold the office of Governor-General of independent India?",
    ["C. Rajagopalachari", "Rajendra Prasad", "Lord Mountbatten", "Sardar Patel"],
    "Why: Mountbatten was the last Viceroy and the first Governor-General of free India. When he left in June 1948, Rajagopalachari (Rajaji) took over and remained till January 1950. "
    "Sibling of: the first Viceroy (Canning) and other 'firsts'. "
    "Family: Rajendra Prasad became the first President in 1950.")

add(H, "The system of dual control over the Company by the Board of Control and the Court of Directors began with:",
    ["Pitt's India Act, 1784", "The Regulating Act, 1773", "The Charter Act of 1833", "The Act of 1858"],
    "Why: Pitt's India Act made the Board of Control (a Crown body) watch the Company's political work, while the Directors kept trade and patronage. The Act of 1858 ended both. "
    "Sibling of: the Acts matched with their features (2025 Q76). "
    "Family: Regulating Act 1773; Pitt's Act 1784; Charter Acts 1813, 1833, 1853.")

add(H, "The Regulating Act of 1773 made the Governor of Bengal the:",
    ["Governor-General of Bengal", "Viceroy of India", "Governor-General of India", "Chief Justice of Calcutta"],
    "Why: Warren Hastings became the first Governor-General of Bengal, with a Council of four. The Act also set up the Supreme Court at Calcutta (1774). Bentinck was the first Governor-General of India after 1833. "
    "Sibling of: the Supreme Court and Elijah Impey (2025 Q45). "
    "Family: the Act of 1773 was the first Parliament move to control the Company.")

add(H, "Consider the following statements about the Government of India Act, 1935:\n1. It introduced provincial autonomy.\n2. It provided for an All-India Federation.\n3. It abolished the office of the Secretary of State for India.\nWhich of the statements given above is/are correct?",
    S3,
    "Why: the Act gave autonomy to the provinces and planned a Federation of provinces and princely states, which never began because the princes did not join. The Secretary of State stayed until 1947, but his Council was dropped. So statements 1 and 2 are true and 3 is false. "
    "Sibling of: the Act that created provincial autonomy and the Federal Court (2025 Q38). "
    "Family: Burma separated in 1937; Orissa and Sind created in 1936; the Federal Court was set up at Delhi in 1937.",
    k="stmt", a=0)

# ================================================================ E. The Revolt of 1857
# (neighbours of: Bareilly, Sambalpur, Hugh Rose and Gwalior, the 1857 'wrongly matched' question)

add(H, "Tantia Tope was the general of which leader of 1857?",
    ["Nana Sahib", "Bahadur Shah Zafar", "Begum Hazrat Mahal", "Kunwar Singh"],
    "Why: Nana Sahib, the adopted son of the last Peshwa, was the leader at Kanpur, and Tantia Tope led his army. Tope later joined Lakshmibai. "
    "Sibling of: 'Revolt at Kanpur – Nana Sahib' in the wrongly matched question (2025 Q75). "
    "Family: Tope was captured and hanged in April 1859.")

add(H, "Who led the revolt of 1857 at Lucknow?",
    ["Begum Hazrat Mahal", "Rani Lakshmibai", "Maulvi Ahmadullah", "Liaquat Ali"],
    "Why: Hazrat Mahal, wife of the Nawab Wajid Ali Shah, put her son Birjis Qadr on the throne after Awadh was annexed. Colin Campbell took Lucknow in March 1858. "
    "Sibling of: 'Revolt at Faizabad – Hazrat Mahal' in 2025 Q75, where it was wrongly placed. "
    "Family: Awadh annexed in 1856; its soldiers made up much of the Bengal Army.")

add(H, "Kunwar Singh of Jagdishpur led the revolt of 1857 in which present-day State?",
    ["Bihar", "Uttar Pradesh", "Madhya Pradesh", "Odisha"],
    "Why: Kunwar Singh was an aged zamindar of Jagdishpur (Arrah). He fought until April 1858 and died soon after a victory. "
    "Sibling of: 'Revolt at Jagdishpur – Kunwar Singh' (2025 Q75), now asked as a place. "
    "Family: the other Bihar leader to name is Amar Singh, his brother.")

add(H, "Who led the revolt of 1857 at Faizabad?",
    ["Maulvi Ahmadullah Shah", "Khan Bahadur Khan", "Bakht Khan", "Nana Sahib"],
    "Why: Ahmadullah Shah, the Maulvi of Faizabad, was a leader of the Lucknow revolt too, and he was killed in 1858. "
    "Sibling of: Bareilly (Khan Bahadur Khan) and Delhi (Bakht Khan). "
    "Family: Awadh and Rohilkhand were the heart of the revolt.")

add(H, "Which sepoy of the 34th Native Infantry attacked British officers at Barrackpore on 29 March 1857?",
    ["Mangal Pandey", "Tantia Tope", "Bakht Khan", "Shah Nawaz Khan"],
    "Why: Pandey was hanged in April 1857, but the main revolt began at Meerut on 10 May. 2018 Q29 asked where the revolt was 'kindled' (Meerut). "
    "Sibling of: the place of the first outbreak. "
    "Family: the cause was the greased cartridge; Barrackpore was near Calcutta.")

add(H, "The immediate cause of the Revolt of 1857 was the introduction of:",
    ["Cartridges greased with animal fat for the Enfield rifle", "The Doctrine of Lapse", "The Vernacular Press Act", "The Permanent Settlement"],
    "Why: the sepoys had to bite the cartridges, and they thought the grease was cow and pig fat. That hurt both Hindus and Muslims. Lapse, taxes and the annexation of Awadh were the long-term causes. "
    "Sibling of: 'where was the revolt kindled?' (2018 Q29). "
    "Family: Mangal Pandey, Meerut (10 May 1857), Delhi, Kanpur.")

add(H, "Queen Victoria's Proclamation of 1858 was read out at a Durbar at Allahabad by:",
    ["Lord Canning", "Lord Dalhousie", "Lord Lytton", "Lord Ripon"],
    "Why: Canning read it on 1 November 1858. It promised no more annexations and equal treatment, and it respected religion. "
    "Sibling of: the 1858 Act that ended the Company. "
    "Family: Canning, the 'Clemency Canning', was both the last Governor-General and the first Viceroy.")

add(H, "After the Revolt of 1857, the last Mughal emperor, Bahadur Shah Zafar, was exiled to:",
    ["Rangoon", "Mandalay", "Port Blair", "Calcutta"],
    "Why: Hodson captured him at Humayun's Tomb in September 1857. He was tried, sent to Rangoon and died there in 1862. His sons were shot. "
    "Sibling of: the Delhi centre of 1857 and Bakht Khan. "
    "Family: Tilak was sent to Mandalay and the Andamans held the Cellular Jail.")

# ================================================================ F. Revolutionaries, INA and leaders
# (neighbours of: Chittagong, Kakori, Komagata Maru, titles of leaders, Bose)

add(H, "Who, with Bhagat Singh, threw bombs in the Central Legislative Assembly on 8 April 1929?",
    ["Batukeshwar Dutt", "Sukhdev", "Rajguru", "Chandrashekhar Azad"],
    "Why: they threw harmless bombs and leaflets to protest the Public Safety and Trade Disputes Bills and then gave themselves up. Sukhdev and Rajguru were hanged with Bhagat Singh in 1931. "
    "Sibling of: the Chittagong raid and Kakori (Mock 01). "
    "Family: HSRA formed in 1928; Lahore Conspiracy Case.")

add(H, "Bhagat Singh and his comrades killed the police officer Saunders in December 1928 to avenge the death of:",
    ["Lala Lajpat Rai", "Chittaranjan Das", "Tilak", "Khudiram Bose"],
    "Why: the lathi-charge at Lahore killed Lajpat Rai (Simon Commission protest). The HSRA shot Saunders. "
    "Sibling of: the Lajpat Rai question and the Chittagong raid (1930). "
    "Family: HSRA led by Chandrashekhar Azad as commander.")

add(H, "Chandrashekhar Azad died in 1931 in a shoot-out at Alfred Park in:",
    ["Allahabad", "Lahore", "Kanpur", "Delhi"],
    "Why: surrounded by police, he shot himself with his last bullet. He had sworn to remain 'Azad' (free). "
    "Sibling of: the Kakori case (HRA) and Bhagat Singh. "
    "Family: Azad led the HSRA after Bismil's execution.")

add(H, "India House in London (1905), a centre for Indian revolutionaries, was founded by:",
    ["Shyamji Krishna Varma", "Madan Lal Dhingra", "V. D. Savarkar", "Lala Har Dayal"],
    "Why: Shyamji Krishna Varma started India House and the paper 'The Indian Sociologist'. Savarkar later joined; Dhingra shot Curzon Wyllie in 1909. "
    "Sibling of: the Ghadar Party at San Francisco (2018 Q30) and Savarkar's Free India Society. "
    "Family: Madam Cama, Virendranath Chattopadhyaya.")

add(H, "Who unfurled an Indian national flag at the International Socialist Congress at Stuttgart in 1907?",
    ["Madam Bhikaji Cama", "Annie Besant", "Sarojini Naidu", "Aruna Asaf Ali"],
    "Why: Madam Cama raised the flag and called for freedom. She worked with the India House group in Europe. "
    "Sibling of: the first national flag hoisting (2018 Q89). "
    "Family: Aruna Asaf Ali hoisted the flag at Gowalia Tank in 1942.")

add(H, "Who handed over the leadership of the Indian Independence League to Subhas Chandra Bose in 1943?",
    ["Rash Behari Bose", "Mohan Singh", "Lala Har Dayal", "Shah Nawaz Khan"],
    "Why: Rash Behari Bose, who had lived in Japan since 1915, led the League and gave the lead to Subhas Bose in Singapore in July 1943. "
    "Sibling of: Bose's Provisional Government (2018 Q33). "
    "Family: First INA (Mohan Singh, 1942); Second INA (Bose, 1943).")

add(H, "Who commanded the Rani of Jhansi Regiment of the Indian National Army?",
    ["Lakshmi Sahgal (Swaminadhan)", "Sarojini Naidu", "Aruna Asaf Ali", "Kasturba Gandhi"],
    "Why: Captain Lakshmi, a doctor from Madras, commanded the women's regiment that Bose founded in 1943. "
    "Sibling of: Rani Lakshmibai of Jhansi (1857), whose name it bore. "
    "Family: the INA; 'Chalo Delhi'.")

add(H, "The 'Lal-Bal-Pal' trio of the Extremists was made up of:",
    ["Lala Lajpat Rai, Tilak and Bipin Chandra Pal", "Lalmohan Ghosh, Tilak and Pherozeshah Mehta", "Lala Har Dayal, Balwantrai and Pal", "Lalji Mehrotra, Gokhale and Pal"],
    "Why: Lal (Lajpat Rai, Punjab), Bal (Tilak, Maharashtra) and Pal (Bipin Chandra Pal, Bengal) were the leading Extremists during the Swadeshi days. "
    "Sibling of: the titles of leaders (Punjab Kesari, Lokmanya). "
    "Family: the Moderates were Naoroji, Gokhale and Mehta.")

add(H, "Match the title with the leader:\nList I\na. Lok Nayak\nb. Bharat Kokila\nc. Gurudev\nd. Lauh Purush\nList II\n1. Rabindranath Tagore\n2. Sardar Patel\n3. Jayaprakash Narayan\n4. Sarojini Naidu",
    [M(3, 4, 1, 2), M(4, 3, 1, 2), M(3, 4, 2, 1), M(3, 1, 4, 2)],
    "Why: JP is 'Lok Nayak', Sarojini Naidu is the 'Nightingale of India' (Bharat Kokila), Tagore is 'Gurudev' and Patel is the 'Iron Man' (Lauh Purush). "
    "Sibling of: the titles question (Utkal Gourav, Punjab Kesari, Frontier Gandhi, Deshbandhu). "
    "Family: Lokmanya – Tilak; Netaji – Bose; Bapu – Gandhi.",
    k="match", a=0)

# ================================================================ G. Social and religious reform
# (the gap in the three papers: a syllabus line never asked, so likely)

add(H, "The Brahmo Samaj was founded in 1828 by:",
    ["Raja Ram Mohan Roy", "Debendranath Tagore", "Keshab Chandra Sen", "Dayananda Saraswati"],
    "Why: Ram Mohan Roy started it as the Brahmo Sabha in 1828. Debendranath Tagore and Keshab Chandra Sen led it later. "
    "Sibling of: Prarthana Samaj and Arya Samaj pairs in the reform question. "
    "Family: Roy also started Sambad Kaumudi and fought sati.")

add(H, "'Satyarth Prakash', the main book of the Arya Samaj, was written by:",
    ["Dayananda Saraswati", "Swami Vivekananda", "Keshab Chandra Sen", "Ram Mohan Roy"],
    "Why: Dayananda wrote it in Hindi, and it called for a return to the Vedas. He founded the Arya Samaj at Bombay in 1875. "
    "Sibling of: the Arya Samaj – Dayananda pair. "
    "Family: DAV schools; the 'Back to the Vedas' call; shuddhi.")

add(H, "Swami Vivekananda spoke at the Parliament of Religions at Chicago in which year?",
    ["1893", "1875", "1897", "1905"],
    "Why: in September 1893 he spoke of tolerance. He founded the Ramakrishna Mission in 1897 to serve people. "
    "Sibling of: Ramakrishna Mission – Vivekananda. "
    "Family: Belur Math; Ramakrishna Paramhansa.")

add(H, "The Muhammadan Anglo-Oriental (MAO) College at Aligarh was founded in 1875 by:",
    ["Sir Syed Ahmad Khan", "Aga Khan", "Badruddin Tyabji", "Muhammad Iqbal"],
    "Why: Sir Syed wanted Muslims to take up modern English learning. The college later became the Aligarh Muslim University (1920). "
    "Sibling of: the Central National Mohammedan Association (2025 Q57). "
    "Family: the Aligarh Movement; Sir Syed's paper, the Tahzib-ul-Akhlaq.")

add(H, "The Theosophical Society of India has its headquarters at:",
    ["Adyar, Madras", "Pondicherry", "Belur", "Pune"],
    "Why: Madame Blavatsky and Colonel Olcott started the Society at New York in 1875 and moved to Adyar in 1882. Annie Besant became its president in 1907. "
    "Sibling of: Annie Besant's Home Rule League at Adyar. "
    "Family: Central Hindu College at Banaras (Besant).")

add(H, "'Gulamgiri' (1873), which attacked caste, was written by:",
    ["Jyotirao Phule", "B. R. Ambedkar", "Dayananda Saraswati", "M. G. Ranade"],
    "Why: Phule wrote it in Marathi, and he founded the Satyashodhak Samaj in 1873. He started a girls' school in Pune in 1848 with his wife, Savitribai. "
    "Sibling of: Satyashodhak Samaj – Phule. "
    "Family: Ambedkar's Mooknayak (1920).")

add(H, "The Sarda Act of 1929 was passed to stop:",
    ["Child marriage", "Sati", "Female infanticide", "Polygamy among Muslims"],
    "Why: the Child Marriage Restraint Act (1929) set the minimum age at 14 for girls and 18 for boys. Harbilas Sarda moved it. "
    "Sibling of: the Widow Remarriage Act 1856 and the 1829 sati ban. "
    "Family: Age of Consent Act 1891; Special Marriage Act 1872.")

add(H, "Ambedkar's Mahad Satyagraha (1927) was for the right of the depressed classes to:",
    ["Use the water of the Chavdar Tank", "Enter the Jagannath temple", "Vote in elections", "Carry arms"],
    "Why: it asserted the right to draw water from a public tank at Mahad (Maharashtra). Later he led the Kalaram Temple entry movement at Nashik (1930). "
    "Sibling of: the Poona Pact. "
    "Family: Ambedkar's Bahishkrit Hitakarini Sabha (1924).")

# ================================================================ H. Education, land revenue, economy
# (neighbours of: Wood's Despatch, Sadler, Ryotwari, Permanent Settlement)

add(H, "Macaulay's Minute of 1835 supported the use of which language in higher education?",
    ["English", "Sanskrit", "Persian", "Arabic"],
    "Why: it settled the debate between the Orientalists and Anglicists in favour of English, and Bentinck agreed. Macaulay wanted a class 'Indian in blood but English in taste'. "
    "Sibling of: Wood's Despatch, 1854, and the Charter Act of 1813 (2021 Q23). "
    "Family: the 1813 Act gave one lakh rupees a year for education.")

add(H, "The Hunter Commission of 1882 stressed:",
    ["Primary education and private effort", "Technical education", "University reform", "Women's education only"],
    "Why: W. W. Hunter's Commission said primary and secondary schools should be handled by local bodies and private people. The 1919 'Hunter Committee' on Jallianwala Bagh is a different body. "
    "Sibling of: the Sadler Commission (1917) and Hartog Committee (1929) in 2025 Q81. "
    "Family: Raleigh Commission 1902; Sargent Plan 1944.")

add(H, "The Indian Universities Act of 1904 was passed under Viceroy:",
    ["Lord Curzon", "Lord Minto", "Lord Lytton", "Lord Hardinge"],
    "Why: after the Raleigh Commission of 1902, Curzon gave the Government more control over universities. Indians said it cut their freedom. "
    "Sibling of: the Partition of Bengal, another Curzon act of the same period. "
    "Family: Curzon's Archaeological Survey and the Police Commission.")

add(H, "In the Mahalwari system, revenue was settled with:",
    ["The village community through its headmen", "The zamindar of a district", "Each peasant individually", "The Company's agent"],
    "Why: the Mahalwari system (Holt Mackenzie, 1822) took the village or 'mahal' as the unit for the North-West Provinces. Zamindars were the Permanent Settlement's unit and individual farmers were the Ryotwari unit. "
    "Sibling of: the Ryotwari question (2025 Q88) and Permanent Settlement. "
    "Family: three land systems: Zamindari, Ryotwari, Mahalwari.")

add(H, "Consider the following statements about the Swadeshi Movement:\n1. It began with the Rowlatt Satyagraha.\n2. It included a boycott of British goods.\n3. Rabindranath Tagore promoted 'Rakhi Bandhan' during it.\nWhich of the statements given above is/are correct?",
    S3,
    "Why: the Swadeshi and boycott movement began after the Partition of Bengal (October 1905), not after the Rowlatt Act (1919), so statement 1 is false. Statements 2 and 3 are true. "
    "Sibling of: the Partition of Bengal (Curzon) and Lal–Bal–Pal. "
    "Family: the boycott resolution in Calcutta Town Hall (7 August 1905); National Council of Education.",
    k="stmt", a=1)

add(H, "The Partition of Bengal was annulled in:",
    ["1911", "1905", "1909", "1919"],
    "Why: George V announced at the Delhi Durbar that the partition was cancelled, and the capital moved to Delhi. Bihar and Orissa were separated from Bengal in 1912. "
    "Sibling of: the Curzon–partition question. "
    "Family: 1912 gave Bihar and Orissa a separate province, a step toward Odisha's own province in 1936.")

add(H, "Who was the first Indian to be elected to the British House of Commons (1892)?",
    ["Dadabhai Naoroji", "W. C. Bonnerjee", "Surendranath Banerjee", "Pherozeshah Mehta"],
    "Why: Naoroji won the Finsbury Central seat as a Liberal. Lal Mohan Ghosh had been defeated in 1885. "
    "Sibling of: 'Poverty and Un-British Rule in India' (his book). "
    "Family: Naoroji presided over the Congress in 1886, 1893 and 1906.")

# ================================================================ I. Odisha
# (neighbours of: Surendra Sai, Utkal Sammilani, Orissa province 1936)

add(H, "The Paika Rebellion of 1817 in Odisha was led by:",
    ["Bakshi Jagabandhu Bidyadhar", "Surendra Sai", "Madhusudan Das", "Chakra Bisoyi"],
    "Why: Bakshi Jagabandhu, the commander of the Gajapati King's army (the Paikas), led the rising in Khurda against the British land policy. Surendra Sai fought in Sambalpur in 1857, and Chakra Bisoyi in Ghumsur. "
    "Sibling of: Surendra Sai and Sambalpur (1857). "
    "Family: the Odisha Government now calls the 1817 rising the 'first war of independence'.")

add(H, "By the Treaty of Deogaon (1803), the British took Cuttack from:",
    ["Raghuji Bhonsle II", "Baji Rao II", "Daulat Rao Sindhia", "Tipu Sultan"],
    "Why: the Bhonsle ruler of Nagpur gave up Cuttack and Balasore after the Second Anglo-Maratha War. This was the start of British rule in Odisha. "
    "Sibling of: the Treaty of Bassein (2018 Q71) and the other treaties of 1802–03. "
    "Family: Orissa province 1936; Utkal Divas on 1 April.")

add(H, "The great Odisha famine of 1866 is called:",
    ["Na'anka Durbhiksha", "The Chalisa famine", "Bengal famine", "Doji Bara"],
    "Why: it began in 1865 and was worst in 1866, the 'Na'anka' (the year 9 in the Odia calendar). Nearly a third of the people of Odisha died. It led to the first Famine Commission thinking. "
    "Sibling of: the Famine Commission of 1880 (Strachey). "
    "Family: Utkal Dipika wrote about it.")

add(H, "Gopabandhu Das started which Odia newspaper in 1919?",
    ["The Samaja", "Utkal Dipika", "Bodhadayini", "Asha"],
    "Why: The Samaja began at Satyabadi and later moved to Cuttack. Gopabandhu ('Utkalmani') also ran the Satyabadi school at Sakhigopal. "
    "Sibling of: Utkal Dipika. "
    "Family: Gopabandhu Das was elected to the Bihar and Orissa Council in 1917.")

add(H, "In Odisha, the Salt Satyagraha of 1930 was held at:",
    ["Inchudi, Balasore", "Puri", "Cuttack", "Sambalpur"],
    "Why: volunteers led by Gopabandhu Choudhury and Acharya Harihar Das made salt at Inchudi on the coast. The movement spread to Kujang and Chandbali. "
    "Sibling of: Dandi (2018 Q32). "
    "Family: Gandhi first visited Odisha in 1921, at Cuttack.")

add(H, "The Eram firing of 1942, in which freedom fighters were killed, took place in which district of Odisha?",
    ["Jagatsinghpur", "Cuttack", "Puri", "Balasore"],
    "Why: the police fired on a peaceful procession at Eram on 28 September 1942, during Quit India. About twenty-nine people died. "
    "Sibling of: the Quit India resolution. "
    "Family: Bhubaneswar's Ekamra; the Mahatab group's role in Quit India.")

add(H, "Who became the first Congress Premier of Odisha in 1937?",
    ["Biswanath Das", "Krushna Chandra Gajapati", "Harekrushna Mahatab", "Nabakrushna Choudhury"],
    "Why: after the 1937 elections the Congress took office in Odisha and Biswanath Das was Premier. Gajapati was the first Premier of the new province in 1936 (before the elections). Mahatab was Premier in 1946. "
    "Sibling of: the creation of the province of Orissa in 1936. "
    "Family: Sir John Hubback was the first Governor.")

add(H, "The Ghumsur rising of 1835–36 in Odisha was led by:",
    ["Chakra Bisoyi", "Dora Bisoyi", "Surendra Sai", "Bakshi Jagabandhu"],
    "Why: the Kandhas of Ghumsur resisted British rule, and Chakra Bisoyi became a symbol of tribal resistance. "
    "Sibling of: the Paika Rebellion and the Sambalpur rising. "
    "Family: the Kandha revolts against the Meriah (human sacrifice) rules.",
    c=True)

# ================================================================ J. Organisations and the Muslim League
# (neighbours of: Central National Mohammedan Association, Indian Association, Servants of India Society)

add(H, "Which of the following was NOT a Moderate leader of the early Congress?",
    ["Bal Gangadhar Tilak", "Dadabhai Naoroji", "G. K. Gokhale", "Pherozeshah Mehta"],
    "Why: Tilak was an Extremist, who wanted more than petitions. The Moderates believed in constitutional methods and prayers to the British Government. "
    "Sibling of: the Servants of India Society (Gokhale) and the Indian Association (Surendranath Banerjee). "
    "Family: Moderates: Naoroji, Gokhale, Mehta, Banerjee, Bonnerjee. Extremists: Lal, Bal, Pal.",
    k="not")

add(H, "The British Indian Association (1851), an early political body, was formed at:",
    ["Calcutta", "Bombay", "Madras", "Poona"],
    "Why: it was the first political body of its kind and had zamindars as members. Debendranath Tagore was its first secretary. "
    "Sibling of: the Indian Association (1876, Calcutta) and the Madras Mahajana Sabha (1884). "
    "Family: the Bombay Association (1852); the Poona Sarvajanik Sabha (1870).")

add(H, "The All India Muslim League was formed at Dhaka in 1906. Which man hosted the meeting?",
    ["Nawab Salimullah", "Sir Syed Ahmad Khan", "Aga Khan", "Muhammad Ali Jinnah"],
    "Why: the Nawab of Dhaka, Khwaja Salimullah, hosted it and was a founder. The Aga Khan was its first president. Jinnah joined in 1913. "
    "Sibling of: the Central National Mohammedan Association (2025 Q57). "
    "Family: the 1909 Act gave Muslims separate electorates.")

add(H, "The Khilafat Movement (1919–24) in India was led by:",
    ["Muhammad Ali and Shaukat Ali", "Muhammad Iqbal and Jinnah", "Maulana Azad and Hakim Ajmal Khan", "Sir Syed and Aga Khan"],
    "Why: the Ali brothers led it to back the Caliph of Turkey, and Gandhi joined it to unite Hindus and Muslims. It faded after Turkey ended the Caliphate in 1924. "
    "Sibling of: the Non-Cooperation Movement, which it joined. "
    "Family: Muhammad Ali also published the Comrade.")

add(H, "The Lahore Resolution (Pakistan Resolution) of March 1940 was moved by:",
    ["A. K. Fazlul Huq", "Muhammad Ali Jinnah", "Liaquat Ali Khan", "Chaudhry Rahmat Ali"],
    "Why: the Bengal Premier A. K. Fazlul Huq moved it at the Muslim League session, which Jinnah presided over. The Congress called it a call to break up the country. "
    "Sibling of: the Lahore Congress (1929). "
    "Family: Rahmat Ali coined the name 'Pakistan' in 1933.")

add(H, "The idea of a separate Muslim State in north-west India was put forward by Muhammad Iqbal in his presidential address to the Muslim League at Allahabad in:",
    ["1930", "1906", "1940", "1947"],
    "Why: Iqbal spoke of such a State in December 1930. Jinnah's Lahore Resolution came ten years later. "
    "Sibling of: the Lahore Resolution (1940). "
    "Family: Iqbal wrote 'Sare Jahan Se Accha'.")

add(H, "Arrange these events in order of time:\n(i) The Poona Pact\n(ii) The Jallianwala Bagh massacre\n(iii) The Nehru Report\n(iv) The Chauri Chaura incident",
    ["ii, iv, iii, i", "iv, ii, iii, i", "ii, iii, iv, i", "ii, iv, i, iii"],
    "Why: Jallianwala Bagh 1919, Chauri Chaura 1922, Nehru Report 1928, Poona Pact 1932. "
    "Sibling of: the order of four movements (2018 Q87). "
    "Family: Rowlatt 1919, Swaraj Party 1923, Simon Commission 1927, Dandi 1930.",
    k="order")
