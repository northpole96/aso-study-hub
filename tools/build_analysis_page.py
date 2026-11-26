"""Builds ASO-Analysis.html: for every paper (GA, Reasoning, Maths, English, Odia) how many past questions came
from each topic and each family in every year. Data: the aso-mock skill's tagged PYQs and family maps
(Reasoning 2015 is tagged by hand in tools/build_pyq_bank.py, T15). Run: python3 tools/build_analysis_page.py"""
import sys, re, json, collections, importlib
sys.path.insert(0, '.claude/skills/aso-mock/scripts'); sys.path.insert(0, '.claude/skills/aso-mock')
import pyq
sys.path.insert(0, 'tools'); import pyq2015 as P15

# Reasoning 2015 tags (topic, family) from the PYQ bank builder
src = open('tools/build_pyq_bank.py', encoding='utf8').read()
a = src.index('T15 = {}'); b = src.index('assert sorted(T15)')
ns = {}; exec(src[a:b], ns); T15 = ns['T15']

PAPERS = [
    ('ga', 'General Awareness', 'Paper I', 100),
    ('reasoning', 'Reasoning', 'Paper II (A)', 50),
    ('maths', 'Maths', 'Paper II (B)', 50),
    ('english', 'English', 'Paper III (A)', 100),
    ('odia', 'Odia', 'Paper III (B)', 100),
]
STYLE = {'one': 'Single answer', 'stmt': 'Statements', 'match': 'Match the following', 'not': 'NOT / except', 'order': 'Put in order', 'fig': 'Figure question'}
KIND = {'static': 'Static', 'news': 'Current news', 'day': 'Days and themes', 'verbal': 'Text', 'nonverbal': 'Figure'}
# the questions themselves come from pyq-data.js (shared with the PYQ Bank); counts must agree with it
dj = open('pyq-data.js', encoding='utf8').read()
dec = json.JSONDecoder(); k = dj.index('=') + 1
_, e = dec.raw_decode(dj[k:]); k += e
BANK, _ = dec.raw_decode(dj[k + 3:])
BP = {'ga': 'ga', 'reasoning': 're', 'maths': 'ma', 'english': 'en', 'odia': 'od'}
out = []
for key, name, paper, size in PAPERS:
    rows = [dict(r) for r in pyq.load(key)]
    mp = importlib.import_module('data.map_' + key)
    if key == 'reasoning':
        for n in range(1, 51):
            t, f = T15[n]; rows.append(dict(y=2015, q=n, topic=t, family=f, style='fig' if n >= 31 else 'one', kind='nonverbal' if n >= 31 else 'verbal'))
    if key in ('ga', 'english'):   # 2015 from the Udyam books (tags in tools/pyq2015.py)
        tg = P15.GA if key == 'ga' else P15.EN
        for n in range(1, 101):
            t, f = tg[n]; rows.append(dict(y=2015, q=n, topic=t, family=t + '.' + f, style='one', kind='static'))
    years = sorted({r['y'] for r in rows})
    excl = set(getattr(mp, 'EXCLUDE', []))
    cnt = collections.defaultdict(lambda: collections.Counter())
    for r in rows: cnt[r['family']][r['y']] += 1
    fam = []
    for f, (t, tier, *rest) in mp.FAMILIES.items():
        c = cnt.get(f, {})
        fam.append(dict(f=f, t=t, tier=tier, y=[c.get(y, 0) for y in years], n=rest[0] if rest else ''))
    for f in cnt:
        if f not in mp.FAMILIES: fam.append(dict(f=f, t=f.split('.')[0], tier='?', y=[cnt[f].get(y, 0) for y in years], n=''))
    topics = []
    for t, lab in mp.LABEL.items():
        yy = [sum(1 for r in rows if r['topic'] == t and r['y'] == y) for y in years]
        topics.append(dict(id=t, name=lab, y=yy, out=t in excl))
    def dist(field, names):
        vals = collections.Counter((r[field], r['y']) for r in rows)
        ks = sorted({k for k, _ in vals})
        if len(ks) < 2: return []
        return [dict(name=names.get(k, k), y=[vals.get((k, y), 0) for y in years]) for k in ks]
    mix = []
    if dist('style', STYLE): mix.append(dict(title='Question styles', rows=sorted(dist('style', STYLE), key=lambda d: -sum(d['y']))))
    if dist('kind', KIND): mix.append(dict(title='Static, news and days' if key == 'ga' else 'Text and figure questions', rows=sorted(dist('kind', KIND), key=lambda d: -sum(d['y']))))
    sizes = [sum(1 for r in rows if r['y'] == y) for y in years]
    assert all(topics and sum(t['y'][i] for t in topics) == sizes[i] for i in range(len(years))), (key, sizes)
    assert sum(sum(f['y']) for f in fam) == len(rows), key
    bc = collections.Counter((d['y'], d['t'].split(':')[1], d['f']) for d in BANK if d['p'] == BP[key])
    mc = collections.Counter((r['y'], r['topic'], r['family'].split('.', 1)[1]) for r in rows)
    assert bc == mc, (key, list((bc - mc).items())[:5], list((mc - bc).items())[:5])
    out.append(dict(id=key, bp=BP[key], name=name, paper=paper, years=years, sizes=sizes, topics=topics, fam=fam, mix=mix, total=len(rows)))
    print(key, years, sizes, len(topics), len(fam))
tpl = open('tools/analysis_template.html', encoding='utf8').read()
html = tpl.replace('__DATA__', json.dumps(out, ensure_ascii=False, separators=(',', ':')))
open('ASO-Analysis.html', 'w', encoding='utf8').write(html)
print(len(html))
