# Your Data Model

Fill in this file **before you come to the workshop**.

Describe the data model of the product you are working on.
No perfect schema needed — just what you know. The AI fills in the gaps.

---

## Entity

What is the central object in your product?
*(Examples: Deal, Account, Order, Project, Ticket, User, Report)*

**Entity:** [YOUR ENTITY NAME]

---

## Fields

What fields does this entity have? Aim for 4–8 fields.
More than 8 makes the UI hard to use.

| Field | Type | Possible values | Description |
|---|---|---|---|
| [field_name] | string / number / date / enum | — | [What this field means] |
| [field_name] | enum | value1, value2, value3 | [What this field means] |
| [field_name] | date | — | [What this field means] |

**Type options:**
- `string` — free text (name, ID, description)
- `number` — numeric value (amount, score, count)
- `date` — date (ISO 8601: 2026-08-16)
- `enum` — fixed set of values (status, category, priority)

---

## Sample Rows

Min 20, up to 100 real or representative entries.
Real values expose gaps in your model. Placeholders don't.
Anonymize if needed.

| [field_1] | [field_2] | [field_3] | [field_4] |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

---

## Notes

Anything important to know about this model?
Any fields you're unsure about?
Any dependencies on other entities?

[Optional — free text]
