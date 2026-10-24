# Sample size and low-traffic options

## Using the script

```bash
python3 scripts/sample_size.py --baseline 0.025 --lift 0.20 --weekly-visitors 3000
```

Run it from the skill's folder. It returns visitors per variant, total visitors and whole weeks needed, for a two-sided test at 5% significance and 80% power (the usual defaults). Pass several lifts at once, such as `--lift 0.2,0.3,0.5`, to see the trade-off. Use `--variants 3` for an A/B/C test. Each extra variant adds a full sample, and the script makes no correction for comparing several variants, so a 3-way winner needs more caution.

Inputs:

- Baseline: the current rate for the exact step being tested, measured over at least four recent weeks.
- Lift: the smallest relative change that would be worth the effort of shipping. Set it from the business case. A 10% lift on a page worth $2,000 a month isn't worth a two-month test.
- Weekly visitors: only visitors who would see the change. A checkout test counts people who reach checkout, not all site visitors.

## Rough sizes

Visitors per variant at 5% significance and 80% power:

| Baseline | +10% relative | +20% relative | +30% relative | +50% relative |
| --- | --- | --- | --- | --- |
| 1% | about 163,000 | about 43,000 | about 20,000 | about 7,800 |
| 3% | about 53,000 | about 14,000 | about 6,500 | about 2,500 |
| 5% | about 31,000 | about 8,200 | about 3,800 | about 1,500 |
| 10% | about 14,800 | about 3,800 | about 1,800 | about 700 |

Run the script for exact figures. Small lifts on small rates need more traffic than most small sites get.

## Rules while a test runs

- Fix the sample size and the end date before launch. Read the result once.
- Run whole weeks, with a minimum of two.
- Don't change the page, the traffic mix or the price during the test.
- Split traffic evenly and randomly per visitor, not per session.
- If the guardrail metric falls clearly while the test runs (revenue per visitor down, refunds up), stop and investigate. That's a safety stop, not a result.

## When there isn't enough traffic

Pick the first option that fits.

1. Fix defects and clear problems without testing.
2. Test a bigger change. A new offer, a different page structure or a different price presentation can move the rate enough to detect with a smaller sample.
3. Test higher in the funnel, where there are more events. For example, "added to cart" instead of "purchased". Treat that as a leading indicator and still watch purchases.
4. Before-and-after comparison: ship the change, then compare four equal weeks before and after, on the same days of the week. Note anything else that changed. Label the result directional.
5. Qualitative tests: watch five people from the target audience try the flow while thinking aloud. Nielsen Norman Group's research found five users turn up most of the obvious usability problems.

## Reading a finished test

- Report the observed rates, the difference and the confidence interval, not only "significant or not".
- A result that isn't significant means the test couldn't detect a lift of the planned size. It doesn't prove the change does nothing.
- Check the guardrails before calling a winner.
- Write the result in the test log, including losses and no-change results. They stop the same idea from being tested twice.
