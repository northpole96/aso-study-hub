#!/usr/bin/env python3
"""Parse the Udyam IAS Odia PYQ book (pyq/OPSC-ASO-Odia-PYQs-2018-2021-2025-Udyam.txt) into
.claude/skills/aso-mock/data/odia.py and pyq/OPSC-ASO-<year>-Odia-Paper-III.md. Tags (topic, family) are set below."""
import re,json

import os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S=os.path.join(ROOT,'pyq','OPSC-ASO-Odia-PYQs-2018-2021-2025-Udyam.txt')
s=open(S).read()
s=re.sub(r'\n=== PDF page \d+ ===\n','\n',s)
parts=re.split(r'\n?\s*(20\d\d) ASO Odia Questions[^\n]*\n[^\n]*\n',s)
# parts: [pre, y, body, y, body...]
res={}
for i in range(1,len(parts),2):
    y=int(parts[i]);body=parts[i+1]
    chunks=re.split(r'\n\s*(?=\d{1,3}\.\s*[^\s\d])',"\n"+body)
    qs={}
    for c in chunks:
        m=re.match(r'\s*(\d{1,3})\.\s*(.*)',c,re.S)
        if not m: continue
        n=int(m.group(1));t=m.group(2)
        a=re.search(r'\nAnswer\s*:\s*(.*?)(?:\n|$)',t)
        if not a: print('noans',y,n);continue
        qpart=t[:a.start()];ans=a.group(1).strip();expl=re.sub(r'\s+',' ',t[a.end():]).strip()
        o=re.split(r'\n\s*([A-D])\.\s+',"\n"+qpart)
        stem=re.sub(r'\s+',' ',o[0]).strip()
        opts={o[k]:re.sub(r'\s+',' ',o[k+1]).strip() for k in range(1,len(o)-1,2)}
        qs[n]=dict(y=y,q=n,stem=stem,opts=opts,ans=ans,expl=expl)
    res[y]=qs

d={str(y):{n:q for n,q in qs.items()} for y,qs in res.items()}
R=lambda a,b:list(range(a,b+1))
# build clean:
F={}
def add(f,y,qs): F.setdefault(f,{}).setdefault(y,[]).extend(qs)
# ---- subject-verb relation
add("skr.person-number",2018,[1,4,6,10,17]); add("skr.person-number",2021,[31,42,50,63])
add("skr.gender",2018,[2,9]); add("skr.gender",2021,[39])
add("skr.subject-predicate",2018,[3,5,7]); add("skr.subject-predicate",2021,[69])
add("skr.anwaya",2021,[66,75]); add("skr.anwaya",2025,[69])
add("skr.sentence-pattern",2018,[8]); add("skr.sentence-pattern",2021,[37])
# ---- verb
add("kri.finite-nonfinite",2018,[20,39,45,52]); add("kri.finite-nonfinite",2021,[49,67,85]); add("kri.finite-nonfinite",2025,[46,49])
add("kri.reduplication",2018,[23,35,36,37,64])
add("kri.kinds",2018,[13,25,31,32,34,40,41,42,55,66,67]); add("kri.kinds",2021,[38,46,79]); add("kri.kinds",2025,[31,33,42,43,59,64,66])
add("kri.transitive",2018,[33,48]); add("kri.transitive",2021,[61,78,98,99]); add("kri.transitive",2025,[54])
add("kri.causative",2018,[30,58,63]); add("kri.causative",2021,[33]); add("kri.causative",2025,[51,65])
add("kri.namadhatu",2018,[50,54]); add("kri.namadhatu",2021,[77,91,95]); add("kri.namadhatu",2025,[47,48,67])
add("kri.dhatu-origin",2018,[38]); add("kri.dhatu-origin",2021,[43,45,56,94]); add("kri.dhatu-origin",2025,[36,37,38,39,57,63,70])
add("kri.negative",2018,[29,47,49,62,65]); add("kri.negative",2025,[52,61])
add("kri.vibhakti",2018,[19,24,27,44]); add("kri.vibhakti",2021,[71,73,82]); add("kri.vibhakti",2025,[40,41,50,58])
# ---- tense
add("kal.form-identify",2018,[14,15,16,22,53,57]); add("kal.form-identify",2021,[36,68]); add("kal.form-identify",2025,[44])
add("kal.suffix",2018,[12,43,46,51,56]); add("kal.suffix",2021,[81]); add("kal.suffix",2025,[32,35,45,55])
add("kal.basics",2018,[11,28]); add("kal.basics",2025,[34])
# ---- adverb
add("adv.identify",2018,[18,21,26]); add("adv.identify",2021,[34,54]); add("adv.identify",2025,[53,62,68])
# ---- spelling
add("err.spelling",2018,[61,68]+R(71,80)); add("err.spelling",2021,R(1,10)+[93]); add("err.spelling",2025,R(1,10))
# ---- synonyms and antonyms by theme
# syn.sky-weather: sky, cloud, wind, moon, sun, hail ; syn.land-water: lake, river, forest, mountain, earth, road, boat, house, lotus
# syn.creatures: snake, crow, elephant, bird, cow ; syn.gods-people: Ganesha, Shiva, daughter, student, demon
SYN={2018:{59:'sky',70:'land',81:'sky',82:'god',83:'god',84:'land',85:'god',86:'land',87:'cre',88:'sky',89:'cre',90:'sky'},
 2021:{11:'sky',12:'sky',13:'land',14:'god',15:'cre',16:'cre',17:'land',18:'land',19:'cre',20:'land'},
 2025:{21:'sky',22:'cre',23:'god',24:'land',25:'god',26:'god',27:'sky',28:'sky',29:'land',30:'land'}}
name={'sky':'syn.sky-weather','land':'syn.land-water','cre':'syn.creatures','god':'syn.gods-people'}
for y,m in SYN.items():
    for q,k in m.items(): add(name[k],y,[q])
ANT={2018:{60:'dc',69:'dsi',91:'sk',92:'sk',93:'sk',94:'sk',95:'pre',96:'pre',97:'dsi',98:'sk',99:'dsi',100:'dsi'},
 2021:{21:'sk',22:'sk',23:'sk',24:'sk',25:'sk',26:'sk',27:'sk',28:'dsi',29:'sk',30:'sk',100:'dsi'},
 2025:{11:'sk',12:'sk',13:'dsi',14:'sk',15:'dsi',16:'sk',17:'sk',18:'pre',19:'pre',20:'sk'}}
an={'dc':'ant.prefix','sk':'ant.sanskrit-pair','pre':'ant.prefix','dsi':'ant.desi-pair'}
for y,m in ANT.items():
    for q,k in m.items(): add(an[k],y,[q])
# ---- sentence work
add("rea.transform",2025,R(71,79)); add("rea.sentence-kind",2021,[76,90,96]); add("rea.sentence-kind",2025,[81,82,85,86,90])
add("rea.narration",2025,[80,83,88,89]); add("rea.voice",2025,[84,87])
add("com.passage-detail",2025,[91,92,93,95,96,97,99,100]); add("com.passage-inference",2025,[94,98])
# ---- outside the printed syllabus
add("oth.karaka",2021,[32,35,44,65,70]); add("oth.karaka",2025,[56,60])
add("oth.pronoun",2021,[41,55,60,62])
add("oth.noun-adjective",2021,[40,47,51,72,86,87,88])
add("oth.word-formation",2021,[48,52,57,58,59,80,89,97])
add("oth.avyaya",2021,[53,64,74,92])
add("oth.morpheme",2021,[83,84])
rows={}
for f,ys in F.items():
    for y,qs in ys.items():
        for q in qs:
            assert (y,q) not in rows,(y,q,f,rows[(y,q)])
            rows[(y,q)]=f
miss=[(y,q) for y in (2018,2021,2025) for q in range(1,101) if (y,q) not in rows]
assert not miss,miss

# ---------------------------------------------------------------- clean text, write outputs
FAMILY = rows                       # {(year, q): family}
MARK = re.compile(r' (?=[\u0B01-\u0B03\u0B3E-\u0B4D\u0B56\u0B57])')   # the PDF text puts a space before a stray vowel sign
def clean(v, page=False):
    v = MARK.sub('', v)
    if page:
        v = re.sub(r'\s\d{1,2}$', '', v)     # page number glued on at a page break
    return v.strip()

NV = {2018: [5, 62], 2021: [13, 83, 84], 2025: [33, 34, 38]}      # "Not valued" in OPSC's key
# CHECK reasons. First 9 = the book itself says so; the other 11 were added on 24 Nov 2026 after reading all 300 keys against
# standard Odia grammar and vocabulary (no official OPSC key could be fetched: opsc.gov.in serves its PDFs through postbacks).
CHECK_WHY = {
    (2018, 74): "book: the scan does not show if the doubled ଜ is printed; ନିର୍ଧନ (D) is also a real word",
    (2018, 75): "book: the scan is unclear",
    (2021, 2): "book: the scan is unclear",
    (2021, 4): "book: the scan is unclear",
    (2021, 27): "printed as ପ୍ରତିଶବ୍ଦ (synonym) but the key ଜଙ୍ଗମ is the antonym of ସ୍ଥାବର; B ଅଚଳ is the true synonym",
    (2021, 43): "book: the scan is unclear",
    (2025, 2): "book: the scan is unclear",
    (2025, 9): "OPSC accepted two answers, B ମଧୁଳିକା and D ମଧୁଲିକା; stored as B",
    (2025, 23): "book: the scan is unclear",
    (2018, 78): "reviewer: B ଅଧୀନସ୍ଥ is also a correct word, the key is D ଅଧୀନ",
    (2018, 87): "reviewer: key ପରଭୃତ means the koel (cuckoo), not the crow (କାଉ); no option is a crow word, so the stem may be misprinted (କୋଇଲି?)",
    (2018, 95): "reviewer: the real opposite of ଆବୃତ (covered) is ଅନାବୃତ (B); the key follows the printed ଆବୃତ୍ତ and picks ଅନାବୃତ୍ତ",
    (2021, 7): "reviewer: both ସାର୍ବଜନୀନ (key) and ସର୍ବଜନୀନ (B) are used",
    (2021, 79): "reviewer: the question asks for the compound verb but the key picks only the verb part କରୁଥିଲେ of the mixed verb ଆହାର କରୁଥିଲେ",
    (2021, 90): "reviewer: a rhetorical question ('who else could hit such a six?'); the key says exclamatory (D), arguably it is a question or a negative statement",
    (2025, 16): "reviewer: B ଅଶିଷ୍ଟ is also a fair opposite of ଶିଷ୍ଟ; key is ଦୁଷ୍ଟ",
    (2025, 71): "reviewer: options A and B are both complex sentences; A is the closer one",
    (2025, 79): "reviewer: the key B (ଶୁଣିଲେ ହେଁ) changes 'and' into 'although'; no option is a clean simple sentence",
    (2025, 82): "reviewer: key C is a statement of need rather than a command",
    (2025, 86): "reviewer: a rhetorical question ('who in Odisha does not know Madhubabu?') keyed as exclamatory, like 2021 Q90",
}
CHECK = set(CHECK_WHY)

raw = re.sub(r'\n=== PDF page \d+ ===\n', '\n', open(S).read()).split('2025 ASO Odia Questions')[1]
PASS = {}
for a, b in ((91, 95), (96, 100)):
    m = re.search(r'ଅନୁଚ୍ଛେଦ - ପ୍ରଶ୍ନ %d-%d\s*\n(.*?)\n\s*%d\.' % (a, b, a), raw, re.S)
    t = re.sub(r'Printed passage:.*', '', m.group(1), flags=re.S)         # the publisher's own note
    ls = [l.strip() for l in t.split('\n') if l.strip()]
    PASS[(a, b)] = clean(re.sub(r'\s+', ' ', ' '.join(ls[3:])))              # first 3 lines = the instruction

ROWS = []
for y in (2018, 2021, 2025):
    for q in range(1, 101):
        x = res[y][q]
        a = x['ans'][:1] if x['ans'][:1] in 'ABCD' and x['ans'][1:2] in (' ', '') else '?'
        opts = [clean(x['opts'][k], page=(k == 'D')) for k in 'ABCD']
        ROWS.append((y, q, FAMILY[(y, q)].split('.')[0], FAMILY[(y, q)], 'one', 'static', a, (y, q) in CHECK,
                     clean(x['stem']), opts))

def write_data():
    out = ['# Paper III (B) Odia (ଓଡ଼ିଆ), 2018, 2021 and 2025 (100 questions each).',
           '# Source: the Udyam IAS book "OPSC ASO Previous Year Questions & Solutions: Odia" (300 questions), read 24 Nov 2026.',
           '# Full text with the publisher\'s keys and notes: pyq/OPSC-ASO-<year>-Odia-Paper-III.md (git-ignored).',
           '# No OPSC key is in the folder: "ans" is the book\'s key; "?" = OPSC marked the question Not valued (listed in NV).',
           '# Rows: (year, q, topic, family, style, kind, ans, check, stem, [A, B, C, D]). Built by tools/build_odia_data.py.',
           '# 2025 Q91-95 and Q96-100 are passage questions: the passage text is in PASSAGES.',
           'NV = %r' % NV,
           'CHECK_WHY = {',
           ]
    for k, v in CHECK_WHY.items():
        out.append('    %r: %r,' % (k, v))
    out.append('}')
    out.append('PASSAGES = {')
    for (a, b), t in PASS.items():
        out.append('    (%d, %d): %r,' % (a, b, t))
    out += ['}', 'ROWS = [']
    for r in ROWS:
        out.append('    %r,' % (r,))
    out.append(']')
    p = os.path.join(ROOT, '.claude', 'skills', 'aso-mock', 'data', 'odia.py')
    open(p, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    print('wrote', p)

TITLE = {2018: '2018-19 recruitment, Series B, exam 20 January 2019',
         2021: '2021-22 recruitment, Series A, exam 27 August 2022',
         2025: 'Office of the Advocate General, Series A, exam 9 November 2025'}
def write_md():
    for y in (2018, 2021, 2025):
        o = ['# OPSC ASO %d: Paper III (B) Odia, 100 questions' % y, '',
             '**Source:** Udyam IAS, "OPSC ASO Previous Year Questions & Solutions: Odia" (%s).' % TITLE[y],
             'Text taken from the book\'s PDF text layer on 24 Nov 2026; stray spaces before vowel signs were removed and page numbers stripped. '
             'The key and the notes are the **publisher\'s**, not OPSC\'s. **Not valued** = the book says OPSC dropped the question. '
             '**CHECK** = the book itself is unsure of the scan, or the printed stem and the key disagree. Local file only (the notes are the publisher\'s).', '']
        for q in range(1, 101):
            x = res[y][q]; r = [r for r in ROWS if r[0] == y and r[1] == q][0]
            for (a, b), t in PASS.items():
                if y == 2025 and q == a:
                    o += ['---', '', '**Passage for Q%d-%d**' % (a, b), '', t, '', '---', '']
            tag = ' (%s)' % FAMILY[(y, q)]
            o.append('**%d.** %s%s' % (q, r[8], tag))
            o.append('')
            for k, v in zip('ABCD', r[9]):
                o.append('(%s) %s  ' % (k, v))
            o.append('')
            ans = clean(x['ans'], page=True)
            o.append('**Answer:** %s%s' % (ans, '  **[CHECK: %s]**' % CHECK_WHY[(y, q)] if (y, q) in CHECK else '') + ('  **[NOT VALUED]**' if q in NV[y] else ''))
            o.append('')
            o.append('> ' + clean(x['expl'], page=True))
            o.append('')
        p = os.path.join(ROOT, 'pyq', 'OPSC-ASO-%d-Odia-Paper-III.md' % y)
        open(p, 'w', encoding='utf-8').write('\n'.join(o))
        print('wrote', p)

if __name__ == '__main__':
    write_data(); write_md()
