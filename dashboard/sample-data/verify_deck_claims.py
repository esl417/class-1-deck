#!/usr/bin/env python3
"""
Checks every numeric claim in the deck against orders.csv / ad-spend.csv.

The deck once carried a set of figures the data did not produce (112 returns/wk,
74.5 hrs, 93% of ceiling, "grow paid_search 20% -> overtime"). None of it was in
the file; a live build would have contradicted the slides on stage. This script
exists so that can't happen again quietly.

Run it after ANY change to generate.py, and after editing figures on a slide:

    python3 verify_deck_claims.py

Exits non-zero if a claim no longer matches. The data is the source of truth --
if this fails, fix the deck, not the assertion.
"""
import csv
import datetime
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).parent
CEILING_HOURS = 80          # 2 CS people x 40 hrs, owner-supplied in the prompt
MINUTES_PER_RETURN = 40     # owner-supplied in the prompt


def load():
    rows = list(csv.DictReader(open(HERE / "orders.csv")))
    ads = list(csv.DictReader(open(HERE / "ad-spend.csv")))
    dates = sorted(r["order_date"] for r in rows)
    d0 = datetime.date.fromisoformat(dates[0])
    d1 = datetime.date.fromisoformat(dates[-1])
    weeks = ((d1 - d0).days + 1) / 7
    return rows, ads, weeks


def metrics():
    rows, ads, weeks = load()
    orders, returns, customers = defaultdict(int), defaultdict(int), defaultdict(set)
    for r in rows:
        c = r["channel"]
        orders[c] += 1
        customers[c].add(r["customer_id"])
        if r["was_returned"] == "1":
            returns[c] += 1

    spend = defaultdict(float)
    for a in ads:
        spend[a["channel"]] += float(a["ad_spend"])

    total_returns = sum(returns.values())
    total_hours = total_returns * MINUTES_PER_RETURN / 60 / weeks
    headroom = CEILING_HOURS - total_hours

    def min_per_order(c):
        return returns[c] * MINUTES_PER_RETURN / orders[c]

    def growth_room(c):
        return headroom / (returns[c] * MINUTES_PER_RETURN / 60 / weeks) * 100

    return {
        "returns_per_week": total_returns / weeks,
        "total_hours": total_hours,
        "people_equivalent": total_hours / 40,   # 40-hr week per person
        "pct_of_ceiling": total_hours / CEILING_HOURS * 100,
        "paid_min_per_order": min_per_order("paid_search"),
        "email_min_per_order": min_per_order("email"),
        "ratio": min_per_order("paid_search") / min_per_order("email"),
        "paid_pct_of_load": returns["paid_search"] / total_returns * 100,
        "paid_growth_room": growth_room("paid_search"),
        "email_growth_room": growth_room("email"),
        "paid_return_rate": returns["paid_search"] / orders["paid_search"] * 100,
        "paid_cac": spend["paid_search"] / len(customers["paid_search"]),
        "email_cac": spend["email"] / len(customers["email"]),
        "paid_customers": len(customers["paid_search"]),
        "spare_hours": headroom,
        "email_extra_orders": headroom * 60 / min_per_order("email"),
        "paid_extra_orders": headroom * 60 / min_per_order("paid_search"),
        "hours_if_paid_up_20": (
            returns["paid_search"] * 1.2
            + sum(v for k, v in returns.items() if k != "paid_search")
        ) * MINUTES_PER_RETURN / 60 / weeks,
    }


# (label, key, value as printed in the deck, tolerance)
CLAIMS = [
    ("112 returns a week (slides 6, 7)",     "returns_per_week",    112,  1.0),
    ("74 hours a week (slides 6, 7, 8)",     "total_hours",         74,   0.6),
    ("93% of the ceiling (slides 7, 8)",     "pct_of_ceiling",      93,   0.6),
    ("just under two people (slide 6)",      "people_equivalent",   1.9,  0.06),
    ("13 min per paid-search order",         "paid_min_per_order",  13.0, 0.1),
    ("2.5 min per email order",              "email_min_per_order", 2.5,  0.1),
    ("5.2x asymmetry (the headline)",        "ratio",               5.2,  0.1),
    ("62% of returns load",                  "paid_pct_of_load",    62,   0.6),
    ("paid search can grow 12%",             "paid_growth_room",    12,   0.6),
    ("email can grow 64%",                   "email_growth_room",   64,   1.0),
    ("33% paid-search return rate",          "paid_return_rate",    33,   0.6),
    ("paid search has most customers",       "paid_customers",      1350, 2),
    ("grow paid search 20% -> overtime",     "hours_if_paid_up_20", 83.6, 0.2),
    ("5.6 spare hours (slide 8)",            "spare_hours",         5.6,  0.1),
    ("136 extra email orders (slide 8)",     "email_extra_orders",  136,  1.5),
    ("26 extra paid orders (slide 8)",       "paid_extra_orders",   26,   1.0),
]


def main():
    m = metrics()
    failures = []
    for label, key, claimed, tol in CLAIMS:
        actual = m[key]
        ok = abs(actual - claimed) <= tol
        print(f"{'OK  ' if ok else 'FAIL'} {label:<38} data={actual:>8.1f}  deck={claimed}")
        if not ok:
            failures.append((label, actual, claimed))

    print()
    if failures:
        print(f"{len(failures)} claim(s) no longer match the data.")
        print("The data is the source of truth: update the deck, not this file.")
        for label, actual, claimed in failures:
            print(f"  - {label}: deck says {claimed}, data says {actual:.1f}")
        return 1
    print("All deck claims verified against orders.csv.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
