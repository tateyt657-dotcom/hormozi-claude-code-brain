# Base44 CRM Build Plan (Hormozi Money Machine CRM)

Most CRMs store contacts. This one tracks money. Every screen answers one question: where are leads leaking, and what does the team do next?

The design follows four $100M Playbooks:

- **Lead Nurture:** availability, speed, personalization, volume. Schedule rate, show rate, throughput.
- **Closing:** objection tracking and rebooking anyone who doesn't close.
- **Retention:** the 5 Horsemen (track attendance, text 2x a week, handwritten cards, events, exit interviews).
- **Lifetime Value:** upsell, downsell, and cross-sell at set moments.

---

## The pipeline

```
New Lead -> Contacted -> Booked -> Showed -> Closed -> Active Customer -> Ascended / Referred
                 |          |         |
              Nurture    No-show   Not closed -> Rebook on the spot
```

## The 8 numbers on the home screen

| Metric | Formula | Target | Source |
|---|---|---|---|
| Speed to lead | Minutes from lead created to first touch | Under 5 min | Lead Nurture, Pillar II |
| Touches per lead | Count of touch attempts | 7+ before giving up | Lead Nurture, Pillar IV |
| Schedule rate | Booked / engaged leads | Track weekly | Lead Nurture |
| Show rate | Showed / booked | Track weekly | Lead Nurture |
| Days to appointment | Booking date to appointment date | 3 days max | Lead Nurture, Pillar II |
| Close rate | Closed / showed | Track by rep | Closing |
| Monthly churn | Cancels / active customers at month start | Under 3% | Retention |
| LTV | Avg monthly revenue x avg months retained | Up every quarter | Lifetime Value |

Hormozi on speed: "A 391% increase in sales conversions occurs when leads are contacted within the first 60 seconds."

Hormozi on churn: "A reduction in churn from 9% to 3% is a 3.3x increase in lifetime value."

---

## How to build it in Base44

Don't paste one giant prompt. Base44 builds better in phases. Paste one prompt, test it, fix it, then paste the next.

### Prompt 1: Data model

```
Build a CRM called "Money Machine". Create these entities:

Lead: full_name, phone, email, source (ad, referral, organic, outbound, walk-in), ad_campaign, stage (new, contacted, booked, showed, closed_won, closed_lost, nurture, dead), owner (user), created_at, first_contact_at, speed_to_lead_minutes (calculated), touch_count, last_touch_at, main_problem, dream_outcome, budget, decision_maker (yes/no), notes, lost_reason, preferred_channel (call, text, DM, email).

Touch: lead (link), type (call, text, DM, email, voicemail), direction (outbound/inbound), outcome (no answer, left voicemail, replied, booked, not interested), note, created_by, created_at.

Appointment: lead (link), rep (user), scheduled_for, booked_at, days_out (calculated), status (scheduled, confirmed, showed, no_show, rescheduled, cancelled), outcome (closed, not closed, follow-up booked), objection (price, think about it, spouse/partner, timing, trust, other), objection_notes.

Deal: lead (link), offer (link), amount, payment_type (paid in full, payment plan, subscription), closed_by (user), closed_at.

Offer: name, price, type (core, upsell, downsell, cross-sell), description, active (yes/no).

Customer: lead (link), start_date, plan, monthly_value, status (active, at_risk, cancel_requested, cancelled, paused), last_engagement_at, engagement_this_week, next_milestone (3, 6, 12 months), referral_count, total_revenue, cancel_reason.

Task: title, related_lead or related_customer (link), assigned_to (user), due_at, priority (urgent, high, normal), type (speed to lead, follow-up, reminder, rebook, check-in, card, exit interview, referral ask, upsell), status (open, done, skipped).

Add role-based access: Admin sees everything. Rep sees only their own leads, appointments, and tasks.
```

### Prompt 2: First reply time

```
Track how long it took to make first contact with each lead:
1. When the first outbound Touch is logged on a Lead, save its time as first_contact_at.
2. Calculate speed_to_lead_minutes = first_contact_at minus created_at, in minutes.
3. Show it on each lead card as "First reply: X min". Leave it blank until the first touch is logged.
4. Add a column for it in the leads table so it can be sorted.
```

### Prompt 3: Follow-up cadence (volume)

```
Build an automatic follow-up cadence for leads that are not booked. Create Tasks on this schedule:

Day 1: call, then text right away. Double dial and text 2 more times that day, a few hours apart.
Day 2: call + text in the morning, call + DM in the afternoon.
Day 3: call + email.
Day 5: call + text.
Day 7: call + text + email.
Day 14: text.
Day 30: text. Then move the lead to "nurture".

If a lead replies on any channel, switch preferred_channel to that channel and continue the conversation there.
Stop the cadence the moment the lead books.
Show touch_count on every lead card. Flag any lead marked "dead" with fewer than 7 touches.
```

### Prompt 4: Booking and show-rate engine

```
For Appointments:
1. Only allow booking up to 3 days out. Warn the rep if they try to book further.
2. Send automated reminders 24 hours, 12 hours, and 3 hours before. Label them as automated, for example: "This is an automated reminder from [Business]."
3. Create manual reminder tasks for the rep: the night before, the morning of, and 60 minutes before. These should be sent from the rep's phone.
4. When an appointment is marked no_show, create an urgent "Rebook now" task due in 15 minutes and restart the follow-up cadence.
5. When an appointment is marked "not closed", require the rep to pick an objection and book the next appointment before saving.
```

### Prompt 5: Closing tracker

```
Build a "Closing" screen for each rep showing: appointments this week, show rate, close rate, average deal size, and revenue.
Show a chart of objections by type for the last 30 days.
When a rep selects an objection on an appointment, show a short script card for that objection that the admin can edit in settings.
Build a leaderboard ranking reps by revenue closed this month.
```

Paste your own objection scripts from `playbooks/$100M Playbook_ Closing` into the script cards.

### Prompt 6: Retention (the 5 Horsemen)

```
For Customers:
1. Track engagement. Log each time the customer uses the service (session, login, visit, or call). If engagement drops below the customer's normal weekly level, set status to at_risk and create a high-priority "Check in" task.
2. Create a task twice a week for each active customer: "Text a win or solve a problem."
3. Create a "Send handwritten card" task when the customer signs up, on their birthday, and at 3, 6, and 12 months.
4. Keep an internal event calendar. Remind the admin to plan a customer event every 42 days.
5. When status changes to cancel_requested, create an urgent "Exit interview" task. Cancellation cannot be completed until the exit interview is logged with a cancel_reason.

Build an "At Risk" screen listing every at_risk and cancel_requested customer, sorted by monthly_value.
```

### Prompt 7: LTV and ascension

```
At the 3, 6, and 12 month milestones, create two tasks: "Ask for a referral" and "Offer the upsell".
When a customer requests cancellation, show the downsell offers (lower price or lower quantity) on the exit interview screen.
Track referral_count and total_revenue per customer.
Show a cohort table: customers grouped by start month, with % still active in each month after.
```

### Prompt 8: Owner dashboard

```
Build the home dashboard for Admin with:
- The 8 numbers: speed to lead (avg minutes), touches per lead, schedule rate, show rate, average days to appointment, close rate, monthly churn, LTV.
- Each number shows this week vs last week, green if better, red if worse.
- A funnel chart: leads -> contacted -> booked -> showed -> closed, with % drop at each step. Highlight the biggest drop in red.
- Revenue by lead source and ad campaign (cost per acquired customer if ad spend is entered).
- "Money left on the table": no-shows x close rate x average deal size this month.
- Today's open urgent tasks by rep.
```

### Prompt 9: AI layer

```
Add AI features using the built-in LLM integration:
1. On each lead, a "Write my next message" button. It reads the lead's main_problem, dream_outcome, and touch history, then drafts a short personal text in a friendly tone.
2. After an appointment, a box where the rep pastes call notes. AI summarizes them, fills in objection and next steps, and suggests the best follow-up.
3. A weekly AI report for the admin: the biggest leak in the funnel and the one fix to make this week.
```

---

## Build order and what to test

1. **Prompts 1 and 2 first.** Add 5 fake leads, log a first touch on each, and confirm the first reply time shows in minutes.
2. **Prompts 3 and 4.** Book a fake appointment 5 days out and confirm the warning. Mark one as no-show and confirm the rebook task.
3. **Prompts 5 to 7.** Create a fake customer, drop their engagement, and confirm the at-risk flag.
4. **Prompts 8 and 9 last.** The dashboard only means something once data flows in.
5. **Connect lead sources.** Hook your ad forms and website form to create Leads automatically, through a webhook or Zapier. If leads are typed in by hand, speed to lead stays slow.

## Limits to check before you commit

- **SMS:** Check if your Base44 plan can send texts. If not, connect Twilio through a backend function or Zapier.
- **Calendar booking:** Base44 may not replace Calendly or GoHighLevel booking out of the box. You can embed a booking tool and sync bookings in by webhook.
- **Phone dialer:** Click-to-call opens the rep's phone. A true power dialer needs a separate tool.
- **Scale:** Base44 is great for one business or a small team. If you plan to sell this CRM to many businesses, you need multi-tenant setup (each client's data kept separate). Plan that from Prompt 1.
