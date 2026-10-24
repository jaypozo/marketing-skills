---
name: lead-magnet
description: Plans and drafts a lead magnet tied to one specific page. Picks the page whose readers match the buyer, finds what those readers get stuck on next, and designs a small resource that gets them past it (checklist, template, worksheet, calculator, swipe file or short email course). Writes the signup boxes, thank-you page and delivery email, and sets up how to judge whether the new subscribers are any good. Use when someone wants to grow an email list or get more subscribers, or asks for a freebie, opt-in, content upgrade, gated download or squeeze page. If they want to know why signups are low before adding an offer, use conversion-diagnosis. For the emails after the delivery email, use welcome-emails.
metadata:
  version: "1.1"
---

# Lead magnet

A lead magnet works when it helps someone with the exact task they were already doing on the page. A generic "free guide" in the footer collects few addresses, and often the wrong ones. This skill starts from one page with the right readers and finds the step where those readers get stuck. Then it builds the smallest useful resource for that step, one that leads on to what the business sells.

## Ask the user first

You can't pick a page without traffic figures, so get those first. Anything else you have to assume goes in the plan as `[CONFIRM: ...]`.

1. Their top pages by entry sessions over the last 90 days, with a monthly breakdown if possible. Include current signups per page if they track it.
2. What they sell, the price, and what the paid product contains (a course outline, a product list). You need the contents to check the resource doesn't give the product away.
3. The URL or text of the page you'll work on, so the signup boxes can go in the right place.
4. Who the ideal subscriber is.
5. Resources they already have: checklists, spreadsheets, templates, recordings, internal docs.
6. Their email tool, whether it uses double opt-in, and the list's average click rate on regular emails.
7. How many hours they have to build the resource, and what design help.

## Procedure

1. Pick the page. Rank pages by entry sessions, then strike out any whose readers aren't likely buyers of the offer the resource will lead to. If the business has more than one offer, choose the offer that fits the page topic, and note the other. From what's left, choose a page with steady traffic (no month below half its average) and a practical task the reader has to carry out after reading. Write down why you picked it, and name the runner-up page for later.
2. Find the next obstacle. What does the reader have to do once they've finished the page, and where will they get stuck? Look at the page's queries in Search Console, the comments and the related support questions. Use the readers' own words for the obstacle.
3. Choose the format from the obstacle:

   | The reader needs to... | Format |
   | --- | --- |
   | remember steps in order, away from the screen | printable checklist |
   | put in their own numbers, or track them | calculator or spreadsheet |
   | write something (an email, a brief, a policy) | fill-in template or swipe file |
   | choose between options | comparison table or scorecard |
   | build a habit over days | 5-day email course |
   | see it done | short recorded walkthrough |

   If two rows fit, pick the one that matches the words readers use for the obstacle. Then open [references/formats.md](references/formats.md) and check the build time against the hours the user has.
4. Check the bridge to the paid product. Using the resource should lead naturally to what the business sells. A setup checklist for a home espresso corner bridges well to a shop that sells grinders. A free version of the paid product doesn't bridge; it replaces the sale. Compare the resource with the product's contents. Then check the gate: the answer the searcher came for stays free on the page. The resource helps with the step after it.
5. Write the resource. Do it in full if it's text (checklist, template, email course). For designed pieces, give a section-by-section draft with sample content. For spreadsheets and calculators, write out the formulas and test them with three realistic cases. Name it by outcome and format, for example "The 7-day sourdough starter feeding schedule".
6. Write two signup boxes. Put one inline, right after the paragraph where the obstacle comes up, and one at the end of the page. Each gets a headline that names the result, one or two lines on what's inside, a small preview image and a button with a verb ("Send me the schedule"). On phones, the preview image sits above the headline or is dropped. Give each box its own form, so the two can be compared. On this page, the new boxes replace the generic footer form.
7. Keep each form to an email field. Add a first-name field only if the emails will use the name.
8. Write the delivery path.
   - Single opt-in: the thank-you page gives the download link right away, and the delivery email sends it again.
   - Double opt-in: the confirmation email is the delivery. Its button confirms the address and opens the resource. The thank-you page tells people to check their inbox, from which sender name, and to look in Promotions or Spam.

   Either way, the delivery email says what emails come next and how often, and gives one next step. It also serves as email 1 of the welcome sequence, so hand it to welcome-emails.
9. Set up measurement before launch. Tag the new subscribers with the resource's name in the email tool, and add UTM tags or affiliate sub-IDs to the links in the follow-up emails. Then fill the measurement table in "Output".

## Decision rules

- Prefer an offer matched to the article over a sitewide one. Backlinko reported (2016) one article's signup rate going from 0.54% to 4.82% after it got its own matched resource.
- Make sure the page has enough traffic to judge the result. Estimate the weeks to 100 signups, assuming a 3% signup rate for a matched resource. That's an optimistic guess; replace it with the page's own rate after four weeks. If even that takes more than three months, pick a busier page, or plan to judge on subscriber quality alone.
- Keep it short. Each sitting with the resource should take 15 minutes or less, and the whole resource should have one outcome.
- Add a popup only if the two boxes underperform after four weeks. Trigger it on exit intent on desktop, or after the reader is about halfway down. On phones, never cover the content when the page loads. Google treats intrusive mobile interstitials as a page experience problem.
- Judge quality as well as count. Over the first 30 days, compare these subscribers' click rate on the regular emails (leave the delivery email out) with the list average. If they click at less than half the list average, the resource is drawing the wrong people, whatever the signup count.
- Start with a single page and measure it for a month. Only then copy the pattern to the runner-up page.

## Output

```markdown
## Lead magnet plan: [resource title]

Page: [URL], [entry sessions per month], current signups [n] ([x]% of sessions that included the page)
Why this page: [one line]   Runner-up page: [URL]
Reader's next obstacle, in their words: [one line]
Format: [format], [n] minutes per sitting, build time [n] hours
Bridge to paid offer: [one line]   Checked against product contents: [yes / CONFIRM]

## Measurement
Signup rate = signups from this page's forms / sessions that included the page.
| Metric | Baseline (4 weeks before) | At 4 weeks | At 60 days |
| Signup rate, inline box | | | |
| Signup rate, end box | | | |
| Confirmation rate (double opt-in) | | | |
| Click rate on regular emails vs list average | | | |
| Purchases or affiliate clicks from this tag | | | |
```

Then: the resource itself (with tested formulas, where there are any), the two box texts, the thank-you page, the delivery email and the list of CONFIRM items.

For the baseline, use the exact four weeks before launch, or prorate the 90-day figures and say so.

## Example

An online bakery-supply shop. Its article on making a sourdough starter gets 6,200 entry sessions a month, and 0.3% of readers sign up through the footer form. The comments keep asking what to do on day 3, when the starter smells odd and stops rising.

Plan: a one-page printable feeding schedule. It covers days 1 to 7, with the flour and water weights for each feeding and a column for what you'll see and what to do. Day 3 gets its own troubleshooting box. The inline box sits right after the article's day 3 paragraph:

```text
Stuck on day 3?
Get the 7-day feeding schedule: exact weights for every feeding, and what to do when the starter smells sour or goes flat.
[Send me the schedule]
```

The bridge: the schedule lists the flour by weight and the jar size, and the shop sells both. The delivery email links to the schedule and to a short "first loaf" article. The welcome sequence offers the banneton and lame kit in week 3.

## Final check

- [ ] The page was chosen from traffic and reader fit, with the reason and a runner-up written down.
- [ ] The resource solves the next step after the page. The answer the searcher came for is still free.
- [ ] The resource was compared with the paid product's contents and doesn't replace it.
- [ ] One sitting takes 15 minutes or less. Any formulas were tested with three cases.
- [ ] Two boxes, each with its own form, and only the fields the emails will use.
- [ ] The delivery path matches the opt-in setting, and the thank-you page says where to look.
- [ ] New subscribers are tagged, and follow-up links are tracked.
- [ ] The baseline is recorded before launch. The plan checks subscriber quality at 4 weeks and purchases at 60 days.
- [ ] CONFIRM items are collected at the end of the plan.
