---
name: keyword-map
description: Builds a buyer-intent keyword map and writes content briefs. Collects the search queries customers use, reads the live results to see what each search wants, groups queries that one page can answer, and assigns each group to an existing or new page (article, category, product or comparison page) with a priority and publishing order. The top new pages get briefs a writer can work from. Use when someone asks for keyword research, an SEO content plan, topic clusters, which pages, blog posts or category pages to create, how to fix pages competing for the same keyword, or a content brief for a writer or agency. To improve one existing page, use on-page-seo. For paid search keywords, use paid-ads-test.
metadata:
  version: "1.1"
---

# Keyword map

This skill produces a map of which page answers which search. Each group of searches gets its own page, and no page tries to answer two groups. Volume figures help, but most decisions come from the actual results pages. What ranks now, and can this business give a better answer?

## Ask the user first

You can start with nothing but the site URL: pull the sitemap and read the results yourself. Ask for the rest, and mark anything you had to guess `[CONFIRM: ...]`.

1. The site and a list of its pages (sitemap or CMS export), including category and product pages.
2. What they sell, prices, and which products or services matter most to revenue. Note any seasonal peaks.
3. A Search Console export of queries and pages for the last 3 to 12 months.
4. Which keyword tools they have. None is fine: the procedure works with search suggestions, Search Console and the results pages.
5. Country, language and the regions they serve.
6. Two to five competitors, including publishers and forums that show up for their topics, not only rival businesses.
7. Customer language: a buyer brief, support tickets, sales call notes.
8. How much they can publish or rework a month.

## Procedure

1. Build the seed list from five sources:
   - The customer's own words (the brief, tickets, calls).
   - Every product and category name, so each category gets at least one row.
   - Search Console queries that already bring impressions.
   - Competitors' main topics, found in their menus, category lists, blog indexes or sitemaps if there's no paid tool.
   - Branded searches, kept in a separate list.
2. Expand each seed with search suggestions, "People also ask", the related searches at the foot of the results and any keyword tool. Convert all volumes to monthly figures, and record their source.
3. Drop what the business can't serve or wouldn't want: other industries, job searches, searches for a free version when only a paid one exists, places it doesn't cover.
4. Read the results for each likely group's main query, with the right country set. Use a web search tool or SERP API with country and language parameters, or a browser set to the location. Note the types of page that rank (product, category, guide, comparison, video, forum, map pack), the winning format, how fresh the results are, and what sits above the organic results: ads, shopping, AI answers, map pack. If you can't see the results, mark the group `[results not checked]`, give provisional scores and put the check first in the plan.
5. Group the queries:
   - Searches that need a different page type go in different groups, even when the words look alike.
   - Among searches with the same page type, two queries go together when their top 10 results share three or more URLs.
   - Without the URLs, group them when one page would fully answer both.

   Name each group after its clearest query. Customer phrases with no measurable volume can go in a group's notes.
6. Score each group with [references/scoring.md](references/scoring.md). The rubric covers business value, ability to win, demand and click opportunity, and gives a sort order. Leave out any group with business value 0 unless there's a stated reason.
7. Map each group to a URL: an existing page to improve, or a new page with its page type. For overlap, open Search Console, filter by the group's main query and look at the Pages tab. Two of the site's pages taking turns over time is a sign they compete. Settle each case with the overlap rules below. Where the wrong page ranks for a group, the target is still the right page. Link to it from the page that ranks, and expect a short dip while Google switches.
8. Build the plan for the next eight weeks. A slot is one unit of the monthly capacity the user gave. A new page or full rewrite takes one slot, and a refresh of an existing page takes half. Put seasonal pages first if they peak within the next three months: publish them at least eight weeks before the peak. Then follow the priority order. Refreshes go to on-page-seo, one page at a time.
9. Write a brief for each new page and each full rewrite in the plan, using [references/content-brief.md](references/content-brief.md).
10. Add the links between pages: for each topic, name the hub page (usually the category or main guide) and the pages that link to and from it.
11. Say how to judge the plan. As a rule of thumb, impressions move first (often 2 to 6 weeks after indexing), then position, then clicks. Review the map at eight weeks against the Search Console baseline.

## Decision rules

- Group the long tail. A Backlinko study of 306 million keywords (2020) found that 91.8% of them got 10 or fewer searches a month, yet together they made up only 3.3% of search volume. Don't write a page for each variant; one strong page collects them.
- Use the competition figure in ad tools with care. It measures advertisers bidding, not organic difficulty. Judge organic difficulty from who ranks and how good their pages are.
- Shopping results: when a shopping carousel sits above the organic results, the business's products can appear there through a merchant feed (free listings in Google Merchant Center). Count that as part of the click opportunity and tell the user.
- Look at a 12-month view so seasonality shows, and check the last three months separately for recent change.
- Overlap between the site's own pages: if two pages serve the same intent and neither ranks well, merge them into the stronger URL and 301 redirect the other. If they serve different intents (a guide and a product page), keep both. Make the difference clear in their titles and openings, and link between them. Don't merge pages just because a tool says both rank for a phrase.
- Use competitor keywords as leads to check. Keep only the groups the business can answer from its own expertise, data or products.
- Health, money, safety and legal topics: these need accurate sourcing, and they may be limited by advertising rules (health claims on food or supplements, for example). Flag them in the notes. The brief has to name who checks the claims.
- Only build many similar pages from a template (city pages, product-by-use pages) when the business has distinct, accurate data for each one.
- If AI answers sit above the results for a group, note it. For whether the brand is cited in those answers, use ai-search-visibility.

## Output

1. The map, as a table the user can paste into a spreadsheet:

| Group | Main query | Other queries | Intent | Page type | URL (existing or NEW) | Value 0-3 | Win 0-3 | Demand tier (monthly, source) | Click opp. | Priority | Reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

2. Branded searches, listed separately with the page each should land on.
3. Overlap cases, each with its decision: merge, separate or leave alone.
4. The eight-week plan: slots, order, seasonal deadlines, and which items go to on-page-seo.
5. Hub and link structure for each topic.
6. Briefs for the new pages and full rewrites.
7. How to judge it, and the review date. Then the CONFIRM items and any `[results not checked]` groups.

## Example

An online shop selling resin and epoxy supplies to hobbyists, with 40 product pages, 12 category pages and 9 blog posts. Three rows from the map, with some columns left out:

| Group | Main query | Other queries | Page type | URL | Value | Win | Priority | Reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Resin for river tables | best epoxy for river table | deep pour epoxy, epoxy for wood slab table | Category with a buying guide on top | /deep-pour-epoxy | 3 | 2 | 1 | Buying intent; existing page at position 11 |
| Resin bubbles | how to get bubbles out of resin | resin bubbles fix, heat gun resin | Step-by-step guide | NEW /guides/resin-bubbles | 2 | 3 | 2 | Forum threads and thin posts rank; we have workshop photos for each step |
| Resin safety | is epoxy resin toxic | resin fumes, resin respirator | Guide with product list | NEW /guides/resin-safety | 2 | 1 | 4 | Strong health and government pages rank, but none compares respirators for resin work. Flag: health claims need checking. |

## Final check

- [ ] Every group was checked against the live results, or is marked `[results not checked]` with provisional scores.
- [ ] Every product category has at least one row. Branded searches are listed separately.
- [ ] No two groups point to the same URL, and no URL serves two intents.
- [ ] Every group in the plan has scores and a written reason for its priority.
- [ ] Overlap cases have a decision.
- [ ] Volumes are monthly, labeled as estimates, with their source and country.
- [ ] The plan fits the user's capacity, puts seasonal pages before their deadline, and sends refreshes to on-page-seo.
- [ ] Each brief asks for something original (data, photos, experience, a worked example) and names who checks any health, money or safety claims.
