#!/usr/bin/env python3
"""
Rebuild dashboard.html from a fresh export.

    python3 build_dashboard.py [data_dir] [-o dashboard.html]

data_dir must contain orders.csv and ad-spend.csv (defaults to ./sample-data).

orders.csv    order_date, channel, revenue, discount_amount, was_returned
              (order_id, customer_id, discount_code used when present)
ad-spend.csv  date, channel, ad_spend

Everything downstream is derived, so a longer export, new channels, or a
channel that stops running ads all flow through without edits here.
"""

import argparse
import csv
import datetime as dt
import json
import os
import sys
from collections import defaultdict

# Categorical slots 1-4 of the validated palette, light/dark steps.
# Assigned to channels alphabetically so a given channel keeps its color
# across rebuilds, and always rendered in slot order so the adjacent-pair
# CVD validation holds.
SLOTS = [
    ("#2a78d6", "#3987e5"),  # blue
    ("#eb6834", "#d95926"),  # orange
    ("#1baf7a", "#199e70"),  # aqua
    ("#eda100", "#c98500"),  # yellow
    ("#e87ba4", "#d55181"),  # magenta
    ("#008300", "#008300"),  # green
    ("#4a3aa7", "#9085e9"),  # violet
    ("#e34948", "#e66767"),  # red
]

REQUIRED_ORDER_COLS = {"order_date", "channel", "revenue", "was_returned"}
REQUIRED_SPEND_COLS = {"date", "channel", "ad_spend"}


def die(msg):
    sys.exit(f"build_dashboard.py: {msg}")


def read_csv(path, required, label):
    if not os.path.exists(path):
        die(f"missing {label}: {path}")
    with open(path, newline="", encoding="utf-8-sig") as fh:
        rows = list(csv.DictReader(fh))
    if not rows:
        die(f"{label} has no data rows")
    missing = required - set(rows[0])
    if missing:
        die(f"{label} is missing column(s): {', '.join(sorted(missing))}")
    return rows


def num(value, default=0.0):
    try:
        return float(str(value).replace(",", "").replace("$", "").strip() or default)
    except ValueError:
        return default


def parse_date(value):
    text = str(value).strip()[:10]
    for fmt in ("%Y-%m-%d", "%m/%d/%Y", "%d/%m/%Y", "%Y/%m/%d"):
        try:
            return dt.datetime.strptime(text, fmt).date()
        except ValueError:
            continue
    return None


def blank(chan):
    return {
        "channel": chan,
        "orders": 0,
        "kept": 0.0,
        "refunded": 0.0,
        "returns": 0,
        "discount": 0.0,
        "spend": 0.0,
        "orders_nocode": 0,
        "returns_nocode": 0,
        "orders_code": 0,
        "returns_code": 0,
        "customers": 0,
        "repeat_customers": 0,
        "cohort_kept": 0.0,
    }


def aggregate(data_dir):
    orders = read_csv(os.path.join(data_dir, "orders.csv"), REQUIRED_ORDER_COLS, "orders.csv")
    spend_rows = read_csv(os.path.join(data_dir, "ad-spend.csv"), REQUIRED_SPEND_COLS, "ad-spend.csv")

    chans = defaultdict(lambda: None)
    cust_orders = defaultdict(list)   # customer_id -> [(date, channel, kept_revenue)]
    weeks = defaultdict(lambda: {"by_channel": defaultdict(lambda: [0, 0, 0.0])})
    dates, skipped = [], 0

    for row in orders:
        day = parse_date(row.get("order_date"))
        chan = (row.get("channel") or "").strip() or "unattributed"
        if day is None:
            skipped += 1
            continue
        dates.append(day)

        if chans[chan] is None:
            chans[chan] = blank(chan)
        c = chans[chan]

        revenue = num(row.get("revenue"))
        returned = str(row.get("was_returned", "")).strip().lower() in ("1", "true", "yes", "y", "t")
        has_code = bool((row.get("discount_code") or "").strip())

        c["orders"] += 1
        c["discount"] += num(row.get("discount_amount"))
        if returned:
            c["returns"] += 1
            c["refunded"] += revenue
        else:
            c["kept"] += revenue
        if has_code:
            c["orders_code"] += 1
            c["returns_code"] += returned
        else:
            c["orders_nocode"] += 1
            c["returns_nocode"] += returned

        cust = (row.get("customer_id") or "").strip()
        if cust:
            cust_orders[cust].append((day, chan, 0.0 if returned else revenue))

        monday = day - dt.timedelta(days=day.weekday())
        agg = weeks[monday]["by_channel"][chan]
        agg[0] += 1
        agg[1] += returned
        agg[2] += revenue if not returned else 0.0

    if not dates:
        die("no orders rows had a readable order_date")

    # Credit each customer, and everything they ever spent, to the channel that first brought them in.
    # Repeat rate is only meaningful over the window in the export - a short window understates it.
    for cust, hist in cust_orders.items():
        hist.sort(key=lambda h: h[0])
        first_chan = hist[0][1]
        if chans[first_chan] is None:
            chans[first_chan] = blank(first_chan)
        c = chans[first_chan]
        c["customers"] += 1
        if len(hist) > 1:
            c["repeat_customers"] += 1
        c["cohort_kept"] += sum(h[2] for h in hist)

    first, last = min(dates), max(dates)
    span_days = (last - first).days + 1

    spend_undated = spend_outside = 0
    for row in spend_rows:
        chan = (row.get("channel") or "").strip() or "unattributed"
        day = parse_date(row.get("date"))
        if day is None:
            spend_undated += 1
            continue
        if not (first <= day <= last):
            spend_outside += 1      # spend/week is derived from the orders window; other rows would inflate it
            continue
        if chans[chan] is None:
            chans[chan] = blank(chan)
        chans[chan]["spend"] += num(row.get("ad_spend"))

    channels = sorted((c for c in chans.values() if c), key=lambda c: c["channel"])
    for i, c in enumerate(channels):
        light, dark = SLOTS[i % len(SLOTS)]
        c["color"] = light
        c["color_dark"] = dark

    week_list = []
    for monday in sorted(weeks):
        wk = weeks[monday]
        covered = (min(monday + dt.timedelta(days=6), last) - max(monday, first)).days + 1
        week_list.append({
            "start": monday.isoformat(),
            "days": covered,
            "by_channel": {ch: {"orders": v[0], "returns": v[1], "kept": round(v[2], 2)}
                           for ch, v in wk["by_channel"].items()},
        })

    return {
        "meta": {
            "first_day": first.isoformat(),
            "last_day": last.isoformat(),
            "span_days": span_days,
            "weeks": round(span_days / 7.0, 4),
            "orders_rows": len(orders),
            "skipped_rows": skipped,
            "spend_undated": spend_undated,
            "spend_outside": spend_outside,
            "has_customers": bool(cust_orders),
            "built_at": dt.datetime.now().strftime("%Y-%m-%d %H:%M"),
            "source": os.path.abspath(data_dir),
        },
        "channels": [{k: (round(v, 2) if isinstance(v, float) else v) for k, v in c.items()}
                     for c in channels],
        "weeks": week_list,
    }


HTML = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Returns &amp; Capacity — Monday Dashboard</title>
<style>
:root{
  color-scheme: light dark;
  --plane:#f9f9f7; --surface:#fcfcfb; --ink:#0b0b0b; --ink2:#52514e; --muted:#898781;
  --grid:#e1e0d9; --axis:#c3c2b7; --border:rgba(11,11,11,0.10);
  --good:#0ca30c; --warn:#fab219; --serious:#ec835a; --crit:#d03b3b; --goodtext:#006300;
  --wash:rgba(11,11,11,0.04);
__CSS_LIGHT__
}
@media (prefers-color-scheme: dark){
  :root:where(:not([data-theme="light"])){
    --plane:#0d0d0d; --surface:#1a1a19; --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781;
    --grid:#2c2c2a; --axis:#383835; --border:rgba(255,255,255,0.10);
    --goodtext:#0ca30c; --wash:rgba(255,255,255,0.06);
__CSS_DARK__
  }
}
*{box-sizing:border-box}
body{margin:0;background:var(--plane);color:var(--ink);
  font:14px/1.55 system-ui,-apple-system,"Segoe UI",sans-serif;
  -webkit-font-smoothing:antialiased}
.wrap{max-width:1180px;margin:0 auto;padding:28px 20px 64px}
h1{font-size:24px;line-height:1.25;margin:0 0 6px;letter-spacing:-0.01em}
h2{font-size:12px;letter-spacing:.09em;text-transform:uppercase;color:var(--muted);
   margin:0 0 14px;font-weight:600}
h3{font-size:14px;margin:0 0 2px;font-weight:600}
p{margin:0 0 10px}
.sub{color:var(--ink2);font-size:13px}
.card{background:var(--surface);border:1px solid var(--border);border-radius:12px;padding:20px}
section{margin-top:34px}
.grid{display:grid;gap:14px}
.g2{grid-template-columns:1fr 1fr}
.g3{grid-template-columns:repeat(3,1fr)}
@media(max-width:860px){.g2,.g3{grid-template-columns:1fr}}

/* assumptions */
.assume{display:flex;flex-wrap:wrap;gap:10px 22px;align-items:flex-end;
  background:var(--surface);border:1px solid var(--border);border-radius:12px;padding:14px 18px;
  position:sticky;top:0;z-index:20}
.field{display:flex;flex-direction:column;gap:3px}
.field label{font-size:11px;letter-spacing:.05em;text-transform:uppercase;color:var(--muted);font-weight:600}
.field input{width:96px;padding:6px 8px;font:inherit;font-variant-numeric:tabular-nums;
  color:var(--ink);background:var(--plane);border:1px solid var(--axis);border-radius:7px}
.field input:focus{outline:2px solid var(--ink);outline-offset:1px}
.assume .note{font-size:12px;color:var(--muted);margin-left:auto;max-width:270px;text-align:right}
button.reset{font:inherit;font-size:12px;padding:6px 12px;border-radius:7px;cursor:pointer;
  border:1px solid var(--axis);background:var(--plane);color:var(--ink2)}
button.reset:hover{background:var(--wash)}

/* hero */
.hero{display:flex;flex-wrap:wrap;gap:26px;align-items:flex-start}
.heronum{font-size:60px;line-height:1;font-weight:650;letter-spacing:-0.03em}
.herolab{font-size:13px;color:var(--ink2);margin-top:8px;max-width:290px}
.tiles{display:grid;grid-template-columns:repeat(2,minmax(150px,1fr));gap:12px;flex:1;min-width:320px}
@media(max-width:560px){.tiles{grid-template-columns:1fr}}
.tile{border:1px solid var(--border);border-radius:10px;padding:12px 14px;background:var(--plane)}
.tile .v{font-size:22px;font-weight:620;letter-spacing:-0.01em}
.tile .k{font-size:11px;letter-spacing:.05em;text-transform:uppercase;color:var(--muted);
  font-weight:600;margin-bottom:5px}
.tile .h{font-size:12px;color:var(--ink2);margin-top:3px}

/* status chip */
.chip{display:inline-flex;align-items:center;gap:6px;font-size:12px;font-weight:600;
  padding:3px 10px 3px 8px;border-radius:999px;border:1px solid var(--border);background:var(--plane)}
.chip .dot{width:8px;height:8px;border-radius:50%;flex:none}
.chip.critical .dot{background:var(--crit)} .chip.serious .dot{background:var(--serious)}
.chip.warning .dot{background:var(--warn)} .chip.good .dot{background:var(--good)}

/* table */
table{width:100%;border-collapse:collapse;font-variant-numeric:tabular-nums;font-size:13px}
th,td{padding:9px 10px;text-align:right;border-bottom:1px solid var(--grid);white-space:nowrap}
th{font-size:11px;letter-spacing:.04em;text-transform:uppercase;color:var(--muted);
  font-weight:600;vertical-align:bottom;border-bottom:1px solid var(--axis)}
th:first-child,td:first-child{text-align:left}
tbody tr:hover{background:var(--wash)}
tfoot td{font-weight:650;border-bottom:none;border-top:1px solid var(--axis)}
.swatch{display:inline-block;width:9px;height:9px;border-radius:2px;margin-right:8px;vertical-align:baseline}
.scroll{overflow-x:auto}
.neg{color:var(--crit)}

/* charts */
.chart{width:100%;display:block;overflow:visible}
.legend{display:flex;flex-wrap:wrap;gap:6px 16px;margin:2px 0 12px;font-size:12px;color:var(--ink2)}
.legend span{display:inline-flex;align-items:center;gap:6px}
.legend i{width:9px;height:9px;border-radius:2px;display:inline-block}
#tip{position:fixed;pointer-events:none;opacity:0;transition:opacity .1s;z-index:100;
  background:var(--surface);border:1px solid var(--border);border-radius:8px;padding:8px 10px;
  font-size:12px;line-height:1.45;box-shadow:0 6px 22px rgba(0,0,0,.16);max-width:250px}
#tip b{font-weight:650}
.callout{border-left:3px solid var(--crit);padding:2px 0 2px 14px;margin:14px 0}
.callout.ok{border-left-color:var(--good)}
.callout.warn{border-left-color:var(--warn)}
.foot{margin-top:38px;padding-top:18px;border-top:1px solid var(--border);
  font-size:12.5px;color:var(--ink2)}
.foot ul{margin:8px 0 0;padding-left:18px} .foot li{margin-bottom:5px}
code{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:12px;
  background:var(--wash);padding:1.5px 5px;border-radius:4px}
</style>
</head>
<body>
<div id="tip" role="status" aria-live="polite"></div>
<div class="wrap">

<header>
  <h1>Returns &amp; capacity by channel</h1>
  <p class="sub" id="window"></p>
</header>

<div class="assume" id="assume">
  <div class="field"><label for="mins">Min / return</label><input id="mins" type="number" min="1" max="240" step="1" value="40"></div>
  <div class="field"><label for="agents">CS people</label><input id="agents" type="number" min="1" max="50" step="1" value="2"></div>
  <div class="field"><label for="hrs">Hrs each / wk</label><input id="hrs" type="number" min="1" max="80" step="1" value="40"></div>
  <div class="field"><label for="wage">CS $ / hr</label><input id="wage" type="number" min="0" max="500" step="0.5" value="22"></div>
  <button class="reset" id="reset" type="button">Reset</button>
  <div class="note">Change any number and every figure below re-reads. Wage is an assumption — set yours.</div>
</div>

<section>
  <h2>1 · How much of the team is left</h2>
  <div class="card">
    <div class="hero">
      <div>
        <div class="heronum" id="utilNum"></div>
        <div class="herolab" id="utilLab"></div>
        <div style="margin-top:12px" id="utilChip"></div>
      </div>
      <div class="tiles" id="capTiles"></div>
    </div>
    <div style="margin-top:24px">
      <h3>Where those hours go</h3>
      <p class="sub" style="margin-bottom:12px">Return-handling hours per week, stacked against the hours you have.</p>
      <svg id="capBar" class="chart" height="132" role="img" aria-label="Return-handling hours per week by channel against team capacity"></svg>
    </div>
  </div>
</section>

<section>
  <h2>2 · Every channel, money and hours side by side</h2>
  <div class="card">
    <div class="scroll"><table id="board">
      <thead><tr>
        <th>Channel</th><th>Orders<br>/wk</th><th>Kept rev<br>/wk</th><th>Ad spend<br>/wk</th>
        <th>Return<br>rate</th><th>Returns<br>/wk</th><th>CS hrs<br>/wk</th><th>% of<br>team</th>
        <th>Refunded<br>/wk</th><th>Discounts<br>/wk</th><th>CS hrs per<br>$1k kept</th>
        <th>Contribution<br>/wk</th><th>Contrib per<br>CS hr</th>
      </tr></thead>
      <tbody></tbody><tfoot></tfoot>
    </table></div>
    <p class="sub" style="margin:14px 0 0;font-size:12.5px">
      Contribution = kept revenue &minus; ad spend &minus; return-handling labour. It does
      <b>not</b> subtract cost of goods, shipping or platform fees — those aren't in the export,
      so treat these as channel <i>rankings</i>, not profit.
    </p>
  </div>
</section>

<section>
  <h2>3 · The channel quietly eating the most</h2>
  <div class="card">
    <div id="flagCallout"></div>
    <div class="grid g2" style="margin-top:20px">
      <div>
        <h3>Return rate — with and without a discount code</h3>
        <p class="sub" style="margin-bottom:8px" id="codeNote"></p>
        <div class="legend"><span><i style="background:var(--ink2)"></i>No code</span><span><i style="background:var(--ink2);opacity:.45"></i>With code</span></div>
        <svg id="rateBar" class="chart" role="img" aria-label="Return rate by channel, split by whether a discount code was used"></svg>
      </div>
      <div>
        <h3>CS hours burned per $1,000 of kept revenue</h3>
        <p class="sub" style="margin-bottom:8px">Lower is a channel that pays for itself in your team's time.</p>
        <svg id="effBar" class="chart" role="img" aria-label="CS hours per one thousand dollars of kept revenue by channel"></svg>
      </div>
    </div>
  </div>
</section>

<section>
  <h2>4 · What you can still afford to grow</h2>
  <div class="card">
    <p class="sub" style="margin-bottom:16px" id="growIntro"></p>
    <div class="grid g2">
      <div>
        <h3>Extra orders per week you could absorb</h3>
        <p class="sub" style="margin-bottom:8px">Before someone goes into overtime, if all the growth came from one channel.</p>
        <svg id="growBar" class="chart" role="img" aria-label="Additional orders per week each channel could absorb within spare capacity"></svg>
      </div>
      <div>
        <h3>Contribution per CS hour it consumes</h3>
        <p class="sub" style="margin-bottom:8px">What an hour of your team's time is worth in each channel.</p>
        <svg id="cphBar" class="chart" role="img" aria-label="Contribution per CS hour by channel"></svg>
      </div>
    </div>
    <div id="quality" style="margin-top:24px">
      <h3>What each channel actually brings you</h3>
      <p class="sub" style="margin-bottom:10px" id="qualityNote"></p>
      <div class="scroll"><table id="qualityTable">
        <thead><tr>
          <th>Channel</th><th>Customers<br>acquired</th><th>Come back<br>again</th>
          <th>Kept revenue per<br>customer acquired</th><th>Cost to<br>acquire one</th>
          <th>CS minutes<br>per order</th><th>Orders/wk<br>trend</th>
        </tr></thead><tbody></tbody>
      </table></div>
    </div>
    <div id="growCallout" style="margin-top:20px"></div>
  </div>
</section>

<section>
  <h2 id="sensHead">5 · Is the handling time really what's limiting you</h2>
  <div class="card">
    <div class="grid g2">
      <div>
        <h3>Hours per week vs. minutes per return</h3>
        <p class="sub" style="margin-bottom:8px">At today's return volume. The flat line is the hours you have.</p>
        <svg id="sensLine" class="chart" role="img" aria-label="Weekly return-handling hours as a function of minutes per return"></svg>
      </div>
      <div>
        <h3>Two levers, same week</h3>
        <div id="levers"></div>
      </div>
    </div>
    <div id="sensCallout"></div>
  </div>
</section>

<section>
  <h2>6 · Is this a bad month or the shape of the business</h2>
  <div class="card">
    <h3>Return-handling hours per week, by channel</h3>
    <p class="sub" style="margin-bottom:10px">Normalised to a full 7-day week. Hollow markers are partial weeks at the edges of the export.</p>
    <div class="legend" id="trendLegend"></div>
    <svg id="trendLine" class="chart" role="img" aria-label="Weekly return-handling hours by channel over time"></svg>
    <div id="trendCallout"></div>
  </div>
</section>

<div class="foot">
  <b>How to re-run this on Monday.</b> Drop the fresh <code>orders.csv</code> and
  <code>ad-spend.csv</code> into the data folder and run:
  <div style="margin:8px 0"><code id="cmd"></code></div>
  <ul>
    <li>Every figure is derived from the two CSVs — a longer window, a new channel, or a
        channel that stops running ads all flow through without editing anything.</li>
    <li>Rates are per-week, computed from the actual number of days in the export, so a
        partial week never inflates or deflates a weekly number.</li>
    <li><b>Not in the export, so not in the maths:</b> cost of goods, shipping, payment and
        platform fees, and any CS work that isn't a return — tickets, pre-sale questions,
        WISMO. Real headroom is smaller than the number above, never larger.</li>
    <li id="builtNote"></li>
  </ul>
</div>

</div>
<script>
const DATA = __DATA__;
</script>
<script>
__JS__
</script>
</body>
</html>
"""


JS = r"""
'use strict';
const $ = s => document.querySelector(s);
const M = DATA.meta, WKS = M.weeks;
const TIP = $('#tip');

const money = v => (v < 0 ? '−$' : '$') + Math.round(Math.abs(v)).toLocaleString();
const pct = (v, d=1) => (v*100).toFixed(d) + '%';
const n1 = v => v.toFixed(1);
const dateFmt = s => new Date(s+'T00:00:00').toLocaleDateString(undefined,{month:'short',day:'numeric',year:'numeric'});

function inputs(){
  const g = (id, dflt) => { const v = parseFloat($(id).value); return (isFinite(v) && v > 0) || (v === 0 && id === '#wage') ? v : dflt; };
  return { mins:g('#mins',40), agents:g('#agents',2), hrs:g('#hrs',40), wage:g('#wage',22) };
}

function compute(){
  const I = inputs();
  const capacity = I.agents * I.hrs;
  const rows = DATA.channels.map((c,i) => {
    const rate = c.orders ? c.returns / c.orders : 0;
    const hrsWk = c.returns * I.mins / 60 / WKS;
    const keptWk = c.kept / WKS, spendWk = c.spend / WKS;
    const contribWk = keptWk - spendWk - hrsWk * I.wage;
    return {
      ...c, i, rate, hrsWk, keptWk, spendWk, contribWk,
      ordersWk: c.orders / WKS, returnsWk: c.returns / WKS,
      refundWk: c.refunded / WKS, discWk: c.discount / WKS,
      hrsPer1k: keptWk > 0 ? hrsWk/(keptWk/1000) : (hrsWk > 0 ? Infinity : 0),
      repeatRate: c.customers ? c.repeat_customers / c.customers : null,
      ltv: c.customers ? c.cohort_kept / c.customers : null,
      cac: c.customers && c.spend > 0 ? c.spend / c.customers : null,
      contribPerHr: hrsWk > 0 ? contribWk / hrsWk : null,
      minsPerOrder: rate * I.mins
    };
  });
  const used = rows.reduce((a,r) => a + r.hrsWk, 0);
  const returnsWk = rows.reduce((a,r) => a + r.returnsWk, 0);
  const free = capacity - used;
  const T = {
    ordersWk: rows.reduce((a,r)=>a+r.ordersWk,0), keptWk: rows.reduce((a,r)=>a+r.keptWk,0),
    spendWk: rows.reduce((a,r)=>a+r.spendWk,0), refundWk: rows.reduce((a,r)=>a+r.refundWk,0),
    discWk: rows.reduce((a,r)=>a+r.discWk,0), contribWk: rows.reduce((a,r)=>a+r.contribWk,0),
    returns: rows.reduce((a,r)=>a+r.returns,0), orders: rows.reduce((a,r)=>a+r.orders,0)
  };
  rows.forEach(r => {
    r.headroom = free <= 0 ? 0 : (r.minsPerOrder > 0 ? free*60/r.minsPerOrder : Infinity);
    r.momentum = momentum(r.channel);
  });
  // channels big enough to judge: at least 5% of orders
  const solid = rows.filter(r => r.orders >= 0.05 * T.orders && r.orders > 0);
  const worst = (solid.length ? solid : rows).slice().sort((a,b) => b.hrsWk - a.hrsWk)[0];
  const best  = (solid.length ? solid : rows).slice().sort((a,b) => a.rate - b.rate)[0];
  return { I, capacity, rows, used, free, returnsWk, T,
           util: capacity > 0 ? used/capacity : 0,
           breakEven: returnsWk > 0 ? capacity*60/returnsWk : Infinity,
           worst, best };
}

/* Order-volume drift across the FULL weeks of the export: mean of the later half
   against the mean of the earlier half. Null until there are 4 full weeks to compare. */
function momentum(chan){
  const full = DATA.weeks.filter(w => w.days >= 7);
  if (full.length < 4) return null;
  const v = full.map(w => (w.by_channel[chan] || {orders:0}).orders);
  const h = Math.floor(v.length/2);
  const early = v.slice(0, h).reduce((a,b)=>a+b,0)/h;
  const late  = v.slice(-h).reduce((a,b)=>a+b,0)/h;
  return early > 0 ? late/early - 1 : null;
}

/* ---------- svg helpers ---------- */
const esc = s => String(s).replace(/[&<>"']/g,
  c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const label = c => c.replace(/_/g,' ');
function svgSize(el, h){ el.setAttribute('height', h); return { w: el.clientWidth || el.parentNode.clientWidth || 520, h }; }
function paint(el, h, inner){ const s = svgSize(el, h); el.innerHTML = inner(s.w, s.h); wireTips(el); return s; }
function wireTips(el){
  el.querySelectorAll('[data-tip]').forEach(node => {
    node.style.cursor = 'default';
    node.addEventListener('mousemove', e => {
      TIP.innerHTML = node.getAttribute('data-tip');
      TIP.style.opacity = 1;
      const r = TIP.getBoundingClientRect();
      TIP.style.left = Math.min(e.clientX + 14, window.innerWidth - r.width - 10) + 'px';
      TIP.style.top  = Math.max(8, e.clientY - r.height - 12) + 'px';
    });
    node.addEventListener('mouseleave', () => { TIP.style.opacity = 0; });
  });
}
/** Horizontal bars: items = [{name,value,color,text,tip,alt?}] ; alt = second (ghost) value */
function hbars(el, items, opts){
  const o = Object.assign({ pad:120, rowH:30, barH:13, fmt:v=>n1(v) }, opts||{});
  const grouped = items.some(i => i.alt !== undefined);
  const rowH = grouped ? o.rowH + 12 : o.rowH;
  const h = items.length * rowH + 10;
  paint(el, h, (w) => {
    const maxV = Math.max(1e-9, ...items.map(i => Math.max(i.value, i.alt ?? 0)));
    const minV = Math.min(0, ...items.map(i => i.value));
    const x0 = o.pad, plot = Math.max(40, w - o.pad - 68);
    const span = maxV - minV || 1;
    const xz = x0 + (0 - minV)/span * plot;                 // zero position
    const px = v => x0 + (v - minV)/span * plot;
    let s = '';
    if (minV < 0) s += `<line x1="${xz}" y1="2" x2="${xz}" y2="${h-8}" stroke="var(--axis)" stroke-width="1"/>`;
    items.forEach((it, k) => {
      const yTop = k*rowH + 6;
      const bars = grouped ? [{v:it.value,op:1,t:it.text,tip:it.tip},{v:it.alt,op:.45,t:it.altText,tip:it.altTip}]
                           : [{v:it.value,op:1,t:it.text,tip:it.tip}];
      s += `<text x="${x0-10}" y="${yTop + (grouped?13:o.barH-2)}" text-anchor="end" font-size="12.5"
              fill="var(--ink)">${esc(label(it.name))}</text>`;
      bars.forEach((b, bi) => {
        const y = yTop + bi*(o.barH+4);
        const a = Math.min(px(b.v), xz), bb = Math.max(px(b.v), xz);
        const wd = Math.max(1.5, bb-a);
        s += `<rect x="${a}" y="${y}" width="${wd}" height="${o.barH}" rx="4" fill="${it.color}"
                opacity="${b.op}" data-tip="${esc(b.tip||'')}"/>`;
        s += `<text x="${bb+8}" y="${y+o.barH-2}" font-size="12" fill="var(--ink2)"
                font-variant-numeric="tabular-nums">${esc(b.t ?? o.fmt(b.v))}</text>`;
      });
    });
    return s;
  });
}
/** Line chart: series = [{name,color,pts:[{x,y,tip,hollow?}]}] */
function lines(el, series, opts){
  const o = Object.assign({ h:230, yLab:'', xLab:'', rule:null, ruleText:'', marks:[], xTicks:null, yMin:0 }, opts||{});
  paint(el, o.h, (w,h) => {
    const L=52, R=(series.some(se=>se.direct) ? 80 : 14), Tp=(o.yLab?28:14), B=34;
    const dots = series.every(s => s.pts.length <= 14);
    const pw = Math.max(40, w-L-R), ph = h-Tp-B;
    const xs = series.flatMap(s=>s.pts.map(p=>p.x)), ys = series.flatMap(s=>s.pts.map(p=>p.y));
    const xmin=Math.min(...xs), xmax=Math.max(...xs);
    let ymax = Math.max(...ys, o.rule ?? 0) * 1.12 || 1;
    const ymin = o.yMin;
    const X = v => L + (xmax===xmin ? pw/2 : (v-xmin)/(xmax-xmin)*pw);
    const Y = v => Tp + ph - (v-ymin)/(ymax-ymin || 1)*ph;
    let s = '';
    const ticks = 4;
    for (let i=0;i<=ticks;i++){
      const v = ymin + (ymax-ymin)*i/ticks, y = Y(v);
      s += `<line x1="${L}" y1="${y}" x2="${L+pw}" y2="${y}" stroke="var(--grid)" stroke-width="1"/>`;
      s += `<text x="${L-9}" y="${y+4}" text-anchor="end" font-size="11" fill="var(--muted)"
             font-variant-numeric="tabular-nums">${Math.round(v)}</text>`;
    }
    (o.xTicks || []).forEach(t => {
      s += `<text x="${X(t.x)}" y="${Tp+ph+18}" text-anchor="middle" font-size="11" fill="var(--muted)">${esc(t.t)}</text>`;
    });
    if (o.xLab) s += `<text x="${L+pw/2}" y="${h-2}" text-anchor="middle" font-size="11" fill="var(--muted)">${esc(o.xLab)}</text>`;
    if (o.yLab) s += `<text x="0" y="11" font-size="11" fill="var(--muted)">${esc(o.yLab)}</text>`;
    if (o.rule !== null && o.rule <= ymax){
      const y = Y(o.rule);
      s += `<line x1="${L}" y1="${y}" x2="${L+pw}" y2="${y}" stroke="var(--crit)" stroke-width="2"/>`;
      s += `<text x="${L+4}" y="${y-7}" font-size="11.5" font-weight="600"
             fill="var(--crit)">${esc(o.ruleText)}</text>`;
    }
    const used = [];
    series.forEach(se => {
      const d = se.pts.map((p,i)=>(i?'L':'M')+X(p.x)+' '+Y(p.y)).join(' ');
      s += `<path d="${d}" fill="none" stroke="${se.color}" stroke-width="2"
              stroke-linejoin="round" stroke-linecap="round"/>`;
      se.pts.forEach(p => {
        if (dots || p.hollow)
          s += `<circle cx="${X(p.x)}" cy="${Y(p.y)}" r="4.5" fill="${p.hollow?'var(--surface)':se.color}"
                  stroke="${p.hollow?se.color:'var(--surface)'}" stroke-width="2" data-tip="${esc(p.tip||'')}"/>`;
        s += `<circle cx="${X(p.x)}" cy="${Y(p.y)}" r="${dots?11:7}" fill="transparent" data-tip="${esc(p.tip||'')}"/>`;
      });
      const last = se.pts[se.pts.length-1];
      if (se.direct){
        let ly = Y(last.y) + 4;
        while (used.some(u => Math.abs(u - ly) < 13)) ly += 13;   // avoid label collisions
        used.push(ly);
        s += `<text x="${X(last.x)+9}" y="${ly}" font-size="11.5" fill="var(--ink2)">${esc(label(se.name))}</text>`;
      }
    });
    (o.marks||[]).forEach((mk, mi) => {
      const mx = X(mk.x), ly = Tp + 11 + mi*16;
      const flip = mx > L + pw*0.62;   // keep the label inside the plot near the right edge
      s += `<line x1="${mx}" y1="${Tp}" x2="${mx}" y2="${Tp+ph}" stroke="${mk.color}" stroke-width="1.5"/>`;
      s += `<circle cx="${mx}" cy="${Y(mk.y)}" r="5" fill="${mk.color}" stroke="var(--surface)" stroke-width="2"/>`;
      s += `<text x="${mx + (flip?-7:7)}" y="${ly}" text-anchor="${flip?'end':'start'}" font-size="11.5"
              font-weight="600" fill="${mk.color}">${esc(mk.t)}</text>`;
    });
    return s;
  });
}
"""

JS += r"""
/* ---------- render ---------- */
function render(){
  const S = compute(), I = S.I;

  /* 1 · capacity */
  $('#utilNum').textContent = pct(S.util, 0);
  $('#utilNum').style.color = S.util >= 1 ? 'var(--crit)' : S.util >= 0.85 ? 'var(--serious)' : 'var(--ink)';
  $('#utilLab').innerHTML = `of your ${n1(S.capacity)}-hour week is spent handling returns —
    <b>before</b> a single other ticket, question or phone call.`;
  const state = S.util >= 1 ? ['critical','Already over — this is overtime']
              : S.util >= 0.85 ? ['serious','No slack — one bad week is overtime']
              : S.util >= 0.7 ? ['warning','Tight but standing']
              : ['good','Comfortable'];
  $('#utilChip').innerHTML = `<span class="chip ${state[0]}"><i class="dot"></i>${state[1]}</span>`;

  $('#capTiles').innerHTML = [
    ['Returns / week', Math.round(S.returnsWk).toLocaleString(), `${S.T.returns.toLocaleString()} across the window`],
    ['Hours on returns', n1(S.used) + ' h', `at ${I.mins} min each`],
    ['Hours left / week', (S.free < 0 ? '−' : '') + n1(Math.abs(S.free)) + ' h',
      S.free < 0 ? 'overtime already' : `${n1(S.free/I.agents)} h per person`],
    ['Cost of that time', money(S.used * I.wage) + ' /wk', `at $${I.wage}/hr`]
  ].map(t => `<div class="tile"><div class="k">${t[0]}</div><div class="v">${t[1]}</div><div class="h">${t[2]}</div></div>`).join('');

  const cap = $('#capBar');
  paint(cap, 150, (w) => {
    const L=0, pw=w-2, top=16, bh=42;
    const scale = Math.max(S.capacity, S.used) * 1.06;
    const X = v => L + v/scale*pw;
    let s = `<rect x="${L}" y="${top}" width="${X(S.capacity)}" height="${bh}" rx="6"
               fill="var(--wash)" stroke="var(--axis)" stroke-width="1"/>`;
    let acc = 0;
    S.rows.slice().sort((a,b)=>a.i-b.i).forEach(r => {
      if (r.hrsWk <= 0) return;
      const x = X(acc), wd = Math.max(0, X(acc + r.hrsWk) - x - 2);
      s += `<rect x="${x}" y="${top}" width="${wd}" height="${bh}" rx="4" fill="${r.color}"
              data-tip="${esc(`<b>${esc(label(r.channel))}</b><br>${n1(r.hrsWk)} h/wk · ${pct(r.hrsWk/S.capacity,0)} of the team<br>${Math.round(r.returnsWk)} returns/wk`)}"/>`;
      if (wd > 54) s += `<text x="${x+wd/2}" y="${top+bh/2+4}" text-anchor="middle" font-size="12"
              font-weight="600" fill="#fff" style="paint-order:stroke" >${n1(r.hrsWk)} h</text>`;
      acc += r.hrsWk;
    });
    const cx = X(S.capacity);
    s += `<line x1="${cx}" y1="${top-8}" x2="${cx}" y2="${top+bh+8}" stroke="var(--crit)" stroke-width="2"/>`;
    s += `<text x="${cx-6}" y="${top-12}" text-anchor="end" font-size="11.5" font-weight="600"
            fill="var(--crit)">capacity ${n1(S.capacity)} h</text>`;
    if (S.free > 0)
      s += `<text x="${(cx + X(S.used))/2}" y="${top+bh+17}" text-anchor="middle" font-size="11.5"
              fill="var(--muted)">${n1(S.free)} h free</text>`;
    let lx = 0;
    s += S.rows.slice().sort((a,b)=>a.i-b.i).map(r => {
      const t = `<g transform="translate(${lx},${top+bh+40})"><rect width="9" height="9" y="-8" rx="2" fill="${r.color}"/>
        <text x="14" y="0" font-size="12" fill="var(--ink2)">${esc(label(r.channel))} · ${n1(r.hrsWk)} h</text></g>`;
      lx += 42 + (label(r.channel).length * 6.6) + 34;
      return t;
    }).join('');
    return s;
  });

  /* 2 · scoreboard */
  const sorted = S.rows.slice().sort((a,b) => b.hrsWk - a.hrsWk);
  $('#board tbody').innerHTML = sorted.map(r => `<tr>
    <td><span class="swatch" style="background:${r.color}"></span>${esc(label(r.channel))}</td>
    <td>${Math.round(r.ordersWk)}</td><td>${money(r.keptWk)}</td>
    <td>${r.spendWk > 0 ? money(r.spendWk) : '—'}</td>
    <td>${pct(r.rate)}</td><td>${Math.round(r.returnsWk)}</td>
    <td><b>${n1(r.hrsWk)}</b></td><td>${pct(r.hrsWk/S.capacity,0)}</td>
    <td>${money(r.refundWk)}</td><td>${money(r.discWk)}</td>
    <td>${isFinite(r.hrsPer1k) ? n1(r.hrsPer1k) : '\u2014'}</td>
    <td class="${r.contribWk<0?'neg':''}">${money(r.contribWk)}</td>
    <td class="${r.contribPerHr!==null&&r.contribPerHr<0?'neg':''}">${r.contribPerHr===null?'—':money(r.contribPerHr)}</td>
  </tr>`).join('');
  $('#board tfoot').innerHTML = `<tr>
    <td>All channels</td><td>${Math.round(S.T.ordersWk)}</td><td>${money(S.T.keptWk)}</td>
    <td>${money(S.T.spendWk)}</td><td>${pct(S.T.orders?S.T.returns/S.T.orders:0)}</td>
    <td>${Math.round(S.returnsWk)}</td><td>${n1(S.used)}</td><td>${pct(S.util,0)}</td>
    <td>${money(S.T.refundWk)}</td><td>${money(S.T.discWk)}</td>
    <td>${S.T.keptWk>0 ? n1(S.used/(S.T.keptWk/1000)) : '\u2014'}</td>
    <td class="${S.T.contribWk<0?'neg':''}">${money(S.T.contribWk)}</td>
    <td>${money(S.used>0?S.T.contribWk/S.used:0)}</td></tr>`;

  /* 3 · the flag */
  const W = S.worst, B = S.best;
  const noReturns = S.T.returns === 0;
  const onlyOne = W.channel === B.channel;
  const rateNo  = W.orders_nocode ? W.returns_nocode/W.orders_nocode : null;
  const rateYes = W.orders_code   ? W.returns_code/W.orders_code     : null;
  const comparable = rateNo !== null && rateYes !== null;
  const discountIsCause = comparable && (rateYes - rateNo) > 0.06;
  $('#flagCallout').innerHTML = noReturns ? `
    <span class="chip good"><i class="dot"></i>No returns in this export</span>
    <h3 style="margin:12px 0 6px;font-size:17px">Nothing in this file is consuming return-handling time</h3>
    <p class="sub">Either the window is genuinely clean, or <code>was_returned</code> isn't being populated
      in the export. Worth checking before trusting the capacity figure above.</p>`
    : onlyOne ? `
    <span class="chip warning"><i class="dot"></i>Only one channel to judge</span>
    <h3 style="margin:12px 0 6px;font-size:17px">${esc(label(W.channel))} carries all
      ${n1(W.hrsWk)} hours a week</h3>
    <p class="sub">It returns at <b>${pct(W.rate)}</b>, costing ${money(W.refundWk)} of refunded revenue a week.
      With no second channel at meaningful volume there's nothing to benchmark it against — the comparison
      below fills in once another channel is running.</p>`
    : `
    <span class="chip critical"><i class="dot"></i>Biggest hidden cost</span>
    <h3 style="margin:12px 0 6px;font-size:17px">${esc(label(W.channel))} is eating
      ${pct(W.hrsWk/S.capacity,0)} of your customer-service team</h3>
    <p class="sub">It returns at <b>${pct(W.rate)}</b> against ${esc(label(B.channel))}'s ${pct(B.rate)}.
      That is <b>${n1(W.hrsWk)} hours a week</b> — roughly
      ${n1(W.hrsWk/I.hrs)} of your ${I.agents} people — plus <b>${money(W.refundWk)}</b> of revenue
      handed back every week and <b>${money(W.discWk)}</b> in discounts.
      ${W.spendWk <= 0
        ? `It costs you nothing in ad spend, so the entire bill arrives as your team's hours.`
        : W.spendWk >= Math.max(...S.rows.map(r=>r.spendWk))
        ? `On the invoice it looks like your biggest ad channel; the real bill arrives as your team's hours.`
        : `On the invoice it is just another ad line; the real bill arrives as your team's hours.`}</p>
    <p class="sub">${!comparable
      ? `${esc(label(W.channel))} ${W.orders_code ? 'puts a discount code on every order' : 'never uses a discount code'},
         so there is no within-channel comparison to make — this export can't pin its return rate on discounting
         either way.`
      : discountIsCause
      ? `Its discount codes look implicated: coded orders return at ${pct(rateYes)} vs ${pct(rateNo)} without one.`
      : `<b>And it isn't the discounting.</b> ${esc(label(W.channel))} orders with no code at all return at
         ${pct(rateNo)} — versus ${pct(rateYes)} with one. The traffic itself is the problem, so pulling the
         codes would save the ${money(W.discWk)}/wk of discount but leave the hours untouched.`}</p>`;
  $('#codeNote').textContent = !comparable
    ? 'A channel with no orders on one side of the split has nothing to compare — read those rows as one number.'
    : discountIsCause
    ? 'Where the two bars diverge, the discount is pulling in returning buyers.'
    : 'Two bars at the same height mean the discount code is not what is causing returns.';

  hbars($('#rateBar'), sorted.map(r => ({
    name: r.channel, color: r.color,
    value: r.orders_nocode ? r.returns_nocode/r.orders_nocode : 0,
    alt:   r.orders_code   ? r.returns_code/r.orders_code     : 0,
    text:  pct(r.orders_nocode ? r.returns_nocode/r.orders_nocode : 0, 0),
    altText: pct(r.orders_code ? r.returns_code/r.orders_code : 0, 0),
    tip: `<b>${esc(label(r.channel))}</b> — no code<br>${r.returns_nocode} of ${r.orders_nocode} orders returned`,
    altTip: `<b>${esc(label(r.channel))}</b> — with a code<br>${r.returns_code} of ${r.orders_code} orders returned`
  })), { pad:110 });

  const effRows = S.rows.slice().sort((a,b) =>
    (isFinite(a.hrsPer1k)?a.hrsPer1k:1e18) - (isFinite(b.hrsPer1k)?b.hrsPer1k:1e18));
  const effMax = Math.max(1e-9, ...effRows.filter(r=>isFinite(r.hrsPer1k)).map(r=>r.hrsPer1k));
  hbars($('#effBar'), effRows.map(r => ({
    name: r.channel, color: r.color,
    value: isFinite(r.hrsPer1k) ? r.hrsPer1k : effMax,
    text: isFinite(r.hrsPer1k) ? n1(r.hrsPer1k)+' h' : 'no kept revenue',
    tip: `<b>${esc(label(r.channel))}</b><br>${n1(r.hrsWk)} h/wk on ${money(r.keptWk)} kept revenue<br>`
       + (isFinite(r.hrsPer1k) ? `${n1(r.hrsPer1k)} hours per $1,000`
                               : 'every order came back \u2014 no kept revenue to divide into')
  })), { pad:110, rowH:34 });

  /* 4 · growth */
  const growable = S.rows.slice().filter(r => r.ordersWk > 0)
    .sort((a,b) => a.minsPerOrder - b.minsPerOrder);   // cheapest in CS minutes first, capacity or not
  $('#growIntro').innerHTML = S.free > 0
    ? `You have <b>${n1(S.free)} spare hours a week</b>. Every extra order costs you return-handling
       minutes at that channel's own return rate, so the same spare hour buys very different amounts
       of growth depending on where you spend it.`
    : `You have <b>no spare hours</b> — you are ${n1(-S.free)} hours past capacity. Nothing is growable
       until returns come down or you add a person; the bars below show what would open up at zero.`;
  const capBarMax = Math.max(1, ...growable.map(r => isFinite(r.headroom) ? r.headroom : 0));
  hbars($('#growBar'), growable.map(r => ({
    name: r.channel, color: r.color, value: isFinite(r.headroom) ? r.headroom : capBarMax,
    text: isFinite(r.headroom) ? Math.round(r.headroom) + ' orders' : 'no return load',
    tip: `<b>${esc(label(r.channel))}</b><br>${n1(r.minsPerOrder)} min of CS per order placed
          <br>(${pct(r.rate)} return rate × ${I.mins} min)<br>${n1(Math.max(S.free,0))} spare h \u00f7 that =
          ${isFinite(r.headroom) ? Math.round(r.headroom)+' orders/wk' : 'no CS limit'}`
  })), { pad:110, rowH:34 });
  hbars($('#cphBar'), S.rows.slice().filter(r=>r.contribPerHr!==null).sort((a,b)=>b.contribPerHr-a.contribPerHr).map(r => ({
    name: r.channel, color: r.color, value: r.contribPerHr, text: money(r.contribPerHr),
    tip: `<b>${esc(label(r.channel))}</b><br>${money(r.contribWk)} contribution ÷ ${n1(r.hrsWk)} CS hours`
  })), { pad:110, rowH:34 });
  const top = growable[0], hi = S.rows.slice().sort((a,b)=>(b.contribPerHr??-1e9)-(a.contribPerHr??-1e9))[0];
  const wkFull = DATA.weeks.filter(w => w.days >= 7).length;
  if (!M.has_customers){
    $('#quality').style.display = 'none';
  } else {
    $('#quality').style.display = '';
    $('#qualityNote').innerHTML = `Customers are credited to the channel that <b>first</b> brought them in,
      and everything they have spent since is credited there too. Over a
      ${(M.span_days/7).toFixed(1)}-week window this understates repeat rate for every channel equally —
      read it as a ranking, not a lifetime value.` +
      (wkFull >= 4 ? '' : ` Trend needs 4 full weeks; this export has ${wkFull}.`);
    const trend = r => r.momentum === null ? '—'
      : `<span style="color:${r.momentum > 0.05 ? 'var(--goodtext)' : r.momentum < -0.05 ? 'var(--crit)' : 'var(--ink2)'}">`
        + (r.momentum > 0 ? '+' : '') + pct(r.momentum, 0) + '</span>';
    $('#qualityTable tbody').innerHTML = S.rows.slice()
      .sort((a,b) => (b.ltv ?? -1) - (a.ltv ?? -1)).map(r => `<tr>
        <td><span class="swatch" style="background:${r.color}"></span>${esc(label(r.channel))}</td>
        <td>${r.customers.toLocaleString()}</td>
        <td>${r.repeatRate === null ? '—' : pct(r.repeatRate)}</td>
        <td>${r.ltv === null ? '—' : money(r.ltv)}</td>
        <td>${r.cac === null ? '—' : money(r.cac)}</td>
        <td>${n1(r.minsPerOrder)}</td>
        <td>${trend(r)}</td></tr>`).join('');
  }

  const ratio = top.minsPerOrder > 0 ? W.minsPerOrder/top.minsPerOrder : Infinity;
  const rising = S.rows.filter(r => r.momentum !== null && r.momentum > 0.1 && r.channel !== W.channel)
                       .sort((a,b) => b.momentum - a.momentum)[0];
  const bestLtv = S.rows.filter(r => r.ltv !== null).sort((a,b) => b.ltv - a.ltv)[0];
  const hr = r => isFinite(r.headroom) ? Math.round(r.headroom).toLocaleString() + ' orders/wk'
                                       : 'no CS limit';
  $('#growCallout').innerHTML = noReturns
    ? `<div class="callout ok"><p class="sub" style="margin:0">
       <b>Nothing is competing for CS time in this window,</b> so every channel is equally growable on
       hours. Rank them on contribution per CS hour once the export contains returns.</p></div>`
    : (top.channel === W.channel)
    ? `<div class="callout warn"><p class="sub" style="margin:0">
       <b>${esc(label(top.channel))} is both your cheapest and your most expensive channel in hours</b> —
       there is only one channel carrying real volume here, so there is no reallocation to make.
       Your spare ${n1(Math.max(S.free,0))} hours buys ${hr(top)} before overtime.</p></div>`
    : `<div class="callout ok"><p class="sub" style="margin:0">
       <b>Grow ${esc(label(top.channel))} first.</b> An order there costs
       ${n1(top.minsPerOrder)} minutes of your team against ${esc(label(W.channel))}'s ${n1(W.minsPerOrder)} —
       ${isFinite(ratio) ? n1(ratio)+'\u00d7 cheaper in hours' : 'free in hours'}${
         hi.channel===top.channel ? `, and it also returns the most contribution per CS hour (${money(hi.contribPerHr)})` :
         `. ${esc(label(hi.channel))} returns the most contribution per CS hour (${money(hi.contribPerHr)}), so split growth between them`}.
       Your spare ${n1(Math.max(S.free,0))} hours buys ${hr(top)} of ${esc(label(top.channel))},
       against ${hr(W)} of ${esc(label(W.channel))}.
       ${bestLtv && bestLtv.channel === top.channel
         ? `It also brings back the best customers — ${money(bestLtv.ltv)} of kept revenue per customer
            acquired, against ${esc(label(W.channel))}'s ${W.ltv === null ? 'n/a' : money(W.ltv)}.`
         : bestLtv ? `Watch one thing though: ${esc(label(bestLtv.channel))} brings the most valuable
            customers (${money(bestLtv.ltv)} each vs ${esc(label(top.channel))}'s
            ${top.ltv === null ? 'unknown — those orders carry no customer id' : money(top.ltv)}).` : ''}
       ${rising ? `<br><br><b>And ${esc(label(rising.channel))} is the one actually compounding</b> —
         orders are ${pct(rising.momentum,0)} up across the full weeks of this export
         ${rising.channel === top.channel ? '' : `while ${esc(label(top.channel))} is
           ${top.momentum === null ? 'not comparable across this window'
             : Math.abs(top.momentum) < 0.05 ? 'flat'
             : (top.momentum > 0 ? 'up ' : 'down ') + pct(Math.abs(top.momentum),0)}`}.
         It costs ${n1(rising.minsPerOrder)} CS minutes an order, so your spare hours would absorb
         ${hr(rising)} of it — worth funding alongside ${esc(label(top.channel))}.` : ''}
       </p></div>`;


  /* 5 · is it the 40 minutes */
  const pts = [];
  for (let t = 5; t <= Math.max(60, I.mins + 15); t += 1) pts.push({ x:t, y:S.returnsWk*t/60,
    tip:`<b>${t} min per return</b><br>${n1(S.returnsWk*t/60)} h/wk · ${pct(S.returnsWk*t/60/S.capacity,0)} of the team` });
  const marks = [{ x:I.mins, y:S.used, color:'var(--ink)', t:`today ${I.mins} min` }];
  if (isFinite(S.breakEven) && S.breakEven >= 5 && S.breakEven <= Math.max(60, I.mins+15))
    marks.push({ x:S.breakEven, y:S.capacity, color:'var(--crit)', t:`overtime at ${n1(S.breakEven)} min` });
  lines($('#sensLine'), [{ name:'hours', color:'var(--ink)', pts }],
    { h:250, rule:S.capacity, ruleText:`${n1(S.capacity)} h available`, marks,
      xLab:'minutes spent handling one return', yLab:'CS hours / week',
      xTicks:[10,20,30,40,50,60].filter(v=>v<=Math.max(60,I.mins+15)).map(v=>({x:v,t:v+'m'})) });

  // A proportional cut scales with whatever handling time is set; a fixed 10 minutes
  // is a rounding error at 240 min/return and most of the job at 15.
  const shave = Math.max(1, Math.round(I.mins * 0.25));
  const leverA = S.returnsWk * shave / 60;
  const excess = Math.max(0, W.returns - W.orders * B.rate);
  const leverB = excess * I.mins / 60 / WKS;
  const cashB = W.returns > 0 ? (W.refunded / W.returns) * excess / WKS : 0;
  $('#levers').innerHTML = (noReturns || onlyOne) ? `
    <div class="tile"><div class="k">Not applicable yet</div>
    <div class="h" style="margin-top:6px">${noReturns
      ? 'No returns in this window, so neither lever has anything to pull on.'
      : 'Only one channel at meaningful volume — there is no cleaner channel to benchmark a target rate against. Lever A (faster handling) would free ' + n1(leverA) + ' h/wk.'}</div></div>` : `
    <div class="tile" style="margin-bottom:10px">
      <div class="k">Lever A · faster handling</div>
      <div class="v">${n1(leverA)} h/wk</div>
      <div class="h">Cut handling time by a quarter (${I.mins} → ${I.mins-shave} min per return).
        Frees time, returns no money.</div></div>
    <div class="tile">
      <div class="k">Lever B · fewer returns</div>
      <div class="v">${n1(leverB)} h/wk</div>
      <div class="h">Bring ${esc(label(W.channel))} from ${pct(W.rate)} down to
        ${esc(label(B.channel))}'s ${pct(B.rate)} — about ${Math.round(excess/WKS)} fewer returns a week.
        Also stops refunding <b>${money(cashB)}</b> a week.</div></div>`;

  $('#sensHead').textContent = `5 · Is the ${I.mins} minutes really what's limiting you`;

  const slack = S.breakEven - I.mins;
  if (noReturns){
    $('#sensCallout').innerHTML = `<div class="callout ok"><p class="sub" style="margin:0">
      <b>Returns aren't your constraint in this export — there are none.</b> Handling time can't be
      what limits you when nothing is being handled, so the ${I.mins}-minute figure has nothing to act on
      here. Re-run against a window that contains returns.</p></div>`;
  } else {
    // Three honest states, read off the numbers rather than asserted.
    const tight = slack > 0 && slack < I.mins * 0.25;
    const opener = S.used > S.capacity
      ? `<b>At ${I.mins} minutes a return you are past the line, not near it.</b> Returns alone need
         ${n1(S.used)} h against the ${n1(S.capacity)} h you have — that gap is overtime every week,
         and it costs ${money((S.used - S.capacity) * I.wage)} a week on top of the wage bill.`
      : tight
      ? `<b>The ${I.mins} minutes is what makes this fragile, not what makes it expensive.</b>
         Your break-even is <b>${n1(S.breakEven)} minutes</b> per return, so you are ${n1(slack)}
         minute${slack < 2 ? '' : 's'} from paying overtime — any slowdown, a sick day, a returns spike,
         puts you over that week.`
      : `<b>Handling time is not what is binding you right now.</b> Break-even is
         ${n1(S.breakEven)} minutes a return and you are at ${I.mins}, so there is genuine room in the
         process before overtime — returns are using ${pct(S.util,0)} of the team.`;
    const compare = leverB >= leverA
      ? `The volume lever is still the bigger one: fixing ${esc(label(W.channel))}'s return rate frees
         <b>${n1(leverB)} h/wk</b> against <b>${n1(leverA)} h/wk</b> from cutting handling time by a
         quarter — and it hands back ${money(cashB)} a week in refunds that a faster process never
         recovers. Work the return rate first; treat process time as the safety margin.`
      : `At ${I.mins} min a return, process time is the dominant term — cutting it by a quarter frees
         <b>${n1(leverA)} h/wk</b> against <b>${n1(leverB)} h/wk</b> from fixing
         ${esc(label(W.channel))}'s rate. Work the process first, but note the ${money(cashB)}/wk of
         refunds only comes back via the return rate.`;
    $('#sensCallout').innerHTML = `<div class="callout ${S.used > S.capacity ? '' : tight ? 'warn' : 'ok'}">
      <p class="sub" style="margin:0">${opener} ${compare}</p></div>`;
  }

  /* 6 · trend */
  const wks = DATA.weeks;
  const series = S.rows.slice().sort((a,b)=>a.i-b.i).map(r => ({
    name: r.channel, color: r.color, direct: true,
    pts: wks.map((wk,ix) => {
      const d = wk.by_channel[r.channel] || { orders:0, returns:0 };
      const norm = 7 / Math.max(1, wk.days);
      return { x:ix, y:d.returns * norm * I.mins / 60, hollow: wk.days < 7,
        tip:`<b>${esc(label(r.channel))}</b> · week of ${dateFmt(wk.start)}
             <br>${d.returns} returns in ${wk.days} day${wk.days===1?'':'s'}
             <br>${n1(d.returns*norm*I.mins/60)} h per full week
             ${wk.days<7?'<br><i>partial week — scaled to 7 days</i>':''}` };
    })
  }));
  $('#trendLegend').innerHTML = series.map(s =>
    `<span><i style="background:${s.color}"></i>${esc(label(s.name))}</span>`).join('');
  lines($('#trendLine'), series, { h:250, yLab:'CS hours / week',
    xTicks: wks.map((wk,ix)=>({x:ix,t:dateFmt(wk.start).replace(/,.*/,'')}))
              .filter((_,ix)=>wks.length<=8||ix%2===0) });

  const full = wks.filter(w => w.days >= 7);
  let trendMsg;
  if (full.length >= 3){
    const rate = w => { const d = w.by_channel[W.channel]||{orders:0,returns:0};
                        return d.orders ? d.returns/d.orders : null; };
    const rs = full.map(rate).filter(v => v !== null);
    const half = Math.floor(rs.length/2);
    const early = rs.slice(0,half).reduce((a,b)=>a+b,0)/Math.max(1,half);
    const late  = rs.slice(-half).reduce((a,b)=>a+b,0)/Math.max(1,half);
    const drift = late - early;
    trendMsg = Math.abs(drift) < 0.03
      ? `<b>It's the shape of the business, not a bad month.</b> ${esc(label(W.channel))} has returned at
         ${pct(W.rate)} in every full week of this export — it does not spike and settle, so waiting it out
         costs you ${n1(W.hrsWk)} hours a week indefinitely.`
      : `<b>${esc(label(W.channel))}'s return rate is ${drift>0?'getting worse':'improving'}</b> —
         ${pct(early)} in the earlier full weeks against ${pct(late)} in the later ones.
         ${drift>0?'The hours bill is growing; act before it does.':'Whatever changed is working — keep going.'}`;
  } else {
    trendMsg = `Only ${full.length} full week${full.length===1?'':'s'} in this export — not enough to call a
                trend. Re-run once you have four or more.`;
  }
  $('#trendCallout').innerHTML = `<div class="callout warn" style="margin-top:16px">
    <p class="sub" style="margin:0">${trendMsg}</p></div>`;
}

/* ---------- boot ---------- */
$('#window').innerHTML = `${dateFmt(M.first_day)} – ${dateFmt(M.last_day)} ·
  <b>${M.span_days} days</b> (${(M.span_days/7).toFixed(1)} weeks) · ${M.orders_rows.toLocaleString()} orders
  ${M.skipped_rows ? ` · <span style="color:var(--serious)">${M.skipped_rows} rows skipped (unreadable date)</span>` : ''}`;
$('#cmd').textContent = 'python3 build_dashboard.py ' + M.source;
$('#builtNote').textContent = 'Built ' + M.built_at + ' from ' + M.source + '.';
['#mins','#agents','#hrs','#wage'].forEach(id => $(id).addEventListener('input', render));
$('#reset').addEventListener('click', () => {
  $('#mins').value = 40; $('#agents').value = 2; $('#hrs').value = 40; $('#wage').value = 22; render();
});
let rt; addEventListener('resize', () => { clearTimeout(rt); rt = setTimeout(render, 120); });
render();
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("data_dir", nargs="?", default="sample-data")
    ap.add_argument("-o", "--out", default="dashboard.html")
    args = ap.parse_args()

    payload = aggregate(args.data_dir)

    light, dark = [], []
    for i, c in enumerate(payload["channels"]):
        light.append(f"  --series-{i+1}:{c['color']};")
        dark.append(f"    --series-{i+1}:{c['color_dark']};")
        c["color"] = f"var(--series-{i+1})"
        c.pop("color_dark")
    if not light:
        light, dark = ["  --series-1:#2a78d6;"], ["    --series-1:#3987e5;"]

    html = (HTML
            .replace("__CSS_LIGHT__", "\n".join(light))
            .replace("__CSS_DARK__", "\n".join(dark))
            .replace("__DATA__", json.dumps(payload, separators=(",", ":"))
                     .replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026"))
            .replace("__JS__", JS))

    with open(args.out, "w", encoding="utf-8") as fh:
        fh.write(html)

    m = payload["meta"]
    print(f"wrote {args.out}  ({len(html)//1024} KB)")
    print(f"  {m['orders_rows']} orders · {m['first_day']} to {m['last_day']} "
          f"({m['span_days']} days) · {len(payload['channels'])} channels")
    if m["skipped_rows"]:
        print(f"  warning: {m['skipped_rows']} order rows skipped (unreadable order_date)")
    if m["spend_undated"]:
        print(f"  warning: {m['spend_undated']} ad-spend rows skipped (unreadable date)")
    if m["spend_outside"]:
        print(f"  warning: {m['spend_outside']} ad-spend rows fall outside the orders window "
              f"({m['first_day']}..{m['last_day']}) and were excluded")


if __name__ == "__main__":
    main()
