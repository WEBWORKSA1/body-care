# -*- coding: utf-8 -*-
"""Body.Care static site generator.
Usage:  python3 build/build.py      (writes the site into the repo root)
Add articles in build/content.py, tools/pages in pages_*.py, then rebuild and push."""
import os, sys, json, datetime
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from layout import SITE, LOGO
from content import ARTICLES, CATEGORIES
import pages_main as M, pages_more as P

def w(rel, text):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

pages = {
    "index.html": M.home(), "library.html": M.library(), "videos.html": M.videos(), "free-plan.html": M.free_plan(),
    "picks.html": M.picks(), "search.html": M.search(),
    "tools/index.html": P.tools_index(), "tools/skin-quiz.html": P.skin_quiz(), "tools/routine-builder.html": P.routine_builder(),
    "tools/ingredient-checker.html": P.ingredient_checker(), "tools/layering-checker.html": P.layering_checker(),
    "tools/hydration-calculator.html": P.hydration_calc(), "tools/sunscreen-calculator.html": P.sunscreen_calc(),
    "support.html": P.support(), "contests.html": P.contests(), "careers.html": P.careers(), "advertise.html": P.advertise(),
    "about.html": P.about(), "contact.html": P.contact(),
    "privacy.html": P.legal("privacy.html", "Privacy Policy", "How Body.Care collects, uses and protects your data, cookies and advertising.", P.PRIVACY),
    "terms.html": P.legal("terms.html", "Terms of Use", "Terms of use for Body.Care.", P.TERMS),
    "disclaimer.html": P.legal("disclaimer.html", "Medical & Affiliate Disclaimer", "Body.Care medical disclaimer, affiliate disclosure and sponsored content policy.", P.DISCLAIMER),
    "404.html": P.notfound(),
}
for a in ARTICLES:
    pages[f'articles/{a["slug"]}.html'] = M.article(a)
for rel, html in pages.items():
    w(rel, html)

# ---- search index
CATN = {k: n for k, n, _ in CATEGORIES}
idx = [{"u": f'articles/{a["slug"]}.html', "t": a["title"], "d": a["desc"], "k": a["kw"], "c": CATN[a["cat"]]} for a in ARTICLES]
idx += [{"u": f"tools/{h}", "t": t, "d": d, "k": "tool calculator quiz free", "c": "Tool"} for h, _, t, d in M.TOOLS]
idx += [{"u": u, "t": t, "d": d, "k": k, "c": "Page"} for u, t, d, k in [
    ("free-plan.html", "Free personalised body care plan", "Get a 30-day plan and optional clinic matching.", "plan routine dermatologist clinic"),
    ("videos.html", "Video library", "Dermatologist-led videos.", "video youtube watch"),
    ("picks.html", "Body.Care Picks", "What to buy, ingredient-first.", "products buy best shop"),
    ("contests.html", "Giveaways & Awards", "Monthly giveaway and Readers' Choice awards.", "win prize contest giveaway award"),
    ("support.html", "Support Body.Care", "Donate or become a member.", "donate support membership"),
    ("advertise.html", "Advertise & partner", "Sponsorships and clinic lead program.", "advertise sponsor clinic partner media kit"),
    ("careers.html", "Careers", "Writers, reviewers, creators.", "jobs hiring writer creator")]]
w("search-index.json", json.dumps(idx, ensure_ascii=False))

# ---- sitemap / robots / ads.txt / manifest / sw / nojekyll
today = datetime.date.today().isoformat()
urls = [p for p in pages if p != "404.html"]
prio = lambda p: "1.0" if p == "index.html" else "0.9" if p.startswith(("tools/", "free-plan")) else "0.8" if p.startswith("articles/") else "0.5"
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
    f'  <url><loc>{SITE}/{p.replace("index.html", "")}</loc><lastmod>{today}</lastmod><priority>{prio(p)}</priority></url>\n' for p in urls) + "</urlset>\n"
w("sitemap.xml", sm)
w("robots.txt", f"User-agent: *\nAllow: /\nDisallow: /build/\n\nSitemap: {SITE}/sitemap.xml\n")
w("ads.txt", "# Google AdSense — replace pub-0000000000000000 with your publisher ID, then remove the leading '#'.\n# google.com, pub-0000000000000000, DIRECT, f08c47fec0942fa0\n")
w(".nojekyll", "")
w("manifest.webmanifest", json.dumps({"name": "Body.Care", "short_name": "Body.Care", "description": "Science-first care for your whole body", "start_url": "./index.html", "scope": "./",
   "display": "standalone", "background_color": "#fbf8f3", "theme_color": "#0f5e59",
   "icons": [{"src": "assets/img/icon-192.png", "sizes": "192x192", "type": "image/png"}, {"src": "assets/img/icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any maskable"}]}, indent=1))
core = ["./", "index.html", "assets/css/main.css", "assets/js/config.js", "assets/js/main.js", "assets/js/tools.js", "assets/js/ingredients.js", "tools/index.html", "offline.html"]
w("sw.js", """/* Body.Care service worker: cache-first for assets, network-first for pages, offline fallback. */
const V = "bc-v1.0.0"; const CORE = %s;
self.addEventListener("install", e => { e.waitUntil(caches.open(V).then(c => c.addAll(CORE)).then(() => self.skipWaiting())); });
self.addEventListener("activate", e => { e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== V).map(k => caches.delete(k)))).then(() => self.clients.claim())); });
self.addEventListener("fetch", e => {
  const r = e.request; if (r.method !== "GET" || new URL(r.url).origin !== location.origin) return;
  if (r.mode === "navigate") { e.respondWith(fetch(r).then(res => { const c = res.clone(); caches.open(V).then(x => x.put(r, c)); return res; }).catch(() => caches.match(r).then(m => m || caches.match("offline.html")))); return; }
  e.respondWith(caches.match(r).then(m => m || fetch(r).then(res => { const c = res.clone(); caches.open(V).then(x => x.put(r, c)); return res; })));
});
""" % json.dumps(core))
w("offline.html", '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Offline | Body.Care</title><link rel="stylesheet" href="assets/css/main.css"></head><body><main class="section center"><div class="wrap"><h1>You\'re offline</h1><p class="lead" style="margin:auto">Pages you\'ve visited are still available. Reconnect to load new guides.</p><p style="margin-top:20px"><a class="btn btn-brand" href="index.html">Try again</a></p></div></main></body></html>')
w("assets/img/favicon.svg", LOGO.replace('aria-hidden="true"', 'xmlns="http://www.w3.org/2000/svg"'))

# ---- raster icons + OG image
try:
    from PIL import Image, ImageDraw, ImageFont
    def icon(size):
        im = Image.new("RGB", (size, size), "#0f5e59"); d = ImageDraw.Draw(im)
        for y in range(size):
            t = y / size; d.line([(0, y), (size, y)], fill=(int(15 + (232 - 15) * t * .55), int(94 + (103 - 94) * t), int(89 + (74 - 89) * t)))
        s = size / 40
        pts = []
        import math
        for i in range(200):
            th = i / 200 * 2 * math.pi
            x = 16 * math.sin(th) ** 3; y = 13 * math.cos(th) - 5 * math.cos(2 * th) - 2 * math.cos(3 * th) - math.cos(4 * th)
            pts.append((20 * s + x * .6 * s, 20.5 * s - y * .6 * s))
        d.polygon(pts, fill="white"); r = 2.6 * s
        d.ellipse([20 * s - r, 20 * s - r, 20 * s + r, 20 * s + r], fill="#e8674a")
        return im
    os.makedirs(os.path.join(ROOT, "assets/img"), exist_ok=True)
    icon(192).save(os.path.join(ROOT, "assets/img/icon-192.png")); icon(512).save(os.path.join(ROOT, "assets/img/icon-512.png"))
    og = Image.new("RGB", (1200, 630), "#fbf8f3"); d = ImageDraw.Draw(og)
    d.rectangle([0, 0, 1200, 630], fill="#0f5e59"); d.ellipse([820, -160, 1360, 380], fill="#e8674a")
    og.paste(icon(160), (80, 80))
    def font(sz, bold=True):
        for p in ["/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"]:
            if os.path.exists(p): return ImageFont.truetype(p, sz)
        return ImageFont.load_default()
    d.text((80, 300), "Body.Care", font=font(110), fill="white")
    d.text((84, 440), "Science-first care for your whole body.", font=font(40, False), fill="#d9ece9")
    d.text((84, 510), "Guides · Free tools · Videos · Personal plans", font=font(30, False), fill="#ffb199")
    og.save(os.path.join(ROOT, "assets/img/og-image.png"))
except Exception as ex:
    print("icon generation skipped:", ex)

print(f"Built {len(pages)} pages, {len(idx)} search entries.")
