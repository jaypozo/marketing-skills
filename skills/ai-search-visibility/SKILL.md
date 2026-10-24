---
name: ai-search-visibility
description: Audits how AI assistants and AI search describe and recommend a brand, then plans fixes. Covers ChatGPT, Perplexity, Gemini, Claude, Copilot and Google's AI Overviews and AI Mode. Builds a fixed set of real customer questions, runs each one several times, and records mentions, recommendations, cited sources and factual errors, split by branded and unbranded questions. Traces wrong answers to the pages or model memory behind them, and checks crawler access and indexing. Ends with a list of corrections, content gaps and third-party coverage to earn, and a re-test date. Use when someone asks about AI SEO, GEO, AEO or LLM visibility, whether ChatGPT or other assistants recommend them, why an AI tool gets their pricing or features wrong, how to get cited in AI answers, which AI crawlers to allow, or how to track AI mentions against competitors. To rewrite a page, use on-page-seo; to pitch the sites that get cited, use partner-outreach.
metadata:
  version: "1.1"
---

# AI search visibility

AI assistants answer from two places: what the model learned in training, and pages it fetches while answering. The business controls neither directly. It does control whether accurate, consistent facts about it are easy to find, and it can earn mentions in the third-party sources assistants read. You ask the same set of customer questions several times on each assistant, log what comes back, trace the wrong answers to their source, and fix what the brand controls. Answers change between runs, so keep the question set and conditions identical at every audit.

## Ask the user first

Wrong answers can only be spotted against the real facts, so get item 1 before running anything. Mark other gaps `[CONFIRM: ...]`.

1. The brand and products, with current facts: what it does, who it's for, prices and plans, main features, integrations, locations or markets, founding year.
2. Three to five competitors that customers compare it with.
3. The questions customers ask before buying, from sales calls, support, demos and reviews.
4. Which assistants their customers use. If unknown, default to ChatGPT, Google's AI Overviews or AI Mode, and whichever other assistant shows up in referral traffic.
5. Analytics access, for referral visits and conversions from AI tools.
6. Which markets matter (countries, languages), and any earlier audit to compare with.
7. Who owns the website, the review profiles and sales materials, so fixes have owners.

## Procedure

1. Build the question set: 20 to 40 questions across five types, using [references/prompt-set.md](references/prompt-set.md). The types are category, problem, comparison, brand facts, and use case with context. Write them the way customers talk, with the context they'd give. Mark each question branded (it names the brand) or unbranded. Freeze the set and give it a version number.
2. Decide how the runs will be done, and tell the user the cost in time.
   - By hand in the consumer apps: logged out, or logged in with memory and history off, a fresh chat for every question, location set. About 2 to 3 minutes a run, so 270 runs is 9 to 14 hours.
   - With browser automation or a paid AI-visibility tracker: faster, but check that it records full answers and cited sources.
   - Through the developers' APIs: cheap and repeatable, but the answers differ from the consumer apps customers use. Label results from APIs as such.
   - Google AI Overviews appear only on some searches. Record whether one appeared, and who it cited.
3. Run every question three times on each assistant, and in each market that matters. Surfer's 2025 research on query fan-out, reported by Backlinko, found that only 27% of the sub-searches an AI tool generated for a question stayed the same across repeats, so the sources it reads change between runs. Save the full answer text or a screenshot for every run; you'll need them as evidence for corrections. Record the results in the tracking sheet in the reference file.
4. Score the results, overall and per assistant, and separately for branded and unbranded questions. Branded questions nearly always mention the brand, which inflates the totals.
   - Mention rate: runs that name the brand ÷ all runs.
   - Recommendation rate: runs where the brand is a top pick, or in a shortlist of five or fewer with a positive reason, ÷ all runs. A name in a longer list counts as a mention only.
   - Share of voice: runs naming the brand ÷ (runs naming the brand + the sum, across competitors in the set, of runs naming each one), with the set stated.
   - Citations: domains cited, split into owned, competitor-owned and third-party.
   - Error log: each wrong fact, quoted, with how many runs it appeared in and on which assistants.
5. Trace each factual error.
   - Open the cited sources.
   - Search for the source wording, not the assistant's paraphrase. "Portal coming soon" will find the page. "Has no client portal" usually won't.
   - Check the brand's old pages, review and directory profiles, app store listings, old press releases and comparison articles.
   - Where the assistant allows it, run the brand-fact questions again with web search off. An error that appears only without search comes from model memory. It changes only with later models, so it needs strong, consistent public facts over time. An error that appears with search comes from a page, which can be fixed in weeks.
6. Classify each source and fix it:
   - Owned, including profiles the business controls on other sites (G2, Capterra, app stores, directories, social bios, business listings): fix it now.
   - Third party you can ask: request a correction, with evidence and the saved answer.
   - Opinion: not an error. Answer it with better evidence elsewhere; don't ask for its removal.
   - Name confusion with another entity: use the exact same name everywhere, and add a short category descriptor where the name appears ("VaultLedger, document software for accounting firms"). Add Organization structured data with `sameAs` links to the official profiles, and keep entries on Wikidata, Crunchbase and LinkedIn accurate where they exist.
7. Fix the owned facts. Keep one page that states the core facts (what it is, who it's for, pricing, plans, integrations, markets, support), and make every owned profile match it. Redirect or update old pages with outdated prices or features. Add structured data that matches the visible page (Organization; Product or SoftwareApplication). It helps Google's features and keeps the facts consistent. Its effect on AI answers is unproven.
8. Close the gaps. For each unbranded question where competitors are named and the brand isn't, look at what the assistants cite. That's usually comparison articles, "best of" lists, forum threads, review platforms, integration directories and documentation. Plan two kinds of work:
   - On the site: pages that answer the question directly in the first lines, then give the evidence. Hand page rewrites to on-page-seo.
   - Off the site: earn a place in the cited sources. Send current customer data to the authors of comparison articles. Ask customers for fresh reviews on the platforms that get cited. Get listed in partners' integration directories. Take part in relevant communities under the brand's own name. Hand the pitching to partner-outreach.
9. Check access and indexing.
   - robots.txt and any CDN or firewall bot rules must not block the assistants' search crawlers: OAI-SearchBot and ChatGPT-User (ChatGPT), PerplexityBot and Perplexity-User, Claude-SearchBot and Claude-User, Googlebot and Bingbot. OpenAI says ChatGPT-User may not follow robots.txt, so firewall rules are what actually block it.
   - Blocking training (GPTBot, ClaudeBot and the Google-Extended robots.txt token) is a separate choice. Using the Google-Extended token doesn't remove a site from AI Overviews.
   - Check the facts page is indexed in Google Search Console and in Bing Webmaster Tools. Copilot uses Bing's index, and ChatGPT search has used Bing data too.
   - If server logs are available, confirm the search crawlers are reaching the key pages.
10. Give sales a short sheet that corrects the common wrong answers, so prospects who arrive with them can be put right on the first call.
11. Set the re-test: the same question set, assistants, markets and conditions, about six weeks after the main fixes go live, then monthly. Track AI referrals and their conversions in analytics alongside each audit.

## Decision rules

- Never report one answer as the brand's visibility. Three runs per question per assistant is the minimum.
- Keep mentions, recommendations and citations separate, and report unbranded results on their own.
- Noise: three runs of one question are closely related, so the real sample is nearer the number of questions than the number of runs. Treat a change in mention rate as real only if it's bigger than about 15 points, or if it shows up in two audits in a row. With fewer than 30 questions per assistant, raise the bar to 20 points.
- Third-party coverage matters more than owned pages for being recommended. AirOps' 2025 report, cited by Backlinko, found brand mentions on commercial questions came from third-party pages about 6.5 times as often as from the brand's own site. Correct the owned facts first anyway, since the business can change those today.
- Say "associated with", not "caused by". Assistants change models and sources often.
- No fake reviews, no undisclosed posts by staff, no microsites dressed up as independent, and no mass-posting in communities. They get found out, and they pollute the sources assistants rely on.
- Skip unproven tricks. As of 2026 there's no good evidence that the major assistants read llms.txt files. Check again at each audit.
- If the brand barely appears in unbranded answers and has little third-party coverage, AI visibility will follow ordinary visibility. Tell the user that, and point to keyword-map and partner-outreach.

## Output

```markdown
# AI visibility audit: [brand], [date], question set v[n]

How the runs were done: [by hand / tool / API], assistants, modes, login state, locations, web search on or off
Runs: [questions] × [assistants] × 3 × [markets]

## Scores
| Assistant | Mention rate (unbranded / branded) | Recommendation rate (unbranded) | Share of voice (unbranded) |
| By question type | ... |

## Citations
| Domain | Owned / competitor / third party | Times cited |

## Gaps: unbranded questions where competitors appear and the brand doesn't
| Question | Competitors named | Sources cited | Gap type (not in third-party lists / no owned answer / wrong facts / name confusion) |

## Factual errors
| Wrong claim (quoted) | Runs | Assistants | Source found | Memory or page | Class | Fix |

## Access and indexing
## Fix list
| Action | Type (owned fact / new page / third party / access / sales sheet) | Owner | Due |

## Re-test date, and what will be compared
## CONFIRM items
```

## Example

A CRM for small real-estate teams. Thirty questions (ten branded), three assistants, three runs each, by hand over two days: 270 runs.

On unbranded questions, the brand was mentioned in 9% of runs and recommended in 4%. Two competitors appeared in over 60%. Five brand-fact questions got the starting price wrong in 14 runs: $39 a month, when it's $25 per user. Searching for the wording "$39/month" found the brand's own old "pricing-2023" page, still live and in the sitemap, and a 2023 review-site profile the company controls. With web search off, the price error didn't appear, so the cause was pages, not model memory.

First fixes:

1. Redirect the old pricing page to the current one, and remove it from the sitemap. (Owned, this week.)
2. Update the review-site profile's price and features. (Owned profile, this week.)
3. Publish a page comparing the CRM with spreadsheets for small teams. The use-case questions kept citing a forum thread on exactly that, and the brand had no page. (New page, via on-page-seo.)
4. Send the authors of the three most-cited "best real estate CRM" lists a short note with real customer numbers and a demo login. (Third party, via partner-outreach.)

Re-test six weeks after the redirect goes live, with question set v1 and the same conditions.

## Final check

- [ ] The question set uses customer wording, covers all five types, marks branded questions, and has a version number.
- [ ] Run method, conditions and markets are recorded. Every question ran at least three times per assistant, and answers are saved.
- [ ] Unbranded results are reported separately. Recommendation and share of voice use the definitions above.
- [ ] Citations are split into owned, competitor and third party.
- [ ] Each error is quoted, traced to a page or to model memory, and classified. Owned profiles on other sites are treated as owned.
- [ ] Name confusion, if any, has an entity fix.
- [ ] Crawler access and Bing and Google indexing were checked.
- [ ] Planned third-party work is earned and disclosed.
- [ ] The report claims associations, not causes, treats small changes as noise, and has a re-test date after the fixes.
