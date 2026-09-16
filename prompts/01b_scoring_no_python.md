# Prompt 01b — Score and Rank Bets (No Python Required)

Use this prompt instead of `python3 bet_ranker/score.py` if you cannot run Python on your machine.
The scoring formula is identical to score.py. All mathematical values are pre-computed below — no calculator needed.

---

## Before you run this

Make sure `_context/signals_segmented.json` exists and is filled in from Prompt 00.

---

## The prompt

```
Read the file `_context/signals_segmented.json`.

You are going to score and rank every product bet using the Fermi Leverage formula below.
Follow each step exactly. Show your work for each bet.

---

## STEP 1 — Group signals by bet

Group all signal objects by their `bet` field.
List each unique bet name and the signals that belong to it.
Count the signals per bet (n).

---

## STEP 2 — For each bet, compute the score

Use this formula:

  score = customer_weight × volume_factor

Where:

  customer_weight = log10( total_proxy_arr + 1 )
  volume_factor   = weighted_sum / sqrt( n + 5 )

And:

  total_proxy_arr = sum of ARR_PROXY[customer_size] for every signal in the bet
  weighted_sum    = sum of SIGNAL_WEIGHT[type] for every signal in the bet

---

## LOOKUP TABLE 1 — ARR_PROXY by customer_size

Use these exact values. Do not estimate.

  XL  →  10,000,000
  L   →   1,000,000
  M   →     100,000
  S   →      10,000
  XS  →       1,000

---

## LOOKUP TABLE 2 — SIGNAL_WEIGHT by type

Use these exact values. This is sqrt(TYPE_WEIGHT) — pre-calculated for you.

  deal-loss  →  5.477
  problem    →  3.162
  friction   →  1.732
  mention    →  1.000

---

## LOOKUP TABLE 3 — log10 for common total_proxy_arr values

This table covers the most common cases. Use the closest match.
If your total_proxy_arr falls between two rows, interpolate linearly
or use the row below (conservative rounding).

  total_proxy_arr         log10(total + 1)
  ─────────────────────   ────────────────
          1,000            3.000
         10,000            4.000
         11,000            4.042
         20,000            4.301
         21,000            4.322
        100,000            5.000
        101,000            5.004
        110,000            5.041
        200,000            5.301
        210,000            5.322
      1,000,000            6.000
      1,001,000            6.000
      1,010,000            6.004
      1,100,000            6.041
      2,000,000            6.301
      2,100,000            6.322
      3,000,000            6.477
     10,000,000            7.000
     10,001,000            7.000
     10,010,000            7.000
     10,100,000            7.004
     11,000,000            7.041
     20,000,000            7.301
     21,000,000            7.322
     30,000,000            7.477
     40,000,000            7.602
     50,000,000            7.699
    100,000,000            8.000

For totals not in this table: log10(N) = number of digits in N minus 1, plus a decimal fraction.
Example: log10(15,000,000) ≈ 7.176. When in doubt, round to 2 decimal places.

---

## LOOKUP TABLE 4 — sqrt(n + 5) for signal counts n = 1 to 15

  n   sqrt(n+5)
  ─   ─────────
  1     2.449
  2     2.646
  3     2.828
  4     3.000
  5     3.162
  6     3.317
  7     3.464
  8     3.606
  9     3.742
 10     3.873
 11     4.000
 12     4.123
 13     4.243
 14     4.359
 15     4.472

For n > 15: sqrt(n + 5) — compute or approximate. Each additional signal adds diminishing returns.

---

## STEP 3 — Score label

After computing score, assign a label:

  score ≥ 20.00  →  High Leverage
  score ≥ 10.00  →  Medium Leverage
  score < 10.00  →  Low Confidence

---

## STEP 4 — Rank and output

Sort all bets by score descending. Assign rank 1 to the highest.

Save the result as `_context/bets.json` in this exact format:

[
  {
    "rank": 1,
    "title": "Bet Name",
    "score": 00.00,
    "label": "High Leverage",
    "signal_count": 0,
    "top_customer_size": "XL",
    "signals": [
      { "text": "...", "type": "...", "severity": "..." }
    ]
  }
]

Where:
- score is rounded to 2 decimal places
- top_customer_size is the largest customer_size tier present in the bet's signals
  (XL > L > M > S > XS)
- signals lists each signal's raw_signal text, type, and severity

---

## STEP 5 — Confirm output

After saving, print a summary table:

  | Rank | Bet | Score | Label | Signals | Top Size |
  |------|-----|-------|-------|---------|----------|

Then confirm: "Saved to _context/bets.json. N bets scored."
```

---

## Worked example (for verification)

Use this to check the AI's math against a known case.

**Bet: "CSV Export" — 3 signals**

| Signal | Type | Size | SIGNAL_WEIGHT | ARR_PROXY |
|---|---|---|---|---|
| Signal A | deal-loss | XL | 5.477 | 10,000,000 |
| Signal B | friction | L | 1.732 | 1,000,000 |
| Signal C | mention | M | 1.000 | 100,000 |

**Step-by-step:**

1. n = 3
2. total_proxy_arr = 10,000,000 + 1,000,000 + 100,000 = 11,100,000
3. customer_weight = log10(11,100,001) ≈ 7.045
4. weighted_sum = 5.477 + 1.732 + 1.000 = 8.209
5. sqrt(n + 5) = sqrt(8) = 2.828
6. volume_factor = 8.209 / 2.828 ≈ 2.903
7. score = 7.045 × 2.903 ≈ **20.45**
8. label = **High Leverage** (≥ 20)

If your AI produces a score in the range 20.40–20.50 for this example, the formula is correct.

---

## When to use this vs. score.py

| Situation | Use |
|---|---|
| Python available (any OS) | `python3 bet_ranker/score.py` — faster, exact |
| No Python (iPad, Chromebook, locked corporate laptop) | This prompt — same formula, AI-computed |
| Checking the AI's math | Compare against the worked example above |
