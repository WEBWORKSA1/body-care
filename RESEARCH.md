# Body.Care — Concept, Competitive Research & Revenue Model

## 1. The winning concept

**Body.Care = an independent, science-first "head-to-toe" care hub + free interactive tools + a consented lead engine.**

Why this beats the alternatives for this domain:

| Option | Traffic ceiling | RPM / yield | Moat | Verdict |
|---|---|---|---|---|
| Skincare-only blog | High, but saturated (Byrdie, Allure, Healthline) | Mid | Weak | ❌ Me-too |
| E-commerce store (own brand) | Paid-traffic dependent | High margin, high capex | Brand | ⚠️ Phase 3 option, not launch |
| Directory of clinics | Low organic | Leads only | Medium | ⚠️ Folded in as the lead engine |
| **Content + tools + lead engine (chosen)** | **Very high (whole-body keyword universe)** | **3 stacked revenue lines per visit** | **Tools = links + return visits; data = lead scoring** | ✅ |

The domain literally *is* the category ("body care"), which covers skin, body, sun, hair/scalp, hands/nails/feet, oral, men's care and sleep. Almost every competitor covers only one slice (skincare **or** health **or** beauty retail). Owning the umbrella term lets Body.Care rank for the long tail across all slices and cross-sell between them.

## 2. Revenue model (stacked per visit)

| Stream | Mechanism in the build | Assumption (tier-1 health/beauty benchmarks, conservative) |
|---|---|---|
| Google AdSense | Header, in-article, sidebar, multiplex, footer slots; consent banner with non-personalised fallback | $8–$20 RPM per 1,000 pageviews |
| Clinic / practitioner leads | `free-plan.html` 5-step wizard → lead score (HOT/WARM/NURTURE), explicit partner consent | $25–$150 per consented aesthetic/derm lead; typical sale $30–$60 |
| Affiliate | `picks.html`, Amazon tag auto-appended from config | 3–10% commission; ~$0.5–$2 EPC per 1,000 PV |
| YouTube | `videos.html` facades, channel CTA; own uploads earn YPP revenue | $3–$10 RPM for beauty/health on YouTube |
| Sponsorships | Newsletter slots, sponsored tools/guides, prize sponsorship, awards seal licensing | $250–$5,000 per placement once list > 10k |
| Donations / membership | `support.html`: one-time + monthly, Stripe/PayPal/Ko-fi/BMC/GitHub Sponsors/Patreon | 0.1–0.5% of engaged users; $5–$15 avg |

**Illustrative month at 100k pageviews / 70k visitors (assumptions, not promises):**

- AdSense: 100k × $12 RPM = **~$1,200**
- Lead engine: 70k × 1.5% plan-completion = 1,050 leads; 20% tick partner consent = 210 × $40 = **~$8,400** *(this is the profit centre — requires signed clinic buyers)*
- Affiliate: **~$150–$300**
- Newsletter sponsorship (list growing ~1,000+/mo from 6 lead magnets): **$0 → $1,000+** after month 6
- Donations: **~$100–$300**

Lead generation is worth 5–7× AdSense at the same traffic, which is why the lead wizard is the site's primary CTA on every page (header button, sticky mobile CTA, exit-intent modal, post-tool capture, in-article bands).

## 3. Competitive research — 30 sites reviewed

**[F]** = fetched and inspected. **[S]** = the site blocked automated access, so the notes come from search results and known public features.

| # | Site | Key features extracted |
|---|---|---|
| 1 | Healthline [F] | Condition/Wellness/Product-review IA; calculators; newsletters; 130+ medical reviewers; content-integrity policy; Bezzy communities |
| 2 | WebMD [F] | Symptom checker, drug interaction checker, BMI/ovulation calculators; slideshows, video; "100+ doctors"; sponsored special sections |
| 3 | Mayo Clinic [F] | A–Z health library; appointment request; e-newsletter; **large donation CTA**; no ads |
| 4 | Cleveland Clinic [F] | 7-group health library + filters; Health Essentials newsletter; podcasts; book-appointment CTA |
| 5 | Medical News Today [F] | Citation counts on articles; myth-busting series; tools; editorial process page |
| 6 | Verywell Health [S] | "Medically reviewed / fact-checked" bylines; numbered sources; affiliate "tested" roundups |
| 7 | Everyday Health [S] | Review board; many condition newsletters; quizzes; sponsored hubs |
| 8 | AAD public site [F] | Diseases, everyday care, **darker skin tones hub**; find-a-derm locator; free screening campaigns; donations |
| 9 | DermNet [F] | 25k+ images; symptom-based skin checker; PRO subscription; donations; image licensing |
| 10 | Byrdie [S] | **Beauty Awards** amplified by press; review board; affiliate |
| 11 | Allure [S] | Best of Beauty **seal licensing**; Beauty Box subscription; Readers' Choice |
| 12 | Paula's Choice [F] | **Ingredient dictionary** rated Best→Worst with citations; skin quiz; email-for-discount |
| 13 | INCIDecoder [F] | **Paste-an-INCI decoder**; product/ingredient DB; monthly newsletter |
| 14 | Skinsort [F] | Routine creator; fungal-acne & pore-clog checkers; product compare; dupe finder |
| 15 | The Ordinary [F] | 11-step **regimen builder that asks for email at step 1**; layering guide |
| 16 | Sephora [F] | Loyalty points; "Clean at" badges; community gallery |
| 17 | CeraVe [F] | 6 product-finder quizzes; "Skin Smarts" hub; **sweepstakes**; where-to-buy |
| 18 | mindbodygreen [F] | 5 segmented newsletters; own supplements; certification courses |
| 19 | Well+Good [F] | Expert interviews; wellness verticals |
| 20 | goop [F] | Commerce-first; refer-a-friend; waitlists |
| 21 | Prevention [S] | Premium membership; Beauty Awards; review board |
| 22 | SELF [S] | Healthy Beauty Awards judged by dermatologists |
| 23 | Women's Health [S] | WH+ paid membership; advisory board |
| 24 | Men's Health [S] | Grooming Awards with **brand submissions**; Amazon storefront |
| 25 | Skin Type Solutions [F] | 16-type quiz → "shop my routine"; rewards cashback; physician finder |
| 26 | Lab Muffin [F] | Chemistry-PhD explainers; **free PDF lead magnet**; YouTube; book |
| 27 | NHS [F] | A–Z conditions; "when to get help" boxes; last-reviewed dates; accessibility |
| 28 | Curology [F] | Quiz → provider → subscription funnel; hard proof stats; before/after |
| 29 | Glamour Beauty [S] | Awards; affiliate roundups; video |
| 30 | Harper's Bazaar Beauty [S] | "Best of" affiliate lists; membership upsell |

## 4. Must-have features, and where each one is in this build

| Feature (source pattern) | Status in Body.Care v1 |
|---|---|
| A–Z/categorised library with filters (NHS, Cleveland) | ✅ `library.html` with 8 categories, live filter, hash deep-links |
| Fixed article template: body, "when to see a doctor", FAQ, sources (NHS, MNT) | ✅ All 14 guides + MedicalWebPage/FAQ/Breadcrumb schema |
| Darker-skin coverage (AAD) | ✅ Hyperpigmentation guide; mineral-tint, mandelic, PIH logic in tools |
| Skin-type quiz (Paula's, Baumann) | ✅ `tools/skin-quiz.html` |
| Regimen builder with pregnancy/sensitivity logic (The Ordinary) | ✅ `tools/routine-builder.html` |
| INCI decoder + fungal-acne/pore-clog flags (INCIDecoder, Skinsort) | ✅ `tools/ingredient-checker.html` (80+ entries) |
| Layering/compatibility (The Ordinary guide) | ✅ `tools/layering-checker.html` |
| Calculators (WebMD, Healthline) | ✅ Sunscreen (+ reapply timer), Hydration, Body Care Score |
| Quiz → email capture (The Ordinary, Curology) | ✅ Every tool unlocks a pre-filled "email me this + 30-day plan" form |
| Consultation / provider funnel (Curology, AAD locator) | ✅ `free-plan.html` wizard + clinic match + lead scoring |
| Segmented newsletter (mindbodygreen) | ✅ Footer, modal, tool and wizard sources are tagged per form |
| Sweepstakes (CeraVe) + awards and seal licensing (Allure, Byrdie) | ✅ `contests.html`: monthly giveaway, countdown, referral bonus links, awards nominations |
| Donations (Mayo, AAD, DermNet) | ✅ `support.html` with one-time/monthly, goal meter, allocation transparency |
| Affiliate with disclosure (Verywell, Skinsort) | ✅ `picks.html` + disclaimer page |
| Editorial policy / E-E-A-T pages | ✅ `about.html#editorial`, disclaimer, privacy |
| Video (all majors) | ✅ `videos.html` click-to-load facades (fast LCP) |
| PWA / offline | ✅ manifest + service worker |
| Site search | ✅ Client-side JSON index |

**Deliberately excluded (honesty and risk):** symptom checker and "medically reviewed" badges. Both need real credentialed reviewers (see §5). The careers page recruits reviewers. Add their names only once they have actually signed off.

## 5. Risks and how the build handles them

- **YMYL / Google E-E-A-T:** health content is ranked strictly. Every guide cites primary sources and has a doctor box. The build contains no fake reviewer names, testimonials or traffic statistics. Getting credentialed reviewers is the single biggest ranking lever.
- **Lead-privacy law (GDPR, PIPEDA/Quebec Law 25, CCPA):** partner sharing uses a separate, optional checkbox, and the privacy policy covers it.
- **AdSense approval:** needs original content (✅ 14 long-form guides), policy pages (✅) and ads.txt (✅ placeholder). For EEA/UK traffic, turn on Google's certified CMP inside AdSense.
- **Contest law:** the rules include no-purchase-necessary, age limits and a skill-testing question for Canadian winners. Have counsel review the rules for each country you accept entries from.
