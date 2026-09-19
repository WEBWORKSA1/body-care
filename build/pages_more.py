# -*- coding: utf-8 -*-
from layout import page, ad, breadcrumb, crumb_schema, plan_form, e, SITE, NAME, I
from pages_main import TOOLS, tool_cards

def tool_page(fname, title, h1, desc, lead, inner, schema_name):
    body = f"""
<section class="page-hero"><div class="wrap" style="max-width:960px">{breadcrumb("{base}", [("tools/index.html", "Tools"), ("", h1)])}
 <span class="eyebrow">Free tool</span><h1>{h1}</h1><p class="lead">{lead}</p></div></section>
<section class="section" style="padding-top:10px"><div class="wrap" style="max-width:960px">
 {inner}
 {ad("inArticle")}
 <div data-lead-after hidden>{plan_form("{base}", fname.replace(".html", ""))}</div>
 <h2 style="margin-top:40px">More free tools</h2><div class="grid g3">{"".join(c for c in [tool_cards()] )}</div>
</div></section>"""
    body = body.replace(f'href="{{base}}tools/{fname}"', 'href="#main"')
    sch = [crumb_schema([("tools/index.html", "Tools"), ("", h1)]),
           {"@context": "https://schema.org", "@type": "WebApplication", "name": schema_name, "applicationCategory": "HealthApplication", "operatingSystem": "Any",
            "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}, "url": f"{SITE}/tools/{fname}"}]
    return page(f"tools/{fname}", title, desc, body, "tools/index.html", sch, ["ingredients.js", "tools.js"])

def step_q(name, q, options, hint=""):
    o = "".join(f'<label class="option"><input type="radio" name="{name}" value="{v}" data-s="{s}"><span><b>{v}</b></span></label>' for v, s in options)
    return f'<div class="step"><h2 style="font-size:1.5rem">{q}</h2>{f"<p class=muted>{hint}</p>" if hint else ""}<div class="option-grid" data-required="{name}">{o}</div></div>'

def nav_btns():
    return '<div class="step-nav"><button class="btn btn-ghost btn-sm" type="button" data-back>← Back</button><button class="btn btn-brand" type="button" data-next>Next →</button></div>'

def tools_index():
    body = f"""
<section class="page-hero"><div class="wrap">{breadcrumb("{base}", [("", "Tools")])}
 <span class="eyebrow">Free · instant · private</span><h1>Body care tools</h1>
 <p class="lead">Personalised answers in under a minute. Everything runs in your browser — nothing is stored unless you choose to email yourself the result.</p></div></section>
<section class="section" style="padding-top:10px"><div class="wrap"><div class="grid g3">{tool_cards()}</div>{ad("footer")}</div></section>"""
    return page("tools/index.html", "Free Body Care Tools: Skin Quiz, Routine Builder, Ingredient Checker", "Free interactive body care tools: skin type quiz, routine builder, ingredient checker, layering checker, sunscreen and hydration calculators.", body, "tools/index.html", [crumb_schema([("", "Tools")])])

def skin_quiz():
    qs = [
        step_q("q1", "About an hour after washing (no products), your face feels…", [("Tight, maybe flaky", "dry"), ("Shiny all over", "oily"), ("Shiny T-zone, normal/dry cheeks", "combo"), ("Comfortable", "normal")]),
        step_q("q2", "By midday your skin is…", [("Oily / shiny all over", "oily"), ("Oily only on nose & forehead", "combo"), ("Rough or dull", "dry"), ("About the same as morning", "normal")]),
        step_q("q3", "Your pores look…", [("Large and visible across the face", "oily"), ("Larger on nose, small elsewhere", "combo"), ("Small / barely visible", "dry"), ("Small to medium, even", "normal")]),
        step_q("q4", "How often do you get breakouts?", [("Often", "oily"), ("Sometimes, mostly T-zone", "combo"), ("Rarely", "normal"), ("Almost never, but I get dry patches", "dry")]),
        step_q("q5", "New products usually make your skin…", [("Sting, burn or go red", "sensitive"), ("Itchy or bumpy sometimes", "sensitive"), ("Break out occasionally", "oily"), ("Nothing much happens", "normal")]),
        step_q("q6", "In the sun or wind your skin…", [("Flushes or stings easily", "sensitive"), ("Gets tight and chapped", "dry"), ("Gets oilier", "oily"), ("Is fine", "normal")]),
        step_q("q7", "Do you have visible redness, flushing or broken capillaries?", [("Yes, often", "sensitive"), ("Sometimes", "sensitive,combo"), ("Rarely", "normal"), ("No", "normal")]),
    ]
    inner = f"""<div class="stepper" id="skin-quiz"><div class="progress"><i></i></div><p class="small muted" data-count></p>{"".join(qs)}{nav_btns()}</div><div id="skin-result" hidden></div>"""
    return tool_page("skin-quiz.html", "Skin Type Quiz: What's My Skin Type? (60 Seconds)", "Skin Type Quiz", "Free 7-question skin type quiz: find out if you're oily, dry, combination or normal — plus a sensitivity check and starter routine.",
                     "Seven quick questions. Find out if you're oily, dry, combination or normal — and whether your skin is sensitive.", inner, "Body.Care Skin Type Quiz")

def routine_builder():
    def o(name, items, multi=False):
        t = "checkbox" if multi else "radio"
        dr = "" if multi else f' data-required="{name}"'
        return f'<div class="option-grid"{dr}>' + "".join(f'<label class="option"><input type="{t}" name="{name}" value="{v}"><span><b>{l}</b></span></label>' for v, l in items) + "</div>"
    inner = f"""<div class="stepper" id="routine-builder"><div class="progress"><i></i></div><p class="small muted" data-count></p>
 <div class="step"><h2 style="font-size:1.5rem">Your skin type</h2><p class="muted">Don't know? <a href="skin-quiz.html">Take the quiz</a> — your result carries over.</p>{o("type", [("oily", "Oily"), ("dry", "Dry"), ("combo", "Combination"), ("normal", "Normal")])}</div>
 <div class="step"><h2 style="font-size:1.5rem">Main concerns</h2><p class="muted">Choose up to three.</p>{o("concern", [("acne", "Acne / clogged pores"), ("pigment", "Dark spots / uneven tone"), ("aging", "Fine lines / firmness"), ("texture", "Rough texture"), ("redness", "Redness / rosacea-prone"), ("dryness", "Dehydration"), ("body", "Body acne / rough body skin")], True)}</div>
 <div class="step"><h2 style="font-size:1.5rem">Is your skin sensitive?</h2>{o("sensitive", [("yes", "Yes — reacts easily"), ("no", "No")])}</div>
 <div class="step"><h2 style="font-size:1.5rem">Pregnant, trying or breastfeeding?</h2>{o("pregnant", [("yes", "Yes"), ("no", "No")])}</div>
 <div class="step"><h2 style="font-size:1.5rem">How involved should it be?</h2>{o("level", [("simple", "Minimal (3–4 steps)"), ("balanced", "Balanced (5–6 steps)"), ("advanced", "Advanced (I love skincare)")])}</div>
 <div class="step"><h2 style="font-size:1.5rem">Budget</h2>{o("budget", [("low", "Budget"), ("mid", "Mid-range"), ("high", "Premium")])}</div>
 {nav_btns()}</div><div id="routine-result" hidden></div>"""
    return tool_page("routine-builder.html", "Skincare Routine Builder: Free AM/PM Routine Generator", "Routine Builder", "Build a free personalised morning and night skincare routine for your skin type, concerns, sensitivity, pregnancy status and budget.",
                     "Six questions → a personalised morning, night and weekly routine with pregnancy-safe and sensitive-skin logic built in.", inner, "Body.Care Routine Builder")

def ingredient_checker():
    inner = """<form id="inci-form" class="card form">
 <div class="field"><label for="inci-text">Paste the ingredient list (INCI)</label><textarea id="inci-text" placeholder="Aqua, Glycerin, Niacinamide, Cetearyl Alcohol, …" required></textarea></div>
 <div><label>Flag ingredients for my profile</label><div class="chips">
  <label class="chip"><input type="checkbox" name="profile" value="acne" checked><span>Acne-prone</span></label>
  <label class="chip"><input type="checkbox" name="profile" value="sensitive" checked><span>Sensitive</span></label>
  <label class="chip"><input type="checkbox" name="profile" value="fungal"><span>Fungal acne</span></label>
  <label class="chip"><input type="checkbox" name="profile" value="pregnant"><span>Pregnant / breastfeeding</span></label></div></div>
 <div style="display:flex;gap:10px;flex-wrap:wrap"><button class="btn btn-brand" type="submit">Analyse ingredients</button><button class="btn btn-ghost" type="button" data-sample>Try a sample</button></div>
</form><div id="inci-result" hidden style="margin-top:24px"></div>"""
    return tool_page("ingredient-checker.html", "Ingredient Checker: Decode Any Skincare INCI List", "Ingredient Checker", "Paste any skincare or body care ingredient list to see what each ingredient does, plus pore-clogging, fungal-acne, irritant and pregnancy flags.",
                     "Paste an ingredient list from any product. We'll explain each ingredient and flag potential issues for your skin profile.", inner, "Body.Care Ingredient Checker")

def layering_checker():
    acts = [("retinoid", "Retinol / retinoid"), ("acid", "AHA / BHA (glycolic, lactic, salicylic)"), ("vitc", "Vitamin C"), ("bp", "Benzoyl peroxide"), ("vitaminb3", "Niacinamide")]
    chips = "".join(f'<label class="chip"><input type="checkbox" name="active" value="{v}"><span>{l}</span></label>' for v, l in acts)
    inner = f"""<form id="layer-form" class="card form"><label>Select the actives you want to use</label><div class="chips">{chips}</div><button class="btn btn-brand" type="submit" style="justify-self:start">Check compatibility</button></form><div id="layer-result" hidden style="margin-top:24px"></div>"""
    return tool_page("layering-checker.html", "Skincare Layering Checker: Can I Mix Retinol, Vitamin C, AHA?", "Layering Checker", "Check which skincare actives can be layered together: retinol, AHA/BHA, vitamin C, benzoyl peroxide and niacinamide — plus the correct layering order.",
                     "Which actives can share a routine, which to separate AM/PM, and the correct layering order.", inner, "Body.Care Layering Checker")

def hydration_calc():
    inner = """<form id="hydration-form" class="card form">
 <div class="form-row two"><div class="field"><label for="hy-weight">Body weight</label><input id="hy-weight" type="number" min="30" max="700" step="0.1" required></div>
 <div class="field"><label for="hy-unit">Unit</label><select id="hy-unit"><option value="kg">kg</option><option value="lb">lb</option></select></div></div>
 <div class="form-row two"><div class="field"><label for="hy-exercise">Exercise per day (minutes)</label><input id="hy-exercise" type="number" min="0" max="600" value="30"></div>
 <div class="field"><label for="hy-climate">Climate</label><select id="hy-climate"><option value="temperate">Temperate / cool</option><option value="hot">Hot & dry</option><option value="humid">Hot & humid</option></select></div></div>
 <div class="field"><label for="hy-state">Life stage</label><select id="hy-state"><option value="none">None of these</option><option value="pregnant">Pregnant</option><option value="breastfeeding">Breastfeeding</option></select></div>
 <button class="btn btn-brand" type="submit" style="justify-self:start">Calculate</button></form><div id="hy-result" hidden style="margin-top:24px"></div>"""
    return tool_page("hydration-calculator.html", "Water Intake Calculator: How Much Water Should I Drink?", "Hydration Calculator", "Calculate your daily water intake from body weight, exercise, climate and pregnancy or breastfeeding.",
                     "Your daily fluid target based on weight, exercise, climate and life stage.", inner, "Body.Care Hydration Calculator")

def sunscreen_calc():
    areas = [(3, "Face + neck (≈ ¼ tsp)", True), (1, "Ears", True), (4, "Both arms", True), (6, "Chest + stomach", False), (6, "Back", False), (8, "Both legs", False), (2, "Feet + tops of hands", False)]
    chips = "".join(f'<label class="chip"><input type="checkbox" name="area" value="{v}"{" checked" if c else ""}><span>{l}</span></label>' for v, l, c in areas)
    inner = f"""<form id="spf-form" class="card form"><label>Which areas are exposed?</label><div class="chips">{chips}</div>
 <div class="form-row two"><div class="field"><label for="uv">Today's UV index (check your weather app)</label><input id="uv" type="number" min="0" max="15" value="6"></div>
 <div class="field"><label for="spf-activity">Activity</label><select id="spf-activity"><option value="normal">Normal outdoor day</option><option value="sweat">Sport / heavy sweating</option><option value="water">Swimming</option></select></div></div>
 <button class="btn btn-brand" type="submit" style="justify-self:start">Calculate</button></form>
 <div id="spf-result" hidden style="margin-top:24px"></div>
 <div id="timer-box" class="card center" hidden style="margin-top:18px"><h3>Reapply timer</h3><div class="timer" id="timer-display">00:00</div><button class="btn btn-primary" id="timer-start" type="button" style="margin-top:12px">Start timer</button><p class="small muted" style="margin-top:8px">Allow notifications to get an alert.</p></div>"""
    return tool_page("sunscreen-calculator.html", "Sunscreen Calculator: How Much SPF Do I Need? + Reapply Timer", "Sunscreen Calculator", "Calculate how much sunscreen to apply for the areas you expose, the right SPF for today's UV index, and set a reapply timer.",
                     "How much sunscreen you actually need, what SPF suits today's UV index, and a reapply timer.", inner, "Body.Care Sunscreen Calculator")

# ------------------------------------------------------------------ SUPPORT / DONATE
def support():
    tiers = [(5, "Coffee"), (15, "Supporter"), (35, "Champion"), (100, "Patron")]
    tier_html = "".join(f'<label class="tier"><input type="radio" name="amt" value="{v}"{" checked" if v == 15 else ""}><span><b>${v}</b>{n}</span></label>' for v, n in tiers)
    alloc = [("Expert review", 35), ("New tools & site", 25), ("Video production", 20), ("Giveaways & prizes", 10), ("Marketing & outreach", 10)]
    bars = "".join(f'<div class="bar-row"><span>{n}</span><div class="meter"><i style="width:{p}%"></i></div><span>{p}%</span></div>' for n, p in alloc)
    body = f"""
<section class="hero" style="padding-bottom:30px"><div class="wrap hero-grid">
 <div><span class="eyebrow">Reader-supported</span><h1>Keep Body.Care <em>free for everyone.</em></h1>
  <p class="lead">No paywalls, no pay-to-rank reviews. Your support funds expert review, new tools, video production, community giveaways and hiring great creators.</p>
  <div class="stack" style="max-width:520px"><div class="meter" data-goal-meter><i></i></div><p class="small muted" data-goal-label>Monthly goal</p></div></div>
 <form id="donate-form" class="stepper" style="display:grid;gap:16px">
  <div class="seg" role="group" aria-label="Frequency"><button type="button" class="active" data-freq="once" aria-pressed="true">One-time</button><button type="button" data-freq="monthly" aria-pressed="false">Monthly ❤️</button></div>
  <div class="tiers">{tier_html}</div>
  <div class="field"><label for="custom-amount">Or enter an amount (USD)</label><input id="custom-amount" type="number" min="1" step="1" placeholder="Custom amount"></div>
  <p id="donate-summary" style="font-weight:600;margin:0"></p>
  <button class="btn btn-primary btn-block" type="submit">Continue to secure checkout →</button>
  <div class="chips" style="justify-content:center"><a class="btn btn-ghost btn-sm" data-donate-link="paypal" target="_blank" rel="noopener">PayPal</a><a class="btn btn-ghost btn-sm" data-donate-link="kofi" target="_blank" rel="noopener">Ko-fi</a><a class="btn btn-ghost btn-sm" data-donate-link="buymeacoffee" target="_blank" rel="noopener">Buy Me a Coffee</a><a class="btn btn-ghost btn-sm" data-donate-link="githubSponsors" target="_blank" rel="noopener">GitHub Sponsors</a><a class="btn btn-ghost btn-sm" data-donate-link="patreon" target="_blank" rel="noopener">Patreon</a></div>
  <p class="small muted center" style="margin:0">Payments are processed securely by the provider. Body.Care never sees your card details.</p>
 </form>
</div></section>
<section class="section alt"><div class="wrap grid g2" style="align-items:center">
 <div><span class="eyebrow">Where your money goes</span><h2>Transparent by default</h2><p class="lead">We publish a quarterly breakdown. Target allocation:</p>{bars}</div>
 <div class="grid" style="gap:14px">
  <div class="card"><h3>☕ Body.Care Circle (monthly)</h3><p>Supporters get the ad-light members' digest, early access to new tools, bonus giveaway entries and a name on the supporters wall (optional).</p></div>
  <div class="card"><h3>🏢 Sponsor a tool or guide</h3><p>Companies can underwrite a tool, translation or guide series with clear, non-editorial credit. <a href="{{base}}advertise.html">Learn more</a>.</p></div>
  <div class="card"><h3>🎁 Fund a prize</h3><p>Sponsor a monthly giveaway prize and reach an engaged audience. <a href="{{base}}contests.html#sponsor">Details</a>.</p></div>
 </div>
</div></section>
<section class="section"><div class="wrap" style="max-width:820px">
 <h2 class="center">Other ways to help (free)</h2>
 <div class="grid g3" style="margin-top:20px"><div class="card"><h3>Share</h3><p>Send a guide to someone who'd benefit.</p><button class="btn btn-ghost btn-sm" data-share="native" style="margin-top:10px">Share Body.Care</button></div><div class="card"><h3>Subscribe</h3><p>Subscribe on YouTube and turn on notifications.</p><a class="btn btn-ghost btn-sm" data-yt-channel target="_blank" rel="noopener" style="margin-top:10px">YouTube</a></div><div class="card"><h3>Contribute</h3><p>Write, film, translate or review with us.</p><a class="btn btn-ghost btn-sm" href="{{base}}careers.html" style="margin-top:10px">Join us</a></div></div>
 <details class="faq" style="margin-top:28px"><summary>Is my donation tax-deductible?</summary><div>Body.Care is an independent publisher, not a registered charity, so contributions are not tax-deductible. They go directly into operations.</div></details>
 <details class="faq"><summary>Can I cancel a monthly contribution?</summary><div>Yes, anytime, via the receipt email from your payment provider or by emailing us.</div></details>
</div></section>"""
    return page("support.html", "Support Body.Care — Donate & Become a Member", "Support Body.Care with a one-time or monthly contribution. Funds expert review, free tools, videos, giveaways and hiring creators.", body, "support.html", [crumb_schema([("", "Support")])])

# ------------------------------------------------------------------ CONTESTS & AWARDS
def contests():
    cats = ["Best Gentle Cleanser", "Best Face Moisturiser", "Best Body Lotion", "Best Face Sunscreen", "Best Body Sunscreen", "Best Retinoid", "Best Budget Buy", "Best Anti-Dandruff", "Best Deodorant / Antiperspirant", "Best Men's Grooming"]
    cat_opts = "".join(f"<option>{c}</option>" for c in cats)
    body = f"""
<section class="hero" style="padding-bottom:30px"><div class="wrap hero-grid">
 <div><span class="eyebrow">🏆 Giveaways & Awards</span><h1><span data-contest-title>Monthly Body Care Kit Giveaway</span></h1>
  <p class="lead">Prize: <b data-contest-prize>curated body-care kit</b>. Free to enter. Draw on <b data-contest-end>the 1st</b>. Get <b>+3 bonus entries</b> for every friend who enters with your link.</p>
  <div class="countdown" data-countdown aria-label="Time left"><div><b>00</b><small>days</small></div><div><b>00</b><small>hrs</small></div><div><b>00</b><small>min</small></div><div><b>00</b><small>sec</small></div></div></div>
 <form class="stepper form" data-form="contest" data-success="You're entered! Share your link below for bonus entries.">
  <input type="text" name="_gotcha" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true"><input type="hidden" name="type" value="giveaway-entry"><input type="hidden" name="referrer" value="">
  <h2 style="font-size:1.5rem">Enter the giveaway</h2>
  <div class="form-row two"><div class="field"><label for="ct-n">Full name</label><input id="ct-n" name="name" required autocomplete="name"></div><div class="field"><label for="ct-e">Email</label><input id="ct-e" type="email" name="email" required autocomplete="email"></div></div>
  <div class="form-row two"><div class="field"><label for="ct-c">Country</label><input id="ct-c" name="country" required autocomplete="country-name"></div><div class="field"><label for="ct-ig">Instagram / TikTok (optional)</label><input id="ct-ig" name="social_handle" placeholder="@handle"></div></div>
  <div class="field"><label for="ct-q">What's your #1 body care struggle? (helps us plan content)</label><input id="ct-q" name="struggle" required></div>
  <label class="consent"><input type="checkbox" name="age_ok" required> I'm 18+ (or the age of majority where I live) and accept the <a href="#rules">official rules</a>.</label>
  <label class="consent"><input type="checkbox" name="consent" required> Subscribe me to the Body.Care digest (required for entry; unsubscribe anytime).</label>
  <button class="btn btn-primary btn-block" type="submit">Enter now — it's free</button><p class="form-msg" role="status"></p>
  <div id="ref-box" hidden class="result-box"><b>Your bonus-entry link</b><p class="small muted">+3 entries for every friend who enters with it.</p><div style="display:flex;gap:8px"><input type="text" readonly aria-label="Referral link"><button class="btn btn-brand btn-sm" type="button" onclick="var i=this.previousElementSibling;i.select();navigator.clipboard&&navigator.clipboard.writeText(i.value);BC.toast('Copied!')">Copy</button></div></div>
 </form>
</div></section>

<section class="section alt" id="awards"><div class="wrap grid g2" style="align-items:start">
 <div><span class="eyebrow">Body.Care Awards</span><h2>Nominate & vote: Readers' Choice</h2><p class="lead">Every year readers nominate the products that truly work. Finalists are screened on formula, fragrance, evidence and value; readers vote for winners across 10 categories.</p>
  <ul class="pill-list">{"".join(f"<li>{c}</li>" for c in cats)}</ul>
  <p class="small muted">Brands can't buy awards. Winners may license the Body.Care Awards seal for packaging and marketing.</p></div>
 <form class="card form" data-form="contest" data-success="Nomination received — thank you!">
  <input type="text" name="_gotcha" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true"><input type="hidden" name="type" value="award-nomination">
  <h3>Nominate a product</h3>
  <div class="field"><label for="aw-cat">Category</label><select id="aw-cat" name="category" required><option value="">Choose…</option>{cat_opts}</select></div>
  <div class="form-row two"><div class="field"><label for="aw-b">Brand</label><input id="aw-b" name="brand" required></div><div class="field"><label for="aw-p">Product</label><input id="aw-p" name="product" required></div></div>
  <div class="field"><label for="aw-w">Why does it deserve to win?</label><textarea id="aw-w" name="why" required></textarea></div>
  <div class="field"><label for="aw-e">Your email (for voting reminders)</label><input id="aw-e" type="email" name="email" required></div>
  <button class="btn btn-brand" type="submit">Submit nomination</button><p class="form-msg" role="status"></p>
 </form>
</div></section>

<section class="section" id="sponsor"><div class="wrap grid g3">
 <div class="card"><div class="card-ico">🎁</div><h3>Sponsor a prize</h3><p>Brands supply the prize; we promote across site, newsletter and social. Transparent "Prize provided by" credit.</p></div>
 <div class="card"><div class="card-ico">📸</div><h3>Creator challenges</h3><p>30-day routine challenges and before/after (honest, unfiltered) stories with cash prizes for creators.</p></div>
 <div class="card"><div class="card-ico">🏫</div><h3>Community grants</h3><p>Quarterly micro-grants for community skin-health education projects, funded by supporters.</p><a class="btn btn-ghost btn-sm" href="{{base}}advertise.html" style="margin-top:12px">Partner with us →</a></div>
</div></section>

<section class="section alt" id="rules"><div class="wrap prose" style="max-width:820px">
 <h2>Official rules (summary)</h2>
 <ol><li><b>No purchase necessary.</b> A purchase does not improve your chances of winning.</li><li>Open to legal residents 18+ (or age of majority) where not prohibited by law. Void where prohibited. Quebec residents: see full rules for Régie des alcools, des courses et des jeux requirements where applicable.</li><li>Entry period: from the 1st to the last day of each calendar month (local time as displayed).</li><li>One base entry per person per month; +3 bonus entries per unique valid referral, capped at 30 bonus entries.</li><li>Winner drawn at random from eligible entries within 7 days of close and notified by email; 7 days to respond before an alternate is drawn. Canadian winners must correctly answer a skill-testing question.</li><li>Prize as described; no cash alternative except at sponsor's discretion. Odds depend on the number of eligible entries.</li><li>Personal data is used per our <a href="{{base}}privacy.html">privacy policy</a>. Not sponsored, endorsed or administered by Instagram, TikTok or YouTube.</li></ol>
 <p class="small muted">Operators should have full rules reviewed by counsel for each country in which entries are accepted.</p>
</div></section>"""
    return page("contests.html", "Giveaways & Body.Care Awards — Enter Free", "Enter the free monthly Body.Care giveaway, earn bonus entries by referral, and nominate products for the Body.Care Readers' Choice Awards.", body, "contests.html", [crumb_schema([("", "Giveaways & Awards")])])

# ------------------------------------------------------------------ CAREERS
def careers():
    roles = [("Freelance health & beauty writer", "Remote · per article", "Plain-English, source-cited guides. Science or journalism background preferred."),
             ("Medical reviewer (MD / FAAD / NP / PharmD)", "Remote · per review", "Review guides for accuracy; credited on every page you review."),
             ("Video creator / editor (YouTube & Shorts)", "Remote · per video", "Scripting, filming or editing educational body care videos."),
             ("SEO & growth marketer", "Remote · part-time", "Topic clusters, internal linking, Pinterest & newsletter growth."),
             ("Partnerships & clinic sales", "Remote · commission", "Sign clinics and brands to lead and sponsorship programs."),
             ("Community & giveaway manager", "Remote · part-time", "Run contests, awards voting and social community."),
             ("Translator (ES, FR, HI, PT, AR)", "Remote · per word", "Localise top guides and tools for new markets."),
             ("Campus / community ambassador", "Remote · rewards", "Share tools and earn prizes, swag and referral rewards.")]
    cards = "".join(f'<div class="card"><span class="tag">{w}</span><h3 style="margin-top:.6rem">{t}</h3><p>{d}</p></div>' for t, w, d in roles)
    role_opts = "".join(f"<option>{t}</option>" for t, _, _ in roles)
    body = f"""
<section class="page-hero"><div class="wrap">{breadcrumb("{base}", [("", "Careers")])}
 <span class="eyebrow">Work with us</span><h1>Careers, creators & contributors</h1><p class="lead">Help millions of people take better care of their bodies. Remote-first, flexible, output-focused.</p></div></section>
<section class="section" style="padding-top:10px"><div class="wrap"><div class="grid g3">{cards}</div></div></section>
<section class="section alt" id="creators"><div class="wrap grid g2" style="align-items:start">
 <div><span class="eyebrow">Apply</span><h2>Tell us what you'd bring</h2><p class="lead">We reply to every application within 10 working days.</p>
  <ul class="checklist"><li>Paid per piece or per month — rates shared on first call</li><li>Credit and bio on everything you create</li><li>Revenue-share options for top video creators</li></ul></div>
 <form class="card form" data-form="careers" data-success="Application received — we'll be in touch within 10 working days.">
  <input type="text" name="_gotcha" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
  <div class="form-row two"><div class="field"><label for="cr-n">Full name</label><input id="cr-n" name="name" required autocomplete="name"></div><div class="field"><label for="cr-e">Email</label><input id="cr-e" type="email" name="email" required autocomplete="email"></div></div>
  <div class="field"><label for="cr-r">Role</label><select id="cr-r" name="role" required><option value="">Choose…</option>{role_opts}<option>Something else</option></select></div>
  <div class="form-row two"><div class="field"><label for="cr-l">Portfolio / LinkedIn / channel URL</label><input id="cr-l" type="url" name="portfolio" required placeholder="https://"></div><div class="field"><label for="cr-c">Credentials (if any)</label><input id="cr-c" name="credentials" placeholder="e.g. MD, RN, BSc Chem"></div></div>
  <div class="field"><label for="cr-m">Why Body.Care? (2–3 sentences)</label><textarea id="cr-m" name="message" required></textarea></div>
  <label class="consent"><input type="checkbox" name="consent" required> I agree to Body.Care processing my application data.</label>
  <button class="btn btn-brand" type="submit">Send application</button><p class="form-msg" role="status"></p>
 </form>
</div></section>"""
    return page("careers.html", "Careers: Writers, Medical Reviewers, Video Creators", "Join Body.Care as a writer, medical reviewer, video creator, marketer, translator or ambassador. Remote-first roles.", body, "", [crumb_schema([("", "Careers")])])

# ------------------------------------------------------------------ ADVERTISE / PARTNER / LEAD BUYERS
def advertise():
    pk = [("Starter", "Newsletter feature", ["1 sponsored newsletter slot", "Clear 'Sponsored' label", "Click & open report"]),
          ("Growth", "Sponsored guide or tool", ["Underwrite a guide series or tool", "Logo + 'made possible by' credit", "90-day placement", "Editorial independence guaranteed"]),
          ("Performance", "Qualified leads", ["Pay-per-lead or territory plans", "Consented, pre-qualified enquiries", "Concern, budget, timeline, city", "Exclusive or max-3 shared"])]
    cards = "".join(f'<div class="card"><span class="tag accent">{n}</span><h3 style="margin-top:.6rem">{t}</h3><ul class="checklist" style="margin-top:12px">{"".join(f"<li>{x}</li>" for x in li)}</ul></div>' for n, t, li in pk)
    body = f"""
<section class="page-hero"><div class="wrap">{breadcrumb("{base}", [("", "Advertise & Partner")])}
 <span class="eyebrow">Media kit</span><h1>Advertise & partner with Body.Care</h1><p class="lead">Reach people actively researching skin, hair and body care — at the exact moment they're choosing a routine, product or clinic.</p>
 <div class="hero-cta"><a class="btn btn-primary" href="#partner-form">Request media kit & rates</a><a class="btn btn-ghost" href="#leads">Clinic lead program</a></div></div></section>
<section class="section" style="padding-top:10px"><div class="wrap"><div class="grid g3">{cards}</div></div></section>
<section class="section alt" id="leads"><div class="wrap grid g2" style="align-items:center">
 <div><span class="eyebrow">For clinics & practitioners</span><h2>Patient enquiry program</h2><p class="lead">Our free plan wizard captures intent: concern, budget, timeline and city — and explicit consent to be contacted. You get ready-to-book enquiries, not cold clicks.</p>
  <ul class="checklist"><li>Dermatology · med-spa · laser · hair restoration · body contouring · dental aesthetics</li><li>Lead scoring (HOT / WARM / NURTURE)</li><li>Delivered by email, webhook or CRM</li><li>Replacement credit for invalid leads</li></ul></div>
 <div class="card" id="brands"><h3>For brands</h3><ul class="checklist"><li>Independent product review submissions (no paid outcomes)</li><li>Giveaway prize sponsorship</li><li>Awards seal licensing (winners only)</li><li>Affiliate & creator campaigns</li></ul><p class="small muted">All sponsored content is labelled. Advertisers never influence ratings or medical content.</p></div>
</div></section>
<section class="section" id="partner-form"><div class="wrap" style="max-width:820px">
 <form class="stepper form" data-form="partner" data-success="Thanks! Our partnerships team will reply within 2 business days.">
  <input type="text" name="_gotcha" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
  <h2 style="font-size:1.6rem">Partner enquiry</h2>
  <div class="form-row two"><div class="field"><label for="ad-n">Name</label><input id="ad-n" name="name" required autocomplete="name"></div><div class="field"><label for="ad-e">Work email</label><input id="ad-e" type="email" name="email" required autocomplete="email"></div></div>
  <div class="form-row two"><div class="field"><label for="ad-c">Company / clinic</label><input id="ad-c" name="company" required autocomplete="organization"></div><div class="field"><label for="ad-w">Website</label><input id="ad-w" type="url" name="website" placeholder="https://"></div></div>
  <div class="form-row two"><div class="field"><label for="ad-t">I'm interested in</label><select id="ad-t" name="interest" required><option value="">Choose…</option><option>Clinic lead program</option><option>Newsletter sponsorship</option><option>Sponsored guide / tool</option><option>Giveaway prize sponsorship</option><option>Product review submission</option><option>Awards seal licensing</option><option>Affiliate partnership</option></select></div>
  <div class="field"><label for="ad-b">Monthly budget</label><select id="ad-b" name="budget"><option>Under $500</option><option>$500–$2,000</option><option>$2,000–$10,000</option><option>$10,000+</option></select></div></div>
  <div class="field"><label for="ad-g">Markets / cities</label><input id="ad-g" name="markets" placeholder="e.g. Toronto, Montréal, Mumbai"></div>
  <div class="field"><label for="ad-m">Goals</label><textarea id="ad-m" name="message"></textarea></div>
  <button class="btn btn-primary" type="submit">Send enquiry</button><p class="form-msg" role="status"></p>
 </form>
</div></section>"""
    return page("advertise.html", "Advertise, Sponsor & Clinic Lead Program", "Advertise with Body.Care: newsletter sponsorships, sponsored tools, giveaway prizes and a consented patient-enquiry lead program for clinics.", body, "", [crumb_schema([("", "Advertise & Partner")])])

# ------------------------------------------------------------------ ABOUT
def about():
    body = f"""
<section class="page-hero"><div class="wrap" style="max-width:900px">{breadcrumb("{base}", [("", "About")])}
 <span class="eyebrow">About Body.Care</span><h1>Clear, honest care for the body you live in.</h1>
 <p class="lead">Body.Care is an independent publisher of evidence-based guides, free tools and videos covering skin, hair, body, oral care and everyday wellbeing.</p></div></section>
<section class="section" style="padding-top:10px"><div class="wrap prose">
 <h2 id="mission">Our mission</h2><p>Make trustworthy body care information free, fast and practical — for every skin tone, gender, age and budget. We cut through marketing claims and fear-based "toxin" content with plain-English science.</p>
 <h2 id="editorial">Editorial policy</h2>
 <ul><li><b>Evidence first.</b> We prioritise dermatology society guidance, systematic reviews and government health sources, and link them in every guide.</li><li><b>Safety boxes.</b> Every guide includes a "when to see a doctor" section.</li><li><b>Review.</b> Content is written by the editorial team and is being progressively reviewed by credentialed clinicians; reviewer names and credentials appear on reviewed pages. <a href="careers.html">Clinicians can apply here</a>.</li><li><b>Updates.</b> Guides show the last-updated date and are re-checked at least yearly.</li><li><b>Corrections.</b> Spotted an error? <a href="contact.html">Tell us</a> — we correct and note substantive changes.</li></ul>
 <h2 id="money">How we make money</h2><p>Display advertising (Google AdSense), clearly labelled sponsorships, affiliate links, a consent-based clinic enquiry program and reader contributions. Advertisers and affiliates never influence ratings or health content. Sponsored content is always labelled.</p>
 <h2 id="inclusive">Inclusive by design</h2><p>We cover melanin-rich skin, men's care, teen and midlife skin, and budget options in every category — because good care shouldn't depend on who you are or what you earn.</p>
 <div class="hero-cta"><a class="btn btn-primary" href="free-plan.html">Get your free plan</a><a class="btn btn-ghost" href="contact.html">Contact us</a></div>
</div></section>"""
    return page("about.html", "About Body.Care & Editorial Policy", "About Body.Care: our mission, editorial and review policy, how we make money and our commitment to inclusive, evidence-based body care.", body, "", [crumb_schema([("", "About")])])

def contact():
    body = f"""
<section class="page-hero"><div class="wrap">{breadcrumb("{base}", [("", "Contact")])}
 <h1>Contact us</h1><p class="lead">Questions, corrections, topic requests or partnerships — we read everything.</p></div></section>
<section class="section" style="padding-top:10px"><div class="wrap grid g2" style="align-items:start">
 <form class="card form" data-form="contact" data-success="Message sent — we usually reply within 2 business days.">
  <input type="text" name="_gotcha" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
  <div class="form-row two"><div class="field"><label for="co-n">Name</label><input id="co-n" name="name" required autocomplete="name"></div><div class="field"><label for="co-e">Email</label><input id="co-e" type="email" name="email" required autocomplete="email"></div></div>
  <div class="field"><label for="co-t">Topic</label><select id="co-t" name="topic"><option>General question</option><option>Correction</option><option>Topic request</option><option>Partnership / advertising</option><option>Press</option><option>Privacy request</option></select></div>
  <div class="field"><label for="co-m">Message</label><textarea id="co-m" name="message" required></textarea></div>
  <p class="small muted">We can't give personal medical advice by email. For urgent symptoms, contact a doctor or emergency services.</p>
  <button class="btn btn-brand" type="submit">Send message</button><p class="form-msg" role="status"></p>
 </form>
 <div class="grid" style="gap:14px"><div class="card"><h3>Email</h3><p><a href="mailto:hello@body.care">hello@body.care</a></p></div><div class="card"><h3>Partnerships</h3><p><a href="advertise.html">Advertise & partner →</a></p></div><div class="card"><h3>Join the team</h3><p><a href="careers.html">Open roles →</a></p></div></div>
</div></section>"""
    return page("contact.html", "Contact Body.Care", "Contact Body.Care for questions, corrections, topic requests, press and partnerships.", body, "", [crumb_schema([("", "Contact")])])

def legal(fname, title, desc, content):
    body = f'<section class="page-hero"><div class="wrap prose">{breadcrumb("{base}", [("", title)])}<h1>{title}</h1><p class="muted">Last updated: September 19, 2026</p></div></section><section class="section" style="padding-top:0"><div class="wrap prose">{content}<p class="small muted">This template should be reviewed by qualified counsel for your jurisdictions before launch.</p></div></section>'
    return page(fname, title, desc, body, "", [], popup=False)

PRIVACY = """<h2>What we collect</h2><ul><li><b>You give us:</b> name, email, and optional details you enter in forms (plan wizard answers, phone, city, contest entries, applications).</li><li><b>Automatically:</b> with your consent, analytics cookies (Google Analytics) and advertising cookies (Google AdSense) that may collect device and usage data.</li><li><b>Tools:</b> quiz and calculator answers are processed in your browser and are not sent to us unless you submit a form. Some preferences (theme, quiz result) are kept in your browser's local storage.</li></ul>
<h2>How we use it</h2><ul><li>To send the plan, results or newsletter you requested.</li><li>To run giveaways and contact winners.</li><li>To share your enquiry with up to 3 partner clinics <b>only if you tick the partner-consent box</b>.</li><li>To measure and improve the site and show ads.</li></ul>
<h2>Advertising</h2><p>Third-party vendors, including Google, use cookies to serve ads based on prior visits to this and other websites. Google's use of advertising cookies enables it and its partners to serve ads based on visits to this site and/or other sites. You can opt out of personalised advertising at <a href="https://adssettings.google.com" rel="noopener">Google Ads Settings</a> or <a href="https://www.aboutads.info" rel="noopener">aboutads.info</a>. Choosing "Essential only" in our banner requests non-personalised ads. For EEA/UK/Swiss visitors, a Google-certified consent management platform should be enabled in AdSense.</p>
<h2>Your rights</h2><p>You may access, correct, delete or export your data, and withdraw consent at any time (GDPR, UK GDPR, CCPA/CPRA, Canada PIPEDA / Quebec Law 25, India DPDP Act). Email <a href="mailto:hello@body.care">hello@body.care</a>. Every email includes an unsubscribe link.</p>
<h2>Health information</h2><p>Plan wizard answers may describe skin or health concerns. We use them only to create your plan and, with separate consent, to route your enquiry. We don't sell personal data.</p>
<h2>Retention & security</h2><p>We keep form data only as long as needed for the purpose, then delete it. Data is transmitted over HTTPS to our form and email providers.</p>
<h2>Children</h2><p>Body.Care is not directed to children under 16, and giveaways are 18+.</p>"""

TERMS = """<h2>Use of the site</h2><p>Content is for personal, non-commercial educational use. Don't scrape, republish or frame our content without permission.</p><h2>No medical advice</h2><p>See our <a href="disclaimer.html">medical disclaimer</a>. Using Body.Care does not create a doctor–patient relationship.</p><h2>Third-party links & partners</h2><p>We aren't responsible for third-party sites, products or clinics. Partner clinics are independent businesses; evaluate credentials yourself.</p><h2>Contests</h2><p>Giveaways are governed by their official rules on the <a href="contests.html#rules">contests page</a>.</p><h2>Contributions</h2><p>Donations are voluntary, non-refundable except where required by law, and not tax-deductible.</p><h2>Liability</h2><p>The site is provided "as is". To the extent permitted by law, Body.Care is not liable for damages arising from use of the site.</p><h2>Changes</h2><p>We may update these terms; continued use means acceptance.</p>"""

DISCLAIMER = """<h2 id="medical">Medical disclaimer</h2><p>Body.Care content, tools and videos are for general educational purposes only and are not a substitute for professional medical advice, diagnosis or treatment. Always seek the advice of a qualified health provider with questions about a medical condition. Never disregard professional advice or delay seeking it because of something you read here. If you think you have a medical emergency, call your local emergency number.</p><p>Tool outputs (quizzes, calculators, ingredient ratings) are generalised estimates and may not suit your individual situation.</p>
<h2 id="affiliate">Affiliate disclosure</h2><p>Some links are affiliate links (including as an Amazon Associate): we may earn from qualifying purchases at no extra cost to you. Affiliate relationships never affect our criteria, ratings or editorial content.</p><h2 id="sponsored">Sponsored content</h2><p>Sponsored placements are always labelled "Sponsored" or "Made possible by". Sponsors don't review or approve editorial content.</p>"""

def notfound():
    body = """<section class="section center"><div class="wrap" style="max-width:640px"><span class="eyebrow">404</span><h1>This page took a spa day.</h1><p class="lead">It may have moved. Try search, or start with our most useful pages.</p>
<form action="search.html" style="display:flex;gap:8px;margin:20px 0"><input type="search" name="q" placeholder="Search Body.Care" aria-label="Search"><button class="btn btn-brand">Search</button></form>
<div class="hero-cta" style="justify-content:center"><a class="btn btn-primary" href="index.html">Home</a><a class="btn btn-ghost" href="tools/index.html">Free tools</a><a class="btn btn-ghost" href="library.html">Guides</a></div></div></section>"""
    out = page("404.html", "Page not found", "Page not found.", body, "", [], popup=False)
    # GitHub Pages serves 404.html at any depth: resolve relative links from the site root.
    fix = '<script>(function(){var p=location.pathname.split("/");var root=location.hostname.endsWith("github.io")?"/"+p[1]+"/":"/";document.write(\'<base href="\'+root+\'">\')})()</script>'
    return out.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n' + fix, 1).replace('<meta name="robots" content="index,follow,max-image-preview:large">', '<meta name="robots" content="noindex">')
