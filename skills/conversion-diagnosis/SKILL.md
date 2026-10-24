---
name: conversion-diagnosis
description: Diagnoses why a page, checkout, signup or trial flow isn't converting, then writes a fix list and an experiment brief. Defines the outcome that matters and checks the tracking against real orders. Compares the funnel before and after any recent change, and finds where people drop off by step, device, browser and traffic source. Explains each drop with customer evidence and separates what to fix now from what to test. Every test gets a hypothesis, guardrail metrics, a sample size and a stop rule that fit the traffic. Use when someone says their conversion rate is low or dropped, the checkout or signup leaks, traffic isn't turning into sales or leads, or asks for CRO help, a funnel audit, an A/B test plan or test sizing. Use this before rewriting a page whose problem is unknown; to rewrite the copy, use landing-page-copy.
metadata:
  version: "1.1"
---

# Conversion diagnosis

Before proposing anything, find out which of four things is wrong. The tracking may be broken. Something may be broken or confusing at one step. The page may not earn trust. Or the traffic may not fit the offer. Measure success in revenue and qualified customers. Many small sites don't have the traffic for an A/B test. For them, the right move is to fix the clear defects and compare before and after.

## Ask the user first

Items 1 to 3 decide whether any rate can be trusted, so ask for those first. If the rest is missing, carry on, say what you assumed, and list it under "Needed" in the output.

1. The outcome that matters (purchases, qualified leads, booked calls, activated accounts) and what one is worth: average order value and margin, or the value of a lead.
2. Analytics exports for the last four to eight weeks: sessions and conversions by funnel step, device, browser and main traffic source.
3. Backend numbers for the same dates: orders or signups from the store, CRM or database.
4. Recent changes: redesigns, new themes, price changes, payment providers, new traffic sources, tracking changes. Ask for the same funnel for an equal period before any change.
5. Weekly traffic to the page or flow.
6. Customer evidence: support tickets, chats, survey answers, session recordings, reviews, and return or exchange reasons.
7. Whether they have a testing tool, and any sales or seasonal peaks coming up.

## Procedure

1. Define the conversion and its denominator in writing, for example "orders ÷ sessions that viewed a product page". Use the same denominator for every comparison. List the funnel steps.
2. Check the measurement with [references/tracking-checks.md](references/tracking-checks.md). First, compare analytics conversions with backend records for the same dates. If they differ by more than about 10%, fixing tracking is finding number one. Give the rate both ways (analytics, and backend orders ÷ analytics sessions), and say which you used for what. A gap usually sits at the last step, so it makes that step look worse than it is.
3. If the user named a change ("since the new theme"), compare the same funnel for equal periods before and after it. Check whether the change itself broke tracking, such as tags in the old theme that the new one dropped. If the change clearly caused the drop, list rolling it back, or testing old against new, as an option.
4. Build the funnel table: visitors at each step and the step-to-step rate, split by device. Add browser and traffic source where the data has them. To rank where to look, estimate recoverable value for each step: the gap between this segment's rate and a fair comparison (desktop for mobile, the period before the change, or the site's best segment), times the number of people who reach that step each month, times the share of them who would go on to buy, times the value of a conversion. Raw "people lost × order value" always points at the top of the funnel and isn't money anyone could recover.
5. Walk the path yourself on a real phone and a desktop, starting from the real traffic sources. If you can't, ask the user for a screen recording, or for answers to the walk-through list at the end of references/tracking-checks.md. Try the awkward cases: a discount code, an address abroad, a card decline, the back button, guest checkout, express pay buttons. Note every defect and every moment you hesitate.
6. Gather the reasons. Read the tickets and chats about the problem step. Watch 20 to 30 session recordings of people who dropped there, if they exist. If the user can add a one-question exit survey ("What's stopping you from [buying] today?"), suggest it for two weeks.
7. Sort what you found:
   - Tracking problems: fix first. Until they're fixed, every other number is suspect.
   - Defects: things that are broken or wrong. Fix them now, without a test.
   - Clarity problems: people don't understand the offer, the price or the next step.
   - Trust gaps: missing proof, unclear returns, surprise costs.
   - Fit problems: traffic that was never likely to buy.
8. Rank the clarity, trust and fit problems by evidence strength (data and customer words, or only one), the share of traffic affected, and effort.
9. For each top problem, decide whether to fix or test, using the traffic rule below. Related small fixes can be bundled into one test of a bigger change. Get the numbers with `python3 scripts/sample_size.py --baseline <rate> --lift <lift> --weekly-visitors <n>`, run from this skill's folder. It accepts several lifts at once (`--lift 0.2,0.3,0.5`). Read [references/sample-size.md](references/sample-size.md) for the method and the options when traffic is low.
10. Write an experiment brief for each test, and a short monitoring plan for each fix shipped without a test. Size tests on a baseline of at least four weeks measured after the defect fixes go live. If you size them before that, say the user should rerun the script once those four weeks are in.
11. Tell the user to keep a test log: what changed, the result (including no change) and what's still uncertain.

## Decision rules

- A higher conversion rate counts only if revenue per visitor or qualified leads also improve. For stores, make revenue per visitor a primary metric next to conversion rate.
- Measurement first. An analytics-to-backend gap above about 10% means tracking gets fixed before anything else. A common cause is a payment or booking step on another domain, where buyers come back as referral traffic.
- Device gap: if the phone rate is under half the desktop rate for the same traffic source, look for a mobile usability problem first. Split by browser too. Bugs that affect only one browser hide inside "mobile".
- When to test: if a test needs more than six weeks of traffic, don't run it. Ship clear improvements and compare equal periods before and after, or test a bigger change. If it needs less than two weeks, still run two full weeks, so every day of the week is covered.
- Set the smallest lift worth detecting from the business case. At a 3% baseline, a 20% relative lift takes about 14,000 visitors per variant to detect.
- Fix the sample size before launch, and read the result once, when it's reached. The only early stop is a safety stop: a guardrail falling clearly (revenue per visitor down, refunds up).
- Every test watches at least one number that could get worse: revenue per visitor, average order value, refund rate or lead quality.
- Keep tests out of big sales periods (Black Friday, a brand's own sale) unless the test is about that period, because traffic and intent shift during them.
- Sessions are an acceptable stand-in for visitors in the sizing. Testing tools split by visitor, so the real sample will be a bit smaller.

## Output

```markdown
# Conversion diagnosis: [site or flow], [date range]

Outcome: [definition, denominator, value per conversion]
Tracking check: [pass / gap of x%], rate by analytics [x%] and by backend [y%]
Before vs after [change]: [rates for equal periods], if a change was named

## Funnel
| Step | Visitors (mobile / desktop) | Step rate (mobile / desktop) | Comparison rate | Recoverable value per month |

## Findings, ranked
1. [Problem] - [kind] - evidence: [data] + [customer words] - affects [share] of traffic

## Fix now (tracking and defects)
| Issue | Where | How to reproduce | Owner (role if no name) |

## Experiment briefs
### Test 1: [name]
Hypothesis: Because we saw [evidence], we believe [change] for [segment] will raise [primary metric].
Primary metrics: ...   Guardrails: ...
Smallest lift worth detecting: ...   Visitors per variant: ...   Weeks: ...   Dates: ...
Stop rule: read once at [n] per variant, no earlier than [date]; safety stop if [guardrail].
QA before launch: [devices, browsers, tracking]

## Not testing, and why
## Monitoring plan for fixes shipped without a test
## Needed from the user
```

## Example

A coffee subscription shop has 9,000 sessions a month and 160 subscription orders, a 1.78% rate. Analytics showed 151 orders against the store's 160, a gap within 6%, so tracking passes. Phones bring 70% of sessions but convert at 1.1%, against 3.4% on desktop.

Findings:

1. Defect. On phones, the grind selector sits below a sticky "Subscribe" bar. Tapping Subscribe without a grind shows an error at the top of the page, off screen. It appears in 9 of 25 recordings, and in support emails saying "the button doesn't work". Fix now.
2. Trust gap. Eleven support tickets in eight weeks ask whether the subscription can be paused. The answer (pause or skip any time) appears only in the FAQ.

The user wanted to test a new pricing table. At a 1.78% baseline, detecting a 25% relative lift needs about 15,600 visitors per variant: 15 weeks at about 2,080 visitors a week. So, no A/B test. Ship the grind fix and a "Pause or skip any time" line under the price. Compare four weeks after with four weeks before, on orders and revenue per visitor, and label the result directional.

## Final check

- [ ] The conversion, its denominator and its value are written down.
- [ ] Analytics were compared with backend records. Any gap is finding number one, and both rates are shown.
- [ ] Any change the user named was checked with equal before and after periods, including whether it broke tracking.
- [ ] Funnel steps are ranked by recoverable value, not raw people lost × order value.
- [ ] Each finding names its data and its customer evidence, or says one is missing.
- [ ] Tracking problems and defects are listed to fix now, with steps to reproduce.
- [ ] Each test has a script-based sample size, at most six weeks, dates clear of big sales periods, a fixed stop rule and a revenue or quality guardrail.
- [ ] Before-and-after results are labeled directional.
