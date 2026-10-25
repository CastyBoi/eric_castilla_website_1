"""Generates HTML for the 6 "tool" mock images (fake data). Run via mockups/render.sh."""
import re, html
def w(name,css,body,W=1600,H=740):
    body=re.sub(r'(=[^\s"\'>]+)/>',r'\1 />',body)
    open(name+'.html','w').write(f"<!doctype html><html><head><meta charset=utf-8><style>*{{box-sizing:border-box;margin:0;padding:0}}html,body{{width:{W}px;height:{H}px;overflow:hidden;font-family:-apple-system,'Helvetica Neue',Arial,sans-serif}}{css}</style></head><body>{body}</body></html>")
KW=r'\b(import|from|as|def|return|if|else|for|in|with|True|False|None)\b'
def hl(src):
    out=[]
    for line in src.strip('\n').split('\n'):
        tok=re.compile(r'(#.*$)|("[^"]*"|\'[^\']*\')|(\b\d[\d_.]*\b)|'+KW+r'|(\b[a-zA-Z_]+)(?=\()')
        res="";pos=0
        for m in tok.finditer(line):
            res+=html.escape(line[pos:m.start()])
            t=html.escape(m.group(0))
            cls='c' if m.group(1) else 's' if m.group(2) else 'n' if m.group(3) else 'k' if m.group(4) else 'f'
            res+=f"<span class={cls}>{t}</span>";pos=m.end()
        res+=html.escape(line[pos:]);out.append(res)
    return "<br>".join(out)
CODECSS=".code{font:15px/1.7 Menlo,monospace;color:#d7dae0}.code .c{color:#7f848e}.code .s{color:#98c379}.code .n{color:#d19a66}.code .k{color:#c678dd}.code .f{color:#61afef}"

# ---------- 01 Projection builder (3-step) ----------
css="""body{background:#16181d;color:#f3efe8}
.top{height:74px;display:flex;align-items:center;padding:0 44px;gap:18px;border-bottom:1px solid #2b2f38}.top b{font-size:25px;letter-spacing:.01em}.top span{color:#9aa0ab;font-size:15px}.top em{margin-left:auto;font-style:normal;font-size:14px;color:#9aa0ab;border:1px solid #2f343e;padding:7px 14px;border-radius:20px}
.steps{display:flex;gap:0;padding:30px 44px 0;align-items:stretch}
.p{flex:1;background:#1f232b;border:1px solid #2d323d;border-radius:14px;padding:24px;height:520px}
.ar{width:54px;display:flex;align-items:center;justify-content:center;color:#f08a24;font-size:30px}
.nb{display:inline-flex;width:30px;height:30px;border-radius:50%;background:#f08a24;color:#16181d;font-weight:800;align-items:center;justify-content:center;margin-right:10px}
.p h2{font-size:20px;display:flex;align-items:center;margin-bottom:6px}.p .sub{color:#9aa0ab;font-size:14px;margin-bottom:20px}
.dz{border:2px dashed #475064;border-radius:12px;height:130px;display:flex;flex-direction:column;align-items:center;justify-content:center;color:#9aa0ab;font-size:15px;gap:6px}.dz b{color:#f08a24;font-size:30px}
.fi{display:flex;justify-content:space-between;background:#272c36;border-radius:8px;padding:12px 14px;margin-top:10px;font-size:14px}.fi i{font-style:normal;color:#7ddc9b}
.lb{font-size:12px;letter-spacing:.09em;color:#9aa0ab;text-transform:uppercase;margin:16px 0 8px}
.chips span{display:inline-block;background:#272c36;border:1px solid #3a4150;padding:8px 14px;border-radius:18px;font-size:14px;margin:0 8px 8px 0}.chips .on{background:#f08a24;color:#16181d;border-color:#f08a24;font-weight:700}
.seg{display:inline-flex;border:1px solid #3a4150;border-radius:8px;overflow:hidden}.seg span{padding:9px 18px;font-size:14px}.seg .on{background:#3a4150;font-weight:700}
.sel{background:#272c36;border:1px solid #3a4150;border-radius:8px;padding:11px 14px;font-size:14px;display:flex;justify-content:space-between}
.tg{display:flex;justify-content:space-between;font-size:14px;padding:9px 0;border-bottom:1px solid #2b2f38}.tg i{font-style:normal;color:#f08a24;font-weight:700}
.of{display:flex;align-items:center;gap:12px;background:#272c36;border-radius:8px;padding:11px 13px;margin-bottom:9px;font-size:14px}.of u{text-decoration:none;background:#34506b;color:#9ed0ff;font-size:11px;font-weight:700;padding:4px 7px;border-radius:4px}.of s{text-decoration:none;margin-left:auto;color:#9aa0ab;font-size:13px}
.gbtn{margin-top:14px;background:#f08a24;color:#16181d;text-align:center;font-weight:800;padding:14px;border-radius:9px;font-size:16px}
.foot{padding:16px 44px;color:#9aa0ab;font-size:14px}"""
body="""<div class=top><b>Projection Builder</b><span>Upload data &rarr; aggregate &rarr; generate files</span><em>Last run: Oct 24 &middot; 6 files &middot; 2.1s</em></div>
<div class=steps>
<div class=p><h2><i class=nb>1</i>Upload data</h2><div class=sub>Drop the latest source extracts.</div><div class=dz><b>&#8679;</b>Drag .xlsx / .csv here</div>
<div class=fi><span>sales_history_fy26.xlsx</span><i>48,210 rows &#10003;</i></div><div class=fi><span>open_orders_oct.csv</span><i>6,912 rows &#10003;</i></div><div class=fi><span>adjustments_oct.xlsx</span><i>318 rows &#10003;</i></div></div>
<div class=ar>&rarr;</div>
<div class=p><h2><i class=nb>2</i>Build aggregation</h2><div class=sub>Choose how the data is rolled up.</div>
<div class=lb>Group by</div><div class=chips><span class=on>Region</span><span class=on>Product family</span><span>Customer tier</span><span>Plant</span></div>
<div class=lb>Period</div><div class=seg><span>Week</span><span class=on>Month</span><span>Quarter</span></div>
<div class=lb>Method</div><div class=sel><span>Weighted average (12 mo)</span><span>&#8964;</span></div>
<div class=lb>Options</div><div class=tg><span>Apply manual adjustments</span><i>ON</i></div><div class=tg><span>Exclude one-time orders</span><i>ON</i></div></div>
<div class=ar>&rarr;</div>
<div class=p><h2><i class=nb>3</i>Generate files</h2><div class=sub>One output per audience.</div>
<div class=of><u>XLSX</u>region_rollup_NE.xlsx<s>212 KB</s></div><div class=of><u>XLSX</u>region_rollup_SW.xlsx<s>198 KB</s></div><div class=of><u>XLSX</u>region_rollup_W.xlsx<s>240 KB</s></div><div class=of><u>CSV</u>supply_chain_summary.csv<s>96 KB</s></div><div class=of><u>CSV</u>sql_upload_batch.csv<s>1.4 MB</s></div>
<div class=gbtn>Generate all files</div></div></div>"""
w("01_sales_projection_hub",css,body)

# ---------- 02 Script runner (IDE) ----------
code=hl('''
import pandas as pd
from sqlalchemy import create_engine

df = pd.read_excel(path, sheet_name="Export")
df = df.dropna(subset=["order_id"])
df["ship_date"] = pd.to_datetime(df["ship_date"])

daily = (df.groupby(["plant", "ship_date"], as_index=False)
           ["qty"].sum())

daily.to_sql("daily_deliveries", engine,
             if_exists="append", index=False)''')
scripts=[("delivery_report.py",True),("production_report.py",False),("work_orders_a.py",False),("work_orders_b.py",False),("placeholder.py",False)]
sl="".join(f"<div class='sc{' on' if o else ''}'><span>{n}</span><b>&#9654; Run</b></div>" for n,o in scripts)
css=CODECSS+"""body{background:#1a1d23;color:#d7dae0}
.top{height:56px;background:#14161b;border-bottom:1px solid #2a2e37;display:flex;align-items:center;padding:0 24px;gap:16px;font-size:18px;font-weight:700}.top i{margin-left:auto;font-style:normal;font-size:13px;font-weight:400;color:#8bd49c}
.m{display:flex;height:684px}.sb{width:340px;background:#15171c;border-right:1px solid #2a2e37;padding:20px 16px}.sb h4{font-size:12px;letter-spacing:.1em;color:#7f848e;margin-bottom:14px}
.sc{display:flex;justify-content:space-between;align-items:center;padding:13px 14px;border-radius:7px;margin-bottom:6px;font:14px Menlo,monospace}.sc b{font:700 12px Arial;background:#2a2e37;color:#cfd3da;padding:6px 11px;border-radius:5px}.sc.on{background:#242933;outline:1px solid #3b4252}.sc.on b{background:#e8a33a;color:#1a1d23}
.ed{flex:1;display:flex;flex-direction:column}.tab{height:40px;background:#14161b;border-bottom:1px solid #2a2e37;padding:0 20px;display:flex;align-items:center;font:13px Menlo,monospace;color:#cfd3da;gap:20px}.tab u{text-decoration:none;border-bottom:2px solid #e8a33a;padding:11px 0}
.code{padding:24px 34px;height:370px}.con{border-top:1px solid #2a2e37;background:#101216;padding:18px 34px;font:14px/1.8 Menlo,monospace;flex:1;color:#9aa0ab}.con b{color:#8bd49c;font-weight:400}.con em{font-style:normal;color:#e8a33a}"""
body=f"""<div class=top>Plant ETL Hub<i>&#9679; connected to warehouse</i></div><div class=m><div class=sb><h4>SCRIPTS</h4>{sl}</div>
<div class=ed><div class=tab><u>delivery_report.py</u><span style='color:#7f848e'>Processes the weekly delivery export</span></div><div class=code>{code}</div>
<div class=con><em>$ run delivery_report.py</em><br>reading orders_wk42.xlsx ...<br>cleaned 3,912 rows &rarr; dropped 72 blanks<br><b>&#10003; loaded 3,840 rows into daily_deliveries in 1.2s</b></div></div></div>"""
w("02_etl_hub",css,body)

# ---------- 03 Upload + transform (light) ----------
code=hl('''
import pandas as pd

df = pd.read_excel(uploaded_file)
df.columns = df.columns.str.strip().str.lower()

df = df[df["status"] == "Shipped"]
summary = (df.groupby("product").agg(
    orders=("order_id", "count"),
    units=("qty", "sum")).reset_index())

summary.to_excel("delivery_summary.xlsx", index=False)''')
css=CODECSS+"""body{background:#eef4f1;color:#18322a}
.top{height:60px;background:#fff;border-bottom:1px solid #d6e3dd;display:flex;align-items:center;padding:0 38px;font-size:20px;font-weight:700;color:#1b6b4f}.top span{font-weight:400;color:#6a8a7e;font-size:15px;margin-left:12px}
.w{display:flex;gap:26px;padding:26px 38px}
.l{width:560px;background:#fff;border:1px solid #d6e3dd;border-radius:14px;padding:28px;height:600px}.l h2{font-size:21px;margin-bottom:6px}.l p{color:#6a8a7e;font-size:15px;margin-bottom:24px}
.ub{display:inline-block;background:#1b9d6b;color:#fff;font-weight:700;font-size:18px;padding:16px 34px;border-radius:10px;box-shadow:0 6px 14px rgba(27,157,107,.35)}
.fc{margin-top:20px;border:1px solid #cfe3d9;background:#f4faf7;border-radius:9px;padding:13px 15px;font-size:15px;display:flex;justify-content:space-between}
.st{margin-top:26px;font-size:15px;line-height:2.2;color:#2f5547}.st i{color:#1b9d6b;font-style:normal;font-weight:800;margin-right:8px}
.r{flex:1;display:flex;flex-direction:column;gap:16px}.cd{background:#1d2127;border-radius:14px;padding:22px 30px;height:352px}.cd small{font:12px Arial;letter-spacing:.1em;color:#7f848e;display:block;margin-bottom:12px}
.pv{background:#fff;border:1px solid #d6e3dd;border-radius:14px;padding:18px 24px;flex:1}.pv small{font-size:12px;letter-spacing:.1em;color:#6a8a7e;display:block;margin-bottom:8px}
table{width:100%;border-collapse:collapse;font-size:15px}th{text-align:left;color:#6a8a7e;font-weight:600;font-size:13px;padding:7px 8px;border-bottom:2px solid #d6e3dd}td{padding:9px 8px;border-bottom:1px solid #edf3f0}"""
body=f"""<div class=top>Delivery Report Upload<span>Excel in &rarr; summary out</span></div><div class=w><div class=l><h2>Upload workbook</h2><p>Choose the weekly export and run the transform.</p><span class=ub>Choose .xlsx file</span>
<div class=fc><span>orders_week42.xlsx</span><span style='color:#6a8a7e'>184 KB</span></div><div class=st><i>&#10003;</i>Columns normalized<br><i>&#10003;</i>Filtered to shipped orders (3,840)<br><i>&#10003;</i>Grouped by product<br><i>&#10003;</i>delivery_summary.xlsx ready</div></div>
<div class=r><div class=cd><small>TRANSFORM</small><div class=code>{code}</div></div><div class=pv><small>OUTPUT PREVIEW</small><table><tr><th>product</th><th>orders</th><th>units</th></tr><tr><td>Widget A</td><td>412</td><td>9,870</td></tr><tr><td>Widget B</td><td>388</td><td>8,115</td></tr><tr><td>Assembly C</td><td>301</td><td>4,226</td></tr><tr><td>Kit D</td><td>257</td><td>3,904</td></tr></table></div></div></div>"""
w("03_delivery_report_upload",css,body)

# ---------- 04 Forecast loader (violet) ----------
code=hl('''
import pandas as pd

df = pd.read_csv(uploaded_file)
wk = df.melt(id_vars="machine", var_name="week",
             value_name="demand")

wk = wk[wk["machine"] == machine]
wk["forecast"] = (wk["demand"]
                  .rolling(4).mean().shift(-1))

out = wk[wk["week"] >= start_week]''')
bars="".join(f"<rect x='{20+i*54}' y='{120-v}' width='38' height='{v}' fill='{'#8f7bff' if i>=5 else '#4a4f7a'}'/><text x='{39+i*54}' y='140' font-size=12 fill='#9aa0c8' text-anchor=middle>W{40+i}</text>" for i,v in enumerate([52,60,57,66,71,78,74,83,80,90]))
css=CODECSS+"""body{background:linear-gradient(135deg,#141330,#231a4d);color:#ecebff}
.top{height:60px;display:flex;align-items:center;padding:0 38px;font-size:20px;font-weight:700;border-bottom:1px solid #342d6a}.top span{margin-left:12px;font-weight:400;color:#9a95d6;font-size:15px}
.w{display:flex;gap:26px;padding:26px 38px}
.l{width:540px;background:#1d1a40;border:1px solid #382f73;border-radius:16px;padding:28px;height:612px}.l h2{font-size:21px;margin-bottom:22px}
label{display:block;font-size:12px;letter-spacing:.09em;color:#9a95d6;margin:18px 0 8px}.in{background:#14122d;border:1px solid #433a8a;border-radius:9px;padding:13px 15px;font-size:15px;display:flex;justify-content:space-between}
.fl{margin-top:18px;font-size:14px;color:#8bd49c}.btn{margin-top:26px;background:#8f7bff;color:#12102a;text-align:center;font-weight:800;font-size:17px;padding:16px;border-radius:10px}
.r{flex:1;display:flex;flex-direction:column;gap:18px}.cd{background:#100f24;border:1px solid #382f73;border-radius:16px;padding:24px 30px;height:352px}.cd small,.ch small{font:12px Arial;letter-spacing:.1em;color:#9a95d6;display:block;margin-bottom:12px}
.ch{background:#1d1a40;border:1px solid #382f73;border-radius:16px;padding:18px 26px;flex:1}"""
body=f"""<div class=top>Forecast File Loader<span>Pick a machine, set the start week, upload</span></div><div class=w><div class=l><h2>Upload &amp; process</h2>
<label>MACHINE</label><div class=in><span>Machine 07 &middot; Line B</span><span>&#8964;</span></div><label>FORECAST START WEEK</label><div class=in><span>Wk 43 &mdash; Oct 19, 2026</span><span>&#8964;</span></div><label>FILE</label><div class=in><span>demand_by_week.csv</span><span style='color:#9a95d6'>Browse</span></div><div class=fl>&#10003; 52 weeks detected &middot; 1 machine matched</div><div class=btn>Upload and process</div></div>
<div class=r><div class=cd><small>PROCESSING LOGIC</small><div class=code>{code}</div></div><div class=ch><small>RESULT &mdash; DEMAND (DIM) VS FORECAST (BRIGHT)</small><svg width=800 height=150>{bars}</svg></div></div></div>"""
w("04_forecast_file_upload",css,body)

# ---------- 05 Log viewer ----------
logs=[("08:06:03","INFO","main_pipeline","Job executed successfully; next run 2026-10-24 08:06 PDT"),("08:06:03","INFO","main_pipeline","Total time: 3.60 seconds"),("08:06:03","INFO","sql_loader","Completed insert into etl_all_plant_data"),("08:06:02","INFO","sql_loader","Committed refresh for plant_a: deleted=3840 inserted=3840 dupes=0"),("08:05:59","WARN","extract","Source file 4 min older than expected; continuing"),("08:05:58","ERROR","sql_loader","DBAPIError: Transaction (Process ID 83) was deadlocked and chosen as victim (1205)"),("TB","","","Traceback (most recent call last):\n  File \"C:\\svc_etl\\pipeline\\loader.py\", line 88, in refresh\n    conn.execute(delete_stmt, params)\n  File \"C:\\svc_etl\\venv\\Lib\\site-packages\\sqlalchemy\\engine\\base.py\", line 1964, in _exec\npyodbc.Error: ('40001', 'Transaction was deadlocked on lock resources')"),("08:05:58","INFO","sql_loader","Retry 1/3 after 2s backoff"),("08:05:55","INFO","extract","Read 3,840 rows from plant_a export")]
rows=""
for t,l,j,m in logs:
    if t=="TB": rows+=f"<div class=tb>{html.escape(m).replace(chr(10),'<br>')}</div>";continue
    rows+=f"<div class='r {l}'><span class=t>{t}</span><span class='lv {l}'>{l}</span><span class=j>{j}</span><span class=m>{html.escape(m)}</span></div>"
css="""body{background:#f4f6fa;color:#1f2733}
.top{height:62px;background:#1f3a5f;color:#fff;display:flex;align-items:center;padding:0 30px;gap:18px;font-size:21px;font-weight:700}.top span{font-weight:400;font-size:14px;opacity:.8;margin-left:auto}.top i{font-style:normal;background:#2c8a5a;font-size:12px;padding:5px 11px;border-radius:12px;font-weight:700}
.fb{display:flex;gap:12px;padding:18px 30px;align-items:center}.ch{background:#fff;border:1px solid #d3dae4;border-radius:18px;padding:8px 16px;font-size:14px}.ch.on{background:#1f3a5f;color:#fff;border-color:#1f3a5f}.ch b{margin-left:6px}.ch.e b{color:#d64545}
.se{margin-left:auto;background:#fff;border:1px solid #d3dae4;border-radius:8px;padding:9px 14px;width:300px;font-size:14px;color:#8a95a5}.jb{background:#fff;border:1px solid #d3dae4;border-radius:8px;padding:9px 14px;font-size:14px}
.lg{margin:0 30px;background:#fff;border:1px solid #d3dae4;border-radius:10px;overflow:hidden}
.r{display:flex;align-items:center;gap:18px;padding:13px 20px;border-bottom:1px solid #edf0f5;font-size:15px}.r.ERROR{background:#fdeeee}.r.WARN{background:#fff8e6}
.t{font:14px Menlo,monospace;color:#6b7788;width:80px}.lv{width:70px;text-align:center;font-size:11px;font-weight:700;padding:4px 0;border-radius:4px}.lv.INFO{background:#e1efff;color:#1f5fb0}.lv.WARN{background:#ffe7a8;color:#8a5a00}.lv.ERROR{background:#d64545;color:#fff}
.j{font:14px Menlo,monospace;color:#6b7788;width:130px}.m{flex:1}
.tb{background:#161a20;color:#ff8f8f;font:13px/1.7 Menlo,monospace;padding:14px 26px 14px 190px;border-bottom:1px solid #edf0f5;white-space:nowrap}"""
body=f"""<div class=top>Pipeline Log Viewer<i>&#9679; LIVE</i><span>Auto-refresh 30s &middot; last refreshed 3:22:48</span></div>
<div class=fb><span class='ch on'>All<b>412</b></span><span class=ch>Info<b>398</b></span><span class=ch>Warn<b>11</b></span><span class='ch e'>Error<b>3</b></span><span class=jb>Job: all &#8964;</span><span class=se>Search messages&hellip;</span></div>
<div class=lg>{rows}</div>"""
w("05_etl_pipeline_logs",css,body)

# ---------- 06 Productivity review ----------
STD=[("WLD",13204),("FAB",10112),("PNT",9876),("SHP",8410),("RCV",7955),("DIE",7620),("LOG",6788),("INS",5302),("MLD",4655),("QA",2729)]
VAR=[518,-66,402,-190,88,231,-145,97,322,129]
TOT_STD,TOT_ACT=76651,78037
assert sum(v for _,v in STD)==TOT_STD, sum(v for _,v in STD)
assert sum(VAR)==TOT_ACT-TOT_STD==1386, sum(VAR)
depts=[(d,s_,s_+v) for (d,s_),v in zip(STD,VAR)]
assert sum(a_ for _,_,a_ in depts)==TOT_ACT
mx=15000
db="";
for i,(d,s,a) in enumerate(depts):
    y=10+i*38
    col="#2dd4bf" if a<=s*1.03 else "#fb7185"
    db+=f"<text x=0 y={y+19} font-size=14 fill='#cbd5e1' font-weight=700>{d}</text><rect x=52 y={y} width={s/mx*470} height=24 rx=4 fill='#1e2a44'/><rect x=52 y={y+5} width={a/mx*470} height=14 rx=3 fill='{col}'/><line x1={52+s/mx*470} x2={52+s/mx*470} y1={y-3} y2={y+29} stroke='#fbbf24' stroke-width=3/><text x={52+max(s,a)/mx*470+10} y={y+19} font-size=13 fill='#94a3b8'>{a:,}</text>"
emps=[("EMP-1001",3458,1931,-1527,179),("EMP-1008",3399,2360,-1039,144),("EMP-1015",3271,1768,-1503,185),("EMP-1022",3074,1537,-1537,200),("EMP-1029",3041,3620,579,84),("EMP-1036",3011,2230,-781,135),("EMP-1043",2888,2601,-287,111),("EMP-1050",2742,3046,304,90),("EMP-1057",2729,2624,-105,104),("EMP-1064",2633,1408,-1225,187)]
er=""
for e,s,a,v,p in sorted(emps,key=lambda r:-r[4]):
    stt=("Review","#fb7185") if p<95 else ("Top","#2dd4bf") if p>=140 else ("On std","#94a3b8")
    bw=min(p,200)/200*120
    er+=f"<div class=er><b>{e}</b><span class=bg><i style='width:{bw}px;background:{stt[1]}'></i></span><span class=pc>{p}%</span><u style='color:{stt[1]};border-color:{stt[1]}'>{stt[0]}</u></div>"
css="""body{background:#0f172a;color:#e2e8f0}
.hd{height:64px;display:flex;align-items:center;padding:0 34px;gap:22px;border-bottom:1px solid #1e293b}.hd b{font-size:23px}.hd span{color:#94a3b8;font-size:14px}
.fp{margin-left:auto;display:flex;gap:10px}.fp div{background:#1e293b;border:1px solid #334155;border-radius:8px;padding:8px 14px;font-size:13px;color:#cbd5e1}.fp b{color:#fff;font-size:13px}
.k{display:flex;gap:16px;padding:20px 34px 0}.kt{flex:1;background:#1e293b;border-radius:12px;padding:16px 20px;border-top:3px solid var(--c)}.kt small{color:#94a3b8;font-size:13px}.kt b{display:block;font-size:34px;margin-top:6px}
.g{display:flex;gap:18px;padding:18px 34px}.pn{background:#162033;border:1px solid #243049;border-radius:12px;padding:18px 22px;height:468px}.pn h3{font-size:15px;color:#cbd5e1;margin-bottom:6px}.pn small{color:#64748b;font-size:12px;display:block;margin-bottom:14px}
.lg{display:flex;gap:16px;font-size:12px;color:#94a3b8;margin-bottom:12px}.lg i{display:inline-block;width:12px;height:12px;border-radius:2px;margin-right:6px;vertical-align:-2px}
.er{display:flex;align-items:center;gap:12px;padding:8px 0;border-bottom:1px solid #1e293b;font-size:14px}.er b{width:84px;font-weight:600}.bg{width:120px;height:10px;background:#1e293b;border-radius:5px;display:inline-block}.bg i{display:block;height:10px;border-radius:5px}.pc{width:48px;text-align:right}.er u{text-decoration:none;font-size:11px;font-weight:700;border:1px solid;border-radius:10px;padding:3px 9px;width:60px;text-align:center}
.sk{display:flex;justify-content:space-between;padding:10px 0;border-bottom:1px solid #1e293b;font-size:14px}.sk span:last-child{font-weight:700}"""
body=f"""<div class=hd><b>Plant Productivity &amp; Review</b><span>Standard vs actual hours &middot; FY2026</span><div class=fp><div>Year <b>2026</b></div><div>Department <b>All</b></div><div>Weeks <b>1 &ndash; 39</b></div></div></div>
<div class=k><div class=kt style='--c:#38bdf8'><small>Standard hours</small><b>76,651</b></div><div class=kt style='--c:#fbbf24'><small>Actual hours</small><b>78,037</b></div><div class=kt style='--c:#fb7185'><small>Variance hours</small><b>+1,386</b></div><div class=kt style='--c:#a78bfa'><small>Orders</small><b>12,409</b></div><div class=kt style='--c:#2dd4bf'><small>Overall efficiency</small><b>98%</b></div></div>
<div class=g><div class=pn style='width:640px'><h3>Hours by department &middot; all 10 departments</h3><div class=lg><span><i style='background:#1e2a44;border:1px solid #475569'></i>Standard (line)</span><span><i style='background:#2dd4bf'></i>Actual &le; standard</span><span><i style='background:#fb7185'></i>Actual over standard</span></div><svg width=590 height=400>{db}</svg><div style='position:absolute;left:0;right:0;bottom:0'></div></div>
<div class=pn style='width:470px'><h3>Employee ranking</h3><small>Top 10 of 142 employees &middot; flags for supervisor review</small>{er}</div>
<div class=pn style='flex:1'><h3>Top products by variance</h3><small>Hours over / under standard</small><div class=sk><span>Assembly C</span><span style='color:#fb7185'>+412 h</span></div><div class=sk><span>Widget B</span><span style='color:#fb7185'>+286 h</span></div><div class=sk><span>Kit D</span><span style='color:#fb7185'>+131 h</span></div><div class=sk><span>Widget A</span><span style='color:#2dd4bf'>-94 h</span></div><div class=sk><span>Housing F</span><span style='color:#2dd4bf'>-210 h</span></div><div class=sk><span>All other products</span><span style='color:#fb7185'>+861 h</span></div><div class=sk style='border-top:2px solid #334155;margin-top:6px'><span><b>Total variance</b></span><span style='color:#fb7185'>+1,386 h</span></div></div></div>"""
w("06_productivity_monitor",css,body)
