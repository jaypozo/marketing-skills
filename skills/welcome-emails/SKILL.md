---
name: welcome-emails
description: Writes the welcome email sequence new subscribers get after signing up. Delivers what the signup promised, gives a quick useful win, answers the objections that stop people buying and makes one relevant offer. Comes with send timing, branch and exit rules, a pre-send test list and the numbers to watch. Use when someone needs a welcome series, nurture sequence, onboarding emails for a newsletter, an automated flow after a popup, lead magnet or webinar signup, or asks what to send new subscribers in Klaviyo, Mailchimp, Kit or a similar tool. Not for abandoned-cart or post-purchase flows, one-off newsletters or cold email. For launch emails, use product-launch.
metadata:
  version: "1.1"
---

# Welcome emails

The sequence has four jobs, in order. Keep the promise made on the signup form, help the subscriber get one small result, deal with what stops them buying, and make an offer. After that they move to the regular newsletter.

## Ask the user first

Email 1 can't be written without the exact signup promise and the resource, so get those first. Put `[CONFIRM: ...]` in the draft wherever another fact is missing.

1. The exact promise on the signup form or popup, word for word.
2. The resource they were given (the file itself, or its sections), so the emails can point to real pages in it.
3. What they sell, prices, and links. If there are several product lines, ask which one matters most to new customers.
4. Whether any deadline, discount or bonus will be enforced: a standing welcome code, a seasonal last-order date, a price rise. Don't invent one (see the decision rules).
5. Objections buyers raise: the buyer brief's list if there is one, or the questions people ask before buying.
6. Who signs the emails. If there are several founders, pick one and keep them for the whole sequence. Also get the sending address and the postal address for the footer.
7. A few paragraphs the founder or brand has written, to match the voice.
8. Their email tool and what it can do: tags, branching on clicks or form fields, excluding buyers, frequency caps.
9. How often the regular newsletter goes out, and which other automated flows exist (abandoned cart, post-purchase), so they don't collide.
10. Reviews, results and customer stories they have permission to quote.

## Procedure

1. Write the sequence map first (see "Output"), then the emails. The default is five emails over about ten days:

   | # | When | Job |
   | --- | --- | --- |
   | 1 | Right away | Deliver what was promised. Say what's coming and how often. Ask one question they can answer by replying. |
   | 2 | Day 1 or 2 | One quick win: a single action they can do in about ten minutes with the resource. |
   | 3 | Day 3 or 4 | Take on the main objection or wrong belief. Back it with a story or proof. |
   | 4 | Day 6 or 7 | The offer: what it is, who it's for, the price, what happens after buying. |
   | 5 | Day 9 or 10 | Answer the remaining objections and practical questions, then hand over to the newsletter. |

   Change the count for the price. Under about $30, swap emails 3 and 4: make the offer on day 3 or 4, and handle the objection in the email after it. From $30 to a few hundred dollars, keep five. Above that, add one or two teaching emails before the offer.
2. If a lead-magnet plan already wrote the delivery email, use it as email 1 rather than writing a second one.
3. If the signup promised two things ("a care guide, plus first look at new pieces"), the sequence delivers the first. Say in email 1 that the newsletter keeps the second.
4. Set the branch and exit rules.
   - Anyone who buys leaves the offer emails at once.
   - People who were already customers when they signed up skip email 4, or get a version about care, refills or accessories.
   - To split two groups with different needs, add a choice in email 1 ("Buying for yourself or as a gift?"), with one link per answer, and branch on the click. A reply can't drive a branch automatically.
   - Hold new subscribers out of the regular newsletter until the sequence ends. Check that the tool's frequency cap won't silently skip a sequence email. Exclude them from other promotional flows while the sequence runs.
5. Write each email around one job and one main link. The only extra links allowed are the segment links in email 1. Keep each email to 120 to 300 words, from the chosen person, in the first person. One or two of the five should look like plain text. For physical products, the offer and proof emails can carry product photos.
6. Write the subject and preheader as a pair. The subject says what's inside. The preheader adds the second piece of information instead of repeating the subject.
7. Make the offer email specific. Use one product line, not the whole catalog. Give the price, who it's for and who it's not for, and what happens from purchase to delivery. Use only deadlines and bonuses the business will honor. Make no claims about competitors that the user can't back up.
8. Email 5 closes the offer only if the offer has an end date. Otherwise it answers questions, gives the main link once more, and says what the newsletter will bring.
9. Run the pre-send tests in [references/preflight.md](references/preflight.md) on the live automation. If you don't have access to the account, hand the list to the user and mark each item "Not run: needs the live account".
10. Set up the measures and a review date (see "Decision rules"). Say who reads the replies and how useful answers get tagged. Log useful replies as evidence for buyer-research.

## Decision rules

Offers and deadlines

- A welcome discount is fine when it's real: every new subscriber gets it, it's a working code, and it expires when stated. If the owner proposes one, check those three points. If it isn't set up that way, leave it out and say why. Never add a countdown or "last chance" line to a deadline that doesn't exist.
- Seasonal last-order dates and announced price rises are real deadlines. Use them.

Content

- Backlinko's planning guide (2025) of roughly 80% education to 20% promotion works out to one offer email in five, plus light mentions elsewhere.
- Subject lines: phone inboxes often cut subjects off after 30 to 40 characters, so put the meaning in the first 30. Two- or three-word subjects are worth a test.

Measuring

- Opens are unreliable. Since Apple's Mail Privacy Protection launched in 2021, many opens are recorded automatically. Judge each email on clicks, replies and unsubscribes, and the sequence on purchases within 30 days of signup.
- Review after 200 people have finished the sequence, or after eight weeks, whichever comes first. Starting thresholds, to be replaced with your own baselines:
  - An unsubscribe rate over 1% on one email means it broke the promise or came too soon.
  - If email 2 gets less than half the clicks of email 1, the quick win isn't appealing or isn't quick.
  - Keep spam complaints under 0.1%. Google warns senders never to reach 0.3%, the level at which Gmail starts filtering. Stop and fix the sequence well before that.

Delivery and list health

- Gmail and Yahoo require bulk senders (5,000 or more emails a day to their users) to authenticate their domain (SPF, DKIM and DMARC) and to offer one-click unsubscribe. The preflight list checks both.
- After the sequence, call a subscriber inactive after about 20 sends with no clicks. Send one re-engagement email, then suppress the people who don't respond. Don't delete them.

## Output

```markdown
## Sequence map: [name]
Trigger: [form or tag]   Exit: [purchase]   Excluded: [existing customers -> variant]   Then: [newsletter, cadence]
Sender: [person]   Newsletter hold: [yes, until email 5]

| # | Send | Job | Subject (alt) | Preheader | Main link | Branch or exit rule |
```

Then each email in full: subject, alternate subject, preheader, body, sign-off and P.S. if used. After that, the preflight list with each item's status, the measures table (one row per email for clicks, replies, unsubscribes and complaints, then purchases for the sequence), the review date, and every CONFIRM item.

## Example

A weekly newsletter on pricing for freelance designers. Signups get a rate calculator spreadsheet. The paid product is a $79 self-paced course on raising your rates. The main objection is "clients will leave if I raise prices".

| # | Send | Job | Subject | Main link |
| --- | --- | --- | --- | --- |
| 1 | 0 min | Deliver the calculator | Your rate calculator | Spreadsheet copy link |
| 2 | Day 2 | Quick win | Your real hourly rate | Calculator, tab 2 |
| 3 | Day 4 | Objection: losing clients | What happened when Dana raised her rate 30% | Case write-up |
| 4 | Day 7 | Offer | The rates course, $79 | Course page |
| 5 | Day 10 | Questions, then handover | Before you decide | Course page FAQ |

Email 2:

```text
Subject: Your real hourly rate
Preheader: Ten minutes, one number you probably haven't worked out

Hi,

Open the calculator and go to the second tab. Put in last month's invoices and the hours you actually worked, including the emails, the revisions and the call that ran long.

If the number is well below the rate you quote, that gap is money you're already losing.

Write it down. In two days I'll show you how one designer used hers to raise prices without losing her two biggest clients.

Reply with your number if you like. I read every reply.

Sam
```

## Final check

- [ ] Email 1 delivers exactly what the form promised, with a working link, and says what's coming.
- [ ] Each email has one job and one main link.
- [ ] The offer email names one product line, its price, who it's for and not for, and what happens through delivery.
- [ ] Every deadline, discount and bonus is real and set up. No claims about competitors without proof.
- [ ] Buyers exit, existing customers are handled, and new subscribers are held out of the newsletter and other promotional flows.
- [ ] Subjects make sense in the first 30 characters, and each preheader adds something.
- [ ] Each preflight item is marked as passed, or as "Not run" for the user.
- [ ] Measures use clicks, replies, unsubscribes, complaints and purchases, and there's a review date.
- [ ] The open CONFIRM items are listed at the end, for the user.
