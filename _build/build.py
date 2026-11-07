# -*- coding: utf-8 -*-
"""Static site generator for the Smart Click Media website.

Usage:  python3 _build/build.py
Writes plain HTML files into the repository root (index.html, services/..., etc.).
No dependencies beyond the Python 3 standard library.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import *  # noqa: E402,F401,F403

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------------------
# Icons (simple stroke icons, drawn for this site)
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
}


def icon(name):
    return ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>' % ICON_PATHS[name])


WA_SVG = ('<svg viewBox="0 0 32 32" fill="currentColor" aria-hidden="true"><path d="M16 3C8.8 3 3 8.7 3 15.8c0 2.5.7 4.9 2 7L3 29l6.4-2c2 1.1 4.3 1.7 6.6 1.7 7.2 0 13-5.7 13-12.8S23.2 3 16 3zm0 23.4c-2.1 0-4.1-.6-5.9-1.6l-.4-.3-3.8 1.2 1.2-3.7-.3-.4a10.4 10.4 0 01-1.7-5.8C5.1 9.9 10 5.1 16 5.1s10.9 4.8 10.9 10.7S22 26.4 16 26.4zm6-8c-.3-.2-1.9-1-2.2-1.1-.3-.1-.5-.2-.7.2l-1 1.2c-.2.2-.4.2-.7.1-.3-.2-1.4-.5-2.6-1.6-1-.9-1.6-1.9-1.8-2.2-.2-.3 0-.5.1-.7l.5-.6.3-.5c.1-.2 0-.4 0-.6l-1-2.4c-.3-.6-.5-.5-.7-.5h-.6c-.2 0-.6.1-.9.4-.3.3-1.2 1.1-1.2 2.8s1.2 3.2 1.4 3.4c.2.2 2.4 3.6 5.8 5 .8.4 1.4.6 1.9.7.8.3 1.5.2 2.1.1.6-.1 1.9-.8 2.2-1.5.3-.7.3-1.4.2-1.5-.1-.2-.3-.3-.6-.4z"/></svg>')

LOGO_SVG = ('<svg viewBox="0 0 48 48" aria-hidden="true">'
            '<defs><linearGradient id="lg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#19c37d"/>'
            '<stop offset="1" stop-color="#3b6cff"/></linearGradient></defs>'
            '<rect width="48" height="48" rx="13" fill="url(#lg)"/>'
            '<path d="M17 13l17 9.5-7.4 1.7 4.6 8.4-3.6 2-4.6-8.4-5.3 5.2z" fill="#fff"/>'
            '<path d="M12 12.5l-2.6-2.6M17 9.5V6M12 18H8.4" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>'
            '</svg>')


def logo(root):
    return ('<a class="logo" href="%sindex.html" aria-label="%s home">%s<span>Smart Click'
            '<small>Media · Harare</small></span></a>' % (root, BRAND, LOGO_SVG))


def wa_link(text="Hi Smart Click Media, I'd like to talk about growing my business."):
    from urllib.parse import quote
    return "https://wa.me/%s?text=%s" % (WA_NUMBER, quote(text))


# ---------------------------------------------------------------------------
# Layout
# ---------------------------------------------------------------------------
def header(root, active):
    mega = "".join(
        '<a href="%sservices/%s/index.html"><span class="mi">%s</span><span>%s<em>%s</em></span></a>'
        % (root, s["slug"], icon(s["icon"]), s["name"], s["short"].split(",")[0].split(".")[0][:58])
        for s in SERVICES)

    def cur(key):
        return ' aria-current="page"' if key == active else ""

    return """
<a class="skip-link" href="#main">Skip to content</a>
<div class="topbar"><div class="container">
  <span class="tb-hide">Harare-based digital marketing agency serving all 10 provinces of Zimbabwe</span>
  <span>Call or WhatsApp: <a href="tel:{tel}">{phone}</a></span>
</div></div>
<header class="site-header">
  <div class="container nav">
    {logo}
    <nav aria-label="Main">
      <ul class="nav-links">
        <li class="has-mega"><a href="{r}services/index.html"{c_services}>Services</a><div class="mega">{mega}</div></li>
        <li><a href="{r}industries/index.html"{c_ind}>Industries</a></li>
        <li><a href="{r}about/index.html"{c_about}>About</a></li>
        <li><a href="{r}faq/index.html"{c_faq}>FAQ</a></li>
        <li><a href="{r}contact/index.html"{c_contact}>Contact</a></li>
      </ul>
    </nav>
    <div class="nav-cta">
      <a class="btn btn-outline" href="tel:{tel}">{phone}</a>
      <a class="btn btn-primary" href="{r}contact/index.html">Free strategy session</a>
      <button class="menu-toggle" aria-label="Open menu" aria-expanded="false"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>""".format(tel=PHONE_TEL, phone=PHONE_LOCAL, logo=logo(root), r=root, mega=mega,
                    c_services=cur("services"), c_ind=cur("industries"), c_about=cur("about"),
                    c_faq=cur("faq"), c_contact=cur("contact"))


def footer(root):
    core = [s for s in SERVICES if s.get("core")]
    more = [s for s in SERVICES if not s.get("core")]
    li = lambda s: '<li><a href="%sservices/%s/index.html">%s</a></li>' % (root, s["slug"], s["name"])
    return """
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        {logo}
        <p>A Harare-based digital marketing agency helping businesses across Zimbabwe get found, get chosen and grow, through search, AI, ads, social and websites that sell.</p>
        <p><strong style="color:#fff">Call / WhatsApp:</strong> <a href="tel:{tel}">{phone}</a><br>
        <strong style="color:#fff">Office:</strong> Harare, Zimbabwe<br>
        <strong style="color:#fff">Service area:</strong> All of Zimbabwe and the diaspora</p>
      </div>
      <div><h4>Core services</h4><ul>{core}</ul></div>
      <div><h4>More services</h4><ul>{more}</ul></div>
      <div><h4>Company</h4><ul>
        <li><a href="{r}about/index.html">About us</a></li>
        <li><a href="{r}industries/index.html">Industries</a></li>
        <li><a href="{r}services/index.html">All services</a></li>
        <li><a href="{r}faq/index.html">FAQ</a></li>
        <li><a href="{r}contact/index.html">Contact</a></li>
        <li><a href="{r}privacy-policy/index.html">Privacy policy</a></li>
      </ul></div>
    </div>
    <div class="footer-bottom">
      <span>&copy; <span id="year">2026</span> {brand}. Harare, Zimbabwe.</span>
      <span>Digital marketing · Websites · SEO · AEO · Paid ads</span>
    </div>
  </div>
</footer>
<a class="wa-float" href="{wa}" target="_blank" rel="noopener" aria-label="Chat with us on WhatsApp">{wa_svg}</a>
""".format(logo=logo(root), tel=PHONE_TEL, phone=PHONE_LOCAL, core="".join(li(s) for s in core),
           more="".join(li(s) for s in more), r=root, brand=BRAND, wa=wa_link(), wa_svg=WA_SVG)


def org_schema():
    return {
        "@context": "https://schema.org",
        "@type": ["LocalBusiness", "ProfessionalService"],
        "@id": SITE_URL + "/#organization",
        "name": BRAND,
        "url": SITE_URL + "/",
        "logo": SITE_URL + "/assets/img/logo.svg",
        "image": SITE_URL + "/assets/img/og-image.svg",
        "telephone": PHONE_INTL,
        "description": "Digital marketing agency in Harare, Zimbabwe offering digital marketing, website development, SEO, AEO, paid ads, social media, e-commerce and more to businesses across Zimbabwe.",
        "address": {"@type": "PostalAddress", "addressLocality": CITY, "addressRegion": "Harare", "addressCountry": "ZW"},
        "areaServed": [{"@type": "Country", "name": COUNTRY}] + [{"@type": "City", "name": c} for c in CITIES[:10]],
        "knowsAbout": [s["name"] for s in SERVICES],
        "hasOfferCatalog": {
            "@type": "OfferCatalog", "name": "Digital marketing services",
            "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": s["name"]}} for s in SERVICES],
        },
    }


def faq_schema(faqs):
    return {
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs],
    }


def page(path, title, description, body, active="", schemas=None, root=None):
    depth = path.count("/")
    if root is None:
        root = "../" * depth
    url_path = path[:-len("index.html")] if path.endswith("index.html") else path
    canonical = SITE_URL + "/" + url_path
    schemas = [org_schema()] + (schemas or [])
    ld = "\n".join('<script type="application/ld+json">%s</script>' % json.dumps(s, ensure_ascii=False) for s in schemas)
    full_title = title if BRAND in title else "%s | %s" % (title, BRAND)
    html = """<!doctype html>
<html lang="en-ZW">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta name="geo.region" content="ZW-HA">
<meta name="geo.placename" content="Harare">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{brand}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{site}/assets/img/og-image.svg">
<meta property="og:locale" content="en_ZW">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0a1630">
<link rel="icon" href="{r}assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}assets/css/styles.css">
{ld}
</head>
<body>
{header}
<main id="main">
{body}
</main>
{footer}
<script src="{r}assets/js/main.js" defer></script>
</body>
</html>
""".format(title=esc(full_title), desc=esc(description), canonical=canonical, brand=BRAND, site=SITE_URL,
           r=root, ld=ld, header=header(root, active), body=body.replace("{r}", root), footer=footer(root))
    out = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    return canonical


def esc(s):
    return s.replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;").replace(">", "&gt;")


def strip_tags(s):
    import re
    return re.sub(r"<[^>]+>", "", s)


# ---------------------------------------------------------------------------
# Reusable sections
# ---------------------------------------------------------------------------
def cta_band(heading="Ready to grow? Let's talk.", text="Book a free, no-obligation strategy session. We'll look at your current marketing, show you where the quick wins are and give you an honest plan, whether you hire us or not."):
    return """
<section class="section-sm"><div class="container">
  <div class="cta-band reveal">
    <div>
      <h2>{h}</h2>
      <p>{t}</p>
      <div class="btn-row">
        <a class="btn btn-primary" href="{{r}}contact/index.html">Book my free session</a>
        <a class="btn btn-outline" href="{wa}" target="_blank" rel="noopener">WhatsApp us</a>
      </div>
    </div>
    <div>
      <span style="opacity:.8">Call us in Harare</span>
      <a class="cta-phone" href="tel:{tel}">{phone}</a>
      <span style="opacity:.8">Mon to Fri, 8am to 5pm · Sat, 8am to 1pm</span>
    </div>
  </div>
</div></section>""".format(h=heading, t=text, wa=wa_link(), tel=PHONE_TEL, phone=PHONE_LOCAL)


def service_card(s, featured=False):
    return """<a class="card service-card reveal{f}" href="{{r}}services/{slug}/index.html">{badge}
  <div class="icon">{icon}</div><h3>{name}</h3><p>{short}</p><span class="more">Learn more →</span></a>""".format(
        slug=s["slug"], icon=icon(s["icon"]), name=s["name"], short=s["short"],
        f=" featured" if featured else "", badge='<span class="badge">Core</span>' if s.get("core") else "")


def faq_block(faqs):
    return '<div class="faq">' + "".join(
        "<details><summary>%s</summary><div><p>%s</p></div></details>" % (q, a) for q, a in faqs) + "</div>"


def cities_block(dark=False):
    return '<div class="cities">' + "".join(
        '<span class="%s">%s</span>' % ("hq" if c == CITY else "", c + (" (HQ)" if c == CITY else ""))
        for c in CITIES) + "</div>"


PROCESS = [
    ("Free strategy session", "We learn about your business, goals and numbers, and review what you're doing now."),
    ("Audit & plan", "You get an honest audit and a 90-day plan with clear targets, budgets and channels."),
    ("Launch fast", "Campaigns, pages and tracking go live, often in the same month you say yes."),
    ("Report & grow", "Weekly optimisation, a plain-English monthly report and a call with your specialist."),
]

PRINCIPLES = [
    ("shield", "Radical transparency", "You own your ad accounts, website and data. You see every dollar spent and every task done."),
    ("users", "Senior specialists, not juniors", "The person who plans your strategy is the person who runs it. No hand-offs to interns."),
    ("chart", "Measured on revenue", "We judge our work by leads, sales and return on spend, not likes and impressions."),
    ("award", "Done properly", "Proper keyword research, clean tracking, tested creative. The unglamorous details that actually move results."),
    ("message", "Local know-how", "We understand Zimbabwean buyers, mobile-first browsing, WhatsApp culture and the diaspora market."),
    ("clock", "No long lock-ins", "Month-to-month agreements. We keep your business by delivering, not by contracts."),
]


def steps_html(steps, dark=False):
    cls = "steps five" if len(steps) == 5 else "steps"
    return '<div class="%s">' % cls + "".join(
        '<div class="step reveal"><h3>%s</h3><p>%s</p></div>' % (t, d) for t, d in steps) + "</div>"


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------
def build_home():
    core = [s for s in SERVICES if s.get("core")]
    rest = [s for s in SERVICES if not s.get("core")]
    channels = ["Google Search", "Google Maps", "ChatGPT", "Gemini", "Perplexity", "Google AI Overviews",
                "Facebook", "Instagram", "TikTok", "YouTube", "LinkedIn", "WhatsApp", "Microsoft Copilot", "Bing"]
    marquee = "".join("<span>%s</span>" % c for c in channels * 2)
    body = """
<section class="hero">
  <div class="container hero-grid">
    <div>
      <span class="eyebrow">Digital marketing agency · Harare, Zimbabwe</span>
      <h1>Get found. Get chosen. <span class="hl">Grow across Zimbabwe.</span></h1>
      <p class="lead">Smart Click Media helps Zimbabwean businesses win more customers through SEO, AI search (AEO), paid ads, social media and websites built to sell. Based in Harare, working with brands in every province.</p>
      <div class="btn-row">
        <a class="btn btn-primary" href="{r}contact/index.html">Get my free strategy session</a>
        <a class="btn btn-outline" href="tel:%(tel)s">Call %(phone)s</a>
      </div>
      <div class="hero-badges">
        <span class="chip"><b>●</b> SEO &amp; AEO</span>
        <span class="chip"><b>●</b> Google &amp; Meta Ads</span>
        <span class="chip"><b>●</b> Websites &amp; E-commerce</span>
        <span class="chip"><b>●</b> All 10 provinces</span>
      </div>
    </div>
    <div class="hero-card" aria-hidden="true">
      <div class="hc-top"><span class="dots"><i></i><i></i><i></i></span><span>Your brand, everywhere buyers look</span></div>
      <div class="hc-search">%(search)s best digital marketing agency in Harare</div>
      <div class="hc-result"><span class="tag">#1</span><b>Your Business · Harare, Zimbabwe</b><small>yourbusiness.co.zw</small><br>Trusted by customers across Zimbabwe. Call or WhatsApp today…</div>
      <div class="hc-ai"><strong>AI answer:</strong> For this in Zimbabwe, a well-reviewed option is <strong>Your Business</strong>, based in Harare and serving clients nationwide…</div>
      <div class="hc-bars"><i style="height:30%%"></i><i style="height:42%%"></i><i style="height:38%%"></i><i style="height:55%%"></i><i style="height:63%%"></i><i style="height:72%%"></i><i style="height:86%%"></i><i style="height:100%%"></i></div>
    </div>
  </div>
</section>

<div class="marquee" aria-label="Channels we optimise for"><div class="marquee-track">%(marquee)s</div></div>

<section class="section">
  <div class="container">
    <div class="center">
      <span class="eyebrow">What we do</span>
      <h2>Five core services. One goal: more customers.</h2>
      <p class="lead">Whether people find you on Google, ask an AI assistant, scroll Facebook or land on your website, we make sure you show up and get chosen.</p>
    </div>
    <div class="grid grid-3" style="margin-top:48px">%(core)s
      <a class="card reveal" href="{r}services/index.html" style="background:var(--navy);color:#fff;border-color:var(--navy)">
        <div class="icon" style="background:rgba(25,195,125,.2);color:var(--brand)">%(spark)s</div>
        <h3 style="color:#fff">+ %(nrest)s more specialist services</h3>
        <p style="color:#b9c4dc">Social media, local SEO, e-commerce, email &amp; WhatsApp, CRM, CRO, analytics, content and hosting.</p>
        <span class="more" style="color:var(--brand)">See all services →</span>
      </a>
    </div>
  </div>
</section>

<section class="section bg-dark">
  <div class="container">
    <div class="split">
      <div>
        <span class="eyebrow">Why Smart Click</span>
        <h2>Most agencies show you likes and clicks. We show you <span class="hl">revenue</span>.</h2>
        <p class="lead">Too many Zimbabwean businesses have paid for marketing that looked busy and delivered nothing. We do things differently: senior specialists, honest reporting and every campaign judged on the money it brings in.</p>
        <div class="btn-row"><a class="btn btn-primary" href="{r}about/index.html">How we work</a></div>
      </div>
      <div class="grid grid-2">%(principles)s</div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container split">
    <div class="panel reveal">
      <span class="eyebrow">The new search</span>
      <h2>Your customers now ask AI. Does it recommend you?</h2>
      <p>Buyers increasingly skip the search results and ask ChatGPT, Gemini or Google's AI Overviews for a recommendation. They get one or two names, and they act on them.</p>
      <p>We do Answer Engine Optimisation (AEO) properly: built on top of the strong SEO foundations it depends on, and tracked prompt by prompt.</p>
      <a class="btn btn-dark" href="{r}services/aeo/index.html">Explore AEO</a>
    </div>
    <div class="reveal">
      <div class="table-wrap"><table class="compare">
        <thead><tr><th></th><th>SEO</th><th>AEO</th></tr></thead>
        <tbody>
          <tr><td>Wins you</td><td>A ranking on Google</td><td>A recommendation from AI</td></tr>
          <tr><td>Where</td><td>Google &amp; Bing results, Maps</td><td>ChatGPT, Gemini, Perplexity, Copilot, AI Overviews</td></tr>
          <tr><td>What counts</td><td>Links, content, technical health</td><td>Mentions, clear answers, consistent brand facts</td></tr>
          <tr><td>Measured by</td><td>Rankings, traffic, leads</td><td>Share of voice in AI answers, leads</td></tr>
        </tbody>
      </table></div>
      <p class="form-note" style="margin-top:14px">You need both. AEO is built on top of good SEO, so we do them together.</p>
    </div>
  </div>
</section>

<section class="section bg-soft">
  <div class="container">
    <div class="center">
      <span class="eyebrow">How it works</span>
      <h2>From first call to growing revenue</h2>
    </div>
    <div style="margin-top:48px">%(process)s</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="center">
      <span class="eyebrow">More ways we help</span>
      <h2>Everything you need to grow online, under one roof</h2>
    </div>
    <div class="grid grid-3" style="margin-top:48px">%(rest)s</div>
  </div>
</section>

<section class="section bg-dark">
  <div class="container center">
    <span class="eyebrow">Based in Harare. Serving the whole nation.</span>
    <h2>From Harare to Victoria Falls, and the diaspora</h2>
    <p class="lead">Our team works from Harare, but our clients are everywhere. We run campaigns targeting every province of Zimbabwe, plus Zimbabweans living in South Africa, the UK, the US and Australia.</p>
    %(cities)s
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="center"><span class="eyebrow">Honest fit</span><h2>We're not for everyone, and that's on purpose</h2></div>
    <div class="fit" style="margin-top:40px">
      <div class="card reveal"><h3>%(check)s We're a great fit if you…</h3><ul class="checklist">
        <li>Want measurable growth in leads and sales, not just more followers</li>
        <li>Have a product or service people genuinely want</li>
        <li>Can follow up leads quickly (we'll help you with that too)</li>
        <li>Want a long-term partner who tells you the truth</li>
      </ul></div>
      <div class="card no reveal"><h3>%(x)s We're not the right fit if you…</h3><ul class="xlist">
        <li>Want the cheapest option, whatever the result</li>
        <li>Want someone to just say yes to every idea</li>
        <li>Expect overnight SEO miracles or guaranteed #1 rankings</li>
        <li>Aren't ready to invest in growth for at least 3 months</li>
      </ul></div>
    </div>
  </div>
</section>

<section class="section bg-soft">
  <div class="container">
    <div class="center"><span class="eyebrow">FAQ</span><h2>Questions we get asked a lot</h2></div>
    <div style="margin-top:40px">%(faq)s</div>
    <p class="center" style="margin-top:24px"><a href="{r}faq/index.html">See all FAQs →</a></p>
  </div>
</section>
%(cta)s
""" % {
        "tel": PHONE_TEL, "phone": PHONE_LOCAL, "search": icon("search"), "marquee": marquee,
        "core": "".join(service_card(s) for s in core), "spark": icon("sparkles"), "nrest": len(rest),
        "principles": "".join('<div class="card card-dark reveal"><div class="icon">%s</div><h3>%s</h3><p>%s</p></div>'
                              % (icon(i), t, d) for i, t, d in PRINCIPLES[:4]),
        "process": steps_html(PROCESS), "rest": "".join(service_card(s) for s in rest),
        "cities": cities_block(True), "check": icon("check"), "x": icon("x"),
        "faq": faq_block(FAQS_GENERAL[:5]), "cta": cta_band(),
    }
    return page("index.html", "Smart Click Media | Digital Marketing Agency in Harare, Zimbabwe",
                "Harare-based digital marketing agency serving all of Zimbabwe. SEO, AEO (AI search), Google & Facebook ads, website development, social media and e-commerce. Call 0771 269 979.",
                body, "home", [faq_schema(FAQS_GENERAL[:5])])


def page_hero(eyebrow, h1, lead, crumbs, buttons=True):
    crumb_html = '<div class="breadcrumb"><a href="{r}index.html">Home</a>' + "".join(
        " / " + ('<a href="%s">%s</a>' % (href, name) if href else name) for name, href in crumbs) + "</div>"
    btns = ""
    if buttons:
        btns = ('<div class="btn-row"><a class="btn btn-primary" href="{r}contact/index.html">Get a free strategy session</a>'
                '<a class="btn btn-outline" href="%s" target="_blank" rel="noopener">WhatsApp %s</a></div>' % (wa_link(), PHONE_LOCAL))
    return """<section class="hero page-hero"><div class="container">%s
  <span class="eyebrow">%s</span><h1>%s</h1><p class="lead">%s</p>%s</div></section>""" % (crumb_html, eyebrow, h1, lead, btns)


def breadcrumb_schema(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": SITE_URL + "/" + u}
                                for i, (n, u) in enumerate(items)]}


def build_service(s):
    included = "".join('<div class="card reveal"><div class="icon">%s</div><h3>%s</h3><p>%s</p></div>'
                       % (icon("check"), t, d) for t, d in s["included"])
    problems = "".join("<li>%s</li>" % p for p in s["problems"])
    related = "".join(service_card(SERVICE_BY_SLUG[r]) for r in s["related"])
    body = page_hero("%s · Harare, Zimbabwe" % s["name"], s["h1"], s["intro"],
                     [("Services", "{r}services/index.html"), (s["name"], None)])
    body += """
<section class="section">
  <div class="container split">
    <div class="reveal">
      <span class="eyebrow">Sound familiar?</span>
      <h2>The problems we fix</h2>
      <ul class="xlist">%(problems)s</ul>
    </div>
    <div class="panel-dark reveal">
      <h3>What you get with Smart Click</h3>
      <ul class="checklist">
        <li>A senior specialist running your account, not a junior</li>
        <li>A clear plan with targets tied to leads and sales</li>
        <li>Full access to your accounts, data and reports</li>
        <li>Plain-English monthly reporting and a review call</li>
        <li>Month-to-month terms, no long lock-in</li>
      </ul>
      <a class="btn btn-primary" href="tel:%(tel)s">Call %(phone)s</a>
    </div>
  </div>
</section>
<section class="section bg-soft">
  <div class="container">
    <div class="center"><span class="eyebrow">What's included</span><h2>Our %(lname)s service</h2></div>
    <div class="grid grid-3" style="margin-top:48px">%(included)s</div>
  </div>
</section>
<section class="section bg-dark">
  <div class="container">
    <div class="center"><span class="eyebrow">Our approach</span><h2>How we deliver %(lname)s</h2></div>
    <div style="margin-top:48px">%(steps)s</div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="center"><span class="eyebrow">FAQ</span><h2>%(name)s questions, answered</h2></div>
    <div style="margin-top:40px">%(faq)s</div>
  </div>
</section>
<section class="section bg-soft">
  <div class="container">
    <div class="center"><span class="eyebrow">Works well with</span><h2>Related services</h2></div>
    <div class="grid grid-3" style="margin-top:40px">%(related)s</div>
  </div>
</section>
%(cta)s
""" % {"problems": problems, "tel": PHONE_TEL, "phone": PHONE_LOCAL, "included": included,
       "lname": s["name"] if s["name"].isupper() or s["slug"] in ("seo", "aeo", "cro") else s["name"].lower(),
       "name": s["name"], "steps": steps_html(s["steps"]), "faq": faq_block(s["faqs"]), "related": related,
       "cta": cta_band("Let's talk about %s for your business" % (s["name"] if s["slug"] in ("seo", "aeo", "cro") else s["name"].lower()))}
    path = "services/%s/index.html" % s["slug"]
    service_ld = {
        "@context": "https://schema.org", "@type": "Service", "name": s["name"], "serviceType": s["name"],
        "description": s["short"], "provider": {"@id": SITE_URL + "/#organization"},
        "areaServed": {"@type": "Country", "name": COUNTRY},
    }
    return page(path, s["title"], strip_tags(s["intro"])[:155].rsplit(" ", 1)[0] + "…", body, "services",
                [service_ld, faq_schema(s["faqs"]),
                 breadcrumb_schema([("Home", ""), ("Services", "services/"), (s["name"], "services/%s/" % s["slug"])])])


def build_services_index():
    core = [s for s in SERVICES if s.get("core")]
    rest = [s for s in SERVICES if not s.get("core")]
    body = page_hero("Our services", "Every service you need to <span class=\"hl\">grow online</span> in Zimbabwe",
                     "%d specialist services, one joined-up team. Start with the one you need most, and we'll connect it to everything else." % len(SERVICES),
                     [("Services", None)])
    body += """
<section class="section"><div class="container">
  <div class="center"><span class="eyebrow">Core services</span><h2>Where most clients start</h2></div>
  <div class="grid grid-3" style="margin-top:40px">%s</div>
</div></section>
<section class="section bg-soft"><div class="container">
  <div class="center"><span class="eyebrow">Specialist services</span><h2>Go further</h2></div>
  <div class="grid grid-3" style="margin-top:40px">%s</div>
</div></section>
<section class="section bg-dark"><div class="container">
  <div class="center"><span class="eyebrow">How we work</span><h2>One process, every service</h2></div>
  <div style="margin-top:48px">%s</div>
</div></section>
%s""" % ("".join(service_card(s) for s in core), "".join(service_card(s) for s in rest), steps_html(PROCESS), cta_band())
    return page("services/index.html", "Digital Marketing Services in Zimbabwe",
                "SEO, AEO, paid ads, website development, social media, e-commerce, email & WhatsApp marketing, CRM and more from Smart Click Media, Harare.",
                body, "services", [breadcrumb_schema([("Home", ""), ("Services", "services/")])])


def build_about():
    body = page_hero("About Smart Click Media", "A Harare agency built on <span class=\"hl\">results you can see</span>",
                     "We started Smart Click Media because too many Zimbabwean businesses were paying for marketing that looked busy and delivered nothing. We wanted to build the agency we'd want to hire ourselves.",
                     [("About", None)])
    body += """
<section class="section"><div class="container split">
  <div class="reveal">
    <span class="eyebrow">Our story</span>
    <h2>Digital marketing, done properly, for Zimbabwe</h2>
    <p>Smart Click Media is a digital marketing agency based in Harare. We help businesses across Zimbabwe, from start-ups to established national brands, get found online, get chosen over their competitors and grow their revenue.</p>
    <p>We combine specialist skills in SEO, AI search, paid advertising, websites and social media with a deep understanding of the Zimbabwean market: how people search, how they shop on their phones, how much they rely on WhatsApp, and how to reach the millions of Zimbabweans living abroad.</p>
    <p>We're not interested in vanity metrics. Every campaign we run is judged on one thing: whether it grows your business.</p>
  </div>
  <div class="panel-dark reveal">
    <h3>Our mission</h3>
    <p>To help Zimbabwean businesses compete and win online, with honest, measurable digital marketing that pays for itself.</p>
    <h3 style="margin-top:28px">What we believe</h3>
    <ul class="checklist">
      <li>Marketing should be measured in sales, not likes</li>
      <li>Clients deserve full transparency and ownership</li>
      <li>Small details done properly beat big promises</li>
      <li>Local knowledge matters</li>
    </ul>
  </div>
</div></section>
<section class="section bg-soft"><div class="container">
  <div class="center"><span class="eyebrow">How we're different</span><h2>Six promises we make to every client</h2></div>
  <div class="grid grid-3" style="margin-top:48px">%(principles)s</div>
</div></section>
<section class="section"><div class="container">
  <div class="center"><span class="eyebrow">Our process</span><h2>How we work with you</h2></div>
  <div style="margin-top:48px">%(process)s</div>
</div></section>
<section class="section bg-dark"><div class="container center">
  <span class="eyebrow">Where we work</span>
  <h2>Harare headquarters, national reach</h2>
  <p class="lead">We work with clients in all ten provinces: %(provinces)s. Most of our collaboration happens on WhatsApp, video calls and in your inbox, and we're happy to meet in person in Harare.</p>
  %(cities)s
</div></section>
%(cta)s""" % {
        "principles": "".join('<div class="card reveal"><div class="icon">%s</div><h3>%s</h3><p>%s</p></div>' % (icon(i), t, d)
                              for i, t, d in PRINCIPLES),
        "process": steps_html(PROCESS), "provinces": ", ".join(PROVINCES[:-1]) + " and " + PROVINCES[-1],
        "cities": cities_block(True), "cta": cta_band()}
    return page("about/index.html", "About Us | Digital Marketing Agency in Harare",
                "Smart Click Media is a Harare-based digital marketing agency helping businesses across Zimbabwe grow through SEO, AEO, paid ads, websites and social media.",
                body, "about", [breadcrumb_schema([("Home", ""), ("About", "about/")])])


def build_industries():
    cards = "".join('<div class="card reveal"><div class="icon">%s</div><h3>%s</h3><p>%s</p></div>' % (icon(i), n, d)
                    for n, i, d in INDUSTRIES)
    body = page_hero("Industries", "Marketing that understands <span class=\"hl\">your industry</span>",
                     "Every sector in Zimbabwe has its own buyers, seasons and challenges. We bring the right mix of services to each one.",
                     [("Industries", None)])
    body += """
<section class="section"><div class="container">
  <div class="grid grid-3">%s</div>
</div></section>
<section class="section bg-soft"><div class="container split">
  <div class="reveal">
    <span class="eyebrow">Diaspora marketing</span>
    <h2>Reach Zimbabweans wherever they live</h2>
    <p>Millions of Zimbabweans live in South Africa, the UK, the US, Australia and beyond, and many of them buy property, pay school fees, send groceries and invest back home. We build campaigns that reach them with the right message, at the right time, in the right place.</p>
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
%s""" % (cards, cta_band("Don't see your industry?", "We've probably worked in something similar. Tell us about your business and we'll show you how we'd approach it."))
    return page("industries/index.html", "Industries We Serve in Zimbabwe",
                "Digital marketing for retail, tourism, real estate, education, healthcare, agriculture, mining, solar, NGOs and more across Zimbabwe.",
                body, "industries", [breadcrumb_schema([("Home", ""), ("Industries", "industries/")])])


def build_faq():
    extra = []
    for s in SERVICES:
        extra.extend(s["faqs"][:2])
    body = page_hero("FAQ", "Frequently asked <span class=\"hl\">questions</span>",
                     "Straight answers about working with Smart Click Media and about digital marketing in Zimbabwe.",
                     [("FAQ", None)], buttons=False)
    body += """
<section class="section"><div class="container">
  <div class="center"><h2>About Smart Click Media</h2></div>
  <div style="margin-top:32px">%s</div>
</div></section>
<section class="section bg-soft"><div class="container">
  <div class="center"><h2>About our services</h2></div>
  <div style="margin-top:32px">%s</div>
</div></section>
%s""" % (faq_block(FAQS_GENERAL), faq_block(extra), cta_band("Still have a question?", "Call or WhatsApp us on %s. A real person will answer." % PHONE_LOCAL))
    return page("faq/index.html", "FAQ | Digital Marketing in Zimbabwe",
                "Answers to common questions about Smart Click Media, SEO, AEO, paid ads, websites and digital marketing in Zimbabwe.",
                body, "faq", [faq_schema(FAQS_GENERAL + extra), breadcrumb_schema([("Home", ""), ("FAQ", "faq/")])])


def build_contact():
    options = "".join('<label><input type="checkbox" name="services" value="%s"> %s</label>' % (s["name"], s["name"]) for s in SERVICES)
    body = page_hero("Contact", "Let's grow your business. <span class=\"hl\">Talk to us today.</span>",
                     "Book a free strategy session, ask a question or request a quote. We usually reply within one working day, often much sooner on WhatsApp.",
                     [("Contact", None)], buttons=False)
    body += """
<section class="section"><div class="container split" style="align-items:start">
  <div>
    <span class="eyebrow">Get in touch</span>
    <h2>Speak to a specialist</h2>
    <div class="contact-card"><div class="icon">%(phone_i)s</div><div><h3>Call us</h3><p><a href="tel:%(tel)s">%(phone)s</a> · %(intl)s</p></div></div>
    <div class="contact-card"><div class="icon" style="background:#dcfce7;color:#15803d">%(msg_i)s</div><div><h3>WhatsApp</h3><p><a href="%(wa)s" target="_blank" rel="noopener">Chat with us on WhatsApp</a></p></div></div>
    <div class="contact-card"><div class="icon">%(pin_i)s</div><div><h3>Office</h3><p>Harare, Zimbabwe. Serving clients nationwide and in the diaspora.</p></div></div>
    <div class="contact-card"><div class="icon">%(clock_i)s</div><div><h3>Hours</h3><p>Monday to Friday, 8am to 5pm<br>Saturday, 8am to 1pm</p></div></div>
    <div class="panel" style="margin-top:24px">
      <h3>What happens next?</h3>
      <ul class="checklist">
        <li>We'll contact you to book a free 30-minute strategy session</li>
        <li>We review your website, ads and online presence beforehand</li>
        <li>You get honest recommendations, with no pressure to sign</li>
      </ul>
    </div>
  </div>
  <div class="card" style="padding:36px">
    <h2 style="font-size:1.7rem">Request your free strategy session</h2>
    <p class="form-note">Fill this in and press send. It opens WhatsApp with your details ready to send to us.</p>
    <form class="form" data-wa-form>
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
        <div><label for="f-city">Town / city</label><select id="f-city" name="city" data-label="Location"><option value="">Select…</option>%(cities)s<option>Outside Zimbabwe</option></select></div>
      </div>
      <div><label>What can we help with?</label><div class="checks">%(options)s</div></div>
      <div><label for="f-budget">Monthly marketing budget (USD)</label><select id="f-budget" name="budget" data-label="Budget">
        <option value="">Prefer not to say</option><option>Under $300</option><option>$300 to $1,000</option><option>$1,000 to $3,000</option><option>$3,000 to $10,000</option><option>$10,000+</option></select></div>
      <div><label for="f-msg">Tell us about your goals</label><textarea id="f-msg" name="message" data-label="Message" placeholder="What would you like to achieve in the next 6 to 12 months?"></textarea></div>
      <button class="btn btn-primary" type="submit">Send via WhatsApp</button>
      <p class="form-success form-note" hidden style="color:var(--brand-dark);font-weight:600">Thanks! WhatsApp should have opened with your message. If it didn't, call us on %(phone)s.</p>
    </form>
  </div>
</div></section>
<section class="section bg-dark"><div class="container center">
  <span class="eyebrow">Service area</span>
  <h2>We work with businesses all over Zimbabwe</h2>
  %(cities_block)s
</div></section>""" % {
        "phone_i": icon("phone"), "msg_i": icon("message"), "pin_i": icon("pin"), "clock_i": icon("clock"),
        "tel": PHONE_TEL, "phone": PHONE_LOCAL, "intl": PHONE_INTL, "wa": wa_link(),
        "cities": "".join("<option>%s</option>" % c for c in CITIES), "options": options,
        "cities_block": cities_block(True)}
    return page("contact/index.html", "Contact Us | Call 0771 269 979",
                "Contact Smart Click Media in Harare, Zimbabwe. Call or WhatsApp 0771 269 979 for a free digital marketing strategy session.",
                body, "contact", [breadcrumb_schema([("Home", ""), ("Contact", "contact/")])])


def build_privacy():
    body = page_hero("Legal", "Privacy policy", "How Smart Click Media collects, uses and protects your information.", [("Privacy policy", None)], buttons=False)
    body += """
<section class="section"><div class="container prose">
  <p><em>Last updated: November 2026</em></p>
  <p>Smart Click Media ("we", "us") respects your privacy. This policy explains what information we collect through this website and how we use it, in line with Zimbabwe's Cyber and Data Protection Act [Chapter 12:07].</p>
  <h2>Information we collect</h2>
  <ul>
    <li><strong>Information you give us:</strong> when you call, WhatsApp or fill in our contact form, we receive details such as your name, phone number, email address, business name and message.</li>
    <li><strong>Usage information:</strong> if analytics tools are enabled on this site, we may collect anonymous information about how visitors use it, such as pages viewed and device type.</li>
  </ul>
  <h2>How we use your information</h2>
  <ul>
    <li>To respond to your enquiry and provide the services you ask for</li>
    <li>To send you information you've asked to receive</li>
    <li>To improve our website and services</li>
  </ul>
  <p>We do not sell your personal information.</p>
  <h2>WhatsApp</h2>
  <p>Our contact form opens WhatsApp with your message pre-filled. Messages sent through WhatsApp are also subject to WhatsApp's own privacy policy.</p>
  <h2>Keeping your information safe</h2>
  <p>We take reasonable technical and organisational measures to protect your information and keep it only as long as needed for the purposes above.</p>
  <h2>Your rights</h2>
  <p>You may ask to see, correct or delete the personal information we hold about you. Contact us on <a href="tel:%s">%s</a>.</p>
  <h2>Changes</h2>
  <p>We may update this policy from time to time. The latest version will always be on this page.</p>
</div></section>""" % (PHONE_TEL, PHONE_LOCAL)
    return page("privacy-policy/index.html", "Privacy Policy", "Privacy policy for the Smart Click Media website.", body, "")


def build_404():
    body = """<section class="hero page-hero"><div class="container center">
  <span class="eyebrow">Error 404</span><h1>This page took a wrong turn</h1>
  <p class="lead" style="margin:0 auto">The page you're looking for doesn't exist or has moved.</p>
  <div class="btn-row"><a class="btn btn-primary" href="{r}index.html">Back to home</a><a class="btn btn-outline" href="{r}services/index.html">View services</a></div>
</div></section>"""
    page("404.html", "Page not found", "Page not found.", body, "", root="/")


def build_extras(urls):
    today = "2026-11-07"
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for u in urls:
            f.write("  <url><loc>%s</loc><lastmod>%s</lastmod></url>\n" % (u, today))
        f.write("</urlset>\n")
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write("User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % SITE_URL)
    # llms.txt: a plain-text summary for AI assistants (supports our own AEO)
    lines = ["# %s" % BRAND, "",
             "> Digital marketing agency based in Harare, Zimbabwe, serving businesses across all 10 provinces and the Zimbabwean diaspora. Phone / WhatsApp: %s (%s)." % (PHONE_LOCAL, PHONE_INTL),
             "", "## Services", ""]
    for s in SERVICES:
        lines.append("- [%s](%s/services/%s/): %s" % (s["name"], SITE_URL, s["slug"], s["short"]))
    lines += ["", "## Company", "",
              "- [About](%s/about/): who we are and how we work" % SITE_URL,
              "- [Industries](%s/industries/): sectors we serve in Zimbabwe" % SITE_URL,
              "- [FAQ](%s/faq/): common questions" % SITE_URL,
              "- [Contact](%s/contact/): call or WhatsApp %s" % (SITE_URL, PHONE_LOCAL), ""]
    with open(os.path.join(ROOT, "llms.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def main():
    urls = [build_home(), build_services_index()]
    urls += [build_service(s) for s in SERVICES]
    urls += [build_about(), build_industries(), build_faq(), build_contact(), build_privacy()]
    build_404()
    build_extras(urls)
    print("Built %d pages" % (len(urls) + 1))


if __name__ == "__main__":
    main()
