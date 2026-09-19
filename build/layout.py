# -*- coding: utf-8 -*-
"""Shared layout: <head>, header, footer, overlays. Every page goes through page()."""
import json, html

SITE = "https://body.care"
NAME = "Body.Care"
TAGLINE = "Science-first care for your whole body"
VERSION = "1.0.0"
# JEKYLL=True: pages are emitted as front matter + body and wrapped by _layouts/default.html
# (GitHub Pages builds them server-side, so no Actions workflow is needed). False: full static HTML.
JEKYLL = True

LOGO = ('<svg viewBox="0 0 40 40" aria-hidden="true"><defs><linearGradient id="lg" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="#0f5e59"/><stop offset="1" stop-color="#e8674a"/></linearGradient></defs>'
        '<rect width="40" height="40" rx="12" fill="url(#lg)"/>'
        '<path d="M20 30c-6-4-10-7.6-10-12.2A5.4 5.4 0 0 1 20 14.6a5.4 5.4 0 0 1 10 3.2C30 22.4 26 26 20 30z" fill="#fff"/>'
        '<circle cx="20" cy="20" r="2.4" fill="#e8674a"/></svg>')

I = {
 "sun": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>',
 "menu": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M3 6h18M3 12h18M3 18h18"/></svg>',
 "search": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>',
 "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"><path d="M5 12l5 5L20 7"/></svg>',
 "x": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M6 6l12 12M18 6 6 18"/></svg>',
 "ig": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor"/></svg>',
 "yt": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M23 7.2a3 3 0 0 0-2.1-2.1C19 4.6 12 4.6 12 4.6s-7 0-8.9.5A3 3 0 0 0 1 7.2 31 31 0 0 0 .5 12a31 31 0 0 0 .5 4.8 3 3 0 0 0 2.1 2.1c1.9.5 8.9.5 8.9.5s7 0 8.9-.5a3 3 0 0 0 2.1-2.1 31 31 0 0 0 .5-4.8 31 31 0 0 0-.5-4.8zM9.8 15.1V8.9l5.8 3.1-5.8 3.1z"/></svg>',
 "tt": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M16.5 3a4.8 4.8 0 0 0 4 4.4v3.2a8 8 0 0 1-4-1.2v6.3A5.7 5.7 0 1 1 10.8 10v3.3a2.5 2.5 0 1 0 2.5 2.5V3h3.2z"/></svg>',
 "pin": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 0 0-3.6 19.3c-.1-.8-.2-2 0-2.9l1.3-5.4s-.3-.7-.3-1.6c0-1.5.9-2.7 2-2.7.9 0 1.4.7 1.4 1.5 0 .9-.6 2.3-.9 3.6-.3 1.1.5 2 1.6 2 1.9 0 3.4-2 3.4-5 0-2.6-1.9-4.4-4.5-4.4-3.1 0-4.9 2.3-4.9 4.7 0 .9.4 1.9.8 2.5l.1.4-.3 1.2c0 .2-.2.3-.4.2-1.4-.6-2.2-2.6-2.2-4.2 0-3.4 2.5-6.6 7.2-6.6 3.8 0 6.7 2.7 6.7 6.3 0 3.8-2.4 6.8-5.7 6.8-1.1 0-2.2-.6-2.5-1.3l-.7 2.6c-.2 1-.9 2.2-1.4 2.9A10 10 0 1 0 12 2z"/></svg>',
 "xs": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.8 3h3.1l-6.8 7.8L22 21h-6.2l-4.9-6.4L5.3 21H2.2l7.3-8.3L2 3h6.4l4.4 5.8L17.8 3zm-1.1 16.2h1.7L7.4 4.7H5.6l11.1 14.5z"/></svg>',
}

NAV = [("library.html", "Guides"), ("tools/index.html", "Tools"), ("videos.html", "Videos"), ("picks.html", "Picks"),
       ("contests.html", "Giveaways"), ("support.html", "Support")]

def e(s):
    return html.escape(str(s), quote=True)

def head(title, desc, path, base, schema=None, og_type="website", extra=""):
    canon = SITE + "/" + path.replace("index.html", "")
    full_title = title if NAME in title else f"{title} | {NAME}"
    sch = ""
    for s in (schema or []):
        sch += '<script type="application/ld+json">' + json.dumps(s, ensure_ascii=False) + "</script>\n"
    return f"""<!doctype html>
<html lang="en" data-base="{base}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(full_title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{canon}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="theme-color" content="#0f5e59">
<meta property="og:site_name" content="{NAME}">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{e(full_title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{SITE}/assets/img/og-image.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{base}assets/img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{base}assets/img/favicon.svg">
<link rel="manifest" href="{base}manifest.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{base}assets/css/main.css?v={VERSION}">
<script>try{{var t=localStorage.getItem("bc-theme");if(t)document.documentElement.setAttribute("data-theme",t)}}catch(e){{}}</script>
<script src="{base}assets/js/config.js?v={VERSION}"></script>
{sch}{extra}</head>
"""

def header(base, active=""):
    cur = ' aria-current="page"'
    items = "".join(
        f'<li><a href="{base}{h}"{cur if h == active else ""}>{t}</a></li>' for h, t in NAV)
    mob = "".join(f'<a href="{base}{h}">{t}</a>' for h, t in NAV + [("advertise.html", "Advertise & Partner"), ("careers.html", "Careers"), ("about.html", "About"), ("contact.html", "Contact"), ("search.html", "Search")])
    return f"""<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
 <div class="wrap nav">
  <a class="logo" href="{base}index.html" aria-label="Body.Care home">{LOGO}<span>Body<b>.</b>Care</span></a>
  <ul class="menu">{items}</ul>
  <div class="nav-actions">
   <a class="icon-btn search-btn" href="{base}search.html" aria-label="Search">{I['search']}</a>
   <button class="icon-btn" data-theme-toggle aria-label="Toggle dark mode">{I['sun']}</button>
   <a class="btn btn-primary btn-sm" href="{base}free-plan.html">Free Plan</a>
   <button class="icon-btn burger" aria-label="Menu" aria-expanded="false">{I['menu']}</button>
  </div>
 </div>
 <nav class="mobile-menu" aria-label="Mobile">{mob}<a href="{base}free-plan.html" style="color:var(--accent)">Get my free plan →</a></nav>
</header>
"""

def newsletter_form(base, where="footer"):
    return f"""<form class="newsletter" data-form="newsletter" data-success="Welcome aboard! Your first issue lands this week.">
 <input type="text" name="_gotcha" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
 <input type="hidden" name="source" value="{where}">
 <label class="hp" for="nl-{where}">Email</label>
 <input id="nl-{where}" type="email" name="email" required placeholder="you@email.com" autocomplete="email">
 <button class="btn btn-primary" type="submit">Subscribe</button>
 <p class="form-msg" role="status" style="flex-basis:100%"></p>
</form>"""

def footer(base, popup=True, jekyll=False):
    cats = "".join(f'<li><a href="{base}library.html#{k}">{n}</a></li>' for k, n, _ in __import__("content").CATEGORIES[:6])
    modal = f"""<div class="modal" id="lead-modal" role="dialog" aria-modal="true" aria-labelledby="lm-title">
 <div class="modal-box">
  <button class="icon-btn modal-close" aria-label="Close">{I['x']}</button>
  <span class="eyebrow">Free · 2 minutes</span>
  <h2 id="lm-title" style="font-size:1.7rem">Get your personalised 30-day body care plan</h2>
  <p class="muted">A routine built for your skin, hair and lifestyle — plus our weekly 3-minute science digest. No spam, unsubscribe anytime.</p>
  <form class="form" data-form="plan" data-success="Done! Check your inbox for your plan.">
   <input type="text" name="_gotcha" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
   <input type="hidden" name="source" value="exit-modal">
   <div class="field"><label for="lm-name">First name</label><input id="lm-name" name="name" type="text" required autocomplete="given-name"></div>
   <div class="field"><label for="lm-email">Email</label><input id="lm-email" name="email" type="email" required autocomplete="email"></div>
   <label class="consent"><input type="checkbox" name="consent" required> I agree to receive emails and accept the <a href="{base}privacy.html">privacy policy</a>.</label>
   <button class="btn btn-primary btn-block" type="submit">Send my free plan</button>
   <p class="form-msg" role="status"></p>
  </form>
 </div>
</div>""" if popup else ""
    if jekyll:
        modal = "{% unless page.nopopup %}" + modal + "{% endunless %}"
    return f"""
<footer class="site-footer">
 <div class="wrap">
  <div class="foot-grid">
   <div style="grid-column:span 2;min-width:0">
    <a class="logo" href="{base}index.html">{LOGO}<span>Body<b>.</b>Care</span></a>
    <p style="margin-top:14px;max-width:40ch">{TAGLINE}. Independent, evidence-based guides, free tools and videos for skin, hair, body and everyday wellbeing.</p>
    <p style="font-weight:600;color:#fff;margin-bottom:8px">The 3-minute Sunday digest</p>
    {newsletter_form(base)}
    <div class="socials">
     <a data-social="instagram" aria-label="Instagram" rel="noopener" target="_blank">{I['ig']}</a>
     <a data-social="youtube" aria-label="YouTube" rel="noopener" target="_blank">{I['yt']}</a>
     <a data-social="tiktok" aria-label="TikTok" rel="noopener" target="_blank">{I['tt']}</a>
     <a data-social="pinterest" aria-label="Pinterest" rel="noopener" target="_blank">{I['pin']}</a>
     <a data-social="x" aria-label="X" rel="noopener" target="_blank">{I['xs']}</a>
    </div>
   </div>
   <div><h4>Guides</h4><ul>{cats}</ul></div>
   <div><h4>Free tools</h4><ul>
    <li><a href="{base}tools/skin-quiz.html">Skin Type Quiz</a></li><li><a href="{base}tools/routine-builder.html">Routine Builder</a></li>
    <li><a href="{base}tools/ingredient-checker.html">Ingredient Checker</a></li><li><a href="{base}tools/layering-checker.html">Layering Checker</a></li>
    <li><a href="{base}tools/sunscreen-calculator.html">Sunscreen Calculator</a></li><li><a href="{base}tools/hydration-calculator.html">Hydration Calculator</a></li></ul></div>
   <div><h4>Body.Care</h4><ul>
    <li><a href="{base}about.html">About & editorial policy</a></li><li><a href="{base}free-plan.html">Free personal plan</a></li>
    <li><a href="{base}support.html">Support us / donate</a></li><li><a href="{base}contests.html">Giveaways & Awards</a></li>
    <li><a href="{base}advertise.html">Advertise & partner</a></li><li><a href="{base}careers.html">Careers & creators</a></li>
    <li><a href="{base}contact.html">Contact</a></li></ul></div>
  </div>
  <div class="foot-bottom">
   <span>© <span data-year></span> Body.Care. Educational content only — not a substitute for professional medical advice.</span>
   <span><a href="{base}privacy.html">Privacy</a> · <a href="{base}terms.html">Terms</a> · <a href="{base}disclaimer.html">Medical & affiliate disclaimer</a></span>
  </div>
 </div>
</footer>
<div class="cookie" role="dialog" aria-label="Cookie consent">
 <b>Cookies & ads</b>
 <p class="small" style="margin:.4rem 0 0">We use cookies for analytics and to show ads that keep Body.Care free. Choose "Essential only" for non-personalised ads. <a href="{base}privacy.html">Learn more</a>.</p>
 <div class="row"><button class="btn btn-brand btn-sm" data-consent="all">Accept all</button><button class="btn btn-ghost btn-sm" data-consent="essential">Essential only</button></div>
</div>
{modal}
<div class="sticky-cta"><a class="btn btn-primary" href="{base}free-plan.html">Get my free body care plan →</a></div>
<script src="{base}assets/js/main.js?v={VERSION}" defer></script>
"""

def page(path, title, desc, body_html, active="", schema=None, scripts=(), og_type="website", popup=True, body_attr="", extra_fm=None):
    depth = path.count("/")
    base = "../" * depth
    sch = [{"@context": "https://schema.org", "@type": "WebSite", "name": NAME, "url": SITE,
            "potentialAction": {"@type": "SearchAction", "target": SITE + "/search.html?q={q}", "query-input": "required name=q"}}] if path == "index.html" else []
    sch += (schema or [])
    if JEKYLL:
        return jekyll_page(path, title, desc, body_html.replace("{base}", base), base, active, sch, scripts, og_type, popup, body_attr, extra_fm)
    out = head(title, desc, path, base, sch, og_type) + header(base, active).replace("<body>", f"<body{(' ' + body_attr) if body_attr else ''}>", 1)
    out += '<main id="main">' + body_html.replace("{base}", base) + "</main>" + footer(base, popup)
    for s in scripts:
        out += f'<script src="{base}assets/js/{s}?v={VERSION}" defer></script>\n'
    out += "</body>\n</html>\n"
    return out

def ad(slot="inArticle", fmt="auto"):
    return f'<div class="ad-slot" data-slot="{slot}" data-format="{fmt}"></div>'

def breadcrumb(base, trail):
    parts = [f'<a href="{base}index.html">Home</a>'] + [f'<a href="{base}{h}">{e(t)}</a>' if h else e(t) for h, t in trail]
    return '<nav class="breadcrumb" aria-label="Breadcrumb">' + " / ".join(parts) + "</nav>"

def crumb_schema(trail):
    items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"}]
    for i, (h, t) in enumerate(trail):
        it = {"@type": "ListItem", "position": i + 2, "name": t}
        if h: it["item"] = SITE + "/" + h
        items.append(it)
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}

def plan_form(base, tool, heading="Email me this result + a free 30-day plan", sub="We'll send your result, a printable routine and weekly tips. Free, no spam."):
    return f"""<section class="lead-band" style="margin-top:28px" data-lead-after>
 <div><span class="eyebrow" style="color:var(--accent-2)">Free · instant</span><h2>{heading}</h2><p>{sub}</p>
  <ul class="checklist"><li>Your personalised result, saved</li><li>30-day step-by-step plan</li><li>Member-only product deals & giveaway entries</li></ul></div>
 <form class="form on-dark" data-form="plan" data-tool="{tool}" data-success="Sent! Check your inbox (and promotions tab).">
  <input type="text" name="_gotcha" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
  <input type="hidden" name="source" value="tool:{tool}"><input type="hidden" name="result" value="">
  <div class="form-row two"><div class="field"><label for="pf-n-{tool}">First name</label><input id="pf-n-{tool}" name="name" type="text" required autocomplete="given-name"></div>
  <div class="field"><label for="pf-e-{tool}">Email</label><input id="pf-e-{tool}" name="email" type="email" required autocomplete="email"></div></div>
  <label class="consent"><input type="checkbox" name="consent" required> Send me my plan and the weekly digest. I accept the <a href="{base}privacy.html" style="color:#fff">privacy policy</a>.</label>
  <button class="btn btn-primary btn-block" type="submit">Send my free plan →</button>
  <p class="form-msg" role="status"></p>
 </form>
</section>"""


# ------------------------------------------------------------------ Jekyll output
def _q(v):
    """YAML double-quoted scalar (JSON strings are valid YAML)."""
    return json.dumps(v, ensure_ascii=False)

def jekyll_page(path, title, desc, body_html, base, active, schema, scripts, og_type, popup, body_attr, extra_fm=None):
    full_title = title if NAME in title else f"{title} | {NAME}"
    fm = ["---", "layout: default", f"full_title: {_q(full_title)}", f"description: {_q(desc)}",
          f"canon_path: {_q(path.replace('index.html', ''))}", f"base: {_q(base)}", f"og_type: {_q(og_type)}",
          f"active: {_q(active)}"]
    if body_attr: fm.append(f"body_attr: {_q(body_attr)}")
    if not popup: fm.append("nopopup: true")
    if scripts: fm.append("scripts: [" + ", ".join(_q(x) for x in scripts) + "]")
    if schema:
        fm.append("schema: |")
        for sc in schema:
            fm.append('  <script type="application/ld+json">' + json.dumps(sc, ensure_ascii=False) + "</script>")
    for k, v in (extra_fm or {}).items():
        fm.append(f"{k}: {_q(v) if isinstance(v, str) else json.dumps(v)}")
    fm.append("---")
    return "\n".join(fm) + "\n{% raw %}" + body_html + "{% endraw %}\n"

def jekyll_layout():
    """Build _layouts/default.html from the same head/header/footer functions (single source of truth)."""
    B = "@@B@@"
    h = head("@@T@@", "@@D@@", "@@P@@", B, [], "@@OG@@", "@@SCHEMA@@")
    h = h.replace("<title>@@T@@ | Body.Care</title>", "<title>{{ page.full_title | escape }}</title>")
    h = h.replace('content="@@T@@ | Body.Care"', 'content="{{ page.full_title | escape }}"')
    h = h.replace('content="@@D@@"', 'content="{{ page.description | escape }}"')
    h = h.replace(SITE + "/@@P@@", SITE + "/{{ page.canon_path }}")
    h = h.replace('content="@@OG@@"', 'content="{{ page.og_type }}"')
    h = h.replace("@@SCHEMA@@", "{{ page.schema }}{{ page.extra_head_end }}")
    h = h.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n{{ page.extra_head }}', 1)
    h = h.replace('<meta name="robots" content="index,follow,max-image-preview:large">',
                  '<meta name="robots" content="{% if page.noindex %}noindex{% else %}index,follow,max-image-preview:large{% endif %}">')
    hd = header(B, "")
    hd = hd.replace("<body>", "<body{% if page.body_attr %} {{ page.body_attr }}{% endif %}>", 1)
    for href, _t in NAV:
        hd = hd.replace(f'<li><a href="{B}{href}">', f'<li><a href="{B}{href}"{{% if page.active == "{href}" %}} aria-current="page"{{% endif %}}>', 1)
    ft = footer(B, True, jekyll=True)
    out = h + hd + '<main id="main">{{ content }}</main>' + ft
    out += '{% for s in page.scripts %}<script src="' + B + 'assets/js/{{ s }}?v=' + VERSION + '" defer></script>\n{% endfor %}'
    out += "</body>\n</html>\n"
    return out.replace(B, "{{ page.base }}")
