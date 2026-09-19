# Body.Care — Phase-Wise Build Prompts

Copy-paste prompts to build, extend, or rebuild **Body.Care** in stages with any capable AI coding assistant.

Each phase has three parts: **Goal**, **Prompt** and **Acceptance criteria**. Run the phases in order. Phases 1–7 are already implemented in this repo; use them to rebuild from scratch or to clone the model onto another domain.

---

## PHASE 0 — Strategy lock (run once)

**Goal:** Fix the positioning before writing any code.

**Prompt:**
> You are a growth strategist for a health-and-beauty publisher. The domain is **Body.Care**. Define the positioning as "an independent, science-first, head-to-toe body care hub with free interactive tools and a consented lead engine."
>
> Output the following:
> 1. An 8-category information architecture: Face & Skin, Body Care, Sun Care, Hair & Scalp, Hands/Nails/Feet, Oral Care, Men's Care, Sleep & Wellness.
> 2. 6 interactive tools, each of which doubles as a lead magnet.
> 3. A stacked revenue model: AdSense, clinic leads, affiliate, YouTube, sponsorships, awards seal licensing, donations. Include per-stream yield assumptions.
> 4. A 12-month content calendar with 150 keyword-clustered articles.
> 5. E-E-A-T requirements for YMYL content.
>
> Recommend clearly; don't hedge. Flag legal risks: lead privacy, contests, medical claims.

**Acceptance criteria:** One-page strategy, revenue table with assumptions, IA diagram, 150-topic backlog.

---

## PHASE 1 — Foundation and design system

**Goal:** A static, dependency-free site that runs on the free GitHub Pages plan.

**Prompt:**
> Build a static website for Body.Care. It must host on GitHub Pages free tier: no server, no build step required to serve, and all paths relative so it works both at `username.github.io/repo/` and at a custom domain.
>
> Create:
> - A Python generator in `/build` that writes HTML to the repo root, with shared layout functions for head, header, footer and overlays.
> - `assets/css/main.css` with design tokens on `:root`:
>   - Palette: cream background #fbf8f3, deep teal brand #0f5e59, coral accent #e8674a.
>   - Fonts: Fraunces for headings, Inter for body.
>   - Full dark mode via `prefers-color-scheme` plus a `[data-theme]` toggle.
>   - 16px mobile gutters and no horizontal scroll at 360px width.
> - Components: sticky blurred header with mobile menu, buttons, cards, stat tiles, chips, option cards, multi-step stepper with progress bar, forms, tables, FAQ accordions, callouts, ad slots, modal, cookie banner, sticky mobile CTA, toast, countdown and meters.
> - Accessibility: skip link, focus-visible rings, reduced-motion support, ARIA labels and print styles.
> - `assets/js/config.js`: a single config object holding every monetisation ID (AdSense client and slots, GA4, form endpoints per form type, donation links, Amazon tag, YouTube channel and video list, contest settings, social links). Every feature must degrade gracefully when its value is blank.

**Acceptance criteria:** Lighthouse Accessibility ≥ 95; no layout shift from ads (reserved min-height); dark mode works.

---

## PHASE 2 — Content engine and SEO

**Goal:** Rankable YMYL content with full structured data.

**Prompt:**
> Create `build/content.py` holding CATEGORIES and ARTICLES as data. Each article has: slug, category, title, description, keywords, read time, HTML body with `h2#sN` anchors, FAQs, a "when to see a doctor" text, and 2–4 authoritative sources (AAD, NHS, CDC, Mayo).
>
> Write 14 evidence-based guides covering:
> - 3-step routine basics
> - Sunscreen
> - Dry body skin
> - Body acne
> - Retinol for beginners
> - Hyperpigmentation on darker skin
> - Eczema
> - Scalp and hair
> - Hands and nails
> - Feet
> - Oral care
> - Men's grooming
> - Body odour and sweat
> - Sleep and skin
>
> Each generated article page needs:
> - Breadcrumbs and a byline with editorial-policy link, date, read time and source count.
> - Share buttons (native, Pinterest, WhatsApp).
> - A sticky table of contents with related guides.
> - An auto-inserted in-article ad after the second section.
> - The doctor callout, FAQ, numbered sources, a lead-capture band and a reading-progress bar.
> - JSON-LD for MedicalWebPage (with citations), FAQPage and BreadcrumbList.
>
> Also generate:
> - `library.html` with category filters, live text filter and hash deep-links.
> - `search.html` backed by a generated `search-index.json`.
> - `sitemap.xml` with priorities, `robots.txt`, canonical tags, Open Graph/Twitter tags and a 1200×630 OG image.
>
> Never invent reviewer names, statistics or testimonials.

**Acceptance criteria:** Schemas pass Google's Rich Results Test; every page has a unique title and description; no broken internal links.

---

## PHASE 3 — Interactive tools (the traffic and link moat)

**Goal:** Six tools that rank on their own, earn backlinks and capture leads.

**Prompt:**
> Build `assets/js/tools.js` and `assets/js/ingredients.js`, plus one page per tool under `/tools/`.
>
> 1. **Skin Type Quiz:** 7-step stepper with weighted scoring across oily, dry, combo and normal, plus a sensitivity flag. Show the result with a starter routine and save it to localStorage.
> 2. **Routine Builder:** 6 steps (type, concerns, sensitivity, pregnancy, complexity, budget). Output AM, PM and weekly tables.
>    - Rules: pregnancy removes retinoids and high-dose BHA; sensitive skin means fragrance-free and gentler actives; the pigment concern adds tinted mineral SPF.
>    - Pre-fill the skin type from the quiz result.
> 3. **Ingredient Checker:** paste an INCI list. Tokenise it and match against an 80+ entry database. Each entry has keys, rating (good/caution/avoid/neutral), function, note, and flags: comedogenic, sensitiser, pregnancy, fungal-acne, photosensitising.
>    - The user picks profile chips (acne, sensitive, fungal, pregnant) to get personal alerts.
>    - Show stats tiles, a gentleness score and a per-ingredient table.
> 4. **Layering Checker:** choose from retinoid, acid, vitamin C, benzoyl peroxide and niacinamide. Show a conflict matrix with explanations and the correct layering order.
> 5. **Sunscreen Calculator:** body-area chips, UV index and activity. Output ml per application, reapply interval, SPF advice, and a reapply countdown timer with Notification API support.
> 6. **Hydration Calculator:** weight in kg or lb, exercise, climate and life stage. Output litres, cups and fl oz, plus a daily distribution chart.
>
> Also add a homepage **Body Care Score**: a 6-question self-assessment that returns a score out of 100 and the user's weakest areas.
>
> Every tool must, on completion, reveal a lead form pre-filled with a summary of that tool's result. Send a GA4 `tool_complete` event.

**Acceptance criteria:** All tools work offline after first load; results are correct for sample inputs; zero console errors.

---

## PHASE 4 — Lead generation engine (primary profit centre)

**Goal:** Turn visitors into consented, scored, sellable leads.

**Prompt:**
> Build `free-plan.html` as the site's main conversion page.
>
> **The wizard (5 steps):**
> 1. Goals (multi-select)
> 2. Skin type
> 3. Age, country, budget and life stage
> 4. Professional-help interest, city and timeline
> 5. Name, email, optional phone/WhatsApp, a required email consent box, and a separate *optional* consent to share details with up to 3 partner clinics
>
> **Before submit:** compute `lead_score`. Clinic interest +40, phone +15, timeline within 1 month +20, budget $60+ +15, partner consent +10. Set `lead_tier` to HOT (≥60), WARM (≥30) or NURTURE.
>
> **Form handling:** one universal JS handler for all `form[data-form]` forms (plan, clinic, newsletter, partner, contest, careers, contact). It must:
> - Include honeypot anti-spam.
> - POST JSON to the per-type endpoint from config, falling back to a pre-filled mailto when no endpoint is set.
> - Attach UTM parameters, gclid, landing page and current page.
> - Fire a GA4 `generate_lead` event.
>
> **Every page carries these capture points:**
> - Header "Free Plan" button
> - Sticky mobile CTA
> - Exit-intent/timed modal (once per 7 days, never after conversion, suppressed on the plan page)
> - Footer newsletter
> - Lead band inside articles
> - Post-tool capture
>
> Add a B2B section recruiting partner clinics that links to the advertise page.

**Acceptance criteria:** A complete wizard submission produces a JSON payload with all fields plus score, tier and attribution.

---

## PHASE 5 — Monetisation layers

**Goal:** AdSense, affiliate, YouTube and sponsorship.

**Prompt:**
> **AdSense:**
> - Add reserved ad slots: header (horizontal), in-article (fluid), sidebar (vertical), multiplex (autorelaxed) and footer.
> - Load the AdSense script only after cookie consent. "Essential only" sets `requestNonPersonalizedAds=1`.
> - Ship `ads.txt` with a placeholder line.
>
> **Affiliate:** build `picks.html` with ingredient-first category picks linking to Amazon search. Auto-append the Amazon tag from config. Mark links `rel="sponsored"`, track clicks, and include a disclosure callout.
>
> **YouTube:** build `videos.html` with click-to-load facades (thumbnail first, iframe only on click, using youtube-nocookie), category filters, a channel subscribe CTA and a video-topic request form.
>
> **Sponsorship:** build `advertise.html` with a media kit, three packages (newsletter, sponsored tool/guide, performance leads), a clinic lead program, brand review submissions, and a partner enquiry form that captures budget and markets.

**Acceptance criteria:** With config blank, placeholders show and nothing breaks. With IDs filled, ads render in every slot.

---

## PHASE 6 — Donations, contests, awards, hiring

**Goal:** Community revenue and growth loops.

**Prompt:**
> **`support.html`:**
> - One-time/monthly toggle, amount tiers plus a custom amount, and a live summary.
> - Checkout routing priority: Stripe Payment Link, then PayPal (amount pre-filled), then Ko-fi, then Buy Me a Coffee, then GitHub Sponsors, then mailto pledge.
> - Goal progress meter from config, a transparent fund-allocation chart, and a membership ("Body.Care Circle") description.
> - Sponsor-a-tool and fund-a-prize options, plus free ways to help.
>
> **`contests.html`:**
> - Monthly giveaway with a live countdown (auto end-of-month) and an entry form (18+ confirmation, consent).
> - After entry, generate a personal referral link that awards +3 bonus entries.
> - Readers' Choice Awards with 10 categories and a nomination form; winners can license the seal.
> - Prize sponsorship and creator challenges.
> - An official rules summary: no purchase necessary, eligibility, skill-testing question for Canada.
>
> **`careers.html`:** 8 roles (writers, medical reviewers, video creators, SEO, partnerships, community, translators, ambassadors) and an application form.

**Acceptance criteria:** Countdown ticks; referral link appears after entry; donation routing works with any subset of links configured.

---

## PHASE 7 — Trust, legal, PWA, QA, deploy

**Goal:** Pass AdSense review and ship.

**Prompt:**
> **Pages:** `about.html` (mission, editorial policy, how we make money, inclusivity), `contact.html`, `privacy.html` (AdSense cookie disclosure, consent, GDPR/CCPA/PIPEDA/Law 25/DPDP rights, health-data handling), `terms.html`, and `disclaimer.html` (medical, affiliate, sponsored).
>
> **404:** a `404.html` that works at any path depth on GitHub Pages by injecting `<base href>` from the hostname.
>
> **PWA:** `manifest.webmanifest`, 192 and 512 icons, a service worker (network-first pages, cache-first assets, offline fallback) and `.nojekyll`.
>
> **QA:** run a Playwright crawl of every page. Check for zero JS errors, zero broken internal links and no horizontal overflow at 390px and 1280px. Run functional tests of every tool and every form flow.
>
> **Deploy:** push to GitHub and enable Pages from the `main` branch root.

**Acceptance criteria:** Crawl is clean; the site loads at `https://<user>.github.io/<repo>/`.

---

## PHASE 8 — Go-live configuration (manual, ~1 hour)

1. **Custom domain:** In repo Settings → Pages → Custom domain, enter `body.care`. At your registrar, add A records → `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`, and a `www` CNAME → `webworksa1.github.io`. Then tick **Enforce HTTPS**.
2. **Forms:** Create Formspree forms (free plan: 50 submissions/month) or a Google Apps Script/Make webhook, and paste the endpoints into `config.js → forms`. **Leads aren't captured server-side until this is done.**
3. **AdSense:** Apply with body.care, paste `ca-pub-…` and the slot IDs into config, and update `ads.txt`. Enable Google's certified CMP for EEA/UK traffic.
4. **GA4:** Paste the measurement ID and mark `generate_lead` as a conversion.
5. **Donations:** Create Stripe Payment Links (one-time + monthly) and paste the PayPal, Ko-fi and other links.
6. **Affiliate:** Join Amazon Associates and set `amazonTag`.
7. **YouTube:** Set your channel URL and replace the videos list with your own uploads.
8. **Search Console:** Verify the domain and submit `sitemap.xml`.

---

## PHASE 9 — Growth prompts (repeat monthly)

- **Content:** "Write 10 new Body.Care guides for the cluster `<cluster>` in the exact `content.py` schema. Target long-tail 'how to / best / vs / for <skin type>' keywords. Cite AAD, NHS or peer-reviewed sources, and include a doctor box and 3 FAQs." Then rebuild and push.
- **Programmatic SEO:** "Generate an ingredient page for every entry in `ingredients.js` (`/ingredients/<slug>.html`) with what it does, who it's for, conflicts, pregnancy notes, schema and internal links to the tools."
- **Localisation:** "Clone the top 20 guides and all tools into `/es/`, `/fr/`, `/hi/` with hreflang tags."
- **Lead ops:** "Build a Google Apps Script that receives form JSON, writes to Sheets, emails HOT leads instantly to the matched clinic by city, and sends a Mailchimp/Beehiiv welcome sequence."
- **Pinterest and Shorts:** "Create 30 vertical pin/Short scripts from existing guides, each linking to a tool."

## PHASE 10 — Scale plays (bold path)

- Recruit 3 board-certified dermatologists as named reviewers. This is the biggest YMYL ranking lever. Only then add "Medically reviewed by" badges.
- Sign 10 clinics per metro on pay-per-lead (Toronto, Montréal, Vancouver, NYC, LA, London, Dubai, Mumbai, Delhi, Bangalore).
- Launch Body.Care Awards annually and license the winner seal ($1k–$5k per brand).
- Offer a premium membership: ad-free, saved routines, monthly derm AMA.
- Private-label launch (cleanser, moisturiser, SPF) once the newsletter passes 50k subscribers.
