# Eco Shield: current site map

Mapped on 18 November 2026 from https://ecoshield.uk. The full page list,
with titles, descriptions and headings, is in `current-site-pages.csv`.

## Summary

His site has **49 live pages** and **1 old address** that redirects.

| Type | Count | What they are |
|---|---|---|
| Homepage | 1 | `/` |
| Service pages | 10 | The 8 services, plus 2 extra pages that overlap with them |
| Location pages | 7 | "Damp and mould survey" pages for each town |
| Case studies | 22 | Real jobs, named by town |
| Blog articles | 4 | Advice articles |
| Other pages | 3 | Blog list, Our Work list, Contact |
| Legal pages | 2 | Cookie and privacy policies |
| Old address | 1 | `/exterior-coatings-2/` already redirects to `/exterior-coatings/` |

Every one of these addresses must keep working on the new site, either as a
rebuilt page at the same address or as a redirect.

## Problems on his current site

The new site fixes all of these. Some of them are likely costing him Google
rankings now.

1. **The Salisbury page is broken.** `/damp-mould-surveys-salisbury/`
   redirects to `/damp-mould-surveys-salisbury-wiltshire/`, which shows
   "Page not found". Anyone searching for a damp survey in Salisbury who
   clicks through lands on an error.
2. **The Southampton survey page tells Google to ignore it.** Its canonical
   tag (a hidden "this is the main version" note) points at
   `/damp-proofing-and-preservation/`. Google will likely drop the
   Southampton page from results.
3. **His main damp proofing page is missing from his sitemap.**
   `/damp-proofing-and-preservation/` is live and in his menu, but his
   sitemap doesn't list it, so Google may find it later or less often.
4. **Two pages share the same title and description.** The damp proofing page
   and the floor damp proofing page are both titled "Damp Proofing &
   Treatment Southampton | Free Damp Survey | EcoShield UK". Google can't
   tell them apart, and the floor page's title doesn't mention floors.
5. **Six key pages have no main heading (H1).** The homepage, contact page,
   and the floor, ventilation, mould and roof service pages. Google uses this
   heading to understand what a page is about.
6. **Two pages have two main headings.** The Awaab's Law page and the Guildford
   case study.
7. **Many page titles end in a stray " -".** For example "Insulation Services
   Dorset and Hampshire -". The site name is missing after the dash.
8. **The privacy policy has almost no description** (just "Privacy Policy").
9. **A case study is outside his area.** "Rising Damp Solution in Guildford"
   is in Surrey. Worth asking Elliot if he still covers Surrey.

## Every page, and the plan for it

### Homepage

| Current address | Plan |
|---|---|
| `/` | Replace with the new homepage. |

### Service pages (10)

| Current address | Current title | Plan |
|---|---|---|
| `/damp-proofing-and-preservation/` | Damp Proofing & Treatment Southampton | Rebuild. Fix the title. Add to sitemap. |
| `/mould-treatment-diagnostics/` | Mould Treatment & Inspection Hampshire & Dorset | Rebuild. Add an H1. |
| `/ventilation-solutions-hampshire-dorset/` | Ventilation Solutions Hampshire & Dorset | Rebuild. Add an H1. |
| `/floor-damp-proofing-subfloor-refurbishment-services/` | Damp Proofing & Treatment Southampton (duplicate) | Rebuild. Give it its own floor title. Add an H1. |
| `/roof-repairs-upgrades/` | Roof Repairs & Roof Leak Repair Hampshire & Dorset | Rebuild. Add an H1. |
| `/insulation/` | Home Insulation Services Dorset and Hampshire | Rebuild. |
| `/exterior-coatings/` | Exterior Wall Coatings Hampshire & Dorset | Rebuild. |
| `/awaabs-law/` | Awaab's Law Explained | Rebuild. One H1. |
| `/damp-proofer/` | Damp Proofer | Overlaps with damp proofing. **Ask:** keep as its own page, or redirect to `/damp-proofing-and-preservation/`. |
| `/mould-and-condensation/` | Mould and Condensation | Overlaps with mould treatment. **Ask:** keep, or redirect to `/mould-treatment-diagnostics/`. |

Before redirecting either overlap page, check Search Console. If it brings
in Google visitors, keep it.

### Location pages (7)

| Current address | Plan |
|---|---|
| `/damp-mould-surveys-southampton/` | Rebuild. Fix the canonical so Google counts it. |
| `/damp-mould-survey-bournemouth-and-poole/` | Rebuild. |
| `/damp-mould-survey-winchester/` | Rebuild. |
| `/damp-mould-surveys-dorchester/` | Rebuild. |
| `/damp-mould-survey-portsmouth/` | Rebuild. |
| `/damp-mould-surveys-salisbury/` | Rebuild at this address. Fixes the broken redirect. |
| `/damp-proofing-and-treatment-specialists-poole/` | Rebuild. Overlaps with Bournemouth and Poole, so give it distinct content. |

These use one template with a different town each time, which makes them
quick to build. His listed towns Ringwood and Christchurch have no page yet.
They could be added later.

### Case studies (22)

Rebuild all 22 at the same addresses with one case study template: before
and after slider, the problem, the fix, the town, and a booking button.

`/black-mould-treatment-and-condensation-prevention-in-fordingbridge/`,
`/breathable-lime-plaster-restoration-in-winchester/`,
`/cavity-wall-insulation-in-bournemouth/`,
`/chimney-rebuild-lead-flashing-masonry-protection-in-blandford/`,
`/chimney-removal-ferndown/`, `/chimney-restoration-in-dorset/`,
`/damp-proofing-and-floor-renovation-in-the-new-forest/`,
`/external-facade-coating-in-ringwood/`, `/facade-coating-southampton/`,
`/fixing-penetrating-damp-in-portsmouth-with-one-coat-k-rend/`,
`/full-bungalow-refurbishment-christchurch/`, `/piv-installation-in-poole/`,
`/piv-unit-installation-in-hampshire/`,
`/rising-damp-floor-restoration-in-bournemouth/`,
`/rising-damp-solution-in-guildford/`,
`/rising-damp-treatment-in-blandford-forum-dorset/`,
`/rising-damp-treatment-in-southampton/`, `/rising-damp-treatment-ringwood/`,
`/roof-replacement-solar-installation-southbourne/`,
`/severe-black-mould-and-rising-damp-treatment-poole-bungalow/`,
`/upgrading-loft-insulation-in-christchurch/`,
`/ventilation-improvement-in-bournemouth/`

### Blog articles (4)

Rebuild all 4 at the same addresses with one article template.

`/what-is-a-piv-system-and-does-it-stop-mould/`,
`/condensation-vs-damp-how-to-tell-the-difference/`,
`/what-causes-black-mould-in-homes-and-how-to-stop-it-permanently/`,
`/awaabs-law-explained-what-southampton-landlords-need-to-know-about-damp-and-mould-compliance/`

### Other pages

| Current address | Plan |
|---|---|
| `/our-work/` | Rebuild as a grid of all case studies. |
| `/blog/` | Rebuild as a list of articles. |
| `/contact-us/` | Rebuild with the booking form, phone, WhatsApp and hours. Add an H1. |
| `/cookie-policy/` | Copy across. Update if the new site uses no cookies. |
| `/privacy-policy/` | Copy across. Update for the new form service. Add a description. |

### Redirects for the new site

| From | To |
|---|---|
| `/exterior-coatings-2/` | `/exterior-coatings/` (keep the existing redirect) |
| `/damp-mould-surveys-salisbury-wiltshire/` | `/damp-mould-surveys-salisbury/` (catches old links to the broken address) |
| `/damp-proofer/` | Only if Elliot agrees to merge it |
| `/mould-and-condensation/` | Only if Elliot agrees to merge it |

Also redirect the WordPress feed and sitemap addresses to the new sitemap,
so nothing returns an error.

## What the build needs

| Template | Pages |
|---|---|
| Homepage | 1 |
| Service page | 8 to 10 |
| Location page | 7 |
| Case study | 22 |
| Blog article | 4 |
| List pages (Our Work, Blog) | 2 |
| Contact and legal | 3 |
| **Total** | **47 to 49 pages from 6 templates** |

## Questions for Elliot

1. Keep `/damp-proofer/` and `/mould-and-condensation/` as separate pages, or merge them?
2. Does he still work in Surrey (the Guildford job)?
3. Can you get access to his Google Search Console? It shows which pages bring
   in visitors, so we protect those first.
4. Does he want location pages for Ringwood and Christchurch added?

## Notes on this map

- Built from his sitemap (`/sitemap_index.xml`) plus every internal link on
  every page. It found one live page the sitemap misses.
- It only shows what his site links to. Search Console can show other old
  addresses that still get visits. Check it before launch.
