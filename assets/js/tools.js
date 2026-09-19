/* Body.Care interactive tools. Each tool renders a result, then offers
   "email me this + a full plan" — every tool doubles as a lead magnet. */
(function () {
  "use strict";
  var $ = BC.$, $$ = BC.$$;
  var esc = function (s) { return String(s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); };

  /* Attach the tool result to the lead form below it so the lead is pre-qualified. */
  function feedLead(tool, summary) {
    var f = $('form[data-form="plan"][data-tool="' + tool + '"]');
    if (!f) return;
    for (var p = f.parentElement; p; p = p.parentElement) { if (p.hasAttribute && p.hasAttribute("data-lead-after")) p.hidden = false; }
    var h = f.querySelector('[name="result"]'); if (h) h.value = summary;
    BC.track && BC.track("tool_complete", { tool: tool });
  }

  /* ---------- Generic multi-step engine ---------- */
  function stepper(root, onFinish) {
    var steps = $$(".step", root), i = 0, bar = $(".progress i", root), back = $("[data-back]", root), next = $("[data-next]", root), count = $("[data-count]", root);
    function show() {
      steps.forEach(function (s, j) { s.classList.toggle("active", j === i); });
      if (bar) bar.style.width = ((i + 1) / steps.length * 100) + "%";
      if (back) back.style.visibility = i ? "visible" : "hidden";
      if (next) next.textContent = i === steps.length - 1 ? "See my results →" : "Next →";
      if (count) count.textContent = "Step " + (i + 1) + " of " + steps.length;
    }
    function valid() {
      var req = $$("[data-required]", steps[i]);
      for (var k = 0; k < req.length; k++) { var n = req[k].getAttribute("data-required"); if (!$('input[name="' + n + '"]:checked', steps[i])) { BC.toast("Pick an option to continue"); return false; } }
      return true;
    }
    if (next) next.addEventListener("click", function () { if (!valid()) return; if (i < steps.length - 1) { i++; show(); root.scrollIntoView({ behavior: "smooth", block: "start" }); } else onFinish(); });
    if (back) back.addEventListener("click", function () { if (i) { i--; show(); } });
    show();
    return { reset: function () { i = 0; show(); } };
  }
  function val(root, name) { var el = $('input[name="' + name + '"]:checked', root); return el ? el.value : ""; }
  function vals(root, name) { return $$('input[name="' + name + '"]:checked', root).map(function (x) { return x.value; }); }

  /* ================= 1. Skin Type Quiz ================= */
  var sq = $("#skin-quiz");
  if (sq) {
    stepper(sq, function () {
      var score = { oily: 0, dry: 0, combo: 0, normal: 0, sensitive: 0 };
      $$("input:checked", sq).forEach(function (x) { (x.getAttribute("data-s") || "").split(",").forEach(function (k) { if (k) score[k.trim()] = (score[k.trim()] || 0) + 1; }); });
      var sens = score.sensitive >= 2;
      delete score.sensitive;
      var type = Object.keys(score).sort(function (a, b) { return score[b] - score[a]; })[0];
      var info = {
        oily: ["Oily", "Your skin makes more sebum, especially across the T-zone. Pores can look larger and breakouts are more likely.", ["Gel or foaming gentle cleanser", "Niacinamide serum", "Lightweight gel moisturiser (yes, still moisturise)", "Salicylic acid 2–3×/week", "Oil-free SPF 30+ daily"]],
        dry: ["Dry", "Your skin makes less oil and loses water faster, so it can feel tight, rough or flaky.", ["Cream or milky non-foaming cleanser", "Hyaluronic acid on damp skin", "Ceramide-rich cream", "Lactic acid or urea 1–2×/week", "Hydrating SPF 30+ daily"]],
        combo: ["Combination", "Oilier T-zone, normal-to-dry cheeks. You'll get the best results by treating zones differently.", ["Gentle gel-cream cleanser", "Niacinamide all over", "Light lotion; add richer cream to cheeks only", "BHA on the T-zone only", "Fluid SPF 30+ daily"]],
        normal: ["Normal / balanced", "Few issues with oil or dryness. The job is to protect and maintain.", ["Gentle cleanser", "Antioxidant (vitamin C) in the morning", "Moisturiser matched to season", "Retinoid at night for long-term prevention", "SPF 30+ daily"]]
      }[type];
      var html = '<div class="result-box"><span class="tag accent">Your result</span><h2 style="margin:.6rem 0">' + info[0] + (sens ? " + Sensitive" : "") + " skin</h2><p>" + info[1] + "</p>" +
        (sens ? '<div class="callout"><strong>Sensitive flag</strong>Choose fragrance-free products, introduce one new product at a time and patch test for 5–7 days.</div>' : "") +
        "<h3>Your starter routine</h3><ol>" + info[2].map(function (x) { return "<li>" + x + "</li>"; }).join("") + '</ol><p class="small muted">Educational guidance only. Persistent rashes, acne or changing moles need a dermatologist.</p><div class="hero-cta" style="margin:1rem 0 0"><a class="btn btn-brand btn-sm" href="routine-builder.html">Build my full AM/PM routine</a><button class="btn btn-ghost btn-sm" data-retake>Retake quiz</button></div></div>';
      var out = $("#skin-result"); out.innerHTML = html; out.hidden = false; sq.hidden = true;
      $("[data-retake]", out).addEventListener("click", function () { out.hidden = true; sq.hidden = false; $$("input", sq).forEach(function (x) { x.checked = false; }); location.reload(); });
      try { localStorage.setItem("bc-skintype", type + (sens ? "-sensitive" : "")); } catch (e) {}
      feedLead("skin-quiz", info[0] + (sens ? " + Sensitive" : ""));
      out.scrollIntoView({ behavior: "smooth" });
    });
  }

  /* ================= 2. Routine Builder ================= */
  var rb = $("#routine-builder");
  if (rb) {
    try { var st = localStorage.getItem("bc-skintype"); if (st) { var base = st.split("-")[0]; var r = $('input[name="type"][value="' + base + '"]', rb); if (r) r.checked = true; if (st.indexOf("sensitive") > -1) { var s2 = $('input[name="sensitive"][value="yes"]', rb); if (s2) s2.checked = true; } } } catch (e) {}
    stepper(rb, function () {
      var type = val(rb, "type"), concerns = vals(rb, "concern"), sens = val(rb, "sensitive") === "yes", preg = val(rb, "pregnant") === "yes", level = val(rb, "level") || "simple", budget = val(rb, "budget") || "mid";
      var am = [], pm = [], weekly = [], notes = [];
      var cleanser = { oily: "Gentle gel/foaming cleanser", dry: "Cream / non-foaming cleanser", combo: "Gentle gel-cream cleanser", normal: "Gentle cleanser" }[type] || "Gentle cleanser";
      var moist = { oily: "Oil-free gel moisturiser", dry: "Rich ceramide cream", combo: "Light lotion (richer on dry zones)", normal: "Balanced moisturiser" }[type] || "Moisturiser";
      am.push(["Cleanse", type === "dry" ? "Rinse with water or " + cleanser.toLowerCase() : cleanser]);
      if (concerns.indexOf("pigment") > -1 || concerns.indexOf("aging") > -1 || level !== "simple") am.push(["Antioxidant", sens ? "Vitamin C derivative (gentler)" : "Vitamin C serum (10–15%)"]);
      if (concerns.indexOf("acne") > -1 && !preg) am.push(["Treat", "Benzoyl peroxide 2.5% (spot or wash) — optional"]);
      if (concerns.indexOf("redness") > -1) am.push(["Calm", "Azelaic acid 10% or niacinamide"]);
      am.push(["Moisturise", moist]);
      am.push(["Protect", concerns.indexOf("pigment") > -1 ? "Tinted mineral SPF 30–50 (iron oxides help melasma)" : "Broad-spectrum SPF 30+ — two finger-lengths for face + neck"]);
      pm.push(["Cleanse", level === "advanced" ? "Double cleanse if wearing SPF/makeup: balm, then " + cleanser.toLowerCase() : cleanser]);
      if (preg) { pm.push(["Treat", concerns.indexOf("acne") > -1 || concerns.indexOf("pigment") > -1 ? "Azelaic acid (commonly considered pregnancy-compatible — confirm with your OB)" : "Bakuchiol or peptide serum"]); notes.push("Pregnant/breastfeeding: skip retinoids and high-strength salicylic acid; confirm every active with your doctor."); }
      else if (concerns.indexOf("acne") > -1) pm.push(["Treat", "Adapalene 0.1% (every other night to start)"]);
      else if (concerns.indexOf("aging") > -1 || concerns.indexOf("texture") > -1) pm.push(["Treat", sens ? "Retinyl ester or bakuchiol, 2 nights/week" : "Retinol 0.25–0.5%, 2–3 nights/week, build up"]);
      if (concerns.indexOf("pigment") > -1 && !preg) pm.push(["Brighten", "Tranexamic acid or alpha arbutin serum (on non-retinoid nights)"]);
      if (concerns.indexOf("dryness") > -1 || type === "dry") pm.push(["Hydrate", "Hyaluronic acid on damp skin"]);
      pm.push(["Moisturise", moist + (type === "dry" ? " — seal with a thin layer of petrolatum on very dry patches" : "")]);
      if (concerns.indexOf("acne") > -1 || type === "oily") weekly.push(sens ? "Mandelic acid 1–2×/week (non-retinoid nights)" : "Salicylic acid 2% 2–3×/week (non-retinoid nights)");
      else if (concerns.indexOf("texture") > -1 || type === "dry") weekly.push("Lactic acid 1–2×/week (non-retinoid nights)");
      if (concerns.indexOf("body") > -1) weekly.push("Body: salicylic or benzoyl-peroxide body wash for back/chest (leave 1–2 min, rinse); urea or lactic lotion for rough arms/legs");
      if (sens) notes.push("Sensitive: fragrance-free only, introduce one product every 2 weeks, patch test behind the ear.");
      if (level === "simple") notes.push("Minimalist mode: if you only do three things — cleanse, moisturise, SPF — you're already ahead of most people.");
      notes.push("Budget tier (" + { low: "budget", mid: "mid-range", high: "premium" }[budget] + "): see matching picks on our Picks page.");
      var row = function (x, i) { return "<tr><td>" + (i + 1) + "</td><td><b>" + esc(x[0]) + "</b></td><td>" + esc(x[1]) + "</td></tr>"; };
      var out = $("#routine-result");
      out.innerHTML = '<div class="result-box"><span class="tag accent">Your personalised routine</span><h2 style="margin:.6rem 0">' + esc({ oily: "Oily", dry: "Dry", combo: "Combination", normal: "Normal" }[type] || "Your") + " skin" + (concerns.length ? " · " + concerns.map(esc).join(", ") : "") + '</h2><div class="grid g2" style="margin-top:14px"><div><h3>☀️ Morning</h3><div class="table-wrap"><table><tbody>' + am.map(row).join("") + '</tbody></table></div></div><div><h3>🌙 Night</h3><div class="table-wrap"><table><tbody>' + pm.map(row).join("") + "</tbody></table></div></div></div>" +
        (weekly.length ? "<h3 style=\"margin-top:18px\">📅 Weekly</h3><ul>" + weekly.map(function (w) { return "<li>" + esc(w) + "</li>"; }).join("") + "</ul>" : "") +
        "<h3>Notes</h3><ul>" + notes.map(function (w) { return "<li>" + esc(w) + "</li>"; }).join("") + '</ul><div class="hero-cta" style="margin:1rem 0 0"><button class="btn btn-ghost btn-sm" onclick="window.print()">Print / save PDF</button><a class="btn btn-ghost btn-sm" href="../picks.html">Shop matching picks</a><a class="btn btn-ghost btn-sm" href="layering-checker.html">Check my layering</a></div></div>';
      out.hidden = false;
      feedLead("routine-builder", "AM: " + am.map(function (x) { return x[1]; }).join(" > ") + " | PM: " + pm.map(function (x) { return x[1]; }).join(" > "));
      out.scrollIntoView({ behavior: "smooth" });
    });
  }

  /* ================= 3. Ingredient Checker ================= */
  var DB = window.BC_INGREDIENTS || [];
  function lookup(token) {
    var t = token.toLowerCase().replace(/\(.*?\)/g, "").replace(/\*/g, "").replace(/\s+/g, " ").trim().replace(/\.$/, "");
    if (!t) return null;
    for (var i = 0; i < DB.length; i++) { if (DB[i].k.indexOf(t) > -1) return DB[i]; }
    for (var j = 0; j < DB.length; j++) { for (var k = 0; k < DB[j].k.length; k++) { var key = DB[j].k[k]; if (key.length > 5 && (t.indexOf(key) > -1)) return DB[j]; } }
    return null;
  }
  function parseList(txt) { return txt.replace(/^\s*(ingredients|inci)\s*:/i, "").split(/,|\n|;|•/).map(function (s) { return s.trim(); }).filter(Boolean); }
  var inci = $("#inci-form");
  if (inci) {
    var sample = $("[data-sample]"); if (sample) sample.addEventListener("click", function () { $("#inci-text").value = "Aqua, Glycerin, Niacinamide, Cetearyl Alcohol, Squalane, Ceramide NP, Sodium Hyaluronate, Panthenol, Dimethicone, Parfum, Linalool, Phenoxyethanol, Xanthan Gum, Citric Acid"; inci.requestSubmit ? inci.requestSubmit() : inci.dispatchEvent(new Event("submit")); });
    inci.addEventListener("submit", function (e) {
      e.preventDefault();
      var list = parseList($("#inci-text").value);
      if (!list.length) { BC.toast("Paste an ingredient list first"); return; }
      var profile = $$('input[name="profile"]:checked', inci).map(function (x) { return x.value; });
      var counts = { good: 0, caution: 0, avoid: 0, neutral: 0, unknown: 0 }, alerts = [], seen = {};
      var rows = list.map(function (raw, i) {
        var hit = lookup(raw), r = hit ? hit.r : "unknown";
        counts[r]++;
        var fl = (hit && hit.flags) || [];
        if (hit && !seen[hit.name]) {
          seen[hit.name] = 1;
          if (profile.indexOf("acne") > -1 && fl.indexOf("c") > -1) alerts.push("⚠️ <b>" + esc(hit.name) + "</b> may clog pores for acne-prone skin.");
          if (profile.indexOf("fungal") > -1 && fl.indexOf("fa") > -1) alerts.push("⚠️ <b>" + esc(hit.name) + "</b> may feed Malassezia (fungal acne).");
          if (profile.indexOf("sensitive") > -1 && fl.indexOf("s") > -1) alerts.push("⚠️ <b>" + esc(hit.name) + "</b> is a common irritant/sensitiser.");
          if (profile.indexOf("pregnant") > -1 && fl.indexOf("p") > -1) alerts.push("🤰 <b>" + esc(hit.name) + "</b> — generally avoided in pregnancy; ask your doctor.");
          if (fl.indexOf("photo") > -1) alerts.push("☀️ <b>" + esc(hit.name) + "</b> increases sun sensitivity — daily SPF essential.");
          if (r === "avoid") alerts.push("⛔ <b>" + esc(hit.name) + "</b> — " + esc(hit.n));
        }
        var cls = { good: "r-good", caution: "r-caution", avoid: "r-avoid", neutral: "r-neutral", unknown: "r-neutral" }[r];
        return "<tr><td>" + (i + 1) + "</td><td><b>" + esc(raw) + "</b>" + (hit && hit.name.toLowerCase() !== raw.toLowerCase() ? '<br><span class="small muted">' + esc(hit.name) + "</span>" : "") + '</td><td><span class="rating ' + cls + '">' + (r === "unknown" ? "not in database" : r) + "</span></td><td>" + (hit ? esc(hit.f) + (hit.n ? '<br><span class="small muted">' + esc(hit.n) + "</span>" : "") : '<span class="small muted">We are still adding this one.</span>') + "</td></tr>";
      });
      var total = list.length, known = total - counts.unknown;
      var score = known ? Math.round(((counts.good * 1 + counts.neutral * 0.7 + counts.caution * 0.35) / known) * 100) : 0;
      var fragrance = list.slice(0).some(function (x) { return /parfum|fragrance|aroma/i.test(x); });
      $("#inci-result").innerHTML = '<div class="grid g4" style="margin-bottom:18px"><div class="stat"><b>' + total + '</b><span>ingredients</span></div><div class="stat"><b>' + counts.good + '</b><span>beneficial</span></div><div class="stat"><b>' + (counts.caution + counts.avoid) + '</b><span>flagged</span></div><div class="stat"><b>' + score + '<small style="font-size:1rem">/100</small></b><span>gentleness score</span></div></div>' +
        (alerts.length ? '<div class="callout"><strong>Personal alerts</strong>' + alerts.join("<br>") + "</div>" : '<div class="callout" style="background:color-mix(in srgb,var(--ok) 10%,var(--surface));border-color:transparent"><strong>No personal red flags</strong>Nothing in this list conflicts with the profile you selected.</div>') +
        (fragrance ? '<p class="small">Contains fragrance — fine for many people, but the #1 cosmetic allergen.</p>' : "") +
        '<div class="table-wrap"><table><thead><tr><th>#</th><th>Ingredient</th><th>Rating</th><th>What it does</th></tr></thead><tbody>' + rows.join("") + '</tbody></table></div><p class="small muted" style="margin-top:10px">Ingredients are listed by concentration down to ~1%. Ratings are general guidance, not a safety verdict for your skin — patch test and see a dermatologist for reactions.</p>';
      $("#inci-result").hidden = false;
      feedLead("ingredient-checker", total + " ingredients, score " + score + ", alerts: " + alerts.length);
    });
  }

  /* ================= 4. Layering Checker ================= */
  var lay = $("#layer-form");
  if (lay) {
    lay.addEventListener("submit", function (e) {
      e.preventDefault();
      var picked = $$('input[name="active"]:checked', lay).map(function (x) { return x.value; });
      if (picked.length < 2) { BC.toast("Pick at least two actives"); return; }
      var out = [], C = window.BC_CONFLICTS;
      for (var i = 0; i < picked.length; i++) for (var j = i; j < picked.length; j++) {
        if (i === j) continue;
        C.forEach(function (c) { if ((c.a === picked[i] && c.b === picked[j]) || (c.b === picked[i] && c.a === picked[j])) out.push(c); });
      }
      var level = { separate: ["r-avoid", "Separate"], caution: ["r-caution", "Caution"], tip: ["r-neutral", "Tip"], ok: ["r-good", "OK together"] };
      var html = out.length ? out.map(function (c) { return '<div class="card" style="margin-bottom:10px"><span class="rating ' + level[c.level][0] + '">' + level[c.level][1] + "</span><p style=\"margin-top:.6rem\">" + esc(c.msg) + "</p></div>"; }).join("") : '<div class="card"><span class="rating r-good">Compatible</span><p style="margin-top:.6rem">No known conflicts between these. Layer thinnest to thickest, and introduce one new active at a time.</p></div>';
      html += '<div class="result-box" style="margin-top:14px"><h3>Golden layering order</h3><ol><li>Cleanser</li><li>Toner / essence (optional)</li><li>Water-based treatment serums (vitamin C, acids, niacinamide)</li><li>Retinoid (PM)</li><li>Moisturiser</li><li>Oil (optional, PM)</li><li>SPF (AM, always last)</li></ol></div>';
      $("#layer-result").innerHTML = html; $("#layer-result").hidden = false;
      feedLead("layering-checker", picked.join(" + ") + " → " + out.length + " notes");
    });
  }

  /* ================= 5. Hydration Calculator ================= */
  var hy = $("#hydration-form");
  if (hy) {
    var unit = $("#hy-unit");
    hy.addEventListener("submit", function (e) {
      e.preventDefault();
      var w = +$("#hy-weight").value; if (!w) { BC.toast("Enter your weight"); return; }
      var kg = unit.value === "lb" ? w * 0.4536 : w;
      var mins = +$("#hy-exercise").value || 0, climate = $("#hy-climate").value, state = $("#hy-state").value;
      var ml = kg * 33; // ~30–35 ml/kg baseline for total fluid from drinks
      ml += mins / 30 * 350; // ~350 ml per 30 min of exercise
      if (climate === "hot") ml += 500; if (climate === "humid") ml += 750;
      if (state === "pregnant") ml += 300; if (state === "breastfeeding") ml += 700;
      var L = ml / 1000, cups = Math.round(ml / 250);
      $("#hy-result").innerHTML = '<div class="result-box"><span class="tag accent">Daily target</span><div class="timer" style="margin:.5rem 0">' + L.toFixed(1) + ' L</div><p>≈ <b>' + cups + " cups</b> (250 ml) or <b>" + Math.round(ml / 29.57) + ' fl oz</b> from drinks per day.</p><div class="bar-row"><span>Morning</span><div class="meter"><i style="width:35%"></i></div><span>35%</span></div><div class="bar-row"><span>Afternoon</span><div class="meter"><i style="width:40%"></i></div><span>40%</span></div><div class="bar-row"><span>Evening</span><div class="meter"><i style="width:25%"></i></div><span>25%</span></div><p class="small muted" style="margin-top:12px">Estimate for healthy adults. Food supplies ~20% of water on top. Pale-yellow urine is the practical check. Heart or kidney conditions: follow your doctor\'s fluid advice. Drinking more water does not by itself fix dry skin — barrier moisturisers do that.</p></div>';
      $("#hy-result").hidden = false;
      feedLead("hydration-calculator", L.toFixed(1) + " L/day");
    });
  }

  /* ================= 6. Sunscreen Calculator + Reapply Timer ================= */
  var spf = $("#spf-form");
  if (spf) {
    spf.addEventListener("submit", function (e) {
      e.preventDefault();
      var areas = $$('input[name="area"]:checked', spf).map(function (x) { return +x.value; });
      var ml = areas.reduce(function (a, b) { return a + b; }, 0);
      var uv = +$("#uv").value, act = $("#spf-activity").value;
      var every = act === "water" ? 80 : act === "sweat" ? 80 : 120;
      var spfRec = uv >= 8 ? "SPF 50+, broad spectrum, water-resistant; seek shade 10am–4pm" : uv >= 6 ? "SPF 30–50+, broad spectrum; hat + sunglasses" : uv >= 3 ? "SPF 30+, broad spectrum" : "SPF 30 on daily exposed skin (UVA still penetrates clouds & windows)";
      $("#spf-result").innerHTML = '<div class="result-box"><div class="grid g3"><div class="stat"><b>' + ml + ' ml</b><span>per application (≈ ' + (ml / 5).toFixed(1) + ' tsp)</span></div><div class="stat"><b>' + every + ' min</b><span>reapply interval</span></div><div class="stat"><b>' + Math.ceil(ml * 3) + ' ml</b><span>for a 6-hour day outdoors</span></div></div><p style="margin-top:14px"><b>UV ' + uv + ":</b> " + spfRec + '.</p><p class="small muted">Based on the 2 mg/cm² test dose (~30 ml / a shot glass for the full adult body). Most people apply a quarter to half of this — which cuts real-world protection dramatically.</p></div>';
      $("#spf-result").hidden = false;
      $("#timer-box").hidden = false; $("#timer-box").setAttribute("data-mins", every);
      $("#timer-display").textContent = String(every).padStart(2, "0") + ":00";
      feedLead("sunscreen-calculator", ml + " ml, reapply " + every + " min, UV " + uv);
    });
    var th = null;
    $("#timer-start").addEventListener("click", function () {
      var mins = +$("#timer-box").getAttribute("data-mins") || 120, end = Date.now() + mins * 60000;
      if ("Notification" in window && Notification.permission === "default") Notification.requestPermission();
      clearInterval(th);
      th = setInterval(function () {
        var s = Math.max(0, Math.round((end - Date.now()) / 1000));
        $("#timer-display").textContent = String(Math.floor(s / 60)).padStart(2, "0") + ":" + String(s % 60).padStart(2, "0");
        if (!s) { clearInterval(th); BC.toast("Time to reapply sunscreen! ☀️"); try { if (Notification.permission === "granted") new Notification("Body.Care", { body: "Time to reapply sunscreen ☀️" }); } catch (e) {} }
      }, 1000);
      BC.toast("Timer started — keep this tab open");
    });
  }

  /* ================= 7. Body Care Score (homepage lead magnet) ================= */
  var cs = $("#care-score");
  if (cs) {
    stepper(cs, function () {
      var total = 0, max = 0, weak = [];
      $$(".step", cs).forEach(function (s) {
        var c = $("input:checked", s); max += 3; if (c) { total += +c.value; if (+c.value <= 1) weak.push(s.getAttribute("data-area")); }
      });
      var pct = Math.round(total / max * 100);
      var grade = pct >= 80 ? ["Excellent", "Your habits are ahead of ~most people. Now optimise."] : pct >= 60 ? ["Good", "Solid foundation with a few easy wins left."] : pct >= 40 ? ["Needs attention", "A few small changes will make a visible difference in 4–8 weeks."] : ["Starting point", "Great news: the biggest improvements come from the first simple steps."];
      var out = $("#care-result");
      out.innerHTML = '<div class="result-box"><span class="tag accent">Your Body Care Score</span><div class="timer" style="margin:.4rem 0">' + pct + '<small style="font-size:1.2rem">/100</small></div><h3>' + grade[0] + "</h3><p>" + grade[1] + "</p>" + (weak.length ? "<p><b>Biggest opportunities:</b> " + weak.map(esc).join(", ") + ".</p>" : "") + "<p><b>Unlock your free 30-day plan</b> tailored to these gaps ↓</p></div>";
      out.hidden = false; cs.hidden = true;
      feedLead("care-score", pct + "/100; weak: " + weak.join(", "));
    });
  }
})();
