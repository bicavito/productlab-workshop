# Ramp-Up Data Prompt

Run this prompt **before** starting the main workshop pipeline if you do not have real customer signals.
The AI picks a domain randomly and generates a complete `_initial_context/` with no manual input required.

**Skip this step** if you already have `signals.csv`, `business_outcome.md`, `product_outcome.md`,
and `data_model.md` in `_initial_context/`.

---

## When to run this

Run `ramp_up_data.md` if any of these are true:
- Your `_initial_context/` is empty or does not exist.
- You are exploring the pipeline with a hypothetical product.
- You want to run the full pipeline before bringing real data.

---

## The prompt

Copy everything between the triple backticks and paste it into your AI agent.

```
## Step 1 — Choose a domain

Pick ONE domain from the list below. Do not ask for input.
Use any pseudo-random heuristic available to you (timestamp, current second, etc.).
Each domain must have an equal chance of being selected.

Domain options:
1. Inventory & supply chain management (Retail / Manufacturing)
2. Field service scheduling and dispatch (Facilities / Maintenance)
3. Clinical trial participant tracking (Healthcare / Research)
4. B2B customer onboarding (SaaS / Professional Services)
5. Short-term rental property management (Hospitality)
6. Fleet and driver management (Logistics)
7. Grant application tracking (Non-profit / Government)
8. Restaurant staff scheduling (Food & Beverage)

After choosing, internally define the following — do NOT print these, just use them:
- PRODUCT NAME: a plausible SaaS product name for this domain
- TARGET USER: job title + company type (be specific)
- CORE USE CASE: one sentence, no marketing language
- PAIN POINTS: 5 realistic pain points for this domain, in the user's own words

Print only this line at the top of your output:
→ Domain chosen: [number]. [domain name]

---

## Step 2 — Generate _initial_context/

Generate all four files. Follow every rule exactly.

---

### FILE 1: _initial_context/signals.csv

Generate 30 synthetic customer signals that simulate real feedback from user interviews,
support tickets, sales calls, churn conversations, and NPS surveys.

Rules:
- Every signal must be in the customer's voice. First person. Conversational. Specific.
  Do not write abstract summaries. Write what a real user would actually say.
- Minimum signal length: 40 words. Maximum: 120 words.
- Distribute customer_size: XL (3–4), L (7–8), M (8–10), S (6–7), XS (3–4).
- Distribute type:
    deal-loss  (1–2): XL or L only. Must name a specific commercial consequence (revenue, renewal, contract).
    problem    (5–7): Critical blocker. User cannot complete their task without a painful workaround.
    friction   (18–22): Recurring annoyance, time waste, or process inefficiency.
    mention    (1–2): Passing reference, nice-to-have.
- Distribute severity: High (8–10), Medium (14–16), Low (4–6).
  High severity = real blocker or risk. Not just a preference.
- Signals must span at least 5 distinct functional themes. Do not cluster everything in one area.
- Include at least 3 signals with a named blocker (something specific preventing task completion).
- Include at least 2 signals with time-sensitive consequences (deadline, renewal at risk, competitor, audit).

CSV format — columns in this order, comma-separated:
id, raw_signal, customer_size, company_type

- id: S001 through S030
- raw_signal: signal text in double quotes. Escape internal double quotes as "".
- customer_size: XL / L / M / S / XS
- company_type: one word (e.g. SaaS, Agency, Retail, Healthcare, Government, Startup)

First line = header row. No comment lines. No extra columns.

Save as: _initial_context/signals.csv

---

### FILE 2: _initial_context/business_outcome.md

One business outcome statement. Company-level goal. Measurable and time-bound.

Format:
```
# Business Outcome

[One sentence. Metric + target + timeframe + mechanism.]
```

Rules:
- Reference a real risk from the signals (churn, expansion block, competitive loss).
- Use a specific number or percentage. "Improve retention" without a target is not acceptable.
- Derive urgency from the signals (renewal windows, compliance deadlines, competitor timelines).

Save as: _initial_context/business_outcome.md

---

### FILE 3: _initial_context/product_outcome.md

One product outcome statement. The user behavior change the product must drive.

Format:
```
# Product Outcome

[One sentence. Behavior change + metric + timeframe + business consequence.]
```

Rules:
- Name the specific action that must change. Not "users engage more" — what action, by whom, how often.
- The behavior change must be something observable in the product.
- Close with "so that [business outcome link]."

Save as: _initial_context/product_outcome.md

---

### FILE 4: _initial_context/data_model.md

The primary entity data model. This is the schema that Prompt 03 and Prompt 04 will build from.

Format:
```
# Data Model

## Primary Entity: [EntityName]

| Field | Type | Description | Example |
|---|---|---|---|
| [field_name] | [type] | [description] | [example value] |
```

Rules:
- Choose ONE primary entity — the thing the product tracks most.
  (candidate, ticket, order, shift, patient, property, application, driver, etc.)
- Include 12–18 fields total.
- Required fields (must be present, named accordingly):
    - An identity field: name or title of the entity (string)
    - A status/stage field with 5–7 named values (enum)
    - An applied_date or created_date (date)
    - A last_activity or last_updated field (date)
    - days_in_stage or days_without_movement (integer — calculated, but must be in model)
    - blocker_reason (string, nullable — reason the entity is stuck)
    - assigned_to or owner (string — the person responsible)
    - priority: enum[High, Medium, Low]
    - department or category (string — grouping dimension)
    - source (string — how it entered the system)
- All remaining fields are domain-specific. Make them realistic and useful for the app.
- Use snake_case for all field names.
- Types: string, integer, float, boolean, date, enum[value1, value2, ...]

Save as: _initial_context/data_model.md

---

## Step 3 — Summary

After generating all four files, print a summary table:

| File | Status | Key content |
|---|---|---|
| signals.csv | ✅ created | [N] signals, [N] bets, [N] deal-loss |
| business_outcome.md | ✅ created | [one-line summary] |
| product_outcome.md | ✅ created | [one-line summary] |
| data_model.md | ✅ created | Entity: [name], [N] fields |

Then list the signal themes (bets) and their signal counts.

Then flag any assumptions made that the participant should review and correct.

---

## Optional override

If you want to use your own product instead of a random domain, add this before running:

OVERRIDE:
PRODUCT NAME: [your product]
TARGET USER: [your user]
CORE USE CASE: [your use case]
PAIN POINTS: [your known pain points]

The AI will use your override instead of choosing randomly.
```

---

## After you run this

Before running `00_segment.md`, review the four generated files:

1. **signals.csv** — Do the signals sound realistic for this domain? Replace any that feel generic.
2. **business_outcome.md** — Is the metric and timeframe plausible? Adjust if needed.
3. **product_outcome.md** — Is the behavior change observable in a real product?
4. **data_model.md** — Does the primary entity and its fields make sense for this domain?

The synthetic context is a starting point, not ground truth.
The more you correct it, the better your Feature Brief and app will be.

When satisfied, run `00_segment.md`.
