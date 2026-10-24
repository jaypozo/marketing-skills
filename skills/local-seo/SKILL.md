---
name: local-seo
description: Improves how a local business shows up in map results and local searches. Audits and fixes the Google Business Profile, matches categories and services to the words customers search, finds duplicate and outdated listings, and cleans up name, address and phone consistency. Plans service and location pages with real local detail, and sets up an honest review request routine with reply templates, including privacy-safe replies for healthcare and other regulated businesses. Use when a business with a storefront or service area (plumber, dentist, clinic, salon, restaurant, contractor, gym, shop) asks about local SEO, ranking on Google Maps or in the map pack, its Google Business Profile, getting more reviews, citations, "near me" searches, a move to a new address, or location pages. Not for online-only businesses. To optimize a single service page, use on-page-seo; to write its copy, use landing-page-copy.
metadata:
  version: "1.1"
---

# Local SEO

Google ranks local results on relevance, distance and prominence. You can't move the business, so the work goes into the other two. Make the listing say exactly what the business does, keep its details the same everywhere, and get honest reviews coming in every month.

## Ask the user first

Get the exact name, address and phone first; every other step checks against them. Mark anything else you had to assume `[CONFIRM: ...]`.

1. The business name as it appears on the sign and on legal documents, the address (or the service area, if customers don't visit), and the main phone number.
2. Opening hours, including holidays.
3. Services, with the most profitable ones marked, and the towns or neighborhoods served.
4. How many locations there are. Whether individual practitioners (doctors, dentists, lawyers, agents) have their own listings.
5. The website, and who has access to the Google Business Profile.
6. Review count and rating for the business and for the top three competitors in the map results.
7. Past names, addresses and phone numbers. Moves and old numbers cause many of the listing problems.
8. Whether the business is regulated: healthcare, legal, financial. That changes how reviews can be answered and which words can be used.

## Procedure

1. Check eligibility. The business must serve customers in person during its stated hours, at its own premises or at the customer's. Service-area businesses hide their street address and list the areas they serve. Virtual offices, shared mailboxes and PO boxes don't qualify. Never create a listing for a place the business doesn't operate from.
2. Research local search terms. Take the customer's words for each service from calls, emails and reviews. People often search for the problem rather than the service ("toothache", "AC not cooling"). Combine those words with each town and with modifiers such as "near me", "emergency", "cost" and "open now". Check which searches show a map pack. Use a web search tool or rank-grid tool set to the location, or ask the user for screenshots. If you can't check, mark the column "not checked".
3. Audit the profile with [references/gbp-checklist.md](references/gbp-checklist.md). The items that matter most:
   - Primary category: the one that matches what most customers search for. Check which primary category the top competitors use. If customer searches and the top competitors both point to a category other than the current one, change the primary, then watch profile calls and views for four to six weeks before deciding.
   - Secondary categories: only for services the business provides, and only words it's allowed to use. In regulated professions, words like "orthodontist" or "specialist" may be limited to licensed specialists.
   - Name: exactly as on the sign and legal documents. Adding keywords breaks Google's guidelines and can get the listing suspended.
   - Services, hours and photos: complete and current, with real photos.
   - Changing the name, address or category can trigger re-verification. Warn the owner before making those changes.
4. Find duplicates and stale listings. Search Google Maps for the old address, the old phone number and variations of the name. A business that moved often has a second listing at the old address. Mark that one as moved, or ask Google support to merge it. Check whether the old phone number now belongs to someone else.
5. Make name, address and phone (NAP) consistent. Write down the one correct version. Check sources in this order:
   - Google, then Apple Business Connect (Apple Maps), then Bing Places (it can import from Google).
   - Facebook.
   - The data aggregators that feed many smaller sites: in the US, Data Axle, Foursquare and Localeze (now part of TransUnion). Other countries have their own.
   - The main directories for the trade. For healthcare, that means the NPI registry, insurers' find-a-provider directories, Healthgrades and Zocdoc. For restaurants, Yelp, Tripadvisor and booking platforms. For trades, the big home-services sites.
   - Local chambers and trade bodies.

   Fix the 10 to 15 that matter most. Don't buy bulk citation packages.
6. Plan the website pages:
   - One page per core service, written in the customer's words, with the answer to the top questions (price ranges, insurance accepted, how soon). on-page-seo can optimize each page, and landing-page-copy can write it.
   - A location page only for a real location, or for a service area where the business has real local detail: jobs done there, reviews from there, local rules, staff based there. A single storefront usually needs no town pages at all.
   - Never publish the same text with the town name swapped.
   - Add LocalBusiness structured data matching the profile, a tap-to-call button on phones and a map on the contact page.
7. Set up the review routine with [references/review-templates.md](references/review-templates.md). Ask every customer when the job is done or the visit ends, with a direct link to the review form. Send one reminder after three to five days. A printed QR code that customers scan on their own phones is fine. A shared tablet or kiosk at the business isn't. Regulated businesses use the privacy-safe reply templates.
8. Plan local links and mentions from existing relationships: suppliers, trade bodies, local sponsorships, local news, partner businesses.
9. Check competitors for spam. Keyword-stuffed names, fake locations and fake reviews can be reported through "Suggest an edit" on the listing, and Google's business redressal form. Reported spam listings are sometimes removed within weeks, which can move the business up a place.
10. Set up tracking (see the decision rules), and a 90-day schedule with owners.

## Decision rules

- Ask everyone for a review. Never ask only happy customers, and never check satisfaction first and send the link only to those who were satisfied. That screening is called review gating, and Google's policy bans it. In the US, the FTC's rule in force since October 2024 bans fake reviews, paying for reviews that must be positive, undisclosed reviews by insiders, and threats used to suppress negative ones. The FTC has also warned that gating can be deceptive. Google's policy goes further: never offer anything in exchange for a review.
- Set a monthly review target from visit volume and the gap to competitors. If 300 customers a month are asked and 5% leave a review, that's 15 a month. Then check whether that closes the gap to the top competitor in a reasonable time. Readers look at how recent the reviews are, not only how many there are.
- Reply to reviews within about two working days, as good practice. For negative reviews, acknowledge the problem, give a named person to contact and take it off the platform. Regulated businesses acknowledge the concern in general terms only (see below).
- Texting review requests needs the customer's consent first. In the US that's under the TCPA, for every kind of business.
- Regulated businesses: in US healthcare, a public reply that confirms someone is a patient, or mentions their treatment, can breach HIPAA, and practices have been fined for it. Reply without confirming the relationship or any details. Any vendor that handles patient data (review, texting or call tracking tools) needs a business associate agreement.
- Rankings vary with where the searcher stands, and they usually fall away with distance from the business. Use a grid check across the service area (a 3×3 or 5×5 grid), with points about a mile apart in a town and wider apart in rural areas, rather than one check from the office.
- If the business uses call tracking, put the tracking number as the primary number on the profile and the main number as an additional one. Keep the main number on the website.
- Multi-location businesses keep one spreadsheet as the source of truth for every location's details. Each location gets its own profile and page, plus a UTM-tagged website link so enquiries trace back to the branch.
- Judge progress by calls, direction requests, website clicks from the profile, and booked jobs or appointments, rather than rank position.

## Output

```markdown
# Local SEO plan: [business], [date]

Eligibility: [storefront / service area / hybrid], [notes]   Regulated: [yes, which rules / no]
Correct NAP: [name] | [address or "service area: ..."] | [phone]

## Search terms by service and place
| Service | Customer words | Towns | Map pack shown? (yes / no / not checked) | Priority |

## Profile fixes
| Field | Current | Change to | Why | Re-verification risk |

## Duplicates and listings to fix
| Site | Wrong detail found | Correct detail | Order | Done |

## Website pages
| Page | Exists? | Local detail it will include | Priority |

## Review routine
Who asks, when, how, the message text, the reminder, reply owner and time, monthly target, privacy rules if regulated.

## Competitor spam to report
## Tracking
## 90-day schedule
| Week | Task | Owner |

## CONFIRM items
```

## Example

A heating and cooling company with two vans covers three towns: Millbrook, Ashford and Kent Falls. It works from the owner's home and has no storefront. It has 38 reviews (4.7 average). The top competitor has 212 (4.6).

- The profile showed the home address. Change it to a service-area listing covering the three towns, with the address hidden.
- The primary category was "HVAC contractor". Two of the three top competitors use "Air conditioning contractor", and summer searches are mostly for AC repair. Change the primary to "Air conditioning contractor" and watch calls for six weeks. Keep "HVAC contractor" and "Furnace repair service" as secondary categories.
- The listed name was "Brightline HVAC | AC Repair Millbrook". Change it to "Brightline Heating & Cooling", the name on the vans and the license.
- The old phone number was still live on Yelp, a trade directory and the chamber of commerce site. Correct all three, starting with the directory.
- Pages: replace the single "Services" page with AC repair, furnace repair and heat pump installation pages. Add one page per town, with photos and notes from jobs done there, reviews from customers in that town, and the local permit rules for heat pumps.
- Reviews: the technician texts the review link from the van when the job is signed off, and sends one reminder three days later. About 200 jobs a month at a 6% review rate gives roughly 12 reviews a month. The office manager replies within two working days.

## Final check

- [ ] The business is eligible for each listing, and service-area businesses hide their address.
- [ ] The profile name matches the real-world name with nothing added. Categories match real services and allowed terms.
- [ ] The owner has been warned about re-verification before name, address or category changes.
- [ ] Duplicate and old-address listings were searched for, and the old phone number was checked.
- [ ] One correct NAP is written down, and the listings to fix are in priority order, including the trade's own directories and the data aggregators.
- [ ] No location pages without real local detail.
- [ ] The review routine asks everyone, with no gating, no incentives and no shared device. It has a reply owner, and privacy-safe replies if the business is regulated.
- [ ] Ranking checks use a grid, and success is measured in calls, bookings and jobs.
- [ ] Every task in the 90-day schedule has an owner.
