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
- Every interactive part must work with JavaScript turned off. The sliders
  fall back to a draggable CSS resize corner. The form falls back to a plain
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
| Elliot with a damp meter (full-width hero, share image) | https://ecoshield.uk/wp-content/uploads/2025/12/Eco-Shield-Damp-Mould-Survey-scaled.jpg |
| Elliot kneeling with a damp meter (booking section) | https://ecoshield.uk/wp-content/uploads/2025/12/NWD04501-scaled.jpg |
| Poole slider "During": kitchen stripped back | https://ecoshield.uk/wp-content/uploads/2025/10/Black-Mould-and-Rising-Damp-1.jpeg |
| Poole slider "After": new kitchen, same window | https://ecoshield.uk/wp-content/uploads/2025/10/Black-Mould-and-Rising-Damp3-1.jpg |
| Poole: mould behind the units ("Don't leave it too late") | https://ecoshield.uk/wp-content/uploads/2025/10/Black-Mould-and-Rising-Damp1-1-scaled.jpeg |
| Christchurch slider "Before": old kitchen | https://ecoshield.uk/wp-content/uploads/2026/02/IMG_3457-1.jpeg |
| Christchurch slider "After": same kitchen refurbished | https://ecoshield.uk/wp-content/uploads/2026/02/IMG_CF0C1BDF-0085-4505-9278-A13B90377A32-scaled.jpeg |
| Bournemouth slider "Before": rotten joists | https://ecoshield.uk/wp-content/uploads/2025/09/IMG_0809.jpeg |
| Bournemouth slider "After": new floor | https://ecoshield.uk/wp-content/uploads/2025/09/IMG_0807.jpeg |
| Winchester "Finished": lime plaster | https://ecoshield.uk/wp-content/uploads/2025/09/IMG_0800-scaled.jpeg |
| Southbourne "Finished": new roof and solar | https://ecoshield.uk/wp-content/uploads/2025/10/Roof-Replacement-Solar-Installation-Southbourne-2.jpg |

Crop each slider pair to the same square so the two photos line up. Label
the Poole pair "During" and "After", because its first photo shows the work
in progress, not the mould.

Winchester and Southbourne have no real before photo: show the finished photo
with a "Finished" tag.
Don't use IMG_7256.jpg (it looks like stock) or drimaster_house_detail.jpg
(a manufacturer's diagram).

## Page structure (in this order)

1. **Sticky header.** "Eco Shield", "Damp, mould and property protection",
   "Call Elliot 07369 286705" and a "Book a free survey" button.
2. **Hero.** A full-width photo of Elliot testing a wall with a damp meter,
   with a dark gradient over the left side. On it, in white: "Damp and mould
   fixed at the source." and "Free damp survey across Hampshire, Dorset,
   Wiltshire and the New Forest." Two actions: "Book a free survey" (scrolls
   to the form) and "Call 07369 286705". Below them, a round face photo of
   Elliot with "Elliot does your survey himself." and a "Rated Excellent from
   41 Google reviews" link to the reviews. On mobile, show the photo as a
   band at the top that fades into the dark text area, so Elliot and the
   meter stay in view.
3. **Why choose us.** Four items with line icons:
   - Free damp survey: "Elliot checks your home and tells you what he finds.
     No charge."
   - You deal with the owner: "Elliot runs Eco Shield and does your survey
     himself."
   - The cause, not the patch: "We find where the damp comes from, so it
     stays fixed."
   - Rated Excellent: "41 Google reviews. Most of them name Elliot."
4. **Meet Elliot.** His portrait plus: "Elliot owns Eco Shield. He comes out
   and does your survey himself." and "He finds what is causing the damp,
   not just the patch you can see. Then he fixes that." Review 4 below.
5. **Who we help.** Three cards with icons in copper-tinted circles, links
   pinned to the bottom: Homeowners (including buyers: "Elliot can survey it
   before you sign"), Landlords and letting agents (mention Awaab's Law and
   link to that page), Housing associations. Then "We also help renters and
   commercial properties."
6. **What are you seeing?** Nine cards, three across on desktop, two on
   tablets, one on phones. Each card has a line icon in a copper-tinted
   circle, the problem, what you see, and the matching service as a link;
   the whole card is clickable. Rising damp, condensation, black mould,
   timber decay, damp floors, cold rooms, roof leaks, rain soaking walls,
   and damp in a rented home (links to the Awaab's Law page).
7. **Don't leave it too late.** Stack the real cost of leaving mould and
   damp. Use general facts only and never invent prices.
   - Intro: "Mould and damp don't go away on their own. The longer they're
     left, the further they spread: into your home, your health and your
     bank balance."
   - Three stages with a coloured top edge that goes green, amber, red, each
     with a "UK guide price" pinned to the bottom of the card: Caught early
     (find the cause, treat it, make good: £200 to £1,000), Left a while
     (strip and replaster, replace rotten skirting, treat every room: £1,000
     to £3,000, plus replastering), Left for years (lift floors, replace
     joists, sometimes a full refurbishment, linking the Bournemouth and
     Christchurch jobs: £2,500 to £7,500 or more). Add a note that guide
     prices are typical UK ranges from trade cost guides such as Checkatrade
     (2025 to 2026), that your price depends on your home, and that the
     survey is free.
   - Three columns with icons. Your health: spores in the bedroom; the NHS
     warns of breathing problems, asthma and allergies; babies, children,
     older people and people with lung conditions are most at risk. Your
     home: timber rots and dry rot can spread through brickwork; rising damp
     salts mean plaster has to come off; mould stains paint, carpets,
     clothes and furniture. Your money: a small treatment grows into new
     plaster, floors and joists; damp walls raise heating bills; damp in a
     buyer's survey can mean a lower offer or a lost sale; many home
     insurance policies won't pay for damage that builds up slowly.
   - The Poole mould-behind-the-units photo, with two notes beside it.
     Buying a home: one buyer says Elliot's visit "saved us thousands of
     pounds". Renting out a home: Awaab's Law is named after Awaab Ishak, a
     two-year-old who died in 2020 after long exposure to mould in his
     family's home; link to the Awaab's Law page. Add "Health information
     from the NHS."
   - End with a dark band: "Spotted damp or mould? Get it checked now, while
     it's a small job." Book and Call buttons.
8. **How it works.** Numbered circles joined by a line: Free survey, Written
   report, The fix, Guarantee. Guarantee shows the placeholder "Guarantee
   length: confirm with Elliot".
9. **Recent work.** "Drag across each photo to see the change." Before and
   after sliders for Poole, Christchurch and Bournemouth in a row of three,
   then finished photos for Winchester and Southbourne sharing the second
   row at half width each, so there is no gap. Each slider: the after photo
   underneath, the before photo on top cut off at a white divider, a round
   handle, and small tags in the top corners. Drag anywhere on the photo to
   move it, and use the arrow keys too. Without JavaScript, the divider must
   still be draggable (use CSS `resize` on the before layer).
10. **What customers say.** "Rated Excellent from 41 Google reviews" under
    the heading, then reviews 1, 2, 3 and 5 (review 4 is already in Meet
    Elliot) as white cards in a 2 by 2 grid, each with one large copper
    quote mark and the name pinned to the bottom.
11. **Book a free survey form.** "Tell us what's wrong and where you are.
    Elliot will call you to pick a time." Fields: name, phone, postcode,
    "What's the problem?" as tap-to-pick options (Rising damp, Condensation
    or mould, Timber decay, Roof, Something else), optional photo upload
    with the hint "A photo helps Elliot see the problem before he visits".
    Button: "Book my free survey". Front-end only, with a clear success
    message and a note that the preview doesn't send. Show the photo of
    Elliot kneeling with the damp meter beside it, with the hours.
12. **Footer.** Phone, email, office address, hours, areas covered, and
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

- **Colour (Eco Shield's real brand colours, from ecoshield.uk):** Near-black
  `#141414` (text, dark sections), Copper `#A26028` (main buttons, icons and
  accents; it matches the house in his logo), Light grey `#F5F5F5` (page),
  White `#FFFFFF` (alternate sections, form), Grey `#5E5E5E` for secondary
  text (his `#757575` fails AA contrast on light grey). The cost stages use
  green, amber and red edges.
- **Logo:** use his real logo from
  https://ecoshield.uk/wp-content/uploads/2024/09/Screenshot-2023-10-31-at-17.21.01.png
  (a screenshot on white). Cut it out to a transparent background, crop it
  tight, and make a light version for the dark footer. Use the house mark as
  the favicon.
- **Type:** Archivo only. Headings narrow (`wdth` 78) and bold, large and
  tight with balanced line breaks. Body at normal width.
- **Bold elements:** the full-width hero photo of Elliot at work, and the
  before and after sliders. Keep everything else calm.
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
images load. Run an axe accessibility scan. Test the sliders and the form
with JavaScript on and off. Fix what looks off, then screenshot again.
Repeat until it looks finished.

## When you're done, give me

1. The design plan and what you changed after reviewing it.
2. The final mobile and desktop screenshots.
3. A single self-contained HTML file with the photos embedded, so I can open
   and click through it.
4. A list of every placeholder that needs real content from Elliot.
5. Three to five short bullets I can send Elliot on WhatsApp that say what's
   better than his current site, in plain words.
