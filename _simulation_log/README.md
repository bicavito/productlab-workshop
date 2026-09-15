# Simulation Log

This directory captures what happened at each step of the workshop pipeline simulation.

Use it to identify where prompts need improvement for the Afternoon Session (QA & Optimization).

---

## How to use

After running each step, fill in the corresponding log file.
Use the template in each file. Be honest about what broke.

| File | Fill after |
|---|---|
| `step_0_segmentation.md` | Running segment.md (AI classifies signals) |
| `step_1_scoring.md` | Running score.py (bets ranked) |
| `step_2_feature_brief.md` | Running Prompt 00 (feature brief generated) |
| `step_3_dataset.md` | Running Prompt 01 (JSON dataset generated) |
| `step_4_wireframe.md` | Running Prompt 02 (wireframe built) |
| `step_5_design.md` | Running Prompt 04 (design system applied) |
| `issues.md` | Ongoing — running list of all issues |
