# CV Project Context — Jacob Tomy
> Last updated: April 2026
> Use this file to resume work with an AI assistant in a new session.

---

## Project Overview

- **Goal:** Single-page, best-of-three CV generated programmatically via Python + ReportLab
- **Script:** `generate_cv.py` (project root)
- **Outputs:**
  - `cv/jacob_tomy_cv_intl.pdf` — for **international recruiters** (includes IIT context note)
  - `cv/jacob_tomy_cv.pdf` — for **Indian recruiters** (IIT name alone, no explanation needed)
- **Rebuild:** `python3 generate_cv.py` — always builds both variants
- **Library:** `reportlab 4.4.10` (already installed)

---

## Candidate Facts

| Field | Value |
|---|---|
| Name | Jacob Tomy |
| Email | jacobtomy721@gmail.com |
| LinkedIn | linkedin.com/in/jacob-tomy |
| Location | Bengaluru, India |
| Total Experience | 7 years |
| Current Role | Senior Software Development Engineer, Walmart Global Tech |

---

## Employment History

### Walmart Global Tech — E-Commerce · Retail
- **Senior SDE** — 2024 – Present
- **SDE III** — 2022 – 2024
- Stack: Java 21, Spring Boot 3.x, Kafka, Cosmos DB, Kubernetes, Azure, Redis, Python, LLMs
- Platform scale: **6K OPM** avg, **40K OPM** peak, **20-engineer platform**
- Express orders: **300+ OPM** (≈10% of total), handled by dedicated priority Kafka pipeline

### Clari — Revenue Intelligence · CRM
- **SDE II** — 2021 – 2022
- **SDE I** — 2019 – 2021
- Stack: Java 8, Spring Boot, PostgreSQL, MongoDB, AWS

### Samsung R&D — Mobile · Android
- **Software Engineer (Android)** — 2019 (5 months, prior FTE)
- **Removed from CV** — short tenure, irrelevant domain, no bullets

---

## Key Content Decisions & Factual Ground Truth

### AI On-Call Agent
- Tool: GPT-4o (originally GPT-4o mini, updated to GPT-4o)
- Behaviour: **surfaces context only** (runbook excerpts, incident history, live dependency state)
- Does NOT autonomously resolve incidents
- Outcome: **60% MTTR reduction**
- Earlier wrong version said "autonomously resolving 40%" — that was corrected

### Workspace Integrations (Clari)
- **One-directional only**: pulls FROM G Suite / Outlook INTO Clari
- NOT bidirectional — earlier version incorrectly said "Bidirectional Clari ↔ G Suite/Outlook"

### API Contracts
- Jacob **authored** Kafka payload schemas adopted by upstream/downstream teams
- Did NOT create the global BOM — **adopted** it and standardised it across platform

### Java Migration
- Migrated the team's own services Java 8/11 → Java 21 + Spring Boot 3.x
- Also **guided 3 other teams** through the same upgrade
- Standardised BOM adoption across the platform

### Priority Kafka Pipeline
- Dedicated lane for express orders
- Routes **300+ OPM of express orders**
- Zero additional infrastructure cost
- Express = ~10% of total order volume

### Compression
- zstd-based custom dictionary compression for Cosmos DB
- **40% storage reduction**
- Achieved — not "cut" (passive voice fixed)

### IIT Kharagpur
- India's founding technical institutes
- **Top 0.1% national admit rate**
- International CV: include parenthetical context
- Indian CV: name alone is sufficient

### M.Tech Project
- Healthcare records system
- Built in collaboration with **AIIMS clinicians**

### Generative AI Certification
- Course by **IIT Kharagpur**, delivered at Walmart
- Year: 2025–2026
- Placed in Education section (not Skills) — IIT branding makes it more impactful there

---

## CV Structure (Section Order)

1. **Header** — Name, tagline, contact
2. **Summary** — 3-sentence paragraph
3. **Experience** — Walmart (9 bullets) → Clari (3 bullets)
4. **Skills** — Single-column, 6 categories
5. **Achievements** — 2-column grid, 6 entries
6. **Education** — IIT KGP (4 rows: name, degree, M.Tech project, GenAI cert)

---

## Bullet Ordering — Walmart (Staff signals first)

1. API Contract Ownership ← **#1 Staff signal** (cross-team, platform scale)
2. Java 21 Migration ← **#2 Staff signal** (guided 3 teams, BOM standardisation)
3. AI On-Call Agent ← innovation + MTTR -60%
4. Real-time Order Amendment ← 400ms → 20ms
5. Custom Dictionary Compression ← 40% storage, cloud cost
6. Priority Kafka Pipeline ← system design, 300+ OPM
7. Pay for Speed ← business feature, no metric available
8. Container Security & CI/CD ← operational hygiene
9. Team Leadership ← last (expected, not differentiating at Staff level)

---

## Skills (Single-Column)

| Category | Values |
|---|---|
| Languages & Frameworks | Java (8, 17, 21), Spring Boot (2.7, 3.x), Python, ReactJS |
| Distributed Systems | Kafka, Kubernetes, Docker, REST APIs, Redis, Elasticsearch |
| Cloud & Infra | Azure, AWS, CI/CD (Looper), Prometheus, Grafana |
| Databases | Cosmos DB, PostgreSQL, MongoDB, Cassandra |
| AI & Tooling | LLMs, LangGraph, NL2SQL, AI Agents, Claude Code |
| Design & Delivery | HLD, LLD, API Contracts, UML, JIRA, Agile / Scrum |

**Removed from skills (intentional):**
- `Figma` — user never uses it professionally
- `GitHub Actions` — internal CI/CD is Looper; GitHub Actions not used at Walmart

---

## Achievements (2-column grid, left to right)

| # | Achievement |
|---|---|
| 1 | ★★ 2nd Prize — lablab.ai Global AI Hackathon (2026) |
| 2 | ★ Excellence Award (2025) — Walmart (zstd compression) |
| 3 | ★ Bravo Award (2025) — Walmart (AI on-call agent) |
| 4 | ★ Excellence Award (2024) — Walmart (Priority Kafka pipeline) |
| 5 | ● Walmart Global Techathon — Runner-Up (2022) |
| 6 | ● Clari Innovates Hackathon — Winner (2021) |

---

## ReportLab Technical Notes

### Known Issues & Fixes
| Issue | Fix |
|---|---|
| `▶` (U+25B6) renders as `■` | Use `●` (U+25CF) — Helvetica safe |
| Raw `&` in Paragraph strings crashes | Must use `&amp;` throughout |
| Emoji (🥈🏅) render as `■` | Use unicode-safe: `★` (U+2605), `●` (U+25CF) |
| Role title2 font mismatch | `R_TITLE2` must match `R_TITLE` exactly (Bold, 8.5pt, DARK) |
| Row height misalignment in role headers | Use flat 3-column 2-row Table, NOT nested left/right tables |
| Orphan 2–3 word last lines | Use `TA_LEFT` not `TA_JUSTIFY` for bullets and summary |

### Style Definitions (current)
```
ML=15mm, MR=15mm, MT=10mm, MB=8mm
BW = A4_width - 30mm = 180mm

NAME:    Helvetica-Bold, 20pt, DARK, center
TAGLINE: Helvetica, 8.8pt, GREY, center
CONTACT: Helvetica, 8pt, RED, center
SUMMARY: Helvetica, 8.3pt, GREY, left, leading=12.2
SEC:     Helvetica-Bold, 9.5pt, RED
CO_NAME: Helvetica-Bold, 8.8pt, RED
CO_DOM:  Helvetica-Oblique, 7.5pt, GREY
R_TITLE: Helvetica-Bold, 8.5pt, DARK
R_TITLE2:Helvetica-Bold, 8.5pt, DARK, leading=11.5
R_DATE:  Helvetica, 8.5pt, GREY, right
STACK:   Helvetica-Oblique, 8pt, GREY, leading=11
BUL:     Helvetica, 8.2pt, leading=11.2, leftIndent=8, left
SK_KEY:  Helvetica-Bold, 8.3pt
SK_VAL:  Helvetica, 8.3pt, GREY
EDU_I:   Helvetica-Bold, 8.5pt
EDU_D:   Helvetica-Oblique, 8pt, GREY
EDU_CERT:Helvetica-Oblique, 7.8pt, GREY, leading=10.5
```

### role_block() — flat table architecture
```python
# 3 columns, 2 rows — NEVER nest tables (causes row height mismatch)
col_w = [BW*0.20, BW*0.57, BW*0.23]
# Row 0: company | title1 | date1
# Row 1: domain  | title2 | date2
```

### Single-page constraint
The 1-page fit is tight. Key levers if overflow occurs:
1. Reduce `BUL` fontSize (currently 8.2 — don't go below 7.8)
2. Reduce `Spacer` values (currently 3–4pt between sections)
3. Reduce `spaceAfter` on bullets (currently 0.8)
4. Shorten a bullet's text
5. Do NOT widen margins (currently 15mm each side — minimum comfortable)

---

## Dual CV Variants

```python
build(intl=True)   # → cv/jacob_tomy_cv_intl.pdf
build(intl=False)  # → cv/jacob_tomy_cv.pdf
```

**Only difference:** IIT parenthetical in Education row 0:
- `intl=True`: "Indian Institute of Technology, Kharagpur (IIT — India's founding technical institutes, top 0.1% national admit rate)"
- `intl=False`: "Indian Institute of Technology, Kharagpur"

---

## Potential Future Improvements

- **Pay for Speed** — only bullet without a metric; add if revenue/adoption data becomes available
- **Clari Autocapture** — "200+ enterprise organisations" is a scale metric but no outcome; add conversion/efficiency stat if known
- **LinkedIn URL** — verify `linkedin.com/in/jacob-tomy` is correct before sending
- **Phone number** — not on CV currently; add if required by specific applications
- **Cover letter** — not generated yet; could be added as a second script
- **AI-targeted variant** — current CV appeals to both backend and AI roles via summary + skills; a dedicated AI-role variant could front-load AI bullets further
