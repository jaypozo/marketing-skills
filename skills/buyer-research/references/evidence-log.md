# Evidence log and public search patterns

## Log columns

Keep one row per quote. A spreadsheet works; so does a Markdown table if the set is small.

| Column | What goes in it |
| --- | --- |
| id | Q001, Q002 ... so the brief can point back to rows |
| quote | The exact words. Fix nothing except obvious typos. |
| person | A stable label for the speaker ("reviewer amzn-17", "interview B3"). This is what you count. |
| source type | interview, own reviews (app store reviews of the product count here), competitor reviews, support, open-text survey, multiple-choice survey, sales calls, forums (video comments count here) |
| link or file | Where you found it |
| date | When it was said, not when you read it |
| stage | before purchase, after purchase, cancelled, never bought, unknown |
| customer type | Segment, if known (first order, repeat, business buyer) |
| codes | trigger, outcome, alternative, objection, criterion, proof, problem words |
| note | Your interpretation, kept apart from the quote |

When a source reports a count without separate quotes ("four customers asked this"), log one row with the best quote and put the count in the note. Count those people, not the row.

## Behavior table

What people did is stronger than what they say. Log it separately:

| Measure | Value | Period | Source |
| --- | --- | --- | --- |
| Trial to paid rate | | | |
| Refund rate, and the top refund reasons | | | |
| Day of the trial when people cancel | | | |
| Features used by buyers vs non-buyers | | | |
| Return or repeat purchase rate | | | |

## Searches that find unprompted customer talk

Replace the brackets. Run each in a normal search engine and, where noted, inside the site.

- `[category] recommendations` and `best [category] for [situation]` on Reddit or forums
- `[competitor] alternative` and `[competitor] vs`
- `switched from [competitor]` and `cancelled [competitor]`
- `is [category] worth it`
- `[problem in plain words] help` or `how do I [task] without [annoyance]`
- `site:reddit.com [category] [problem]`
- Marketplace product pages for competitors: read the questions section as well as reviews
- App stores: filter reviews to the most recent and to 2 and 3 stars

## Reading reviews quickly

1. Sort by most recent, then read the 2 and 3 star reviews first.
2. Skip reviews about shipping damage or a single bad batch unless that is the decision you are researching.
3. Copy any sentence that names a situation ("when my toddler...", "for a team of five..."). Those sentences hold the triggers and the words.
4. Stop a source when 20 reviews in a row add nothing new.

## Survey questions worth adding

Suggest these when the existing survey is multiple-choice only, or when there is no survey. If the user can send a short survey to recent buyers, these four questions return the most useful text. Keep every question open-ended.

1. What was going on that made you start looking for something like this?
2. What else did you consider, including not buying anything?
3. What nearly stopped you from buying?
4. How would you describe what we sell to a friend?
