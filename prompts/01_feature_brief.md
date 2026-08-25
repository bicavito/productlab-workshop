# Prompt 01 — Generate the Feature Brief

Use this prompt to turn your context into a concrete build target.

---

## What this does

The AI reads your three context files and your ranked bets.
It generates a Feature Brief: one focused document that defines what you build today, why, and how you know when you're done.

You review it. You correct it. Then you build from it.

---

## Before you run this

Make sure these files exist and are filled in:

| File | What it contains |
|---|---|
| `_initial_context/business_outcome.md` | What the business needs to achieve |
| `_initial_context/product_outcome.md` | What user behavior needs to change |
| `_initial_context/data_model.md` | Your product's entities and fields |
| `_context/bets.json` | Ranked bets from `score.py` |

If `_context/bets.json` is missing, run `python3 bet_ranker/score.py` first.

---

## The prompt

```
Read the following files:
- _initial_context/business_outcome.md
- _initial_context/product_outcome.md
- _initial_context/data_model.md
- _context/bets.json
- schemas/view_patterns.md

Then generate a Feature Brief for the top-ranked bet (rank 1).
Based on the bet, select the most appropriate View Pattern from view_patterns.md.

Use exactly this format:

---

# Feature Brief: [Bet title from bets.json]

## Business Outcome
[One sentence from business_outcome.md. Include the metric and timeframe.]

## Product Outcome
[One sentence from product_outcome.md. State the behavior change and why it matters.]

## The Best Bet
Bet: [title]
Score: [score] ([label])
Signals: [signal_count] signals — top customer: [top_customer_size]

## What I'm Building
[One sentence. A specific, concrete feature or view. Not a platform. Not a system. One thing.]

## What I'm NOT Building
[2–4 bullet points. Explicit scope exclusions to prevent scope creep.]

## Done Condition
[Describe the user journey moment: what does the user see, what decision do they make, what do they no longer need to do?
Format: "A [user role] opens this view and immediately [action] without [friction they had before]. They can [decision] in under [time]."
This should feel like a real product win, not a feature checklist item.]

## Data Contract
Entity: [The primary entity from data_model.md this feature targets]
Source: _initial_context/data_model.md
Required fields: [All fields the user needs to see in this view to make a decision without leaving the screen or asking someone else. Include status, temporal, and contextual fields — not just identifiers. Minimum 6 fields.]

## View
Pattern: [The selected View Pattern name, exactly as it appears in view_patterns.md]
Why this pattern: [One sentence. State the user's primary job-to-be-done and why this pattern is the right fit. Do not restate the pattern description.]
Pattern Metadata:
  [List only the metadata properties required by this pattern's "Data Structure" in view_patterns.md.
   Examples:
   - For Table:       fields: [field_key, label, filterable: true/false, badge: true/false]
   - For Kanban:      stages: [...], group_by: [field]
   - For Timeline:    sort_by: [date field], order: ascending
   - For Card Grid:   title_field: [...], subtitle_field: [...], status_field: [...]
   - For Dashboard:   metrics: [metric name, source field, aggregation: count/sum/avg]
   - For Scorecard:   dimensions: [...], weight: [...], total_field: [...]
   - For Form:        fields: [field_key, label, type: text/select/date, required: true/false]
   Do not add properties not listed for this pattern in view_patterns.md.]

## Interactions
Primary action: [The one thing a user does most often in this view — e.g., "filter by status", "click to expand row", "move card to next stage"]
Secondary action: [One supporting action, or "none"]

## Secondary View *(optional — omit entirely if not needed)*
Pattern: [A View Pattern name from view_patterns.md — or omit this section]
Why this pattern: [One sentence. Why does the secondary view add value that the primary view cannot deliver?]
Pattern Metadata:
  [Same structure as ## View — only the metadata properties required by this pattern in view_patterns.md.]
Trigger: [What user action opens the Secondary View — e.g., "Click on a table row", "Select a card"]
Build phase: Prompt 03

---

Rules:
- Use only information from the files above. Do not invent signals or outcomes.
- Choose the View Pattern with the highest feasibility that fits the feature. Never select a pattern with Low feasibility without flagging it.
- When two patterns both fit, prefer the higher-feasibility one unless the lower-feasibility pattern delivers meaningfully clearer signal to the user. Always call out the tradeoff explicitly in 'Why this pattern'.
- Pattern Metadata must exactly reflect the requirements listed in view_patterns.md for the selected pattern. Do not mix properties from different patterns.
- Keep all other sections to the word count shown. Do not expand.
- If bets.json is empty or missing, stop and tell me.
- If a Secondary View is defined, the Done Condition must be achievable with the Primary View alone. The Secondary View is never part of the Done Condition.
- Never define more than one Secondary View.
- Save the result as _context/feature_brief.md
```

---

## After you run this

Read the brief carefully. Ask yourself:

1. **Business Outcome** — Is this the metric that actually matters right now?
2. **Product Outcome** — Does this behavior change lead to that metric?
3. **The Best Bet** — Do you agree this is the right thing to build?
4. **What I'm Building** — Is this specific enough to build in one session?
5. **View Pattern** — Is the selected pattern realistic for a 50-minute sprint? (Stick to "High" or "Very High" feasibility).
6. **Done Condition** — Can you actually test this hypothesis today?

Correct anything that's wrong before you move to Prompt 02.

The brief is your contract with yourself. Build exactly this. Nothing more.
