#!/usr/bin/env python3
"""Visitors needed per variant for an A/B test on a conversion rate.

Uses the normal approximation for a two-sided test of two proportions.
Standard library only (Python 3.8+).

Usage (from the skill folder):
  python3 scripts/sample_size.py --baseline 0.03 --lift 0.20
  python3 scripts/sample_size.py --baseline 0.03 --lift 0.10,0.20,0.30 --weekly-visitors 2500

--baseline   current conversion rate as a fraction (0.03 = 3%)
--lift       smallest relative change worth detecting (0.20 = +20%);
             several values separated by commas print one block each
--alpha      false-positive rate, two-sided (default 0.05)
--power      chance of detecting the lift if it is real (default 0.80)
--weekly-visitors  eligible visitors per week across all variants (optional).
             Sessions are an acceptable stand-in if visitors aren't available.
--variants   number of variants including control (default 2). Each variant is
             compared with control at the same alpha, with no correction for
             multiple comparisons, so treat a 3-way test's winner with care.
"""
import argparse
import math
import sys
from statistics import NormalDist


def visitors_per_variant(baseline, lift, alpha=0.05, power=0.80):
    p1 = baseline
    p2 = baseline * (1 + lift)
    if not 0 < p1 < 1 or not 0 < p2 < 1:
        raise ValueError(
            f"rates must stay between 0 and 1 (baseline {p1:.4f}, with lift {p2:.4f})"
        )
    z_alpha = NormalDist().inv_cdf(1 - alpha / 2)
    z_power = NormalDist().inv_cdf(power)
    p_bar = (p1 + p2) / 2
    top = (z_alpha * math.sqrt(2 * p_bar * (1 - p_bar))
           + z_power * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2
    return math.ceil(top / (p2 - p1) ** 2)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--baseline", type=float, required=True)
    ap.add_argument("--lift", type=str, required=True)
    ap.add_argument("--alpha", type=float, default=0.05)
    ap.add_argument("--power", type=float, default=0.80)
    ap.add_argument("--weekly-visitors", type=float)
    ap.add_argument("--variants", type=int, default=2)
    a = ap.parse_args()

    def fail(msg):
        print(f"Error: {msg}", file=sys.stderr)
        sys.exit(2)

    try:
        lifts = [float(x) for x in a.lift.split(",") if x.strip()]
    except ValueError:
        fail("--lift takes numbers, for example 0.2 or 0.1,0.2,0.3")
    if not 0 < a.baseline < 1:
        fail("--baseline is a fraction between 0 and 1 (3% is 0.03)")
    if not lifts or any(l <= 0 or l >= 5 for l in lifts):
        fail("--lift is a positive fraction below 5 (a 20% lift is 0.20). "
             "Size tests for the lift you hope to see, not for a drop.")
    if not 0 < a.alpha < 1 or not 0 < a.power < 1:
        fail("--alpha and --power are fractions between 0 and 1")
    if a.variants < 2:
        fail("a test needs at least 2 variants (control plus one)")
    if a.weekly_visitors is not None and a.weekly_visitors <= 0:
        fail("--weekly-visitors must be above 0")

    for i, lift in enumerate(lifts):
        try:
            n = visitors_per_variant(a.baseline, lift, a.alpha, a.power)
        except ValueError as e:
            fail(str(e))
        total = n * a.variants
        if i:
            print()
        print(f"Baseline {a.baseline:.2%}, detecting {a.baseline * (1 + lift):.2%} "
              f"({lift:+.0%} relative), alpha {a.alpha}, power {a.power:.0%}")
        print(f"Visitors per variant: {n:,}")
        print(f"Total visitors ({a.variants} variants): {total:,}")
        print(f"Conversions expected in control: about {math.ceil(n * a.baseline):,}")
        if a.weekly_visitors:
            weeks = math.ceil(total / a.weekly_visitors)
            print(f"Whole weeks at {a.weekly_visitors:,.0f} eligible visitors a week: {weeks}")
            if weeks > 6:
                print("Over 6 weeks: don't run this as an A/B test. Ship clear fixes and "
                      "compare before and after, or test a bigger change.")
            elif weeks < 2:
                print("Under 2 weeks: still run for 2 full weeks so every day of the week is covered.")


if __name__ == "__main__":
    main()
