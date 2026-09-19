# -*- coding: utf-8 -*-
"""Body.Care editorial content. Add a dict to ARTICLES and re-run build.py —
the article page, library card, sitemap entry, search index and schema are generated."""

CATEGORIES = [
    ("skin", "Face & Skin", "🧴"),
    ("body", "Body Care", "🛁"),
    ("sun", "Sun Care", "☀️"),
    ("hair", "Hair & Scalp", "💇"),
    ("hands", "Hands, Nails & Feet", "💅"),
    ("oral", "Oral Care", "🦷"),
    ("men", "Men's Care", "🧔"),
    ("wellness", "Sleep & Wellness", "🌙"),
]

AAD = "https://www.aad.org/public"
NHS = "https://www.nhs.uk/conditions/"

ARTICLES = [
{
 "slug": "skincare-routine-basics",
 "cat": "skin", "title": "The 3-Step Skincare Routine That Actually Works",
 "desc": "Cleanse, moisturise, protect: why a minimalist routine beats a 10-step shelf, and exactly how to build one for your skin type.",
 "kw": "skincare routine beginners basic morning night steps",
 "mins": 7,
 "body": """
<p>Most visible skin improvement comes from three habits done daily for months — not from the tenth product on the shelf. Dermatology bodies such as the American Academy of Dermatology consistently point to the same foundation: gentle cleansing, moisturising, and daily sun protection.</p>
<h2 id="s1">Step 1: Cleanse gently</h2>
<p>Wash your face once or twice a day and after sweating. Use lukewarm water and a non-abrasive, pH-balanced cleanser. Hot water and scrubbing strip lipids and worsen dryness and redness.</p>
<ul><li><b>Oily / acne-prone:</b> gel or light foaming cleanser.</li><li><b>Dry / sensitive:</b> cream, milk or non-foaming cleanser — or just water in the morning.</li><li><b>Wearing SPF or makeup:</b> consider a cleansing balm first at night ("double cleanse").</li></ul>
<h2 id="s2">Step 2: Moisturise</h2>
<p>Moisturisers combine humectants (glycerin, hyaluronic acid) that attract water, emollients (squalane, fatty alcohols) that smooth, and occlusives (petrolatum, dimethicone) that seal. Apply within a few minutes of washing while skin is still slightly damp. Even oily skin benefits from a light, oil-free gel.</p>
<h2 id="s3">Step 3: Protect with SPF every morning</h2>
<p>Use a broad-spectrum SPF 30 or higher on all exposed skin, every day, including cloudy days. UV exposure drives most visible ageing (photoageing) and skin cancer risk. Use about two finger-lengths for face and neck.</p>
<blockquote>If you add just one "active" later, make it a retinoid at night — but only after the three basics are a habit.</blockquote>
<h2 id="s4">When to add actives</h2>
<p>After 4–6 weeks of consistency, add one targeted product at a time, two weeks apart, so you can tell what helps or irritates:</p>
<ul><li><b>Uneven tone / dullness:</b> vitamin C (AM) or niacinamide.</li><li><b>Acne / clogged pores:</b> salicylic acid, benzoyl peroxide, or adapalene.</li><li><b>Fine lines / texture:</b> retinol at night, 2–3 times per week to start.</li></ul>
<p>Not sure what fits? Use our free <a href="../tools/routine-builder.html">Routine Builder</a> — it generates a morning and night routine for your skin type and concerns.</p>
""",
 "faq": [("How long before I see results?", "Hydration improves in days. Tone and texture changes usually take 6–12 weeks of consistent use; retinoids can take 3–6 months."),
         ("Do I need toner?", "No. Modern toners are optional hydrating or exfoliating steps. Old-school alcohol toners can be drying."),
         ("Is a moisturiser with SPF enough?", "It can be, if you apply enough of it for a full SPF dose. Most people under-apply, so a dedicated sunscreen is more reliable.")],
 "doctor": "See a dermatologist for acne that scars or doesn't respond to over-the-counter care after 2–3 months, persistent redness, or any changing mole.",
 "sources": [("AAD: Everyday skin care", AAD + "/everyday-care"), ("AAD: How to apply sunscreen", AAD + "/everyday-care/sun-protection/shade-clothing-sunscreen/how-to-apply-sunscreen")]
},
{
 "slug": "sunscreen-guide",
 "cat": "sun", "title": "Sunscreen, Decoded: SPF, UVA, Amount & Reapplying",
 "desc": "What SPF numbers really mean, mineral vs chemical filters, how much to use, and the reapplication rules most people get wrong.",
 "kw": "sunscreen spf uva uvb mineral chemical reapply how much",
 "mins": 8,
 "body": """
<p>Sunscreen is the single most evidence-backed anti-ageing and skin-cancer-prevention product you can buy. Yet most people apply only a quarter to half the tested amount.</p>
<h2 id="s1">SPF, UVB and UVA</h2>
<p><b>SPF</b> measures protection against UVB (burning rays). SPF 30 filters roughly 97% of UVB, SPF 50 about 98%. <b>UVA</b> penetrates deeper, passes through clouds and windows, and drives photoageing and pigmentation. Look for "broad spectrum" (US), a UVA logo in a circle (EU/UK), or PA+++ / PA++++ (Asia).</p>
<h2 id="s2">Mineral vs chemical filters</h2>
<ul><li><b>Mineral (zinc oxide, titanium dioxide):</b> gentle, good for sensitive and post-procedure skin; can leave a white cast on deeper skin tones (tinted versions help).</li><li><b>Chemical/organic (avobenzone, and newer filters in EU/Asia):</b> elegant, invisible textures; occasionally sting around eyes.</li></ul>
<p>The best sunscreen is the one you'll apply generously every day.</p>
<h2 id="s3">How much to use</h2>
<p>SPF testing uses 2 mg/cm². In practice: about <b>1 ounce (≈30 ml, a shot glass)</b> for the whole adult body, and about <b>¼ teaspoon</b> or two finger-lengths for the face and neck. Calculate yours with the <a href="../tools/sunscreen-calculator.html">Sunscreen Calculator</a>.</p>
<h2 id="s4">Reapplying</h2>
<ul><li>Every 2 hours outdoors.</li><li>Immediately after swimming or heavy sweating — "water-resistant" labels last 40 or 80 minutes.</li><li>Apply 15 minutes before going out.</li></ul>
<h2 id="s5">Beyond the bottle</h2>
<p>Shade (especially 10am–4pm), wide-brimmed hats, UV-blocking sunglasses and UPF clothing reduce exposure without reapplication. For melasma, tinted sunscreens with iron oxides also block visible light that can worsen pigmentation.</p>
""",
 "faq": [("Do darker skin tones need sunscreen?", "Yes. Melanin gives some natural protection but doesn't prevent photoageing, hyperpigmentation or skin cancer."),
         ("Is SPF 100 twice as good as SPF 50?", "No. Returns diminish above SPF 50; application amount and reapplication matter far more."),
         ("Do I need sunscreen indoors?", "If you sit near windows for long periods, yes — UVA passes through most glass.")],
 "doctor": "See a doctor for a severe sunburn with blistering over a large area, fever, chills or confusion. Get any new, changing, bleeding or itchy spot checked.",
 "sources": [("AAD: How to select a sunscreen", AAD + "/everyday-care/sun-protection/shade-clothing-sunscreen/how-to-select-sunscreen"), ("AAD: How to apply sunscreen", AAD + "/everyday-care/sun-protection/shade-clothing-sunscreen/how-to-apply-sunscreen"), ("NHS: Sunscreen and sun safety", "https://www.nhs.uk/live-well/seasonal-health/sunscreen-and-sun-safety/")]
},
{
 "slug": "dry-skin-body-care",
 "cat": "body", "title": "Dry, Itchy Body Skin: A Dermatologist-Style Fix Plan",
 "desc": "Shower habits, the right moisturiser textures, urea and lactic acid, and a 14-day plan to calm rough, flaky, itchy body skin.",
 "kw": "dry skin body itchy flaky moisturiser lotion shower winter urea",
 "mins": 6,
 "body": """
<p>Dry body skin (xerosis) is mostly a barrier problem: the outer layer loses lipids and water faster than it can replace them. Winter air, hot showers and harsh soaps are the usual culprits.</p>
<h2 id="s1">Fix the shower first</h2>
<ul><li>Keep showers to 5–10 minutes with warm, not hot, water.</li><li>Use a fragrance-free, syndet ("soap-free") body wash; soap only where needed (underarms, groin, feet).</li><li>Pat dry — don't rub.</li></ul>
<h2 id="s2">Moisturise within 3 minutes</h2>
<p>Apply moisturiser while skin is still damp to trap water. Texture matters: <b>ointments</b> (petrolatum) are most protective, <b>creams</b> are the everyday sweet spot, <b>lotions</b> are lightest and least effective for very dry skin.</p>
<h2 id="s3">Ingredients that work</h2>
<ul><li><b>Urea (5–10%) and lactic acid:</b> hydrate and gently smooth rough patches, elbows, shins and keratosis pilaris ("chicken skin").</li><li><b>Ceramides + cholesterol:</b> replace barrier lipids.</li><li><b>Glycerin, petrolatum, dimethicone:</b> reliable, inexpensive workhorses.</li><li><b>Colloidal oatmeal:</b> soothes itch.</li></ul>
<p>Check any product in seconds with the <a href="../tools/ingredient-checker.html">Ingredient Checker</a>.</p>
<h2 id="s4">14-day reset</h2>
<ol><li>Days 1–14: short warm showers, fragrance-free wash, cream twice daily.</li><li>Day 4 onward: urea or lactic lotion on rough areas at night.</li><li>Run a humidifier in the bedroom in winter.</li><li>Wear breathable cotton; wash clothes with fragrance-free detergent.</li></ol>
""",
 "faq": [("Why does my skin itch more at night?", "Skin loses more water in the evening and itch perception increases at night. Moisturise before bed and keep the bedroom cool."),
         ("Can drinking water cure dry skin?", "Only if you're dehydrated. For most people, topical barrier care makes the real difference.")],
 "doctor": "See a doctor if itching disrupts sleep, skin cracks or bleeds, you see red inflamed patches (possible eczema or psoriasis), or dryness appears with fatigue or weight change.",
 "sources": [("AAD: Dermatologists' top tips for relieving dry skin", AAD + "/everyday-care/skin-care-basics/dry/dermatologists-tips-relieve-dry-skin"), ("NHS: Keratosis pilaris", NHS + "keratosis-pilaris/")]
},
{
 "slug": "body-acne-guide",
 "cat": "body", "title": "Back & Chest Acne: What Works (and What Makes It Worse)",
 "desc": "Why body acne happens, the benzoyl-peroxide wash trick, fungal acne look-alikes, and gym habits that clear skin.",
 "kw": "body acne back acne bacne chest breakouts fungal acne gym",
 "mins": 6,
 "body": """
<p>The back and chest have dense oil glands, and sweat, friction and occlusive clothing trap everything against the skin.</p>
<h2 id="s1">The benzoyl peroxide wash method</h2>
<p>Use a 4–10% benzoyl peroxide wash on affected areas and let it sit for 1–2 minutes before rinsing so it has time to work. It bleaches fabric — use white towels.</p>
<h2 id="s2">Add salicylic acid</h2>
<p>A salicylic-acid body spray or wash helps unclog pores on alternate days. Don't combine too many drying products at once.</p>
<h2 id="s3">Is it actually fungal acne?</h2>
<p><b>Pityrosporum (Malassezia) folliculitis</b> looks like uniform, itchy small bumps, often worse in heat and after sweating, and doesn't respond to acne treatments. Anti-fungal washes (ketoconazole or zinc pyrithione, left on for a few minutes) often help. Check your products for Malassezia triggers with our <a href="../tools/ingredient-checker.html">Ingredient Checker</a>.</p>
<h2 id="s4">Habits that matter</h2>
<ul><li>Shower soon after workouts; change out of sweaty clothes.</li><li>Choose loose, moisture-wicking fabrics.</li><li>Rinse hair conditioner off your back last.</li><li>Use non-comedogenic body lotion and sunscreen.</li></ul>
""",
 "faq": [("How long until body acne clears?", "Expect 6–8 weeks of consistent treatment. Dark marks can take months to fade — daily SPF helps."),
         ("Should I pop body pimples?", "No. It increases inflammation, scarring and dark marks.")],
 "doctor": "See a dermatologist for painful deep cysts, scarring, or acne that doesn't improve after 2–3 months — prescription treatments are very effective.",
 "sources": [("AAD: Acne resource center", AAD + "/diseases/acne")]
},
{
 "slug": "retinol-for-beginners",
 "cat": "skin", "title": "Retinol for Beginners: A Week-by-Week Start Plan",
 "desc": "How retinoids work, which one to start with, the 'sandwich method', purging vs irritation, and who should skip them.",
 "kw": "retinol retinoid beginners adapalene tretinoin purging sandwich anti aging",
 "mins": 7,
 "body": """
<p>Retinoids (vitamin A derivatives) are among the most researched topical ingredients for acne, texture, fine lines and uneven tone. They speed cell turnover and support collagen over time.</p>
<h2 id="s1">The retinoid ladder</h2>
<ul><li><b>Retinyl esters:</b> gentlest, slowest.</li><li><b>Retinol (0.25–1%):</b> the classic over-the-counter option.</li><li><b>Retinal (retinaldehyde):</b> stronger and faster than retinol.</li><li><b>Adapalene 0.1%:</b> over-the-counter in many countries; excellent for acne.</li><li><b>Tretinoin / tazarotene:</b> prescription strength.</li></ul>
<h2 id="s2">Week-by-week start</h2>
<ol><li><b>Weeks 1–2:</b> a pea-sized amount for the whole face, 2 nights per week, on dry skin.</li><li><b>Weeks 3–4:</b> 3 nights per week if skin is comfortable.</li><li><b>Weeks 5–8:</b> every other night.</li><li><b>After:</b> nightly if tolerated. Irritation = step back a stage.</li></ol>
<h2 id="s3">The sandwich method</h2>
<p>Sensitive? Apply moisturiser, then retinoid, then moisturiser again. It buffers irritation with minimal loss of results.</p>
<h2 id="s4">Rules</h2>
<ul><li>Wear SPF every morning.</li><li>Don't use with AHA/BHA the same night at first — check combinations with the <a href="../tools/layering-checker.html">Layering Checker</a>.</li><li>Avoid around the nostrils and lip corners.</li><li><b>Skip during pregnancy and breastfeeding</b> unless your doctor says otherwise.</li></ul>
""",
 "faq": [("Is purging real?", "Yes — retinoids can bring existing clogs to the surface for 4–6 weeks in acne-prone areas. New breakouts in areas you don't usually break out suggest irritation instead."),
         ("Can I use retinol around my eyes?", "Many people can with a gentler formula, starting slowly. Stop if you get stinging or flaking.")],
 "doctor": "Talk to a dermatologist for prescription retinoids, severe irritation, or if you're pregnant, trying to conceive or breastfeeding.",
 "sources": [("AAD: Acne resource center", AAD + "/diseases/acne"), ("Mayo Clinic: Wrinkle creams", "https://www.mayoclinic.org/healthy-lifestyle/adult-health/in-depth/wrinkle-creams/art-20047463")]
},
{
 "slug": "hyperpigmentation-darker-skin",
 "cat": "skin", "title": "Dark Spots & Hyperpigmentation on Melanin-Rich Skin",
 "desc": "Post-inflammatory hyperpigmentation, melasma and sun spots — gentle, effective ingredients and the mistakes that make marks darker.",
 "kw": "hyperpigmentation dark spots melasma pih darker skin brown skin tone",
 "mins": 7,
 "body": """
<p>Melanin-rich skin is more prone to <b>post-inflammatory hyperpigmentation (PIH)</b>: dark marks left after acne, bites, eczema or irritation. The key principle is simple — <b>prevent inflammation</b>, because irritation makes pigment worse.</p>
<h2 id="s1">Know the type</h2>
<ul><li><b>PIH:</b> flat brown-to-dark marks after a pimple or injury.</li><li><b>Melasma:</b> symmetrical patches on cheeks, forehead, upper lip; triggered by UV, visible light and hormones.</li><li><b>Sun spots:</b> small, defined spots on sun-exposed areas.</li></ul>
<h2 id="s2">Ingredients with evidence</h2>
<ul><li><b>Daily broad-spectrum SPF</b> — tinted with iron oxides for melasma.</li><li><b>Azelaic acid</b> — treats acne and pigment; well tolerated.</li><li><b>Niacinamide, tranexamic acid, alpha arbutin, vitamin C</b> — gentle brighteners.</li><li><b>Retinoids</b> — speed turnover; start slowly to avoid irritation-driven PIH.</li><li><b>Mandelic acid</b> — a gentler exfoliating acid.</li></ul>
<h2 id="s3">Mistakes that deepen marks</h2>
<ul><li>Picking or squeezing spots.</li><li>Harsh scrubs, lemon juice, DIY peels.</li><li>Unregulated "whitening" creams — some contain mercury or potent steroids. Buy from reputable sources.</li></ul>
<h2 id="s4">Timeline</h2>
<p>PIH in the top layer fades over 3–12 months; deeper pigment takes longer. Consistency plus sun protection is the whole game.</p>
""",
 "faq": [("Will laser fix it faster?", "Some lasers and peels help but carry a risk of worsening pigment on deeper skin tones. Choose a dermatologist experienced with skin of colour."),
         ("Is hydroquinone safe?", "It's effective but should be used under medical supervision, for limited periods.")],
 "doctor": "See a dermatologist (ideally experienced with skin of colour) for melasma, rapidly changing dark spots, or any new dark streak in a nail.",
 "sources": [("AAD: How to fade dark spots in darker skin tones", AAD + "/everyday-care/skin-care-secrets/routine/fade-dark-spots"), ("AAD: Melasma", AAD + "/diseases/a-z/melasma-overview")]
},
{
 "slug": "eczema-care",
 "cat": "skin", "title": "Eczema-Prone Skin: Daily Care That Reduces Flares",
 "desc": "Soak-and-seal bathing, the moisturisers that matter, trigger tracking and what to do during a flare.",
 "kw": "eczema atopic dermatitis flare itch moisturiser soak and seal",
 "mins": 6,
 "body": """
<p>Atopic dermatitis (eczema) involves a leaky skin barrier plus an overactive immune response. Daily barrier care is the base layer of every treatment plan.</p>
<h2 id="s1">Soak and seal</h2>
<ol><li>Bathe or shower 5–10 minutes in lukewarm water.</li><li>Use a gentle, fragrance-free cleanser only where needed.</li><li>Pat dry, apply any prescribed medication to flare areas, then moisturise everywhere within 3 minutes.</li></ol>
<h2 id="s2">Choose the right moisturiser</h2>
<p>Thicker is better: ointments and creams in tubs or jars beat pump lotions. Look for fragrance-free formulas with ceramides, glycerin, petrolatum or colloidal oatmeal. Apply at least twice daily — including when skin looks clear.</p>
<h2 id="s3">Track your triggers</h2>
<ul><li>Fragrance and certain preservatives (e.g. methylisothiazolinone).</li><li>Wool and rough fabrics; sweat and heat.</li><li>Low humidity; stress; some detergents.</li></ul>
<p>Scan your products with the <a href="../tools/ingredient-checker.html">Ingredient Checker</a> using the "Sensitive" profile.</p>
<h2 id="s4">During a flare</h2>
<p>Keep nails short, use cool compresses for itch, and follow your clinician's plan (often a short course of topical anti-inflammatory medication). Don't stop moisturising.</p>
""",
 "faq": [("Is eczema contagious?", "No. But broken eczema skin can become infected, so watch for crusting, oozing or pus."),
         ("Can diet cure eczema?", "Food allergies affect a minority, mostly young children. Don't cut major food groups without medical advice.")],
 "doctor": "See a doctor for eczema that disturbs sleep, spreads, oozes or crusts, or doesn't improve with good daily care.",
 "sources": [("AAD: Eczema resource center", AAD + "/diseases/eczema"), ("NHS: Atopic eczema", NHS + "atopic-eczema/")]
},
{
 "slug": "scalp-and-hair-care",
 "cat": "hair", "title": "Scalp Care 101: Dandruff, Oil, Build-Up & Healthy Hair",
 "desc": "How often to wash for your hair type, anti-dandruff ingredients that work, and daily habits that reduce breakage.",
 "kw": "hair care scalp dandruff washing oily hair breakage shampoo conditioner",
 "mins": 6,
 "body": """
<p>Healthy hair starts at the scalp — it's skin, with the same needs for gentle cleansing and balance.</p>
<h2 id="s1">How often to wash</h2>
<ul><li><b>Fine or oily hair:</b> daily or every other day.</li><li><b>Wavy/medium:</b> 2–3 times a week.</li><li><b>Coily or tightly curled hair:</b> once a week to every two weeks, with a moisturising routine in between.</li></ul>
<p>Shampoo the scalp; let the suds rinse through the lengths. Condition the lengths and ends.</p>
<h2 id="s2">Dandruff and seborrheic dermatitis</h2>
<p>Flaking is usually linked to the yeast Malassezia. Rotate anti-dandruff shampoos with <b>zinc pyrithione, ketoconazole, selenium sulfide or salicylic acid</b>, and leave lather on the scalp for 3–5 minutes before rinsing.</p>
<h2 id="s3">Reduce breakage</h2>
<ul><li>Use heat protectant and the lowest effective heat.</li><li>Avoid tight ponytails and braids that pull (traction alopecia).</li><li>Detangle wet hair gently with a wide-tooth comb, from ends upward.</li><li>Sleep on silk or satin to reduce friction.</li></ul>
<h2 id="s4">Shedding vs hair loss</h2>
<p>Losing 50–100 hairs a day is normal. Sudden heavy shedding 2–3 months after illness, childbirth or stress (telogen effluvium) usually recovers. Widening parting or receding hairline warrants a doctor visit — early treatment works best.</p>
""",
 "faq": [("Does cutting hair make it grow faster?", "No — trims prevent split ends travelling up the shaft, which helps you retain length."),
         ("Are sulfate-free shampoos better?", "For dry, curly or colour-treated hair they're often gentler. Oily scalps may prefer a sulfate shampoo.")],
 "doctor": "See a dermatologist for patchy hair loss, scalp pain or scarring, sudden heavy shedding lasting over 6 months, or a very itchy inflamed scalp.",
 "sources": [("AAD: Tips for healthy hair", AAD + "/everyday-care/hair-scalp-care/hair/healthy-hair-tips"), ("AAD: Hair loss resource center", AAD + "/diseases/hair-loss")]
},
{
 "slug": "hand-nail-care",
 "cat": "hands", "title": "Hands & Nails: Stop Cracking, Peeling and Brittle Nails",
 "desc": "Hand-washing without damage, cuticle care, the truth about brittle nails, and warning signs to never ignore.",
 "kw": "hand care nails brittle peeling cuticles cracked hands",
 "mins": 5,
 "body": """
<p>Frequent washing and sanitiser use strip the skin on your hands, which has few oil glands. Nails suffer from the same wet–dry cycling.</p>
<h2 id="s1">Hands</h2>
<ul><li>Moisturise after every wash — keep a tube by each sink.</li><li>At night, apply a thick ointment and wear cotton gloves for severely cracked hands.</li><li>Wear gloves for dishes and cleaning products.</li></ul>
<h2 id="s2">Nails</h2>
<ul><li>Keep nails short and file in one direction.</li><li>Don't cut or push cuticles aggressively — they protect against infection.</li><li>Rub moisturiser into nails and cuticles daily.</li><li>Limit acetone removers and give gel manicures breaks.</li></ul>
<h2 id="s3">Brittle nails</h2>
<p>Most brittleness comes from water exposure and dryness, not deficiency. Biotin supplements help only if you're deficient — and they can interfere with some lab tests, so tell your doctor if you take them.</p>
""",
 "faq": [("Why do my nails have white spots?", "Usually minor trauma to the nail base. They grow out."),
         ("Are ridges normal?", "Fine vertical ridges are common with age. New horizontal dents across all nails can follow illness — mention them to a doctor.")],
 "doctor": "Get urgent attention for a new dark streak in a nail, nail lifting with pain or pus, or a nail change with swelling around it.",
 "sources": [("AAD: Healthy hair and nails", AAD + "/public-health/good-skin-knowledge/lesson-plans/healthy-hair-and-nails"), ("AAD: Hand eczema", AAD + "/diseases/eczema/types/hand-eczema")]
},
{
 "slug": "foot-care-guide",
 "cat": "hands", "title": "Foot Care: Cracked Heels, Odour, Calluses & Athlete's Foot",
 "desc": "A weekly foot routine, urea for heels, how to stop odour and fungus, and when feet need a professional.",
 "kw": "foot care cracked heels athletes foot odour calluses feet",
 "mins": 5,
 "body": """
<h2 id="s1">Weekly routine</h2>
<ol><li>Wash daily and dry thoroughly, especially between toes.</li><li>Twice weekly, gently file calluses on dry skin — never cut them.</li><li>Apply a urea (10–25%) or salicylic cream to heels at night; cotton socks on top.</li><li>Trim toenails straight across.</li></ol>
<h2 id="s2">Odour</h2>
<p>Foot odour comes from bacteria breaking down sweat. Alternate shoes so each pair dries for 24 hours, wear moisture-wicking socks, and consider an antiperspirant on the soles at night.</p>
<h2 id="s3">Athlete's foot</h2>
<p>Itchy, scaly or peeling skin between toes is often fungal. Over-the-counter antifungals (terbinafine, clotrimazole) work — continue 1–2 weeks after it clears. Wear flip-flops in gym showers.</p>
""",
 "faq": [("Why do my heels crack?", "Thick, dry heel skin splits under pressure. Urea creams thin and hydrate it; open-backed shoes can make it worse.")],
 "doctor": "People with diabetes or poor circulation should check feet daily and see a clinician for any cut, blister or colour change. Also seek help for ingrown nails with redness or pus.",
 "sources": [("NHS: Athlete's foot", NHS + "athletes-foot/")]
},
{
 "slug": "oral-care-basics",
 "cat": "oral", "title": "Oral Care Basics: Brushing, Flossing & Fresh Breath",
 "desc": "The 2-minute brushing standard, fluoride facts, interdental cleaning and what actually fixes bad breath.",
 "kw": "oral care teeth brushing flossing fluoride bad breath gums",
 "mins": 5,
 "body": """
<h2 id="s1">The daily standard</h2>
<ul><li>Brush twice a day for 2 minutes with fluoride toothpaste.</li><li><b>Spit, don't rinse</b> after brushing so fluoride stays on teeth.</li><li>Clean between teeth once a day — floss, interdental brushes or a water flosser.</li><li>Replace your toothbrush every 3–4 months.</li></ul>
<h2 id="s2">Bad breath</h2>
<p>Most bad breath comes from bacteria on the tongue and between teeth. Brush or scrape your tongue, clean between teeth, stay hydrated, and treat gum disease. Mouthwash masks odour temporarily.</p>
<h2 id="s3">Gums</h2>
<p>Bleeding gums when brushing are often an early sign of gum inflammation (gingivitis) — keep cleaning gently, not less. Book a dental check if it persists beyond two weeks.</p>
""",
 "faq": [("Electric or manual brush?", "Both work with good technique. Powered brushes can remove more plaque for many people."),
         ("Is whitening safe?", "Dentist-supervised or reputable peroxide products are generally safe; sensitivity is common and temporary.")],
 "doctor": "See a dentist for tooth pain, swelling, persistent bleeding gums, loose teeth or a mouth ulcer lasting over 3 weeks.",
 "sources": [("NHS: How to keep your teeth clean", "https://www.nhs.uk/live-well/healthy-teeth-and-gums/how-to-keep-your-teeth-clean/"), ("ADA MouthHealthy", "https://www.mouthhealthy.org/")]
},
{
 "slug": "mens-skincare-grooming",
 "cat": "men", "title": "Men's Skincare & Shaving: The No-Nonsense Routine",
 "desc": "A 3-minute routine, how to shave without razor bumps, and beard care that keeps the skin underneath healthy.",
 "kw": "men skincare shaving razor bumps beard grooming routine",
 "mins": 5,
 "body": """
<p>Men's skin is typically thicker and oilier, and daily shaving adds friction. The fundamentals are the same — cleanse, moisturise, SPF — with a smarter shave on top.</p>
<h2 id="s1">3-minute routine</h2>
<ol><li>AM: gentle gel cleanser → moisturiser with SPF 30+.</li><li>PM: cleanse → light moisturiser (add retinol later for texture/ageing).</li></ol>
<h2 id="s2">Shave without bumps</h2>
<ul><li>Shave after a warm shower when hair is soft.</li><li>Use a sharp blade and a moisturising shave cream.</li><li>Shave with the grain; rinse the blade after each stroke.</li><li>Don't stretch the skin.</li><li>Ingrown hairs (razor bumps) often improve with a salicylic or glycolic product 2–3 nights a week, a single-blade razor, or trimming instead of close shaving.</li></ul>
<h2 id="s3">Beard care</h2>
<p>Wash your beard with a gentle cleanser, condition it, and moisturise the skin underneath. Flaky beard skin is often seborrheic dermatitis — anti-dandruff shampoo used as a beard wash helps.</p>
""",
 "faq": [("Aftershave with alcohol?", "Alcohol-heavy aftershaves sting and dry the skin. A fragrance-free, soothing balm is better.")],
 "doctor": "See a dermatologist for persistent razor bumps with scarring or dark spots (pseudofolliculitis barbae) — prescription and laser options exist.",
 "sources": [("AAD: Tips for men's skin care", AAD + "/everyday-care/skin-care-basics/care/skin-care-for-men"), ("AAD: How to shave", AAD + "/everyday-care/skin-care-basics/hair/how-to-shave")]
},
{
 "slug": "body-odor-hygiene",
 "cat": "body", "title": "Body Odour & Sweat: Deodorant vs Antiperspirant, Explained",
 "desc": "Why sweat smells, how antiperspirants actually work (apply at night!), and fixes for excessive sweating.",
 "kw": "body odour sweat deodorant antiperspirant hyperhidrosis underarm",
 "mins": 5,
 "body": """
<h2 id="s1">Why sweat smells</h2>
<p>Fresh sweat is nearly odourless. Odour comes from skin bacteria breaking down sweat from apocrine glands in the underarms and groin.</p>
<h2 id="s2">Deodorant vs antiperspirant</h2>
<ul><li><b>Deodorant:</b> reduces bacteria and masks odour; doesn't stop sweat.</li><li><b>Antiperspirant:</b> aluminium salts temporarily plug sweat ducts.</li></ul>
<p><b>Pro tip:</b> apply antiperspirant at night to completely dry skin — sweat glands are least active, so the plugs form better and last through the next day, even after a morning shower.</p>
<h2 id="s3">Other odour fixes</h2>
<ul><li>Wash with an antibacterial or benzoyl-peroxide wash in underarms.</li><li>Choose natural, breathable fabrics and wash workout gear promptly.</li><li>Trim underarm hair to reduce bacteria-holding surface.</li></ul>
<h2 id="s4">Excessive sweating</h2>
<p>Hyperhidrosis — sweating that soaks clothing or interferes with daily life — is common and treatable: clinical-strength antiperspirants, prescription wipes, iontophoresis, botulinum toxin injections and more.</p>
""",
 "faq": [("Do antiperspirants cause cancer?", "Major cancer organisations report no convincing evidence linking antiperspirants to breast cancer.")],
 "doctor": "See a doctor for new night sweats, sudden changes in body odour, or sweating with weight loss, fever or palpitations.",
 "sources": [("NHS: Excessive sweating", NHS + "excessive-sweating-hyperhidrosis/")]
},
{
 "slug": "sleep-and-skin",
 "cat": "wellness", "title": "Sleep, Stress & Skin: The Overnight Repair Routine",
 "desc": "How sleep and stress show up on your skin, and a simple evening routine that supports both.",
 "kw": "sleep skin stress beauty sleep night routine wellness",
 "mins": 5,
 "body": """
<p>Short sleep and chronic stress are linked with a weaker skin barrier, slower recovery and flares of conditions like acne, eczema and psoriasis. Adults generally need 7 or more hours per night.</p>
<h2 id="s1">A 30-minute wind-down</h2>
<ol><li>Dim lights and screens 30–60 minutes before bed.</li><li>Cleanse and apply your night routine — a consistent ritual cues sleep.</li><li>Keep the bedroom cool, dark and quiet; a humidifier helps dry skin in winter.</li><li>Change pillowcases weekly (twice weekly for acne-prone skin).</li></ol>
<h2 id="s2">Stress and skin</h2>
<p>Stress can trigger scratching, picking and flares. Short daily practices — a 10-minute walk, breathing exercises, journaling — are low-cost and helpful. Pair them with sleep and a steady routine.</p>
<h2 id="s3">Puffy eyes</h2>
<p>Salt, alcohol, allergies and sleeping flat can cause morning puffiness. Sleep slightly elevated and use a cool compress. Persistent dark circles are often genetic or structural.</p>
""",
 "faq": [("Does 'beauty sleep' really exist?", "Research links poor sleep with visible signs like dull skin and puffy eyes, and slower barrier recovery. Sleep is foundational self-care.")],
 "doctor": "Talk to a doctor if you have ongoing insomnia, loud snoring with daytime sleepiness, or stress that's affecting daily life.",
 "sources": [("CDC: About sleep", "https://www.cdc.gov/sleep/about/index.html")]
},
]
