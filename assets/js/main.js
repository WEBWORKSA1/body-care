/* Body.Care — core runtime: theme, nav, consent, ads, forms, lead capture, video, donate, contest. */
(function () {
  "use strict";
  var C = window.BC_CONFIG || {};
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var store = {
    get: function (k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
    set: function (k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  };
  var ss = {
    get: function (k) { try { return sessionStorage.getItem(k); } catch (e) { return null; } },
    set: function (k, v) { try { sessionStorage.setItem(k, v); } catch (e) {} }
  };
  window.BC = { $: $, $$: $$, store: store };

  /* ---------- Theme ---------- */
  var saved = store.get("bc-theme");
  if (saved) document.documentElement.setAttribute("data-theme", saved);
  $$("[data-theme-toggle]").forEach(function (b) {
    b.addEventListener("click", function () {
      var cur = document.documentElement.getAttribute("data-theme");
      var dark = cur ? cur === "dark" : matchMedia("(prefers-color-scheme: dark)").matches;
      var next = dark ? "light" : "dark";
      document.documentElement.setAttribute("data-theme", next);
      store.set("bc-theme", next);
    });
  });

  /* ---------- Mobile menu ---------- */
  var burger = $(".burger"), mm = $(".mobile-menu");
  if (burger && mm) burger.addEventListener("click", function () {
    var open = mm.classList.toggle("open");
    burger.setAttribute("aria-expanded", open ? "true" : "false");
  });

  /* ---------- Toast ---------- */
  function toast(msg) {
    var t = $(".toast");
    if (!t) { t = document.createElement("div"); t.className = "toast"; t.setAttribute("role", "status"); document.body.appendChild(t); }
    t.textContent = msg; t.classList.add("show");
    clearTimeout(t._h); t._h = setTimeout(function () { t.classList.remove("show"); }, 3200);
  }
  window.BC.toast = toast;

  /* ---------- UTM / attribution capture (lead source tracking) ---------- */
  (function () {
    var p = new URLSearchParams(location.search), keep = {};
    ["utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content", "ref", "gclid"].forEach(function (k) { if (p.get(k)) keep[k] = p.get(k); });
    if (Object.keys(keep).length) ss.set("bc-attr", JSON.stringify(keep));
    if (!ss.get("bc-landing")) ss.set("bc-landing", location.pathname);
  })();

  /* ---------- Consent + AdSense + GA4 ---------- */
  function loadScript(src, attrs) {
    var s = document.createElement("script"); s.async = true; s.src = src;
    Object.keys(attrs || {}).forEach(function (k) { s.setAttribute(k, attrs[k]); });
    document.head.appendChild(s);
  }
  function initAds(personalised) {
    if (!C.adsenseClient) return; // placeholders stay visible for layout until configured
    window.adsbygoogle = window.adsbygoogle || [];
    if (!personalised) window.adsbygoogle.requestNonPersonalizedAds = 1;
    loadScript("https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=" + C.adsenseClient, { crossorigin: "anonymous" });
    $$(".ad-slot[data-slot]").forEach(function (el) {
      var id = (C.adSlots || {})[el.getAttribute("data-slot")];
      el.classList.add("live");
      var ins = document.createElement("ins");
      ins.className = "adsbygoogle"; ins.style.display = "block";
      ins.setAttribute("data-ad-client", C.adsenseClient);
      if (id) ins.setAttribute("data-ad-slot", id);
      ins.setAttribute("data-ad-format", el.getAttribute("data-format") || "auto");
      ins.setAttribute("data-full-width-responsive", "true");
      el.appendChild(ins);
      try { (window.adsbygoogle = window.adsbygoogle || []).push({}); } catch (e) {}
    });
  }
  function initGA() {
    if (!C.ga4Id) return;
    loadScript("https://www.googletagmanager.com/gtag/js?id=" + C.ga4Id);
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { dataLayer.push(arguments); };
    gtag("js", new Date()); gtag("config", C.ga4Id);
  }
  function track(name, params) { if (window.gtag) window.gtag("event", name, params || {}); }
  window.BC.track = track;

  var consent = store.get("bc-consent");
  var banner = $(".cookie");
  if (consent) { initAds(consent === "all"); if (consent === "all") initGA(); }
  else if (banner) {
    setTimeout(function () { banner.classList.add("show"); }, 900);
    banner.addEventListener("click", function (e) {
      var v = e.target.getAttribute("data-consent"); if (!v) return;
      store.set("bc-consent", v); banner.classList.remove("show");
      initAds(v === "all"); if (v === "all") initGA();
    });
  }

  /* ---------- Forms: one handler for every lead form ---------- */
  function endpointFor(kind) { var f = C.forms || {}; return f[kind] || f.default || ""; }
  function serialize(form) {
    var data = {}, fd = new FormData(form);
    fd.forEach(function (v, k) { if (k === "_gotcha") return; data[k] = data[k] ? [].concat(data[k], v) : v; });
    data._form = form.getAttribute("data-form");
    data._page = location.pathname;
    data._landing = ss.get("bc-landing") || "";
    data._submitted = new Date().toISOString();
    try { Object.assign(data, JSON.parse(ss.get("bc-attr") || "{}")); } catch (e) {}
    return data;
  }
  function mailtoFallback(kind, data) {
    var body = Object.keys(data).map(function (k) { return k + ": " + [].concat(data[k]).join(", "); }).join("\n");
    location.href = "mailto:" + (C.contactEmail || "") + "?subject=" + encodeURIComponent("[Body.Care] " + kind + " submission") + "&body=" + encodeURIComponent(body);
  }
  $$("form[data-form]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var kind = form.getAttribute("data-form");
      var msg = $(".form-msg", form) || form.parentNode.querySelector(".form-msg");
      if (form._gotcha && form._gotcha.value) return; // bot
      var hp = form.querySelector('[name="_gotcha"]'); if (hp && hp.value) return;
      if (!form.checkValidity()) { form.reportValidity(); return; }
      var data = serialize(form);
      if (typeof form._enrich === "function") form._enrich(data);
      var btn = form.querySelector('[type="submit"]'); if (btn) { btn.disabled = true; btn._t = btn.textContent; btn.textContent = "Sending…"; }
      var url = endpointFor(kind);
      var done = function (ok) {
        if (btn) { btn.disabled = false; btn.textContent = btn._t; }
        if (msg) { msg.className = "form-msg " + (ok ? "ok" : "err"); msg.textContent = ok ? (form.getAttribute("data-success") || "Thanks! You're in — check your inbox.") : "Something went wrong. Please try again or email " + C.contactEmail + "."; }
        if (ok) { track("generate_lead", { form: kind }); store.set("bc-lead", "1"); form.reset(); form.dispatchEvent(new CustomEvent("bc:success", { detail: data })); }
      };
      if (!url) { mailtoFallback(kind, data); done(true); return; }
      fetch(url, { method: "POST", headers: { "Content-Type": "application/json", Accept: "application/json" }, body: JSON.stringify(data) })
        .then(function (r) { done(r.ok); }).catch(function () { done(false); });
    });
  });

  /* ---------- Exit-intent / timed lead modal (once per 7 days, never after conversion) ---------- */
  var modal = $("#lead-modal");
  if (modal) {
    var last = +store.get("bc-modal") || 0, converted = store.get("bc-lead");
    var eligible = !converted && Date.now() - last > 7 * 864e5 && !document.body.hasAttribute("data-no-popup");
    var show = function () { if (!eligible) return; eligible = false; store.set("bc-modal", Date.now()); modal.classList.add("show"); track("lead_modal_view"); };
    if (eligible) {
      document.addEventListener("mouseout", function (e) { if (!e.relatedTarget && e.clientY < 10) show(); });
      setTimeout(show, 45000);
      var scrolled = false;
      window.addEventListener("scroll", function () { if (!scrolled && scrollY / (document.body.scrollHeight - innerHeight) > 0.6) { scrolled = true; setTimeout(show, 1500); } }, { passive: true });
    }
    modal.addEventListener("click", function (e) { if (e.target === modal || e.target.closest(".modal-close")) modal.classList.remove("show"); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") modal.classList.remove("show"); });
  }

  /* ---------- Sticky mobile CTA ---------- */
  var sticky = $(".sticky-cta");
  if (sticky) window.addEventListener("scroll", function () { sticky.classList.toggle("show", scrollY > 700); }, { passive: true });

  /* ---------- Reveal on scroll ---------- */
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (en) { en.forEach(function (x) { if (x.isIntersecting) { x.target.classList.add("in"); io.unobserve(x.target); } }); }, { rootMargin: "0px 0px -8% 0px" });
    $$(".reveal").forEach(function (el) { io.observe(el); });
  } else $$(".reveal").forEach(function (el) { el.classList.add("in"); });

  /* ---------- YouTube facades (fast pages; iframe only on click) ---------- */
  function mountVideo(el) {
    var id = el.getAttribute("data-yt");
    el.innerHTML = '<iframe src="https://www.youtube-nocookie.com/embed/' + encodeURIComponent(id) + '?autoplay=1&rel=0" title="' + (el.getAttribute("data-title") || "Video") + '" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>';
    track("video_play", { id: id });
  }
  function renderVideos() {
    var box = $("[data-videos]"); if (!box) return;
    var list = C.videos || [], limit = +box.getAttribute("data-limit") || list.length, cat = box.getAttribute("data-cat") || "All";
    var items = list.filter(function (v) { return cat === "All" || v.cat === cat; }).slice(0, limit);
    box.innerHTML = items.map(function (v) {
      return '<article class="card" style="padding:14px"><div class="video" data-yt="' + v.id + '" data-title="' + v.title.replace(/"/g, "") + '" role="button" tabindex="0" aria-label="Play: ' + v.title.replace(/"/g, "") + '"><img loading="lazy" src="https://i.ytimg.com/vi/' + v.id + '/hqdefault.jpg" alt=""><button tabindex="-1" aria-hidden="true">▶</button></div><div style="padding:12px 4px 2px"><span class="tag">' + v.cat + '</span><h3 style="font-size:1.05rem;margin:.6rem 0 .2rem">' + v.title + '</h3><p class="small muted">' + (v.src || "") + "</p></div></article>";
    }).join("");
  }
  renderVideos();
  $$("[data-video-filter]").forEach(function (b) {
    b.addEventListener("click", function () {
      $$("[data-video-filter]").forEach(function (x) { x.classList.remove("active"); }); b.classList.add("active");
      var box = $("[data-videos]"); box.setAttribute("data-cat", b.getAttribute("data-video-filter")); renderVideos();
    });
  });
  document.addEventListener("click", function (e) { var v = e.target.closest(".video[data-yt]"); if (v && !v.querySelector("iframe")) mountVideo(v); });
  document.addEventListener("keydown", function (e) { var v = e.target.closest && e.target.closest(".video[data-yt]"); if (v && (e.key === "Enter" || e.key === " ") && !v.querySelector("iframe")) { e.preventDefault(); mountVideo(v); } });
  $$("[data-yt-channel]").forEach(function (a) { a.href = C.youtubeChannel || "#"; });

  /* ---------- Affiliate tagging ---------- */
  if (C.amazonTag) $$('a[href*="amazon."]').forEach(function (a) {
    try { var u = new URL(a.href); u.searchParams.set("tag", C.amazonTag); a.href = u.toString(); } catch (e) {}
  });
  $$("a[data-aff]").forEach(function (a) { a.addEventListener("click", function () { track("affiliate_click", { item: a.getAttribute("data-aff") }); }); });

  /* ---------- Social links ---------- */
  $$("[data-social]").forEach(function (a) { var u = (C.social || {})[a.getAttribute("data-social")]; if (u) a.href = u; else a.remove(); });

  /* ---------- Share ---------- */
  $$("[data-share]").forEach(function (b) {
    b.addEventListener("click", function () {
      var t = document.title, u = location.href, kind = b.getAttribute("data-share");
      if (kind === "native" && navigator.share) { navigator.share({ title: t, url: u }).catch(function () {}); return; }
      if (kind === "copy" || kind === "native") { (navigator.clipboard ? navigator.clipboard.writeText(u) : Promise.reject()).then(function () { toast("Link copied"); }, function () { prompt("Copy this link:", u); }); return; }
      var map = { x: "https://x.com/intent/tweet?url=", facebook: "https://www.facebook.com/sharer/sharer.php?u=", whatsapp: "https://wa.me/?text=", pinterest: "https://pinterest.com/pin/create/button/?url=" };
      window.open(map[kind] + encodeURIComponent(u), "_blank", "noopener,width=640,height=560");
      track("share", { method: kind });
    });
  });

  /* ---------- Donations ---------- */
  var D = C.donate || {};
  var fmt = function (n) { try { return new Intl.NumberFormat(undefined, { style: "currency", currency: D.currency || "USD", maximumFractionDigits: 0 }).format(n); } catch (e) { return "$" + n; } };
  $$("[data-donate-link]").forEach(function (a) { var u = D[a.getAttribute("data-donate-link")]; if (u) a.href = u; else a.style.display = "none"; });
  var meter = $("[data-goal-meter]");
  if (meter) {
    var pct = D.goal ? Math.min(100, Math.round((D.raised || 0) / D.goal * 100)) : 0;
    $("i", meter).style.width = Math.max(pct, 2) + "%";
    var lab = $("[data-goal-label]"); if (lab) lab.textContent = fmt(D.raised || 0) + " raised of " + fmt(D.goal) + " goal (" + pct + "%)";
  }
  var dform = $("#donate-form");
  if (dform) {
    var freq = "once";
    $$(".seg button", dform).forEach(function (b) {
      b.addEventListener("click", function () { $$(".seg button", dform).forEach(function (x) { x.classList.remove("active"); x.setAttribute("aria-pressed", "false"); }); b.classList.add("active"); b.setAttribute("aria-pressed", "true"); freq = b.getAttribute("data-freq"); upd(); });
    });
    var custom = $("#custom-amount", dform), out = $("#donate-summary");
    function amount() { if (custom.value) return +custom.value; var r = $('input[name="amt"]:checked', dform); return r ? +r.value : 0; }
    function upd() { var a = amount(); out.textContent = a ? "You're giving " + fmt(a) + (freq === "monthly" ? " every month" : " once") + ". Thank you!" : "Choose an amount"; }
    dform.addEventListener("input", function (e) { if (e.target.name === "amt") custom.value = ""; upd(); });
    dform.addEventListener("submit", function (e) {
      e.preventDefault(); var a = amount(); if (!a) { toast("Choose an amount first"); return; }
      track("begin_checkout", { value: a, currency: D.currency, freq: freq });
      var link = freq === "monthly" ? (D.stripeMonthlyLink || D.patreon || D.githubSponsors) : (D.stripeLink || D.paypal || D.kofi || D.buymeacoffee || D.githubSponsors);
      if (link) { var u = link; if (/paypal\.com\/donate/.test(u)) u += (u.indexOf("?") > -1 ? "&" : "?") + "amount=" + a; window.open(u, "_blank", "noopener"); }
      else location.href = "mailto:" + C.contactEmail + "?subject=" + encodeURIComponent("Body.Care support pledge: " + fmt(a) + " (" + freq + ")");
    });
    upd();
  }

  /* ---------- Contest countdown ---------- */
  var cd = $("[data-countdown]");
  if (cd) {
    var ct = C.contest || {}, end = ct.endsISO ? new Date(ct.endsISO) : (function () { var d = new Date(); return new Date(d.getFullYear(), d.getMonth() + 1, 1, 0, 0, 0); })();
    $$("[data-contest-title]").forEach(function (el) { el.textContent = ct.title || el.textContent; });
    $$("[data-contest-prize]").forEach(function (el) { el.textContent = ct.prize || el.textContent; });
    $$("[data-contest-end]").forEach(function (el) { el.textContent = end.toLocaleDateString(undefined, { month: "long", day: "numeric", year: "numeric" }); });
    var tick = function () {
      var s = Math.max(0, Math.floor((end - Date.now()) / 1000));
      var v = [Math.floor(s / 86400), Math.floor(s % 86400 / 3600), Math.floor(s % 3600 / 60), s % 60];
      $$("b", cd).forEach(function (b, i) { b.textContent = String(v[i]).padStart(2, "0"); });
    };
    tick(); setInterval(tick, 1000);
  }
  /* Referral bonus entries: every contest entrant gets a personal link */
  var cform = $('form[data-form="contest"]');
  if (cform) {
    var ref = new URLSearchParams(location.search).get("ref"); if (ref && cform.referrer) cform.referrer.value = ref;
    cform.addEventListener("bc:success", function (e) {
      var code = (e.detail.email || "friend").split("@")[0].replace(/[^a-z0-9]/gi, "").slice(0, 12) + Math.random().toString(36).slice(2, 6);
      var link = location.origin + location.pathname + "?ref=" + code;
      var box = $("#ref-box"); if (box) { box.hidden = false; $("input", box).value = link; }
    });
  }

  /* ---------- Site search (client-side index) ---------- */
  var sInput = $("#site-search");
  if (sInput) {
    var base = document.documentElement.getAttribute("data-base") || "";
    var idx = null, res = $("#search-results");
    var load = function () { return idx ? Promise.resolve(idx) : fetch(base + "search-index.json").then(function (r) { return r.json(); }).then(function (j) { idx = j; return j; }); };
    var run = function () {
      var q = sInput.value.trim().toLowerCase();
      if (q.length < 2) { res.innerHTML = ""; return; }
      load().then(function (list) {
        var terms = q.split(/\s+/);
        var hits = list.map(function (p) { var hay = (p.t + " " + p.d + " " + p.k).toLowerCase(), sc = 0; terms.forEach(function (t) { if (hay.indexOf(t) > -1) sc += p.t.toLowerCase().indexOf(t) > -1 ? 3 : 1; }); return { p: p, sc: sc }; })
          .filter(function (x) { return x.sc >= terms.length; }).sort(function (a, b) { return b.sc - a.sc; }).slice(0, 12);
        res.innerHTML = hits.length ? hits.map(function (h) { return '<a class="card" href="' + base + h.p.u + '"><span class="tag">' + h.p.c + '</span><h3 style="margin-top:.6rem">' + h.p.t + '</h3><p>' + h.p.d + "</p></a>"; }).join("") : '<p class="muted">No results. Try "sunscreen", "retinol", "dry skin" or "hair".</p>';
        track("search", { search_term: q });
      });
    };
    sInput.addEventListener("input", run);
    var q0 = new URLSearchParams(location.search).get("q"); if (q0) { sInput.value = q0; run(); }
  }

  /* ---------- Library filter ---------- */
  var lib = $("[data-library]");
  if (lib) {
    var btns = $$("[data-filter]"), fInput = $("#lib-filter");
    var apply = function () {
      var act = ($("[data-filter].active") || {}).getAttribute ? $("[data-filter].active").getAttribute("data-filter") : "all";
      var q = (fInput && fInput.value || "").toLowerCase(), shown = 0;
      $$("[data-cat]", lib).forEach(function (c) {
        var ok = (act === "all" || c.getAttribute("data-cat") === act) && (!q || c.textContent.toLowerCase().indexOf(q) > -1);
        c.style.display = ok ? "" : "none"; if (ok) shown++;
      });
      var e = $("#lib-empty"); if (e) e.hidden = shown > 0;
    };
    btns.forEach(function (b) { b.addEventListener("click", function () { btns.forEach(function (x) { x.classList.remove("active"); }); b.classList.add("active"); apply(); }); });
    if (fInput) fInput.addEventListener("input", apply);
    var hash = location.hash.slice(1); if (hash) { var hb = $('[data-filter="' + hash + '"]'); if (hb) hb.click(); }
  }

  /* ---------- Reading progress + year ---------- */
  var rp = $("#read-progress");
  if (rp) window.addEventListener("scroll", function () { var h = document.documentElement; rp.style.width = (h.scrollTop / (h.scrollHeight - h.clientHeight) * 100) + "%"; }, { passive: true });
  $$("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });

  /* ---------- PWA ---------- */
  if ("serviceWorker" in navigator && location.protocol === "https:") {
    window.addEventListener("load", function () { navigator.serviceWorker.register((document.documentElement.getAttribute("data-base") || "") + "sw.js").catch(function () {}); });
  }
})();
