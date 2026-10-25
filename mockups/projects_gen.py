"""Generates the HTML for 7 project-card mock images (fake data, fixed seed).
Run via mockups/render.sh. Each w(name, css, body) call writes name.html in the cwd,
sized 1600x740 (the size every card image uses)."""
import random, re
random.seed(7)

BASE = """<!doctype html><html><head><meta charset=utf-8><style>
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1600px;height:740px;overflow:hidden;font-family:-apple-system,'Helvetica Neue',Arial,sans-serif}
%s
</style></head><body>%s</body></html>"""


def w(name, css, body):
    # unquoted SVG attrs like y2=670/> break the parser; add a space before />
    body = re.sub(r'(=[^\s"\'>]+)/>', r'\1 />', body)
    open(name + '.html', 'w').write(BASE % (css, body))


# ---------------- Equipment Utilization Tracker ----------------
locs = [("Phoenix, AZ", 87), ("Dallas, TX", 81), ("Denver, CO", 74), ("Atlanta, GA", 69),
        ("Reno, NV", 63), ("Tampa, FL", 58), ("Omaha, NE", 46), ("Boise, ID", 39)]
rows = ""
for l, u in locs:
    c = "#2e9e5b" if u >= 75 else "#e0a416" if u >= 55 else "#d64545"
    rows += (f"<tr><td>{l}</td><td>{random.randint(18, 64)}</td><td>{random.randint(9, 48)}</td>"
             f"<td><div class=bar><i style='width:{u}%;background:{c}'></i></div></td><td><b>{u}%</b></td></tr>")
css = """body{background:#f3f5f8;color:#1f2933}
.nav{height:56px;background:#1f2a37;color:#fff;display:flex;align-items:center;padding:0 32px;gap:36px;font-size:17px}
.nav b{font-size:20px}.nav span{opacity:.7}.nav .on{opacity:1;border-bottom:3px solid #4da3ff;padding:17px 0}
.wrap{display:flex;gap:28px;padding:28px 32px}
.card{background:#fff;border:1px solid #dde3ea;border-radius:8px;padding:22px}
.left{width:470px}.right{flex:1}
h2{font-size:19px;margin-bottom:14px}
.drop{border:2px dashed #9db4cc;border-radius:8px;height:150px;display:flex;flex-direction:column;align-items:center;justify-content:center;color:#52667a;background:#f8fbff;font-size:16px;gap:6px}
.drop b{font-size:34px;color:#4da3ff}
.file{display:flex;justify-content:space-between;padding:10px 14px;background:#eef6ee;border:1px solid #b8dcc0;border-radius:6px;margin-top:14px;font-size:15px}
.btn{display:inline-block;background:#2f7de1;color:#fff;padding:11px 22px;border-radius:6px;font-size:15px;margin-top:16px;font-weight:600}
.steps{margin-top:18px;font-size:14px;color:#52667a;line-height:2}.steps i{color:#2e9e5b;font-style:normal;font-weight:700}
table{width:100%;border-collapse:collapse;font-size:15px}th{text-align:left;color:#52667a;font-size:12px;text-transform:uppercase;letter-spacing:.06em;padding:8px 10px;border-bottom:2px solid #dde3ea}
td{padding:11px 10px;border-bottom:1px solid #eef1f5}.bar{height:12px;background:#e6ebf1;border-radius:6px;width:210px}.bar i{display:block;height:100%;border-radius:6px}
.top{display:flex;justify-content:space-between;align-items:center}.pill{background:#e7f1ff;color:#2f7de1;padding:5px 12px;border-radius:14px;font-size:13px;font-weight:600}"""
body = f"""<div class=nav><b>UtilTracker</b><span class=on style='color:#fff'>Upload</span><span>Locations</span><span>Machines</span><span>Monthly Summary</span><span>Docs</span></div>
<div class=wrap><div class='card left'><h2>1 &nbsp;Upload raw rental data</h2><div class=drop><b>&#8679;</b>Drop .csv / .xlsx here or click to browse</div>
<div class=file><span>rental_export_2026-09.xlsx</span><span>2.4 MB &nbsp;&#10003;</span></div>
<div class=steps><i>&#10003;</i> File parsed &mdash; 14,882 rows<br><i>&#10003;</i> Location names matched (41 / 43)<br><i>&#10003;</i> Machine IDs matched (1,206 / 1,219)<br><span style='color:#c27c0e'>&#9888;</span> 15 rows need review</div><span class=btn>Clean &amp; load to database</span></div>
<div class='card right'><div class=top><h2>Monthly utilization by location &middot; Sep 2026</h2><span class=pill>Month-to-date</span></div>
<table><tr><th>Location</th><th>Machines</th><th>On rent</th><th>Utilization</th><th></th></tr>{rows}</table></div></div>
<div style='padding:0 32px'><div class=card><h2>Recent uploads</h2><table><tr><th>File</th><th>Uploaded by</th><th>Rows</th><th>Status</th></tr><tr><td>rental_export_2026-08.xlsx</td><td>ops_user</td><td>14,310</td><td style='color:#2e9e5b;font-weight:700'>Loaded</td></tr><tr><td>rental_export_2026-07.xlsx</td><td>ops_user</td><td>13,954</td><td style='color:#2e9e5b;font-weight:700'>Loaded</td></tr></table></div></div>"""
w("rental-utilization", css, body)

# ---------------- Executive Dashboards Suite (Tableau-ish) ----------------
cur = [62, 71, 68, 80, 77, 91, 86, 95, 88, 102, 97, 110]
prv = [55, 60, 66, 70, 72, 78, 80, 82, 85, 88, 90, 93]


def line(v, c, dash=""):
    pts = " ".join(f"{40 + i * 52},{230 - x * 1.7}" for i, x in enumerate(v))
    return f"<polyline fill=none stroke='{c}' stroke-width=3 {dash} points='{pts}'/>"


regions = [("West", 112), ("Southwest", 98), ("Central", 91), ("Southeast", 84), ("Northeast", 67), ("Mountain", 59)]
rb = "".join(f"<div class=rr><span>{n}</span><div class=rbar><i style='width:{v / 112 * 100}%'></i></div><b>{v}</b></div>" for n, v in regions)
css = """body{background:#fff;color:#333;font-family:'Helvetica Neue',Arial,sans-serif}
.hd{height:64px;border-bottom:1px solid #d9d9d9;display:flex;align-items:center;padding:0 28px;gap:16px}
.hd h1{font-size:23px;font-weight:600;color:#1e3a5f}.hd small{color:#777;font-size:14px}
.crumb{margin-left:auto;font-size:14px;color:#1e6fb8}
.main{display:flex;height:676px}.side{width:250px;border-right:1px solid #e0e0e0;background:#fafafa;padding:20px;font-size:14px}
.side h4{font-size:12px;text-transform:uppercase;color:#888;margin:0 0 8px;letter-spacing:.06em}
.chk{padding:6px 0;color:#444}.chk:before{content:'\\2611  ';color:#1e6fb8}.sel{background:#e8f1fa;border:1px solid #b6d3ee;padding:8px 10px;margin-bottom:18px;border-radius:2px}
.cont{flex:1;padding:20px 26px}
.kpis{display:flex;gap:16px;margin-bottom:18px}.k{flex:1;border:1px solid #dcdcdc;padding:14px 18px}.k small{color:#777;font-size:13px}.k b{display:block;font-size:34px;color:#1e3a5f;margin-top:4px}.k i{font-style:normal;font-size:13px}
.up{color:#2a8a4a}.dn{color:#c0392b}
.row{display:flex;gap:18px}.pnl{border:1px solid #dcdcdc;padding:14px 16px}.pnl h3{font-size:15px;font-weight:600;color:#444;margin-bottom:8px}
.rr{display:flex;align-items:center;gap:10px;font-size:14px;margin:11px 0}.rr span{width:92px}.rbar{flex:1;height:18px;background:#eef2f6}.rbar i{display:block;height:100%;background:#4e79a7}.rr b{width:34px;text-align:right}"""
svg = f"""<svg width=640 height=250><g stroke='#eee'>{''.join(f"<line x1=30 x2=640 y1={y} y2={y}/>" for y in (60, 110, 160, 210))}</g>
{line(prv, '#b0b7c0', 'stroke-dasharray=6,5')}{line(cur, '#e15759')}
<g font-size=12 fill='#888'>{''.join(f"<text x={36 + i * 52} y=242>{m}</text>" for i, m in enumerate('JFMAMJJASOND'))}</g></svg>"""
body = f"""<div class=hd><h1>Regional Performance Overview</h1><small>FY2026 &middot; Updated daily 6:00 AM</small><span class=crumb>All Regions &rsaquo; West &rsaquo; Phoenix District</span></div>
<div class=main><div class=side><h4>Fiscal year</h4><div class=sel>FY2026</div><h4>Date range</h4><div class=sel>Jan 1 &ndash; Sep 30 &middot; MTD</div><h4>Product group</h4><div class=chk>Group A</div><div class=chk>Group B</div><div class=chk>Group C</div><div class=chk>Group D</div><h4 style='margin-top:18px'>Compare to</h4><div class=sel>Budget &amp; Prior Year</div></div>
<div class=cont><div class=kpis><div class=k><small>Revenue</small><b>$48.2M</b><i class=up>&#9650; 8.4% vs PY</i></div><div class=k><small>vs Budget</small><b>102.6%</b><i class=up>&#9650; $1.2M</i></div><div class=k><small>Revenue / Unit</small><b>$3,410</b><i class=dn>&#9660; 1.9% vs PY</i></div><div class=k><small>Units</small><b>14.1K</b><i class=up>&#9650; 10.5% vs PY</i></div></div>
<div class=row><div class=pnl style='width:700px'><h3>Monthly revenue &mdash; current vs prior year ($M)</h3>{svg}</div>
<div class=pnl style='flex:1'><h3>Revenue by region ($M) &mdash; click to drill down</h3>{rb}</div></div>
<div class=pnl style='margin-top:18px'><h3>Top districts &mdash; West region</h3><table style='width:100%;border-collapse:collapse;font-size:14px'><tr style='color:#888;text-align:left'><th>District</th><th>Revenue</th><th>vs Budget</th><th>vs PY</th><th>Rev / Unit</th></tr><tr><td>Phoenix</td><td>$12.4M</td><td class=up>+4.1%</td><td class=up>+9.2%</td><td>$3,520</td></tr><tr><td>Las Vegas</td><td>$9.8M</td><td class=up>+1.7%</td><td class=up>+6.0%</td><td>$3,390</td></tr><tr><td>San Diego</td><td>$8.1M</td><td class=dn>-2.2%</td><td class=up>+3.4%</td><td>$3,305</td></tr></table></div></div></div>"""
w("exec-dashboard", css, body)

# ---------------- Multi-Site Production Monitoring (dark kiosk) ----------------
sites = [("Plant 01", "RUNNING", "#2ecc71", 94), ("Plant 02", "RUNNING", "#2ecc71", 88), ("Plant 03", "DOWN", "#e74c3c", 0),
         ("Plant 04", "RUNNING", "#2ecc71", 91), ("Plant 05", "IDLE", "#f1c40f", 12), ("Plant 06", "RUNNING", "#2ecc71", 79)]
tiles = "".join(f"<div class=t style='border-top:5px solid {c}'><small>{n}</small><b style='color:{c}'>{s}</b><div class=meter><i style='width:{u}%;background:{c}'></i></div><span>{u}% of target</span></div>" for n, s, c, u in sites)
css = """body{background:#0f1419;color:#e6edf3}
.hd{height:70px;background:#161d26;border-bottom:1px solid #263241;display:flex;align-items:center;padding:0 30px;gap:24px}
.hd h1{font-size:24px;letter-spacing:.04em}.clock{margin-left:auto;font-size:26px;font-family:Menlo,monospace;color:#7ee0a0}
.g{display:grid;grid-template-columns:repeat(6,1fr);gap:16px;padding:22px 30px}
.t{background:#18212b;padding:16px;border-radius:4px}.t small{color:#8b9db0;font-size:14px}.t b{display:block;font-size:26px;margin:6px 0 12px}.meter{height:10px;background:#263241}.meter i{display:block;height:100%}.t span{font-size:13px;color:#8b9db0;display:block;margin-top:8px}
.bot{display:flex;gap:22px;padding:0 30px}.p{background:#18212b;padding:22px;border-radius:4px}
.p h3{font-size:18px;margin-bottom:14px;color:#cfe0f1}
label{display:block;font-size:13px;color:#8b9db0;margin:12px 0 5px}.in{background:#0f1419;border:1px solid #33465b;padding:12px 14px;font-size:17px;border-radius:3px}
.go{margin-top:18px;background:#2d7ff9;padding:15px;text-align:center;font-size:18px;font-weight:700;border-radius:3px}
table{width:100%;border-collapse:collapse;font-size:15px;font-family:Menlo,monospace}th{text-align:left;color:#8b9db0;font-weight:400;padding:8px;border-bottom:1px solid #33465b}td{padding:10px 8px;border-bottom:1px solid #222e3b}"""
body = f"""<div class=hd><h1>PRODUCTION MONITOR</h1><span style='color:#8b9db0'>All Sites &middot; Shift 2</span><span class=clock>14:32:07</span></div>
<div class=g>{tiles}</div>
<div class=bot><div class=p style='width:520px'><h3>Log downtime event</h3><label>Site / Line</label><div class=in>Plant 03 &middot; Line 2</div><label>Reason code</label><div class=in>Mechanical &mdash; Conveyor jam</div><label>Start time</label><div class=in>14:11</div><div class=go>SUBMIT EVENT</div></div>
<div class=p style='flex:1'><h3>Recent events</h3><table><tr><th>TIME</th><th>SITE</th><th>EVENT</th><th>DUR</th></tr><tr><td>14:11</td><td>P03-L2</td><td>Conveyor jam</td><td style='color:#e74c3c'>21m &#9679;</td></tr><tr><td>13:40</td><td>P05-L1</td><td>Changeover</td><td>32m</td></tr><tr><td>12:58</td><td>P01-L3</td><td>Material wait</td><td>9m</td></tr><tr><td>12:15</td><td>P02-L1</td><td>Sensor fault</td><td>14m</td></tr><tr><td>11:47</td><td>P06-L2</td><td>Planned PM</td><td>45m</td></tr><tr><td>10:30</td><td>P04-L1</td><td>Material wait</td><td>6m</td></tr></table></div></div>"""
w("multisite-monitoring", css, body)

# ---------------- Document Automation ----------------
css = """body{background:#eef0f3;color:#222}
.nav{height:54px;background:#fff;border-bottom:1px solid #d8dce1;display:flex;align-items:center;padding:0 30px;font-size:18px;font-weight:700;color:#3b4a6b;gap:12px}.nav small{font-weight:400;color:#888;font-size:14px}
.wrap{display:flex;gap:26px;padding:26px 30px}
.form{width:520px;background:#fff;border:1px solid #d8dce1;border-radius:8px;padding:24px}.form h2{font-size:18px;margin-bottom:6px}
label{display:block;font-size:13px;font-weight:600;color:#555;margin:14px 0 5px}.in{border:1px solid #c8cfd8;border-radius:5px;padding:11px 13px;font-size:15px;background:#fff}.ta{height:104px;line-height:1.5}
.row{display:flex;gap:14px}.row>div{flex:1}
.btn{margin-top:20px;background:#5b4bd5;color:#fff;text-align:center;padding:14px;border-radius:6px;font-weight:700;font-size:16px}
.doc{flex:1;background:#fff;border:1px solid #d8dce1;border-radius:8px;padding:30px 44px;position:relative}
.doc .tag{position:absolute;right:20px;top:16px;background:#e8e4ff;color:#5b4bd5;font-size:12px;font-weight:700;padding:5px 11px;border-radius:12px}
.doc h1{font-size:23px;margin-bottom:4px}.doc .sub{color:#888;font-size:13px;margin-bottom:20px}
.doc h3{font-size:14px;text-transform:uppercase;letter-spacing:.07em;color:#5b4bd5;margin:18px 0 6px}
.l{height:11px;background:#e5e8ec;border-radius:3px;margin:9px 0}.doc p{font-size:15px;line-height:1.6;color:#444}"""
body = """<div class=nav>DocGen <small>&middot; Field Report Assistant</small></div>
<div class=wrap><div class=form><h2>New field report</h2><span style='color:#888;font-size:14px'>Fill in the details &mdash; the draft is generated for you.</span>
<div class=row><div><label>Report type</label><div class=in>Service visit</div></div><div><label>Date</label><div class=in>09/24/2026</div></div></div>
<label>Site</label><div class=in>Site 14 &middot; West Region</div><label>Field notes</label><div class='in ta'>Unit down on arrival. Replaced worn drive belt, re-tensioned, ran 30 min test. Noted oil seep at rear housing &mdash; recommend follow-up.</div>
<div class=btn>&#10024; Generate document</div></div>
<div class=doc><span class=tag>AI DRAFT</span><h1>Service Visit Report</h1><div class=sub>Site 14 &middot; West Region &middot; 24 Sep 2026</div>
<h3>Summary</h3><p>Technician arrived to find the unit non-operational. The drive belt was found worn and was replaced and re-tensioned, followed by a 30-minute test run with normal results.</p>
<h3>Observations</h3><p>A minor oil seep was noted at the rear housing. Not currently affecting operation.</p><h3>Recommendations</h3><div class=l style='width:92%'></div><div class=l style='width:78%'></div><div class=l style='width:85%'></div></div></div>"""
w("cs-doc-automation", css, body)

# ---------------- AI Document-Parsing GPT (custom GPT: PDF -> Excel with confidence) ----------------
items = [("A-1042", 'Hydraulic hose 3/4"', "12", "$18.40", "$220.80", 99, False),
         ("B-2210", "Drive belt, B-section", "4", "$31.25", "$125.00", 97, False),
         ("C-0087", "Bearing kit", "10", "$22.50", "$225.00", 78, True),
         ("D-3391", "Filter element", "6", "$9.95", "$59.70", 81, True),
         ("E-5504", "Gasket set", "8", "$14.10", "$112.80", 96, False)]
assert abs(sum(float(t[4].strip("$")) for t in items) - 743.30) < 0.001
trs = ""
for p, d, q, u, t, c, flag in items:
    cls = " class=fl" if flag else ""
    badge = f"<span class='cf {'lo' if flag else 'hi'}'>{c}%</span>"
    trs += f"<tr{cls}><td>{p}</td><td>{d}</td><td>{q}</td><td>{u}</td><td>{t}</td><td>{badge}</td></tr>"
css = """body{background:#17191f;color:#e6e8ee}
.top{height:58px;background:#101217;border-bottom:1px solid #272b35;display:flex;align-items:center;padding:0 28px;gap:14px;font-size:18px;font-weight:700}
.av{width:32px;height:32px;border-radius:50%;background:linear-gradient(135deg,#2dd4bf,#6366f1);display:inline-block}.top small{font-weight:400;color:#8b93a5;font-size:14px}
.m{display:flex;gap:26px;padding:22px 28px}
.chat{width:1000px;display:flex;flex-direction:column;gap:16px}
.u{align-self:flex-end;background:#262b38;border-radius:16px 16px 4px 16px;padding:14px 18px;font-size:16px;max-width:620px}
.u .f{display:flex;align-items:center;gap:10px;background:#1b1f29;border:1px solid #343a49;border-radius:8px;padding:9px 12px;margin-bottom:10px;font-size:14px}.u .f b{background:#d64545;color:#fff;font-size:11px;padding:3px 6px;border-radius:4px}
.a{background:#1d212b;border:1px solid #2b303d;border-radius:16px 16px 16px 4px;padding:18px 20px;font-size:16px;line-height:1.5}
.a h4{font-size:16px;margin-bottom:10px;color:#fff}
table{width:100%;border-collapse:collapse;font-size:15px;margin:10px 0 12px}th{text-align:left;font-size:12px;letter-spacing:.07em;text-transform:uppercase;color:#8b93a5;padding:8px 10px;border-bottom:1px solid #343a49}
td{padding:10px;border-bottom:1px solid #2b303d}tr.fl td{background:rgba(251,191,36,.14)}tr.fl td:nth-child(3),tr.fl td:nth-child(4){outline:2px solid #fbbf24;outline-offset:-2px;font-weight:700;color:#fde68a}
.cf{font-weight:700;font-size:13px;padding:3px 9px;border-radius:10px}.cf.hi{background:#134e3f;color:#6ee7b7}.cf.lo{background:#5a4210;color:#fcd34d}
.w{background:#2b2410;border:1px solid #6b5416;border-radius:8px;padding:10px 14px;font-size:14px;color:#fde68a;line-height:1.6}
.ok{font-size:14px;color:#6ee7b7;margin-top:10px}
.dl{display:inline-block;margin-top:12px;background:#2dd4bf;color:#06201c;font-weight:800;font-size:15px;padding:10px 18px;border-radius:8px}
.ins{flex:1;background:#101217;border:1px solid #272b35;border-radius:12px;padding:20px 22px;height:638px}
.ins h3{font-size:12px;letter-spacing:.1em;color:#8b93a5;margin-bottom:12px}.ins pre{font:14px/1.75 Menlo,monospace;color:#b8c0d4;white-space:pre-wrap}.ins b{color:#2dd4bf}"""
body = f"""<div class=top><span class=av></span>Doc-to-Excel Assistant <small>&middot; custom GPT</small></div>
<div class=m><div class=chat>
<div class=u><div class=f><b>PDF</b>invoice_batch_0412.pdf &middot; 2 pages</div>Convert this to Excel.</div>
<div class=a><h4>Done &mdash; 5 line items extracted &middot; overall confidence 90%</h4>
<table><tr><th>Part #</th><th>Description</th><th>Qty</th><th>Unit price</th><th>Total</th><th>Confidence</th></tr>{trs}</table>
<div class=w>&#9888; 2 fields need your review: <b>C-0087 qty</b> (could be &ldquo;10&rdquo; or &ldquo;1O&rdquo;) and <b>D-3391 unit price</b> (smudged in scan). Highlighted above.</div>
<div class=ok>&#10003; Line totals add up to $743.30, matching the invoice subtotal.</div>
<span class=dl>&#11015; Download invoice_batch_0412.xlsx</span></div></div>
<div class=ins><h3>GPT INSTRUCTIONS (EXCERPT)</h3><pre><b>Role:</b> Convert uploaded PDFs of invoices and
packing lists into clean, Excel-ready tables.

<b>Always:</b>
1. Keep the same column order every time.
2. Give each field a confidence score (0&ndash;100%).
3. Highlight anything under 85% and say why.
4. Check that line totals add up to the subtotal.
5. Never guess &mdash; if unreadable, flag it blank.

<b>Output:</b> table in chat + downloadable .xlsx.</pre></div></div>"""
w("ai-image-parsing", css, body)

# ---------------- Production Line Layout Redesign (CAD-style) ----------------
css = """body{background:#1c2128;color:#cbd5e1;font-family:'Courier New',monospace}
.bar{height:36px;background:#2a323d;border-bottom:1px solid #3a4452;display:flex;align-items:center;padding:0 16px;gap:22px;font-size:14px;color:#aab5c4}.bar b{color:#fff}
.cmd{position:absolute;bottom:0;left:0;right:0;height:34px;background:#232a33;border-top:1px solid #3a4452;font-size:14px;padding:8px 16px;color:#9fb0c4}
svg{position:absolute;top:36px;left:0}"""
st = ""
for i, (x, l) in enumerate([(210, "STATION 1"), (420, "STATION 2"), (630, "STATION 3"), (840, "STATION 4"), (1050, "PACK-OUT")]):
    col = "#00d1ff" if i < 4 else "#7bff6a"
    st += f"<rect x={x} y=250 width=150 height=140 fill='none' stroke='{col}' stroke-width=2/><text x={x + 75} y=326 fill='{col}' font-size=14 text-anchor=middle>{l}</text>"
    if i < 4:
        st += f"<line x1={x + 150} y1=320 x2={x + 210} y2=320 stroke='#ffd24a' stroke-width=2 marker-end='url(#a)'/>"
body = f"""<div class=bar><b>Line_Layout_Rev3.dwg</b><span>MODEL</span><span>LAYOUT1</span><span>Scale 1/4"=1'</span><span style='margin-left:auto'>Layer: EQUIPMENT</span></div>
<svg width=1600 height=670 viewBox='0 0 1600 670'><defs><marker id=a markerWidth=10 markerHeight=10 refX=8 refY=5 orient=auto><path d='M0,0 L10,5 L0,10 z' fill='#ffd24a'/></marker></defs>
<g stroke='#2a323d'>{''.join(f"<line x1={x} x2={x} y1=0 y2=670/>" for x in range(0, 1600, 80))}{''.join(f"<line y1={y} y2={y} x1=0 x2=1600/>" for y in range(0, 670, 80))}</g>
<rect x=130 y=130 width=1230 height=440 fill=none stroke='#fff' stroke-width=3/>
<text x=145 y=158 fill='#fff' font-size=15>PRODUCTION AREA &mdash; BAY 3</text>{st}
<rect x=170 y=450 width=360 height=90 fill=none stroke='#ff6ad5' stroke-width=2 stroke-dasharray='8,5'/><text x=350 y=500 fill='#ff6ad5' font-size=14 text-anchor=middle>MATERIAL STAGING</text>
<g stroke='#9fb0c4' stroke-width=1.5 fill='#9fb0c4' font-size=14><line x1=210 x2=1200 y1=215 y2=215/><line x1=210 x2=210 y1=205 y2=225/><line x1=1200 x2=1200 y1=205 y2=225/><text x=700 y=205 text-anchor=middle>99'-0"</text>
<line x1=1400 x2=1400 y1=250 y2=390/><line x1=1390 x2=1410 y1=250 y2=250/><line x1=1390 x2=1410 y1=390 y2=390/><text x=1425 y=325>14'-0"</text></g>
<text x=1130 y=520 fill='#cbd5e1' font-size=13>REV 3 &mdash; STAKEHOLDER APPROVED</text></svg>
<div class=cmd>Command: _DIMLINEAR &nbsp; Specify first extension line origin or &lt;select object&gt;:</div>"""
w("line-layout-redesign", css, body)

# ---------------- Internal Support Chatbot ----------------
css = """body{background:#f0f2f5;color:#1c1e21}
.nav{height:56px;background:#fff;border-bottom:1px solid #dfe2e6;display:flex;align-items:center;padding:0 30px;font-size:19px;font-weight:700;color:#0a6e5e;gap:12px}.nav small{font-weight:400;color:#8a8f98;font-size:14px}
.wrap{display:flex;height:684px}.side{width:300px;background:#fff;border-right:1px solid #dfe2e6;padding:20px;font-size:15px}.side h4{font-size:12px;text-transform:uppercase;color:#8a8f98;margin:0 0 10px;letter-spacing:.07em}.side div{padding:9px 12px;border-radius:6px;margin-bottom:4px;color:#444}.side .on{background:#e5f4f1;color:#0a6e5e;font-weight:600}
.chat{flex:1;padding:26px 60px;display:flex;flex-direction:column;gap:18px}
.u{align-self:flex-end;background:#0a6e5e;color:#fff;padding:14px 20px;border-radius:16px 16px 4px 16px;max-width:620px;font-size:17px}
.b{align-self:flex-start;background:#fff;border:1px solid #dfe2e6;padding:18px 22px;border-radius:16px 16px 16px 4px;max-width:820px;font-size:17px;line-height:1.55}
.b ol{margin:8px 0 12px 22px}.src{display:inline-block;background:#e5f4f1;color:#0a6e5e;border-radius:12px;padding:5px 12px;font-size:13px;font-weight:600;margin:4px 6px 0 0}
.in{margin-top:auto;background:#fff;border:1px solid #cfd3d8;border-radius:24px;padding:15px 22px;font-size:16px;color:#8a8f98;display:flex;justify-content:space-between}.in b{color:#0a6e5e}"""
body = """<div class=nav>PlantAssist <small>&middot; equipment support chatbot</small></div>
<div class=wrap><div class=side><h4>Knowledge sources</h4><div class=on>Equipment manuals (48)</div><div>Troubleshooting guides (22)</div><div>Parts reference</div><div>Sales / spec sheets</div><h4 style='margin-top:22px'>Recent chats</h4><div>Hydraulic pressure low</div><div>Fault code E-214</div></div>
<div class=chat><div class=u>Unit shows fault code E-214 and won't start. What should I check first?</div>
<div class=b>E-214 indicates a <b>drive overload</b>. Recommended checks, in order:<ol><li>Inspect the drive belt for wear or slack.</li><li>Check the motor amp draw against the nameplate rating.</li><li>Clear the fault and run a no-load test.</li></ol>If the fault returns, escalate to service.<br><span class=src>&#128196; Model XR Service Manual &middot; p. 42</span><span class=src>&#128196; Troubleshooting Guide &middot; Faults E-2xx</span></div>
<div class=u>Where's the belt tension spec?</div>
<div class=b>Belt tension should be set per <b>Section 6.3</b> of the service manual. <span class=src>&#128196; Service Manual &middot; p. 118</span></div>
<div class=in><span>Ask about any equipment, fault code, or procedure&hellip;</span><b>&#10148;</b></div></div></div>"""
w("equipment-chatbot", css, body)
