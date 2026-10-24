# Tracking checks

Do these before reading any conversion rate.

## Totals

- [ ] Analytics conversions vs backend records (store orders, CRM leads, database signups) for the same date range and time zone. A gap under about 10% is normal. Above that, find the cause before going further.
- [ ] Revenue in analytics vs revenue in the store, for the same orders. Check whether tax and shipping are included in both.
- [ ] The conversion event counts once per order. Refreshing the thank-you page shouldn't add another.

## Path

- [ ] Every funnel step has an event or a page view that fires on phones and desktops. Test each one yourself with the analytics debug view open.
- [ ] Checkout or booking on another domain you control (a booking tool or scheduler that accepts your tag) is set up for cross-domain tracking. Otherwise buyers come back as referral traffic, and their purchases are credited to the wrong source.
- [ ] Payment provider domains (Stripe, PayPal and the like) are on GA4's "List unwanted referrals" setting.
- [ ] Forms that submit without loading a new page fire an event on success, not on button click.

## Consent and blockers

- [ ] If there's a consent banner, find out what share of visitors decline, and whether the analytics setup models or drops their data. Analytics will undercount by roughly that share.
- [ ] Ad blockers stop some analytics scripts. Compare with backend totals to estimate how much is missing, rather than assuming it.

## Changes

- [ ] Note any tracking change, site release, price change or campaign launch in the period. Rates measured across a change aren't comparable.
- [ ] After a redesign or theme change, check that every tag and event from the old version still fires. Tags written into the old theme's code are often lost.
- [ ] Look for bot traffic: spikes of sessions with zero engagement from one country, source or browser. Exclude them from the denominator.

## Segments

- [ ] Device, traffic source and new vs returning visitors can all be split in the reports.
- [ ] Internal traffic (staff, the agency, test orders) is filtered out.

## Walk-through list

Use this on a real phone and a desktop, or send it to the user if you can't do it yourself. Start from the page a real ad, email or search result sends people to.

- [ ] The main action button is visible on the first phone screen, or one short scroll down.
- [ ] Every pop-up, size chart and menu opens and closes, on iPhone Safari and on Android Chrome.
- [ ] Price, shipping cost and delivery time are visible before checkout.
- [ ] Choosing options (size, color, plan) works, and errors appear next to the field, on screen.
- [ ] A discount code applies, and a wrong one shows a clear message.
- [ ] Guest checkout is possible, or the need for an account is explained.
- [ ] Express pay buttons (Apple Pay, Google Pay, Shop Pay, PayPal) work.
- [ ] A declined card shows a clear message, and the cart is kept.
- [ ] The back button doesn't empty the cart or the form.
- [ ] Phone keyboards match the fields (number pad for phone and card numbers).
- [ ] The confirmation page and email arrive, and say what happens next.
