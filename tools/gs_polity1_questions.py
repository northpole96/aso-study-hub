# GS Polity Mock 01: 10 questions on syllabus topic (d) Constitution, made with the aso-mock skill (23 Nov 2026).
# Plan: python3 .claude/skills/aso-mock/scripts/draw.py ga --topics pol --n 10 --seed 382599
# First option is right unless a is given.

S12 = ["Only 1", "Only 2", "Both 1 and 2", "Neither 1 nor 2"]
S3 = ["Only 1 and 2", "Only 2 and 3", "Only 1 and 3", "1, 2 and 3"]
def M(a, b, c, d):
    return "a-%d, b-%d, c-%d, d-%d" % (a, b, c, d)

META = dict(
    paper="ga",
    title="ASO GS Polity Mock 01",
    hub_title="Polity 10 · GS Mock 01",
    link_title="Polity 10 mock",
    masthead="GS Polity 01",
    heading="General Studies Paper I · Polity Mock 01",
    tagline="10 questions on<br><b>the Constitution</b><br>drawn by probability.",
    key="aso-gs-polity-1",
    code="POL3",
    out="ASO-GS-Mock-Polity-1.html",
    minutes=9,
    seed=382599,
    order="mixed",
    topic="pol",
    date="23 Nov 2026",
    draw="python3 .claude/skills/aso-mock/scripts/draw.py ga --topics pol --n 10 --seed 382599",
    intro=[
        "This is a short mock on syllabus topic (d), the Indian Constitution. The ten questions were drawn by probability from the polity families of the 2018, 2021 and 2025 papers: the commission, the Preamble, elections, the Directive Principles, two amendments, the Governor, the Prime Minister and Council of Ministers, the Finance Commission and the All India Services.",
        "Every question is the next angle of a family the examiner has already used, not a repeat. There are no news questions and no CHECK tags. Read each explanation: it names the question it grew from and the facts of the family that are likely to come next.",
    ],
)

Q = []
def add(s, q, o, e, k="one", n=False, c=False, a=None, **x):
    d = dict(s=s, q=q, o=o, e=e, k=k, n=n, c=c, a=a); d.update(x); Q.append(d)

# 1 nhrc
add("Polity", "As amended in 2019, what is the term of office of the Chairperson of the National Human Rights Commission?",
    ["Three years or until the age of 70, whichever is earlier",
     "Five years or until the age of 65, whichever is earlier",
     "Five years or until the age of 70, whichever is earlier",
     "Six years or until the age of 65, whichever is earlier"],
    "Why: the Protection of Human Rights (Amendment) Act, 2019 cut the term from five years to three years (or age 70, whichever comes first), and a member can be appointed again. The older five-year term is the trap. "
    "Grew from: the NHRC has come in all three papers (eligibility 2018 Q65, first chairperson 2021 Q51, selection committee 2025 Q87). "
    "Family: the Act is the Protection of Human Rights Act, 1993; the first chairperson was Justice Ranganath Misra; the President appoints the chairperson; removal is only on proved misbehaviour or incapacity after an inquiry by the Supreme Court; State Human Rights Commissions are appointed by the Governor.")

# 2 preamble
add("Polity", "Who described the Preamble of the Indian Constitution as its 'political horoscope'?",
    ["K. M. Munshi", "Ernest Barker", "N. A. Palkhivala", "B. R. Ambedkar"],
    "Why: K. M. Munshi, a member of the Drafting Committee, called the Preamble the political horoscope of the Constitution. Barker called it the keynote, and Palkhivala called it the identity card. Ambedkar did not describe it so. "
    "Grew from: 2025 Q35 asked who called it the keynote (Ernest Barker), and 2025 Q32 asked which amendment inserted 'Secular'. "
    "Family: the 42nd Amendment (1976) added Socialist, Secular and Integrity; Nehru moved the Objectives Resolution on 13 December 1946; the Preamble is part of the basic structure (Kesavananda Bharati, 1973) after the Berubari case (1960) had held it was not part of the Constitution.")

# 3 elections (match)
add("Polity", "Match List I with List II:\nList I (body or office)\na. Lok Sabha\nb. Rajya Sabha\nc. President of India\nd. Vice-President of India\nList II (who elects it)\n1. Elected members of both Houses of Parliament and of the State Legislative Assemblies\n2. All members of both Houses of Parliament, elected and nominated\n3. Elected members of the State Legislative Assemblies, by single transferable vote\n4. Voters directly, by the first-past-the-post method",
    [M(4, 3, 2, 1), M(4, 3, 1, 2), M(3, 4, 1, 2), M(4, 1, 3, 2)],
    "Why: the Lok Sabha is the only House chosen directly (4). Rajya Sabha members are elected by the elected members of each State Assembly through the single transferable vote (3). The President is chosen by an electoral college of the elected members of Parliament and of the State Assemblies (1). The Vice-President is chosen by all members of both Houses, nominated ones too (2). The two code swaps (c with d, and a with b) are the traps. "
    "Grew from: 2025 Q83 asked the method for the Lok Sabha (first-past-the-post). "
    "Family: both President and Vice-President elections use proportional representation by the single transferable vote with a secret ballot; the Delhi and Puducherry Assemblies are in the President's college; the voting age was lowered to 18 by the 61st Amendment (1988); NOTA came after a 2013 Supreme Court order.",
    k="match", a=1)

# 4 dpsp (stmt)
add("Polity", "Consider the following statements:\n1. Article 40 directs the State to organise village panchayats.\n2. Article 44 directs the State to secure a Uniform Civil Code for the citizens.\n3. Article 45 directs the State to provide free and compulsory education to all children between six and fourteen years of age.\nWhich of the statements given above is/are correct?",
    S3,
    "Statement 3 is wrong. Free and compulsory education for children of six to fourteen years is a Fundamental Right under Article 21A (86th Amendment, 2002). After that amendment Article 45 was changed to direct early childhood care and education for children below six years. Statements 1 and 2 are right. "
    "Grew from: 2025 Q78 asked the Article on foreign policy (51) and 2025 Q98 asked a principle added by amendment. "
    "Family: 39A free legal aid and equal justice (42nd Amendment), 43A workers in management, 48 cow and animal husbandry, 48A environment and wildlife, 50 separation of the judiciary from the executive. Directive Principles are not enforceable in court (Article 37).",
    k="stmt", a=0)

# 5 amendments
add("Polity", "The 73rd Constitution Amendment Act (1992) gave constitutional status to which of the following?",
    ["Panchayati Raj institutions", "Municipalities", "Co-operative societies", "The Goods and Services Tax Council"],
    "Why: the 73rd Amendment added Part IX and the Eleventh Schedule for Panchayati Raj. The 74th Amendment did the same for Municipalities (Part IXA, Twelfth Schedule), the 97th for co-operative societies (2011) and the 101st for the GST Council (Article 279A). The trap is mixing 73 and 74. "
    "Grew from: amendments are asked in every paper (2018 Q75 Delhi as a capital territory, 2021 Q37 the 99th, 2021 Q39 the 44th, 2025 Q91 the 91st). "
    "Family: the 73rd and 74th came into force in 1993; Panchayat elections every five years; a State Election Commission and a State Finance Commission for local bodies; Article 243 onwards.")

# 6 amendments (voting age)
add("Polity", "Which Constitution Amendment Act lowered the voting age from 21 years to 18 years?",
    ["61st", "42nd", "44th", "52nd"],
    "Why: the 61st Amendment (1988, in force 1989) changed Article 326, so every citizen of 18 or more can vote. The 42nd added Socialist and Secular and is called the Mini-Constitution; the 44th removed the right to property from the Fundamental Rights; the 52nd added the anti-defection law and the Tenth Schedule. "
    "Grew from: 2021 Q39 asked what the 44th repealed (Articles 19(1)(f) and 31), which makes the neighbouring amendments a likely next. "
    "Family: 86th (2002) Article 21A; 91st (2003) Council of Ministers up to 15% of the Lok Sabha; 101st (2016) GST; 103rd (2019) 10% reservation for economically weaker sections; 104th (2020) ended seats reserved for Anglo-Indians; 106th (2023) one-third seats for women.")

# 7 governor (not)
add("Polity", "Which one of the following statements about the Governor of a State is NOT correct?",
    ["He is elected by the members of the State Legislative Assembly",
     "He must have completed the age of 35 years",
     "He can promulgate an ordinance under Article 213 when the Legislature is not in session",
     "The same person can be appointed Governor of two or more States"],
    "Why: the Governor is appointed by the President (Article 155), not elected. The other three are true: 35 years is the minimum age (Article 157), Article 213 gives the ordinance power, and the 7th Amendment (1956) allows one person to be Governor of more than one State. "
    "Grew from: 2025 Q89 asked which commission recommended that the Governor be appointed after consulting the Chief Minister (Sarkaria). "
    "Family: Governor holds office at the pleasure of the President for a normal term of five years; Articles 153 to 162; the Punchhi Commission (2010) is the next commission after Sarkaria (1983); the Governor's discretionary powers include reserving a Bill for the President (Article 200).",
    k="not")

# 8 pm and council of ministers (stmt)
add("Polity", "Consider the following statements:\n1. The Council of Ministers is collectively responsible to the Rajya Sabha.\n2. The Prime Minister is appointed by the President.\n3. Article 74 provides for a Council of Ministers with the Prime Minister at the head to aid and advise the President.\nWhich of the statements given above is/are correct?",
    S3,
    "Statement 1 is wrong: the Council of Ministers is collectively responsible to the Lok Sabha (Article 75(3)), and a no-confidence vote in the Lok Sabha makes the whole Council resign. Statements 2 (Article 75) and 3 (Article 74) are right. "
    "Grew from: 2025 Q18 asked three statements on the Prime Minister and the Council, and 2025 Q91 asked the size limit (15%, from the 91st Amendment). "
    "Family: a person who is not a member of Parliament can be a minister for at most six months; the Prime Minister was called the 'keystone of the cabinet arch' by Lord Morley; the Cabinet is the smaller group inside the Council of Ministers.",
    k="stmt", a=1)

# 9 finance commission
add("Polity", "The Finance Commission of India is constituted by the President under which Article?",
    ["Article 280", "Article 270", "Article 275", "Article 266"],
    "Why: Article 280 provides for the Finance Commission, which the President sets up every five years or earlier. It has a chairman and four other members, and its advice is not binding. The others are near-misses: Article 270 is the sharing of taxes, Article 275 is grants-in-aid to States and Article 266 is the Consolidated Fund. "
    "Grew from: 2021 Q43 asked how many members the Finance Commission has (five, including the chairman). "
    "Family: the first commission was in 1951 under K. C. Neogy; the 16th Finance Commission is headed by Arvind Panagariya (report for 2026 to 2031); it advises on the share of States in central taxes and on grants.")

# 10 all india services (match)
add("Polity", "Match List I with List II:\nList I\na. Article 312\nb. Article 311\nc. Indian Forest Service\nd. Father of the All India Services\nList II\n1. Created in 1966\n2. Sardar Vallabhbhai Patel\n3. Protection of civil servants against dismissal without inquiry\n4. A new All India Service can be created by a Rajya Sabha resolution",
    [M(3, 4, 1, 2), M(4, 3, 2, 1), M(4, 3, 1, 2), M(1, 2, 3, 4)],
    "Why: Article 312 lets Parliament create a new All India Service if the Rajya Sabha passes a resolution by a two-thirds majority of members present and voting (4). Article 311 protects civil servants from being dismissed or reduced in rank without an inquiry (3). The Indian Forest Service was created in 1966 (1). Sardar Patel is called the father of the All India Services (2). "
    "Grew from: 2021 Q45 asked how a new All India Service is created. "
    "Family: the three All India Services are the IAS, the IPS and the Indian Forest Service; they are common to the Union and the States; the All India Services Act is of 1951; the Union Public Service Commission recruits for them (Article 315).",
    k="match", a=2)
