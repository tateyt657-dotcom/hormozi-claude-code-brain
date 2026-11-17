# Prompt: Eco Shield homepage preview (Elliot)

Build a preview homepage for Eco Shield, a damp, mould and property protection
company in Ringwood, Hampshire. This is a sales preview: the owner, Elliot,
will look at it and decide whether to pay for it. Its job is to make him think
"that gets me more survey bookings than my current site."

## What to build

- One responsive homepage as a single static `index.html` with inline CSS and
  minimal vanilla JS. No frameworks, no build step.
- Put it in a new folder called `ecoshield-preview/`.
- Use real content only (below). Where something is missing, show a clearly
  marked placeholder (for example a grey box saying "Before photo goes
  here"). Never invent reviews, numbers, guarantees, accreditations or years
  in business.
- Every interactive part must work with JavaScript turned off. Build the hero
  wall toggle as a CSS checkbox switch. The form must fall back to a plain
  submit that shows the success message. Use JS only as an extra.

## The business (real content, use exactly)

- Name: Eco Shield
- Owner: Elliot (customers mention him by name in almost every review).
  Technician: Diego.
- Phone: 07369 286705 (use `tel:07369286705`)
- Email: contact@ecoshield.uk
- Office: Ringwood, BH24 3ED
- Hours: Mon to Fri 8am to 7pm, Sat 8am to 4pm, Sunday closed
- Areas: Hampshire, Dorset, Wiltshire and the New Forest. Towns: Ringwood,
  Bournemouth, Southampton, Salisbury, Poole, Christchurch, Winchester.
- Reviews: rated Excellent, 41 Google reviews
- Partner: Optimum Ventilation Management
- Main offer: a free damp survey
- Who they help: homeowners, landlords, letting agents, renters, commercial
  properties, housing associations

Services (each one links to the existing page, keep these exact URLs):

- Damp proofing and preservation: https://ecoshield.uk/damp-proofing-and-preservation/
- Ventilation (PIV systems, extractor fans): https://ecoshield.uk/ventilation-solutions-hampshire-dorset/
- Mould treatment and diagnostics: https://ecoshield.uk/mould-treatment-diagnostics/
- Roof repairs and upgrades: https://ecoshield.uk/roof-repairs-upgrades/
- Floor damp proofing: https://ecoshield.uk/floor-damp-proofing-subfloor-refurbishment-services/
- Insulation: https://ecoshield.uk/insulation/
- Exterior coatings: https://ecoshield.uk/exterior-coatings/
- Awaab's Law (for landlords): https://ecoshield.uk/awaabs-law/

Case studies (link to the existing pages):

- Severe black mould and rising damp, Poole bungalow: https://ecoshield.uk/severe-black-mould-and-rising-damp-treatment-poole-bungalow/
- Full bungalow refurbishment, Christchurch: https://ecoshield.uk/full-bungalow-refurbishment-christchurch/
- Rising damp and floor restoration, Bournemouth: https://ecoshield.uk/rising-damp-floor-restoration-in-bournemouth/
- Breathable lime plaster restoration, Winchester: https://ecoshield.uk/breathable-lime-plaster-restoration-in-winchester/
- Roof replacement and solar, Southbourne: https://ecoshield.uk/roof-replacement-solar-installation-southbourne/

Real Google reviews. Quote word for word, never edit:

1. danielwalsh1984: "I had 3 damp specialists out for quotes. I choose Elliot
   as he was professional and the other 2 were giving off cowboy vibes. I am
   very happy in my decision as he overdelivered."
2. Mike: "Elliott was excellent, fitted in a visit to survey damp and roof of
   our potential new home and advised us of the issues before we signed,
   saved us thousands of pounds."
3. Kryseis: "Elliot is an absolutely legend! Decent, Honest guy."
4. NextGen Spaces (property portfolio): "They didn't just point out the
   symptoms; they were excellent at accurately diagnosing the root causes of
   the issues, which gave us total confidence in their proposed solutions."
5. helen h: "The damp proofing and repairs were carried out promptly and
   neatly, and the fee that I paid is entirely fair for the quality standards
   and work ethic that I received."

## Real photos (from ecoshield.uk)

Download these, resize to about 800px, compress to under 120KB, and use them
with alt text, width, height and lazy loading:

| Use | Source |
|---|---|
| Elliot portrait (Meet Elliot, and a face crop for the hero) | https://ecoshield.uk/wp-content/uploads/2025/12/Tattoo-Off-scaled.jpg |
| Elliot with a damp meter (booking section, share image) | https://ecoshield.uk/wp-content/uploads/2025/12/Eco-Shield-Damp-Mould-Survey-scaled.jpg |
| Poole before: black mould under the sink | https://ecoshield.uk/wp-content/uploads/2025/10/Black-Mould-and-Rising-Damp2-1-scaled.jpeg |
| Poole after: new kitchen | https://ecoshield.uk/wp-content/uploads/2025/10/Black-Mould-and-Rising-Damp3-1.jpg |
| Poole: mould behind the units ("Don't leave it too late") | https://ecoshield.uk/wp-content/uploads/2025/10/Black-Mould-and-Rising-Damp1-1-scaled.jpeg |
| Christchurch before: old kitchen | https://ecoshield.uk/wp-content/uploads/2026/02/IMG_3457-1.jpeg |
| Christchurch after: refurbished kitchen | https://ecoshield.uk/wp-content/uploads/2026/02/IMG_CF0C1BDF-0085-4505-9278-A13B90377A32-scaled.jpeg |
| Bournemouth before: rotten joists | https://ecoshield.uk/wp-content/uploads/2025/09/IMG_0809.jpeg |
| Bournemouth after: new floor | https://ecoshield.uk/wp-content/uploads/2025/09/IMG_0807.jpeg |
| Winchester after: lime plaster | https://ecoshield.uk/wp-content/uploads/2025/09/IMG_0800-scaled.jpeg |
| Southbourne after: new roof and solar | https://ecoshield.uk/wp-content/uploads/2025/10/Roof-Replacement-Solar-Installation-Southbourne-2.jpg |

Winchester and Southbourne have no real before photo: keep a placeholder.
Don't use IMG_7256.jpg (it looks like stock) or drimaster_house_detail.jpg
(a manufacturer's diagram).

## Page structure (in this order)

1. **Sticky header.** "Eco Shield", "Damp, mould and property protection",
   "Call Elliot 07369 286705" and a "Book a free survey" button.
2. **Hero.** Headline: "Damp and mould fixed at the source." Sub-line: "Free
   damp survey across Hampshire, Dorset, Wiltshire and the New Forest." Two
   actions: "Book a free survey" (scrolls to the form) and "Call 07369
   286705". Beside them, a round face photo of Elliot with "Elliot does your
   survey himself." and a "Rated Excellent from 41 Google reviews" link to
   the reviews. On the right, the hero wall (see design).
3. **Why choose us.** Four items with line icons:
   - Free damp survey: "Elliot checks your home and tells you what he finds.
     No charge."
   - You deal with the owner: "Elliot runs Eco Shield and does your survey
     himself."
   - The cause, not the patch: "We find where the damp comes from, so it
     stays fixed."
   - Rated Excellent: "41 Google reviews. Most of them name Elliot."
4. **The cowboy review.** Review 1, large, on a dark band with one big green
   quote mark. This answers the biggest fear in this trade: hiring a cowboy.
5. **Meet Elliot.** His portrait plus: "Elliot owns Eco Shield. He comes out
   and does your survey himself." and "He finds what is causing the damp,
   not just the patch you can see. Then he fixes that." Review 4 below.
6. **Who we help.** Homeowners (including buyers: "Elliot can survey it
   before you sign"), Landlords and letting agents (mention Awaab's Law and
   link to that page), Housing associations. Then "We also help renters and
   commercial properties."
7. **What are you seeing?** Problems by what the visitor sees, each linking
   to its service page: rising damp, condensation, black mould, timber
   decay, damp floors, cold rooms, roof leaks, rain soaking walls.
8. **Don't leave it too late.** "Damp doesn't fix itself. The longer it
   sits, the bigger the job and the bill." Six points with icons: mould
   spreads, timber rots, plaster fails, heat escapes, your health suffers
   (cite the NHS), landlords face deadlines (Awaab's Law). Show the Poole
   mould-behind-the-units photo. End with a dark band: "Spotted damp or
   mould? Get it checked now, while it's a small job." Book and Call buttons.
9. **How it works.** Numbered circles joined by a line: Free survey, Written
   report, The fix, Guarantee. Guarantee shows the placeholder "Guarantee
   length: confirm with Elliot".
10. **Recent work.** The 5 case studies in this order: Poole, Christchurch,
    Bournemouth, Winchester, Southbourne. Before and after photos with small
    tags on the images ("Before: black mould", "After: new kitchen").
11. **What customers say.** Reviews 2 to 5, then "Rated Excellent from 41
    Google reviews."
12. **Book a free survey form.** "Tell us what's wrong and where you are.
    Elliot will call you to pick a time." Fields: name, phone, postcode,
    "What's the problem?" as tap-to-pick options (Rising damp, Condensation
    or mould, Timber decay, Roof, Something else), optional photo upload
    with the hint "A photo helps Elliot see the problem before he visits".
    Button: "Book my free survey". Front-end only, with a clear success
    message and a note that the preview doesn't send. Show the damp meter
    photo of Elliot beside it, with the hours.
13. **Footer.** Phone, email, office address, hours, areas covered, and
    "Ventilation partner: Optimum Ventilation Management."

On mobile, add a sticky bottom bar with "Call" and "WhatsApp"
(`https://wa.me/447369286705`). Keep focused fields clear of that bar.

## Design

Work like the design lead at a studio known for giving every client a
distinct identity. Elliot already has a decent agency-built site, so a
generic template won't win him over.

Ground every choice in the trade: lime plaster, old brick, slate, timber,
damp meters, the before and after of a mouldy wall made clean and dry. Don't
default to "eco = bright green".

- **Colour:** Lime putty `#ECEAE4` (page), Limewash `#F8F7F3` (white
  sections, form), Welsh slate `#252E37` (text and dark sections), Slate
  grey `#56616B` (secondary text), Tide mark `#8C7B5B` (only in the wall
  drawing), Meter green `#2D6A4E` (main buttons and the "dry" state only).
- **Type:** Archivo only. Headings narrow (`wdth` 78) and bold, large and
  tight with balanced line breaks. Body at normal width.
- **Bold element (spend boldness only here):** the hero is a drawn wall
  with a brown tide mark of rising damp, a window running with condensation
  and black mould in the corner. Once it's in view, the damp drains away,
  the window clears and a damp meter strip moves from Wet to Dry. A switch
  flips between damp and dry. Frame it in a dark slate casing with a soft
  shadow, like a survey device. With reduced motion, show the dry wall.
- **Premium, not flat:** alternate light, white and dark sections. Soft,
  layered shadows only on photos, the hero frame, the call-to-action band
  and the form. Corners of 6 to 12px. Icons in soft green-tinted circles.
  Buttons with a slight shadow and lift on hover.
- **Avoid:** cream with a serif and terracotta; near-black with neon;
  identical cards with the same shadow; ALL CAPS eyebrow labels; one word
  accented in a headline; arrows on buttons; fade-up animation on every
  section.

Copy rules: plain words, sentence case, active voice, short sentences, no
filler and no hype. Grade 8 reading level. No em dashes.

Quality floor: no horizontal scroll from 360px up, visible keyboard focus,
`prefers-reduced-motion` respected, WCAG AA contrast, line lengths under
about 75 characters, a real `<title>` and meta description, `og:image` set to
the damp meter photo URL above, LocalBusiness schema with the real details,
and images with alt text and lazy loading.

## Check your work

Use Playwright to screenshot at 390px and 1366px. Scroll first so lazy
images load. Run an axe accessibility scan. Test the wall switch and the
form with JavaScript on and off. Fix what looks off, then screenshot again.
Repeat until it looks finished.

## When you're done, give me

1. The design plan and what you changed after reviewing it.
2. The final mobile and desktop screenshots.
3. A single self-contained HTML file with the photos embedded, so I can open
   and click through it.
4. A list of every placeholder that needs real content from Elliot.
5. Three to five short bullets I can send Elliot on WhatsApp that say what's
   better than his current site, in plain words.
