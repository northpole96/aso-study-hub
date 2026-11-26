"""National and international events of 2026 (to 26 November 2026) that may come in the January 2027 ASO GA paper.
Used by tools/build_ca_pyq_analysis.py.

Facts come from the project's news bank (questions/ca-*.json, which carries its own check flags),
ASO-Current-Affairs-2026-Manual.html, ASO-Defence-2026-Digest.md and web searches made on 26 Nov 2026.
A fact found in only one place, or where sources differ, carries ⟨CHECK⟩.

Each section: id, num, title, eyebrow, expect (questions expected), intro (paragraphs), asked (past questions),
blocks: list of (subheading, rows); a row is (tier, title, when, body, hook)
  tier 3 = very likely, 2 = likely, 1 = possible
cards: (tag, question, answer, why)
Markup: **bold**, ⟦2025 Q10⟧ chip, ⟨CHECK⟩ tag.
"""

SECTIONS = [
# ---------------------------------------------------------------- DEFENCE
dict(id="def", title="Defence and security in 2026", eyebrow="Expected 10–13 questions",
 fig="shield",
 intro=[
  "Defence is now the biggest news family. In 2025, 14 of the 30 news questions were about defence: six exercises, three operations, two missiles, a new engine, a renaming and a ministry project. The examiner asks four things again and again: **exercises** (partner country, place, edition, who did not take part), **missiles** (type, range, maker), **operations** (what, where, against whom) and **posts** (who leads now).",
  "2026 is a rich year for all four. All four top posts changed, which almost never happens in one year. India held exercises with more than twenty countries, commissioned its third nuclear missile submarine, and ran a naval escort operation during the Iran war. Learn each item with its partner and its place, because the 2025 statement questions were won or lost on exactly those details.",
 ],
 asked=["⟦2021 Q20⟧ ⟦2025 Q90⟧ Dharma Guardian (Japan), asked twice", "⟦2025 Q55⟧ Nomadic Elephant · ⟦2025 Q7⟧ Sea Dragon (who did NOT take part) · ⟦2025 Q73⟧ Desert Flag", "⟦2025 Q36⟧ Pralay · ⟦2025 Q51⟧ scramjet · ⟦2021 Q87⟧ S-400 · ⟦2025 Q9⟧ Golden Dome", "⟦2025 Q50⟧ Operation Keller · ⟦2025 Q11⟧ Jindagi · ⟦2021 Q4⟧ Sajag", "⟦2021 Q82⟧ present Air Chief · ⟦2025 Q14⟧ renamed buildings · ⟦2025 Q13⟧ Bharat Ranbhoomi Darshan"],
 blocks=[
  ("Who leads the forces now", [
   (3, "Chief of Defence Staff: General N. S. Raja Subramani", "from 31 May 2026", "India's **3rd** CDS, after Bipin Rawat (2020) and Anil Chauhan (2022). His main task is to set up **theatre commands**: joint commands in which the Army, Navy and Air Force of one region work under one commander.", "Who is the 3rd CDS? Whom did he follow?"),
   (3, "Chief of the Army Staff: General Dhiraj Seth", "from 30 June 2026", "He was the Vice Chief before, and took over from General Upendra Dwivedi.", "The 2021 paper asked the 'present' Air Chief ⟦2021 Q82⟧; any of the four can come."),
   (3, "Chief of the Naval Staff: Admiral Krishna Swaminathan", "from 31 May 2026", "He headed the Western Naval Command (Mumbai) and took over from Admiral Dinesh K. Tripathi. The CDS and the Navy chief changed on the same day.", "Which two posts changed on 31 May 2026?"),
   (3, "Chief of the Air Staff: Air Chief Marshal Ashutosh Dixit", "from 31 October 2026", "The **29th** Air Chief, after A. P. Singh. The new Vice Chief of the Air Staff is Air Marshal Inderpal Singh Walia.", "Present Air Chief: a direct repeat of the 2021 style."),
  ]),
  ("Exercises of 2026: partner, place, edition", [
   (3, "Dharma Guardian (7th) · Japan · army", "late Feb – early Mar 2026", "Held in Uttarakhand ⟨CHECK⟩. Asked in 2021 and in 2025, so a third time is possible; if not the partner, then the place or the edition.", "Exact repeat candidate."),
   (3, "KHANJAR (13th) · Kyrgyzstan · special forces", "from 4 Feb 2026", "At Misamari, Sonitpur district, **Assam**. Do not mix up the Central Asian exercises: Kazakhstan = KAZIND and Prabal Dostyk, Uzbekistan = DUSTLIK, Mongolia = Nomadic Elephant.", "A 'match the exercise with the country' question fits here."),
   (3, "Yudh Abhyas (22nd) · USA · army", "from 15 Sep 2026", "At **Auli** (Uttarakhand) and Mahajan (Rajasthan), about 600 soldiers from each side. Older notes say Alaska: that was the 2025 edition.", "Place of Yudh Abhyas 2026."),
   (2, "Tiger Triumph · USA · all three services", "2026", "A disaster-relief exercise at **Visakhapatnam**; the NDRF took part for the first time. India holds more exercises with the USA than with any other country (Yudh Abhyas, Vajra Prahar, Tiger Triumph, Cope India, Malabar).", "Which country does India exercise with most?"),
   (2, "Vajra Prahar · USA · special forces", "early 2026", "At Bakloh, Himachal Pradesh ⟨CHECK⟩.", ""),
   (2, "DUSTLIK (7th) · Uzbekistan · army", "12–25 Apr 2026", "Held in Uzbekistan ⟨CHECK⟩. The two armies take turns; the 2025 edition was reported at Aundh, Pune.", ""),
   (2, "AUSTRAHIND (5th) · Australia · army", "from 19 Oct 2026", "Held in **Kerala**.", "Statement trap: 'held in Rajasthan'."),
   (2, "INDRA 2026 · Russia · army and navy", "13–18 Oct 2026", "Land and sea phases at **Vladivostok** and the Sea of Japan; INS Sahyadri took part.", ""),
   (2, "Garuda Shakti (11th) · Indonesia · special forces", "from 27 Oct 2026", "At Banyuwangi, Indonesia.", ""),
   (2, "Malabar 2026 · USA, Japan, Australia · navy", "5–12 Nov 2026", "Held off **Japan** ⟨CHECK⟩. Malabar began in 1992 as an India–US exercise.", "Malabar = the QUAD navies ⟦2021 Q83⟧."),
   (2, "International Fleet Review and MILAN 2026", "Feb 2026", "Both at **Visakhapatnam**. President Droupadi Murmu reviewed the fleet on 18 February. MILAN is the Navy's many-nation exercise.", "Where were IFR and MILAN 2026 held?"),
   (2, "RAHAT MITRA (1st) · Myanmar · all three services", "5–6 Nov 2026", "India's first relief exercise with Myanmar, at Chennai ⟨CHECK⟩.", "'First edition' is a favourite angle."),
   (1, "Other 2026 exercises", "", "PRAGATI (1st, armies of 12 Indian Ocean countries, Meghalaya ⟨CHECK⟩) · KAZIND (9th, Kazakhstan, Oskemen ⟨CHECK⟩) · Mountain Guardian (UAE, Chaubatia ⟨CHECK⟩) · KONKAN (UK, Plymouth ⟨CHECK⟩) · IBSAMAR IX (Brazil and South Africa, Simon's Town) · SIMBEX (33rd, Singapore ⟨CHECK⟩) · Udara Shakti (Malaysia, air force ⟨CHECK⟩) · Naseem Al Bahr (15th, Oman) · RIMPAC (Pearl Harbor ⟨CHECK⟩) · SAREX (Coast Guard, off Paradip).", "Partner-country matching."),
  ]),
  ("Missiles and tests (most from Odisha's coast)", [
   (3, "Agni-5 with MIRV", "8 May 2026", "Tested from Dr APJ Abdul Kalam Island, Odisha. **MIRV** (Multiple Independently targetable Re-entry Vehicle) means one missile carries several warheads, each able to hit a different target. Range over 5,000 km.", "Statement: 'MIRV means one warhead that splits into decoys' (false)."),
   (3, "Pralay user trial", "5 Nov 2026", "From Dr APJ Abdul Kalam Island. Pralay is a **surface-to-surface quasi-ballistic** missile (it flies a low, changeable path), range about 150–500 km, designed by DRDO's Research Centre Imarat and made by Bharat Dynamics. A salvo test came on 31 Dec 2025.", "The 2025 paper asked Pralay ⟦2025 Q36⟧; the next angle is the maker, the test site or the range."),
   (2, "LRLACM", "15 Jun 2026", "Long-Range Land Attack Cruise Missile; lead lab ADE, Bengaluru.", ""),
   (2, "Kusha", "23 Jul 2026", "First flight of the long-range surface-to-air missile of Project Kusha (India's own long-range air defence).", ""),
   (2, "Agni-4", "6 Aug 2026", "Range about 4,000 km ⟨CHECK test site⟩.", ""),
   (1, "AD-1, K-5, LRAShM", "2026", "AD-1 interceptor for Phase-II ballistic missile defence (November) ⟨CHECK⟩; K-5 submarine-launched missile test ⟨CHECK⟩; LRAShM, a hypersonic anti-ship glide vehicle ⟨CHECK⟩.", ""),
  ]),
  ("Ships, submarines and deals", [
   (3, "INS Aridhaman", "commissioned 3 Apr 2026", "India's **third** Arihant-class SSBN (a nuclear-powered submarine that carries ballistic missiles), at Visakhapatnam. Order: Arihant (1st) → Arighaat (2nd, 2024) → Aridhaman (3rd).", "'Aridhaman is the first SSBN built in India' (false)."),
   (2, "INS Surya (FSS-1)", "launched 6 Oct 2026", "India's first home-built **Fleet Support Ship** (a tanker that refuels and supplies warships at sea), launched at Hindustan Shipyard, Visakhapatnam. First of five.", "'Launched at Cochin Shipyard' (false)."),
   (2, "INS Mahendragiri", "commissioned 11 Jul 2026", "A Nilgiri-class (Project 17A) stealth frigate built by Mazagon Dock. Named after the Mahendragiri hill of Odisha's Eastern Ghats.", "Odisha link: Mahendragiri ⟦2025 Q60⟧ asked the hill ranges."),
   (2, "Rafale-M on INS Vikrant", "29 Oct 2026", "First landing of the naval Rafale on India's home-built carrier ⟨CHECK⟩. 26 Rafale-M were ordered in April 2025.", ""),
   (1, "Other ships", "2026", "INS Nipun (diving support vessel, Mumbai) · INS Samarthak (first multi-purpose vessel) · INS Anjadip and INS Mangrol (shallow-water anti-submarine craft) · ICGS Ajit (Coast Guard, Goa Shipyard ⟨CHECK⟩). One report counts 19 warships in 2026 ⟨CHECK⟩.", ""),
   (2, "Deals and money", "2026", "DAC Acceptance of Necessity for **114 Rafale** (12 Feb ⟨CHECK⟩) · HAL–Safran helicopter engine **'Aravalli'** (contract 26 Aug) · eight Next Generation Corvettes (GRSE five, Goa Shipyard three, November) · record **defence exports of ₹38,424 crore** in 2025-26.", "'DAC' and 'AoN' ⟦2021 Q88⟧."),
  ]),
  ("Operations, renaming and the Army's new shape", [
   (3, "Operation Urja Suraksha", "from about 28 Mar 2026", "'Urja' means energy. Indian Navy warships waited in the **Gulf of Oman** and escorted India-bound oil and gas ships coming out of the Strait of Hormuz during the Iran war.", "Operation names ⟦2025 Q50⟧ ⟦2025 Q11⟧."),
   (2, "Operation Him Setu", "Apr 2026", "Army rescue of tourists stranded by a landslide in North Sikkim (Lachen–Chungthang road) ⟨CHECK⟩.", "Like 'Operation Jindagi' ⟦2025 Q11⟧."),
   (2, "Operation Sindoor and Operation Sindhu (2025)", "May and Jun 2025", "Sindoor (7 May 2025): strikes on terror camps in Pakistan and PoK after the Pahalgam attack (22 April 2025). Sindhu (June 2025): evacuation of Indians from Iran. Old, but still the base for many questions.", "Two years old, like Silkyara in 2025."),
   (3, "246 colonial-era names dropped", "Feb 2026", "The Army renamed 246 roads, buildings and sites. In Delhi Cantonment, Kirby Place became Kenuguruse Vihar and Mall Road became **Arun Khetrapal Marg**; in Jaipur, Queens Line Road became Sundar Singh Marg; in Bareilly, New Birdwood Line became Thimayya Colony.", "Direct next angle of ⟦2025 Q14⟧ (Fort William → Vijay Durg)."),
   (1, "New Army units", "from 1 Jul 2026", "Rudra all-arms brigades, Bhairav light commando battalions, Shaktibaan artillery drone regiments, Divyastra batteries and Ashni drone platoons ⟨CHECK⟩.", ""),
  ]),
 ],
 cards=[
  ("Posts", "Who is India's 3rd Chief of Defence Staff (from May 2026)?", "General N. S. Raja Subramani", "After Bipin Rawat and Anil Chauhan. Next angle of ⟦2021 Q82⟧."),
  ("Exercise", "KHANJAR, held at Misamari in Assam in February 2026, is India's exercise with…", "Kyrgyzstan", "Kazakhstan = KAZIND, Uzbekistan = DUSTLIK, Mongolia = Nomadic Elephant ⟦2025 Q55⟧."),
  ("Submarine", "INS Aridhaman (April 2026) is India's ___ Arihant-class nuclear ballistic-missile submarine.", "Third", "Arihant → Arighaat (2024) → Aridhaman (2026)."),
  ("Operation", "'Operation Urja Suraksha' (2026) was…", "Navy escorts for India-bound oil and gas ships during the Hormuz crisis", "Urja = energy. Next angle of ⟦2025 Q50⟧."),
  ("Renaming", "In 2026 the Army renamed Mall Road in Delhi Cantonment after which Param Vir Chakra winner?", "Second Lieutenant Arun Khetrapal", "One of 246 renamings. Next angle of ⟦2025 Q14⟧."),
  ("Missile", "1. Agni-5 was tested with MIRV in May 2026. 2. MIRV lets one missile hit several targets. Which is/are correct?", "Both 1 and 2", "Tested from Dr APJ Abdul Kalam Island, Odisha."),
  ("Exercise", "Yudh Abhyas 2026 (22nd edition) with the USA was held at…", "Auli (Uttarakhand) and Mahajan (Rajasthan)", "The 2025 edition was in Alaska: an easy trap."),
 ]),

# ---------------------------------------------------------------- DAYS
dict(id="days", title="Days, themes and anniversaries", eyebrow="Expected 4–5 questions",
 fig="calendar",
 intro=[
  "Four or five questions come from days in every paper. There are two kinds. **Fixed dates** never change (World Water Day is always 22 March), so they are safe to learn early. **Themes** change every year, and the examiner likes the year before: in November 2025 it asked the Earth Day theme of **2024** and put the 2025 theme in as the trap. So for each big day, learn both the 2025 and the 2026 theme.",
  "The days asked so far are environmental (Earth Day three times, Oceans Day, Water Day), health (TB Day), citizen days (Voters' Day, Consumer Rights Day) and one government conference theme. The table below covers those days and their close cousins.",
 ],
 asked=["⟦2018 Q61⟧ ⟦2021 Q10⟧ ⟦2025 Q2⟧ Earth Day theme, three papers out of three", "⟦2018 Q9⟧ Oceans Day theme · ⟦2018 Q4⟧ Statistics Day theme · ⟦2018 Q50⟧ e-Governance conference theme", "⟦2025 Q99⟧ Voters' Day theme · ⟦2025 Q72⟧ TB Day statements", "⟦2025 Q22⟧ Water Day date · ⟦2025 Q28⟧ Consumer Rights Day date · ⟦2018 Q85⟧ World Hindi Day date"],
 table=dict(head=["Day and date", "2025 theme", "2026 theme"], rows=[
  ("National Voters' Day · 25 Jan", "Nothing Like Voting, I Vote for Sure", "My India, My Vote ⟨CHECK⟩"),
  ("World Wetlands Day · 2 Feb", "Protecting Wetlands for Our Common Future", "Wetlands and traditional knowledge (cultural heritage)"),
  ("World Consumer Rights Day · 15 Mar", "A Just Transition to Sustainable Lifestyles", "Safe Products, Confident Consumers ⟨CHECK⟩"),
  ("World Water Day · 22 Mar", "Glacier Preservation", "Water and Gender ('Where water flows, equality grows')"),
  ("World TB Day · 24 Mar", "Yes! We Can End TB: Commit, Invest, Deliver", "Yes! We Can End TB: Led by countries, powered by people ⟨CHECK⟩"),
  ("World Health Day · 7 Apr", "Healthy beginnings, hopeful futures", "Together for health. Stand with science."),
  ("Earth Day · 22 Apr", "Our Power, Our Planet (2024: Planet vs. Plastics)", "Reported as the same as 2025 ⟨CHECK⟩"),
  ("Biodiversity Day · 22 May", "Harmony with nature and sustainable development", "Acting Locally for Global Impact"),
  ("World Environment Day · 5 Jun", "Host Republic of Korea; plastic pollution", "Host **Azerbaijan**; climate action, #NowForClimate"),
  ("International Yoga Day · 21 Jun", "Yoga for One Earth, One Health (Visakhapatnam)", "Yoga for Healthy Ageing (12th Yoga Day) ⟨CHECK⟩"),
  ("Indigenous Peoples' Day · 9 Aug", "—", "Honouring Indigenous Midwives: Safeguarding Life and Well-being"),
 ]),
 blocks=[
  ("Fixed dates and their traps", [
   (3, "Water, Earth, Forests", "", "World Water Day **22 March** · Earth Day **22 April** · International Day of Forests **21 March** · World Wetlands Day 2 February (the Ramsar Convention was signed on 2 February 1971).", "⟦2025 Q22⟧ used 22 April and 21 March as traps."),
   (3, "Consumer and Hindi days", "", "World Consumer Rights Day **15 March** · National Consumer Day **24 December** (Consumer Protection Act, 1986) · World Hindi Day **10 January** · Hindi Diwas **14 September**.", "Asked ⟦2025 Q28⟧ and ⟦2018 Q85⟧; World Hindi Day falls a week before the exam."),
   (2, "Days with a story", "", "National Voters' Day 25 January (Election Commission set up 1950) · World Health Day 7 April (WHO founded 1948) · National Handloom Day 7 August (Swadeshi Movement began 1905) · Partition Horrors Remembrance Day 14 August · National Sports Day 29 August (Dhyan Chand) · Police Commemoration Day 21 October (Hot Springs, Ladakh, 1959) · National Unity Day 31 October (Sardar Patel) · National Education Day 11 November (Maulana Azad).", "'Why is the day on this date?' is a safe static hook."),
  ]),
  ("UN years and big anniversaries", [
   (3, "UN international years of 2026", "", "International Year of the **Woman Farmer**, of Rangelands and Pastoralists, and of Volunteers for Sustainable Development. 2025 was the year of Glaciers' Preservation, Cooperatives and Quantum Science and Technology.", "'Which is NOT a UN year of 2026?' with a 2025 year as the answer."),
   (3, "Vande Mataram at 150", "7 Nov 2025 – 7 Nov 2026", "Written by Bankim Chandra Chattopadhyay (1875) and published in Anandamath (1882). A year-long celebration; in 2026 the Prevention of Insults to National Honour Act was amended to protect its singing.", "Author, novel, year: a history question dressed as news."),
   (3, "Utkal Divas at 90", "1 Apr 2026", "Odisha became a separate province on 1 April 1936, so 2026 marked 90 years. The state's centenary (2036) is the target year of Odisha's plans.", "Odisha formation year: very likely somewhere in the paper."),
   (2, "Other anniversaries", "", "Sardar Patel 150 (31 Oct 2025) · Birsa Munda 150 (15 Nov 2025, Janjatiya Gaurav Divas) · **80th** Independence Day (15 Aug 2026; Modi's 13th speech in a row, Nehru gave 17) · SCO 25 years (2001) · BRICS 20 years (2006) · UN 80 years (2025).", ""),
  ]),
 ],
 cards=[
  ("Theme", "What was the theme of Earth Day 2025?", "Our Power, Our Planet", "2024: Planet vs. Plastics ⟦2025 Q2⟧. The examiner asks the year before."),
  ("Theme", "The World Water Day 2026 theme was…", "Water and Gender", "2025: Glacier Preservation. UN-Water sets the theme."),
  ("Host", "Which country hosted World Environment Day 2026?", "Azerbaijan", "2025: Republic of Korea. 2024: Saudi Arabia. UNEP leads the day."),
  ("UN year", "2026 is the UN International Year of the…", "Woman Farmer", "Also Rangelands and Pastoralists, and Volunteers. Cooperatives was 2025."),
  ("Date", "National Voters' Day is on 25 January because…", "The Election Commission was set up on 25 January 1950", "Theme 2025 ⟦2025 Q99⟧."),
  ("Odisha", "Utkal Divas 2026 marked how many years of Odisha as a separate province?", "90 (formed 1 April 1936)", "The centenary is in 2036."),
 ]),

# ---------------------------------------------------------------- SUMMITS
dict(id="summits", title="Summits and world bodies", eyebrow="Expected 2–4 questions",
 fig="globe",
 intro=[
  "Every paper has asked a summit host or a world body: CHOGM 2018, the SCO and BIMSTEC hosts and a new Security Council member in 2021, and BIMSTEC Youth and the WMO in 2025. The safe questions are **where**, **who hosted or chaired**, and **which number** (18th BRICS, 26th SCO). India chaired BRICS in 2026, so the BRICS summit in New Delhi is the strongest candidate.",
  "Climate meetings need care, because there are three different 'COP' meetings with their own numbers: the climate COP (COP31, Antalya), the biodiversity COP (COP17, Yerevan) and the desertification COP (COP17, Ulaanbaatar).",
 ],
 asked=["⟦2018 Q23⟧ CHOGM 2018 host · ⟦2021 Q53⟧ SCO host · ⟦2021 Q56⟧ BIMSTEC host · ⟦2025 Q44⟧ BIMSTEC Youth Summit", "⟦2021 Q57⟧ new UN Security Council member · ⟦2021 Q54⟧ NATO members · ⟦2025 Q5⟧ WMO statements · ⟦2021 Q14⟧ World Forestry Congress"],
 blocks=[
  ("The big summits of 2026", [
   (3, "18th BRICS summit · New Delhi", "12–13 Sep 2026", "**India chaired BRICS** in 2026. The summit adopted the New Delhi Declaration. The theme began with 'B' for Building: Building for Resilience, Innovation, Cooperation and Sustainability. BRICS has 11 members (Indonesia joined in 2025) and turned 20 (formed 2006).", "Host, chair, number of members."),
   (3, "26th SCO summit · Bishkek, Kyrgyzstan", "31 Aug – 1 Sep 2026", "Marked 25 years of the SCO (founded 2001) and produced the Bishkek Declaration. The 2025 summit was at Tianjin, China. The SCO Heads of Government met at Dushanbe in October ⟨CHECK⟩; Pakistan was reported as the next chair ⟨CHECK⟩.", "⟦2021 Q53⟧ confused the two SCO meetings: learn both."),
   (2, "G7 · Évian-les-Bains, France", "Jun 2026", "The 52nd G7 summit, hosted by France.", ""),
   (2, "G20 · USA presidency", "summit 14–15 Dec 2026, Miami", "After South Africa's 2025 summit at Johannesburg (the first G20 summit in Africa). The Miami summit is after this note; watch for the 2027 host.", ""),
   (2, "AI Impact Summit · New Delhi", "Feb 2026", "At Bharat Mandapam; ended with the New Delhi Declaration on AI Impact. India's first global AI summit as host.", "'Which city hosted the AI Impact Summit 2026?'"),
   (1, "CHOGM 2026 · Antigua and Barbuda", "Nov 2026", "The 28th Commonwealth Heads of Government Meeting, at St John's ⟨CHECK⟩. The 2024 meeting was in Samoa; the 2018 one in London ⟦2018 Q23⟧.", "Next angle of ⟦2018 Q23⟧."),
  ]),
  ("Climate and nature meetings", [
   (3, "COP31 · Antalya, Türkiye", "9–22 Nov 2026", "Türkiye hosted and held the presidency (Murat Kurum); Australia's Chris Bowen led the negotiations. It **ended without a main agreement**, the first COP to do so since Copenhagen (2009): about 30–90 countries, including the EU, rejected a text that did not mention fossil fuels. A just-transition mechanism survived. **COP32: Addis Ababa, Ethiopia, November 2027.**", "Host, outcome, next host."),
   (2, "CBD COP17 · Yerevan, Armenia", "2026", "The biodiversity COP. Do not mix it up with the climate COP31.", "'COP17 of which convention was held at Yerevan?'"),
   (1, "UNCCD COP17 · Ulaanbaatar, Mongolia", "Aug 2026", "The desertification COP ⟨CHECK⟩.", ""),
  ]),
  ("The United Nations", [
   (3, "Security Council election", "Jun 2026", "Elected for 2027–28: **Austria, Kyrgyzstan, Portugal, Trinidad and Tobago and Zimbabwe**. Kyrgyzstan won its first seat ever (it beat the Philippines after four rounds); **Germany lost**. Leaving at the end of 2026: Denmark, Greece, Pakistan, Panama, Somalia. Five non-permanent members are elected each year, for two years.", "Direct next angle of ⟦2021 Q57⟧."),
   (3, "Choosing the next Secretary-General", "term of Guterres ends 31 Dec 2026", "The General Assembly appoints the Secretary-General on the Security Council's recommendation. As of 26 November 2026 no one had been appointed; Michelle Bachelet and Macky Sall withdrew, and names in the race include Rebeca Grynspan and Rafael Grossi. **Check the name in December.**", "Who appoints the UN Secretary-General? (static, safe)"),
   (2, "UNESCO World Heritage Committee · Busan", "Jul 2026", "The 48th session added **Sarnath** as India's 45th World Heritage Site (see Environment).", ""),
   (1, "Smaller bodies", "", "The Bahamas became the 116th member of the International Solar Alliance (headquarters Gurugram ⟦2021 Q52⟧) ⟨CHECK⟩ · India joined the WTO fisheries subsidies agreement ⟨CHECK⟩ · the 19th Pravasi Bharatiya Divas is at Kolkata in January 2027 ⟨CHECK⟩ (the 18th was at Bhubaneswar, January 2025).", ""),
  ]),
 ],
 cards=[
  ("BRICS", "Where was the 18th BRICS summit held in September 2026?", "New Delhi (India chaired BRICS in 2026)", "It ended with the New Delhi Declaration. BRICS has 11 members."),
  ("SCO", "The 26th SCO summit (2026), marking 25 years of the SCO, was held at…", "Bishkek, Kyrgyzstan", "2025: Tianjin, China. Next angle of ⟦2021 Q53⟧."),
  ("COP31", "COP31 (November 2026) was hosted by ___ and ended…", "Türkiye (Antalya); without a main agreement", "COP32: Addis Ababa, Ethiopia, 2027."),
  ("UNSC", "Which Central Asian country won its first-ever UN Security Council seat in June 2026?", "Kyrgyzstan", "Germany lost. Next angle of ⟦2021 Q57⟧."),
  ("UN", "Who appoints the UN Secretary-General?", "The General Assembly, on the Security Council's recommendation", "Guterres's term ends on 31 December 2026."),
 ]),

# ---------------------------------------------------------------- WORLD
dict(id="world", title="The world: wars, leaders, firsts and disasters", eyebrow="Expected 2–4 questions",
 fig="strait",
 intro=[
  "World news comes in three shapes. **The biggest story of the year, asked as geography**: in 2022 it was the war in Ukraine (2021 Q17 asked which statement about Ukraine was wrong). In 2026 that story is the war on Iran and the closing of the Strait of Hormuz. **New leaders**: the 2018 paper asked Italy's new Prime Minister. **World firsts in law**: Saudi women driving (2018) and the UK's AI law (2025).",
  "2026 also had a fourth shape that the 2025 paper used: a natural disaster asked as physical geography (Mount Lewotobi in 2025). The twin earthquakes in Venezuela and the eruptions of Kanlaon fit that slot.",
 ],
 asked=["⟦2021 Q17⟧ Ukraine statements · ⟦2021 Q12⟧ Tibet law · ⟦2018 Q7⟧ Italy's new PM · ⟦2018 Q22⟧ Saudi women drive", "⟦2025 Q49⟧ first country to criminalise AI-made abuse images · ⟦2025 Q43⟧ Lewotobi volcano · ⟦2025 Q9⟧ Golden Dome"],
 blocks=[
  ("The Iran war and the Strait of Hormuz", [
   (3, "The war", "from 28 Feb 2026", "The USA and Israel struck Iran; Supreme Leader Ali Khamenei was killed and **Mojtaba Khamenei** was named the new Supreme Leader. Iran closed the Strait of Hormuz. **Pakistan** brokered a two-week ceasefire from 8 April; talks were held in Islamabad, and an 'Islamabad Memorandum' was signed in June, but the truce collapsed on 8 July. In November the war was still on; Iran exempted Indian ships from 4 November.", "Who mediated? Who is the new Supreme Leader?"),
   (3, "The static core: Hormuz", "", "The strait lies between **Iran and Oman** and joins the **Persian Gulf** to the Gulf of Oman and the Arabian Sea. About a fifth of the world's oil passes through it, and much of India's oil and gas.", "Asked like Ukraine in ⟦2021 Q17⟧: a statement about its location."),
  ]),
  ("New leaders", [
   (3, "Bangladesh: Tarique Rahman", "PM from 17 Feb 2026", "Of the **BNP**, after the election of 12 February. He is Khaleda Zia's son; the change ended the era of the 'two Begums'. Parliament elected Mirza Fakhrul Islam Alamgir as President in August ⟨CHECK⟩.", "'He leads the Awami League' (false)."),
   (3, "Nepal: Balendra Shah", "PM from 27 Mar 2026", "His Rastriya Swatantra Party won 182 of 275 seats. Aged 35, a former rapper and mayor of Kathmandu. Sushila Karki led the interim government before the election.", ""),
   (2, "Hungary: Péter Magyar", "election 12 Apr 2026", "His Tisza party ended Viktor Orbán's 16 years in power.", ""),
   (2, "Venezuela: Maduro removed", "3 Jan 2026", "US special forces captured President Nicolás Maduro in Caracas and flew him to the USA; Vice President Delcy Rodríguez became acting president.", ""),
   (2, "Brazil, Colombia, Japan, the Vatican", "", "Lula da Silva won a **fourth** term in Brazil (25 Oct 2026) · Abelardo de la Espriella became President of Colombia (7 Aug) ⟨CHECK⟩ · Sanae Takaichi is Japan's first woman Prime Minister (Oct 2025) · Pope Leo XIV (Robert Prevost) is the first Pope from the USA (May 2025).", ""),
  ]),
  ("World firsts and rulings", [
   (3, "Social media bans for children", "Dec 2025 – Jul 2026", "**Australia** became the first country to ban social media for children under 16 (10 December 2025). **France** became the first EU country with an age limit (under 15, law of July 2026). The UAE set 15 as the minimum age, a first for an Arab country ⟨CHECK⟩.", "Direct next angle of ⟦2025 Q49⟧ ('first country to…')."),
   (2, "Indus Waters Treaty award", "31 Aug 2026", "A Court of Arbitration at The Hague held the 1960 treaty to be fully in force; India rejected the award (it had put the treaty 'in abeyance' after the Pahalgam attack, April 2025). The treaty was signed by Nehru and Ayub Khan with the World Bank's help.", "Static hook: year and broker of the treaty."),
   (1, "Other world news", "", "US Supreme Court: the IEEPA emergency law does not let the President impose tariffs (20 Feb) · Saudi Arabia, Türkiye and Pakistan signed the Mecca Joint Defence Agreement (7 Aug) · the UN General Assembly backed the 'Equal Earth' map in place of Mercator ⟨CHECK⟩ · Paraguay's Senate removed President Santiago Peña ⟨CHECK⟩.", ""),
  ]),
  ("Disasters as geography", [
   (3, "Venezuela's twin earthquakes", "24 Jun 2026", "Magnitude 7.2 and then 7.5, 39 seconds apart, near Morón on the **Caribbean coast**; Caracas and La Guaira were hit hardest. The strongest since 1900; the death toll passed 6,000 by August ⟨CHECK final figure⟩.", "Next angle of ⟦2025 Q43⟧: 'which country / which sea coast'."),
   (2, "Kanlaon volcano", "eruptions Feb, Mar, Jul and Oct 2026", "On Negros island, **Philippines**, part of the Pacific Ring of Fire.", "'Kanlaon is in which country?' (the decoys would be Indonesia and Japan)."),
   (1, "Titan Ridge", "May 2026", "A new undersea volcano in the Bismarck Sea (Papua New Guinea) was given a provisional name ⟨CHECK⟩.", ""),
  ]),
 ],
 cards=[
  ("Geography", "The Strait of Hormuz lies between which two countries?", "Iran and Oman", "It joins the Persian Gulf to the Gulf of Oman."),
  ("Diplomacy", "Which country brokered the April 2026 ceasefire in the Iran war?", "Pakistan", "Talks were held in Islamabad."),
  ("Leaders", "Balendra Shah, Nepal's Prime Minister from March 2026, was earlier…", "Mayor of Kathmandu", "Rastriya Swatantra Party, 182 of 275 seats."),
  ("Leaders", "Tarique Rahman became Prime Minister of Bangladesh in 2026. His party?", "BNP", "Not the Awami League."),
  ("First", "Which was the first EU country to set an age limit for social media (2026)?", "France (under 15)", "Australia was the world's first (under 16, December 2025). Next angle of ⟦2025 Q49⟧."),
  ("Disaster", "The twin earthquakes of June 2026 struck which country's Caribbean coast?", "Venezuela", "Magnitude 7.2 and 7.5. Next angle of ⟦2025 Q43⟧."),
 ]),

# ---------------------------------------------------------------- POLITY
dict(id="polity", title="India: Constitution, courts and posts", eyebrow="Expected 1–3 questions",
 fig="pillar",
 intro=[
  "Polity is the largest static topic (15 questions per paper), but news enters it in only a few ways: a Supreme Court ruling read into **Article 21** (privacy in 2018, maternity leave in 2025), and changes that touch an Article of the Constitution. In 2026 two such changes happened: Kerala became **Keralam** and Parliament raised the number of Supreme Court judges. Both have a clean static hook, which is exactly what the examiner likes.",
  "Office holders are also safe questions, because one name is right on exam day. The table lists who holds each post now.",
 ],
 asked=["⟦2018 Q16⟧ Right to Privacy · ⟦2025 Q6⟧ maternity leave under Article 21", "⟦2025 Q34⟧ Election Commission (static, but the CEC law was in the news)"],
 blocks=[
  ("Changes with an Article behind them", [
   (3, "Kerala becomes Keralam", "Aug 2026", "Done by a **law of Parliament under Articles 3 and 4**, not by a constitutional amendment under Article 368. The same route renamed Orissa as Odisha in 2011.", "'Done by an amendment under Article 368' (false)."),
   (3, "Supreme Court: 38 judges", "2026 law", "Parliament fixes the number by law under **Article 124(1)**. It went from 33 + the Chief Justice (34) to **37 + the Chief Justice (38)**. After three judges took oath on 6 October 2026, the working strength was 37 ⟨CHECK⟩.", "'Fixed by the President' (false)."),
   (2, "Census 2027", "house listing Apr–Sep 2026", "India's **first digital census**, and the first to count caste since 1931. People could fill in their own house details (self-enumeration) for the first time. The count of people is in February 2027; reference date **1 March 2027** (1 October 2026 for snow-bound areas).", "Reference date; caste last counted in 1931."),
   (2, "Vande Mataram protected", "2026", "The Prevention of Insults to National Honour Act was amended so that deliberately stopping the singing of Vande Mataram is punishable.", ""),
   (2, "Other new rules", "2026", "Indian Standard Time is now the only legal time reference (Legal Metrology (IST) Rules, 2026) · a new bench of the High Court of J&K and Ladakh opened at **Leh** (18 Oct) · Gujarat's Uniform Civil Code Bill got the President's assent ⟨CHECK⟩ (Uttarakhand was first, 2025) · heatwave and lightning were added to the notified disasters ⟨CHECK⟩.", ""),
   (1, "Supreme Court rulings of 2026", "", "Menstrual health linked to Article 21 (January) ⟨CHECK⟩ · the 24 hours for producing an arrested person before a magistrate (Article 22(2)) run from the real time of detention ⟨CHECK⟩ · the OBC creamy layer cannot be decided only by parents' salary (6 Nov) ⟨CHECK⟩.", "Article 21 ⟦2025 Q6⟧ ⟦2018 Q16⟧."),
  ]),
  ("Who holds the post now", [
   (3, "Top posts", "26 Nov 2026", "President **Droupadi Murmu** (15th; from Mayurbhanj, Odisha) · Vice-President **C. P. Radhakrishnan** (elected 9 Sep 2025 after Jagdeep Dhankhar resigned in July 2025) · Chief Justice **Surya Kant** (53rd, till 9 Feb 2027; his successor is named in January) · Chief Election Commissioner **Gyanesh Kumar** · CAG **K. Sanjay Murthy** · Governor of Odisha **Braj Mohan Ram** (from October 2026, after Hari Babu Kambhampati).", "'Present holder' questions."),
   (3, "State elections of 2026 (results 4 May)", "", "**West Bengal**: BJP's first government, Suvendu Adhikari Chief Minister; Mamata Banerjee lost Bhabanipur after 15 years in power. **Tamil Nadu**: actor Vijay's TVK (Tamilaga Vettri Kazhagam) won; Vijay became CM and M. K. Stalin lost his seat. **Kerala**: the Congress-led UDF ended ten years of LDF rule; V. D. Satheesan became CM. **Assam**: Himanta Biswa Sarma's second term.", "'Which party won Tamil Nadu?' and 'first BJP CM of West Bengal'."),
   (1, "Parliament", "Monsoon Session 20 Jul – 13 Aug 2026", "The Lok Sabha worked only about 19% of its time and the Rajya Sabha about 39%; twelve Bills passed.", ""),
  ]),
 ],
 cards=[
  ("Article", "Kerala's name was changed to Keralam in 2026 under which Articles?", "Articles 3 and 4 (a law of Parliament)", "Not an amendment under Article 368. Orissa → Odisha (2011) went the same way."),
  ("Judiciary", "After the 2026 law, how many judges can the Supreme Court have in all?", "38 (37 + the Chief Justice)", "Parliament fixes the number under Article 124(1)."),
  ("Census", "Census 2027 will be the first since ___ to count caste.", "1931", "Also India's first digital census. Reference date: 1 March 2027."),
  ("Elections", "Who became the first BJP Chief Minister of West Bengal in May 2026?", "Suvendu Adhikari", "Mamata Banerjee lost Bhabanipur."),
  ("Post", "Justice Surya Kant, the 53rd Chief Justice of India, serves till…", "9 February 2027", "His successor is named in January 2027."),
 ]),

# ---------------------------------------------------------------- ECONOMY
dict(id="economy", title="India: budget, economy and schemes", eyebrow="Expected 2–4 questions",
 fig="ledger",
 intro=[
  "The economy family asks words and names, not big numbers: 'Virtual Digital Assets' from the 2022 budget, a 'Child Budget', the repo rate after a named meeting, the ministry behind a festival. The safe facts for 2027 are the **firsts** (first budget under the 16th Finance Commission, the new GDP base year), the **names of new laws and schemes** and the **trade partners** of 2025–26.",
  "Learn the latest repo rate and the one before it, as 2018 Q76 showed: the setter named the meeting so the key would stay right even after the rate moved.",
 ],
 asked=["⟦2021 Q1⟧ Budget word 'Virtual Digital Assets' · ⟦2021 Q2⟧ Child Budget · ⟦2018 Q76⟧ repo rate after a named meeting", "⟦2018 Q20⟧ POSHAN month · ⟦2021 Q9⟧ BHASHINI · ⟦2021 Q3⟧ Villages of Excellence · ⟦2025 Q3⟧ BBBP campaign · ⟦2025 Q42⟧ Purple Fest"],
 blocks=[
  ("Budget, growth and prices", [
   (3, "Union Budget 2026-27", "1 Feb 2026", "Presented by Nirmala Sitharaman. Fiscal deficit target **4.3%** of GDP (2025-26: 4.4%), revenue deficit 1.5%, debt 55.6% of GDP; no change in income-tax rates. The **first budget under the 16th Finance Commission**.", "'First budget under which Finance Commission?'"),
   (3, "16th Finance Commission", "covers 2026–31", "Chair **Arvind Panagariya**. States keep **41%** of central taxes, as under the 15th (chair N. K. Singh). The Finance Commission is set up under Article 280 ⟦2021 Q43⟧.", "Chair and share."),
   (3, "New base years", "27 Feb 2026", "The GDP series moved from base 2011-12 to **2022-23**; the CPI moved from 2012 to **2024**. Growth for 2025-26 was put at 7.6%. The Index of Core Industries got iron ore as a ninth industry.", "'The new GDP base year is…'"),
   (2, "RBI", "Aug and Oct 2026", "Repo rate kept at 5.25% in August, then **raised to 5.50%** in October (first hike of this cycle; stance changed from 'neutral' to 'calibrated tightening'). SDF 5.25%, MSF and Bank Rate 5.75%. Retail inflation for October was about 6.1%, above the 6% upper limit ⟨CHECK⟩. **Next policy: 2–4 December.**", "Repo: the RBI lends to banks at this rate. Like ⟦2018 Q76⟧."),
  ]),
  ("New laws and schemes", [
   (3, "VB–G RAM G Act", "passed Dec 2025", "The Viksit Bharat – Guarantee for Rozgar and Ajeevika Mission (Gramin) Act **replaced MGNREGA** and raised the work guarantee from 100 to **125 days**. In force from 1 July 2026 ⟨CHECK⟩.", "'It promises 150 days' (false)."),
   (3, "GST 2.0 and the Labour Codes", "Sep and Nov 2025", "GST 2.0 (22 Sep 2025): two main rates, 5% and 18%, plus 40% on luxury and 'sin' goods. Four Labour Codes (21 Nov 2025) replaced **29** old labour laws: Wages, Industrial Relations, Social Security, and Occupational Safety, Health and Working Conditions.", "'Which is NOT a Labour Code?'"),
   (2, "Schemes approved in 2026", "", "India Semiconductor Mission 2.0 (about ₹1.27 lakh crore, July) · **PM Surya Sarovar Yojana** (floating solar, 5,000 MW, July) · **Samudra Manthan**, a national offshore exploration scheme · PM Viksit Gram Swaraj Yojana for panchayats ⟨CHECK⟩ · SUMAN Roadmap 2030 (maternal mortality below 70 per lakh births).", "Scheme → its purpose, like ⟦2021 Q9⟧."),
  ]),
  ("Trade deals", [
   (3, "India–UK, Oman, New Zealand, EU", "2025–26", "UK trade agreement (CETA) signed 24 Jul 2025, in force 15 Jul 2026 · Oman CEPA signed at Muscat, 18 Dec 2025 · **New Zealand** FTA signed 27 Apr 2026 (dairy kept out), in force 20 Oct 2026 · India–EU talks concluded in January 2026 ('the mother of all deals'); the EU's two top leaders were Republic Day 2026 chief guests.", "'With which country did India sign an FTA in April 2026?'"),
   (1, "Smaller items", "", "Talks for a trade agreement with Mexico (28 Oct) and with SACU, the Southern African Customs Union · border trade through Nathu La resumed on 1 August after six years ⟨CHECK⟩ · a UPI link with the Maldives' Favara system ⟨CHECK⟩.", ""),
  ]),
 ],
 cards=[
  ("Budget", "Budget 2026-27 was the first under which Finance Commission?", "The 16th (chair Arvind Panagariya)", "States' share stays at 41%."),
  ("Base year", "The new GDP series released in February 2026 uses which base year?", "2022-23", "Old base 2011-12. CPI's new base is 2024."),
  ("Law", "The VB–G RAM G Act, which replaced MGNREGA, guarantees how many days of work?", "125 days", "MGNREGA gave 100."),
  ("RBI", "After the October 2026 policy, the repo rate is…", "5.50%", "Raised from 5.25%; stance 'calibrated tightening'. Re-check after 2–4 December."),
  ("Trade", "India signed a free trade agreement with which country on 27 April 2026?", "New Zealand", "In force from 20 October 2026."),
 ]),

# ---------------------------------------------------------------- ODISHA
dict(id="odisha", title="Odisha in the news, 2026", eyebrow="Expected 2–3 questions",
 fig="turtle",
 intro=[
  "The 2025 paper had two pure Odisha news questions (the UK's Net Zero Vision for Bhubaneswar and Operation Olivia at Rushikulya), and Odisha appeared inside others: in the ISFR answer, as decoy districts in the Beti Bachao question, and in the Pralay test site. Olive ridleys were asked in 2018 and again in 2025, so the 2026 nesting season is a strong candidate.",
  "Odisha's coast is also India's missile test range. Most tests of 2026 (Agni-5, Pralay) were fired from Dr APJ Abdul Kalam Island or Chandipur, so a defence question can carry an Odisha answer.",
 ],
 asked=["⟦2025 Q27⟧ Operation Olivia, Rushikulya · ⟦2018 Q62⟧ olive ridleys (static)", "⟦2025 Q25⟧ Net Zero Vision with the UK · ⟦2018 Q5⟧ first Tribal Queen · ⟦2025 Q92⟧ Odisha in the ISFR answer"],
 blocks=[
  ("Wildlife and nature", [
   (3, "Olive ridleys 2026", "Feb–Mar 2026", "**Gahirmatha had no mass nesting (arribada)** in 2026, while Rushikulya had mass nesting from mid-March ⟨CHECK numbers⟩. Arribada (Spanish for 'arrival') is when thousands of females come ashore together to lay eggs. Odisha's three mass nesting sites: Gahirmatha, Rushikulya, Devi river mouth.", "Next angle of ⟦2025 Q27⟧: 'Which beach saw no arribada in 2026?'"),
   (2, "Ramsar sites", "", "Odisha has **six**: Chilika (1981, India's first, with Keoladeo), Bhitarkanika (2002), Satkosia, Tampara, Hirakud and Ansupa. India has 103 (October 2026).", "'Which is NOT a Ramsar site of Odisha?' (Similipal)."),
   (1, "Unusual news", "Sep 2026", "Five baby orangutans found in Balasore district were taken to Nandankanan ⟨CHECK⟩.", ""),
  ]),
  ("Money, projects and firsts", [
   (3, "Odisha Budget 2026-27", "20 Feb 2026", "About **₹3.10 lakh crore**, presented by Chief Minister Mohan Charan Majhi, who holds Finance. Fiscal deficit capped at 3.5% of GSDP; aim of 12% nominal GSDP growth. Main schemes: Subhadra (women), Samrudha Krushaka (farmers), Mission PoWaR (Power, Water and Roads for every revenue village), Gopabandhu Jan Arogya Yojana (health).", "Scheme → its group."),
   (3, "Semiconductor MoU", "Jun 2026", "With **Intel** and 3D Glass Solutions (USA), about US$3.3 billion, for a glass-substrate chip packaging unit at Info Valley, Bhubaneswar, called the first of its kind in India.", "'With which companies?' (a foreign partner, like ⟦2025 Q25⟧)."),
   (2, "Upper Indravati pumped storage", "approved 9 Nov 2026", "600 MW at Ranibahal, **Kalahandi**. A pumped-storage plant pumps water uphill when power is cheap and lets it run down through turbines when power is needed.", "District and capacity."),
   (2, "Odisha's coast in defence news", "2026", "Pralay (5 Nov) and Agni-5 MIRV (8 May) from **Dr APJ Abdul Kalam Island**; SAREX-2026, the Coast Guard's search-and-rescue exercise, off **Paradip** (October); HAL's Koraput (Sunabeda) unit delivered its 2,000th aero-engine ⟨CHECK⟩.", ""),
   (1, "Smaller items", "", "Paradip given 'Mega Port' status ⟨CHECK⟩ · Puri first among clean coastal towns in Swachh Survekshan ⟨CHECK⟩ · RBI cyber-security training institute at Bhubaneswar ⟨CHECK⟩ · first National Indoor Athletics Championships at Kalinga Stadium (24–25 Mar) · Suando (Puri), birthplace of Gopabandhu Das, to be developed (₹585 crore).", ""),
  ]),
  ("People and honours", [
   (2, "Literature", "2026", "Sahitya Akademi Award 2025 (Odia): Girijakumar Baliyar Singh for the poetry book **Padapurana** · Sahitya Akademi Fellowship: **Pratibha Ray** (author of Yajnaseni), September · Yuva Puraskar: Subrat Senapati (Kadambana).", ""),
   (2, "Hockey", "Oct 2026", "India's women won Asian Games hockey gold for the first time in 44 years; Odisha has sponsored Indian hockey since 2018 and announced a reward for the players linked to the state ⟨CHECK amount⟩.", ""),
  ]),
 ],
 cards=[
  ("Olive ridley", "Which Odisha nesting beach saw no mass nesting of olive ridleys in 2026?", "Gahirmatha", "Rushikulya did have mass nesting. Next angle of ⟦2025 Q27⟧."),
  ("Project", "The 600 MW Upper Indravati pumped-storage project (approved November 2026) is in which district?", "Kalahandi", "At Ranibahal."),
  ("Defence", "Pralay was test-fired on 5 November 2026 from…", "Dr APJ Abdul Kalam Island, Odisha", "Pralay is surface-to-surface ⟦2025 Q36⟧."),
  ("Industry", "Odisha's 2026 semiconductor MoU was signed with Intel and…", "3D Glass Solutions (USA)", "For a unit at Info Valley, Bhubaneswar."),
  ("Ramsar", "Which is NOT one of Odisha's six Ramsar sites? Chilika, Hirakud, Similipal, Ansupa", "Similipal", "It is a national park and tiger reserve."),
 ]),

# ---------------------------------------------------------------- SPACE
dict(id="space", title="Space, science and the Nobel Prizes", eyebrow="Expected 1–2 questions",
 fig="rocket",
 intro=[
  "Space questions ask the mission, the rocket, the orbit or the lander's name, and they are not only about the latest launch. The 2018 paper asked Chandrayaan-2's lander before it flew; the 2025 paper asked the orbit of a satellite whose launch had failed. In 2026 the PSLV failed again, Gaganyaan's first uncrewed flight slipped, and NASA flew people around the Moon for the first time since 1972.",
  "Nobel Prizes come about once a paper, and not always from the latest year (2021 asked the 2019 Chemistry prize). Learn 2025 and 2026.",
 ],
 asked=["⟦2025 Q48⟧ EOS-09 orbit on PSLV-C61 · ⟦2018 Q59⟧ Chandrayaan-2 lander Vikram · ⟦2021 Q11⟧ China's Chang'e-5", "⟦2021 Q91⟧ Nobel Chemistry 2019 · ⟦2021 Q19⟧ Boltzmann Medal · ⟦2025 Q51⟧ scramjet science"],
 blocks=[
  ("India in space", [
   (3, "PSLV-C62 fails", "12 Jan 2026", "It carried DRDO's **EOS-N1 'Anvesha'** (a maritime surveillance satellite) and 15 small satellites. A problem near the end of the **third stage** stopped them reaching orbit. It was the PSLV's second failure in a row, after PSLV-C61 / EOS-09 (18 May 2025).", "Direct next angle of ⟦2025 Q48⟧."),
   (3, "Gaganyaan G1", "slipped from Dec 2026", "The first uncrewed flight will carry the humanoid robot **Vyommitra**. In November reports said it is unlikely before February 2027; ISRO (chairman V. Narayanan) has not fixed a date. Three uncrewed flights come before the first crewed one.", "Like ⟦2018 Q59⟧: a mission about to fly."),
   (2, "Earlier milestones still asked", "2025", "**Shubhanshu Shukla**: first Indian on the International Space Station (Axiom-4, June–July 2025), second Indian in space after Rakesh Sharma (1984) · **NISAR**: NASA–ISRO radar satellite, launched 30 July 2025 on **GSLV-F16**.", "'NISAR was launched on a PSLV' (false)."),
   (1, "Plans and private rockets", "", "Bharatiya Antariksh Station by 2035; an Indian on the Moon by 2040 · Skyroot's Vikram-1 reported as the first privately built Indian rocket to reach orbit ⟨CHECK⟩ · TRISHNA with France's CNES ⟨CHECK⟩ · LIGO-India at Hingoli, Maharashtra.", ""),
  ]),
  ("World space and science", [
   (3, "Artemis II", "1–10 Apr 2026", "NASA's first crewed flight around the Moon since **Apollo 17 (1972)**, on the SLS rocket in the Orion capsule. Crew: Reid Wiseman (commander), Victor Glover, Christina Koch and **Jeremy Hansen of Canada**. They flew farther from Earth than any humans before (beating Apollo 13). They did not land.", "'Artemis II landed on the Moon' (false)."),
   (1, "Other missions", "", "Japan's MMX, launched in October to study Mars's moons Phobos and Deimos ⟨CHECK⟩.", ""),
  ]),
  ("Nobel Prizes", [
   (3, "2026", "Oct 2026", "Peace: **Navi Pillay** (South Africa, former UN human rights chief) · Literature: **Anne Carson** (Canada) · Medicine: Karl Deisseroth, Peter Hegemann and Georg Nagel for **optogenetics** (controlling nerve cells with light) · Physics: Francis Halzen (IceCube neutrino observatory) · Chemistry: Henri Kagan and Kenso Soai ⟨CHECK⟩ · Economics: Robert E. Hall and Michael Woodford ⟨CHECK⟩.", "One per paper, often an older year."),
   (2, "2025", "Oct 2025", "Peace: María Corina Machado (Venezuela) · Literature: László Krasznahorkai (Hungary) · Economics: Joel Mokyr, Philippe Aghion and Peter Howitt (innovation-led growth).", ""),
  ]),
 ],
 cards=[
  ("ISRO", "Which satellite was lost when PSLV-C62 failed in January 2026?", "EOS-N1 'Anvesha' (DRDO)", "Second PSLV failure in a row, after C61 / EOS-09 ⟦2025 Q48⟧."),
  ("Gaganyaan", "The robot that will fly on Gaganyaan's first uncrewed mission is…", "Vyommitra", "Like the Vikram lander question ⟦2018 Q59⟧."),
  ("Artemis", "Besides three Americans, Artemis II (April 2026) carried an astronaut from…", "Canada (Jeremy Hansen)", "First crewed flight around the Moon since 1972."),
  ("Nobel", "Who won the Nobel Peace Prize 2026?", "Navi Pillay (South Africa)", "2025: María Corina Machado (Venezuela)."),
 ]),

# ---------------------------------------------------------------- ENVIRONMENT
dict(id="env", title="Environment and heritage", eyebrow="Expected 1–2 questions",
 fig="leaf",
 intro=[
  "Environment news questions ask about new protected places, reports and counts. The ISFR came twice (2018 and 2025), the WMO's warmest year in 2025, the Jeypore rainforest in 2021. For 2027, learn three running counts and their newest members: **World Heritage Sites (45)**, **Ramsar sites (103)** and **tiger reserves (58)**.",
 ],
 asked=["⟦2018 Q48⟧ ⟦2025 Q92⟧ India State of Forest Report · ⟦2025 Q5⟧ WMO warmest year · ⟦2021 Q92⟧ Dehing Patkai · ⟦2021 Q14⟧ World Forestry Congress", "⟦2025 Q100⟧ first mammal lost to climate change · ⟦2025 Q86⟧ UNESCO Memory of the World"],
 blocks=[
  ("Counts and newest members", [
   (3, "Sarnath: India's 45th World Heritage Site", "25 Jul 2026", "The 'Ancient Buddhist Site of Sarnath' near Varanasi, **Uttar Pradesh**, added at the 48th session in Busan, South Korea. It is where the Buddha gave his **first sermon**. (Bodh Gaya, in Bihar, is where he gained enlightenment.)", "'Sarnath is in Bihar' (false)."),
   (3, "Ramsar sites: 103", "Oct 2026", "Newest: Sukhna wetland (Chandigarh) and Sauj Jheel (UP), 15 October ⟨CHECK⟩; Glaw Lake, Arunachal Pradesh's first, in August ⟨CHECK⟩. A Ramsar site is a wetland of world importance under the Ramsar Convention (1971, Iran).", "Count and newest site."),
   (3, "Tiger reserves: 58", "", "The 58th is **Madhav**, Madhya Pradesh (March 2025); MP now has nine. 57th: Ratapani (MP); 56th: Guru Ghasidas–Tamor Pingla (Chhattisgarh). The tiger count of 2022 was 3,682; the next report is due in 2027.", ""),
   (2, "COP31 failed", "22 Nov 2026", "No main agreement at Antalya (see Summits). The Dubai (COP28) promise to transition away from fossil fuels still stands.", ""),
  ]),
  ("Wildlife and reports", [
   (2, "Great Indian Bustard rewilding", "Oct 2026", "Captive-bred birds released in Desert National Park, Jaisalmer ⟨CHECK⟩ · captive-bred vultures released in Kaziranga ⟨CHECK⟩ · the Asiatic lion count was 891 in 2025 (523 in 2015), all in Gujarat ⟨CHECK⟩.", ""),
   (2, "Western Ghats", "2026", "A draft notification marked about 56,800 sq km across six states as ecologically sensitive ⟨CHECK⟩.", ""),
   (1, "Watch: the next India State of Forest Report", "", "The ISFR is published every two years by the Forest Survey of India (Dehradun). ISFR 2023 came in December 2024. If ISFR 2025 is released before the exam, it is a strong candidate, because the ISFR has come twice ⟨CHECK release⟩.", "Next angle of ⟦2025 Q92⟧."),
   (1, "Heritage", "Dec 2025", "Deepavali was added to UNESCO's list of Intangible Cultural Heritage at a session hosted by India in New Delhi.", ""),
  ]),
 ],
 cards=[
  ("Heritage", "Which site became India's 45th UNESCO World Heritage Site in July 2026?", "Sarnath (Uttar Pradesh)", "Where the Buddha gave his first sermon."),
  ("Wetlands", "How many Ramsar sites did India have in October 2026?", "103", "Odisha has six; Chilika was first (1981)."),
  ("Tigers", "India's 58th tiger reserve is…", "Madhav, Madhya Pradesh", "MP now has nine tiger reserves."),
 ]),

# ---------------------------------------------------------------- REPORTS
dict(id="reports", title="Reports and India's rank", eyebrow="Expected 0–1 question",
 fig="ranks",
 intro=[
  "Report questions were common in 2018 (Global Peace Index rank, the UN city forecast) and rare since (World Giving Index in 2021; in 2025 reports came only inside other questions). Learn the **publisher**, India's **rank** and the **number of countries**, and the topper.",
 ],
 asked=["⟦2018 Q8⟧ Global Peace Index rank · ⟦2018 Q24⟧ UN urbanisation report · ⟦2021 Q18⟧ World Giving Index topper · ⟦2021 Q15⟧ publisher of South Asia Economic Focus (World Bank)"],
 table=dict(head=["Report 2026 (publisher)", "India", "Top / note"], rows=[
  ("Global Peace Index (Institute for Economics and Peace, Sydney)", "127th of 163", "Iceland most peaceful; Russia least"),
  ("Global Hunger Index (Concern Worldwide and Welthungerhilfe)", "100th of 122, 'serious' (24.1)", "Pakistan 106th; not a UN report"),
  ("Global Innovation Index (WIPO)", "38th of 139", "Switzerland first"),
  ("World Press Freedom Index (Reporters Without Borders, Paris)", "157th of 180", "Down from 151st in 2025"),
  ("Human Development Report 2025 (UNDP)", "130th of 193, HDI 0.685", "'Medium' group"),
  ("World Happiness Report", "about 116th of 147 ⟨CHECK⟩", "Released around 20 March"),
  ("Global Gender Gap (World Economic Forum)", "131st of 145 ⟨CHECK⟩", "Iceland first ⟨CHECK⟩"),
  ("Rule of Law Index (World Justice Project)", "88th of 143 ⟨CHECK⟩", "Denmark first ⟨CHECK⟩"),
  ("World Development Report 2026 (World Bank)", "—", "Theme: artificial intelligence"),
 ]),
 blocks=[],
 cards=[
  ("Report", "Who publishes the Global Hunger Index?", "Concern Worldwide and Welthungerhilfe", "Not a UN body. India 100th of 122 in 2026."),
  ("Rank", "India's rank in the Global Peace Index 2026?", "127th of 163", "Asked as a rank in ⟦2018 Q8⟧."),
 ]),

# ---------------------------------------------------------------- AWARDS
dict(id="awards", title="Awards, books and sports (light)", eyebrow="Expected 0–1 question",
 fig="medal",
 intro=[
  "The 2018 paper had eight questions on pageants, ambassadors, awards, books and sport. The 2021 paper had one (the Boltzmann Medal) and the 2025 paper had none. This family has almost disappeared, so give it the least time: one pass over the list below is enough.",
 ],
 asked=["⟦2018 Q1⟧ Miss India · ⟦2018 Q19⟧ Phalke · ⟦2018 Q21⟧ Magsaysay · ⟦2018 Q25⟧ ⟦2018 Q78⟧ books · ⟦2018 Q18⟧ ⟦2018 Q100⟧ cricket · ⟦2021 Q19⟧ Boltzmann Medal"],
 blocks=[
  ("Awards and books", [
   (1, "Indian awards", "2026", "Dadasaheb Phalke Award **for 2024**: Anant Nag (Kannada; Mohanlal got it for 2023) · 60th Jnanpith: R. Vairamuthu (Tamil); 59th: Vinod Kumar Shukla (Hindi, first from Chhattisgarh) · Padma awards 2026: 131 (5 Vibhushan, 13 Bhushan, 113 Shri); no Bharat Ratna · Ramon Magsaysay 2026: Tommy Koh, Runa Khan, Bo Kyi (no Indian).", "The 'award year' trap ⟦2018 Q19⟧."),
   (1, "World book prizes", "2026", "Booker Prize: M. John Harrison, 'The End of Everything' (oldest winner, 81; first science-fiction winner) · International Booker: 'Taiwan Travelogue' by Yáng Shuāng-zǐ (first from Mandarin). 2025: David Szalay (Flesh); Banu Mushtaq's Heart Lamp (Kannada).", ""),
  ]),
  ("Sports", [
   (1, "Cricket and football", "2026", "Men's T20 World Cup: **India** beat New Zealand by 96 runs at Ahmedabad (8 Mar), India's third T20 title and the first to defend it · FIFA World Cup (USA, Canada, Mexico; first with 48 teams): **Spain** beat Argentina 1–0 · Women's T20 World Cup: Australia.", ""),
   (1, "Multi-sport games", "2026", "Asian Games at Aichi–Nagoya, Japan: India 4th with 85 medals (21 gold), women's hockey gold after 44 years · Commonwealth Games at Glasgow: India 39 medals · next hosts: Asian Games 2030 Doha, Commonwealth Games 2030 **Ahmedabad**.", ""),
  ]),
 ],
 cards=[],
 ),
]

# What still happens before the exam
WATCH = [
 "RBI policy of 2–4 December 2026: the repo rate and the stance.",
 "The new UN Secretary-General (from 1 January 2027): learn the name and country.",
 "G20 summit at Miami (14–15 December): any declaration and the 2027 host.",
 "Gaganyaan G1: whether it flies in December or slips to 2027.",
 "Navy Day, 4 December: where the operational demonstration is held.",
 "Winter Session of Parliament: Bills passed.",
 "The next Chief Justice of India (named in January, takes over after 9 February 2027).",
 "Any new missile test off Odisha and any ship commissioned in December.",
 "Any December report with India's rank, and the ISFR if it comes out.",
 "Odisha: winter-season olive ridley forecast, new GI tags, the 19th Pravasi Bharatiya Divas at Kolkata (January).",
 "Padma awards 2027 are announced on 25 January, after the exam: skip them.",
]

SOURCES = [
 ("OPSC ASO 2018 exam date (Aglasem / Odisha TV)", "https://odishatv.in/jobs/opsc-aso-exam-2018-exam-date-postponed-know-new-date-and-more-337636"),
 ("OPSC ASO 2022 written exam on 27 August (Careers360)", "https://news.careers360.com/opsc-aso-written-exam-2022-date-held-august-27-cpse-paper-i-postponed-amid-glitch-odisha"),
 ("Tribal Queen 2018 (Deccan Chronicle)", "https://www.deccanchronicle.com/nation/current-affairs/260618/in-first-of-its-kind-event-india-crowns-tribal-queen.html"),
 ("A. R. Rahman, Sikkim (Business Standard)", "https://www.business-standard.com/amp/article/pti-stories/a-r-rahman-named-brand-ambassador-of-sikkim-118010801003_1.html"),
 ("IAF Commanders' Conference 2018 (GKToday)", "https://www.gktoday.in/the-first-biannual-indian-air-force-commanders-conference-2018-held-in-new-delhi/"),
 ("Guha's Gandhi, publication (Wikipedia)", "https://en.wikipedia.com/wiki/Gandhi:_The_Years_That_Changed_the_World"),
 ("Villages of Excellence (Deccan Herald)", "https://www.deccanherald.com/india/india-to-convert-150-villages-into-villages-of-excellence-with-technical-help-from-israel-tomar-1075643.html"),
 ("Lamheta Geo Park (ThePrint)", "https://theprint.in/india/indias-first-geo-park-to-come-up-in-mps-jabalpur-district/816782"),
 ("Boltzmann Medal 2022 (Careers360)", "https://news.careers360.com/iiser-pune-physicist-prof-dhar-chosen-for-boltzmann-medal-2022/amp"),
 ("Net Zero Vision for Bhubaneswar (TERI)", "https://teriin.org/press-release/uk-government-and-odisha-energy-department-collaborate-advance-bhubaneswars-net-zero"),
 ("ITBP base at Kutul (GKToday)", "https://www.gktoday.in/itbp-establishes-new-company-operative-base-in-chhattisgarh/"),
 ("Purple Fest 2025 (President of India)", "https://presidentofindia.gov.in/press_releases/rashtrapati-bhavan-hosts-purple-fest-0"),
 ("BIMSTEC Youth Summit 2025 (Tribune)", "https://www.tribuneindia.com/news/world/india-hosts-first-ever-bimstec-youth-summit-in-gandhinagar-focusing-on-regional-cooperation"),
 ("Sea Dragon 2025 (US Navy)", "https://www.navy.mil/Press-Office/News-Stories/Article/4124332/australia-india-japan-korea-and-the-us-complete-multinational-exercise-sea-drag"),
 ("Army renames 246 sites, Feb 2026 (ANI)", "https://aninews.in/news/national/general-news/indian-army-drops-colonial-era-names-renames-246-roads-buildings-and-facilities-nationwide20260205194207/"),
 ("COP31 ends without a deal (UN Türkiye)", "https://turkiye.un.org/en/326519-cop31-ends-without-climate-pact-un-chief-warns-there-%E2%80%98no-ambiguity-science%E2%80%99"),
 ("COP32 host (Wikipedia)", "https://en.wikipedia.org/wiki/2027_United_Nations_Climate_Change_Conference"),
 ("UN Secretary-General selection (UN)", "https://www.un.org/en/sg-selection-and-appointment"),
 ("Gaganyaan G1 delay (Tribune)", "https://www.tribuneindia.com/news/india/isro-to-launch-gaganyaans-first-uncrewed-mission-g1-with-robot-vyommitra-in-december/"),
 ("Venezuela earthquakes (Al Jazeera)", "https://www.aljazeera.com/news/2026/6/25/venezuela-rocked-by-7-5-7-2-earthquakes-what-happened-and-what-we-know"),
 ("Venezuela toll passes 6,000 (Al Jazeera)", "https://aljazeera.com/news/2026/8/3/death-toll-from-venezuela-earthquakes-passes-6000"),
 ("Maduro captured (CBS News)", "https://www.cbsnews.com/news/venezuela-military-delcy-rodriguez-acting-leader-nicolas-maduro"),
 ("France's social media ban (CNN)", "https://www.cnn.com/2026/07/21/world/france-becomes-the-first-eu-country-to-ban-social-media-for-children"),
 ("Kanlaon eruptions (Wikipedia)", "https://en.wikipedia.org/wiki/2024%E2%80%932026_Kanlaon_eruptions"),
 ("Project news bank: questions/ca-*.json, the Current Affairs 2026 manual and the Defence digest (Nov 2026)", ""),
]
