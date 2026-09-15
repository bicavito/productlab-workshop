# Workshop Slides v4 — From Prompt to Product

---

## 1. From Prompt to Product
**How to Ship a Real MVP with AI.**

---

## 2. Who Am I

| Company | Result |
|---|---|
| Endress+Hauser (€3.7B) | CES 3.53 → 1.47 in 6 months |
| KSB AG (€2.9B) | +€10M digital revenue |
| Arcate (my product) | Built and shipped entirely with AI |

Same method. Same pipeline. Today you learn it.

---

## 3. Cooking = Building

**Recipes** = Prompts. Never work on first try.
**Ingredients** = Data. Bad data, bad product.
**Fermentation** = AI. Unpredictable. Steerable through constraints.

---

## 4. Vibe Coding vs. Builder Pattern

| Vibe Coding | Builder Pattern |
|---|---|
| Design before Data | Data first. Design last. |
| "Build me an Uber for X" | Sequential prompts with validation gates |
| Happy path illusion | Edge cases from real customer signals |
| Copy-paste and pray | Schema enforcement |

---

## 5. Your Day — 6 Checkpoints

| CP | What happens | When |
|---|---|---|
| 0 | Setup: repo, agent, Python | Now |
| 1 | First feature on TalentFlow demo data | Morning |
| 2 | Same feature, different user — AI adapts | Morning |
| 3 | Your data, your first feature | Afternoon |
| 4 | Second feature, connected to real data | Afternoon |
| 5 | Show it. Validate it. Take it home. | End of day |

---

## 6. CP 0 — Setup. Do This Now.

1. **Clone the repo** — scan the QR code.
2. **Open your AI agent** — Claude, Cursor, or Antigravity.
3. **Verify Python** — `python3 --version` → must show 3.x.

Stuck? Raise your hand.

---

## 7. Session 1: Watch. Then Build.

I build TalentFlow live.
Every prompt. Every mistake. Every recovery.
Then you do the same.

---

## 8. Anatomy of a Prompt — The Feature Brief

Open `prompts/02_feature_brief.md`. 279 lines. This is not a question. It is a **contract**.

Every line exists because without it, the AI produced something wrong.

| Technique | Line in the prompt | What happens without it |
|---|---|---|
| **Guardrail** | *"Copy Business Outcome verbatim. Do not rephrase."* | AI invents its own outcomes |
| **Edge-case rule** | *"Workaround outside the product = problem, not friction"* | AI classifies too many signals too low |
| **Anti-hallucination** | *"If emotional JTBD uses 'empowered'... rewrite using customer's actual language"* | Every JTBD sounds like a LinkedIn post |

A good prompt is not clever. It is **precise**.

---

## 9. Anatomy of a Prompt — The Build Prompt

Open `prompts/04_first_feature.md`. 287 lines.

| Technique | Line in the prompt | What happens without it |
|---|---|---|
| **Taste reference** | *"Does this look like Linear?"* | AI produces Bootstrap templates |
| **Forbidden list** | *"No inline styles. No SVG. No Canvas."* | AI adds random visual complexity |
| **Density rule** | *"All primary content fits without scrolling. If it doesn't, the hierarchy is wrong."* | AI creates scrolling dashboards with wasted space |

The AI has no taste. You give it taste through **constraints**.

---

## 10. CP 1 — Your Turn

Run these in order:

| Step | What happens |
|---|---|
| Prompt 00 | Segment the signals |
| Prompt 01 | Score and rank the bets |
| Prompt 02 | Generate your Feature Brief |
| Prompt 03 | Generate the dataset |
| Prompt 04 | Build the interface |

**Done when**: it renders in your browser on localhost.

---

## 11. The Prompt Sequence — Why This Order

```
Signals → Segments → Scores → Feature Brief → Dataset → Interface
  raw        structured    ranked     scoped        real       visible
```

Data first. Function second. Design last.

---

## 12. Diagnostic — Check the AI's Judgment

Open `_context/feature_brief.md`. Check four things:

1. **Signal Traceability** — JTBD backed by real quotes, or assumed?
2. **Journey Context** — Trigger is a specific frustration moment, or generic?
3. **Done Condition** — A tester can verify this today. Yes or no?
4. **Evidence Gap** — Anything in the output that has no signal behind it?

---

## 13. CP 2 — Same Data. Different User.

1. Open `_context/feature_brief.md`.
2. Change the **Target User**.
3. Re-run Prompt 04.
4. Compare.

Same data. Same problem. Different interface.

---

## 14. Why Your App Looks Different Every Time

The AI has no memory of your visual decisions. Without a constraint file, it decides fresh every iteration.

Open `schemas/design_system.md`. This is the minimum:

| What's in the schema | What's NOT in the schema |
|---|---|
| Color tokens (5-6 values) | Full brand guidelines |
| Spacing scale (4px, 8px, 12px, 16px, 24px) | Responsive breakpoints |
| Typography: 2 sizes, 2 weights | Icon library |
| Forbidden list: what the AI must never do | Component documentation |

The schema is not a design system. It is the **minimum boundary** that prevents visual drift.

**Run the audit:**
> *"Read schemas/design_system.md. Audit src/app.css and src/index.html against it. List every violation. Fix them."*

---

## 15. What the AI Needs From You

| You give | AI handles |
|---|---|
| Schema | Syntax |
| Constraints | Rendering |
| Data | Structure |
| Non-goals | Edge cases |

**Three rules:**
* 5-10 loops. Never one prompt.
* Bad data = bad product. Always.
* Constraints create speed.

---

## 16. Session 2 Prep

Before we start the afternoon sprint, open `_initial_context/`.
Make sure you have these 4 files ready for your own product:
`signals.csv` · `business_outcome.md` · `product_outcome.md` · `data_model.md`

No data? → Run `prompts/ramp_up_data.md` now.

---

## 17. Session 2: Your Data. Your Product.

This afternoon, you are on your own.
Your signals. Your context. Your MVP.
I am here to unblock you when the AI refuses to listen.

Let's build.

---

## 18. Morning Debrief — What Broke?

**Consistency:** Where did your app look wrong? Which constraint was missing?
**Stuck moments:** Where did the AI resist? What actually fixed it?

Real examples from the room.

---

## 19. Quality Gate

Three checks before you build:

1. `signals.csv` — verbatim quotes, not summaries?
2. `data_model.md` — at least 1 entity with clear attributes?
3. `business_outcome.md` — one hard metric?
4. `product_outcome.md` — one measurable behavior change?

> "If the ingredients are spoiled, we do not cook."

---

## 20. Build Sprint — 90 Minutes

| Time | Do |
|---|---|
| 0-15 | Prompt 00: Segment your signals |
| 15-25 | Prompt 01 + 02: Score bets, generate Feature Brief |
| 25-50 | Prompt 03 + 04: Dataset + Interface |
| 50-90 | Iterate. Debug. Design Audit. Make it real. |

---

## 21. When You're Stuck. Check.

| Level | Action | Question |
|---|---|---|
| **1** | **Check the Data** | Was the input wrong? |
| **2** | **Check the Constraints** | Was the prompt contradictory? |
| **3** | **Check the Step Size** | Was the jump too big? |

> "Do not argue with the model. Reset the boundary conditions."

---

## 22. CP 4 — The Second Feature

1. Review your Feature Brief and signals.
2. Pick the **second-ranked bet** from your `bets.json`.
3. Prompt the AI to build it — connected to your real dataset.
4. Run the Design Audit.

Your app now covers two testable scenarios.

---

## 23. Show & Tell — 90 Seconds Each

Show your screen.

* What did you build?
* What broke and how did you fix it?
* What will you do with it Monday?

---

## 24. Before Today vs. Monday

| Before Today | From Monday |
|---|---|
| 20-page specs in Confluence | Feature Brief + real dataset |
| Weeks waiting for design | Prototype in two hours |
| Debating assumptions | Testing against real signals |
| AI dead ends | Schema enforcement + 3-tier debugging |

---

## 25. Three Questions

1. What worked?
2. Where did you hit a wall?
3. What will you do Monday?

Tell me what didn't work and where I can improve.

---

## 26. The Kitchen is Yours

> "You have the recipes. You have the ingredients. Go cook something extraordinary."

linkedin.com/in/bica/
