# From Prompt to Product — Workshop Preparation

Prepare these four files before September 16th.

Open the `_initial_context/` folder. Fill in each file with real material from your work.

| File | What to put in | Time |
|---|---|---|
| `signals.csv` | 20–50 things customers actually said, word for word | 30–60 min |
| `business_outcome.md` | The business metric you want to move | 5 min |
| `product_outcome.md` | The user behavior that drives that metric | 5 min |
| `data_model.md` | Your product's main entities and fields | 10–15 min |

Each file has instructions inside. Read them first, then fill in your real data.

Bring your laptop with these files on September 16th.

---

Questions? Reply to the workshop email.

---

## Full instructions

### 1. Customer signals — `signals.csv`

A signal is something a customer actually said. Word for word.

Not: "Customers want better export."
But: "We've been doing this manually every Monday for three months. It takes Sarah two hours."

Open the file. You will see the format. Add 5 to 10 rows. Use real things real people said — from support tickets, sales calls, Slack messages, interviews, anything.

If you have more than 10, bring all of them. More signals give better results.

**Why we need this:** In the morning session, we run a tool that reads your signals, groups them by theme, and scores which problem is worth solving first. You will see the output live in your browser. That output tells you what to build in the afternoon.

---

### 2. Your business goal — `business_outcome.md`

Open the file. Answer three questions:
- What business number do you want to move? (churn, revenue, activation rate, anything concrete)
- What is the number today, and where do you want it to be?
- Why does this matter right now?

One sentence each. Short is better.

**Why we need this:** The tool uses your goal to check whether the highest-scoring signal actually moves the right number.

---

### 3. What you want users to do differently — `product_outcome.md`

Open the file. Answer three questions:
- What do you want users to do that they are not doing today?
- How does that behavior connect to your business goal?
- What is stopping them from doing it now?

One sentence each.

**Why we need this:** It keeps the scope honest. Features that don't change behavior don't move metrics.

---

### 4. Your product's data — `data_model.md`

Open the file. You will see a table. Fill in the rows.

What is the main "thing" your product tracks? A deal, a ticket, a customer, a report?

List 4 to 8 fields that describe it. For each field: name, type (text, number, date, or a fixed list of options), and a short description.

Add 3 to 5 real rows at the bottom. Use real values, not "example" or "test".

**Why we need this:** In the afternoon, you build your own app. This is the data it runs on. The more real your data, the more useful the app.

---

### What to bring on the day

- Laptop
- Claude or Cursor (active subscription, logged in)
- Python 3 (pre-installed on Mac — check: `python3 --version` in Terminal)
- The four files filled in with real data

---

### If you are stuck

Reply to the workshop email. I will help you figure it out.

The signals file is the hardest one. If you only have time for one, start there.
