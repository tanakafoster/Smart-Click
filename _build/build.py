# -*- coding: utf-8 -*-
"""Static site generator for the Smart Click Media website.

Usage:  python3 _build/build.py
Writes plain HTML files into the repository root (index.html, services/..., etc.).
Copy lives in _build/content.py and _build/data/*.json. Python 3 standard library only.
"""
import json
import os
import re
import sys
from urllib.parse import quote

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import content as C  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TODAY = "2026-11-07"
SITEMAP = []  # canonical URLs of indexable pages, in build order


def T(tpl, **kw):
    """Tiny template helper: replaces {{name}} with values. Leaves {r} (site root) for page()."""
    for k, v in kw.items():
        tpl = tpl.replace("{{" + k + "}}", str(v))
    return tpl


def esc(s):
    return str(s).replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;").replace(">", "&gt;")


def strip_tags(s):
    return re.sub(r"<[^>]+>", "", s)


def clip(s, n=155):
    s = strip_tags(s)
    return s if len(s) <= n else s[:n].rsplit(" ", 1)[0].rstrip(",;:") + "…"


# ---------------------------------------------------------------------------
# Icons (simple stroke icons drawn for this site)
# ---------------------------------------------------------------------------
ICON_PATHS = {
    "target": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.5"/>',
    "monitor": '<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/>',
    "search": '<circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/>',
    "zap": '<path d="M13 2L4 14h7l-1 8 9-12h-7l1-8z"/>',
    "sparkles": '<path d="M12 3l1.8 4.7L18.5 9.5l-4.7 1.8L12 16l-1.8-4.7L5.5 9.5l4.7-1.8z"/><path d="M19 15l.8 2.2L22 18l-2.2.8L19 21l-.8-2.2L16 18l2.2-.8z"/>',
    "share": '<circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><path d="M8.6 13.5l6.8 4M15.4 6.5l-6.8 4"/>',
    "pin": '<path d="M12 22s7-6.2 7-12a7 7 0 10-14 0c0 5.8 7 12 7 12z"/><circle cx="12" cy="10" r="2.5"/>',
    "cart": '<circle cx="9" cy="20" r="1.5"/><circle cx="18" cy="20" r="1.5"/><path d="M2 3h3l2.7 12.4a2 2 0 002 1.6h8.6a2 2 0 002-1.6L22 7H6"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
    "funnel": '<path d="M3 4h18l-7 9v6l-4 2v-8z"/>',
    "trending": '<path d="M3 17l6-6 4 4 8-8"/><path d="M15 7h6v6"/>',
    "chart": '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
    "pen": '<path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 013 3L7 19l-4 1 1-4z"/>',
    "server": '<rect x="3" y="3" width="18" height="7" rx="2"/><rect x="3" y="14" width="18" height="7" rx="2"/><path d="M7 6.5h.01M7 17.5h.01"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 010 18M12 3a14 14 0 000 18"/>',
    "home": '<path d="M3 11l9-8 9 8v9a1 1 0 01-1 1h-5v-6H9v6H4a1 1 0 01-1-1z"/>',
    "book": '<path d="M4 4h6a3 3 0 013 3v13a2 2 0 00-2-2H4zM20 4h-6a3 3 0 00-3 3v13a2 2 0 012-2h7z"/>',
    "heart": '<path d="M20.8 4.6a5.5 5.5 0 00-7.8 0L12 5.7l-1-1.1a5.5 5.5 0 10-7.8 7.8L12 21l8.8-8.6a5.5 5.5 0 000-7.8z"/>',
    "briefcase": '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M8 7V5a2 2 0 012-2h4a2 2 0 012 2v2M3 13h18"/>',
    "leaf": '<path d="M5 21c0-9 5-15 16-16-1 11-7 16-16 16z"/><path d="M5 21l8-8"/>',
    "car": '<path d="M5 17h14M3 13l2-6h14l2 6v5h-3M3 13v5h3M3 13h18"/><circle cx="7.5" cy="17" r="1.5"/><circle cx="16.5" cy="17" r="1.5"/>',
    "tool": '<path d="M14.7 6.3a4 4 0 00-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 005.4-5.4l-2.5 2.5-2.4-.6-.6-2.4z"/>',
    "coffee": '<path d="M17 8h1a3 3 0 010 6h-1M3 8h14v8a4 4 0 01-4 4H7a4 4 0 01-4-4zM7 2v3M11 2v3M15 2v3"/>',
    "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>',
    "users": '<circle cx="9" cy="8" r="3.5"/><path d="M2 21v-1a6 6 0 0112 0v1"/><circle cx="17" cy="9" r="2.5"/><path d="M16 14.5a5 5 0 016 4.5v2"/>',
    "phone": '<path d="M22 16.9v3a2 2 0 01-2.2 2 19.8 19.8 0 01-8.6-3.1 19.5 19.5 0 01-6-6A19.8 19.8 0 012.1 4.2 2 2 0 014.1 2h3a2 2 0 012 1.7c.1.9.4 1.8.7 2.7a2 2 0 01-.5 2.1L8 9.8a16 16 0 006 6l1.3-1.3a2 2 0 012.1-.4c.9.3 1.8.6 2.7.7a2 2 0 011.7 2z"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/>',
    "eye": '<path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8S1 12 1 12z"/><circle cx="12" cy="12" r="3"/>',
    "award": '<circle cx="12" cy="8" r="6"/><path d="M8.2 13.2L7 22l5-3 5 3-1.2-8.8"/>',
    "message": '<path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z"/>',
    "check": '<path d="M5 12l5 5L20 7"/>',
    "x": '<path d="M18 6L6 18M6 6l12 12"/>',
    "flag": '<path d="M4 22V4M4 4h13l-2 4 2 4H4"/>',
    "play": '<rect x="2" y="5" width="20" height="14" rx="4"/><path d="M10 9l5 3-5 3z"/>',
    "bot": '<rect x="4" y="8" width="16" height="12" rx="3"/><path d="M12 8V5M8.5 13.5h.01M15.5 13.5h.01M9 17h6"/><circle cx="12" cy="4" r="1"/>',
    "layers": '<path d="M12 2l10 5-10 5L2 7z"/><path d="M2 12l10 5 10-5M2 17l10 5 10-5"/>',
    "music": '<path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/>',
    "megaphone": '<path d="M3 11v2a1 1 0 001 1h3l5 4V6L7 10H4a1 1 0 00-1 1z"/><path d="M16 8a5 5 0 010 8M19 5a9 9 0 010 14"/>',
    "camera": '<rect x="2" y="7" width="20" height="14" rx="3"/><circle cx="12" cy="14" r="4"/><path d="M8 7l2-3h4l2 3"/>',
    "grid": '<rect x="3" y="3" width="8" height="8" rx="1"/><rect x="13" y="3" width="8" height="8" rx="1"/><rect x="3" y="13" width="8" height="8" rx="1"/><rect x="13" y="13" width="8" height="8" rx="1"/>',
    "calendar": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
    "compass": '<circle cx="12" cy="12" r="9"/><path d="M15.5 8.5l-2 5-5 2 2-5z"/>',
    "file": '<path d="M14 3H6a2 2 0 00-2 2v14a2 2 0 002 2h12a2 2 0 002-2V9z"/><path d="M14 3v6h6M8 13h8M8 17h5"/>',
    "image": '<rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="9" cy="10" r="2"/><path d="M21 16l-5-5-9 9"/>',
    "map": '<path d="M9 4L3 6v14l6-2 6 2 6-2V4l-6 2z"/><path d="M9 4v14M15 6v14"/>',
}


def icon(name):
    return ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>'
            % ICON_PATHS.get(name, ICON_PATHS["sparkles"]))


WA_SVG = ('<svg viewBox="0 0 32 32" fill="currentColor" aria-hidden="true"><path d="M16 3C8.8 3 3 8.7 3 15.8c0 2.5.7 4.9 2 7L3 29l6.4-2c2 1.1 4.3 1.7 6.6 1.7 7.2 0 13-5.7 13-12.8S23.2 3 16 3zm0 23.4c-2.1 0-4.1-.6-5.9-1.6l-.4-.3-3.8 1.2 1.2-3.7-.3-.4a10.4 10.4 0 01-1.7-5.8C5.1 9.9 10 5.1 16 5.1s10.9 4.8 10.9 10.7S22 26.4 16 26.4zm6-8c-.3-.2-1.9-1-2.2-1.1-.3-.1-.5-.2-.7.2l-1 1.2c-.2.2-.4.2-.7.1-.3-.2-1.4-.5-2.6-1.6-1-.9-1.6-1.9-1.8-2.2-.2-.3 0-.5.1-.7l.5-.6.3-.5c.1-.2 0-.4 0-.6l-1-2.4c-.3-.6-.5-.5-.7-.5h-.6c-.2 0-.6.1-.9.4-.3.3-1.2 1.1-1.2 2.8s1.2 3.2 1.4 3.4c.2.2 2.4 3.6 5.8 5 .8.4 1.4.6 1.9.7.8.3 1.5.2 2.1.1.6-.1 1.9-.8 2.2-1.5.3-.7.3-1.4.2-1.5-.1-.2-.3-.3-.6-.4z"/></svg>')

LOGO_MARK = ('<rect width="48" height="48" rx="13" fill="url(#{id})"/>'
             '<path d="M17 13l17 9.5-7.4 1.7 4.6 8.4-3.6 2-4.6-8.4-5.3 5.2z" fill="#fff"/>'
             '<path d="M12 12.5l-2.6-2.6M17 9.5V6M12 18H8.4" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>')
LOGO_GRAD = ('<linearGradient id="{id}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#2fb3aa"/>'
             '<stop offset="1" stop-color="#0d4f5c"/></linearGradient>')


def logo(gid="lg"):
    svg = ('<svg viewBox="0 0 48 48" aria-hidden="true"><defs>%s</defs>%s</svg>'
           % (LOGO_GRAD.replace("{id}", gid), LOGO_MARK.replace("{id}", gid)))
    return ('<a class="logo" href="{r}index.html" aria-label="%s home">%s<span>Smart Click'
            '<small>Media · Harare</small></span></a>' % (C.BRAND, svg))


def wa_link(text="Hi Smart Click Media, I'd like to talk about growing my business."):
    return "https://wa.me/%s?text=%s" % (C.WA_NUMBER, quote(text))


# ---------------------------------------------------------------------------
# URLs and lookups
# ---------------------------------------------------------------------------
SERVICE_BY = {s["slug"]: s for s in C.SERVICES}
PLATFORM_BY = {p["slug"]: p for p in C.AD_PLATFORMS}
PORTFOLIO_BY = {p["slug"]: p for p in C.PORTFOLIO}
ARTICLE_BY = {a["slug"]: a for a in C.ARTICLES}
LOCATION_BY = {l["slug"]: l for l in C.LOCATIONS}


def url_of(slug):
    """Relative URL (with {r} root placeholder) for any service, platform, project, article or city."""
    if slug in SERVICE_BY:
        return "{r}services/%s/index.html" % slug
    if slug in PLATFORM_BY:
        return "{r}services/paid-ads/%s/index.html" % slug
    if slug in PORTFOLIO_BY:
        return "{r}portfolio/%s/index.html" % slug
    if slug in ARTICLE_BY:
        return "{r}insights/%s/index.html" % slug
    if slug in LOCATION_BY:
        return "{r}locations/%s/index.html" % slug
    raise KeyError("Unknown slug: %s" % slug)


def item_of(slug):
    for table in (SERVICE_BY, PLATFORM_BY, PORTFOLIO_BY, ARTICLE_BY, LOCATION_BY):
        if slug in table:
            return table[slug]
    raise KeyError(slug)


# ---------------------------------------------------------------------------
# Layout
# ---------------------------------------------------------------------------
def header(active):
    services = "".join(
        '<a href="%s"><span class="mi">%s</span><span>%s<em>%s</em></span></a>'
        % (url_of(s["slug"]), icon(s["icon"]), s["name"], clip(s["short"], 60))
        for s in C.SERVICES)
    platforms = "".join(
        '<a href="%s"><span class="mi">%s</span><span>%s</span></a>' % (url_of(p["slug"]), icon(p["icon"]), p["name"])
        for p in C.AD_PLATFORMS)
    ads_menu = ""
    if platforms:
        ads_menu = ('<div class="mega mega-ads">%s<div class="mega-foot"><a href="{r}services/paid-ads/index.html">'
                    'Paid ads overview →</a></div></div>' % platforms)

    def cur(key):
        return ' aria-current="page"' if key == active else ""

    return T("""
<a class="skip-link" href="#main">Skip to content</a>
<div class="topbar"><div class="container">
  <span class="tb-hide">Harare-based digital marketing agency serving all of Zimbabwe · <strong>{{hours}}</strong></span>
  <span><a href="tel:{{tel}}">{{phone}}</a><span class="tb-hide"> · <a href="mailto:{{email}}">{{email}}</a></span></span>
</div></div>
<header class="site-header">
  <div class="container nav">
    {{logo}}
    <nav aria-label="Main">
      <ul class="nav-links">
        <li class="has-mega"><a href="{r}services/index.html"{{c_services}}>Services</a><div class="mega mega-services">{{services}}<div class="mega-foot"><a href="{r}services/index.html">All services →</a><a href="{r}industries/index.html">Industries</a><a href="{r}locations/index.html">Areas we serve</a><a href="{r}faq/index.html">FAQ</a></div></div></li>
        <li class="{{ads_cls}}"><a href="{r}services/paid-ads/index.html"{{c_ads}}>Paid Ads</a>{{ads_menu}}</li>
        <li><a href="{r}portfolio/index.html"{{c_portfolio}}>Portfolio</a></li>
        <li><a href="{r}insights/index.html"{{c_insights}}>Insights</a></li>
        <li><a href="{r}about/index.html"{{c_about}}>About</a></li>
        <li><a href="{r}contact/index.html"{{c_contact}}>Contact</a></li>
      </ul>
    </nav>
    <div class="nav-cta">
      <a class="btn btn-outline" href="tel:{{tel}}">{{phone}}</a>
      <a class="btn btn-primary" href="{r}contact/index.html">Free strategy session</a>
      <button class="menu-toggle" aria-label="Open menu" aria-expanded="false"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>""", hours=C.HOURS, tel=C.PHONE_TEL, phone=C.PHONE_LOCAL, email=C.EMAIL, logo=logo(), services=services,
             ads_cls="has-mega" if ads_menu else "", ads_menu=ads_menu,
             c_services=cur("services"), c_ads=cur("ads"), c_portfolio=cur("portfolio"), c_insights=cur("insights"),
             c_about=cur("about"), c_contact=cur("contact"))


def footer():
    core = [s for s in C.SERVICES if s.get("core")]
    more = [s for s in C.SERVICES if not s.get("core")]
    li = lambda x: '<li><a href="%s">%s</a></li>' % (url_of(x["slug"]), x["name"])
    ads_col = ""
    if C.AD_PLATFORMS:
        ads_col = '<div><h2>Paid ads</h2><ul>%s</ul></div>' % "".join(li(p) for p in C.AD_PLATFORMS)
    return T("""
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        {{logo}}
        <p>A Harare-based digital marketing agency helping businesses across Zimbabwe get found, get chosen and grow, through search, AI, ads, social and websites that sell.</p>
        <ul class="footer-contact">
          <li><strong>Call / WhatsApp:</strong> <a href="tel:{{tel}}">{{phone}}</a></li>
          <li><strong>Email:</strong> <a href="mailto:{{email}}">{{email}}</a></li>
          <li><strong>Hours:</strong> {{hours}}</li>
          <li><strong>Office:</strong> Harare, Zimbabwe</li>
          <li><strong>Serving:</strong> All of Zimbabwe and the diaspora</li>
        </ul>
      </div>
      <div><h2>Core services</h2><ul>{{core}}</ul></div>
      <div><h2>More services</h2><ul>{{more}}</ul></div>
      {{ads_col}}
      <div><h2>Company</h2><ul>
        <li><a href="{r}about/index.html">About us</a></li>
        <li><a href="{r}portfolio/index.html">Portfolio</a></li>
        <li><a href="{r}insights/index.html">Insights</a></li>
        <li><a href="{r}industries/index.html">Industries</a></li>
        <li><a href="{r}locations/index.html">Areas we serve</a></li>
        <li><a href="{r}faq/index.html">FAQ</a></li>
        <li><a href="{r}contact/index.html">Contact</a></li>
        <li><a href="{r}privacy-policy/index.html">Privacy policy</a></li>
        <li><a href="{r}terms/index.html">Terms of service</a></li>
      </ul></div>
    </div>
    <div class="footer-bottom">
      <span>&copy; <span id="year">2026</span> {{brand}}. Harare, Zimbabwe.</span>
      <span>Digital marketing · Websites · SEO · AEO · Paid ads · Google Analytics</span>
    </div>
  </div>
</footer>
<a class="wa-float" href="{{wa}}" target="_blank" rel="noopener" aria-label="Chat with us on WhatsApp">{{wa_svg}}</a>
""", logo=logo("lgf"), tel=C.PHONE_TEL, phone=C.PHONE_LOCAL, email=C.EMAIL, hours=C.HOURS,
             core="".join(li(s) for s in core), more="".join(li(s) for s in more), ads_col=ads_col,
             brand=C.BRAND, wa=wa_link(), wa_svg=WA_SVG)


def org_schema():
    offers = [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": s["name"]}} for s in C.SERVICES]
    offers += [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": p["name"]}} for p in C.AD_PLATFORMS]
    return {
        "@context": "https://schema.org",
        "@type": ["LocalBusiness", "ProfessionalService"],
        "@id": C.SITE_URL + "/#organization",
        "name": C.BRAND,
        "alternateName": "Smart Click",
        "url": C.SITE_URL + "/",
        "logo": C.SITE_URL + "/assets/img/logo.svg",
        "image": C.SITE_URL + "/assets/img/og-image.svg",
        "telephone": C.PHONE_INTL,
        "email": C.EMAIL,
        "description": "Digital marketing agency in Harare, Zimbabwe offering digital marketing, website development, SEO, AEO, paid ads on every major platform, Google Analytics, social media and e-commerce to businesses across Zimbabwe.",
        "address": {"@type": "PostalAddress", "addressLocality": C.CITY, "addressRegion": "Harare", "addressCountry": "ZW"},
        "openingHoursSpecification": [{
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            "opens": "00:00", "closes": "23:59"}],
        "areaServed": [{"@type": "Country", "name": C.COUNTRY}] + [{"@type": "City", "name": c} for c in C.CITIES[:10]],
        "knowsAbout": [s["name"] for s in C.SERVICES] + [p["name"] for p in C.AD_PLATFORMS],
        "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Digital marketing services", "itemListElement": offers},
    }


def faq_schema(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": strip_tags(q),
                            "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}} for q, a in faqs]}


def breadcrumb_schema(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": C.SITE_URL + "/" + u}
                                for i, (n, u) in enumerate(items)]}


GA_SNIPPET = """<script async src="https://www.googletagmanager.com/gtag/js?id={{id}}"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','{{id}}');</script>"""


def page(path, title, description, body, active="", schemas=None, root=None, index=True, crumbs=None):
    depth = path.count("/")
    if root is None:
        root = "../" * depth
    url_path = path[:-len("index.html")] if path.endswith("index.html") else path
    canonical = C.SITE_URL + "/" + url_path
    schemas = [org_schema()] + (schemas or [])
    if crumbs:
        schemas.append(breadcrumb_schema(crumbs))
    ld = "\n".join('<script type="application/ld+json">%s</script>' % json.dumps(s, ensure_ascii=False) for s in schemas)
    # Keep titles near the ~60 character display limit: only add the brand when there is room
    full_title = title if (C.BRAND in title or len(title) > 44 or " | " in title) else "%s | %s" % (title, C.BRAND)
    ga = T(GA_SNIPPET, id=C.GA_MEASUREMENT_ID) if C.GA_MEASUREMENT_ID else ""
    html = T("""<!doctype html>
<html lang="en-ZW">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<script>document.documentElement.className+=" js"</script>
<title>{{title}}</title>
<meta name="description" content="{{desc}}">
{{robots}}<link rel="canonical" href="{{canonical}}">
<meta name="geo.region" content="ZW-HA">
<meta name="geo.placename" content="Harare">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{{brand}}">
<meta property="og:title" content="{{title}}">
<meta property="og:description" content="{{desc}}">
<meta property="og:url" content="{{canonical}}">
<meta property="og:image" content="{{site}}/assets/img/og-image.svg">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0b2530">
<link rel="icon" href="{r}assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}assets/css/styles.css">
{{ga}}
{{ld}}
</head>
<body>
{{header}}
<main id="main">
{{body}}
</main>
{{footer}}
<script src="{r}assets/js/main.js" defer></script>
</body>
</html>
""", title=esc(full_title), desc=esc(description), canonical=canonical, brand=C.BRAND, site=C.SITE_URL,
             robots="" if index else '<meta name="robots" content="noindex">\n', ga=ga, ld=ld,
             header=header(active), body=body, footer=footer())
    html = html.replace("{r}", root)
    out = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    if index:
        SITEMAP.append(canonical)
    return canonical


# ---------------------------------------------------------------------------
# Reusable sections
# ---------------------------------------------------------------------------
def cta_band(heading="Ready to grow? Let's talk.",
             text="Book a free, no-obligation strategy session. We'll look at your current marketing, point out the quick wins and give you an honest plan, whether or not you hire us."):
    return T("""
<section class="section-sm"><div class="container">
  <div class="cta-band reveal">
    <div>
      <h2>{{h}}</h2>
      <p>{{t}}</p>
      <div class="btn-row">
        <a class="btn btn-primary" href="{r}contact/index.html">Book my free session</a>
        <a class="btn btn-outline" href="{{wa}}" target="_blank" rel="noopener">WhatsApp us</a>
      </div>
    </div>
    <div class="cta-contact">
      <span class="cta-label">Call or WhatsApp, any time</span>
      <a class="cta-phone" href="tel:{{tel}}">{{phone}}</a>
      <a class="cta-email" href="mailto:{{email}}">{{email}}</a>
      <span class="cta-hours">{{hours}}</span>
    </div>
  </div>
</div></section>""", h=heading, t=text, wa=wa_link(), tel=C.PHONE_TEL, phone=C.PHONE_LOCAL, email=C.EMAIL,
             hours=C.HOURS_LONG)


def card_for(slug, badge=None):
    x = item_of(slug)
    if slug in PORTFOLIO_BY:
        return portfolio_card(x)
    if slug in ARTICLE_BY:
        return article_card(x)
    b = ""
    if badge is None and x.get("core"):
        b = '<span class="badge">Core</span>'
    elif badge:
        b = '<span class="badge">%s</span>' % badge
    title = x.get("name") or x.get("city")
    short = x.get("short") or x.get("summary") or clip(x.get("intro", ""), 150)
    return T("""<a class="card service-card reveal" href="{{href}}">{{badge}}
  <div class="icon">{{icon}}</div><h3>{{name}}</h3><p>{{short}}</p><span class="more">Learn more →</span></a>""",
             href=url_of(slug), badge=b, icon=icon(x.get("icon", "map")), name=title, short=short)


def faq_block(faqs):
    return '<div class="faq">' + "".join(
        "<details><summary>%s</summary><div><p>%s</p></div></details>" % (q, a) for q, a in faqs) + "</div>"


def cities_block():
    return '<div class="cities">' + "".join(
        '<span class="%s">%s</span>' % ("hq" if c == C.CITY else "", c + (" (HQ)" if c == C.CITY else ""))
        for c in C.CITIES) + "</div>"


def steps_html(steps):
    cls = "steps five" if len(steps) == 5 else "steps"
    return '<div class="%s">' % cls + "".join(
        '<div class="step reveal"><h3>%s</h3><p>%s</p></div>' % (t, d) for t, d in steps) + "</div>"


def page_hero(eyebrow, h1, lead, crumbs, buttons=True, extra=""):
    crumb_html = '<nav class="breadcrumb" aria-label="Breadcrumb"><a href="{r}index.html">Home</a>' + "".join(
        " / " + ('<a href="%s">%s</a>' % (href, name) if href else '<span aria-current="page">%s</span>' % name)
        for name, href in crumbs) + "</nav>"
    btns = ""
    if buttons:
        btns = ('<div class="btn-row"><a class="btn btn-primary" href="{r}contact/index.html">Get a free strategy session</a>'
                '<a class="btn btn-outline" href="%s" target="_blank" rel="noopener">WhatsApp %s</a></div>' % (wa_link(), C.PHONE_LOCAL))
    return ('<section class="hero page-hero"><div class="container">%s<span class="eyebrow">%s</span><h1>%s</h1>'
            '<p class="lead">%s</p>%s%s</div></section>' % (crumb_html, eyebrow, h1, lead, extra, btns))


PROCESS = [
    ("Free strategy session", "We learn about your business, goals and numbers, and look at what you're doing now."),
    ("Audit & plan", "You get an honest audit and a 90-day plan with clear targets, budgets and channels."),
    ("Launch", "Campaigns, pages and tracking go live on a launch date we agree together at the start."),
    ("Report & grow", "Ongoing optimisation, a plain-English monthly report and a regular review call."),
]

PRINCIPLES = [
    ("shield", "Your accounts, your data", "Ad accounts, analytics, website and domain are set up in your business's name. You can see every dollar spent and every task done."),
    ("users", "Specialists who stay close", "The people who plan your strategy are the people who run it day to day, so nothing gets lost in hand-overs."),
    ("chart", "Measured in customers", "Our reports lead with enquiries, sales and revenue from ads. Likes and impressions come second."),
    ("award", "Careful, thorough work", "Solid keyword research, clean tracking and properly tested creative: the groundwork that makes campaigns pay."),
    ("message", "Local know-how", "We understand Zimbabwean buyers, mobile-first browsing, WhatsApp culture and the diaspora market."),
    ("clock", "Open 24/7", "Call or WhatsApp us whenever it suits you. We're open around the clock, every day of the week."),
]


# ---------------------------------------------------------------------------
# Portfolio and article cards (also used on the home page)
# ---------------------------------------------------------------------------
def mockup(p, size=""):
    m = p.get("mock", {})
    return T("""<div class="mock {{size}}" style="--m1:{{c1}};--m2:{{c2}}" aria-hidden="true">
  <div class="mock-bar"><i></i><i></i><i></i></div>
  <div class="mock-body">
    <div class="mock-nav"><b>{{label}}</b><span></span><span></span><span></span></div>
    <div class="mock-hero"><strong>{{headline}}</strong><span class="ln"></span><span class="ln short"></span><em>{{cta}}</em></div>
    <div class="mock-cards"><span></span><span></span><span></span></div>
  </div>
</div>""", size=size, c1=m.get("color1", "#0b2530"), c2=m.get("color2", "#4fbfb8"), label=esc(m.get("label", p["sector"])),
             headline=esc(m.get("headline", p["title"])), cta=esc(m.get("cta", "Get a quote")))


def portfolio_card(p):
    tags = "".join('<span class="tag">%s</span>' % item_of(s)["name"] for s in p["services"][:3])
    return T("""<a class="card portfolio-card reveal" href="{{href}}">
  {{mock}}
  <div class="pc-body"><span class="badge badge-soft">Example project</span><h3>{{title}}</h3><p>{{summary}}</p><div class="tags">{{tags}}</div></div></a>""",
             href=url_of(p["slug"]), mock=mockup(p), title=p["title"], summary=p["summary"], tags=tags)


def article_card(a):
    return T("""<a class="card article-card reveal" href="{{href}}">
  <span class="eyebrow">{{cat}}</span><h3>{{title}}</h3><p>{{desc}}</p>
  <span class="meta">{{mins}} min read</span><span class="more">Read article →</span></a>""",
             href=url_of(a["slug"]), cat=a["category"], title=a["title"], desc=a["description"], mins=a["read_mins"])


# ---------------------------------------------------------------------------
# Home
# ---------------------------------------------------------------------------
AI_QUESTIONS = [
    "Which solar installers in Harare have the best reviews?",
    "What are good private schools in Bulawayo?",
    "Who builds affordable websites in Zimbabwe?",
    "Best lodges near Victoria Falls for a family weekend?",
    "Which accounting firms in Harare help small businesses?",
    "Where can I buy building materials in Mutare?",
]


def build_home():
    core = [s for s in C.SERVICES if s.get("core")]
    rest = [s for s in C.SERVICES if not s.get("core")]
    channels = ["Google Search", "Google Maps", "ChatGPT", "Gemini", "Perplexity", "Google AI Overviews", "Microsoft Copilot",
                "YouTube", "Facebook", "Instagram", "WhatsApp", "TikTok", "LinkedIn", "Bing"]
    marquee = "".join("<span>%s</span>" % c for c in channels * 2)
    ads_grid = ""
    if C.AD_PLATFORMS:
        ads_grid = '<div class="platform-chips">' + "".join(
            '<a class="pchip reveal" href="%s"><span class="mi">%s</span>%s</a>' % (url_of(p["slug"]), icon(p["icon"]), p["name"])
            for p in C.AD_PLATFORMS) + "</div>"
    portfolio_sec = ""
    if C.PORTFOLIO:
        portfolio_sec = T("""
<section class="section">
  <div class="container">
    <div class="center"><span class="eyebrow">Portfolio</span><h2>The kind of work we do</h2>
    <p class="lead">Example projects that show how we approach websites, search and advertising for Zimbabwean businesses.</p></div>
    <div class="grid grid-3" style="margin-top:44px">{{cards}}</div>
    <p class="center" style="margin-top:28px"><a class="btn btn-dark" href="{r}portfolio/index.html">View the portfolio</a></p>
  </div>
</section>""", cards="".join(portfolio_card(p) for p in C.PORTFOLIO[:3]))
    insights_sec = ""
    if C.ARTICLES:
        insights_sec = T("""
<section class="section bg-soft">
  <div class="container">
    <div class="center"><span class="eyebrow">Insights</span><h2>Practical guides for Zimbabwean businesses</h2></div>
    <div class="grid grid-3" style="margin-top:44px">{{cards}}</div>
    <p class="center" style="margin-top:28px"><a href="{r}insights/index.html">See all articles →</a></p>
  </div>
</section>""", cards="".join(article_card(a) for a in C.ARTICLES[:3]))

    body = T("""
<section class="hero">
  <div class="container hero-grid">
    <div>
      <span class="eyebrow">Digital marketing agency · Harare, Zimbabwe · Open 24/7</span>
      <h1>Get found. Get chosen. <span class="hl">Grow across Zimbabwe.</span></h1>
      <p class="lead">Smart Click Media helps Zimbabwean businesses win more customers through SEO, AI search (AEO), paid ads on every major platform, Google Analytics, social media and websites built to sell. Based in Harare, working with brands in every province.</p>
      <div class="btn-row">
        <a class="btn btn-primary" href="{r}contact/index.html">Get my free strategy session</a>
        <a class="btn btn-outline" href="tel:{{tel}}">Call {{phone}}</a>
      </div>
      <div class="hero-badges">
        <span class="chip"><b>●</b> SEO &amp; AEO</span>
        <span class="chip"><b>●</b> Google, Meta, LinkedIn &amp; ChatGPT ads</span>
        <span class="chip"><b>●</b> Google Analytics</span>
        <span class="chip"><b>●</b> Websites &amp; e-commerce</span>
      </div>
    </div>
    <div class="hero-card" aria-hidden="true">
      <div class="hc-top"><span class="dots"><i></i><i></i><i></i></span><span>Illustration: where buyers find you</span></div>
      <div class="hc-search">{{search}} digital marketing agency in Harare</div>
      <div class="hc-result"><span class="tag">Search result</span><b>Your Business · Harare, Zimbabwe</b><small>yourbusiness.co.zw</small><br>Call or WhatsApp today for a free quote…</div>
      <div class="hc-ai"><strong>AI answer:</strong> For this in Zimbabwe, one option to consider is <strong>Your Business</strong>, based in Harare and serving clients nationwide…</div>
      <div class="hc-bars"><i style="height:30%"></i><i style="height:42%"></i><i style="height:38%"></i><i style="height:55%"></i><i style="height:63%"></i><i style="height:72%"></i><i style="height:86%"></i><i style="height:100%"></i></div>
    </div>
  </div>
</section>

<div class="marquee" aria-label="Where we help you show up"><div class="marquee-track">{{marquee}}</div></div>

<section class="section">
  <div class="container">
    <div class="center">
      <span class="eyebrow">What we do</span>
      <h2>Six core services. One goal: more customers.</h2>
      <p class="lead">Whether people find you on Google, ask an AI assistant, scroll Facebook or land on your website, we make sure you show up, get chosen, and can see exactly what it's worth.</p>
    </div>
    <div class="grid grid-3" style="margin-top:48px">{{core}}
      <a class="card more-card reveal" href="{r}services/index.html">
        <div class="icon">{{spark}}</div>
        <div><h3>+ {{nrest}} more specialist services</h3>
        <p>Social media, local SEO, e-commerce, email &amp; WhatsApp marketing, lead generation &amp; CRM, conversion optimisation, content and hosting.</p></div>
        <span class="more">See all services →</span>
      </a>
    </div>
  </div>
</section>

<section class="section bg-dark">
  <div class="container">
    <div class="split">
      <div>
        <span class="eyebrow">Paid ads</span>
        <h2>All the major ad platforms, <span class="hl">one accountable team</span></h2>
        <p class="lead">Search, social, video, messaging, professional networks and the new ad slots inside AI assistants. We plan your budget across the platforms that suit your customers and are open to your business, and track every campaign through to enquiries and sales.</p>
        <div class="btn-row"><a class="btn btn-primary" href="{r}services/paid-ads/index.html">Explore paid ads</a></div>
      </div>
      <div>{{ads_grid}}</div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container split">
    <div class="panel reveal">
      <span class="eyebrow">AI search</span>
      <h2>Your customers now ask AI. Does it mention you?</h2>
      <p>Instead of scrolling through search results, many buyers ask ChatGPT, Gemini, Copilot or Google's AI answers for a recommendation, then contact the one or two names they're given.</p>
      <p>Our AEO service makes your business easy for those tools to understand and trust, then checks every month how often you're named.</p>
      <div class="btn-row"><a class="btn btn-dark" href="{r}services/aeo/index.html">Explore AEO</a><a class="btn btn-outline btn-ink" href="{r}services/seo/index.html">Our SEO service</a></div>
    </div>
    <div class="reveal">
      <h3 class="q-title">Questions like these get asked every day</h3>
      <ul class="ai-questions">{{questions}}</ul>
      <p class="form-note">Examples of the kinds of questions we track across ChatGPT, Gemini, Copilot, Perplexity and Google.</p>
    </div>
  </div>
</section>

<section class="section bg-dark">
  <div class="container">
    <div class="split">
      <div>
        <span class="eyebrow">Why Smart Click</span>
        <h2>We judge marketing the way you judge your business: <span class="hl">in customers and cash</span></h2>
        <p class="lead">Plenty of Zimbabwean businesses have paid for marketing that kept someone busy without growing their sales. We set clear targets, track every enquiry back to where it came from, and tell you plainly what's working.</p>
        <div class="btn-row"><a class="btn btn-primary" href="{r}about/index.html">How we work</a></div>
      </div>
      <div class="grid grid-2">{{principles}}</div>
    </div>
  </div>
</section>

<section class="section bg-soft">
  <div class="container">
    <div class="center"><span class="eyebrow">How it works</span><h2>From first call to growing revenue</h2></div>
    <div style="margin-top:48px">{{process}}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="center"><span class="eyebrow">More ways we help</span><h2>Everything you need to grow online, under one roof</h2></div>
    <div class="grid grid-4" style="margin-top:48px">{{rest}}</div>
  </div>
</section>
{{portfolio}}
<section class="section bg-dark">
  <div class="container center">
    <span class="eyebrow">Based in Harare. Serving the whole nation.</span>
    <h2>From Harare to Victoria Falls, and the diaspora</h2>
    <p class="lead">Our team works from Harare, and our clients are everywhere. We run campaigns targeting every province of Zimbabwe, plus Zimbabweans living in South Africa, the UK, the US and Australia.</p>
    {{cities}}
    <p style="margin-top:28px"><a class="btn btn-outline" href="{r}locations/index.html">Areas we serve</a></p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="center"><span class="eyebrow">Working together</span><h2>What to expect when you work with us</h2></div>
    <div class="grid grid-3" style="margin-top:44px">
      <div class="card reveal"><div class="icon">{{i_cal}}</div><h3>In the first week</h3><p>A strategy session, access to your accounts, and a review of your website, ads, analytics and Google Business Profile.</p></div>
      <div class="card reveal"><div class="icon">{{i_flag}}</div><h3>In the first month</h3><p>A written plan with targets, tracking fixed or set up, and your first campaigns and improvements live.</p></div>
      <div class="card reveal"><div class="icon">{{i_chart}}</div><h3>Every month after that</h3><p>Ongoing optimisation, a plain-English report on enquiries and sales, and a review call to agree next steps.</p></div>
    </div>
  </div>
</section>
{{insights}}
<section class="section">
  <div class="container">
    <div class="center"><span class="eyebrow">FAQ</span><h2>Questions we get asked a lot</h2></div>
    <div style="margin-top:40px">{{faq}}</div>
    <p class="center" style="margin-top:24px"><a href="{r}faq/index.html">See all FAQs →</a></p>
  </div>
</section>
{{cta}}
""", tel=C.PHONE_TEL, phone=C.PHONE_LOCAL, search=icon("search"), marquee=marquee,
             core="".join(card_for(s["slug"]) for s in core), spark=icon("sparkles"), nrest=len(rest),
             ads_grid=ads_grid, questions="".join("<li>%s%s</li>" % (icon("message"), q) for q in AI_QUESTIONS),
             principles="".join('<div class="card card-dark reveal"><div class="icon">%s</div><h3>%s</h3><p>%s</p></div>'
                                % (icon(i), t, d) for i, t, d in PRINCIPLES[:4]),
             process=steps_html(PROCESS), rest="".join(card_for(s["slug"]) for s in rest), portfolio=portfolio_sec,
             cities=cities_block(), i_cal=icon("calendar"), i_flag=icon("flag"), i_chart=icon("chart"),
             insights=insights_sec, faq=faq_block(C.FAQS_GENERAL[:5]), cta=cta_band())
    page("index.html", "Smart Click Media | Digital Marketing Agency in Harare, Zimbabwe",
         "Harare digital marketing agency for all of Zimbabwe, open 24/7: SEO, AEO, Google, Meta, LinkedIn and ChatGPT ads, analytics and websites. Call 0771 269 979.",
         body, "home", [faq_schema(C.FAQS_GENERAL[:5])])


# ---------------------------------------------------------------------------
# Services and ad-platform pages
# ---------------------------------------------------------------------------
def lower_name(x):
    n = x["name"]
    if x.get("group"):  # ad platforms are proper names
        return n
    keep = ("SEO", "AEO", "CRO", "Google", "Meta", "TikTok", "LinkedIn", "YouTube", "Microsoft", "ChatGPT", "WhatsApp", "E-commerce")
    if any(n.startswith(k) for k in keep) or x["slug"] in ("seo", "aeo", "cro"):
        return n
    return n[0].lower() + n[1:]


def platforms_section():
    if not C.AD_PLATFORMS:
        return ""
    groups = []
    seen = []
    for p in C.AD_PLATFORMS:
        g = p.get("group", "Other platforms")
        if g not in seen:
            seen.append(g)
    for g in seen:
        cards = "".join(card_for(p["slug"], badge=p.get("badge", "")) for p in C.AD_PLATFORMS if p.get("group", "Other platforms") == g)
        groups.append('<h3 class="group-title">%s</h3><div class="grid grid-3">%s</div>' % (g, cards))
    return T("""
<section class="section bg-soft" id="platforms">
  <div class="container">
    <div class="center"><span class="eyebrow">Platforms we manage</span><h2>All the major platforms, in one plan</h2>
    <p class="lead">Pick one platform or let us build a mix. Each page explains what we run there, who it suits, where it is available and what to expect.</p></div>
    <div class="platform-groups">{{groups}}</div>
  </div>
</section>""", groups="".join(groups))


def build_service(s, parent=None):
    included = "".join('<div class="card reveal"><div class="icon">%s</div><h3>%s</h3><p>%s</p></div>'
                       % (icon("check"), t, d) for t, d in s["included"])
    problems = "".join("<li>%s</li>" % p for p in s["problems"])
    related = "".join(card_for(r) for r in s.get("related", []) if r != s["slug"])
    crumbs = [("Services", "{r}services/index.html")]
    crumb_ld = [("Home", ""), ("Services", "services/")]
    if parent:
        crumbs.append((parent["name"], url_of(parent["slug"])))
        crumb_ld.append((parent["name"], "services/%s/" % parent["slug"]))
        path = "services/paid-ads/%s/index.html" % s["slug"]
        crumb_ld.append((s["name"], "services/paid-ads/%s/" % s["slug"]))
    else:
        path = "services/%s/index.html" % s["slug"]
        crumb_ld.append((s["name"], "services/%s/" % s["slug"]))
    crumbs.append((s["name"], None))
    note = ""
    if s.get("note"):
        note = '<p class="hero-note">%s %s</p>' % (icon("clock"), s["note"])
    body = page_hero("%s · Harare, Zimbabwe" % s["name"], s["h1"], s["intro"], crumbs, extra=note)
    if s["slug"] == "paid-ads":
        body += platforms_section()
    body += T("""
<section class="section">
  <div class="container split">
    <div class="reveal">
      <span class="eyebrow">Sound familiar?</span>
      <h2>The problems we fix</h2>
      <ul class="xlist">{{problems}}</ul>
    </div>
    <div class="panel-dark reveal">
      <h3>What you get with Smart Click</h3>
      <ul class="checklist">
        <li>A specialist who knows your account and your goals</li>
        <li>A clear plan with targets tied to enquiries and sales</li>
        <li>Full access to your accounts, data and reports</li>
        <li>Plain-English monthly reporting and a review call</li>
        <li>Open 24/7 by phone and WhatsApp</li>
      </ul>
      <a class="btn btn-primary" href="tel:{{tel}}">Call {{phone}}</a>
    </div>
  </div>
</section>
<section class="section bg-soft">
  <div class="container">
    <div class="center"><span class="eyebrow">What's included</span><h2>{{inc_title}}</h2></div>
    <div class="grid grid-3" style="margin-top:48px">{{included}}</div>
  </div>
</section>
<section class="section bg-dark">
  <div class="container">
    <div class="center"><span class="eyebrow">Our approach</span><h2>How we deliver {{lname}}</h2></div>
    <div style="margin-top:48px">{{steps}}</div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="center"><span class="eyebrow">FAQ</span><h2>{{name}} questions, answered</h2></div>
    <div style="margin-top:40px">{{faq}}</div>
  </div>
</section>
<section class="section bg-soft">
  <div class="container">
    <div class="center"><span class="eyebrow">Works well with</span><h2>Related services</h2></div>
    <div class="grid grid-3" style="margin-top:40px">{{related}}</div>
  </div>
</section>
{{cta}}
""", problems=problems, tel=C.PHONE_TEL, phone=C.PHONE_LOCAL, included=included,
              inc_title=s.get("included_title") or "Our %s service" % lower_name(s), lname=lower_name(s), name=s["name"],
              steps=steps_html(s["steps"]), faq=faq_block(s["faqs"]), related=related,
              cta=cta_band("Let's talk about %s for your business" % lower_name(s)))
    service_ld = {"@context": "https://schema.org", "@type": "Service", "name": s["name"], "serviceType": s["name"],
                  "description": strip_tags(s["short"]), "provider": {"@id": C.SITE_URL + "/#organization"},
                  "areaServed": {"@type": "Country", "name": C.COUNTRY}}
    page(path, s["title"], s.get("description") or clip(s["intro"]), body, "ads" if (parent or s["slug"] == "paid-ads") else "services",
         [service_ld, faq_schema(s["faqs"])], crumbs=crumb_ld)


def build_services_index():
    core = [s for s in C.SERVICES if s.get("core")]
    rest = [s for s in C.SERVICES if not s.get("core")]
    ads = ""
    if C.AD_PLATFORMS:
        ads = T("""<section class="section"><div class="container">
  <div class="center"><span class="eyebrow">Paid ads platforms</span><h2>Advertising, wherever your customers are</h2></div>
  <div class="grid grid-3" style="margin-top:40px">{{cards}}</div>
</div></section>""", cards="".join(card_for(p["slug"], badge=p.get("badge", "")) for p in C.AD_PLATFORMS))
    body = page_hero("Our services", "Every service you need to <span class=\"hl\">grow online</span> in Zimbabwe",
                     "%d specialist services and %d ad platforms, one joined-up team. Start with the one you need most, and we'll connect it to everything else."
                     % (len(C.SERVICES), len(C.AD_PLATFORMS)), [("Services", None)])
    body += T("""
<section class="section"><div class="container">
  <div class="center"><span class="eyebrow">Core services</span><h2>Where most clients start</h2></div>
  <div class="grid grid-3" style="margin-top:40px">{{core}}</div>
</div></section>
<section class="section bg-soft"><div class="container">
  <div class="center"><span class="eyebrow">Specialist services</span><h2>Go further</h2></div>
  <div class="grid grid-4" style="margin-top:40px">{{rest}}</div>
</div></section>
{{ads}}
<section class="section bg-dark"><div class="container">
  <div class="center"><span class="eyebrow">How we work</span><h2>One process, every service</h2></div>
  <div style="margin-top:48px">{{process}}</div>
</div></section>
{{cta}}""", core="".join(card_for(s["slug"]) for s in core), rest="".join(card_for(s["slug"]) for s in rest), ads=ads,
              process=steps_html(PROCESS), cta=cta_band())
    page("services/index.html", "Digital Marketing Services in Zimbabwe",
         "SEO, AEO, paid ads on every platform, Google Analytics, websites, social media, e-commerce and WhatsApp marketing from Smart Click Media in Harare.",
         body, "services", crumbs=[("Home", ""), ("Services", "services/")])


# ---------------------------------------------------------------------------
# Portfolio
# ---------------------------------------------------------------------------
EXAMPLE_NOTE = ("These are example projects: illustrations of how we would plan and deliver work for businesses like these. "
                "They are not past client engagements, and the businesses shown are not real clients.")
EXAMPLE_NOTE_ONE = ("This is an example project: an illustration of how we would plan and deliver work for a business like this. "
                    "It is not a past client engagement, and the business described is not a real client.")


def build_portfolio_index():
    body = page_hero("Portfolio", "Our portfolio of <span class=\"hl\">example projects</span>",
                     "A look at how we approach websites, search, AI visibility and advertising for different kinds of Zimbabwean businesses.",
                     [("Portfolio", None)], buttons=False)
    body += T("""
<section class="section"><div class="container">
  <p class="notice">{{note}}</p>
  <h2 class="sr-only">Example projects</h2>
  <div class="grid grid-3" style="margin-top:32px">{{cards}}</div>
</div></section>
{{cta}}""", note=EXAMPLE_NOTE, cards="".join(portfolio_card(p) for p in C.PORTFOLIO),
              cta=cta_band("Want results like these for your business?", "Tell us about your goals, and we'll show you how we'd plan your project. Real client work can be added here as projects complete."))
    page("portfolio/index.html", "Portfolio | Example Digital Marketing Projects",
         "Example website, SEO, AEO and paid ads projects showing how Smart Click Media approaches work for Zimbabwean businesses.",
         body, "portfolio", crumbs=[("Home", ""), ("Portfolio", "portfolio/")])


def build_portfolio_item(p):
    approach = "".join('<div class="step reveal"><h3>%s</h3><p>%s</p></div>' % (t, d) for t, d in p["approach"])
    services = "".join(card_for(s) for s in p["services"][:3])
    body = page_hero("Example project · %s" % p["sector"], p["title"], p["summary"],
                     [("Portfolio", "{r}portfolio/index.html"), (p["title"], None)], buttons=False)
    body += T("""
<section class="section"><div class="container">
  <p class="notice">{{note}}</p>
  <div class="split" style="margin-top:36px">
    <div class="reveal">
      <span class="eyebrow">The brief</span><h2>What the business needs</h2>
      <p>{{brief}}</p>
      <h3 style="margin-top:28px">The challenge</h3>
      <p>{{challenge}}</p>
    </div>
    <div class="reveal">{{mock}}</div>
  </div>
</div></section>
<section class="section bg-dark"><div class="container">
  <div class="center"><span class="eyebrow">Our approach</span><h2>How we would tackle it</h2></div>
  <div class="steps" style="margin-top:48px">{{approach}}</div>
</div></section>
<section class="section"><div class="container split" style="align-items:start">
  <div class="reveal"><span class="eyebrow">Deliverables</span><h2>What we would deliver</h2><ul class="checklist">{{deliverables}}</ul></div>
  <div class="panel reveal"><h3>How we would measure success</h3><ul class="checklist">{{measure}}</ul></div>
</div></section>
<section class="section bg-soft"><div class="container">
  <div class="center"><span class="eyebrow">Services involved</span><h2>The services behind this project</h2></div>
  <div class="grid grid-3" style="margin-top:40px">{{services}}</div>
</div></section>
{{cta}}""", note=EXAMPLE_NOTE_ONE, brief=p["brief"], challenge=p["challenge"], mock=mockup(p, "mock-lg"), approach=approach,
              deliverables="".join("<li>%s</li>" % d for d in p["deliverables"]),
              measure="".join("<li>%s</li>" % m for m in p["measure"]), services=services,
              cta=cta_band("Have a project like this?", "Tell us what you're working on, and we'll put together a plan and a quote."))
    page("portfolio/%s/index.html" % p["slug"], "Example project: %s" % p["sector"], p.get("description") or clip(p["summary"]), body, "portfolio",
         crumbs=[("Home", ""), ("Portfolio", "portfolio/"), (p["title"], "portfolio/%s/" % p["slug"])])


# ---------------------------------------------------------------------------
# Insights (articles)
# ---------------------------------------------------------------------------
def build_insights_index():
    body = page_hero("Insights", "Guides and ideas for <span class=\"hl\">growing online in Zimbabwe</span>",
                     "Practical, plain-English articles on search, AI, advertising, analytics and websites, written for Zimbabwean businesses.",
                     [("Insights", None)], buttons=False)
    body += T("""
<section class="section"><div class="container">
  <h2 class="sr-only">Latest articles</h2>
  <div class="grid grid-3">{{cards}}</div>
</div></section>
{{cta}}""", cards="".join(article_card(a) for a in C.ARTICLES), cta=cta_band())
    page("insights/index.html", "Insights | Digital Marketing Guides for Zimbabwe",
         "Articles and guides from Smart Click Media on SEO, AEO, paid ads, Google Analytics, WhatsApp marketing and websites for Zimbabwean businesses.",
         body, "insights", crumbs=[("Home", ""), ("Insights", "insights/")])


def build_article(a):
    related = "".join(card_for(r) for r in a.get("related", []))
    faqs = a.get("faqs") or []
    faq_html = ""
    if faqs:
        faq_html = '<section class="section bg-soft"><div class="container"><div class="center"><h2>Frequently asked questions</h2></div><div style="margin-top:32px">%s</div></div></section>' % faq_block(faqs)
    meta = '<p class="article-meta">%s · %s min read · By the Smart Click Media team</p>' % (
        "7 November 2026" if a.get("date", TODAY) == TODAY else a["date"], a["read_mins"])
    body = page_hero(a["category"], a["title"], a["description"],
                     [("Insights", "{r}insights/index.html"), (a["title"], None)], buttons=False, extra=meta)
    body += T("""
<section class="section"><div class="container">
  <article class="prose article-body">
    <p class="article-intro">{{intro}}</p>
    {{body}}
  </article>
</div></section>
{{faq}}
<section class="section"><div class="container">
  <div class="center"><span class="eyebrow">Need a hand?</span><h2>Services that can help</h2></div>
  <div class="grid grid-3" style="margin-top:40px">{{related}}</div>
</div></section>
{{cta}}""", intro=a["intro"], body=a["body"], faq=faq_html, related=related, cta=cta_band())
    ld = {"@context": "https://schema.org", "@type": "BlogPosting", "headline": a["title"], "description": a["description"],
          "datePublished": a.get("date", TODAY), "dateModified": a.get("date", TODAY),
          "author": {"@type": "Organization", "name": C.BRAND}, "publisher": {"@id": C.SITE_URL + "/#organization"},
          "mainEntityOfPage": C.SITE_URL + "/insights/%s/" % a["slug"], "image": C.SITE_URL + "/assets/img/og-image.svg"}
    schemas = [ld] + ([faq_schema(faqs)] if faqs else [])
    page("insights/%s/index.html" % a["slug"], a.get("seo_title") or a["title"], clip(a["description"]), body, "insights", schemas,
         crumbs=[("Home", ""), ("Insights", "insights/"), (a["title"], "insights/%s/" % a["slug"])])


# ---------------------------------------------------------------------------
# Locations
# ---------------------------------------------------------------------------
def build_locations_index():
    cards = "".join(card_for(l["slug"]) for l in C.LOCATIONS)
    body = page_hero("Areas we serve", "Digital marketing for businesses <span class=\"hl\">across Zimbabwe</span>",
                     "We're based in Harare and work with businesses in every province, online, on WhatsApp and by phone, any time of day.",
                     [("Areas we serve", None)])
    body += T("""
<section class="section"><div class="container">
  <h2 class="sr-only">Cities we serve</h2>
  <div class="grid grid-3">{{cards}}
    <a class="card service-card reveal" href="{r}index.html"><div class="icon">{{pin}}</div><h3>Harare (our home base)</h3><p>Our team is in Harare, serving the CBD, the suburbs and businesses across the capital and Chitungwiza.</p><span class="more">Learn more →</span></a>
  </div>
</div></section>
<section class="section bg-dark"><div class="container center">
  <span class="eyebrow">Towns and cities</span>
  <h2>We work with businesses in all ten provinces</h2>
  <p class="lead">{{provinces}}.</p>
  {{cities}}
</div></section>
{{cta}}""", cards=cards, pin=icon("pin"), provinces=", ".join(C.PROVINCES[:-1]) + " and " + C.PROVINCES[-1],
              cities=cities_block(), cta=cta_band())
    page("locations/index.html", "Areas We Serve | Digital Marketing Across Zimbabwe",
         "Smart Click Media serves businesses in Bulawayo, Mutare, Gweru, Victoria Falls, Masvingo and every province of Zimbabwe from our Harare base.",
         body, "", crumbs=[("Home", ""), ("Areas we serve", "locations/")])


def build_location(l):
    context = "".join("<p>%s</p>" % p for p in l["context"])
    industries = "".join('<div class="card reveal"><div class="icon">%s</div><h3>%s</h3><p>%s</p></div>'
                         % (icon(i.get("icon", "briefcase")), i["name"], i["text"]) for i in l["industries"])
    focus = "".join('<a class="card service-card reveal" href="%s"><div class="icon">%s</div><h3>%s</h3><p>%s</p><span class="more">Learn more →</span></a>'
                    % (url_of(f["slug"]), icon(item_of(f["slug"])["icon"]), item_of(f["slug"])["name"], f["why"]) for f in l["focus"])
    body = page_hero("Digital marketing · %s, %s" % (l["city"], l["province"]), l["h1"], l["intro"],
                     [("Areas we serve", "{r}locations/index.html"), (l["city"], None)])
    body += T("""
<section class="section"><div class="container split" style="align-items:start">
  <div class="reveal"><span class="eyebrow">Local market</span><h2>Marketing in {{city}}</h2>{{context}}</div>
  <div class="panel reveal"><h3>How we work with {{city}} businesses</h3>
    <ul class="checklist">
      <li>Strategy sessions and reviews on video call, phone or WhatsApp</li>
      <li>Campaigns targeted to {{city}} and the surrounding area</li>
      <li>Google Business Profile and local SEO for your {{city}} location</li>
      <li>Open 24/7 on {{phone}}</li>
    </ul>
    <a class="btn btn-dark" href="{r}contact/index.html">Talk to us</a></div>
</div></section>
<section class="section bg-soft"><div class="container">
  <div class="center"><span class="eyebrow">Key sectors</span><h2>Industries we help in {{city}}</h2></div>
  <div class="grid grid-3" style="margin-top:40px">{{industries}}</div>
</div></section>
<section class="section"><div class="container">
  <div class="center"><span class="eyebrow">Recommended</span><h2>Services that work well in {{city}}</h2></div>
  <div class="grid grid-3" style="margin-top:40px">{{focus}}</div>
</div></section>
<section class="section bg-soft"><div class="container">
  <div class="center"><span class="eyebrow">FAQ</span><h2>{{city}} questions, answered</h2></div>
  <div style="margin-top:32px">{{faq}}</div>
</div></section>
{{cta}}""", city=l["city"], context=context, phone=C.PHONE_LOCAL, industries=industries, focus=focus,
              faq=faq_block(l["faqs"]), cta=cta_band("Growing a business in %s? Let's talk." % l["city"]))
    page("locations/%s/index.html" % l["slug"], l["title"], clip(l["intro"]), body, "", [faq_schema(l["faqs"])],
         crumbs=[("Home", ""), ("Areas we serve", "locations/"), (l["city"], "locations/%s/" % l["slug"])])


# ---------------------------------------------------------------------------
# Company pages
# ---------------------------------------------------------------------------
def build_about():
    body = page_hero("About Smart Click Media", "A Harare agency built on <span class=\"hl\">results you can see</span>",
                     "Smart Click Media exists because too many Zimbabwean businesses were paying for marketing they couldn't measure. We set out to build the kind of agency we'd want to hire ourselves.",
                     [("About", None)])
    body += T("""
<section class="section"><div class="container split">
  <div class="reveal">
    <span class="eyebrow">Our story</span>
    <h2>Digital marketing, done properly, for Zimbabwe</h2>
    <p>Smart Click Media is a digital marketing agency based in Harare. We help businesses across Zimbabwe, from start-ups to established national brands, get found online, get chosen over their competitors and grow their revenue.</p>
    <p>We combine specialist skills in SEO, AI search, paid advertising, analytics, websites and social media with a deep understanding of the Zimbabwean market: how people search, how they shop on their phones, how much they rely on WhatsApp, and how to reach the millions of Zimbabweans living abroad.</p>
    <p>Every campaign we run is judged on one question: is it growing your business?</p>
  </div>
  <div class="panel-dark reveal">
    <h3>Our mission</h3>
    <p>To help Zimbabwean businesses compete and win online, with honest, measurable digital marketing that pays for itself.</p>
    <h3 style="margin-top:28px">What we believe</h3>
    <ul class="checklist">
      <li>Marketing should be measured in customers and sales</li>
      <li>Clients deserve full visibility and ownership</li>
      <li>Small details done properly beat big promises</li>
      <li>Local knowledge matters</li>
    </ul>
  </div>
</div></section>
<section class="section bg-soft"><div class="container">
  <div class="center"><span class="eyebrow">How we're different</span><h2>Six things you can count on</h2></div>
  <div class="grid grid-3" style="margin-top:48px">{{principles}}</div>
</div></section>
<section class="section"><div class="container">
  <div class="center"><span class="eyebrow">Our process</span><h2>How we work with you</h2></div>
  <div style="margin-top:48px">{{process}}</div>
</div></section>
<section class="section bg-dark"><div class="container center">
  <span class="eyebrow">Where we work</span>
  <h2>Harare headquarters, national reach</h2>
  <p class="lead">We work with clients in all ten provinces: {{provinces}}. Most of our collaboration happens on WhatsApp, video calls and email, and we're happy to meet in person in Harare.</p>
  {{cities}}
</div></section>
{{cta}}""", principles="".join('<div class="card reveal"><div class="icon">%s</div><h3>%s</h3><p>%s</p></div>' % (icon(i), t, d)
                                for i, t, d in PRINCIPLES),
              process=steps_html(PROCESS), provinces=", ".join(C.PROVINCES[:-1]) + " and " + C.PROVINCES[-1],
              cities=cities_block(), cta=cta_band())
    page("about/index.html", "About Us | Digital Marketing Agency in Harare",
         "Smart Click Media is a Harare digital marketing agency, open 24/7, helping businesses across Zimbabwe grow with SEO, AEO, paid ads, analytics and websites.",
         body, "about", crumbs=[("Home", ""), ("About", "about/")])


def build_industries():
    cards = "".join('<div class="card reveal"><div class="icon">%s</div><h3>%s</h3><p>%s</p></div>' % (icon(i), n, d)
                    for n, i, d in C.INDUSTRIES)
    body = page_hero("Industries", "Marketing that understands <span class=\"hl\">your industry</span>",
                     "Every sector in Zimbabwe has its own buyers, seasons and challenges. We bring the right mix of services to each one.",
                     [("Industries", None)])
    body += T("""
<section class="section"><div class="container">
  <h2 class="sr-only">Industries we work with</h2>
  <div class="grid grid-3">{{cards}}</div>
</div></section>
<section class="section bg-soft"><div class="container split">
  <div class="reveal">
    <span class="eyebrow">Diaspora marketing</span>
    <h2>Reach Zimbabweans wherever they live</h2>
    <p>Millions of Zimbabweans live in South Africa, the UK, the US, Australia and beyond, and many of them buy property, pay school fees, send groceries and invest back home. We plan campaigns around when and where they spend time online, with offers that make buying from abroad simple.</p>
    <a class="btn btn-dark" href="{r}services/paid-ads/index.html">See our paid ads service</a>
  </div>
  <div class="panel reveal" style="background:#fff">
    <h3>Popular diaspora campaigns</h3>
    <ul class="checklist">
      <li>Residential stands and housing developments</li>
      <li>Grocery, hamper and gift delivery</li>
      <li>Private schools and colleges</li>
      <li>Funeral cover and insurance</li>
      <li>Building materials and solar systems</li>
      <li>Tourism and holiday packages</li>
    </ul>
  </div>
</div></section>
{{cta}}""", cards=cards, cta=cta_band("Don't see your industry?", "Chances are we've worked on something similar. Tell us what you do, and we'll explain how we'd approach it."))
    page("industries/index.html", "Industries We Serve in Zimbabwe",
         "Digital marketing for retail, tourism, real estate, education, healthcare, agriculture, mining, solar, NGOs and more across Zimbabwe.",
         body, "", crumbs=[("Home", ""), ("Industries", "industries/")])


def build_faq():
    extra = []
    for s in C.SERVICES:
        extra.extend(s["faqs"][:2])
    body = page_hero("FAQ", "Frequently asked <span class=\"hl\">questions</span>",
                     "Straight answers about working with Smart Click Media and about digital marketing in Zimbabwe.",
                     [("FAQ", None)], buttons=False)
    body += T("""
<section class="section"><div class="container">
  <div class="center"><h2>About Smart Click Media</h2></div>
  <div style="margin-top:32px">{{general}}</div>
</div></section>
<section class="section bg-soft"><div class="container">
  <div class="center"><h2>About our services</h2></div>
  <div style="margin-top:32px">{{extra}}</div>
</div></section>
{{cta}}""", general=faq_block(C.FAQS_GENERAL), extra=faq_block(extra),
              cta=cta_band("Still have a question?", "Call or WhatsApp us on %s, any time, or email %s." % (C.PHONE_LOCAL, C.EMAIL)))
    page("faq/index.html", "FAQ | Digital Marketing in Zimbabwe",
         "Answers to common questions about Smart Click Media, SEO, AEO, paid ads, Google Analytics, websites and digital marketing in Zimbabwe.",
         body, "", [faq_schema(C.FAQS_GENERAL + extra)], crumbs=[("Home", ""), ("FAQ", "faq/")])


def build_contact():
    options = "".join('<label><input type="checkbox" name="services" value="%s"> %s</label>' % (s["name"], s["name"]) for s in C.SERVICES)
    body = page_hero("Contact", "Let's grow your business. <span class=\"hl\">Talk to us today.</span>",
                     "Book a free strategy session, ask a question or request a quote. We're open 24/7, so call, WhatsApp or email whenever it suits you.",
                     [("Contact", None)], buttons=False)
    body += T("""
<section class="section"><div class="container split" style="align-items:start">
  <div>
    <span class="eyebrow">Get in touch</span>
    <h2>Speak to a specialist</h2>
    <div class="contact-card"><div class="icon">{{i_phone}}</div><div><h3>Call us</h3><p><a href="tel:{{tel}}">{{phone}}</a> · {{intl}}</p></div></div>
    <div class="contact-card"><div class="icon icon-wa">{{i_msg}}</div><div><h3>WhatsApp</h3><p><a href="{{wa}}" target="_blank" rel="noopener">Chat with us on WhatsApp</a></p></div></div>
    <div class="contact-card"><div class="icon">{{i_mail}}</div><div><h3>Email</h3><p><a href="mailto:{{email}}">{{email}}</a></p></div></div>
    <div class="contact-card"><div class="icon">{{i_clock}}</div><div><h3>Hours</h3><p>{{hours_long}}</p></div></div>
    <div class="contact-card"><div class="icon">{{i_pin}}</div><div><h3>Office</h3><p>Harare, Zimbabwe. Serving clients nationwide and in the diaspora.</p></div></div>
    <div class="panel" style="margin-top:24px">
      <h3>What happens next?</h3>
      <ul class="checklist">
        <li>We'll get in touch to arrange a free strategy session</li>
        <li>We look at your website, ads and online presence beforehand</li>
        <li>You get honest recommendations, with no pressure to sign</li>
      </ul>
    </div>
  </div>
  <div class="card form-card">
    <h2>Request your free strategy session</h2>
    <p class="form-note">Fill this in, then send it by WhatsApp or email. Your message opens ready to send.</p>
    <form class="form" data-contact-form novalidate>
      <div class="row">
        <div><label for="f-name">Your name *</label><input id="f-name" name="name" data-label="Name" required autocomplete="name"></div>
        <div><label for="f-company">Business name</label><input id="f-company" name="company" data-label="Business" autocomplete="organization"></div>
      </div>
      <div class="row">
        <div><label for="f-phone">Phone / WhatsApp *</label><input id="f-phone" name="phone" data-label="Phone" type="tel" required autocomplete="tel" placeholder="07..."></div>
        <div><label for="f-email">Email</label><input id="f-email" name="email" data-label="Email" type="email" autocomplete="email"></div>
      </div>
      <div class="row">
        <div><label for="f-web">Website (if you have one)</label><input id="f-web" name="website" data-label="Website" placeholder="www.example.co.zw"></div>
        <div><label for="f-city">Town / city</label><select id="f-city" name="city" data-label="Location"><option value="">Select…</option>{{cities}}<option>Outside Zimbabwe</option></select></div>
      </div>
      <fieldset class="checks-wrap"><legend>What can we help with?</legend><div class="checks">{{options}}</div></fieldset>
      <div><label for="f-budget">Monthly marketing budget (USD)</label><select id="f-budget" name="budget" data-label="Budget">
        <option value="">Prefer not to say</option><option>Under $300</option><option>$300 to $1,000</option><option>$1,000 to $3,000</option><option>$3,000 to $10,000</option><option>$10,000+</option></select></div>
      <div><label for="f-msg">Tell us about your goals</label><textarea id="f-msg" name="message" data-label="Message" placeholder="What would you like to achieve in the next 6 to 12 months?"></textarea></div>
      <div class="btn-row" style="margin-top:4px">
        <button class="btn btn-primary" type="submit" value="whatsapp">Send via WhatsApp</button>
        <button class="btn btn-outline btn-ink" type="submit" value="email">Send by email</button>
      </div>
      <p class="form-success form-note" role="status" hidden>Thanks! Your message should have opened, ready to send. If it didn't, call {{phone}} or email {{email}}.</p>
    </form>
  </div>
</div></section>
<section class="section bg-dark"><div class="container center">
  <span class="eyebrow">Service area</span>
  <h2>We work with businesses all over Zimbabwe</h2>
  {{cities_block}}
</div></section>""", i_phone=icon("phone"), i_msg=icon("message"), i_mail=icon("mail"), i_clock=icon("clock"), i_pin=icon("pin"),
              tel=C.PHONE_TEL, phone=C.PHONE_LOCAL, intl=C.PHONE_INTL, wa=wa_link(), email=C.EMAIL, hours_long=C.HOURS_LONG,
              cities="".join("<option>%s</option>" % c for c in C.CITIES), options=options, cities_block=cities_block())
    page("contact/index.html", "Contact Us | Call 0771 269 979, Open 24/7",
         "Contact Smart Click Media in Harare, Zimbabwe. Open 24/7: call or WhatsApp 0771 269 979 or email info@smartclick.co.zw for a free strategy session.",
         body, "contact", crumbs=[("Home", ""), ("Contact", "contact/")])


def build_privacy():
    body = page_hero("Legal", "Privacy policy", "How Smart Click Media handles the personal information you share with us.",
                     [("Privacy policy", None)], buttons=False)
    body += T("""
<section class="section"><div class="container prose">
  <p><em>Last updated: 7 November 2026</em></p>
  <p>This policy explains how Smart Click Media ("we", "us"), a digital marketing agency in Harare, handles personal information collected through smartclick.co.zw and through enquiries made by phone, WhatsApp or email. We aim to handle personal information in line with Zimbabwe's Cyber and Data Protection Act [Chapter 12:07].</p>
  <h2>Who is responsible</h2>
  <p>Smart Click Media, Harare, Zimbabwe. You can reach us on <a href="tel:{{tel}}">{{phone}}</a> or at <a href="mailto:{{email}}">{{email}}</a>.</p>
  <h2>What we receive</h2>
  <ul>
    <li><strong>Enquiry details:</strong> when you call, WhatsApp, email or use our contact form, we receive what you choose to share, such as your name, phone number, email address, business name, website and message.</li>
    <li><strong>Website usage data:</strong> if analytics is switched on for this website, Google Analytics may record information such as pages visited, approximate location, device and browser type, and how you arrived at the site.</li>
  </ul>
  <h2>Why we use it</h2>
  <ul>
    <li>Answering your enquiry and arranging any meeting or proposal you request</li>
    <li>Delivering services you have agreed to buy from us</li>
    <li>Seeing which pages visitors find useful, so we can improve the website</li>
  </ul>
  <p>We don't sell personal information, and we only share it with service providers who help us run our business (for example email, hosting and analytics providers), or where the law requires it.</p>
  <h2>The contact form and WhatsApp</h2>
  <p>Our contact form doesn't store anything on our website. It opens WhatsApp or your email app with your details filled in, and nothing is sent until you press send there. Messages sent through WhatsApp are also covered by WhatsApp's own privacy policy.</p>
  <h2>Keeping and deleting information</h2>
  <p>Enquiry details are kept only while they are needed for the purposes above, or for longer where the law requires it, and are then deleted.</p>
  <h2>Your choices and rights</h2>
  <p>You can ask for a copy of the personal information we have about you, and have it corrected or deleted. Get in touch using the details above and we'll respond as soon as we can.</p>
  <h2>Changes to this policy</h2>
  <p>If we change how we handle personal information, we'll update this page and the date at the top.</p>
</div></section>""", tel=C.PHONE_TEL, phone=C.PHONE_LOCAL, email=C.EMAIL)
    page("privacy-policy/index.html", "Privacy Policy", "How Smart Click Media handles personal information from website visitors, enquiries and clients, and the choices you have about it.", body, "",
         crumbs=[("Home", ""), ("Privacy policy", "privacy-policy/")])


def build_terms():
    body = page_hero("Legal", "Terms of service", "The terms that apply when you use this website.",
                     [("Terms of service", None)], buttons=False)
    body += T("""
<section class="section"><div class="container prose">
  <p><em>Last updated: 7 November 2026</em></p>
  <p>These terms apply to your use of smartclick.co.zw, the website of Smart Click Media, Harare, Zimbabwe. By using the website you agree to them. Work we do for clients is covered by a separate written proposal or agreement, which takes priority over these terms.</p>
  <h2>Information on this website</h2>
  <p>We work to keep the information on this website accurate and up to date, but it is general information, not professional advice for your specific situation. Services, features and third-party platforms change over time, so please contact us to confirm details before relying on them.</p>
  <h2>Example projects</h2>
  <p>Projects in our portfolio marked as examples illustrate how we approach work. They are not past client engagements and do not promise any particular result.</p>
  <h2>Third-party platforms and links</h2>
  <p>We mention and link to platforms such as Google, Meta, WhatsApp, TikTok, LinkedIn, Microsoft and OpenAI. They are owned by their respective companies, which set their own rules, availability and pricing. We are not responsible for the content of external websites.</p>
  <h2>Intellectual property</h2>
  <p>The text, design and graphics on this website belong to Smart Click Media unless stated otherwise. You may share links to our pages, but please don't copy or reuse our content without permission.</p>
  <h2>Results</h2>
  <p>Marketing results depend on many factors outside our control, including competition, budgets and platform changes. Nothing on this website is a guarantee of rankings, recommendations by AI tools, leads or sales.</p>
  <h2>Liability</h2>
  <p>To the extent the law allows, we are not liable for any loss arising from your use of this website or from relying on its content.</p>
  <h2>Governing law</h2>
  <p>These terms are governed by the laws of Zimbabwe.</p>
  <h2>Contact</h2>
  <p>Questions about these terms? Call <a href="tel:{{tel}}">{{phone}}</a> or email <a href="mailto:{{email}}">{{email}}</a>.</p>
</div></section>""", tel=C.PHONE_TEL, phone=C.PHONE_LOCAL, email=C.EMAIL)
    page("terms/index.html", "Terms of Service", "The terms for using the Smart Click Media website: website information, example projects, third-party platforms, results and liability.", body, "",
         crumbs=[("Home", ""), ("Terms of service", "terms/")])


def build_404():
    body = """<section class="hero page-hero"><div class="container center">
  <span class="eyebrow">Error 404</span><h1>This page took a wrong turn</h1>
  <p class="lead" style="margin:0 auto">The page you're looking for doesn't exist or has moved.</p>
  <div class="btn-row"><a class="btn btn-primary" href="{r}index.html">Back to home</a><a class="btn btn-outline" href="{r}services/index.html">View services</a></div>
</div></section>"""
    page("404.html", "Page not found", "Page not found.", body, "", root="/", index=False)


def build_extras():
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for u in SITEMAP:
            f.write("  <url><loc>%s</loc><lastmod>%s</lastmod></url>\n" % (u, TODAY))
        f.write("</urlset>\n")
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write("User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % C.SITE_URL)
    L = ["# %s" % C.BRAND, "",
         "> Digital marketing agency based in Harare, Zimbabwe, serving businesses across all 10 provinces and the Zimbabwean diaspora. Open 24/7. Phone / WhatsApp: %s (%s). Email: %s." % (C.PHONE_LOCAL, C.PHONE_INTL, C.EMAIL),
         "", "## Services", ""]
    L += ["- [%s](%s/services/%s/): %s" % (s["name"], C.SITE_URL, s["slug"], strip_tags(s["short"])) for s in C.SERVICES]
    if C.AD_PLATFORMS:
        L += ["", "## Paid ads platforms", ""]
        L += ["- [%s](%s/services/paid-ads/%s/): %s" % (p["name"], C.SITE_URL, p["slug"], strip_tags(p["short"])) for p in C.AD_PLATFORMS]
    if C.ARTICLES:
        L += ["", "## Insights", ""]
        L += ["- [%s](%s/insights/%s/): %s" % (a["title"], C.SITE_URL, a["slug"], a["description"]) for a in C.ARTICLES]
    if C.LOCATIONS:
        L += ["", "## Areas we serve", ""]
        L += ["- [%s](%s/locations/%s/)" % (l["city"], C.SITE_URL, l["slug"]) for l in C.LOCATIONS]
    L += ["", "## Company", "",
          "- [About](%s/about/): who we are and how we work" % C.SITE_URL,
          "- [Portfolio](%s/portfolio/): example projects" % C.SITE_URL,
          "- [Industries](%s/industries/): sectors we serve in Zimbabwe" % C.SITE_URL,
          "- [FAQ](%s/faq/): common questions" % C.SITE_URL,
          "- [Contact](%s/contact/): call or WhatsApp %s, email %s" % (C.SITE_URL, C.PHONE_LOCAL, C.EMAIL), ""]
    with open(os.path.join(ROOT, "llms.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(L))


def clean_stale():
    """Remove generated pages for slugs that no longer exist (e.g. a renamed service)."""
    keep = {"services/%s" % s["slug"] for s in C.SERVICES}
    sdir = os.path.join(ROOT, "services")
    if os.path.isdir(sdir):
        for name in os.listdir(sdir):
            p = os.path.join(sdir, name)
            if os.path.isdir(p) and "services/%s" % name not in keep:
                idx = os.path.join(p, "index.html")
                if os.path.exists(idx) and len(os.listdir(p)) == 1:
                    os.remove(idx)
                    os.rmdir(p)


def main():
    clean_stale()
    build_home()
    build_services_index()
    for s in C.SERVICES:
        build_service(s)
    paid = SERVICE_BY["paid-ads"]
    for p in C.AD_PLATFORMS:
        build_service(p, parent=paid)
    if C.PORTFOLIO:
        build_portfolio_index()
        for p in C.PORTFOLIO:
            build_portfolio_item(p)
    if C.ARTICLES:
        build_insights_index()
        for a in C.ARTICLES:
            build_article(a)
    if C.LOCATIONS:
        build_locations_index()
        for l in C.LOCATIONS:
            build_location(l)
    build_about()
    build_industries()
    build_faq()
    build_contact()
    build_privacy()
    build_terms()
    build_404()
    build_extras()
    print("Built %d indexable pages (+404)" % len(SITEMAP))


if __name__ == "__main__":
    main()
