# Smart Click Media website

Website for **Smart Click Media**, a digital marketing agency based in Harare, Zimbabwe, serving the whole country and the Zimbabwean diaspora.

Phone / WhatsApp: **0771 269 979** (+263 77 126 9979)

## What's in the site

| Page | Path |
| --- | --- |
| Home | `index.html` |
| All services | `services/index.html` |
| 14 service pages | `services/<service>/index.html` |
| Industries | `industries/index.html` |
| About | `about/index.html` |
| FAQ | `faq/index.html` |
| Contact (form sends to WhatsApp) | `contact/index.html` |
| Privacy policy | `privacy-policy/index.html` |
| 404 page | `404.html` |

Core services: Digital Marketing, Website Development, SEO, Paid Ads, AEO (AI search optimisation).
Specialist services: Social Media Management, Local SEO & Google Business Profile, E-commerce, Email & WhatsApp Marketing, Lead Generation & CRM, Conversion Rate Optimisation, Analytics & Tracking, Content Marketing & Link Building, Hosting/Maintenance/Speed.

SEO and AEO extras are built in: LocalBusiness, Service, FAQPage and BreadcrumbList structured data on every page, `sitemap.xml`, `robots.txt` and `llms.txt` (a plain-text summary for AI assistants).

## Editing the site

The pages are plain HTML generated from one content file, so text changes happen in one place:

1. Edit copy, services, FAQs, phone number or cities in `_build/content.py`.
2. Layout and page structure are in `_build/build.py`; styles in `assets/css/styles.css`; scripts in `assets/js/main.js`.
3. Rebuild (Python 3, no dependencies):

   ```bash
   python3 _build/build.py
   ```

4. Commit the regenerated HTML.

**Before launch:** set `SITE_URL` in `_build/content.py` to the real domain and rebuild. It is used for canonical links, Open Graph tags, structured data and the sitemap.

## Hosting

It's a static site: upload the repository contents (everything except `_build/` is needed at runtime) to any web host, cPanel, Netlify, Cloudflare Pages or GitHub Pages. No server or database is required. The contact form opens WhatsApp with the visitor's details pre-filled, so enquiries arrive on 0771 269 979.
