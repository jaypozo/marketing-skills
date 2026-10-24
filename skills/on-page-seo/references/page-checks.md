# Technical checks for one page

You need Search Console, a browser and the page source.

## Indexing

- [ ] Search Console URL Inspection says the URL is indexed. If not, read the stated reason before changing content.
- [ ] Google's chosen canonical matches the URL you want. If Google picked another URL, find out why (duplicates, redirects, conflicting canonical tags).
- [ ] No `noindex` in the page's robots meta tag or in the HTTP headers.
- [ ] robots.txt doesn't block the page or the CSS and JavaScript it needs to render.
- [ ] The page is in the XML sitemap, and the sitemap URL matches the canonical exactly (https, www or not, trailing slash).

## What search engines see

- [ ] The main content is in the HTML, or renders without needing someone to click or scroll. Check the rendered HTML in URL Inspection.
- [ ] Headings are real heading tags, not styled paragraphs.
- [ ] Links are real `<a href>` links, not buttons with scripts.
- [ ] Text isn't hidden in tabs or accordions that only load when clicked.

## Phone

- [ ] On a real phone: body text is readable without zooming, buttons are easy to tap, and nothing covers the content on load.
- [ ] Tables and code blocks scroll sideways instead of breaking the layout.
- [ ] The call to action can be seen and tapped.

## Speed

- [ ] Run PageSpeed Insights on the URL. Note LCP, INP and CLS from real-user data if shown, and lab data if not.
- [ ] The largest image is compressed and sized for its slot, and isn't lazy-loaded.
- [ ] No embed (video, map, social post) blocks the first screen from rendering. Load embeds on click where you can.

## Links and redirects

- [ ] No internal links on the page point to redirects or 404s. A browser extension or a crawler can check this.
- [ ] If the URL changed, the old URL 301s straight to the new one in a single hop.

## Snippet and sharing

- [ ] The title and meta description in the source are the ones you wrote, not CMS defaults or duplicates.
- [ ] Open Graph title, description and image are set, so shared links preview properly.
- [ ] Structured data passes Google's Rich Results Test, if any is used.
