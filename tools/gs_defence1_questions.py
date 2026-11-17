# Questions for the GS Defence Mock 01 (50 questions, topic (h) Defence & Indian Armed Forces).
# In every item the FIRST option is the right one, unless "a" is given (then the options stay in the written order).
# k: one | stmt | match | not | order.  n: needs 2025-26 news.  c: Check tag.
# Every question is a next angle of a Defence family from the 2018, 2021 and 2025 papers.
# None repeats a Defence question of GS Mock 01, 02, 03, GA Mock 1 or the GA Full Test.

S12 = ["Only 1", "Only 2", "Both 1 and 2", "Neither 1 nor 2"]
S3 = ["Only 1 and 2", "Only 2 and 3", "Only 1 and 3", "1, 2 and 3"]
def M(a, b, c, d):
    return "a-%d, b-%d, c-%d, d-%d" % (a, b, c, d)

Q = []
D = "Defence"
def add(q, o, e, k="one", n=False, c=False, a=None):
    Q.append(dict(s=D, q=q, o=o, e=e, k=k, n=n, c=c, a=a))

# ================================================================ LEADERS AND ORGANISATION
add("Match List I (Post) with List II (Officer who took over in 2026):\nList I: a. Chief of Defence Staff  b. Chief of the Army Staff  c. Chief of the Naval Staff  d. Chief of the Air Staff\nList II: 1. Admiral Krishna Swaminathan  2. General N. S. Raja Subramani  3. Air Chief Marshal Ashutosh Dixit  4. General Dhiraj Seth",
    [M(2, 4, 1, 3), M(4, 2, 1, 3), M(2, 4, 3, 1), M(1, 4, 2, 3)],
    "Four chairs changed in five months. On 31 May 2026 General N. S. Raja Subramani became the third CDS and Admiral Krishna Swaminathan became Navy chief. General Dhiraj Seth took the Army on 30 June, and Air Chief Marshal Ashutosh Dixit took the Air Force on 31 October. The 2021 paper asked 'the present Chief of Air Staff', so 'who holds which post' is a live family. Order to remember: May (two), June (Army), October (Air Force).",
    k="match", n=True)
add("Consider the following statements about the changes of service chiefs in 2026:\n1. Admiral Krishna Swaminathan succeeded Admiral Dinesh K. Tripathi.\n2. General Dhiraj Seth succeeded General Anil Chauhan.\n3. Air Chief Marshal Ashutosh Dixit succeeded Air Chief Marshal A. P. Singh.\nWhich of the statements given above are correct?",
    S3,
    "Statement 2 is the trap. General Anil Chauhan was the second CDS, not an Army chief. He gave way to General Raja Subramani as CDS. General Dhiraj Seth took over the Army from General Upendra Dwivedi. The examiner likes to swap two names that belong to the same story, so learn each 'took over from' pair. Bipin Rawat was the first CDS (2019).",
    k="stmt", n=True, a=2)
add("Consider the following statements about the Chief of Defence Staff (CDS):\n1. The CDS is the Principal Military Adviser to the Defence Minister on tri-service matters.\n2. The CDS heads the Department of Military Affairs and is its Secretary.\n3. The CDS has operational command over the Army, Navy and Air Force.\nWhich of the statements given above are correct?",
    S3,
    "Statement 3 is wrong. The CDS does not command troops. The three chiefs keep command of their own forces. The CDS plans, joins the forces together and pushes reform such as theatre commands. The post was created in 2019, together with the Department of Military Affairs (DMA) inside the Ministry of Defence. The CDS is also the Permanent Chairman of the Chiefs of Staff Committee.",
    k="stmt", a=0)
add("Which command, set up in 2003 and headed by a Commander-in-Chief, looks after India's nuclear weapons?",
    ["Strategic Forces Command", "Andaman and Nicobar Command", "Integrated Defence Staff", "Defence Space Agency"],
    "The Strategic Forces Command (SFC) was set up in 2003 to manage the nuclear arsenal, and it takes orders from the Nuclear Command Authority. The Andaman and Nicobar Command (2001, Port Blair) was India's first tri-service command. The 2018 and 2021 papers asked about defence bodies and where they sit. Remember also the Defence Space Agency and the Defence Cyber Agency, both set up in 2019.")
add("In October 2021 the 41 factories of the Ordnance Factory Board were turned into how many government-owned companies?",
    ["7", "5", "12", "3"],
    "The Government closed the Ordnance Factory Board and put its 41 factories into seven Defence Public Sector Undertakings, such as Munitions India Limited, Armoured Vehicles Nigam Limited and Advanced Weapons and Equipment India Limited. The aim was better work and more exports. This sits with the 'Make in India in defence' family. Other public companies to remember are HAL (Bengaluru), BEL (Bengaluru), BDL (Hyderabad), Mazagon Dock (Mumbai) and GRSE (Kolkata).")
add("Consider the following statements:\n1. The Innovations for Defence Excellence (iDEX) scheme was launched in 2018 to help start-ups and small firms make defence products.\n2. Defence Industrial Corridors are being set up in Uttar Pradesh and Tamil Nadu.\n3. The Defence Acquisition Council is headed by the Chief of Defence Staff.\nWhich of the statements given above are correct?",
    S3,
    "The Defence Acquisition Council (DAC) is chaired by the Defence Minister, not the CDS. It gives the first approval to big purchases, called 'Acceptance of Necessity'; the 2021 paper asked about an Acceptance of Necessity for an HAL aircraft. iDEX and the two corridors (UP and Tamil Nadu) belong to the same push for self-reliance. In 2020 FDI in defence was raised to 74% through the automatic route.",
    k="stmt", a=0)
add("Under the policy changes of 2020, foreign direct investment in the defence sector is allowed up to ____ through the automatic route.",
    ["74%", "49%", "100%", "26%"],
    "Till 2020 the automatic route allowed 49%, and before 2016 it was only 26%. In 2020 the limit became 74% on the automatic route, and anything above that needs government approval. This is a cross question between the Economy and the Defence parts of the syllabus, and the 2025 paper liked such cross questions. Remember the three numbers in order: 26, 49, 74.")

# ================================================================ FORCES: COMMANDS, SHIPS, AIRCRAFT, WEAPONS
add("Which one of the following Army Commands is NOT correctly matched with its headquarters?",
    ["Eastern Command – Guwahati", "Northern Command – Udhampur", "Southern Command – Pune", "Central Command – Lucknow"],
    "The Eastern Command is at Fort William, Kolkata, not Guwahati. The other pairs are right: Northern (Udhampur), Southern (Pune), Central (Lucknow). Also learn Western (Chandimandir), South Western (Jaipur) and ARTRAC, the training command (Shimla). The 2025 paper asked where the National Police Academy and other bodies sit; 'body and place' pairs are a favourite.",
    k="not")
add("Match List I (Naval Command) with List II (Headquarters):\nList I: a. Western Naval Command  b. Eastern Naval Command  c. Southern Naval Command  d. Andaman and Nicobar Command\nList II: 1. Kochi  2. Mumbai  3. Visakhapatnam  4. Port Blair",
    [M(2, 3, 1, 4), M(3, 2, 1, 4), M(2, 3, 4, 1), M(1, 3, 2, 4)],
    "The Western Command (Mumbai) and the Eastern Command (Visakhapatnam) are the two operational commands. The Southern Command at Kochi is the training command. The Andaman and Nicobar Command at Port Blair, set up in 2001, was India's first tri-service command. Admiral Swaminathan headed the Western Naval Command before he became Navy chief. MILAN 2026 was held at Visakhapatnam, home of the Eastern Command.",
    k="match")
add("INS Chilka, a large training base of the Indian Navy for new sailors, is located in:",
    ["Odisha", "Andhra Pradesh", "Kerala", "Goa"],
    "INS Chilka stands on the shore of Chilika Lake in Odisha. It trains the recruits of the Navy. The same State has the Integrated Test Range at Chandipur and Dr A. P. J. Abdul Kalam Island, where missiles are tested. OPSC likes defence facts that touch Odisha. The Naval Academy is at Ezhimala in Kerala, and the National Defence Academy is at Khadakwasla, Pune.")
add("INS Mahendragiri, a Nilgiri-class stealth frigate commissioned in 2026, is named after a mountain range in which State?",
    ["Odisha", "Tamil Nadu", "Karnataka", "Andhra Pradesh"],
    "Mahendragiri is a hill range of the Eastern Ghats in Gajapati district of Odisha. The seven Project 17A frigates are all named after hills: Nilgiri, Himgiri, Udaygiri, Dunagiri, Taragiri, Vindhyagiri and Mahendragiri. In the Odisha paper the 2025 exam asked about hills from north to south, so the name is useful twice. The Nilgiri class is built in India at Mazagon Dock and GRSE.",
    n=True)
add("Which of India's aircraft carriers was built at Cochin Shipyard and commissioned in September 2022?",
    ["INS Vikrant", "INS Vikramaditya", "INS Viraat", "INS Vishal"],
    "INS Vikrant is India's first aircraft carrier designed and built in India, at Cochin Shipyard Limited. INS Vikramaditya was bought from Russia (it was the Admiral Gorshkov). INS Viraat, the old carrier, was the former British HMS Hermes and left service in 2017. INS Vishal is only the planned name of the next carrier. The first INS Vikrant, a British-built carrier, played a part in the 1971 war.")
add("Consider the following statements about the Indian Navy's aircraft carriers:\n1. INS Vikramaditya was bought from Russia.\n2. INS Vikrant, commissioned in 2022, was built at Cochin Shipyard.\n3. INS Viraat was bought from France.\nWhich of the statements given above are correct?",
    S3,
    "INS Viraat was bought from Britain (the former HMS Hermes), not France. So statement 3 is false. Statements 1 and 2 are right. In 2025 the paper asked three-statement questions on one force or one ship. The trap is always one wrong country or place in an otherwise true set.",
    k="stmt", a=0)
add("The Scorpene-class submarines, such as INS Kalvari, are built at Mazagon Dock in Mumbai with the technology of which country?",
    ["France", "Russia", "Germany", "Sweden"],
    "Project 75 gave India six Scorpene submarines, built at Mazagon Dock Shipbuilders with the French company Naval Group. INS Kalvari was the first, in 2017. Do not mix them with the nuclear submarines of the Arihant class, which are built at Visakhapatnam. Russia is the source of the older Kilo-class boats and the Vikramaditya.")
add("'Surya', launched on 6 October 2026, is India's first home-built:",
    ["Fleet Support Ship", "Aircraft carrier", "Nuclear submarine", "Missile destroyer"],
    "A fleet support ship carries fuel, water, food and spares so that warships can stay at sea for weeks. Surya is the first such ship built fully in India. The Navy also placed orders in November 2026 for eight Next Generation Corvettes, which went to GRSE and Goa Shipyard. The 2025 paper asked news of ships and exercises, so 'which ship, what type' is a good question to expect.",
    n=True)
add("The contracts signed in November 2026 for eight Next Generation Corvettes of the Indian Navy went to:",
    ["Garden Reach Shipbuilders and Goa Shipyard", "Mazagon Dock and Cochin Shipyard", "Hindustan Shipyard and L&T", "Bharat Dynamics and HAL"],
    "Both are public sector shipyards, one in Kolkata and one in Goa. Next Generation Corvettes are small warships for coastal waters and anti-submarine work. Bharat Dynamics (Hyderabad) makes missiles and HAL (Bengaluru) makes aircraft, so they are the wrong sort of company. Learn which yard builds which ship: Mazagon Dock builds destroyers and Scorpene submarines.",
    n=True)
add("The first squadron of the Rafale fighter jets of the Indian Air Force is based at:",
    ["Ambala", "Hasimara", "Jodhpur", "Bhuj"],
    "No. 17 Squadron, the 'Golden Arrows', was formed with Rafale jets at Ambala in Haryana in September 2020. The second squadron is at Hasimara in West Bengal. The Rafale is made by Dassault of France. The 2021 paper asked about an aircraft cleared for HAL, and the S-400 from Russia, so 'which jet, which maker, which country' is a standing family.")
add("In September 2025 the Indian Air Force retired its last squadron of which fighter jet after more than sixty years of service?",
    ["MiG-21", "Jaguar", "Mirage 2000", "MiG-29"],
    "The MiG-21 first joined the Air Force in 1963 and fought in the wars of 1965 and 1971. The farewell was held at Chandigarh in September 2025. The Su-30MKI, built under licence by HAL, is now the main fighter, and the Tejas Mk1A is the new home-built one. A farewell or a first induction is a typical 'news of the year' question.",
    n=True)
add("The Advanced Medium Combat Aircraft (AMCA), India's planned fifth-generation fighter, is being developed by:",
    ["Aeronautical Development Agency", "Hindustan Aeronautics Limited alone", "Bharat Electronics Limited", "Defence Institute of Advanced Technology"],
    "The Aeronautical Development Agency (ADA), Bengaluru, designs it, under DRDO. HAL built the Tejas that ADA designed. Fifth-generation means stealth shape, advanced sensors and the ability to share data. The Tejas Light Combat Aircraft first flew in 2001. Fighter jets, makers and designers are a repeated pairing in the Defence part.")
add("Match List I (Gun) with List II (Country of origin or design):\nList I: a. Bofors  b. M777 ultra-light howitzer  c. K9 Vajra  d. Dhanush\nList II: 1. USA  2. India  3. Sweden  4. South Korea",
    [M(3, 1, 4, 2), M(1, 3, 4, 2), M(3, 1, 2, 4), M(2, 1, 4, 3)],
    "The Bofors gun came from Sweden in the 1980s and was famous for the Kargil war and for the scandal. The M777 is from the USA and fits mountains because it is light. K9 Vajra is a South Korean tracked gun built in India by L&T. Dhanush is the Indian 'desi Bofors', made by an Ordnance Factory. The Pinaka, also a DRDO product, is a rocket launcher, not a gun.",
    k="match")
add("Pinaka, developed by DRDO and named after the bow of Lord Shiva, is a:",
    ["Multi-barrel rocket launcher", "Anti-tank guided missile", "Main battle tank", "Light combat helicopter"],
    "Pinaka fires a salvo of rockets from a truck and has been improved with longer range and guided versions. The Arjun is the Army's main battle tank (made by DRDO's CVRDE at Avadi, a 2018 question), Nag is the anti-tank missile, and Prachand is the HAL light combat helicopter. Learn each weapon with its job: gun, rocket, tank, missile, helicopter.")
add("Agni-4 and the long-range Pinaka rocket, tested in 2026, were fired from which test range?",
    ["Chandipur, Odisha", "Pokhran, Rajasthan", "Sriharikota, Andhra Pradesh", "Kolar, Karnataka"],
    "The Integrated Test Range at Chandipur in Balasore district is DRDO's main missile test site, along with Dr A. P. J. Abdul Kalam Island in Bhadrak district. Pokhran is a nuclear and artillery range, and Sriharikota is for space launches by ISRO. This detail rests on one news report, so treat it with care.",
    n=True, c=True)
add("MIRV technology, shown in the Agni-5 test of March 2024 called 'Mission Divyastra', allows a missile to:",
    ["Carry several warheads that hit different targets", "Fly below radar at a low height", "Change course using a satellite", "Launch from a submarine"],
    "MIRV means Multiple Independently targetable Re-entry Vehicle. One Agni-5 can drop several warheads that fall on different places. Agni-5 has a range of more than 5,000 km. Submarine launch belongs to the K-series, such as K-15 Sagarika. A missile that flies low and level is a cruise missile, such as BrahMos or Nirbhay.")
add("The K-15 'Sagarika' is a:",
    ["Submarine-launched ballistic missile", "Surface-to-air missile", "Air-to-air missile", "Anti-ship cruise missile"],
    "K-15 Sagarika is a short-range missile fired from a submerged submarine. It is made by DRDO, and the longer K-4 is the next of the series. These missiles give the nuclear submarines of the Arihant class their real power. The rule from the earlier papers still holds: name the missile by where it starts and what it hits.")
add("Which one of the following is NOT an Israeli air defence system?",
    ["THAAD", "Iron Dome", "David's Sling", "Arrow"],
    "THAAD is made in the USA by Lockheed Martin. Iron Dome (asked in 2025), David's Sling and Arrow are the three layers of Israel's air defence: short, medium and long range. India's own plan is the 'Sudarshan Chakra' mission, and the S-400, bought from Russia, was asked in 2021.")
add("Which mission, announced by the Prime Minister on 15 August 2025, aims to build a national shield against air attacks?",
    ["Mission Sudarshan Chakra", "Mission Divyastra", "Mission Shakti", "Mission Gaganyaan"],
    "The Prime Minister announced Mission Sudarshan Chakra from the Red Fort. The 2025 paper asked about Iron Dome, so India's own shield is the next angle. Do not confuse it with Mission Shakti (anti-satellite test of 2019), Divyastra (Agni-5 MIRV test of 2024) or Gaganyaan (the human spaceflight mission of ISRO).",
    n=True)
add("In March 2019, India became the fourth country to destroy a satellite in orbit with a missile. The test was called:",
    ["Mission Shakti", "Operation Shakti", "Mission Sudarshan", "Operation Vijay"],
    "Mission Shakti (27 March 2019) was an anti-satellite (ASAT) test by DRDO. The first three were the USA, Russia and China. 'Operation Shakti' is the other test: the Pokhran-II nuclear tests of May 1998. The first test of 1974 was called 'Smiling Buddha'. The examiner may put the two Shaktis side by side.")
add("Consider the following statements about India's nuclear policy:\n1. India follows a 'No First Use' policy.\n2. The Nuclear Command Authority has a Political Council headed by the Prime Minister.\n3. India's nuclear doctrine allows the first use of nuclear weapons against a conventional attack.\nWhich of the statements given above is/are correct?",
    ["Only 1 and 2", "Only 2 and 3", "Only 1 and 3", "1, 2 and 3"],
    "No First Use (NFU) means India will not be the first to use a nuclear weapon, but will hit back hard if attacked. Statement 3 says the opposite. The doctrine speaks of 'credible minimum deterrence'. The Political Council gives the order, and the Executive Council, headed by the National Security Adviser, advises it. The Pokhran tests were in 1974 and in May 1998.",
    k="stmt", a=0)
add("The Pokhran-II nuclear tests of May 1998 were carried out under the code name:",
    ["Operation Shakti", "Smiling Buddha", "Operation Vijay", "Operation Meghdoot"],
    "Pokhran-II (11 and 13 May 1998) was Operation Shakti, in the time of Prime Minister Atal Bihari Vajpayee. National Technology Day is on 11 May for this reason. Pokhran-I (18 May 1974) was called 'Smiling Buddha'. Operation Vijay was the Kargil war of 1999 and Operation Meghdoot took Siachen in 1984.")

# ================================================================ BORDER FORCES, SERVICES, AWARDS, DAYS
add("Match List I (Force) with List II (Motto):\nList I: a. Border Security Force  b. Indo-Tibetan Border Police  c. Central Reserve Police Force  d. Assam Rifles\nList II: 1. Valour, Determination, Devotion to Duty  2. Service and Loyalty  3. Duty unto Death  4. Friends of the Hill People",
    [M(3, 1, 2, 4), M(1, 3, 2, 4), M(3, 2, 1, 4), M(3, 1, 4, 2)],
    "The BSF's motto is 'Jeevan Paryant Kartavya', Duty unto Death. The ITBP's is Shaurya, Dridhta, Karma Nishtha. The CRPF is 'Service and Loyalty' and the Assam Rifles are the 'Friends of the Hill People'. All of them work under the Ministry of Home Affairs, except the Coast Guard, which is under the Ministry of Defence. The 2025 paper had three statements on the ITBP.",
    k="match")
add("Arrange the following forces in the order in which they were raised (earliest first):\nA. Assam Rifles  B. Border Security Force  C. Indo-Tibetan Border Police  D. Central Reserve Police Force",
    ["A, D, C, B", "A, C, D, B", "D, A, C, B", "A, D, B, C"],
    "Assam Rifles began in 1835. The CRPF began in 1939. The ITBP was raised in 1962 after the war with China, and the BSF in 1965 after the war with Pakistan. Then came the SSB (1963 in its first form), the CISF (1969) and the NSG (1984). Learn the ladder 1835, 1939, 1962, 1965, 1969, 1984.",
    k="order")
add("Consider the following statements about the National Security Guard (NSG):\n1. It was set up in 1984.\n2. It works under the Ministry of Defence.\n3. Its commandos are known as the 'Black Cats'.\nWhich of the statements given above are correct?",
    S3,
    "The NSG works under the Ministry of Home Affairs, so statement 2 is wrong. It was raised in 1984 for counter-terror and hijack work, and its men are called Black Cats because of their black dress. The false statement 'a force of Home Affairs works under Defence' has been the examiner's favourite trap, and the only border-type force under Defence is the Coast Guard (set up in 1978).",
    k="stmt", a=2)
add("The Territorial Army, a force of part-time volunteer citizen soldiers, was inaugurated in 1949 by:",
    ["C. Rajagopalachari", "Jawaharlal Nehru", "Sardar Vallabhbhai Patel", "K. M. Cariappa"],
    "C. Rajagopalachari, then Governor-General, inaugurated the Territorial Army on 9 October 1949. Its members hold a regular job and train in their spare time, and they can be called to serve in an emergency. The first Indian Commander-in-Chief, K. M. Cariappa (1949), later became a Field Marshal in 1986. Territorial Army Day is celebrated on 9 October.")
add("The motto of the National Cadet Corps (NCC) is:",
    ["Unity and Discipline", "Service before Self", "Be Prepared", "Duty, Honour, Country"],
    "The NCC was formed under the National Cadet Corps Act of 1948, and it works under the Ministry of Defence. It has an Army, a Navy and an Air Wing. NCC Day falls on the fourth Sunday of November. 'Be Prepared' is the Scouts' motto, a trap for the careless.")
add("Which one of the following is NOT correctly matched?",
    ["Vir Chakra – gallantry award for peacetime", "Param Vir Chakra – highest gallantry award in war", "Maha Vir Chakra – second highest gallantry award in war", "Kirti Chakra – second highest gallantry award in peacetime"],
    "The Vir Chakra is the third gallantry award for war, not for peacetime. The war ladder: Param Vir Chakra, Maha Vir Chakra, Vir Chakra. The peacetime ladder: Ashoka Chakra, Kirti Chakra, Shaurya Chakra. The 2021 paper asked who got the Param Vir Chakra from the Air Force; the Mock 02 key asked the top peacetime award. The medal of the Param Vir Chakra was designed by Savitri Khanolkar.",
    k="not")
add("Match List I (Param Vir Chakra winner) with List II (War or operation):\nList I: a. Major Somnath Sharma  b. Abdul Hamid  c. Flying Officer Nirmal Jit Singh Sekhon  d. Captain Vikram Batra\nList II: 1. Kargil, 1999  2. War of 1971  3. War of 1965  4. Kashmir, 1947",
    [M(4, 3, 2, 1), M(3, 4, 2, 1), M(4, 3, 1, 2), M(4, 2, 3, 1)],
    "Somnath Sharma, the first winner, fell at Badgam in Kashmir in 1947. Abdul Hamid destroyed tanks at Asal Uttar in 1965. Sekhon, the only Air Force winner (asked in 2021), defended Srinagar airfield in 1971. Vikram Batra fought at Point 4875 in Kargil in 1999 ('Yeh Dil Maange More'). The same four wars are a standard 'arrange' and 'match' family.",
    k="match")
add("Who became the first Indian officer to be made a Field Marshal, in January 1973?",
    ["Sam Manekshaw", "K. M. Cariappa", "Arjan Singh", "K. S. Thimayya"],
    "Sam Manekshaw led the Army in the 1971 war that ended with the birth of Bangladesh. K. M. Cariappa was made Field Marshal later, in 1986. Arjan Singh of the Air Force was made Marshal of the Air Force in 2002, and he is the only one. The 2021 paper asked for 'the only Air Force officer' with the Param Vir Chakra, a similar 'only one' question.")
add("Match List I (Day) with List II (Date):\nList I: a. Indian Army Day  b. Indian Air Force Day  c. Indian Navy Day  d. Armed Forces Flag Day\nList II: 1. 8 October  2. 15 January  3. 4 December  4. 7 December",
    [M(2, 1, 3, 4), M(2, 1, 4, 3), M(1, 2, 3, 4), M(2, 3, 1, 4)],
    "Army Day (15 January) marks the day in 1949 when K. M. Cariappa became the first Indian chief. Air Force Day (8 October) marks the founding in 1932. Navy Day (4 December) recalls Operation Trident, the 1971 attack on Karachi harbour. Armed Forces Flag Day (7 December) is for collecting funds for soldiers' families. Remember the trap: 3 and 4 December sit one day apart.",
    k="match")
add("The Atal Tunnel below the Rohtang Pass, built by the Border Roads Organisation and opened in 2020, is in which State?",
    ["Himachal Pradesh", "Jammu and Kashmir", "Arunachal Pradesh", "Uttarakhand"],
    "The Atal Tunnel joins Manali with the Lahaul-Spiti valley and is the world's longest highway tunnel above 10,000 feet. The Border Roads Organisation (BRO) works under the Ministry of Defence. The Sela Tunnel, asked in 2021, is in Arunachal Pradesh and eases the road to Tawang. The Zojila tunnel is for Kashmir and Ladakh.")
add("Match List I (Line) with List II (Meaning):\nList I: a. Radcliffe Line  b. McMahon Line  c. Durand Line  d. Line of Control\nList II: 1. India–China boundary in the east  2. Afghanistan–Pakistan boundary  3. Partition boundary of Punjab and Bengal in 1947  4. Ceasefire line in Jammu and Kashmir",
    [M(3, 1, 2, 4), M(1, 3, 2, 4), M(3, 1, 4, 2), M(3, 2, 1, 4)],
    "Sir Cyril Radcliffe drew the line that split Punjab and Bengal in 1947. The McMahon Line comes from the 1914 Simla Convention and runs along Arunachal Pradesh. The Durand Line (1893) separates Afghanistan and Pakistan. The Line of Control in Jammu and Kashmir was named in the Simla Agreement of 1972 after the 1971 war. The LAC is the border with China in the west and middle sectors.",
    k="match")
add("Match List I (Force or body) with List II (Place):\nList I: a. Naval Academy  b. Air Force Academy  c. Defence Services Staff College  d. College of Defence Management\nList II: 1. Dundigal  2. Wellington  3. Ezhimala  4. Secunderabad",
    [M(3, 1, 2, 4), M(1, 3, 2, 4), M(3, 1, 4, 2), M(3, 2, 1, 4)],
    "The Indian Naval Academy is at Ezhimala, Kerala. The Air Force Academy is at Dundigal near Hyderabad. The Defence Services Staff College is at Wellington in the Nilgiris, and the College of Defence Management at Secunderabad. The Indian National Defence University (asked in 2018 and 2021) is being built at Binola, Haryana. The 2025 paper asked where the Police Academy is: Hyderabad.",
    k="match")

# ================================================================ EXERCISES AND OPERATIONS
add("Match List I (Exercise of 2026) with List II (Place):\nList I: a. Yudh Abhyas  b. Tiger Triumph  c. INDRA  d. KHANJAR\nList II: 1. Vladivostok  2. Misamari, Assam  3. Alaska  4. Visakhapatnam",
    [M(3, 4, 1, 2), M(4, 3, 1, 2), M(3, 4, 2, 1), M(3, 1, 4, 2)],
    "The 22nd edition of Yudh Abhyas, the India–USA army exercise, was held in Alaska. Tiger Triumph, the India–USA tri-service relief exercise, was at Visakhapatnam. INDRA, with Russia, was at Vladivostok (INS Sahyadri took part at sea). KHANJAR, with Kyrgyzstan, was at Misamari in Sonitpur district, Assam. In the 2025 paper the question was always one more step: not only the partner but also the place.",
    k="match", n=True)
add("Tiger Triumph, the exercise of India and the USA, is conducted mainly to practise:",
    ["Humanitarian aid and disaster relief by all three services", "Mountain warfare by the Army", "Anti-submarine warfare by the Navy", "Air combat by the Air Force"],
    "Tiger Triumph is a tri-service exercise, which means the Army, Navy and Air Force of both countries take part, and its theme is relief after a disaster. RAHAT MITRA, the first relief exercise with Myanmar, is of the same kind. The USA is the partner with whom India holds the largest number of exercises.",
    n=True)
add("Match List I (Exercise) with List II (Partner country):\nList I: a. Ekuverin  b. Harimau Shakti  c. Maitree  d. Ajeya Warrior\nList II: 1. Thailand  2. United Kingdom  3. Malaysia  4. Maldives",
    [M(4, 3, 1, 2), M(3, 4, 1, 2), M(4, 3, 2, 1), M(4, 1, 3, 2)],
    "Ekuverin is with the Maldives, Harimau Shakti with Malaysia (the tiger), Maitree with Thailand ('friendship'), and Ajeya Warrior with the United Kingdom. Earlier mocks covered the neighbours Surya Kiran (Nepal), Sampriti (Bangladesh) and Mitra Shakti (Sri Lanka), and the Central Asian three: KHANJAR, DUSTLIK and KAZIND. The 2025 paper asked Nomadic Elephant (Mongolia) and Dharma Guardian (Japan).",
    k="match")
add("Match List I (Air force exercise) with List II (Country linked to it):\nList I: a. Garuda  b. Red Flag  c. Desert Flag  d. Eastern Bridge\nList II: 1. Oman  2. United Arab Emirates  3. France  4. United States",
    [M(3, 4, 2, 1), M(4, 3, 2, 1), M(3, 4, 1, 2), M(3, 2, 4, 1)],
    "Garuda is with France, Red Flag is held in the USA, Desert Flag is held in the UAE (the 2025 paper had a statement question on Desert Flag-10), and Eastern Bridge is with Oman. Pitch Black is held in Australia (Mock 03). Tarang Shakti, held in India in 2024, was the first multinational air exercise India hosted.",
    k="match")
add("Operation Sindoor was launched by India on:",
    ["7 May 2025", "22 April 2025", "26 February 2019", "29 September 2016"],
    "India named the strikes after the Pahalgam terror attack of 22 April 2025. Operation Sindoor began on 7 May 2025. The Balakot air strike was on 26 February 2019 after the Pulwama attack of 14 February, and the 'surgical strikes' across the Line of Control were on 28–29 September 2016 after Uri. The examiner may offer all three dates as options.",
    n=True)
add("Match List I (Evacuation operation) with List II (Country or place):\nList I: a. Operation Ganga  b. Operation Kaveri  c. Operation Devi Shakti  d. Operation Maitri\nList II: 1. Afghanistan  2. Ukraine  3. Nepal earthquake  4. Sudan",
    [M(2, 4, 1, 3), M(4, 2, 1, 3), M(2, 4, 3, 1), M(2, 1, 4, 3)],
    "Operation Ganga (2022) brought Indians back from Ukraine. Kaveri (2023) was from Sudan. Devi Shakti (2021) was from Afghanistan. Maitri (2015) was the relief mission after the Nepal earthquake. The 2025 paper asked Operation Jindagi, Keller, Olivia and Zero Line, and Mock 02 had Brahma, Sindhu and Sagar Bandhu. Learn the purpose of each operation name, not just the name.",
    k="match")
add("Arrange the following in the order of their dates (earliest first):\nA. Operation Pawan in Sri Lanka  B. Operation Polo in Hyderabad  C. The surrender of the Pakistani army at Dhaka  D. The liberation of Goa",
    ["B, D, C, A", "B, C, D, A", "D, B, C, A", "B, D, A, C"],
    "Operation Polo, the police action on Hyderabad, took place in September 1948. Goa was freed in December 1961 by Operation Vijay. The Pakistani army surrendered at Dhaka on 16 December 1971. Operation Pawan, the Indian Peace Keeping Force action in Sri Lanka, began in October 1987. Dates with 'the order of' are easy to guess once the four decades are fixed.",
    k="order")
add("Which one of the following pairs (Operation – Purpose) is NOT correctly matched?",
    ["Operation Blue Star – Capture of the Siachen glacier", "Operation Safed Sagar – Air Force action in Kargil", "Operation Trident – Navy attack on Karachi in 1971", "Operation Pawan – Indian Peace Keeping Force in Sri Lanka"],
    "Operation Blue Star (1984) was the action at the Golden Temple in Amritsar. The capture of Siachen was Operation Meghdoot, in the same year. Safed Sagar was the Air Force's role in the Kargil war; the Navy's was Operation Talwar. Trident is the reason for Navy Day on 4 December. Mock 03 asked Meghdoot, Polo, Cactus and Vijay, so these are the neighbouring operations.",
    k="not")
add("Match List I (Agreement with the USA) with List II (Subject):\nList I: a. LEMOA  b. COMCASA  c. BECA  d. GSOMIA\nList II: 1. Sharing of geospatial data  2. Use of each other's bases for supplies  3. Secure military communication equipment  4. Protecting shared classified military information",
    [M(2, 3, 1, 4), M(3, 2, 1, 4), M(2, 3, 4, 1), M(1, 3, 2, 4)],
    "These are called the 'foundational agreements'. LEMOA (2016) is about logistics and supplies. COMCASA (2018) is about secure communication equipment. BECA (October 2020) is about maps, satellite images and other geospatial data. GSOMIA (2002) protects classified information. India holds the largest number of exercises with the USA, such as Yudh Abhyas, Tiger Triumph and Vajra Prahar.",
    k="match")
