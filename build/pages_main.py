# -*- coding: utf-8 -*-
from layout import page, ad, breadcrumb, crumb_schema, plan_form, e, SITE, NAME, I
from content import ARTICLES, CATEGORIES

CATN = {k: n for k, n, _ in CATEGORIES}
CATI = {k: i for k, _, i in CATEGORIES}

def article_card(a, base="{base}"):
    return (f'<a class="card reveal" data-cat="{a["cat"]}" href="{base}articles/{a["slug"]}.html">'
            f'<span class="tag">{CATI[a["cat"]]} {CATN[a["cat"]]}</span><h3>{e(a["title"])}</h3><p>{e(a["desc"])}</p>'
            f'<div class="card-meta"><span>{a["mins"]} min read</span><span>Evidence-based</span></div></a>')

TOOLS = [
    ("skin-quiz.html", "🧪", "Skin Type Quiz", "7 questions → your skin type, sensitivity flag and a starter routine."),
    ("routine-builder.html", "🗓️", "Routine Builder", "A personalised AM/PM/weekly routine for your type, concerns and budget."),
    ("ingredient-checker.html", "🔬", "Ingredient Checker", "Paste any INCI list — get ratings, pore-clog, fungal-acne & pregnancy flags."),
    ("layering-checker.html", "🧩", "Layering Checker", "Can you use retinol with vitamin C? Check any combination of actives."),
    ("sunscreen-calculator.html", "☀️", "Sunscreen Calculator", "Exactly how much SPF you need, plus a reapply timer with alerts."),
    ("hydration-calculator.html", "💧", "Hydration Calculator", "Your daily fluid target by weight, activity, climate and life stage."),
]

def tool_cards(base="{base}"):
    return "".join(f'<a class="card reveal" href="{base}tools/{h}"><div class="card-ico">{ic}</div><h3>{t}</h3><p>{d}</p><div class="card-meta"><span>Free</span><span>No sign-up to use</span></div></a>' for h, ic, t, d in TOOLS)

# ------------------------------------------------------------------ HOME
def home():
    feat = "".join(article_card(a) for a in ARTICLES[:6])
    body_map = "".join(f'<a href="{{base}}library.html#{k}"><span class="ico">{i}</span>{n.split(" ")[0].replace(",", "")}</a>' for k, n, i in CATEGORIES[:9])
    faq = [("Is Body.Care really free?", "Yes. Guides, tools and videos are free, funded by ads, affiliate partnerships, sponsors and reader support."),
           ("Is this medical advice?", "No. We publish educational, evidence-based information and link to primary sources. For diagnosis or treatment, see a qualified clinician — every guide includes a 'when to see a doctor' section."),
           ("How do you choose products?", "Ingredient-first criteria (formula, fragrance, price per ml, evidence). Affiliate links never change our ratings; see our editorial policy."),
           ("Can brands work with you?", "Yes — sponsorships, newsletter placements, giveaway partnerships and qualified-lead programs. See Advertise & Partner.")]
    faq_html = "".join(f'<details class="faq"><summary>{q}</summary><div>{a}</div></details>' for q, a in faq)
    faq_schema = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}
    org = {"@context": "https://schema.org", "@type": "Organization", "name": NAME, "url": SITE, "logo": SITE + "/assets/img/icon-512.png", "email": "hello@body.care"}
    care_q = [
        ("Sun protection", "How often do you wear sunscreen on exposed skin?", ["Rarely or never", "Only at the beach / on holiday", "Most sunny days", "Every day, reapplying outdoors"]),
        ("Cleansing", "How do you wash your face and body?", ["Hot water + regular bar soap", "Whatever's in the shower", "Gentle cleanser, sometimes hot water", "Gentle cleanser, lukewarm water"]),
        ("Moisturising", "When do you moisturise?", ["Almost never", "When skin feels tight", "Once a day", "Morning and night, on damp skin"]),
        ("Sleep", "How much sleep do you get on most nights?", ["Under 5 hours", "5–6 hours", "6–7 hours", "7+ hours"]),
        ("Hydration & diet", "Which sounds most like you?", ["Mostly sugary drinks, little water", "Some water, lots of processed food", "Mostly water, fairly balanced diet", "Water + plenty of fruit, veg and protein"]),
        ("Skin checks", "Do you check your skin and moles for changes?", ["Never", "Only if something hurts", "Occasionally", "Monthly self-check + yearly exam"]),
    ]
    steps = ""
    for area, q, opts in care_q:
        o = "".join(f'<label class="option"><input type="radio" name="cs-{area}" value="{i}"><span><b>{t}</b></span></label>' for i, t in enumerate(opts))
        steps += f'<div class="step" data-area="{area}"><span class="tag">{area}</span><h3 style="margin-top:.7rem">{q}</h3><div class="option-grid" data-required="cs-{area}">{o}</div></div>'
    body = f"""
<section class="hero">
 <div class="wrap hero-grid">
  <div>
   <span class="eyebrow">Skin · Hair · Body · Everyday wellbeing</span>
   <h1>Care for your whole body, <em>backed by science.</em></h1>
   <p class="lead">Clear, evidence-based guides, free personalised tools and expert videos — from sunscreen and skincare to hair, nails, oral care and sleep. No fluff, no fear-mongering.</p>
   <div class="hero-cta"><a class="btn btn-primary" href="{{base}}free-plan.html">Get my free personal plan →</a><a class="btn btn-ghost" href="{{base}}tools/skin-quiz.html">Take the 60-sec skin quiz</a></div>
   <div class="trust-row"><span>{I['check']} 100% free tools</span><span>{I['check']} Cited primary sources</span><span>{I['check']} "When to see a doctor" in every guide</span></div>
  </div>
  <div class="hero-card reveal">
   <p style="font-weight:600;margin-bottom:12px">Where do you want to start?</p>
   <div class="body-map">{body_map}<a href="{{base}}tools/index.html"><span class="ico">🧰</span>All tools</a></div>
   <form action="{{base}}search.html" style="margin-top:14px;display:flex;gap:8px" role="search"><label class="hp" for="hq">Search</label><input id="hq" type="search" name="q" placeholder="Search: retinol, dandruff, SPF…"><button class="btn btn-brand btn-sm" type="submit">Go</button></form>
  </div>
 </div>
</section>
<div class="wrap">{ad("header", "horizontal")}</div>

<section class="section" style="padding-top:20px">
 <div class="wrap">
  <div class="grid g4">
   <div class="stat"><b>{len(ARTICLES)}+</b><span>in-depth, cited guides</span></div>
   <div class="stat"><b>6</b><span>free interactive tools</span></div>
   <div class="stat"><b>80+</b><span>ingredients decoded</span></div>
   <div class="stat"><b>$0</b><span>forever free to use</span></div>
  </div>
 </div>
</section>

<section class="section alt">
 <div class="wrap">
  <div class="center"><span class="eyebrow">Free interactive tools</span><h2>Answers in seconds, not scrolling</h2><p class="lead">Personalised results instantly. No account needed.</p></div>
  <div class="grid g3" style="margin-top:32px">{tool_cards()}</div>
 </div>
</section>

<section class="section" id="score">
 <div class="wrap grid g2" style="align-items:start">
  <div>
   <span class="eyebrow">60-second self-check</span>
   <h2>What's your Body Care Score?</h2>
   <p class="lead">Six quick questions across sun, cleansing, moisture, sleep, nutrition and skin checks. Get a score out of 100 and your three biggest opportunities.</p>
   <ul class="checklist"><li>Instant score, no sign-up</li><li>Pinpoints your weakest habits</li><li>Optional free 30-day plan to fix them</li></ul>
  </div>
  <div>
   <div class="stepper" id="care-score">
    <div class="progress"><i></i></div><p class="small muted" data-count></p>
    {steps}
    <div class="step-nav"><button class="btn btn-ghost btn-sm" type="button" data-back>← Back</button><button class="btn btn-brand" type="button" data-next>Next →</button></div>
   </div>
   <div id="care-result" hidden></div>
   <div data-lead-after hidden>{plan_form("{base}", "care-score", "Get your free 30-day plan", "Built around the gaps in your score.")}</div>
  </div>
 </div>
</section>

<section class="section alt">
 <div class="wrap">
  <div style="display:flex;justify-content:space-between;align-items:end;flex-wrap:wrap;gap:12px"><div><span class="eyebrow">Most-read guides</span><h2 style="margin:0">Start with the fundamentals</h2></div><a class="btn btn-ghost btn-sm" href="{{base}}library.html">All guides →</a></div>
  <div class="grid g3" style="margin-top:28px">{feat}</div>
 </div>
</section>

<section class="section">
 <div class="wrap">
  <div class="lead-band">
   <div>
    <span class="eyebrow" style="color:var(--accent-2)">Free personalised plan</span>
    <h2>Stop guessing. Get a routine built for <em>your</em> body.</h2>
    <p>Tell us about your skin, hair and goals in 2 minutes. We'll email a step-by-step 30-day plan with budget-matched product options.</p>
    <ul class="checklist"><li>Face, body, hair & scalp — one plan</li><li>Budget, sensitive & pregnancy-safe options</li><li>Optional: get matched with a vetted local clinic</li></ul>
   </div>
   <form class="form on-dark" data-form="plan" data-success="Your plan is on its way — check your inbox!">
    <input type="text" name="_gotcha" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
    <input type="hidden" name="source" value="home-band">
    <div class="field"><label for="hb-n">First name</label><input id="hb-n" name="name" required autocomplete="given-name"></div>
    <div class="field"><label for="hb-e">Email</label><input id="hb-e" type="email" name="email" required autocomplete="email"></div>
    <div class="field"><label for="hb-c">Top concern</label><select id="hb-c" name="concern" required><option value="">Choose one…</option><option>Acne / breakouts</option><option>Dark spots / uneven tone</option><option>Dryness / eczema-prone</option><option>Ageing / fine lines</option><option>Hair thinning / scalp</option><option>Body odour / sweat</option><option>Just want a great routine</option></select></div>
    <label class="consent"><input type="checkbox" name="consent" required> Email me my plan and the weekly digest. <a href="{{base}}privacy.html" style="color:#fff">Privacy</a>.</label>
    <button class="btn btn-primary btn-block" type="submit">Build my free plan →</button>
    <p class="form-msg" role="status"></p>
   </form>
  </div>
 </div>
</section>

<section class="section alt">
 <div class="wrap">
  <div style="display:flex;justify-content:space-between;align-items:end;flex-wrap:wrap;gap:12px"><div><span class="eyebrow">Watch & learn</span><h2 style="margin:0">Dermatologist-led videos</h2></div><a class="btn btn-ghost btn-sm" href="{{base}}videos.html">Video library →</a></div>
  <div class="grid g3" style="margin-top:28px" data-videos data-limit="3"></div>
 </div>
</section>

<div class="wrap">{ad("multiplex", "autorelaxed")}</div>

<section class="section">
 <div class="wrap grid g2">
  <a class="card reveal" href="{{base}}contests.html" style="background:linear-gradient(135deg,color-mix(in srgb,var(--gold) 16%,var(--surface)),var(--surface))"><span class="tag gold">🏆 Monthly giveaway</span><h2 style="margin-top:.7rem">Win a curated body-care kit</h2><p>Free entry every month, bonus entries for referrals. Plus: nominate products for the Body.Care Awards.</p><span class="btn btn-brand btn-sm" style="margin-top:16px">Enter now →</span></a>
  <a class="card reveal" href="{{base}}support.html" style="background:linear-gradient(135deg,color-mix(in srgb,var(--accent) 12%,var(--surface)),var(--surface))"><span class="tag accent">❤️ Reader-supported</span><h2 style="margin-top:.7rem">Keep Body.Care free & independent</h2><p>Your support funds expert review, new tools, videos and community giveaways — without paywalls.</p><span class="btn btn-primary btn-sm" style="margin-top:16px">Support us →</span></a>
 </div>
</section>

<section class="section alt">
 <div class="wrap" style="max-width:820px">
  <div class="center"><span class="eyebrow">FAQ</span><h2>Good questions</h2></div>
  <div style="margin-top:24px">{faq_html}</div>
 </div>
</section>
"""
    return page("index.html", "Body.Care — Science-First Skin, Hair & Body Care Guides and Free Tools",
                "Evidence-based body care: skincare routines, sunscreen, hair, nails, oral care and sleep. Free skin quiz, routine builder, ingredient checker and a personalised plan.",
                body, "", [faq_schema, org], ["ingredients.js", "tools.js"])

# ------------------------------------------------------------------ LIBRARY
def library():
    btns = '<button class="filter-btn active" data-filter="all">All</button>' + "".join(f'<button class="filter-btn" data-filter="{k}">{i} {n}</button>' for k, n, i in CATEGORIES)
    cards = "".join(article_card(a) for a in ARTICLES)
    body = f"""
<section class="page-hero"><div class="wrap">{breadcrumb("{base}", [("", "Guides")])}
 <span class="eyebrow">The Body.Care Library</span><h1>Head-to-toe guides</h1>
 <p class="lead">Evidence-based, plain-English guides with cited sources and a "when to see a doctor" box in every article.</p></div></section>
<section class="section" style="padding-top:20px"><div class="wrap">
 <div class="toolbar"><input type="search" id="lib-filter" placeholder="Filter guides…" aria-label="Filter guides">{btns}</div>
 <div class="grid g3" data-library>{cards}</div>
 <p id="lib-empty" class="muted" hidden>No guides match yet — <a href="{{base}}contact.html">request a topic</a>.</p>
 {ad("footer")}
</div></section>"""
    sch = [crumb_schema([("library.html", "Guides")]),
           {"@context": "https://schema.org", "@type": "CollectionPage", "name": "Body.Care guides", "hasPart": [{"@type": "Article", "headline": a["title"], "url": f'{SITE}/articles/{a["slug"]}.html'} for a in ARTICLES]}]
    return page("library.html", "Body Care Guides: Skin, Hair, Sun, Nails, Oral & Sleep", "Browse evidence-based body care guides by category: face & skin, body, sun care, hair & scalp, hands & feet, oral care, men's care and sleep.", body, "library.html", sch)

# ------------------------------------------------------------------ ARTICLE
def article(a):
    import re
    heads = re.findall(r'<h2 id="(s\d)">(.*?)</h2>', a["body"])
    toc = "".join(f'<li><a href="#{i}">{t}</a></li>' for i, t in heads)
    body_html = a["body"]
    # inject an in-article ad after the 2nd h2 section
    parts = body_html.split('<h2 id="s3">')
    if len(parts) == 2:
        body_html = parts[0] + ad("inArticle", "fluid") + '<h2 id="s3">' + parts[1]
    faq_html = "".join(f'<details class="faq"><summary>{q}</summary><div>{ans}</div></details>' for q, ans in a["faq"])
    src = "".join(f'<li><a href="{u}" rel="noopener nofollow" target="_blank">{e(t)}</a></li>' for t, u in a["sources"])
    related = [r for r in ARTICLES if r["cat"] == a["cat"] and r["slug"] != a["slug"]] + [r for r in ARTICLES if r["cat"] != a["cat"]]
    rel = "".join(f'<li style="margin:.5rem 0"><a href="{r["slug"]}.html">{e(r["title"])}</a></li>' for r in related[:4])
    url = f'{SITE}/articles/{a["slug"]}.html'
    sch = [crumb_schema([("library.html", "Guides"), (f'library.html#{a["cat"]}', CATN[a["cat"]]), ("", a["title"])]),
           {"@context": "https://schema.org", "@type": "MedicalWebPage", "headline": a["title"], "description": a["desc"], "url": url,
            "about": {"@type": "Thing", "name": a["title"]}, "audience": {"@type": "PeopleAudience", "audienceType": "Patient"},
            "author": {"@type": "Organization", "name": "Body.Care Editorial Team", "url": SITE + "/about.html"},
            "publisher": {"@type": "Organization", "name": NAME, "logo": {"@type": "ImageObject", "url": SITE + "/assets/img/icon-512.png"}},
            "datePublished": "2026-09-19", "dateModified": "2026-09-19", "image": SITE + "/assets/img/og-image.png",
            "citation": [u for _, u in a["sources"]]},
           {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": ans}} for q, ans in a["faq"]]}]
    body = f"""
<div id="read-progress" style="position:fixed;top:0;left:0;height:3px;background:var(--accent);z-index:70;width:0"></div>
<section class="page-hero"><div class="wrap" style="max-width:1000px">
 {breadcrumb("{base}", [("library.html", "Guides"), (f'library.html#{a["cat"]}', CATN[a["cat"]])])}
 <span class="tag">{CATI[a["cat"]]} {CATN[a["cat"]]}</span>
 <h1 style="margin-top:.8rem">{e(a["title"])}</h1>
 <p class="lead">{e(a["desc"])}</p>
 <div class="byline"><span class="avatar">BC</span><span><b>Body.Care Editorial Team</b><br><a href="{{base}}about.html#editorial">Editorial & review policy</a></span><span>Updated Sep 19, 2026</span><span>{a["mins"]} min read</span><span>{len(a["sources"])} cited sources</span>
  <span class="share" style="margin-left:auto"><button class="btn btn-ghost btn-sm" data-share="native">Share</button><button class="btn btn-ghost btn-sm" data-share="pinterest">Pin</button><button class="btn btn-ghost btn-sm" data-share="whatsapp">WhatsApp</button></span></div>
</div></section>
<section class="section" style="padding-top:10px"><div class="wrap article-layout" style="max-width:1200px">
 <article class="prose">
  {body_html}
  <div class="callout doc"><strong>🩺 When to see a doctor</strong>{a["doctor"]}</div>
  <h2>FAQ</h2>{faq_html}
  <h2>Sources</h2><ol class="small">{src}</ol>
  <p class="small muted">This guide is educational and not a substitute for professional medical advice. Read our <a href="{{base}}disclaimer.html">medical disclaimer</a>.</p>
  {plan_form("{base}", "article-" + a["slug"], "Want this turned into your personal routine?", "Get a free 30-day plan that fits your skin, budget and schedule.")}
 </article>
 <aside>
  <div class="toc card"><b>On this page</b><ol>{toc}<li><a href="#main">Back to top</a></li></ol>
   <hr style="border:0;border-top:1px solid var(--line);margin:14px 0">
   <b>Related guides</b><ul style="padding-left:1rem;font-size:.92rem">{rel}</ul>
   <a class="btn btn-primary btn-sm btn-block" href="{{base}}tools/routine-builder.html" style="margin-top:12px">Build my routine</a>
  </div>
  {ad("sidebar", "vertical")}
 </aside>
</div></section>"""
    return page(f'articles/{a["slug"]}.html', a["title"], a["desc"], body, "library.html", sch, og_type="article")

# ------------------------------------------------------------------ VIDEOS
def videos():
    body = f"""
<section class="page-hero"><div class="wrap">{breadcrumb("{base}", [("", "Videos")])}
 <span class="eyebrow">Watch & learn</span><h1>Body care, explained on video</h1>
 <p class="lead">Short, practical videos from dermatologists and trusted educators. Subscribe to the Body.Care channel for weekly routines, myth-busting and product breakdowns.</p>
 <div class="hero-cta"><a class="btn btn-primary" data-yt-channel target="_blank" rel="noopener">▶ Subscribe on YouTube</a><a class="btn btn-ghost" href="{{base}}careers.html#creators">Become a Body.Care creator</a></div></div></section>
<section class="section" style="padding-top:20px"><div class="wrap">
 <div class="toolbar"><button class="filter-btn active" data-video-filter="All">All</button><button class="filter-btn" data-video-filter="Routines">Routines</button><button class="filter-btn" data-video-filter="Sun">Sun care</button></div>
 <div class="grid g3" data-videos></div>
 {ad("footer")}
 <div class="card" style="margin-top:28px"><h3>Suggest a video topic</h3><p>What should we film next? The most-requested topics get made first.</p>
  <form class="form" data-form="contact" data-success="Thanks — topic logged!" style="margin-top:14px"><input type="text" name="_gotcha" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true"><input type="hidden" name="type" value="video-topic">
   <div class="form-row two"><div class="field"><label for="vt">Topic</label><input id="vt" name="topic" required placeholder="e.g. body acne routine"></div><div class="field"><label for="ve">Email (optional)</label><input id="ve" type="email" name="email"></div></div>
   <button class="btn btn-brand" type="submit">Submit topic</button><p class="form-msg" role="status"></p></form></div>
</div></section>"""
    return page("videos.html", "Body Care Videos: Skincare Routines, Sunscreen & More", "Watch dermatologist-led body care videos on skincare routines, sunscreen application, sunburn treatment and more.", body, "videos.html", [crumb_schema([("", "Videos")])])

# ------------------------------------------------------------------ FREE PLAN (lead generation hub)
def free_plan():
    def opts(name, items, req=True, multi=False):
        t = "checkbox" if multi else "radio"
        dr = ' data-required="' + name + '"' if req and not multi else ""
        return f'<div class="option-grid"{dr}>' + "".join(
            f'<label class="option"><input type="{t}" name="{name}" value="{v}"><span><b>{v}</b>{f"<small>{s}</small>" if s else ""}</span></label>' for v, s in items) + "</div>"
    body = f"""
<section class="hero" style="padding-bottom:30px"><div class="wrap hero-grid">
 <div>
  <span class="eyebrow">Free · 2 minutes · no card needed</span>
  <h1>Your personalised <em>body care plan</em> — free.</h1>
  <p class="lead">Answer a few questions. Get a 30-day, step-by-step plan for face, body and hair — matched to your skin, concerns, budget and life stage. Want professional help? We'll also match you with a vetted local clinic.</p>
  <div class="trust-row"><span>{I['check']} Takes 2 minutes</span><span>{I['check']} Budget-matched options</span><span>{I['check']} Unsubscribe anytime</span></div>
 </div>
 <div class="grid" style="gap:12px">
  <div class="stat"><b>1 · Tell us</b><span>Skin type, concerns, routine and budget</span></div>
  <div class="stat"><b>2 · Get your plan</b><span>Emailed instantly: AM/PM routine, weekly steps, product options</span></div>
  <div class="stat"><b>3 · Optional expert match</b><span>Connect with a vetted dermatologist or clinic near you</span></div>
 </div>
</div></section>

<section class="section" style="padding-top:10px" id="plan"><div class="wrap" style="max-width:860px">
 <form class="stepper form" id="plan-wizard" data-form="plan" data-success="🎉 Your plan is on its way! Check your inbox in the next few minutes.">
  <input type="text" name="_gotcha" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true"><input type="hidden" name="source" value="plan-wizard"><input type="hidden" name="lead_score" value="">
  <div class="progress"><i></i></div><p class="small muted" data-count></p>
  <div class="step"><h2 style="font-size:1.6rem">What do you want to improve?</h2><p class="muted">Pick all that apply.</p>
   {opts("goals", [("Acne & breakouts", "face, back, chest"), ("Dark spots & tone", "PIH, melasma, sun spots"), ("Dryness & sensitivity", "eczema-prone, itchy"), ("Ageing & texture", "lines, firmness, pores"), ("Hair & scalp", "thinning, dandruff, breakage"), ("Body skin", "KP, rough skin, odour"), ("Sun protection habit", ""), ("Complete simple routine", "")], multi=True)}</div>
  <div class="step"><h2 style="font-size:1.6rem">Your skin type</h2><p class="muted">Not sure? <a href="{{base}}tools/skin-quiz.html" target="_blank">Take the 60-second quiz</a>.</p>
   {opts("skin_type", [("Oily", ""), ("Dry", ""), ("Combination", ""), ("Normal", ""), ("Sensitive", ""), ("Not sure", "")])}</div>
  <div class="step"><h2 style="font-size:1.6rem">A bit about you</h2>
   <div class="form-row two"><div class="field"><label for="pw-age">Age range</label><select id="pw-age" name="age" required><option value="">Select…</option><option>18–24</option><option>25–34</option><option>35–44</option><option>45–54</option><option>55–64</option><option>65+</option></select></div>
   <div class="field"><label for="pw-country">Country</label><input id="pw-country" name="country" required autocomplete="country-name" placeholder="e.g. Canada"></div></div>
   <div class="form-row two" style="margin-top:14px"><div class="field"><label for="pw-budget">Monthly budget for products</label><select id="pw-budget" name="budget" required><option value="">Select…</option><option>Under $25</option><option>$25–$60</option><option>$60–$150</option><option>$150+</option></select></div>
   <div class="field"><label for="pw-life">Life stage</label><select id="pw-life" name="life_stage"><option>None of these</option><option>Pregnant / trying / breastfeeding</option><option>Perimenopause / menopause</option><option>Teen skin (for my child)</option></select></div></div></div>
  <div class="step"><h2 style="font-size:1.6rem">Would professional help be useful?</h2><p class="muted">Many concerns (persistent acne, melasma, hair loss) respond faster with a clinician.</p>
   {opts("pro_interest", [("Yes — match me with a clinic", "Dermatologist, med-spa or trichologist near me"), ("Maybe later", "Send info, no contact yet"), ("No, DIY only", "Just the plan, thanks")])}
   <div class="form-row two" style="margin-top:14px"><div class="field"><label for="pw-city">City (for clinic matching)</label><input id="pw-city" name="city" autocomplete="address-level2"></div>
   <div class="field"><label for="pw-when">Timeline</label><select id="pw-when" name="timeline"><option>Just researching</option><option>Within 1 month</option><option>Within 3 months</option></select></div></div></div>
  <div class="step"><h2 style="font-size:1.6rem">Where should we send your plan?</h2>
   <div class="form-row two"><div class="field"><label for="pw-n">First name</label><input id="pw-n" name="name" required autocomplete="given-name"></div>
   <div class="field"><label for="pw-e">Email</label><input id="pw-e" type="email" name="email" required autocomplete="email"></div></div>
   <div class="field" style="margin-top:14px"><label for="pw-p">Mobile / WhatsApp (optional — for clinic matching)</label><input id="pw-p" type="tel" name="phone" autocomplete="tel"></div>
   <div class="stack" style="margin-top:14px">
    <label class="consent"><input type="checkbox" name="consent_email" required> Email me my plan and the weekly Body.Care digest. I accept the <a href="{{base}}privacy.html">privacy policy</a>.</label>
    <label class="consent"><input type="checkbox" name="consent_partner" value="yes"> Share my details with up to 3 vetted clinics/partners so they can contact me about my request. (Optional.)</label>
   </div>
   <p class="form-msg" role="status"></p></div>
  <div class="step-nav"><button class="btn btn-ghost btn-sm" type="button" data-back>← Back</button><button class="btn btn-primary" type="button" data-next>Next →</button></div>
 </form>
</div></section>

<section class="section alt"><div class="wrap grid g3">
 <div class="card"><div class="card-ico">🔒</div><h3>Privacy-first</h3><p>We never sell your email. Clinic matching happens only if you tick the box.</p></div>
 <div class="card"><div class="card-ico">🧾</div><h3>Evidence-based</h3><p>Plans follow published dermatology guidance and cite sources.</p></div>
 <div class="card"><div class="card-ico">💸</div><h3>Budget-honest</h3><p>Every step has a budget option. Expensive rarely means better.</p></div>
</div></section>

<section class="section" id="clinics"><div class="wrap grid g2" style="align-items:center">
 <div><span class="eyebrow">For clinics, brands & practitioners</span><h2>Receive qualified, consented patient enquiries</h2><p class="lead">Dermatology clinics, med-spas, hair-restoration and body-contouring providers: get exclusive, intent-verified leads in your city — with concern, budget and timeline pre-qualified.</p><a class="btn btn-brand" href="{{base}}advertise.html#leads">Become a partner clinic →</a></div>
 <div class="card"><h3>What partners receive</h3><ul class="checklist"><li>Opt-in enquiries with explicit consent</li><li>Concern, budget, timeline & city</li><li>Exclusive or shared (max 3) delivery</li><li>Pay-per-lead or monthly territory plans</li></ul></div>
</div></section>
"""
    wizard_js = """<script>
document.addEventListener("DOMContentLoaded",function(){
 var f=document.getElementById("plan-wizard"),steps=[].slice.call(f.querySelectorAll(".step")),i=0,bar=f.querySelector(".progress i"),back=f.querySelector("[data-back]"),next=f.querySelector("[data-next]"),cnt=f.querySelector("[data-count]");
 function show(){steps.forEach(function(s,j){s.classList.toggle("active",j===i)});bar.style.width=((i+1)/steps.length*100)+"%";back.style.visibility=i?"visible":"hidden";next.textContent=i===steps.length-1?"Send my free plan →":"Next →";next.type=i===steps.length-1?"submit":"button";cnt.textContent="Step "+(i+1)+" of "+steps.length}
 function ok(){var s=steps[i],r=s.querySelector("[data-required]");if(r&&!s.querySelector('input[name="'+r.getAttribute("data-required")+'"]:checked')){BC.toast("Pick an option to continue");return false}
  if(i===0&&!s.querySelector("input:checked")){BC.toast("Pick at least one goal");return false}
  var bad=[].slice.call(s.querySelectorAll("input,select")).filter(function(x){return !x.checkValidity()});if(bad.length){bad[0].reportValidity();return false}return true}
 next.addEventListener("click",function(e){if(i<steps.length-1){e.preventDefault();if(!ok())return;i++;show();BC.track&&BC.track("plan_step",{step:i+1});f.scrollIntoView({behavior:"smooth",block:"start"})}});
 back.addEventListener("click",function(){if(i){i--;show()}});
 f._enrich=function(d){var s=0;if(/clinic/i.test(d.pro_interest||""))s+=40;if(d.phone)s+=15;if(/1 month/.test(d.timeline||""))s+=20;else if(/3 months/.test(d.timeline||""))s+=10;if(/\\$60|\\$150/.test(d.budget||""))s+=15;if(d.consent_partner)s+=10;d.lead_score=s;d.lead_tier=s>=60?"HOT":s>=30?"WARM":"NURTURE"};
 f.addEventListener("bc:success",function(){i=0;show()});
 show();
});
</script>"""
    return page("free-plan.html", "Free Personalised Body Care Plan + Clinic Matching", "Get a free 30-day personalised skin, hair and body care plan in 2 minutes — with optional matching to a vetted local dermatologist or clinic.", body + wizard_js, "free-plan.html", [crumb_schema([("", "Free plan")])], body_attr="data-no-popup")

# ------------------------------------------------------------------ PICKS (affiliate)
PICKS = [
    ("Cleansers", [("Gentle hydrating cleanser (fragrance-free)", "Dry, sensitive, eczema-prone", "ceramide hydrating facial cleanser fragrance free"),
                   ("Foaming gel cleanser", "Oily, acne-prone", "foaming gel cleanser niacinamide oily skin"),
                   ("Cleansing balm", "Removing SPF & makeup", "cleansing balm fragrance free")]),
    ("Moisturisers", [("Ceramide barrier cream (tub)", "Face & body, very dry skin", "ceramide moisturizing cream tub"),
                      ("Oil-free gel moisturiser", "Oily & combination", "oil free gel moisturizer hyaluronic"),
                      ("Urea 10% body lotion", "Rough skin, KP, heels", "urea 10 percent body lotion")]),
    ("Sunscreen", [("Mineral SPF 50 (tinted)", "Sensitive skin, melasma, deeper tones", "tinted mineral sunscreen spf 50 iron oxides"),
                   ("Lightweight fluid SPF 50", "Daily wear under makeup", "lightweight sunscreen fluid spf 50 broad spectrum"),
                   ("Water-resistant body SPF 50", "Sports, beach, swimming", "water resistant sport sunscreen spf 50 body")]),
    ("Treatments", [("Adapalene 0.1% gel", "Acne (OTC retinoid)", "adapalene gel 0.1"),
                    ("Retinol 0.25–0.5% serum", "Texture & early lines", "retinol serum 0.5 beginners"),
                    ("Azelaic acid 10%", "Redness, acne, dark marks", "azelaic acid 10 suspension"),
                    ("Benzoyl peroxide 4–10% wash", "Back & chest acne", "benzoyl peroxide acne body wash")]),
    ("Hair & body", [("Ketoconazole / zinc anti-dandruff shampoo", "Dandruff, seb derm, fungal acne wash", "ketoconazole anti dandruff shampoo"),
                     ("Clinical-strength antiperspirant", "Heavy sweating", "clinical strength antiperspirant"),
                     ("Silk pillowcase", "Hair breakage & skin friction", "mulberry silk pillowcase")]),
]
def picks():
    blocks = ""
    for cat, items in PICKS:
        cards = "".join(f'<div class="card"><span class="tag">{cat}</span><h3 style="margin-top:.6rem">{e(t)}</h3><p>Best for: {e(b)}</p><div class="hero-cta" style="margin:14px 0 0"><a class="btn btn-brand btn-sm" data-aff="{e(t)}" rel="sponsored noopener" target="_blank" href="https://www.amazon.com/s?k={q.replace(" ", "+")}">See options on Amazon</a><a class="btn btn-ghost btn-sm" href="{{base}}tools/ingredient-checker.html">Check ingredients</a></div></div>' for t, b, q in items)
        blocks += f'<h2 style="margin-top:36px">{cat}</h2><div class="grid g3">{cards}</div>'
    body = f"""
<section class="page-hero"><div class="wrap">{breadcrumb("{base}", [("", "Picks")])}
 <span class="eyebrow">Ingredient-first recommendations</span><h1>Body.Care Picks</h1>
 <p class="lead">What to look for in each category — chosen by formula, fragrance-free options, evidence and price per ml. Not by who pays us.</p>
 <div class="callout small"><strong>Affiliate disclosure</strong>Some links earn us a small commission at no cost to you. This never changes our criteria. <a href="{{base}}disclaimer.html#affiliate">Details</a>.</div></div></section>
<section class="section" style="padding-top:0"><div class="wrap">{blocks}{ad("footer")}
 <div class="card" style="margin-top:28px"><h3>Are you a brand?</h3><p>Submit products for independent review or the Body.Care Awards. Review decisions are editorial and never guaranteed.</p><a class="btn btn-brand btn-sm" style="margin-top:12px" href="{{base}}advertise.html#brands">Brand submissions →</a></div>
</div></section>"""
    return page("picks.html", "Body Care Picks: What to Buy (Ingredient-First)", "Ingredient-first body care picks: cleansers, moisturisers, sunscreen, acne and retinoid treatments, anti-dandruff and antiperspirants.", body, "picks.html", [crumb_schema([("", "Picks")])])

# ------------------------------------------------------------------ SEARCH
def search():
    body = f"""
<section class="page-hero"><div class="wrap" style="max-width:900px">{breadcrumb("{base}", [("", "Search")])}
 <h1>Search Body.Care</h1>
 <input type="search" id="site-search" placeholder="Try: sunscreen, retinol, dandruff, dry skin…" aria-label="Search the site" autofocus style="font-size:1.1rem;padding:1rem 1.2rem">
</div></section>
<section class="section" style="padding-top:10px"><div class="wrap" style="max-width:900px"><div class="grid" id="search-results" aria-live="polite"></div></div></section>"""
    return page("search.html", "Search", "Search Body.Care guides and tools.", body, "", [])
