/* =========================================================================
   BODY.CARE — SITE CONFIG (edit this one file to switch on revenue)
   Every monetization channel reads from here. Empty value = feature
   degrades gracefully (placeholder / mailto fallback), never breaks.
   ========================================================================= */
window.BC_CONFIG = {
  siteName: "Body.Care",
  siteUrl: "https://body.care",
  contactEmail: "hello@body.care",

  /* ---- Google AdSense ----------------------------------------------------
     1) Apply at adsense.google.com with body.care  2) Paste your publisher ID
     (ca-pub-XXXXXXXXXXXXXXXX)  3) Paste slot IDs from Ads > By ad unit.
     Also update /ads.txt with the same pub ID.                              */
  adsenseClient: "",                // e.g. "ca-pub-1234567890123456"
  adSlots: { header: "", inArticle: "", sidebar: "", footer: "", multiplex: "" },

  /* ---- Analytics (optional) --------------------------------------------- */
  ga4Id: "",                         // e.g. "G-XXXXXXXXXX"

  /* ---- Forms / Lead capture ---------------------------------------------
     Paste a Formspree endpoint (https://formspree.io/f/xxxxxxx) or any
     endpoint accepting JSON POST (Getform, Basin, Make/Zapier webhook,
     Google Apps Script). Per-form overrides let you route leads by type.
     Empty = falls back to a pre-filled email to contactEmail.               */
  forms: {
    default: "",
    plan: "",          // Free personalised plan (primary lead magnet)
    clinic: "",        // "Match me with a clinic" — high-value sellable lead
    newsletter: "",    // Newsletter signups (or Mailchimp/Beehiiv form action)
    partner: "",       // Brands / advertisers / lead buyers
    contest: "",       // Giveaway entries + award nominations
    careers: "",       // Job + creator applications
    contact: ""
  },

  /* ---- Donations & support ----------------------------------------------
     Any subset works. Buttons auto-hide when blank.                         */
  donate: {
    stripeLink: "",        // Stripe Payment Link (supports custom amounts)
    stripeMonthlyLink: "", // Stripe Payment Link for a recurring price
    paypal: "",            // e.g. "https://www.paypal.com/donate/?hosted_button_id=XXXX"
    kofi: "",              // e.g. "https://ko-fi.com/bodycare"
    buymeacoffee: "",      // e.g. "https://buymeacoffee.com/bodycare"
    githubSponsors: "https://github.com/sponsors/WEBWORKSA1",
    patreon: "",
    goal: 5000, raised: 0, currency: "USD"   // progress meter on /support
  },

  /* ---- Affiliate --------------------------------------------------------- */
  amazonTag: "",           // e.g. "bodycare-20" — appended to Amazon links

  /* ---- YouTube ------------------------------------------------------------
     Your channel + featured videos. Replace with your own uploads to earn
     YouTube Partner revenue from every embed view.                          */
  youtubeChannel: "https://www.youtube.com/@bodycare",
  videos: [
    { id: "9pg-OybGGCc", title: "How to apply sunscreen: dermatologist tips", cat: "Sun", src: "American Academy of Dermatology" },
    { id: "ytiFpOkTIes", title: "How to treat a sunburn: dermatologist tips", cat: "Sun", src: "American Academy of Dermatology" },
    { id: "-Jt3gczy_4o", title: "How to build your morning skincare routine", cat: "Routines", src: "YouTube" },
    { id: "5xALFP27VRM", title: "A dermatologist's exact night routine", cat: "Routines", src: "Dr Sam Bunting" },
    { id: "cjxLqNwjxI0", title: "Building a skincare routine: product deep-dive", cat: "Routines", src: "Dr Sam Bunting" },
    { id: "3W_uqWNsad0", title: "How to treat a sunburn like a dermatologist", cat: "Sun", src: "YouTube" }
  ],

  /* ---- Contest ------------------------------------------------------------ */
  contest: { title: "Monthly Body Care Kit Giveaway", prize: "US$250 body-care kit + 1-year Body.Care Circle membership", endsISO: "" }, // "" = auto end-of-month

  social: {
    instagram: "https://instagram.com/bodycare",
    tiktok: "https://www.tiktok.com/@bodycare",
    youtube: "https://www.youtube.com/@bodycare",
    pinterest: "https://pinterest.com/bodycare",
    x: "https://x.com/bodycare"
  }
};
