# Roofman homepage build prompt

Paste this into Claude, Lovable, v0 or any AI site builder to rebuild the homepage. `index.html` in this folder is the version already built from it.

---

Build a one-page homepage for **Roofman**, a family roofing company from Leek, Staffordshire that works across the UK. It sells roof cleaning, roof repairs and new roofs. The buyers are homeowners aged 45 to 75, and most of them visit on a phone.

## Brand

| Use | Colour |
|---|---|
| Primary (buttons, highlights, logo "Roof") | Lime green `#72ae00` |
| Green hover / dark text accent | `#5a8a00` |
| Secondary text, logo "Man" | Slate grey `#747a7e` |
| Links and small accents | Blue `#066aab` |
| Dark sections | Near-black `#11161a` / `#1f2427` |
| Light sections | `#f4f6f3` |

- Fonts: Barlow Condensed (headings, uppercase in the hero) and Barlow (body).
- Logo: `assets/logo.png` (green and grey "RoofMan NATIONWIDE" with a house icon).
- Style: clean, confident, trades-premium. Big type, lots of white space, rounded cards, real job photos. No stock photos.

## Page order

1. **Top bar (dark):** "No deposit. You only pay when you're happy with the job." and "Free quote within 24 hours".
2. **Sticky header:** logo, nav (Our Process, Roof Cleaning, Our Work, Reviews, Areas), and one tap-to-call number: **0800 038 5724**. Use no other numbers.
3. **Hero:** dark overlay on a real roof photo.
   - Headline: "Your roof cleaned, treated and guaranteed for 10 years"
   - Subhead: "We strip out the moss, treat every tile and fix broken ones while we're up there. You don't pay a penny until you've inspected the work."
   - Three ticks: no deposit, 10 year guarantee, beat any genuine like-for-like quote.
   - Hero background: a real roof photo, slightly darkened.
   - Two-step quote form on the right. Step 1: one tap on what they need (Roof cleaning / Roof repair / New roof / Not sure). Step 2: postcode, first name, mobile, optional best time to call and optional roof photo. Button: "Get my free quote". Show "Rather talk? Call free on 0800 038 5724" under it.
4. **Green trust strip:** 10 YEARS guarantee / £0 deposit / 24 HRS quote / UK-WIDE, family team from Leek.
5. **Big testimonial:** "My best quote was £9,000 until Roofman came along for a quarter of the price!" from Mrs Lawton, Essex, next to before and after photos.
6. **Scroll photo story: "Scroll through a real job".** A sticky section that steps through real job photos as you scroll: thick moss, lichen close-up, harness on, washing tiles, halfway clean, fungicide, then before/after photos of the same house that wipe across as you scroll. Finish with a "10 year guarantee" badge.
7. **Packages:** Semi-detached £895, Standard detached £1,195, Large detached £1,795. Each includes: every tile cleaned and treated with fungicide, gutters and fascias cleaned, moss and debris cleared, free minor repairs, 10 year guarantee. Under the cards: "Got a quote elsewhere? We'll beat any genuine like-for-like price."
8. **Gallery:** real job photos with one-line captions.
9. **Reviews:** 3 cards with real quotes from Neil (Leek), Mrs Harrison (Cheshire) and Mr W (Alderley Edge). Leave a slot for the live Google rating. Never invent ratings or review counts.
10. **How it works:** 4 steps. Send details, get a fixed quote, we do the job, inspect then pay.
11. **Areas:** "We cover over 900 towns across the UK", a town search box and chips for the main towns. Link the existing `/services/roofman-nationwide/roof-cleaning-in-[town]/` pages. Keep every one of those URLs.
12. **Final green CTA** and a footer with the current year.

## Rules

- Mobile first. Add a fixed bottom bar on phones: "Call free" and "Free quote".
- Don't block pinch-to-zoom.
- One H1 only. Add a page title and meta description.
- Copy at grade 8 reading level. No em dashes.
- Load fast: no sliders, no page builder, compressed WebP images.
