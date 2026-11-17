# Reusable prompt: trades homepage sales preview

This combines your original Eco Shield brief with every change you asked for
afterwards. Swap the parts in [square brackets] for a new client.

---

Build a preview homepage for [Business name], a [trade] company in [town,
county]. This is a sales preview: the owner, [Owner], will look at it and
decide whether to pay for it. Its job is to make them think "that gets me more
[survey / quote] bookings than my current site."

## What to build

- One responsive homepage as a single static `index.html` with inline CSS and
  minimal vanilla JS. No frameworks, no build step.
- Put it in a new folder called `[client]-preview/`.
- Use real content only (below). Where something is missing, show a clearly
  marked placeholder (for example a grey box saying "Photo of [Owner] goes
  here"). Never invent reviews, numbers, guarantees, accreditations or years
  in business.
- Every interactive part must work with JavaScript turned off. Use CSS (for
  example a checkbox switch) for toggles. Use JS only as an extra.

## Real photos

- Pull real photos from the client's current site: [site URL]. Use a photo of
  the owner, a photo of them at work, and before and after pairs from each
  case study page.
- Only call a photo "before" or "after" if you can see it is. Check the same
  room, window or door appears in both. If a job has no real before photo,
  keep a placeholder.
- Skip stock photos and manufacturer diagrams.
- Resize and compress every photo (about 800px, under 120KB). Add alt text,
  width, height and lazy loading.

## The business (real content, use exactly)

- Name: [ ]
- Owner: [ ] (say if customers name them in reviews). Staff: [ ]
- Phone: [ ] (use `tel:[digits]`)
- Email: [ ]
- Office: [ ]
- Hours: [ ]
- Areas: [counties]. Towns: [ ]
- Reviews: rated [ ], [number] Google reviews
- Partner: [ ]
- Main offer: [free survey / free quote]
- Who they help: [ ]
- Services, each linking to its existing page: [name: URL]
- Case studies, each linking to its existing page: [title, town: URL]

Real Google reviews. Quote word for word, never edit:

1. [name]: "[review that answers the biggest fear in the trade]"
2. [name]: "[ ]"
3. [name]: "[ ]"
4. [name]: "[review about finding the root cause]"
5. [name]: "[ ]"

## Page structure (in this order)

1. **Sticky header.** Name, phone, and a "Book a free [survey]" button.
2. **Hero.** Headline about the outcome, not the job title. Sub-line with the
   offer and areas. Two actions: "Book a free [survey]" (scrolls to the form)
   and "Call [phone]". Beside them, a small round photo of [Owner] with
   "[Owner] does your [survey] himself" and a "Rated [ ] from [n] Google
   reviews" link that jumps to the reviews.
3. **Why choose us.** Four items with simple line icons. Facts only: the free
   offer, dealing with the owner, fixing the cause, the rating.
4. **The fear review.** Review 1 shown large on a dark band with one big
   accent quote mark.
5. **Meet [Owner].** Their photo plus 2 short lines. Review 4 backs it up.
6. **Who we help.** Three routes. The landlord route mentions [relevant law]
   and links to that page.
7. **Problems we fix.** Organised by what the visitor can see, each linking
   to the matching service page.
8. **Don't leave it too late.** What happens when the problem is left (only
   general facts, cite any health claim to the NHS). One real photo from a
   job. End with a dark call-to-action band: "Spotted [problem]? Get it
   checked now, while it's a small job." Book and Call buttons.
9. **How it works.** Numbered steps in circles joined by a line: free
   [survey], written report, the fix, guarantee. For the guarantee, show a
   placeholder: "Guarantee length: confirm with [Owner]".
10. **Recent work.** Case studies with town names and real before and after
    photos. Put the strongest pairs first. Label photos with small
    "Before: ..." and "After: ..." tags laid over the image.
11. **More reviews.** Reviews 2 to 5.
12. **Book a free [survey] form.** Name, phone, postcode, "What's the
    problem?" (as tap-to-pick options), optional photo upload with the hint
    "A photo helps [Owner] see the problem before [he/she] visits". Button:
    "Book my free [survey]". Front-end only with a clear success message.
    Show the photo of the owner at work beside it.
13. **Footer.** Phone, email, office address, hours, areas covered, partner.

On mobile, add a sticky bottom bar with "Call" and "WhatsApp"
(`https://wa.me/[number]`). Keep focused fields clear of that bar.

## Design approach

Work like the design lead at a studio known for giving every client a
distinct identity.

**Pass 1: plan before coding.** Write a short design plan: 4 to 6 named hex
colours, one or two typefaces with a type scale, a one-line layout concept
with ASCII wireframes for desktop and mobile, and 3 principles on what makes
this page specific to the client.

Ground every choice in the trade's own materials and tools. Then review the
plan against this brief. If any part would look the same on any trades
website, revise it and write down what you changed and why. Avoid these
defaults unless they truly fit:

- A cream background with a serif display and a terracotta accent
- A near-black background with one neon accent
- Content chopped into identical rounded cards with the same soft shadow
- ALL CAPS eyebrow labels above every heading
- Accenting one word in a headline with italics or a different colour
- Arrows tacked onto button text
- Fade-and-slide-up animation on every section

Spend boldness in one place: one memorable hero element tied to the trade
(for Eco Shield: a drawn wall whose damp drains away while a damp meter
moves from Wet to Dry, in a dark device-like frame). Keep everything else
calm. Before you finish, remove one decoration.

**Make it feel premium, not flat:**

- Alternate section backgrounds (light, white, dark) so the page has rhythm.
- Large, tight display headings with balanced line breaks.
- Soft, layered shadows on photos, the hero element, the call-to-action band
  and the form only. Rounded corners of 6 to 12px.
- Icons in soft tinted circles.
- Buttons with a slight shadow and lift on hover (none with reduced motion).

**Copy rules.** Plain words, sentence case, active voice, short sentences,
no filler and no hype. Buttons say exactly what happens. Grade 8 reading
level. No em dashes.

**Quality floor.** No horizontal scroll from 360px up, visible keyboard
focus, `prefers-reduced-motion` respected, WCAG AA contrast, line lengths
under about 75 characters, real `<title>` and meta description, a share
image (`og:image`), LocalBusiness schema with the real details, and images
with alt text and lazy loading.

**Pass 2: build, then critique with screenshots.** Use Playwright to
screenshot at 390px and 1366px. Scroll the page first so lazy images load.
Run an axe accessibility scan. Test the toggle and the form with JavaScript
on and off. Look at the screenshots, fix what looks off, and repeat until it
looks finished.

## When you're done, give me

1. The design plan and what you changed after reviewing it.
2. The final mobile and desktop screenshots.
3. A single self-contained HTML file with the photos embedded, so I can open
   and click through it.
4. A list of every placeholder that needs real content from the owner.
5. Three to five short bullets I can send the owner on WhatsApp that say
   what's better than their current site, in plain words.
