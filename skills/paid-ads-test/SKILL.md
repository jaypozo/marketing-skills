---
name: paid-ads-test
description: Works out whether paid ads can pay for a product or service before any money is spent, and if so designs a small capped test. Calculates break-even cost per sale, per lead and per click from price, costs, conversion and close rates. Compares that with real keyword costs and gives a go, marginal or no-go verdict per job type. For a test, sets the budget and writes the campaign structure, match types, negative keywords, ads, call and form tracking checks, search-terms reviews and stop rules. Use when someone asks whether Google Ads or paid search is worth it, how much to spend on ads, what CPC or cost per lead they can afford, which keywords to bid on, how to run a first ad test, or whether to try Meta, TikTok or LinkedIn ads on a small budget. Planning only; it never launches campaigns or spends.
metadata:
  version: "1.1"
---

# Paid ads test

Before spending anything, work out what a click is worth to this business and compare it with what clicks cost in its market. Design a test only if the numbers allow one, keep the budget capped, and show every input and assumption.

## Ask the user first

The verdict rests on items 1, 2 and 5, so get those first. Mark other gaps `[CONFIRM: ...]`. A missing cost makes the verdict look better than it is, so assume on the cautious side.

1. Price per order or job, or average order value. If they sell several products or job types with different margins, get each one and the share of sales it makes up.
2. Variable cost per order or job: product or materials, payment fees, shipping, platform fees. Include labor when it's paid per job, or when the time could otherwise be billed.
3. Refunds, redos and free comebacks, as a share of orders.
4. Repeat purchases and referrals within 6 or 12 months, if known. Without data, count the first sale only.
5. For online sales: the conversion rate of the page ads would go to (sessions to sales). For lead businesses: the click-to-lead rate (form fills and calls ÷ visits) and the close rate (paying jobs ÷ leads).
6. The market: country, region or service radius, and language.
7. A monthly amount the user can afford to lose entirely while learning. Ask whether a figure like "about $1,500" is what they'd spend or what they could lose without trouble.
8. What's tracked now: purchases, forms, calls. Ask whether conversions reach the ad platform or only analytics.
9. Keyword ideas, a buyer brief, or past ad account data.

## Procedure

1. Calculate contribution per sale for each product or job type: price × (1 − refund rate) − variable cost. Count repeat or referral contribution only within a payback window the user accepts (for example, 90 days), and say which you used.
2. Work out the click-to-sale rate. For online sales, it's the page's conversion rate. For lead businesses, it's the click-to-lead rate × the close rate. Break-even cost per lead is contribution × close rate. Lead businesses watch that number every day.
3. Get real click costs for each intent group. In Google Keyword Planner (free with an ads account), set the location and language and note the top-of-page bid range. On other platforms, use their own estimates or past account data.
4. Run the script once per job type, from this skill's folder, first with the low end of that job type's top-of-page range. If the verdict is NO-GO even there, stop. Otherwise run it again with the midpoint of the range, and use the worse of the two verdicts in the plan:

   `python3 scripts/ad_math.py --price ... --variable-cost ... --refund-rate ... --cvr ... [--close-rate ...] --cpc ...`

   It prints break-even cost per sale, per lead and per click at the current rate and at 75% of it (paid visitors often convert below the site average). It also gives the ratio to expected CPC and a verdict for each. When one job type is profitable and another isn't, report them separately, because averaging them makes the losing one look viable.
5. Give the verdict using the rules below. For a no-go, say what would have to change and by how much, and name a better channel if the evidence points to one. For local services, compare with Google Business Profile and map results (local-seo) and with pay-per-lead local ads, where they exist in the user's country and trade.
6. For a go or marginal verdict, set the budget: the clicks needed for 10 paying conversions × expected CPC, overall. If the user's limit can't buy that, say that the test will show whether people click and enquire, not whether ads are profitable.
7. Pick one channel. On search, use the structure in [references/search-campaign.md](references/search-campaign.md). Give job types with very different click costs their own campaigns, so the expensive one can't take the whole budget. Choose paid social only when people don't search for the product yet, because it's new or an impulse buy. See the paid social section in the same file.
8. Write the ads. Each ad group's headlines repeat the searcher's words and make the offer clear. Keep within the platform's character limits (Google: 30-character headlines, 90-character descriptions). Check that the landing page matches the ad. landing-page-copy can fix the page, and conversion-diagnosis can find out why its rates are what they are.
9. Check tracking before launch. A test purchase or test lead has to show up in the ad platform itself, not only in analytics. For lead businesses, calls have to be tracked (call assets and calls from the website, with a minimum call length), and closed jobs should be fed back as offline conversions or at least logged by source. Untracked calls block the launch.
10. Write the review schedule and stop rules into the plan.

## Decision rules

Verdict, from break-even CPC ÷ expected CPC:

- Under 0.5: no-go on this channel for now. Improve order value (bundles, upsells), conversion or close rate, or price first. Then rerun the numbers.
- 0.5 to 1.0: marginal. Test only exact and phrase match on the highest-intent terms, with a capped budget, once the landing page is fixed.
- 1.0 or above: test.
- Use the result at 75% of the rate as a stress test. If a group is TEST at the current rate but MARGINAL or NO-GO at 75%, treat it as marginal.

Bidding and budget

- Keyword costs vary a lot. Single keywords run from cents to over $50 a click, so always look up the user's own terms in their own location.
- Start search tests on exact and phrase match. Leave broad match until the account has conversion data and uses conversion-based bidding.
- Start with manual CPC, capped at the break-even CPC. If ads in a marginal group barely show after 7 days, the auction costs more than the business can pay. Record that as the result rather than raising the cap. Move to conversion-based bidding once the campaign has about 30 conversions in 30 days.
- Under about $1,000 in total, test one channel. $500 split across three channels for two weeks is about $12 a day each, which tells you little beyond whether people click.
- On Meta, an ad set needs roughly 50 conversion events a week to leave the learning phase. Optimize for an earlier event (add to cart, lead) when volume is lower, and say that it's a proxy.

Reviews and stopping

- Read the search terms report on day 3, day 7, then weekly. Add negatives for mismatched searches, and note good new terms. Check impression share lost to budget and to rank.
- Stop an ad group when its spend reaches 2× its break-even cost per sale with no paying conversions. For lead businesses, apply this only after the usual time from lead to paid job has passed. For lead businesses, also stop when spend reaches 3× the break-even cost per lead with no leads.
- Stop the test at the planned budget or end date, whichever comes first. Don't top it up mid-test.
- Ten conversions is a small sample. Five versus ten can be luck. Treat test results as directional.
- Scale a profitable campaign 20% to 30% at a time, then check cost per sale after each step.

## Output

```markdown
# Paid ads check: [business], [market]

## Economics (one column per product or job type)
| Item | [Type A] | [Type B] | Source or assumption |
| Price | | | |
| Variable cost (incl. labor if per job) | | | |
| Refund or redo rate | | | |
| Contribution per sale | | | |
| Click to lead / close rate (lead businesses) | | | |
| Click to sale | | | |
| Break-even cost per sale / per lead | | | |
| Break-even CPC (current / at 75%) | | | |
| Expected CPC (keyword group, location) | | | |
| Ratio and verdict (current / at 75%) | | | |

## Verdict and reasoning
## What would change the verdict
## Test plan: channel, campaigns, budget per campaign, dates, conversions targeted
## Keywords, match types and negatives
## Ads
## Tracking checks (launch blockers marked)
## Review schedule and stop rules
## CONFIRM items
```

## Example

A small shop sells printable and tablet planners for $24 as instant downloads. Variable cost is $1.02 (card fees), refunds are 2%, and organic visitors convert at 2.2%. Keyword Planner's top-of-page range for "digital planner for ipad" in the US is $1.10 to $2.90.

The script gives a contribution of $22.50 and a break-even CPC of $0.49 against the low-end $1.10. That's a ratio of 0.45 (0.34 at 75%), so no-go, with no need for the midpoint run.

What would change it: a $49 bundle of planner, stickers and templates, converting at 2%, gives a break-even CPC of $0.92. That's 0.84 against the low end but 0.46 against the $2.00 midpoint, so still no-go. At a 2.2% conversion rate it would be marginal at the midpoint. The recommendation is to build the bundle and test it on organic traffic first. If it converts at 2.2% or better, run a capped search test of about $900, enough for 10 sales at the midpoint CPC, on exact match "digital planner for ipad" and "ipad planner download". Use negatives for free, android and printable, and for the app names notability and goodnotes, unless the planner supports those apps. In the meantime, put the effort into Pinterest, where the shop already gets 60% of its sales.

## Final check

- [ ] Contribution is shown per product or job type, with every input, its source and any assumptions. Labor is included where it's paid per job.
- [ ] Lead businesses have the click-to-lead and close rates multiplied, and a break-even cost per lead.
- [ ] Break-even CPC is shown at the current rate and at 75% of it, using keyword costs for the user's own terms and location.
- [ ] Job types with different economics have their own verdicts and their own campaigns.
- [ ] A no-go says what would have to change, and names a better channel where the evidence shows one.
- [ ] The budget covers about 10 paying conversions, or the plan says it's only a click and enquiry test.
- [ ] Tracking reaches the ad platform. For lead businesses, untracked calls are listed as a launch blocker.
- [ ] Negatives, the review schedule and stop rules are written in.
- [ ] Nothing was launched or spent.
