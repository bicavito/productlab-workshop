# Bet Ranker

Reads your customer signals, scores them by strategic impact, and shows a ranked list of bets in the browser.

The scoring mirrors Arcate's Fermi Leverage Model.

---

## How it works

```
_initial_context/signals.csv  (your raw signals)
        ↓
   Step 1: Segmentation Prompt (AI agent)
        ↓
_initial_context/signals_segmented.csv  (structured signals)
        ↓
   Step 2: score.py  (pure Python 3, no dependencies)
        ↓
 viewer/bets.json
        ↓
 viewer/index.html  (open in browser)
```

---

## Step 1: Segment your signals (AI agent)

Open `prompts/00_segment.md` and follow the instructions.

The prompt tells your AI agent to read `_initial_context/signals.csv` and classify each signal:
- **type** — deal-loss / problem / friction / mention
- **severity** — High / Medium / Low
- **category** — feature / workflow
- **bet** — the initiative this signal is evidence for

Output: `_context/signals_segmented.json`

---

## Step 2: Score

Run from the `starter-repo/` root:

```bash
python3 bet_ranker/score.py
```

Output: `_context/bets.json`

---

## Step 3: View

Open in your browser:

```
bet_ranker/viewer/index.html
```

Or via XAMPP: `http://localhost/productlab_Workshop/starter-repo-simulation/bet_ranker/viewer/index.html`

**Bet #1 is your starting point for the build.**

---

## Scoring model (Arcate Fermi Leverage, simplified)

Per signal:

```
contribution = √(type_weight) × severity_weight
```

Per bet:

```
weighted_sum    = Σ contribution across all signals
customer_weight = max(SIZE_WEIGHT) across linked customers
volume_factor   = weighted_sum / √(n + 5)
score           = customer_weight × volume_factor
```

| Type | Weight | Severity | Weight | Customer Size | Weight |
|---|---|---|---|---|---|
| deal-loss | 30 | High | 3 | XL | 100 |
| problem | 10 | Medium | 2 | L | 30 |
| friction | 3 | Low | 1 | M | 10 |
| mention | 1 | | | S | 3 |
| | | | | XS | 1 |

| Score | Label |
|---|---|
| ≥ 50 | High Leverage |
| ≥ 15 | Medium Leverage |
| < 15 | Low Confidence |
