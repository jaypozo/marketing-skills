# Question set and tracking sheet

## Building the question set

Aim for 20 to 40 questions. Rough mix (round to whole questions):

| Type | Share | Examples (swap in the real category) |
| --- | --- | --- |
| Category | 25% | best [category] for [audience]; top [category] for [situation] |
| Problem | 20% | how do I [problem the product solves]; what's the easiest way to [task] |
| Comparison | 20% | [brand] vs [competitor]; [competitor] alternatives |
| Brand facts | 15% | how much does [brand] cost; does [brand] work with [tool]; is [brand] good for [use] |
| Use case with context | 20% | I run [situation with details], what should I use for [task]? |

Where to get the wording:

- Sales call notes and demo requests: the questions prospects ask first
- Support tickets from new customers: what they expected before buying
- Review sites and forums: how people describe the problem
- The site's search queries in Search Console, especially long questions

Write each question as a person would type or say it, including the context they'd give. Mark each one branded (it names the brand) or unbranded. "[brand] vs [competitor]" is branded; "[competitor] alternatives" is not. Keep the set in a file with a version number and date. When a question has to change, start a new version and note the reason.

## Run conditions to record

| Field | Example |
| --- | --- |
| Assistant | ChatGPT, Perplexity, Gemini, Google AI Mode, Copilot, Claude |
| Mode or model | Default model, search on |
| Account state | Logged out, or logged in with memory and history off |
| Location | Country and city, or VPN location |
| Date and time | 2026-11-03 10:15 |
| Fresh chat | Yes for every question |
| Run method | By hand, tool name, or API (API answers differ from the apps) |
| Web search | On, or off (for the memory check on brand facts) |

## Tracking sheet columns

One row per run.

| Column | Values |
| --- | --- |
| run_id | Q07-perplexity-2 |
| question_id | Q07 |
| branded | yes / no |
| assistant | |
| date | |
| brand_mentioned | yes / no |
| brand_recommended | yes / no (a top pick, or in a shortlist of five or fewer with a positive reason) |
| competitors_named | comma-separated |
| cited_urls | full URLs |
| factual_errors | exact wrong words, quoted |
| answer_file | path to the saved answer text or screenshot |
| notes | anything odd (refused, asked a follow-up, outdated date mentioned, AI Overview not shown) |

## Calculations

- Mention rate = rows with brand_mentioned = yes ÷ all rows. Report it per assistant and overall, and separately for branded and unbranded questions.
- Recommendation rate = rows with brand_recommended = yes ÷ all rows.
- Share of voice = rows naming the brand ÷ (rows naming the brand + the sum, across competitors in the set, of rows naming each one). Count rows, not how many times a name appears in one answer. State the competitor set.
- Citation share by domain = citations of a domain ÷ all citations. Split owned, competitor-owned and third-party domains.

## AI referrals in analytics

Referrer domains to look for (the list changes, so check it each audit): chatgpt.com, perplexity.ai, gemini.google.com, copilot.microsoft.com, claude.ai. ChatGPT also adds `utm_source=chatgpt.com` to many links, so count that source as well as the referrer. A custom channel group for AI referrals in analytics makes the monthly check quicker. Report conversions from these visits as well as sessions. Google AI Overviews and AI Mode traffic mostly arrives as ordinary Google organic traffic, so it can't be separated reliably.
