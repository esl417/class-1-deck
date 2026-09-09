#!/usr/bin/env python3
"""
Generates the sample data for the dashboard lightning lesson.

WHAT THIS DATA IS FOR
---------------------
The demo is not a puzzle. The point is a DECISION SURFACE built around one
owner's constraint -- something no generic dashboard can know, and therefore
something no generic dashboard shows.

The owner supplies this in the prompt, and nowhere else:

    "I have 2 customer service people, paid hourly. I need them under
     40 hours a week each -- overtime is where my margin goes. Start to
     finish, a return takes us about 40 minutes: the email, the label,
     inspecting it, restocking, the refund, the follow-up. Tell me
     whether that is what's limiting me, and what it'd be worth to get
     it down."

That turns returns-handling from a cost adjustment into a HARD CEILING, and a
ceiling reorders decisions in a way a per-customer cost never does. At ~$2.69
per customer, returns change nothing. At 80 hours a week with 74.5 already
spoken for, they decide which channel you are allowed to grow.

WARNING -- THE BLOCK BELOW IS THE *DESIGN TARGET*, NOT WHAT THIS FILE EMITS.
The generator has never hit it. The deck was written from these aspirational
figures and, until 2026-09-08, taught numbers the data does not contain. If you
need the real figures, run `verify_deck_claims.py`, which computes them from
orders.csv. Treat orders.csv as the source of truth and this docstring as
intent.

Design target (NOT ACHIEVED):

    112 returns/week  x  40 min  =  74.5 hrs/wk  against an 80-hr ceiling
    paid_search 64% of load; grow it 20% -> 84.0 hrs OVERTIME

What the file ACTUALLY produces (verified, and what the deck now teaches):

    88.3 returns/week x  40 min  =  58.9 hrs/wk  =  74% of the 80-hr ceiling
    paid_search is 67% of that load (39.5 hrs)

    13.5 min of CS time per paid_search order
     2.3 min                per email order        -- a 5.8x asymmetry
    paid_search can grow 54% before overtime; email 378%

The demo still works, and arguably lands better: the channel every surface
metric says to fund (most customers, cheapest CAC at $9.79) is the one that
costs nearly six times the team time per order, and the only one that cannot
grow far. It is an asymmetry rather than a cliff.

TWO LEVERS, NOT ONE VERDICT
---------------------------
(The per-lever hour deltas below were computed against the unachieved 74.5-hr
baseline; the shape holds but the figures do not. Re-derive before quoting.)

The ceiling is not a wall, it is a price. Minutes-per-return is a number the
owner can CHANGE, not just report, and the screen should price both levers:

    cut 40 -> 35 min/return       +9.3 hrs/wk   fast, fully theirs
    cut 40 -> 30 min/return      +18.6 hrs/wk   fast, real process work
    halve paid_search returns    +23.8 hrs/wk   slow (listings, sizing)
    shift growth to email         +9.5 hrs/wk   slow, compounds via retention

And the two levers interact, which is the whole point:

    at 40 min: grow paid_search 20% -> 84.0 hrs   OVERTIME
    at 35 min: grow paid_search 20% -> 73.5 hrs   affordable

Five minutes off a return converts "you cannot grow paid_search" into "you
can". That is what makes this a decision surface rather than a verdict: the
owner is not told what to do, they are shown what each option costs. It also
answers the owner who refuses to stop funding their growth engine -- fine,
here is the exact process improvement that buys you the right to.

The verdict sentence the screen should support:

    "You are at 93% of CS capacity and 64% of it is paid_search returns.
     Either grow email instead, or take 5 minutes out of your return
     process and paid_search becomes affordable again. Both are real."

The resulting screen answers a question no tool ships:

    You have 80 CS hours a week and returns are consuming ~74 of them.
    The channel your dashboard calls cheapest puts you into overtime in
    about five weeks -- and its customers do not come back anyway. The
    channel with the worse CAC is the one you can actually afford to grow.

Nothing is on fire. That is deliberate: the decision is "grow WHICH", not
"stop the bleeding", which is the harder and more realistic question.

  channel      | looks like            | retention says | capacity says
  -------------|-----------------------|----------------|--------------------
  paid_search  | BEST: most customers, | WORST: ~16%    | THE PROBLEM: growth
               | lowest CAC, top AOV   | ever reorder   | here breaks the
               |                       |                | ceiling first
  marketplace  | mediocre, worst CAC   | healthy, ~45%  | moderate
  email        | unremarkable          | BEST: ~70%     | cheap to serve, and
               |                       |                | safe to grow

Why no tool can ship it: not because the join is hard, but because team size,
hourly pay, and tolerance for overtime exist in the owner's head. Triple Whale
cannot know them at any price.

DESIGN RULES
------------
1. Discount codes appear on EVERY channel, at different rates, with several
   different codes. A discount code is not a channel tag.
2. The trap channel is paid search -- the channel owners are most confident
   about, not one folk wisdom already distrusts. The reveal overturns a belief.
   It is ALSO the returns problem, inverting the industry prior that says
   marketplace returns worst.
3. Average order value points the WRONG way too. The trap channel's first
   orders are genuinely bigger. Nothing leaks the answer early.
4. Nothing in orders.csv is a rate, a ratio, or a lifetime value. Repeat
   behaviour is latent: it exists only if you group by the channel of a
   customer's FIRST order and decide that matters.
5. The winning channel is not the smallest one, so "small = loyal" is not an
   available shortcut.
6. Returns are a plain 0/1 column, deliberately. The insight lives in the
   capacity model, not in finding the returns -- difficulty was never the
   goal, and a plain column keeps a live 4-minute build reliable.
7. Minutes-per-return, headcount and the 40-hour ceiling never appear in the
   file. They come from the prompt, so the owner creates the metric.
8. No metric hits exactly zero. Real churn decays, it does not cliff.
9. Return volume is tuned so total handling time lands near 74.5 hrs/week
   against an 80-hour ceiling -- close enough that growth forces the choice.
   The lever is minutes-per-return in the PROMPT, not the data: at 40 min the
   ceiling binds at 93%. If you change that figure in the deck, re-check the
   grow-20% test above, because the whole decision rests on it.
10. ~7% of customers buy again through a DIFFERENT channel than the one that
   acquired them. A perfect channel partition is the loudest synthetic tell
   there is, and first-touch cohorts still mean something at this rate.

Fixed seed, so every rehearsal produces identical numbers.
"""

import csv
import random
from datetime import date, timedelta
from pathlib import Path

SEED = 20260908

# The business is SIMULATED for HISTORY_DAYS so the growth curve, repeat
# purchases and customer base are those of an established shop. Only the final
# EXPORT_DAYS are written to CSV -- that is what an owner would actually hand
# you: a recent window out of a longer trading history.
#
# Keep these separate. Shortening the simulation instead of the export would
# compress six months of growth into six weeks and shrink the business itself:
# at HISTORY_DAYS=45 the file drops to ~2.5k rows with the wrong volumes.
#
# EXPORT_DAYS is a teaching-time knob. 13k rows (the old 180-day export) took
# too long to process live in a 45-minute class; 45 days is ~4.5k rows and
# still carries the whole story.
HISTORY_DAYS = 180
EXPORT_DAYS = 45
DAYS = HISTORY_DAYS          # simulation length (referenced throughout main)
OUT = Path(__file__).parent

# Shared across channels on purpose: a code tells you nothing about origin.
CODES = ["WELCOME10", "SPRING15", "SAVE20", "THANKYOU5"]

# ---------------------------------------------------------------------------
# Channel behaviour.
#
# return_rate is the quiet one, and it sits on PAID_SEARCH -- inverting the
# industry prior that says marketplace returns worst. The story is coherent:
# heavily-discounted impulse buyers who never come back are also the ones who
# send things back. Because paid_search is also the VOLUME channel, its return
# burden dominates the capacity model even at a per-customer rate that looks
# unremarkable next to a marketplace benchmark.
#
# Rates are tuned so total handling lands near 76 hrs/wk against an 80-hr
# ceiling (2 people x 40), with paid_search owning enough of it that growing
# that channel is what breaks the ceiling first.
# ---------------------------------------------------------------------------
CHANNELS = {
    "paid_search": {
        "new_per_day": (15, 23),         # the volume winner
        "daily_spend": (168.0, 224.0),   # and the cheapest per customer
        "first_order": (56.0, 96.0),     # and the biggest first order
        "discount_prob": 0.82,
        "discount_rate": (0.18, 0.30),
        "repeat_prob": 0.17,             # but they do not come back
        "repeat_orders": (1, 2),
        "repeat_value": (0.62, 0.88),
        "return_rate": 0.34,             # THE STING: discount buyers send it back
    },
    "marketplace": {
        "new_per_day": (9, 15),
        "daily_spend": (150.0, 205.0),   # worst CAC, so it looks mediocre
        "first_order": (41.0, 82.0),
        "discount_prob": 0.34,
        "discount_rate": (0.10, 0.20),
        "repeat_prob": 0.44,             # genuinely healthy retention
        "repeat_orders": (1, 3),
        "repeat_value": (0.92, 1.18),
        "return_rate": 0.115,            # moderate, and NOT the worst
    },
    "email": {
        "new_per_day": (8, 14),          # mid-sized, not the smallest
        "daily_spend": (120.0, 172.0),
        "first_order": (38.0, 74.0),     # unremarkable first orders
        "discount_prob": 0.30,
        "discount_rate": (0.05, 0.15),
        "repeat_prob": 0.68,             # they stay
        "repeat_orders": (2, 5),
        "repeat_value": (1.15, 1.55),    # and they grow
        "return_rate": 0.052,            # they keep what they buy
    },
    "organic": {
        "new_per_day": (4, 8),
        "daily_spend": (0.0, 0.0),       # no direct spend
        "first_order": (36.0, 79.0),
        "discount_prob": 0.22,
        "discount_rate": (0.05, 0.15),
        "repeat_prob": 0.47,
        "repeat_orders": (1, 3),
        "repeat_value": (0.98, 1.28),
        "return_rate": 0.078,
    },
}

WEEKEND_FACTOR = 0.74   # quieter Saturdays and Sundays
GROWTH = 0.42           # gentle growth, so trends look alive


def main() -> None:
    rng = random.Random(SEED)
    today = date.today()
    start = today - timedelta(days=DAYS)

    orders: list[dict] = []
    spend_rows: list[dict] = []
    customer_seq = 0

    for day_index in range(DAYS):
        day = start + timedelta(days=day_index)
        is_weekend = day.weekday() >= 5
        growth = 1.0 + GROWTH * (day_index / DAYS)
        season = WEEKEND_FACTOR if is_weekend else 1.0

        for channel, cfg in CHANNELS.items():
            # --- ad spend for the day (separate file, never on an order row) ---
            lo_s, hi_s = cfg["daily_spend"]
            if hi_s > 0:
                spend = rng.uniform(lo_s, hi_s) * growth * season
                spend_rows.append({
                    "date": day.isoformat(),
                    "channel": channel,
                    "ad_spend": f"{spend:.2f}",
                })

            lo, hi = cfg["new_per_day"]
            n_new = round(rng.uniform(lo, hi) * growth * season)

            for _ in range(n_new):
                customer_seq += 1
                customer_id = f"C-{customer_seq:05d}"

                gross = rng.uniform(*cfg["first_order"])
                if rng.random() < cfg["discount_prob"]:
                    code = rng.choice(CODES)
                    discount = gross * rng.uniform(*cfg["discount_rate"])
                else:
                    code = ""
                    discount = 0.0

                orders.append({
                    "order_date": day.isoformat(),
                    "customer_id": customer_id,
                    "channel": channel,
                    "discount_code": code,
                    "revenue": f"{gross - discount:.2f}",
                    "discount_amount": f"{discount:.2f}",
                    "was_returned": 1 if rng.random() < cfg["return_rate"] else 0,
                })

                # --- do they come back? latent in the rows, never a column ---
                if rng.random() >= cfg["repeat_prob"]:
                    continue

                n_repeat = rng.randint(*cfg["repeat_orders"])
                last = day
                for _ in range(n_repeat):
                    # Wide, decaying gaps: no hard ceiling, so nothing cliffs
                    # to exactly zero in any 30-day bucket.
                    gap = round(rng.triangular(9, 120, 34))
                    when = last + timedelta(days=gap)
                    if when >= today:
                        break
                    last = when

                    # Real attribution is messy: a customer acquired on one
                    # channel sometimes buys again through another. Keep it a
                    # minority so first-touch cohorts still mean something,
                    # but never zero -- a perfect channel partition across
                    # thousands of repeat orders is the loudest synthetic tell
                    # in the file.
                    if rng.random() < 0.22:
                        rch = rng.choice([c for c in CHANNELS if c != channel])
                    else:
                        rch = channel
                    rcfg = CHANNELS[rch]

                    value = rng.uniform(*cfg["first_order"]) * rng.uniform(*cfg["repeat_value"])
                    if rng.random() < 0.18:
                        rcode = rng.choice(CODES)
                        rdisc = value * rng.uniform(0.05, 0.15)
                    else:
                        rcode = ""
                        rdisc = 0.0

                    orders.append({
                        "order_date": when.isoformat(),
                        "customer_id": customer_id,
                        "channel": rch,
                        "discount_code": rcode,
                        "revenue": f"{value - rdisc:.2f}",
                        "discount_amount": f"{rdisc:.2f}",
                        # Returns follow the channel the order came through,
                        # not the one that first acquired the customer.
                        "was_returned": 1 if rng.random() < rcfg["return_rate"] else 0,
                    })

    # Shuffle within each day, then number, so ids run in true chronological
    # sequence and a day's rows are not grouped by channel.
    rng.shuffle(orders)
    orders.sort(key=lambda r: r["order_date"])

    # Leave gaps in order_id: real order tables have cancellations and test
    # rows removed, and a perfectly dense sequence is a synthetic tell.
    oid = 1000
    for o in orders:
        oid += rng.choice([1, 1, 1, 1, 2, 3])
        o["order_id"] = oid

    # Export only the most recent EXPORT_DAYS. Numbering happened above, across
    # the full history, so the export opens at a high order id and its customer
    # ids reference people who first bought before the window -- both true of a
    # real export, and neither affects any figure the deck quotes.
    export_start = (today - timedelta(days=EXPORT_DAYS)).isoformat()
    orders = [o for o in orders if o["order_date"] >= export_start]
    spend_rows = [s for s in spend_rows if s["date"] >= export_start]

    with (OUT / "orders.csv").open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=[
            "order_date", "order_id", "customer_id", "channel",
            "discount_code", "revenue", "discount_amount", "was_returned",
        ])
        w.writeheader()
        w.writerows(orders)

    with (OUT / "ad-spend.csv").open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["date", "channel", "ad_spend"])
        w.writeheader()
        w.writerows(spend_rows)

    print(f"orders.csv    {len(orders):,} rows")
    print(f"ad-spend.csv  {len(spend_rows):,} rows")
    print(f"window        {export_start} .. {today - timedelta(days=1)}"
          f"  ({EXPORT_DAYS} days exported of {HISTORY_DAYS} simulated)")
    print("Now run: python3 verify_deck_claims.py")


if __name__ == "__main__":
    main()
