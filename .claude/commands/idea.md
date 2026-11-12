---
description: Run an idea past both advisors (Hormozi + marketing) and get one combined answer
argument-hint: <your business idea>
---

The user's idea:

$ARGUMENTS

If the idea above is empty, ask the user for their idea in one short question and stop.

## Step 1: Consult both advisors at the same time

In ONE message, start both subagents with the Agent tool so they run in parallel:

1. `hormozi-advisor`: pass the full idea text. Ask for its verdict on the offer, pricing,
   sales, and scaling stage.
2. `marketing-strategist`: pass the full idea text. Ask for its verdict on buyers,
   channels, messaging, and a 30-day go-to-market plan.

Give each one any facts the user shared (revenue, price, audience, location, budget).
Do not answer before both reports come back.

## Step 2: Combine the two reports

Write one answer for the user in this shape:

```
## Bottom line
Build it, change it, or drop it. One or two sentences.

## Where both agree
The points both advisors made. These are the strongest signals.

## Where they differ
Each disagreement, what each side said, and which one you'd follow and why.

## The plan
7 to 10 numbered steps the user can start today. Merge the offer steps (Hormozi)
with the go-to-market steps (marketing). Tag each step [Hormozi] or [Marketing]
with its source file or skill.

## Numbers to hit
The targets to track for the first 30 days.

## Open questions
What's still unknown and how to find out.
```

## Rules

- Don't invent anything that isn't in the two reports.
- If an advisor couldn't find its repo, say which one and how to fix it
  (clone it next to this repo, or set `HORMOZI_BRAIN_DIR` / `MARKETING_SKILLS_DIR`).
- Short sentences, common words, no em dashes or en dashes.
