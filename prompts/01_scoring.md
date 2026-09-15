# Bet Scoring Prompt

Run this prompt in your AI agent to calculate the impact scores of your initiatives and determine what to build next.

---

## What to do

Copy and paste the text below into your AI agent.

---

```
Run the Bet Ranker script to score and rank our product bets:

`python3 bet_ranker/score.py`

This script reads the segmented signals from `_context/signals_segmented.json` and uses the logic defined in `bet_ranker/score.py` to calculate a priority score for each bet. It will output the results to `_context/bets.json`.

After the script completes successfully:
1. Read the newly generated `_context/bets.json` file.
2. Present a short markdown table summarizing the top 3 ranked bets. Include:
   - Rank
   - Bet Name
   - Total Score
   - Number of Signals
   - Top Customer Size affected
3. Present the ranked list and confirm the top-ranked bet.
```
