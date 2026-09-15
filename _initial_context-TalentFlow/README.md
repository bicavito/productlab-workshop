# _initial_context-TalentFlow/

This folder contains the **demo dataset** for the morning session.

TalentFlow is a fictional ATS (Applicant Tracking System) used as the live demonstration example during Session 1.

You do not need to fill anything in here. This data is already complete.

---

## What's in here

| File | What it is |
|---|---|
| `signals.csv` | 40 verbatim customer signals from TalentFlow accounts |
| `business_outcome.md` | The business metric the demo targets |
| `product_outcome.md` | The user behavior the demo targets |
| `data_model.md` | The Candidate entity with all fields and 30 sample rows |

---

## How it's used

During Session 1, Vito runs the full pipeline on this data live.
You follow along using the same files.

```
1. prompts/00_segment.md   → _context/signals_segmented.json
2. python3 bet_ranker/score.py → _context/bets.json
3. prompts/02_feature_brief.md → _context/feature_brief.md
4. prompts/03_data_model.md → data/candidates.json
5. prompts/04_first_feature.md → src/index.html, app.css, app.js
```

---

## After Session 1

Switch to `_initial_context/` and fill in your own data for the afternoon sprint.
