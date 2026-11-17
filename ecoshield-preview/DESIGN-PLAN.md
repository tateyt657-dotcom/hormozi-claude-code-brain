# Eco Shield homepage: design plan

## Concept

A surveyor's wall drawing. The page reads like a damp survey: a plain plaster
wall, ruled lines like a report, and one drawing of a wall that dries in front
of you.

## Colour

| Name | Hex | Role |
|---|---|---|
| Lime putty | `#ECEAE4` | Page background. Cool, grey-white, like fresh lime plaster. |
| Limewash | `#F8F7F3` | Form panel and placeholders. |
| Welsh slate | `#252E37` | Text, header, form section, footer. |
| Slate grey | `#56616B` | Secondary text and rules. |
| Tide mark | `#8C7B5B` | The salt line of rising damp. Used only in the wall drawing. |
| Meter green | `#2D6A4E` | The "dry" light on a damp meter. Used for the main button and the dry state only. |

Green appears in one job: "dry, fixed, book it". It is a dark, muted meter-LED
green, not a bright eco green.

## Type

One family: **Archivo** (variable width and weight).

- Display and headings: Archivo semi-condensed (`wdth` 82), weight 700. It
  echoes sign-written van lettering and builders' stencils.
- Body, labels and buttons: Archivo normal width, weight 400 and 600.

Scale (ratio 1.25, base 17px): 14 / 17 / 21 / 27 / 33 / 42, with the hero
headline at 42 to 60px through `clamp()`.

## Layout

One line: content sits on a single left edge, like text on a survey report,
with ruled lines between sections instead of boxes.

Desktop (1366px):

```
+------------------------------------------------------------------+
| Eco Shield  Damp, mould and property protection     07369 286705 |
+------------------------------------------------------------------+
| Damp and mould fixed      |  [ wall drawing: damp drains away,  ]|
| at the source.            |  [ mould fades, meter moves to Dry  ]|
| Free damp survey across.. |  [ Wet ----- Damp ----- Dry  marker ]|
| [Book a free survey] [Call]                                      |
| Rated Excellent from 41 Google reviews                           |
+------------------------------------------------------------------+
| "I had 3 damp specialists out for quotes ... cowboy vibes ..."   |
|  danielwalsh1984, Google review                                  |
+------------------------------------------------------------------+
| [photo of Elliot]  | Meet Elliot. 2 lines + review 4             |
+------------------------------------------------------------------+
| Homeowners       | Landlords and letting   | Housing             |
|                  | agents (Awaab's Law)    | associations        |
+------------------------------------------------------------------+
| Problem        | What you see                 | Service link     |
| Rising damp    | ...                          | ...              |  ruled rows
+------------------------------------------------------------------+
| 1 Survey ---- 2 Report ---- 3 Fix ---- 4 Guarantee               |
+------------------------------------------------------------------+
| [before][after]  [before][after]  [before][after]                |  case studies
+------------------------------------------------------------------+
| review 2 | review 3 | review 4 | review 5                         |
+------------------------------------------------------------------+
| SLATE: Book a free survey  | [form on limewash panel]            |
+------------------------------------------------------------------+
| SLATE footer: contact | hours | areas                            |
+------------------------------------------------------------------+
```

Mobile (390px):

```
+----------------------+
| Eco Shield    [Call] |
| Damp and mould fixed |
| at the source.       |
| Free damp survey..   |
| [Book a free survey] |
| [Call 07369 286705]  |
| Rated Excellent ..   |
| [  wall drawing   ]  |
| [Wet - Damp - Dry ]  |
|----------------------|
| "cowboy" review      |
|----------------------|
| photo / Meet Elliot  |
| Who we help (stack)  |
| Problems (stacked)   |
| Steps 1 to 4         |
| Case studies         |
| Reviews              |
| Form                 |
| Footer               |
|======================|
| [ Call ][WhatsApp ]  |  sticky
+----------------------+
```

Alignment rules:

- One left edge for all headings and text. Max content width 1160px.
- Body text capped at 62 characters wide.
- Sections split by a 1px slate-grey rule, not by cards or shadows.
- Square corners on everything except buttons (4px).
- Spacing on an 8px grid: 8, 16, 24, 40, 64, 96.

## Principles

1. **Show the fix, not the logo.** The one bold element is the hero wall: a
   tide mark and black mould that drain away while a damp-meter strip moves
   from Wet to Dry. It shows the exact before and after a customer wants.
2. **Elliot is the brand.** Customers name him in almost every review, so the
   page puts his voice, his survey and his reviews ahead of company claims.
3. **Plain like a survey report.** Ruled rows, sentence-case headings, real
   quotes word for word, and grey boxes where real photos must go. Nothing
   made up.

## Review against the brief: what I changed and why

1. **Background.** My first pick was a warm cream "lime plaster" with a serif
   headline. That is the cream, serif and terracotta default. I moved to a
   cooler grey-white lime putty and a condensed grotesk, and dropped brick red
   as an accent.
2. **Green.** My first sketch used a leaf mark and a bright green. Any eco
   company would get that. I replaced it with one dark meter green used only
   for "dry" and the main button.
3. **Services.** I had planned a grid of service cards with icons. Every
   trade site looks like that. I changed it to ruled rows sorted by the
   problem a visitor has (tide mark, wet windows, black spots), like the
   schedule in a survey report.
4. **Hero image.** I had planned a stock-style photo slot of a van or a
   technician. It would say nothing about damp. I replaced it with the wall
   drawing that dries.
5. **Cowboy review.** I considered a dark full-width band with a big quote
   mark. That would be a second bold element. I set it large on the plain
   background with a single rule, so the hero stays the only loud moment.
6. **Removed decoration.** Before finishing, I removed the coloured Google
   "G" logo beside the rating line. It added colour noise next to the main
   buttons, and it is Google's trademark. The plain text "Rated Excellent
   from 41 Google reviews" does the job.

## Changes made after screenshot reviews

- The dry wall looked like an empty box. I added a sash window that runs with
  condensation in the "before" state and clears in the "after" state.
- On mobile the wall dried before anyone scrolled to it. It now dries 1.2
  seconds after it comes into view. With reduced motion it shows dry at once.
- The tide mark crossed the window sill. I lowered it, so it reads as damp
  rising from the floor.
- The salt line looked like torn paper. I made it thinner and fainter.
- Quotes were indented by browser defaults. I removed the indent so all text
  shares one left edge.
- The cowboy review left half the desktop width empty. I set it larger and
  wider.
- The steps on mobile took a full screen each. I put the number beside the
  text.
- The Elliot photo slot was too tall on mobile. It is now 4:3 there.

