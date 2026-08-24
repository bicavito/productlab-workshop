# _initial_context/

This folder is the starting point of your workshop build.

Before you write a single prompt to generate code, you build context here.
The AI can only make good decisions when it understands the problem.
This folder gives it that understanding.

---

## What goes here

Three files. You bring them. You fill them in before the build sprint.

| File | What it is | How long it takes |
|---|---|---|
| `signals.csv` | Raw customer signals you have collected | 30–60 min to fill |
| `business_outcome.md` | The business metric you want to move | 5 min |
| `product_outcome.md` | The user behavior that drives that metric | 5 min |
| `data_model.md` | Your product's data entities and fields | 10–20 min to fill |

---

## The sequence

```
1. Fill in signals.csv with real signals from your work
2. Fill in business_outcome.md
3. Fill in product_outcome.md
4. Fill in data_model.md — your product’s entities and fields
5. Open your AI agent (Claude Code, Cursor, etc.)
6. Run the segmentation prompt (bet_ranker/segment.md)
   → AI classifies each signal: type, severity, category, bet
   → Saves _context/signals_segmented.json
7. Run: python bet_ranker/score.py
   → Saves _context/bets.json
8. Open: bet_ranker/viewer/index.html — see your ranked bets
9. Run prompts/00_feature_brief.md → generates _context/feature_brief.md
10. Run prompts/01_data_model.md → generates data/[your-file].json
11. Build
```

---

## The rule

Real data only. No placeholder signals. No invented outcomes.
If you don't have the data yet, come with the problem. We find the data together.
