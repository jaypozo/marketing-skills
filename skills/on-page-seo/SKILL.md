---
name: on-page-seo
description: Audits and rewrites one page so it fits the search it should rank for. Works for articles, category and collection pages, product pages and service pages. Reads Search Console data to diagnose the problem (snippet, content gap, outdated page, migration or redirect, indexing), compares the page with the live results, then fixes the title tag, meta description, headings, opening, content, internal links, images and structured data, with a plan to measure the change. Use when someone asks to optimize a page, blog post or category page for SEO, improve rankings for a keyword, refresh or update old content, recover a page that lost Google traffic, write title tags and meta descriptions, or raise click-through rate from Google. To plan which pages to create, use keyword-map. If traffic is steady but sales fell, use conversion-diagnosis.
metadata:
  version: "1.1"
---

# On-page SEO

Work on one page at a time, and settle what the page is for before changing anything. An underperforming page usually has one main problem. Its snippet doesn't earn the click, or its content answers a slightly different question than the searcher asked. It may have gone stale, been damaged in a migration, or not be indexed the way the owner thinks. Search Console usually shows which one. When two problems show up, fix the technical one first, then the content, and ship them in that order so you can tell what worked.

## Ask the user first

The diagnosis needs Search Console data, so ask for that first. Without it, say the problem type is a guess. Mark other gaps `[CONFIRM: ...]`.

1. The URL, or the page content if it isn't published yet.
2. The query it should rank for. If they're unsure, Search Console will tell you.
3. A Search Console export for the page: queries with clicks, impressions, CTR and position. Ask for daily data across any drop, and the same period a year earlier for seasonal businesses.
4. What the page is for: the action a visitor should take.
5. What the CMS lets them change: title tag, meta description, slug, structured data, alt text, text above a product grid.
6. Anything that changed: redesign, platform migration, URL changes, rewrite, new competitor.

## Procedure

1. Check the scope. Look at site-wide clicks in Search Console. If many pages dropped on the same date, the problem is site-level (usually a migration, redirects or an update), and fixing one page won't solve it. Say so and list the site-level checks: a redirect map for every old URL, canonicals, and the sitemap. Then carry on with this page.
2. Name the page type: article, category or collection, product, or service or location page. Category and product pages have their own rules in [references/page-types.md](references/page-types.md). Read it for those.
3. Confirm the target. Sort the page's queries by impressions and check that the top ones share one intent. If two intents appear (say "invoice template" and "how to chase an unpaid invoice"), pick one for this page and note the other for keyword-map. A product query that lands on a category page belongs to the product page. A modifier with the same intent ("wide", "waterproof") usually becomes a filter or a section on this page, not a new page.
4. Diagnose from the data pattern:

   | Pattern | Likely problem | Main work |
   | --- | --- | --- |
   | Drop starting at a migration, redesign or URL change | Redirects, canonicals, lost content or internal links | Check the old URL redirects with a 301 in one hop, that Google's canonical is the new URL, and that content and links survived. Then content. |
   | Position 1 to 5, CTR well below the site's other pages at the same positions | Snippet | Title and meta description |
   | Position 6 to 20, steady impressions | Content or intent gap | Rework the content against the results |
   | Clicks and position fell from a clear date, with no site change | Outdated, overtaken or hit by an update | Check Google's list of confirmed updates for that date. Compare with what ranks now and refresh. |
   | Almost no impressions | Indexing or targeting | URL Inspection: indexed? Google's chosen canonical? Then targeting |
   | Good traffic, few actions | Wrong intent or weak next step | Opening and call to action. If traffic is steady and sales fell, hand over to conversion-diagnosis. |

   Use the daily data to find the date a drop started. Two windows of three months can't show it.
5. Read the live results for the target query, with the right country set. Use a web search tool or SERP API with the location set, or ask the user for screenshots. If you can't see results at all, say the comparison wasn't done. Compare against the top results of the same page type as this one, and note any other types that rank. Write down what those results cover that this page doesn't, and what none of them does well. Use the second list to choose what this page adds.
6. Fix the opening. For articles, the first screen answers the query or shows what the page offers. Where there's a direct answer, give it in the first paragraph. For category pages, products stay visible on the first phone screen, under a short line or two of help.
7. Fix the content. Add what a searcher needs that's missing, and something original: real photos, data, a worked example, staff experience, a template. Cut parts that are off topic or out of date. Correct facts. On articles, change the visible date only if the page was really reviewed.
8. Write three title tag options using the rules below, and pick one.
9. Write the meta description: what's on the page and why it's worth the click, in about 140 to 160 characters.
10. Fix the headings. One H1 that keeps the title's promise. H2s that follow the reader's task. Question headings where people search in questions.
11. Add internal links. Find three to five pages on the site that should link here, using a `site:domain.com topic` search or the sitemap. Give the sentence and anchor text for each. From this page, link to the next step.
12. Fix the images. Use descriptive file names and alt text that says what the image shows. Compress them (WebP or AVIF, usually under about 200 KB for content images) and set width and height. Never lazy-load the main image.
13. Add structured data only where it matches what's visible. Article on articles. Product on single product pages. BreadcrumbList on category pages. SoftwareApplication for apps. LocalBusiness for local services. Never promise a rich result; say which ones the page is eligible for under Google's current documentation. FAQ and HowTo rich results were cut back sharply in 2023, and more types have been dropped since.
14. Run the checks in [references/page-checks.md](references/page-checks.md). Report the failures, and list the sections that passed.
15. Write the change log with dates. After publishing, ask the user to request indexing in URL Inspection. Then write the measurement plan.

## Decision rules

- If the page already gets impressions for the query, improve it rather than publishing a second page that would compete with it.
- Title tags: put the main topic near the start and make a specific promise the page keeps. Use no unverifiable claims ("Best Prices"), and keep each title unique on the site. About 50 to 60 characters fits most desktop results. Google rewrites many titles; one that matches the H1 and the content is more likely to survive.
- CTR: compare with the site's own pages at similar positions. A 2019 Backlinko analysis of four million results, from before AI Overviews, found the top result averaged a 27.6% CTR and each position gained made a click about 32% more likely. The curve is flatter on searches with an AI answer, but pages stuck at positions 6 to 10 are still worth the work.
- Keywords: no density target. Use the searcher's words where they fit. Repeating a phrase until it reads oddly hurts the page.
- URLs: don't change the slug of a page that ranks unless it's misleading. If a URL changes, the old one gets a 301 (not a 302) straight to the new one, and internal links are updated.
- Speed: Google treats a largest contentful paint (LCP) under 2.5 seconds as good. Fix page-level causes here, such as one huge image or a slow embed. Problems that come from the site template go to the developer as a separate list.
- Measure 4 to 8 weeks after the changes are indexed. Compare the same query set against an equal earlier period, or year on year for seasonal products. Look at position and CTR separately, check conversions, and note anything else that changed.

## Output

```markdown
# Page audit: [URL] ([page type])

Target: [query group]   Intent: [learn / compare / buy / local]
Evidence: [GSC period], [clicks, impressions, CTR, avg position], drop date if any
Scope: [this page only / site-wide issue found: ...]
Problem type: [from the table] because [data]

## What the results show
## Changes, in the order to ship them
| Element | Current | New | Why |
## Internal links to add
| From page | Sentence | Anchor text |
## Checks: failures, and sections passed
## Template-level issues for the developer
## Change log, indexing request and measurement plan
## CONFIRM items
```

## Example

A B2B invoicing tool's article "How to write a late payment email" sits at position 7.8, with 14,000 impressions over three months and a 1.1% CTR. The top results are copy-and-paste templates, one for each stage (polite reminder, firm, final notice). The article is an essay on cash flow that only reaches an example email halfway down.

Problem type: content or intent gap. Searchers want templates by stage.

- Title, old: "Cash Flow Tips: Dealing With Late Payments". New: "Late Payment Email Templates: 5 Stages, Copy and Paste" (54 characters).
- Opening: replace the two cash-flow paragraphs with one line, "Pick the stage your invoice is at and copy the template", and a jump list.
- Add five templates, each with the subject line, when to send it and what to change. Add something no ranking page has: the tool's own data on which stage most often gets paid, with the sample size and dates.
- Cut the essay to a short closing section that links to the cash-flow guide.
- Internal links from the invoicing features page and two posts on getting paid.

Measure position and CTR for the "late payment email" group eight weeks after reindexing, against the previous eight weeks. Count trial signups from the page too.

## Final check

- [ ] Site-wide clicks were checked, and any site-level issue is reported separately.
- [ ] The page targets one intent, confirmed from Search Console and the live results (or the results check is marked as not done).
- [ ] The problem type is named and backed by the data. Technical fixes come before content in the shipping order.
- [ ] The page adds something the top results don't have, and it's true.
- [ ] The title is unique, front-loads the topic and makes a promise the page keeps. The H1 matches it.
- [ ] Structured data fits the page type and matches visible content. No rich result is promised.
- [ ] Internal links are listed with source page, sentence and anchor.
- [ ] Every URL change has a single-hop 301.
- [ ] The measurement plan compares like periods (year on year if seasonal) and includes conversions.
