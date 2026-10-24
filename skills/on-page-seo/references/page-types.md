# Category and product pages

The main procedure is written around one page and one search. Shop pages follow it too, with these differences.

## Category and collection pages

Category searches are won by pages that help people choose between products. Long articles rarely rank for them.

- First phone screen: H1, one or two lines of help, then products. Don't push the grid below a banner or a long intro.
- Above the grid: 50 to 150 words that help someone choose. What differs between the products ("cushioned or firm", "for mud or for dry trail"), who each type suits, and a link to a deeper guide if there is one. Write it in the staff's own words, from their own experience.
- Below the grid: a short FAQ built from real customer questions (sizing, returns, care). Remove any block of repeated keywords at the bottom of the page. It does nothing for readers, and it looks like stuffing.
- Filters: match the way the searches in Search Console are worded. If people search "wide", "waterproof" or "for women", those should be filters. Only make a filter its own indexable page when it has enough products and its own search demand. Otherwise keep filtered URLs out of the index (canonical to the main category, or noindex, depending on the platform).
- Product cards: a clear name, price, the main distinguishing feature and a real photo. Ratings only if they're real and from the product page.
- Title tag: "[Category] for [audience or use] | [Shop]". Leave out "Best Prices" and "Free Shipping" unless they are true and matter to the buyer. Even then, put them in the meta description instead.
- Structured data: BreadcrumbList. Don't mark up every product in the grid as Product. Product markup belongs on each product's own page.
- Pagination: each page of results gets a self-referencing canonical. Page 2 onward shouldn't canonicalize to page 1.
- Shopping results: when a shopping carousel sits above the organic results, the products can appear there through the merchant feed (Google Merchant Center free listings). Mention it to the user.

## Product pages

- The searcher usually wants a specific model. Make it obvious that this is the page for it: the exact model name in the title, the H1 and the first line.
- Give facts a buyer needs: price, sizes and fit notes, materials, what's in the box, delivery and returns, and stock status.
- Add something original: your own photos, staff notes on fit or use, real customer questions and answers.
- Structured data: Product with offers (price, currency, availability). Add ratings only if real reviews are shown on the page.
- Variants: one URL per product, with variant selection on the page, unless each variant has its own search demand.
- Out of stock: keep the page live if the product is coming back. Say when it returns, and link to similar items. If it's gone for good, 301 the URL to the closest replacement or to its category.

## Shopify and similar platforms

- Products are often reachable at two paths: `/products/x` and `/collections/y/products/x`. Check that the canonical points to `/products/x`, and that internal links use that path.
- Platform migrations often leave old URLs with 302 redirects, or with chains of redirects. Check every old category and product URL for a single 301 to its new address.
