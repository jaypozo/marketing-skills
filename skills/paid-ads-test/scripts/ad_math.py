#!/usr/bin/env python3
"""Break-even ad math for one product, service or job type.

Standard library only. All money in one currency. Run it once per job type
or product line when their margins or keyword costs differ.

Usage (from the skill folder):
  python3 scripts/ad_math.py --price 24 --variable-cost 1.02 --refund-rate 0.02 --cvr 0.022 --cpc 1.10
  python3 scripts/ad_math.py --price 89 --variable-cost 31.26 --cvr 0.06 --close-rate 0.55 --cpc 1.90

--price               what the customer pays per order or job (before sales tax)
--variable-cost       cost per order or job: product, materials, payment fees,
                      shipping, platform fees, and labor if it is paid per job
--refund-rate         share of orders refunded or redone for free (default 0)
--cvr                 click-to-sale rate, or for lead businesses click-to-lead rate
--close-rate          lead businesses only: share of leads that become paying jobs
--cpc                 expected cost per click for this keyword group (optional)
--extra-contribution  repeat or referral contribution you choose to count
                      within your payback window (default 0)
--target-conversions  paying conversions you want the test to produce (default 10)
"""
import argparse
import sys


def verdict(ratio):
    if ratio < 0.5:
        return ("NO-GO", "break-even CPC is under half the expected CPC. Raise order value "
                "or conversion first, or use another channel.")
    if ratio < 1.0:
        return ("MARGINAL", "test only the highest-intent exact and phrase terms, with a "
                "capped budget, after the landing page is fixed.")
    return ("TEST", "the numbers allow a bounded test.")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--price", type=float, required=True)
    ap.add_argument("--variable-cost", type=float, required=True)
    ap.add_argument("--refund-rate", type=float, default=0.0)
    ap.add_argument("--cvr", type=float, required=True)
    ap.add_argument("--close-rate", type=float, default=None)
    ap.add_argument("--cpc", type=float)
    ap.add_argument("--extra-contribution", type=float, default=0.0)
    ap.add_argument("--target-conversions", type=int, default=10)
    a = ap.parse_args()

    problems = []
    if a.price <= 0:
        problems.append("--price must be above 0")
    if a.variable_cost < 0:
        problems.append("--variable-cost can't be negative")
    if a.extra_contribution < 0:
        problems.append("--extra-contribution can't be negative")
    if not 0 <= a.refund_rate < 1:
        problems.append("--refund-rate is a fraction between 0 and 1 (2% is 0.02)")
    if not 0 < a.cvr < 1:
        problems.append("--cvr is a fraction between 0 and 1 (2% is 0.02)")
    if a.close_rate is not None and not 0 < a.close_rate <= 1:
        problems.append("--close-rate is a fraction between 0 and 1 (55% is 0.55)")
    if a.cpc is not None and a.cpc <= 0:
        problems.append("--cpc must be above 0")
    if a.target_conversions < 1:
        problems.append("--target-conversions must be at least 1")
    if problems:
        for p in problems:
            print(f"Error: {p}", file=sys.stderr)
        sys.exit(2)

    contribution = a.price * (1 - a.refund_rate) - a.variable_cost + a.extra_contribution
    if contribution <= 0:
        print(f"Contribution per sale is {contribution:.2f}. Each sale loses money before "
              "any ad spend, so paid ads can't work at this price.", file=sys.stderr)
        sys.exit(1)

    lead_mode = a.close_rate is not None
    sale_rate = a.cvr * (a.close_rate if lead_mode else 1.0)
    rows = [("Contribution per sale", f"{contribution:,.2f}"),
            ("Break-even cost per sale", f"{contribution:,.2f}")]
    if lead_mode:
        rows.append(("Break-even cost per lead", f"{contribution * a.close_rate:,.2f}"))
        rows.append(("Click to paying job", f"{sale_rate:.2%} ({a.cvr:.2%} x {a.close_rate:.0%})"))
    for label, rate in (("current rate", sale_rate), ("at 75% of rate", sale_rate * 0.75)):
        be_cpc = contribution * rate
        rows.append((f"Break-even CPC, {label}", f"{be_cpc:,.2f}"))
        if a.cpc:
            ratio = be_cpc / a.cpc
            name, _ = verdict(ratio)
            rows.append((f"Ratio to expected CPC, {label}", f"{ratio:.3f} {name}"))
    clicks = a.target_conversions / sale_rate
    rows.append((f"Clicks for {a.target_conversions} paying conversions", f"{clicks:,.0f} (at 75% of rate: {clicks / 0.75:,.0f})"))
    if a.cpc:
        rows.append(("Expected CPC", f"{a.cpc:,.2f}"))
        rows.append(("Budget for that many conversions", f"{clicks * a.cpc:,.2f} (at 75% of rate: {clicks / 0.75 * a.cpc:,.2f})"))

    width = max(len(r[0]) for r in rows) + 2
    for label, value in rows:
        print(f"{label + ':':<{width}}{value}")
    if a.cpc:
        name, text = verdict(contribution * sale_rate / a.cpc)
        print(f"Verdict at current rate: {name}: {text}")


if __name__ == "__main__":
    main()
