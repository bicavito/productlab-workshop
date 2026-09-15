# Your Data Model

Fill in this file **before you come to the workshop**.

Describe the data model of the product you are working on.
No perfect schema needed — just what you know. The AI fills in the gaps.

---

## Entity

What is the central object in your product?
*(Examples: Deal, Account, Order, Project, Ticket, User, Report)*

**Entity:** Candidate

---

## Fields

What fields does this entity have?

List **all** fields your product actually tracks for this entity. Don't filter — the AI will select what's relevant for the view it builds.

For each field, ask: "Does a user ever need to see this to make a decision about this item?" If yes, include it.

A typical B2B entity has 10–20 meaningful fields. Fewer than 8 usually means you've left out something important.

| Field | Type | Possible values | Description |
|---|---|---|---|
| candidate_name | string | — | Full name of the applicant |
| job_title | string | — | The position they applied for |
| department | enum | Engineering, Product, Sales, Marketing, HR | Department the role belongs to |
| stage | enum | Applied, Screening, Interview, Offer, Hired, Rejected | Current pipeline stage |
| source | enum | LinkedIn, Job Board, Referral, Career Page, Agency | How the candidate entered the pipeline |
| applied_date | date | — | Date the application was received |
| last_contact | date | — | Last time we communicated with them |
| recruiter | string | — | Assigned recruiter |
| hiring_manager | string | — | Manager deciding on this hire |
| days_in_stage | number | — | Number of days since last stage change |
| priority | enum | High, Medium, Low | Urgency or strategic importance of this hire |
| fit_score | number | 1-10 | Aggregated score from interviewers |
| salary_expectation | number | — | Annual salary expectation in EUR |
| blocker_reason | string | — | Why the candidate is stuck (if any) |
| interview_feedback | string | — | Snippet of the latest feedback |

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

Include rows that show your real edge cases: items that are stuck, overdue, blocked, escalated, or in terminal states (closed, rejected, cancelled). These are the rows that make your app useful — not the clean success cases.

| candidate_name | job_title | department | stage | source | applied_date | last_contact | recruiter | hiring_manager | days_in_stage | priority | fit_score | salary_expectation | blocker_reason | interview_feedback |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lena Kowalski | Senior Backend | Engineering | Interview | LinkedIn | 2026-07-15 | 2026-08-20 | Sarah Chen | David Kim | 8 | High | 8.5 | 110000 | — | "Strong technical skills, good system design" |
| Marcus Rivera | Product Designer | Product | Screening | Career Page | 2026-08-02 | 2026-08-22 | Sarah Chen | Elena Rostova | 5 | Medium | 7.0 | 85000 | — | "Portfolio looks promising, schedule call" |
| Priya Nair | Eng Manager | Engineering | Offer | Referral | 2026-06-28 | 2026-08-24 | Tom Bradley | David Kim | 3 | High | 9.5 | 140000 | Waiting for candidate signature | "Exceptional leadership qualities" |
| Jonas Weber | Sales Manager | Sales | Applied | Job Board | 2026-08-18 | 2026-08-18 | Sarah Chen | Mark Johnson | 2 | Medium | — | 70000 | — | — |
| Fatima Al-Rashid | Data Analyst | Product | Interview | LinkedIn | 2026-07-22 | 2026-08-10 | Maria Lopez | Elena Rostova | 12 | Medium | 6.5 | 65000 | Waiting on Hiring Manager | "Needs to show more SQL depth" |
| Kevin O'Brien | DevOps Eng | Engineering | Screening | Agency | 2026-08-10 | 2026-08-25 | Tom Bradley | David Kim | 6 | High | 8.0 | 100000 | — | "Agency says he's interviewing elsewhere" |
| Aisha Mbeki | CS Lead | Sales | Hired | Referral | 2026-05-15 | 2026-07-01 | Maria Lopez | Mark Johnson | 0 | Low | 9.0 | 95000 | — | "Perfect fit, accepted offer" |
| Daniel Svensson | Frontend Dev | Engineering | Rejected | Career Page | 2026-07-01 | 2026-07-10 | Sarah Chen | David Kim | 0 | Low | 4.0 | 90000 | — | "Failed technical assessment" |
| Clara Zhang | Product Manager | Product | Interview | LinkedIn | 2026-07-28 | 2026-08-15 | Tom Bradley | Elena Rostova | 14 | High | 8.5 | 105000 | Salary mismatch | "Great PM, but wants 20% above band" |
| Raj Patel | QA Engineer | Engineering | Applied | Job Board | 2026-08-20 | 2026-08-21 | Maria Lopez | David Kim | 1 | Low | — | 60000 | — | — |
| Sophie Moreau | UX Researcher | Product | Screening | LinkedIn | 2026-08-05 | 2026-08-15 | Sarah Chen | Elena Rostova | 11 | Medium | 7.5 | 75000 | Missing assignment | "Sent test on 15th, still waiting" |
| Ibrahim Hassan | Sol. Architect | Engineering | Interview | Agency | 2026-07-10 | 2026-08-05 | Tom Bradley | David Kim | 22 | High | 9.0 | 130000 | Visa sponsorship needed | "Excellent, but legal is checking visa status" |
| Elena Petrov | Tech Writer | Product | Applied | Career Page | 2026-08-19 | 2026-08-19 | Maria Lopez | Elena Rostova | 3 | Low | — | 55000 | — | — |
| Nathan Brooks | Head of Eng | Engineering | Offer | Referral | 2026-06-15 | 2026-08-20 | Tom Bradley | CEO | 7 | High | 9.5 | 160000 | — | "Unanimous yes from the board" |
| Yuki Tanaka | Mobile Dev | Engineering | Screening | LinkedIn | 2026-08-08 | 2026-08-18 | Sarah Chen | David Kim | 9 | Medium | 7.0 | 85000 | — | "Looks solid, let's proceed to tech round" |
| Olivia Schmidt | HR Partner | HR | Interview | Job Board | 2026-07-18 | 2026-08-10 | Maria Lopez | HR Director | 15 | Medium | 6.0 | 80000 | Waiting on Hiring Manager | "Needs 2nd round, HM is on vacation" |
| Luis Hernandez | Backend Dev | Engineering | Applied | Career Page | 2026-08-21 | 2026-08-21 | Tom Bradley | David Kim | 1 | Medium | — | 95000 | — | — |
| Anna Kowalczyk | Data Engineer | Product | Rejected | LinkedIn | 2026-06-20 | 2026-07-05 | Sarah Chen | Elena Rostova | 0 | Low | 5.5 | 100000 | — | "Lacks cloud experience" |
| James Okafor | Account Exec | Sales | Screening | Agency | 2026-08-01 | 2026-08-10 | Maria Lopez | Mark Johnson | 14 | High | 8.0 | 85000 | No response | "Emailed twice, candidate ghosting" |
| Mia Chen | Product Designer | Product | Interview | Referral | 2026-07-25 | 2026-08-20 | Sarah Chen | Elena Rostova | 10 | Medium | 8.5 | 90000 | — | "Strong visual skills, team liked her" |
| Viktor Novak | SRE | Engineering | Applied | LinkedIn | 2026-08-22 | 2026-08-22 | Tom Bradley | David Kim | 0 | High | — | 115000 | — | — |
| Sarah Kim | Marketing Mgr | Marketing | Hired | Job Board | 2026-05-30 | 2026-06-20 | Maria Lopez | CMO | 0 | Low | 8.5 | 95000 | — | "Started last week" |
| Thomas Müller | Fullstack Dev | Engineering | Screening | Career Page | 2026-08-12 | 2026-08-21 | Tom Bradley | David Kim | 4 | Medium | 7.5 | 85000 | — | "Passed screening, scheduled coding test" |
| Amara Johnson | Chief of Staff | Operations | Interview | Referral | 2026-07-05 | 2026-08-05 | Tom Bradley | CEO | 28 | High | 8.0 | 130000 | Background check pending | "Final stage, waiting on references" |
| Roberto Silva | Support Eng | Engineering | Applied | Job Board | 2026-08-23 | 2026-08-23 | Maria Lopez | David Kim | 0 | Low | — | 65000 | — | — |
| Nadia Volkov | Security Eng | Engineering | Offer | LinkedIn | 2026-07-01 | 2026-08-24 | Sarah Chen | David Kim | 5 | High | 9.0 | 125000 | — | "Verbal acceptance, contract sent" |
| Patrick Dubois | SDR | Sales | Rejected | Agency | 2026-06-10 | 2026-06-25 | Maria Lopez | Mark Johnson | 0 | Low | 4.5 | 50000 | — | "Not enough B2B experience" |
| Hana Yoshida | Design Sys Lead| Product | Screening | LinkedIn | 2026-08-06 | 2026-08-16 | Sarah Chen | Elena Rostova | 10 | High | 9.0 | 110000 | Missing assignment | "Requested Figma file, pending" |
| Christian Bauer | VP Sales | Sales | Interview | Referral | 2026-07-20 | 2026-08-18 | Tom Bradley | CEO | 16 | High | 8.5 | 180000 | Compensation negotiation | "Counter-offered, needs CEO approval" |
| Emily Watson | Junior Dev | Engineering | Applied | Career Page | 2026-08-24 | 2026-08-24 | Sarah Chen | David Kim | 0 | Low | — | 55000 | — | — |

---

## Notes

Anything important to know about this model?
Any fields you're unsure about?
Any dependencies on other entities?

The "days_in_stage" field is calculated, not entered manually. When a candidate moves to a new stage, it resets to 0. Candidates stuck at high days_in_stage (>14) are usually a problem — either the hiring manager hasn't given feedback or the recruiter is overloaded.

We have cross-dependencies with the "Department" budget (each department has a specific headcount allowed) and the "Hiring Manager" (who is an Employee entity in our main system).
