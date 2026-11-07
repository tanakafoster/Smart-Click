# -*- coding: utf-8 -*-
"""All site copy for Smart Click Media lives here. Edit this file, then run build.py."""

BRAND = "Smart Click Media"
PHONE_LOCAL = "0771 269 979"
PHONE_INTL = "+263 77 126 9979"
PHONE_TEL = "+263771269979"
WA_NUMBER = "263771269979"
CITY = "Harare"
COUNTRY = "Zimbabwe"
EMAIL = "info@smartclick.co.zw"
HOURS = "Open 24/7"
HOURS_LONG = "Open 24 hours a day, 7 days a week"
# Live domain: used for canonical URLs, structured data and sitemap.xml.
SITE_URL = "https://smartclick.co.zw"
# Google Analytics 4 measurement ID (looks like "G-XXXXXXXXXX"). Leave empty to switch tracking off.
GA_MEASUREMENT_ID = ""

CITIES = ["Harare", "Bulawayo", "Chitungwiza", "Mutare", "Gweru", "Kwekwe", "Kadoma", "Masvingo",
          "Chinhoyi", "Marondera", "Bindura", "Victoria Falls", "Hwange", "Kariba", "Beitbridge",
          "Zvishavane", "Chegutu", "Rusape", "Gwanda", "Lupane"]

PROVINCES = ["Harare", "Bulawayo", "Manicaland", "Mashonaland Central", "Mashonaland East",
             "Mashonaland West", "Masvingo", "Matabeleland North", "Matabeleland South", "Midlands"]

# ---------------------------------------------------------------------------
# Services. Order here is the order they appear in menus and grids.
# ---------------------------------------------------------------------------
SERVICES = [
    {
        "slug": "digital-marketing",
        "name": "Digital Marketing",
        "menu": "One growth plan across every channel",
        "icon": "target",
        "description": "Digital marketing agency in Harare: one plan across search, social, ads, email and your website, judged on enquiries and sales. Call 0771 269 979.",
        "core": True,
        "short": "One joined-up growth plan across search, social, ads, email and your website, built around sales, not likes.",
        "title": "Digital Marketing Agency in Harare, Zimbabwe",
        "h1": "Digital marketing that turns Zimbabwean attention into <span class=\"hl\">paying customers</span>",
        "intro": "Most businesses don't need more posts. They need a plan that connects every channel to one number: revenue. We build and run that plan for businesses of any size, anywhere in Zimbabwe.",
        "problems": [
            "You're paying for marketing but can't say which channel actually brings in sales.",
            "Your social pages get likes, yet the phone and WhatsApp stay quiet.",
            "Different freelancers run your ads, website and social, and none of them talk to each other.",
            "You've got no clear monthly report, just screenshots and buzzwords.",
        ],
        "included": [
            ("Growth strategy & market research", "We study your customers, competitors and margins, then set realistic targets for leads, sales and cost per customer."),
            ("Channel planning", "Search, social, paid ads, email, WhatsApp and your website, each with a clear job in the customer journey."),
            ("Funnels & offers", "Landing pages, lead magnets and offers that make it easy to say yes today instead of \"maybe later\"."),
            ("Creative & copy", "Ad creative, video scripts and copy written for Zimbabwean audiences, in English, Shona or Ndebele where it helps."),
            ("Tracking & attribution", "Every enquiry, call and WhatsApp click is tagged, so we know exactly what's working."),
            ("Monthly growth reviews", "A plain-English report and a call with the person running your account, not a junior."),
        ],
        "steps": [
            ("Discover", "We learn your business, numbers and goals, and audit everything you're already doing."),
            ("Plan", "You get a 90-day roadmap with budgets, channels and targets you can hold us to."),
            ("Launch", "Campaigns, pages and tracking go live, usually within the first month."),
            ("Grow", "We test, cut what doesn't work and put more behind what does, every single week."),
        ],
        "faqs": [
            ("What budget do I need for digital marketing in Zimbabwe?", "It depends on your goals and industry. Many local SMEs start with a modest monthly ad budget plus our management fee, then scale up once the results justify it. We'll recommend a budget in your free strategy session and explain exactly where every dollar goes."),
            ("We're not in Harare. Can you still help us?", "Yes. Our team is in Harare, and we can work with businesses in Bulawayo, Mutare, Gweru, Masvingo, Victoria Falls and towns in every province. Most of the work happens online, on WhatsApp and on video calls."),
            ("How soon will I see results?", "Paid ads can bring enquiries within days of launch. SEO and content build over months. Your plan will combine quick wins with long-term growth so you're not waiting a year for a return."),
            ("Can I pay in USD or ZiG?", "We quote in USD and can discuss local payment options when we put your proposal together."),
        ],
        "related": ["paid-ads", "seo", "social-media"],
    },
    {
        "slug": "website-development",
        "name": "Website Development",
        "menu": "Fast, mobile-first sites built to win enquiries",
        "icon": "monitor",
        "description": "Fast, mobile-first websites for Zimbabwean businesses, built to load well on mobile data and turn visitors into calls, WhatsApp chats and enquiries.",
        "core": True,
        "short": "Fast, mobile-first websites that load on any network in Zimbabwe and are built to win enquiries.",
        "title": "Website Design & Development in Harare, Zimbabwe",
        "h1": "Websites built to <span class=\"hl\">sell</span>, not just sit there looking pretty",
        "intro": "In Zimbabwe, most of your visitors will arrive on a smartphone, and many will be paying for every megabyte. Your website has to load quickly, read clearly on a small screen and make calling, messaging on WhatsApp or buying effortless. That's what we design and build.",
        "problems": [
            "Your site takes forever to load on mobile data, so visitors give up.",
            "It looks fine but nobody ever fills in the contact form.",
            "You can't update it yourself, and the developer who built it has vanished.",
            "Google barely shows it, because it was never built with SEO in mind.",
        ],
        "included": [
            ("Custom design", "A look that fits your brand, designed mobile-first and tested on real devices."),
            ("WordPress & custom builds", "Easy-to-edit WordPress sites, or hand-coded builds when speed and flexibility matter most."),
            ("Conversion-focused layouts", "Click-to-call, WhatsApp buttons, clear offers and short forms on every key page."),
            ("SEO-ready from day one", "Clean code, fast loading, schema markup and proper page structure so Google and AI tools understand you."),
            ("Copywriting", "Words that explain what you do, who it's for and why you're the safe choice."),
            ("Training & handover", "We show your team how to update pages, add products and post news."),
        ],
        "steps": [
            ("Brief & sitemap", "We agree goals, pages and features, and map out what each page needs to do."),
            ("Design", "You review designs for desktop and mobile before a line of code is written."),
            ("Build & test", "We build, connect tracking, and test speed, forms and mobile layouts."),
            ("Launch & support", "We go live, submit to Google and stay on hand for updates and fixes."),
        ],
        "faqs": [
            ("How long does a website take?", "A typical business website takes 3 to 6 weeks from brief to launch. Larger e-commerce or custom builds take longer, and you'll get a timeline before we start."),
            ("Will I own my website?", "Yes. You own the domain, the content and the site itself. We'll make sure all logins are in your name."),
            ("Can you redesign my existing site without losing my Google rankings?", "Usually, yes. We plan redirects and keep your best-performing pages intact, so a redesign doesn't throw away the traffic you've already earned. Rankings can wobble for a few weeks afterwards, so we watch them closely."),
            ("Do you offer hosting?", "Yes, see our hosting and maintenance service. We can host, back up and look after your site so you don't have to."),
        ],
        "related": ["ecommerce", "hosting-maintenance", "seo"],
    },
    {
        "slug": "seo",
        "name": "SEO",
        "menu": "Get found on Google for what you sell",
        "icon": "search",
        "description": "SEO for Zimbabwean businesses: keyword research, technical fixes, content and links, with a monthly report on rankings, traffic, leads and work done.",
        "core": True,
        "short": "Help your business rank higher on Google for the searches your customers make.",
        "title": "SEO Agency in Harare | Search Engine Optimisation Zimbabwe",
        "h1": "Get found on Google when Zimbabweans search for <span class=\"hl\">what you sell</span>",
        "intro": "When someone in Harare types \"best plumber near me\" or \"solar installers Zimbabwe\", the top few results take most of the clicks. We aim to get you there with careful, measurable, unglamorous work, done properly every month.",
        "problems": [
            "You've paid for SEO for months, but your rankings haven't moved.",
            "Nobody can tell you what was actually done last month.",
            "Competitors with worse products outrank you for your main keywords.",
            "Your site has technical problems nobody has ever looked at.",
        ],
        "included": [
            ("Keyword research", "We find the terms your buyers really use, including local phrases and suburb-level searches, ranked by buying intent."),
            ("Technical SEO", "Site speed, crawl errors, indexing, mobile usability, structured data and Core Web Vitals, fixed and monitored."),
            ("On-page optimisation", "Titles, headings, internal links and content tuned page by page, not just a plugin ticked on."),
            ("Content that ranks", "Service pages, guides and articles that answer real questions clearly and completely."),
            ("Link building", "Earning mentions and links from relevant Zimbabwean and African sites, directories and media."),
            ("Transparent reporting", "Rankings, traffic, leads and a list of every task completed, every month."),
        ],
        "steps": [
            ("Audit", "A full technical, content and competitor audit with a prioritised fix list."),
            ("Fix the foundations", "We sort out the technical issues holding your site back."),
            ("Build authority", "Content and links that grow your visibility month after month."),
            ("Measure & refine", "We track rankings and leads, and double down on what moves the needle."),
        ],
        "faqs": [
            ("How soon will SEO show results?", "You'll usually see early movement in 2 to 3 months, with strong results building over 6 to 12 months. Anyone promising page one in a week is not being honest with you."),
            ("Do you guarantee number one rankings?", "No one can honestly guarantee a ranking, because Google controls the results. What we do guarantee is transparent work, clear reporting and a strategy built on what actually moves rankings."),
            ("Do I need SEO or AEO?", "Most businesses benefit from both. SEO helps you rank in Google's results, while AEO helps AI assistants such as ChatGPT, Gemini and Google's AI Overviews mention you. AI tools rely heavily on well-optimised, trusted websites, so the two support each other and we usually run them together."),
            ("Can you do SEO for a specific city like Bulawayo or Mutare?", "Yes. Local SEO targets customers in specific towns and suburbs, and it's often a sensible first investment for a local business."),
        ],
        "related": ["aeo", "local-seo", "content-marketing"],
    },
    {
        "slug": "aeo",
        "name": "AEO (AI Search Optimisation)",
        "menu": "Help AI assistants find and recommend you",
        "icon": "sparkles",
        "description": "AEO for Zimbabwean businesses: help ChatGPT, Gemini, Copilot, Perplexity and Google's AI find your business, describe it correctly and recommend it.",
        "core": True,
        "short": "Help ChatGPT, Gemini, Copilot, Perplexity and Google's AI find, understand and recommend your business.",
        "title": "AEO Agency in Zimbabwe | ChatGPT & AI Search Optimisation",
        "h1": "Make your business easy for AI assistants to <span class=\"hl\">recommend</span>",
        "intro": "More and more people ask ChatGPT, Gemini, Microsoft Copilot or Perplexity to suggest a supplier, or read Google's AI answers, instead of scrolling through search results. Answer Engine Optimisation (AEO) is the work of helping those answers mention your business, describe it correctly and send people your way.",
        "problems": [
            "You ask an AI assistant for the best options in your industry in Zimbabwe, and your business isn't mentioned.",
            "AI tools get your details wrong: an old phone number, the wrong town or services you don't offer.",
            "Your website is full of slogans, so there's nothing clear for an AI to quote.",
            "Very little is written about your business on other websites, so AI has little to go on.",
        ],
        "included": [
            ("Consistent business facts", "Your name, services, locations, hours and contact details made identical across your website, Google Business Profile, directories and social profiles."),
            ("Reputation beyond your website", "Reviews, directory listings, local media coverage and industry mentions that show AI tools your business can be trusted."),
            ("Pages built around questions", "Clear question-and-answer content, comparison pages and how-to guides that give AI something accurate to cite."),
            ("Technical readiness", "Fast pages, accurate schema markup and robots.txt settings that let AI search crawlers in, plus an optional llms.txt summary."),
            ("Monthly AI answer checks", "Every month we put the same set of real buyer questions to ChatGPT, Gemini, Copilot, Perplexity and Google's AI answers, and record who gets named."),
            ("AI traffic reporting", "Visits from ChatGPT, Gemini, Perplexity and Copilot tracked in Google Analytics, alongside how often you're recommended."),
        ],
        "steps": [
            ("Ask the questions", "We find the questions your customers put to AI assistants and test them across the main tools."),
            ("Fix the facts", "We correct and align your business information everywhere it appears online."),
            ("Earn the mentions", "Helpful content, reviews and coverage give AI good reasons to recommend you."),
            ("Re-check monthly", "We test the same questions every month and report what has changed."),
        ],
        "faqs": [
            ("What is AEO?", "AEO stands for Answer Engine Optimisation. It means improving how AI assistants such as ChatGPT, Gemini, Microsoft Copilot, Perplexity and Google's AI Overviews describe and recommend your business."),
            ("How is AEO different from SEO?", "SEO is about ranking in search results. AEO is about being named, and described correctly, in AI-generated answers. The two overlap a lot: AI tools lean on websites that are easy to crawl, well organised and widely trusted, so strong SEO makes AEO much easier. We usually run them together."),
            ("Do people in Zimbabwe really use AI assistants?", "Yes. Students, professionals and business buyers increasingly use them, and few Zimbabwean businesses are working on AEO yet, so there's a real chance to get ahead of your competitors."),
            ("Can you guarantee ChatGPT will recommend us?", "No one can. AI answers change, and no agency controls them. What we can do is make your business easy for AI to understand and trust, and show you each month how often you're being mentioned."),
        ],
        "related": ["seo", "content-marketing", "local-seo"],
    },
    {
        "slug": "paid-ads",
        "name": "Paid Ads",
        "menu": "Google, YouTube, Meta, WhatsApp and more, in one plan",
        "icon": "zap",
        "description": "Paid ads planned and managed from Harare on Google, YouTube, Facebook, Instagram, WhatsApp and more, with every campaign tracked to enquiries.",
        "core": True,
        "short": "Google, YouTube, Meta, WhatsApp, LinkedIn and Microsoft ads, plus TikTok and ChatGPT ads for diaspora campaigns, planned and managed by one team and judged on the customers they bring in.",
        "title": "Paid Ads Agency in Harare | Google, Meta, YouTube & LinkedIn",
        "h1": "Advertising on the platforms your customers use, <span class=\"hl\">managed as one plan</span>",
        "intro": "From Google search and YouTube to Facebook, Instagram, WhatsApp, LinkedIn, Microsoft Bing, TikTok and the new ad placements in AI assistants such as ChatGPT, we plan, build and manage paid campaigns for Zimbabwean businesses and for brands reaching Zimbabweans abroad. Platforms differ in the countries they serve, so we confirm what is open to your business and your target markets before you spend, then track every campaign through to enquiries and sales.",
        "problems": [
            "Your ad money is spread across several platforms and nobody can say which one pays for itself.",
            "Boosting posts brings likes and comments, but very few enquiries.",
            "Your cost per enquiry keeps rising and the reports don't explain why.",
            "Your ads reach plenty of people, but rarely the ones who are ready to buy.",
        ],
        "included": [
            ("Channel mix & budgets", "We recommend which platforms to use and how to split your budget, based on where your buyers actually spend their time."),
            ("Campaign build", "Account structure, audiences, keywords, placements and bidding set up properly from the start."),
            ("Ad creative & copy", "Static, carousel and short-video ads written and designed for each platform, then tested against each other."),
            ("Landing pages", "Fast, focused pages that turn ad clicks into calls, WhatsApp chats and form enquiries."),
            ("Retargeting", "Follow-up ads for people who visited your site, watched your videos or messaged you but haven't bought yet."),
            ("Tracking & reporting", "Conversions tracked in every ad platform and as key events in Google Analytics, with one monthly report across all your ads."),
        ],
        "steps": [
            ("Audit & plan", "We review any past campaigns, study your market and agree targets and budgets."),
            ("Build", "Accounts, tracking, audiences and creative are set up and checked before anything goes live."),
            ("Launch", "Campaigns start on the platforms that best fit your goals and budget."),
            ("Improve every week", "We adjust bids, audiences, keywords and creative, and move budget to what's working."),
        ],
        "faqs": [
            ("Which ad platforms do you manage?", "Google Ads (Search, Display, Shopping, Performance Max and more), YouTube, Microsoft Advertising, Meta (Facebook, Instagram and Messenger), Click-to-WhatsApp ads, WhatsApp Status ads where Meta offers them, LinkedIn and programmatic display. TikTok and ChatGPT ads are available for diaspora campaigns run by businesses registered in countries where those platforms sell ads. Pinterest, Snapchat, X, Reddit, Spotify, Apple and Amazon ads are available on request, where the platform accepts your business and target market. The main platforms each have their own page with the details."),
            ("What should our ad budget be?", "That depends on your goals, your industry and the value of each new customer to your business. We usually start with a test budget, learn what works, then scale up. Your ad spend is paid directly to the platforms."),
            ("Can you run ChatGPT ads for us?", "Not for audiences in Zimbabwe yet. As of November 2026, OpenAI doesn't sell ChatGPT ads to Zimbabwe-registered businesses or show them to people in Zimbabwe. If your business is registered in a country where ChatGPT ads are sold and you want to reach customers there, we can plan and manage the campaigns. If not, we can prepare your creative, landing pages and tracking so you're ready if OpenAI opens to more countries, and our AEO service helps you appear in ChatGPT's answers in the meantime."),
            ("Can you reach Zimbabweans living abroad?", "Yes. We can run campaigns for audiences in South Africa, the UK, the US, Australia and elsewhere, for things like property, education, groceries and family services. We reach them through location, interests and your own customer lists, never by targeting nationality."),
        ],
        "related": ["google-analytics", "cro", "digital-marketing"],
    },
    {
        "slug": "google-analytics",
        "name": "Google Analytics & Tracking",
        "menu": "GA4 and Tag Manager, tracking every enquiry",
        "icon": "chart",
        "description": "GA4 and Google Tag Manager set up properly for Zimbabwean websites: key events for WhatsApp clicks, calls and forms, plus dashboards you can act on.",
        "core": True,
        "short": "Google Analytics 4, Tag Manager and conversion tracking set up properly, so you can see which marketing brings in customers.",
        "title": "Google Analytics 4 (GA4) Set-up & Tracking in Zimbabwe",
        "h1": "See exactly which marketing <span class=\"hl\">brings you customers</span>",
        "intro": "Google Analytics 4 is free and powerful, but many installs are missing the things that matter most: enquiries, WhatsApp chats, calls and sales. We set up GA4 and Google Tag Manager properly, connect them to your ad accounts, and turn the numbers into reports you can act on.",
        "problems": [
            "Google Analytics was installed years ago and nobody has checked it since.",
            "You can see how many people visit, but not how many became enquiries or sales.",
            "Google Ads, Meta and your website all report different numbers for the same month.",
            "WhatsApp chats and phone calls that start on your website aren't counted anywhere.",
        ],
        "included": [
            ("GA4 set-up or rescue", "A clean Google Analytics 4 property with the right data streams, filters, retention settings and key events for your business."),
            ("Google Tag Manager", "All your tracking tags in one documented container, so changes don't need a developer."),
            ("Key events & conversions", "Form submissions, WhatsApp clicks, calls, email clicks, bookings and purchases tracked, and shared with Google Ads and Meta."),
            ("E-commerce tracking", "Product views, add-to-cart, checkout steps and revenue measured for online stores."),
            ("Consent & privacy", "Cookie consent and Google Consent Mode set up where your audience needs them, in line with your privacy policy."),
            ("Dashboards & training", "Data Studio dashboards (formerly Looker Studio) with your key numbers, plus a walk-through so your team can read GA4 with confidence."),
        ],
        "steps": [
            ("Tracking audit", "We check what's being measured, what's broken and what's missing."),
            ("Measurement plan", "We agree which actions count as leads and sales, and how each one will be tracked."),
            ("Implementation", "GA4, Tag Manager and ad-platform conversions are set up and tested."),
            ("Reporting", "Dashboards go live, and monthly reviews turn the data into decisions."),
        ],
        "faqs": [
            ("What is Google Analytics 4?", "Google Analytics 4 (GA4) is Google's free analytics tool. It shows how people find and use your website, and which channels lead to enquiries and sales. It replaced the older Universal Analytics in 2023."),
            ("Why don't my Google Ads and Facebook numbers match Google Analytics?", "Each platform counts results with its own rules and time windows. We set up consistent tracking across all of them, plus one dashboard, so you can compare channels fairly."),
            ("Can you track WhatsApp clicks and phone calls?", "Yes. Clicks on WhatsApp buttons, phone numbers and email links can be tracked as key events in GA4 and shared with Google Ads and Meta to improve your campaigns."),
            ("Do I need a cookie banner?", "If you use analytics or ad tracking, you should tell visitors, and in many cases ask for their consent, especially if you have visitors from the UK, the EU or other places with strict privacy rules. We'll recommend a set-up that suits your audience and your privacy policy."),
        ],
        "related": ["paid-ads", "cro", "lead-generation-crm"],
    },
    {
        "slug": "social-media",
        "name": "Social Media Management",
        "menu": "Content, community and social listening",
        "icon": "share",
        "description": "Social media management from Harare: strategy, content, community management and social listening across Facebook, Instagram, TikTok and LinkedIn.",
        "short": "Strategy, content, community management and social listening across Facebook, Instagram, TikTok and LinkedIn.",
        "title": "Social Media Management Agency in Harare, Zimbabwe",
        "h1": "Social media that builds a brand <span class=\"hl\">and</span> brings in business",
        "intro": "Many Zimbabweans use WhatsApp, Facebook, TikTok and Instagram every day. We help you show up there with a clear voice, content people actually want to watch, and a plan for turning followers into customers.",
        "problems": [
            "You post when you remember, and it shows.",
            "Your content looks like everyone else's in your industry.",
            "Messages and comments go unanswered for days.",
            "You don't know what your competitors are doing better.",
        ],
        "included": [
            ("Social media strategy", "Who you're talking to, what you say, which platforms matter and how social links to sales."),
            ("Content creation", "Photos, short videos, Reels, TikToks, carousels and captions produced to a monthly calendar."),
            ("Community management", "Replies to comments and DMs in your brand voice, with leads handed to your team quickly."),
            ("Social listening", "Tracking what people say about your brand, your competitors and your industry online."),
            ("Competitor analysis", "Benchmarking your social performance against the brands you compete with."),
            ("Influencer partnerships", "Finding and managing Zimbabwean creators who fit your brand and audience."),
        ],
        "steps": [
            ("Audit & strategy", "We review your channels and competitors, then set a clear content strategy."),
            ("Content calendar", "A monthly plan of posts, videos and campaigns you approve in advance."),
            ("Publish & engage", "We post, reply and keep your community active."),
            ("Report & refine", "Monthly insights on reach, engagement and, most importantly, enquiries."),
        ],
        "faqs": [
            ("Which platforms should my business be on?", "It depends on your audience. Facebook and WhatsApp reach the widest Zimbabwean audience, TikTok and Instagram skew younger, and LinkedIn is key for B2B. We'll recommend where to focus rather than spreading you thin."),
            ("Do you create the content?", "Yes. We plan, write, design and edit content, and can arrange photo and video shoots in Harare and other cities."),
            ("Is social media management the same as running ads?", "No. Management covers your organic content and community. Paid social ads are a separate service, though they work best together."),
        ],
        "related": ["paid-ads", "content-marketing", "digital-marketing"],
    },
    {
        "slug": "local-seo",
        "name": "Local SEO & Google Business Profile",
        "menu": "Show up on Google Maps in every town you serve",
        "icon": "pin",
        "description": "Google Business Profile and local SEO for Zimbabwean businesses: accurate listings, genuine reviews and location pages that help nearby customers find you.",
        "short": "Show up on Google Maps and \"near me\" searches in Harare, Bulawayo and every town you serve.",
        "title": "Local SEO & Google Business Profile Optimisation | Zimbabwe",
        "h1": "Get found by people searching nearby on <span class=\"hl\">Google Maps</span>",
        "intro": "When someone searches \"pharmacy near me\" in Avondale or \"car hire Victoria Falls\", Google shows a map with three businesses. Local SEO is how you compete for one of those three spots, and for many local businesses it's a sensible first step.",
        "problems": [
            "Your business doesn't show on Google Maps, or shows with the wrong details.",
            "Competitors have dozens of reviews and you have a handful.",
            "Your address, hours and phone number are different on every directory.",
            "You serve several towns but only appear in one.",
        ],
        "included": [
            ("Google Business Profile set-up & optimisation", "Categories, services, photos, products and posts completed and kept fresh, with customer questions answered."),
            ("Review strategy", "Simple systems to ask every customer for a Google review, plus guidance on replying to each one."),
            ("Local citations", "Consistent listings on Zimbabwean and international directories."),
            ("Location pages", "Dedicated pages for each town or suburb you serve."),
            ("Local link building", "Mentions from local news, associations, sponsors and partners."),
            ("Map rank tracking", "We track where you appear on the map across your service area."),
        ],
        "steps": [
            ("Audit", "We check your profile, listings, reviews and map rankings."),
            ("Optimise", "Your profile and website are tuned for local searches."),
            ("Build trust", "Reviews, citations and local links grow week by week."),
            ("Track", "Map rankings, calls and direction requests reported monthly."),
        ],
        "faqs": [
            ("My business doesn't have a shop. Can I still rank locally?", "Yes. Service-area businesses, like plumbers, caterers and consultants, can rank on Google Maps by setting a service area instead of showing an address."),
            ("How important are Google reviews?", "Very. Reviews affect both your map ranking and whether people choose you. We'll help you build a steady flow of genuine reviews from real customers."),
            ("Can you help a business with branches in several cities?", "Yes. We optimise each branch's profile and build location pages so every branch can rank in its own town."),
        ],
        "related": ["seo", "aeo", "website-development"],
    },
    {
        "slug": "ecommerce",
        "name": "E-commerce",
        "menu": "Online stores with local and international payments",
        "icon": "cart",
        "description": "Online stores for Zimbabwean retailers, with local and international payments, delivery zones, product ads and automated email and WhatsApp follow-up.",
        "short": "Online stores with local payments, plus the ads, emails and automations that make them profitable.",
        "title": "E-commerce Website Development & Marketing | Zimbabwe",
        "h1": "Online stores that <span class=\"hl\">sell every day</span>, not just on launch day",
        "intro": "We build online stores for Zimbabwean retailers and brands, connect local and international payment options, and then focus on what really decides success: bringing in profitable traffic and getting customers to come back for a second and third order.",
        "problems": [
            "Your store gets visitors but very few checkouts.",
            "Payment options don't suit local customers or the diaspora.",
            "You're paying for ads but have no idea of your real profit per order.",
            "Most customers only ever place one order.",
        ],
        "included": [
            ("Store design & build", "WooCommerce and Shopify stores designed for mobile shoppers."),
            ("Payments & delivery", "Integration with local payment options such as mobile money and cards, plus international gateways for diaspora buyers, and delivery zones across Zimbabwe."),
            ("Product feeds & Shopping ads", "Optimised product feeds for Google Shopping and Meta catalogue ads."),
            ("Profit-focused advertising", "Campaigns measured on profit per order and customer lifetime value, not just return on ad spend (ROAS)."),
            ("Email & WhatsApp automations", "Abandoned-cart reminders, welcome sequences and repeat-purchase flows."),
            ("Conversion rate optimisation", "Product pages, checkout and offers tested to lift your conversion rate."),
        ],
        "steps": [
            ("Plan", "Products, margins, payments and delivery mapped out."),
            ("Build", "Your store designed, built and tested on real phones."),
            ("Launch & advertise", "Shopping ads, social ads and launch campaigns go live."),
            ("Scale", "Automations, CRO and retention grow revenue per customer."),
        ],
        "faqs": [
            ("Which platform is best for an online store in Zimbabwe?", "WooCommerce (on WordPress) gives the most flexibility for local payment options. Shopify is great for brands selling regionally or internationally. We'll recommend the right fit for you."),
            ("Can customers pay with mobile money?", "Yes, we can integrate locally available payment gateways that support mobile money and cards, depending on your bank and provider."),
            ("Can you help me sell to Zimbabweans abroad?", "Yes. Diaspora-focused stores, for groceries, hampers, building materials and gifts, are a big opportunity, and we know how to market them."),
        ],
        "related": ["website-development", "email-whatsapp-marketing", "cro"],
    },
    {
        "slug": "email-whatsapp-marketing",
        "name": "Email & WhatsApp Marketing",
        "menu": "Automated follow-up by email and WhatsApp",
        "icon": "mail",
        "description": "Email and WhatsApp marketing for Zimbabwean businesses: lead nurturing, newsletters and automated follow-up, sent only to people who have opted in.",
        "short": "Newsletters, lead nurturing and automated WhatsApp and email flows that follow up every lead for you.",
        "title": "Email Marketing & WhatsApp Marketing Automation | Zimbabwe",
        "h1": "Follow up with every lead, <span class=\"hl\">automatically</span>",
        "intro": "Most leads aren't ready to buy the first time they contact you. Email and WhatsApp automations keep you top of mind, answer common questions and nudge people towards a sale, without your team chasing every single one by hand.",
        "problems": [
            "Leads go cold because nobody follows up in time.",
            "You've got a big customer list but never market to it.",
            "Your team answers the same WhatsApp questions all day.",
            "Your newsletters, if you send them, get few opens.",
        ],
        "included": [
            ("Lead nurturing sequences", "Automated messages that educate, build trust and move leads towards a decision."),
            ("WhatsApp Business automation", "Greeting messages, quick replies, catalogues and broadcast lists set up properly."),
            ("Newsletters", "Regular, genuinely useful newsletters that keep your audience engaged."),
            ("E-commerce flows", "Automated welcome series, abandoned-cart reminders, thank-you and review requests, and re-engagement messages."),
            ("List building", "Lead magnets and sign-up forms that grow your list with the right people."),
            ("Segmentation & reporting", "Different messages for different customer groups, with clear open, click and revenue figures."),
        ],
        "steps": [
            ("Map the journey", "We map how leads become customers today and where they drop off."),
            ("Write & design", "Sequences, templates and messages written in your voice."),
            ("Automate", "Flows built in your email platform and WhatsApp Business."),
            ("Optimise", "Subject lines, timing and offers tested to improve results."),
        ],
        "faqs": [
            ("Does email marketing work in Zimbabwe?", "Yes, especially for B2B, professional services and e-commerce. Paired with WhatsApp, which most of your customers already use every day, it gives you a low-cost way to follow up every lead."),
            ("Will WhatsApp broadcasts get my number blocked?", "It's much less likely when it's done properly. We only message people who've opted in and we follow WhatsApp's business policies, though WhatsApp can still restrict a number that many people block or report."),
            ("Which tools do you use?", "We work with popular platforms like Mailchimp, Brevo and Klaviyo, plus the WhatsApp Business app and the WhatsApp Business Platform where volumes justify it."),
        ],
        "related": ["lead-generation-crm", "ecommerce", "digital-marketing"],
    },
    {
        "slug": "lead-generation-crm",
        "name": "Lead Generation & CRM",
        "menu": "Lead capture, call tracking and CRM set-up",
        "icon": "funnel",
        "description": "Lead generation and CRM set-up for Zimbabwean businesses: every enquiry from ads, calls, WhatsApp and forms in one place, followed up and tracked.",
        "short": "Lead-gen systems, call tracking and CRM set-up (such as Pipedrive or HubSpot) that connect marketing to sales.",
        "title": "Lead Generation & CRM Set-up for Zimbabwean Businesses",
        "h1": "Fill your sales pipeline, then <span class=\"hl\">close more of it</span>",
        "intro": "Leads are only valuable if your team can follow them up and close them. We build lead generation systems and set up CRMs, so every enquiry from every channel lands in one place and nothing slips through the cracks.",
        "problems": [
            "Leads arrive by phone, WhatsApp, email and Facebook, and get lost.",
            "You can't tell which campaigns bring in deals, only clicks.",
            "Your sales team works from spreadsheets and memory.",
            "You've bought a CRM before, but nobody uses it.",
        ],
        "included": [
            ("Lead generation campaigns", "Multi-channel campaigns designed to bring in qualified, ready-to-talk leads."),
            ("CRM set-up & migration", "Pipedrive, HubSpot or Zoho set up around how your team really sells."),
            ("Call tracking", "Unique tracking numbers that show which ads and pages make the phone ring."),
            ("Lead scoring & routing", "Hot leads flagged and sent to the right salesperson instantly."),
            ("Sales & marketing alignment", "One source of truth so marketing spend can be judged on closed deals."),
            ("Team training", "Hands-on training so your team actually adopts the system."),
        ],
        "steps": [
            ("Map your sales process", "We document how a lead becomes a customer in your business."),
            ("Configure", "Pipelines, fields, automations and integrations built."),
            ("Connect marketing", "Forms, ads, WhatsApp and calls feed straight into the CRM."),
            ("Train & refine", "Your team is trained, and we refine the set-up as you grow."),
        ],
        "faqs": [
            ("Which CRM do you recommend?", "For most small and medium sales teams, Pipedrive is simple and effective. HubSpot suits businesses that want marketing and sales in one platform. We'll recommend the best fit for your budget and process."),
            ("Can you connect WhatsApp to a CRM?", "Yes. Using official integrations and the WhatsApp Business Platform, we can log WhatsApp conversations against contacts in many CRMs."),
            ("What is call tracking?", "Call tracking assigns different phone numbers to different ads or pages, so you can see exactly which marketing makes your phone ring."),
        ],
        "related": ["email-whatsapp-marketing", "google-analytics", "paid-ads"],
    },
    {
        "slug": "cro",
        "name": "Conversion Rate Optimisation",
        "menu": "Turn more of your visitors into customers",
        "icon": "trending",
        "description": "Conversion rate optimisation for Zimbabwean websites: UX audits, A/B tests, shorter forms and faster pages that turn more visitors into enquiries.",
        "short": "UX audits and A/B testing that turn more of your existing visitors into customers.",
        "title": "Conversion Rate Optimisation (CRO) & UX Audits | Zimbabwe",
        "h1": "Turn more of your visitors into <span class=\"hl\">paying customers</span>",
        "intro": "If twice as many of your visitors got in touch, your marketing would deliver twice the results for the same spend. Conversion rate optimisation finds what stops visitors from taking action and fixes it, using real behaviour data rather than guesswork.",
        "problems": [
            "Plenty of visitors, very few enquiries or sales.",
            "Visitors leave your landing pages within seconds.",
            "Your checkout or contact form is long and confusing.",
            "Design decisions are made on gut feel.",
        ],
        "included": [
            ("UX audits", "An expert review of your site's usability, clarity and trust signals."),
            ("Analytics & heatmaps", "Where people click, scroll and drop off, so we fix the right things."),
            ("Landing page design", "High-converting pages for ads and campaigns."),
            ("A/B testing", "Headlines, offers, layouts and forms tested against each other."),
            ("Form & checkout optimisation", "Fewer fields, clearer steps and fewer abandoned checkouts."),
            ("Speed improvements", "Faster pages convert better, especially on mobile data."),
        ],
        "steps": [
            ("Research", "Analytics, heatmaps, recordings and customer feedback."),
            ("Hypothesise", "A prioritised list of changes most likely to lift conversions."),
            ("Test", "Changes tested properly so we know what really works."),
            ("Roll out", "Winning changes go live, and the next test begins."),
        ],
        "faqs": [
            ("What's a good conversion rate?", "It varies by industry and offer, but many sites convert only 1 to 3 per cent of visitors. Small improvements to that number can make a big difference to revenue."),
            ("Do I need lots of traffic for CRO?", "A/B testing works best with steady traffic, but smaller sites still gain from UX audits and simple, well-tested fixes."),
        ],
        "related": ["website-development", "google-analytics", "paid-ads"],
    },
    {
        "slug": "content-marketing",
        "name": "Content Marketing & Link Building",
        "menu": "Articles, guides and digital PR that earn links",
        "icon": "pen",
        "description": "Content marketing and link building for Zimbabwean businesses: articles, guides, video scripts and digital PR that answer buyers' questions and earn links.",
        "short": "Articles, guides, video scripts and digital PR that build authority with Google, AI and your buyers.",
        "title": "Content Marketing & Link Building Agency | Zimbabwe",
        "h1": "Content that earns <span class=\"hl\">trust, rankings and links</span>",
        "intro": "Useful content answers your customers' questions clearly and completely, and that is what both Google and AI assistants reward. We plan, write and promote content that builds your authority and brings in buyers.",
        "problems": [
            "Your blog hasn't been updated in a year, or ever.",
            "Your content is generic and could be about any company.",
            "You publish articles but they never rank or get shared.",
            "Very few websites link to yours.",
        ],
        "included": [
            ("Content strategy", "Topics mapped to the questions your buyers ask at every stage."),
            ("Articles & guides", "In-depth, well-researched content written by people who understand your industry."),
            ("Service & landing page copy", "Clear, persuasive copy for the pages that make you money."),
            ("Video & social scripts", "Scripts for YouTube, TikTok and Reels that repurpose your best ideas."),
            ("Digital PR & link building", "Stories and assets that earn coverage and links from respected sites."),
            ("Content refreshes", "Updating older content so it keeps ranking."),
        ],
        "steps": [
            ("Research", "Keyword, competitor and audience research to find content gaps."),
            ("Plan", "A content calendar tied to business goals."),
            ("Create", "Writing, design and editing to a high standard."),
            ("Promote", "Distribution, outreach and link building."),
        ],
        "faqs": [
            ("Do you use AI to write content?", "We use AI tools to speed up research, but every piece is planned, written and edited by people who know your industry. Thin, generic AI content doesn't rank or win trust."),
            ("How many articles do I need each month?", "Quality beats volume. For most businesses, a few genuinely excellent pieces a month outperform many short, shallow posts."),
        ],
        "related": ["seo", "aeo", "social-media"],
    },
    {
        "slug": "hosting-maintenance",
        "name": "Hosting, Maintenance & Speed",
        "menu": "Secure hosting, backups, updates and speed fixes",
        "icon": "server",
        "description": "Website hosting, backups, updates, security and speed optimisation for Zimbabwean businesses, so your site stays fast, safe and online.",
        "short": "Secure hosting, backups, updates and speed optimisation to keep your website fast, safe and online.",
        "title": "Website Hosting, Maintenance & Speed Optimisation | Zimbabwe",
        "h1": "A fast, secure website <span class=\"hl\">you never have to worry about</span>",
        "intro": "A slow, hacked or broken website costs you customers every hour it's down. We host, back up, update and speed up websites for Zimbabwean businesses, so yours stays fast and online.",
        "problems": [
            "Your website is slow, especially on mobile data.",
            "Plugins and themes haven't been updated in ages.",
            "You've been hacked before, or worry that you will be.",
            "Nobody is responsible when something breaks.",
        ],
        "included": [
            ("Managed hosting", "Fast, reliable hosting with SSL certificates included."),
            ("Regular backups", "Scheduled off-site backups, so your site can be restored quickly if something goes wrong."),
            ("Updates & security", "Core, theme and plugin updates, malware scanning and firewall protection."),
            ("Speed optimisation", "Image compression, caching and code clean-up for faster load times."),
            ("Uptime monitoring", "Automatic checks that alert us if your site goes down, so we can act fast."),
            ("Content updates", "Small edits and updates handled for you each month."),
        ],
        "steps": [
            ("Health check", "We review speed, security and set-up."),
            ("Migrate", "Your site moved to our hosting with minimal downtime."),
            ("Optimise", "Speed and security improvements applied."),
            ("Maintain", "Ongoing updates, backups and monitoring."),
        ],
        "faqs": [
            ("Can you take over a website someone else built?", "Yes. We'll audit it first, then take over hosting and maintenance, or recommend a rebuild if it's beyond saving."),
            ("Will moving hosting affect my email?", "We'll plan any move carefully, including your domain and email settings, so nothing gets lost."),
        ],
        "related": ["website-development", "cro", "seo"],
    },
]

SERVICE_BY_SLUG = {s["slug"]: s for s in SERVICES}

INDUSTRIES = [
    ("Retail & e-commerce", "cart", "Online stores, supermarkets, fashion and electronics retailers selling locally and to the diaspora."),
    ("Tourism & hospitality", "globe", "Lodges, hotels, safari operators and tour companies in Victoria Falls, Kariba, Nyanga and beyond, attracting local and international travellers."),
    ("Real estate & construction", "home", "Developers, estate agents and builders selling stands, homes and projects, including to Zimbabweans abroad."),
    ("Education", "book", "Private schools, colleges, training centres and online courses filling places every intake."),
    ("Healthcare & pharmacies", "heart", "Clinics, specialists, dentists and pharmacies attracting patients with trust-first marketing."),
    ("Professional services", "briefcase", "Law firms, accountants, consultants and insurers winning high-value clients."),
    ("Agriculture & agribusiness", "leaf", "Seed, fertiliser, irrigation and equipment suppliers, plus farmers selling direct."),
    ("Automotive", "car", "Dealerships, car hire, spares and service centres generating test drives and bookings."),
    ("Mining & industrial", "tool", "Suppliers, engineering firms and service providers reaching procurement decision-makers."),
    ("Food & beverage", "coffee", "Restaurants, cafés, caterers and FMCG brands building a loyal customer base."),
    ("Solar & energy", "sun", "Solar installers and energy companies capturing demand for reliable power."),
    ("NGOs & non-profits", "users", "Organisations raising awareness, recruiting and communicating impact."),
]

FAQS_GENERAL = [
    ("Where is Smart Click Media based?", "We're based in Harare, Zimbabwe, and we can work with businesses in every province, from Bulawayo and Mutare to Victoria Falls, Gweru and Masvingo, as well as brands targeting Zimbabweans abroad."),
    ("What services does Smart Click Media offer?", "Digital marketing strategy, website design and development, SEO, AEO (AI search optimisation), paid ads on the major platforms (Google, YouTube, Microsoft, Meta, WhatsApp, LinkedIn and programmatic, plus TikTok and ChatGPT for diaspora campaigns where available), Google Analytics and tracking, social media management, local SEO, e-commerce, email and WhatsApp marketing, lead generation and CRM, conversion rate optimisation, content marketing, and website hosting and maintenance."),
    ("When can I contact you?", "Any time. We're open 24/7. Call or WhatsApp 0771 269 979, or email info@smartclick.co.zw."),
    ("How do I get started?", "Call or WhatsApp us on 0771 269 979, email info@smartclick.co.zw, or fill in the form on our contact page. We'll set up a free strategy session, look at your current marketing and suggest a plan."),
    ("Do you work with small businesses?", "Yes. We can work with start-ups, small and medium businesses and large organisations. We'll be upfront about the budget needed to get results, and we won't sell you services you don't need."),
    ("How do you report on results?", "You get a clear monthly report covering enquiries, sales, spend and the work done, plus a review call. We focus on business results rather than likes and impressions."),
    ("Can you market to Zimbabweans in the diaspora?", "Yes. We can run campaigns that reach Zimbabweans in South Africa, the UK, the US, Australia and elsewhere for property, education, groceries, hampers and other services. We reach them through location, interests and your own customer lists, never by targeting nationality."),
    ("Can you create content in Shona or Ndebele?", "Yes. Campaigns and content can be produced in English, Shona or Ndebele, depending on what connects best with your audience."),
]

# ---------------------------------------------------------------------------
# Larger collections are kept as JSON in _build/data/ so they are easy to edit.
# ---------------------------------------------------------------------------
import json as _json
import os as _os

_DATA = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "data")


def _load(name):
    path = _os.path.join(_DATA, name)
    if not _os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as f:
        return _json.load(f)


AD_PLATFORMS = _load("ad_platforms.json")   # pages under services/paid-ads/
PORTFOLIO = _load("portfolio.json")         # example projects under portfolio/
ARTICLES = _load("articles.json")           # insights/ blog articles
LOCATIONS = _load("locations.json")         # locations/ city pages
