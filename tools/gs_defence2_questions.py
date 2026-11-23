# GS Defence Mock 02: 25 questions on syllabus topic (h), made with the aso-mock skill (22 Nov 2026).
# Plan: python3 .claude/skills/aso-mock/scripts/draw.py ga --topics def --n 25 --seed 858136
# First option is right unless a is given. Facts: guide/defence-*.txt (Defence Guide) and questions/ca-defence*.json.

S12 = ["Only 1", "Only 2", "Both 1 and 2", "Neither 1 nor 2"]
S3 = ["Only 1 and 2", "Only 2 and 3", "Only 1 and 3", "1, 2 and 3"]

META = dict(
    paper="ga",
    title="ASO GS Defence Mock 02",
    hub_title="Defence 25 · GS Mock 02",
    link_title="Defence 25 mock",
    masthead="GS Defence 02",
    heading="General Studies Paper I · Defence Mock 02",
    tagline="25 questions on<br><b>Defence and the Armed Forces</b><br>drawn by probability.",
    key="aso-gs-defence-2",
    code="DEF2",
    out="ASO-GS-Mock-Defence-2.html",
    minutes=23,
    seed=858136,
    order="mixed",
    topic="def",
    date="22 Nov 2026",
    draw="python3 .claude/skills/aso-mock/scripts/draw.py ga --topics def --n 25 --seed 858136",
    intro=[
        "This is a short paper on one syllabus topic, (h) Defence and Indian Armed Forces, which gave 8 questions in 2018, 10 in 2021 and 12 in 2025. "
        "The families in it were drawn by how likely they are to be asked: exercises and their partners, weapons and where they come from, operations, border forces, ranks, awards, alliances and the 2026 defence news.",
        "Fourteen questions carry news from 2025 and 2026, and one is a real past question asked again (2021 Q81), because the examiner does repeat. "
        "Every answer says why it is right, which past question it grew from and what else in that family is likely next.",
    ],
    weights_note="Families were drawn by the aso-mock skill from the 2018, 2021 and 2025 Defence questions (2021 and 2025 at full weight, 2018 at half). News is from January to November 2026.",
)

Q = []
def add(q, o, e, k="one", n=False, c=False, a=None, **x):
    d = dict(s="Defence", q=q, o=o, e=e, k=k, n=n, c=c, a=a); d.update(x); Q.append(d)

# 1 weapons-platforms (news)
add("In August 2026 the Indian Navy leased two MQ-9B 'Sea Guardian' drones for 30 months. These drones are made by:",
    ["General Atomics", "Israel Aerospace Industries", "Elbit Systems", "Boeing"],
    "The MQ-9B Sea Guardian is a long-endurance drone made by General Atomics of the USA. The Navy had flown two leased MQ-9Bs since 2020, and the bigger deal for 31 MQ-9B drones for all three services was signed in 2024. "
    "The 2018 and 2021 papers asked where a weapon came from (Rafale from France, S-400 from Russia). The rest of the family: Heron drones come from Israel Aerospace Industries, Hermes 900 (Drishti-10) from Elbit's design, and the Apache and Chinook helicopters from Boeing.",
    n=True)
# 2 air-exercises (news)
add("'Veer Guardian', held at Jodhpur in September 2026 with Tejas, Su-30, Rafale and F-2A aircraft, is an air exercise between India and:",
    ["Japan", "Malaysia", "France", "United Arab Emirates"],
    "Veer Guardian is the air force exercise of India and Japan; the F-2A in the question is a Japanese fighter. Its first edition was in Japan in 2023. Do not mix it with Dharma Guardian, the army exercise with Japan, which the papers asked in 2021 and 2025. "
    "The other air exercises: Udara Shakti with Malaysia, Garuda with France, Desert Flag hosted by the UAE (asked in 2025), Pitch Black hosted by Australia and Tarang Shakti hosted by India.",
    n=True)
# 3 operations (stmt)
add("Consider the following statements:\n1. Operation Meghdoot (1984) was launched to secure the Siachen Glacier.\n2. Operation Safed Sagar was the Indian Air Force's operation in the Kargil War.\n3. Operation Trident (1971) was the Navy's attack on Karachi harbour.\nWhich of the statements given above is/are correct?",
    S3,
    "All three are correct. Meghdoot began on 13 April 1984 and gave India the Saltoro ridge above Siachen. In Kargil (1999) the Army's campaign was Operation Vijay, the Air Force's Safed Sagar and the Navy's Talwar. Trident (4 December 1971) was the missile-boat attack on Karachi, remembered on Navy Day. "
    "The 2025 paper asked operations as statements (Keller in Shopian) and by meaning (Zero Line). Learn the newer ones too: Sindoor (7 May 2025), Mahadev (July 2025), Sindhu (Iran evacuation), Brahma (Myanmar earthquake relief), Urja Suraksha (Hormuz escort, 2026).",
    k="stmt", a=3)
# 4 ranks
add("A Wing Commander in the Indian Air Force holds a rank equal to which rank in the Indian Army?",
    ["Lieutenant Colonel", "Major", "Colonel", "Brigadier"],
    "Wing Commander = Lieutenant Colonel = Commander in the Navy. One step below is Squadron Leader = Major (asked in 2021 Q90). One step above is Group Captain = Colonel, then Air Commodore = Brigadier. "
    "Learn the Air Force ladder against the Army's: Flying Officer (Lieutenant), Flight Lieutenant (Captain), Squadron Leader (Major), Wing Commander (Lieutenant Colonel), Group Captain (Colonel), Air Commodore (Brigadier), Air Vice Marshal (Major General), Air Marshal (Lieutenant General), Air Chief Marshal (General).")
# 5 renamed-places (news)
add("In 2025 Fort William in Kolkata, the headquarters of the Army's Eastern Command, was renamed as:",
    ["Vijay Durg", "Nehru Durg", "Manekshaw Durg", "Shivaji Durg"],
    "Fort William became Vijay Durg in 2025 as part of the drive to drop colonial names. In the same fort, Kitchener House became Manekshaw House and St George's Gate became Shivaji Gate. "
    "The 2025 paper (Q14) asked these as wrongly matched pairs, with 'Nehru Durg' and 'Fort St. David' as traps; this question asks the right name directly. The Eastern Command led the 1971 war, which is why its new names honour Manekshaw and victory.",
    n=True)
# 6 alliances
add("AUKUS, the security pact announced in September 2021, mainly aims to help which country build nuclear-powered submarines?",
    ["Australia", "India", "Japan", "Canada"],
    "AUKUS joins Australia, the United Kingdom and the United States; its first pillar gives Australia nuclear-powered (not nuclear-armed) submarines. "
    "The 2021 paper asked the members of the Quad (USA, India, Japan, Australia), so AUKUS is the neighbouring group. India is in the Quad but not in AUKUS; Canada is in the Five Eyes intelligence group (USA, UK, Canada, Australia, New Zealand).")
# 7 capf (stmt)
add("Consider the following statements about the Sashastra Seema Bal (SSB):\n1. It guards India's borders with Nepal and Bhutan.\n2. It works under the Ministry of Defence.\n3. It began in 1963 as the Special Service Bureau, after the war with China.\nWhich of the statements given above is/are correct?",
    S3,
    "Statement 2 is wrong: the SSB is a Central Armed Police Force under the Ministry of Home Affairs, like the BSF, CRPF, ITBP, CISF and Assam Rifles. Statements 1 and 3 are right; it became the SSB in 2003 and took over the Nepal (2001) and Bhutan (2004) borders. "
    "The 2025 paper asked three statements on the ITBP (Q29). Learn each force with its border: BSF (Pakistan and Bangladesh), ITBP (China), SSB (Nepal and Bhutan), Assam Rifles (Myanmar).",
    k="stmt", a=2)
# 8 missiles (news)
add("Project Kusha, whose missile had its first flight from Dr A. P. J. Abdul Kalam Island in July 2026, is developing a:",
    ["Long-range surface-to-air missile", "Air-to-air missile for the Tejas", "Submarine-launched ballistic missile", "Anti-tank guided missile"],
    "Kusha is DRDO's long-range surface-to-air missile system, India's own answer to the S-400, for air defence of cities and bases. Dr A. P. J. Abdul Kalam Island (once Wheeler Island) is in Bhadrak district of Odisha, and almost every big test happens there or at Chandipur. "
    "The 2025 paper asked the type and range of Pralay (Q36), so expect 'what type is missile X' again: Astra is air-to-air, K-4 is submarine-launched, Nag is anti-tank, LRLACM is a land-attack cruise missile.",
    n=True)
# 9 institutions
add("The Defence Services Staff College, which trains mid-career officers of all three services, is located at:",
    ["Wellington, Tamil Nadu", "Dehradun, Uttarakhand", "Khadakwasla, Maharashtra", "Secunderabad, Telangana"],
    "The DSSC is at Wellington in the Nilgiris. The others are the Indian Military Academy (Dehradun), the National Defence Academy (Khadakwasla, near Pune) and the College of Defence Management (Secunderabad). "
    "The 2018 and 2021 papers both asked where the Indian National Defence University is (Binola, Haryana). Learn the rest of the list: Indian Naval Academy at Ezhimala (Kerala), Air Force Academy at Dundigal (Hyderabad), National Defence College at New Delhi, Officers Training Academy at Chennai and Gaya.")
# 10 procurement (news)
add("In February 2026 the Defence Acquisition Council gave Acceptance of Necessity for 114 of which fighter aircraft under the Multi-Role Fighter Aircraft project?",
    ["Rafale", "Su-30MKI", "F-21", "Gripen"],
    "The DAC, chaired by the Defence Minister, cleared 114 Rafale jets on 12 February 2026, along with more P-8I aircraft and S-400 missiles. Acceptance of Necessity is only the first approval of a need: it does not choose a final contract or mean delivery. "
    "The 2021 paper asked an AoN given for an HAL aircraft (Q88). The Air Force already flies 36 Rafale (bases Ambala and Hasimara), and the Navy ordered 26 Rafale Marine in April 2025.",
    n=True)
# 11 capf (stmt)
add("Consider the following statements about the Border Security Force (BSF):\n1. It was raised on 1 December 1965.\n2. It guards India's borders with Pakistan and Bangladesh.\n3. It guards the India–Myanmar border.\nWhich of the statements given above is/are correct?",
    S3,
    "Statement 3 is wrong: the Myanmar border is guarded by the Assam Rifles. The BSF was raised after the 1965 war, guards the Pakistan and Bangladesh borders, and has its own Air Wing, Water Wing and artillery. "
    "The 2025 paper asked 'Operation Zero Line' on the India–Bangladesh border (Q20), which is the BSF's beat. Learn the raising years in order: Assam Rifles 1835, CRPF 1939, ITBP 1962, SSB 1963, BSF 1965, CISF 1969, NSG 1984.",
    k="stmt", a=0)
# 12 awards-people (news; a first by a woman officer)
add("In August 2026 Squadron Leader Bhawana Kanth became the first Indian woman to complete which course of the Indian Air Force?",
    ["Fighter Combat Leader course", "Experimental Test Pilot course", "Qualified Flying Instructor course", "Space flight training course"],
    "She finished the Fighter Combat Leader course at TACDE (Tactics and Air Combat Development Establishment), Gwalior, which trains the Air Force's top tactics instructors. Bhawana Kanth was also one of India's first three women fighter pilots in 2016, with Avani Chaturvedi and Mohana Singh. "
    "Firsts by people are a Defence family (2021 asked the 'Missile Woman of India', Tessy Thomas). Check: this news rests on fewer reports than the others, so confirm it before the exam.",
    n=True, c=True)
# 13 world-defence-systems
add("The THAAD (Terminal High Altitude Area Defense) missile defence system belongs to:",
    ["The United States", "Israel", "Russia", "China"],
    "THAAD is an American system that hits ballistic missiles in their last phase; the USA has placed it in South Korea and Israel. "
    "The 2025 paper asked whose 'Golden Dome' is (USA, Q9). The family: Iron Dome and David's Sling are Israeli, S-400 is Russian, and India's own shields are the two-phase Ballistic Missile Defence programme and 'Mission Sudarshan Chakra' (announced 15 August 2025).")
# 14 gallantry
add("Which is the third-highest gallantry award of India in peacetime?",
    ["Shaurya Chakra", "Kirti Chakra", "Vir Chakra", "Sena Medal"],
    "The peacetime ladder is Ashoka Chakra, Kirti Chakra, Shaurya Chakra. The wartime ladder is Param Vir Chakra, Maha Vir Chakra, Vir Chakra, so the Vir Chakra is a wartime award. The Sena Medal is a lower award of the Army for gallantry or devoted duty. "
    "The 2021 paper asked the only Air Force officer to win the Param Vir Chakra (Nirmal Jit Singh Sekhon). The next angles: the first PVC (Major Somnath Sharma, 1947) and the order of the awards.")
# 15 conferences (news)
add("The Joint Commanders' Conference of May 2026, which marked the first anniversary of Operation Sindoor, was held at:",
    ["Jaipur", "Kolkata", "Lucknow", "Dehradun"],
    "It met at Jaipur on 7 and 8 May 2026 with the theme 'Military Capability in New Domains', and released new doctrines. The Army Commanders' Conference of April 2026 declared 2026 the year of 'Networking and Data Centricity', after the Ministry had called 2025 the 'Year of Reforms'. "
    "The 2018 paper asked where the Air Force Commanders' Conference was held, so 'where and what theme' is the pattern.",
    n=True)
# 16 navy-exercises (stmt)
add("Consider the following pairs (naval exercise – partner country):\n1. Varuna – France\n2. KONKAN – Oman\n3. SLINEX – Sri Lanka\nWhich of the pairs given above is/are correctly matched?",
    S3,
    "Pair 2 is wrong: KONKAN is with the United Kingdom (its 2026 edition was off Plymouth). India's naval exercise with Oman is Naseem Al Bahr. Varuna is with France (24th edition, Toulon, 2026) and SLINEX with Sri Lanka (Visakhapatnam, 2026). "
    "The 2025 paper asked TROPEX, the Navy's own biggest drill (Q4). The rest of the family: SIMBEX (Singapore), JIMEX (Japan), AUSINDEX (Australia), Malabar (USA, Japan, Australia), IBSAMAR (Brazil, South Africa).",
    k="stmt", a=2)
# 17 alliances (not)
add("Which one of the following is NOT one of the four foundational defence agreements signed between India and the United States?",
    ["RELOS", "LEMOA", "COMCASA", "BECA"],
    "RELOS (Reciprocal Exchange of Logistics Support) is India's logistics agreement with Russia. The four with the USA are GSOMIA (2002, military information), LEMOA (2016, logistics), COMCASA (2018, secure communications) and BECA (2020, geospatial data). "
    "The 2021 paper asked the Quad's members; partnerships with the USA are the next angle, and India also has logistics pacts with France, Australia and Japan.",
    k="not")
# 18 world-defence-systems (news)
add("In September 2025 Pakistan signed a 'Strategic Mutual Defence Agreement', under which an attack on one is treated as an attack on both, with:",
    ["Saudi Arabia", "Türkiye", "China", "Qatar"],
    "Pakistan and Saudi Arabia signed the pact on 17 September 2025, months after Operation Sindoor. A link with Türkiye was reported later but is not this agreement. "
    "The 2025 paper asked whose missile shield the Golden Dome is, so world defence news with a country answer is the pattern. Related: NATO now has 32 members (Sweden joined in March 2024), and India's foreign policy rests on Article 51 (asked in 2025).",
    n=True)
# 19 air-exercises (stmt)
add("Consider the following statements:\n1. Exercise Pitch Black is hosted by the United States.\n2. Udara Shakti is an air exercise between India and Malaysia.\n3. Tarang Shakti is a multinational air exercise hosted by India.\nWhich of the statements given above is/are correct?",
    S3,
    "Statement 1 is wrong: Pitch Black is hosted by the Royal Australian Air Force in northern Australia (the IAF sent four Rafale and two C-17 in 2026); Red Flag is the one hosted by the USA. Udara Shakti is with Malaysia (Subang, August 2026), and Tarang Shakti is India's own multinational exercise, first held in 2024. "
    "The 2025 paper asked three statements on Desert Flag-10 (UAE, Q73); this is the same family from new sides.",
    k="stmt", a=1, n=True)
# 20 people
add("Who was India's first Chief of Defence Staff (CDS)?",
    ["General Bipin Rawat", "General Anil Chauhan", "General M. M. Naravane", "Admiral Karambir Singh"],
    "General Bipin Rawat became the first CDS on 1 January 2020 and died in a helicopter crash in December 2021. General Anil Chauhan was the second (2022), and General N. S. Raja Subramani became the third on 31 May 2026. Naravane and Karambir Singh were Army and Navy chiefs of the same time. "
    "The 2021 paper asked the 'present' Chief of Air Staff, so firsts and present holders of the top posts are the pattern; in 2026 all four top posts changed hands.")
# 21 exercise-participants (not)
add("Which one of the following countries is NOT a member of the Malabar naval exercise?",
    ["United Kingdom", "Japan", "Australia", "United States"],
    "Malabar began in 1992 as an India–USA exercise; Japan became a permanent member in 2015 and Australia rejoined in 2020, so the four Quad countries now take part. The 2026 edition was held near Japan. "
    "The 2025 paper asked which country did NOT take part in Sea Dragon 2025 (France, Q7). The same 'not a participant' style can come for RIMPAC, Pitch Black or Cope India.",
    k="not")
# 22 REPEAT 2021 Q81
add("The Indian National Defence University (INDU) is located at:",
    ["Binola Village, Haryana", "Dehradun", "New Delhi", "Chennai"],
    "The INDU is being built at Binola near Gurugram in Haryana to give higher defence education to officers of all three services and civilians. "
    "This exact question was asked in 2021 (Q81), and 2018 asked it too (Q58). The examiner repeats, so learn the whole list of defence academies with their places.",
    src="2021 Q81")
# 23 weapons-platforms (news)
add("The MH-60R 'Romeo' multi-role helicopters, 24 of which were bought for the Indian Navy, come from:",
    ["The United States", "France", "Russia", "Italy"],
    "The MH-60R is made by Lockheed Martin's Sikorsky in the USA and is the Navy's main anti-submarine helicopter; 21 of the 24 were in service by 2026. "
    "The 2021 paper asked which helicopter was inducted at INS Utkrosh, Port Blair (ALH Mk III, made by HAL). Learn the platform-and-country pairs: Rafale (France), S-400 (Russia), Apache and Chinook (USA), Scorpene submarines (France, built at Mazagon Dock).",
    n=True)
# 24 missiles (news)
add("RudraM-II, tested by DRDO and the Indian Air Force in June 2026, is a/an:",
    ["Air-to-surface missile", "Surface-to-air missile", "Submarine-launched ballistic missile", "Anti-tank guided missile"],
    "RudraM-II is an air-launched missile to strike targets on the ground, fired from the Su-30MKI; the RudraM family began with an anti-radiation missile to destroy enemy radars. "
    "The 2025 paper checked the type of Pralay (surface-to-surface, not air-to-surface). Keep one line per missile: Pralay surface-to-surface, Astra air-to-air, Akash surface-to-air, Nag anti-tank, K-4 submarine-launched, BrahMos supersonic cruise.",
    n=True)
# 25 army-exercises (news)
add("MAITREE, whose 15th edition was held at Surat Thani in August 2026, is a joint military exercise between India and:",
    ["Thailand", "Maldives", "Nepal", "Sri Lanka"],
    "MAITREE is the India–Thailand army exercise; Surat Thani is in southern Thailand. The wrong options are other neighbours' exercises: Ekuverin (Maldives), Surya Kiran (Nepal) and Mitra Shakti (Sri Lanka). "
    "Exercise and partner pairs come in every paper: Gandiv Vijay in 2018, Dharma Guardian (Japan) in 2021 and 2025, Nomadic Elephant (Mongolia) in 2025. Most exercises alternate venue each year, so the 2027 edition of MAITREE is likely in India.",
    n=True)
