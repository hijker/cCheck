---
name: tailor-cv-to-jd
key: tailor-cv-to-jd
description: Generate a tailored, single-page CV and a matching PDF cover letter for a specific job description (JD), based on Jacob Tomy's base CV script (generate_cv.py) in this repo. Use when the user pastes or attaches a job description and asks to tailor a resume/CV for a job, apply to a company, or generate a cover letter. This skill is project-scoped to the cCheck repo only.
tags:
  - cv
  - resume
  - cover-letter
  - job-application
metadata:
  author: Jacob Tomy
  version: 1.0
---

# Tailor CV + Cover Letter to a Job Description

Generates a job-specific, single-page CV PDF and a matching cover-letter PDF, both derived
from the ground-truth content in `generate_cv.py` at the repo root. Nothing is invented —
tailoring means **reordering, re-weighting, and rewording existing facts**, never adding new
skills, technologies, or achievements that aren't already in `generate_cv.py`.

## Ground truth

- **Only source of truth: `generate_cv.py`** (repo root). It contains the real experience,
  bullets, skills, education, and achievements.
- **Do NOT use `CV_CONTEXT.md`** as a factual source — it is a stale planning note (last
  updated April, references old numbers/awards/margins that don't match the current script).
  It may be skimmed for style history only, never for facts.
- Never edit `generate_cv.py` itself. Always work from a **copy**.

## Workflow

### 1. Get the job description
If the user's prompt doesn't already contain the JD text, ask them directly to paste it
(plain question — this is free-form text, not a multiple-choice decision).

### 2. Identify the company
Read the JD and extract the hiring company name. If it's ambiguous or missing, ask the user
to confirm the company name before proceeding (needed for folder naming).

### 3. Create the output folder
Path: `cv/<DD-MM-YY>-<CompanyName>/` at the repo root, where:
- `DD-MM-YY` is **today's date** in day-month-2digit-year format (e.g. `05-09-26`).
- `CompanyName` is the company, sanitized to filesystem-safe characters (spaces →
  underscores, strip anything outside `[A-Za-z0-9_-]`).

Example: `cv/05-09-26-Acme_Corp/`

### 4. Extract JD keywords
Pull the key skills/technologies/keywords the JD emphasizes (e.g. specific languages,
frameworks, cloud platforms, architecture terms, seniority signals). Cross-reference these
against what's actually present in `generate_cv.py`. Build a short internal mapping of
"JD keyword → matching existing bullet/skill in generate_cv.py". Anything in the JD that has
no match in `generate_cv.py` must simply be **omitted** — never fabricated or stretched.

### 5. Generate the tailored CV script
Copy the full content of `generate_cv.py` into a new, **self-contained** script inside the
output folder (e.g. `generate_cv_<company_slug>.py`) — do not `import` from the original, so
this application's CV stays reproducible even if the base script changes later.

Tailor it using only reordering/rewording of existing content:
- Reorder bullets within each role so the ones matching JD keywords come first.
- Reorder/re-emphasize the Skills table rows so JD-relevant categories are higher/more
  prominent.
- Lightly reword the summary paragraph to mirror JD terminology, using only facts already
  present (e.g. if the JD says "cloud-native", and the base mentions Azure/Kubernetes, it's
  fine to use "cloud-native" as a rephrasing — but don't claim a technology never mentioned).
- Keep all real numbers/metrics exactly as-is (5×, 40%, 60% MTTR, etc.) — never alter facts.
- Preserve the visual style: same fonts, colors (`DARK`, `BLUE`, `GREY`), margins, and layout
  helpers (`sec`, `role_block`, `b`, `S`) from the base script.
- Set the output path inside `build()` (or via the `out` argument) to write into this same
  folder, e.g. `cv/<date>-<company>/Jacob_Tomy_CV.pdf`.

### 6. Single-page enforcement
The base script is already tuned to fit one A4 page. After tailoring, if content grew, use
the same levers documented as comments/history in the project (in priority order):
1. Trim a reworded bullet back down in length.
2. Reduce `Spacer` gaps between sections (small increments).
3. Reduce bullet `spaceAfter`.
4. As a last resort, drop the least JD-relevant bullet (never drop a bullet that supports a
   metric/skill also asked for in the JD).
Do not widen margins or shrink fonts below what's already in the base script.

### 7. Generate the cover letter script
Create a second self-contained script in the same folder (e.g.
`generate_cover_letter_<company_slug>.py`) that produces a PDF cover letter, reusing the same
visual language as the CV (`reportlab`, same `DARK`/`BLUE`/`GREY` colors, same margins, same
header block: name / contact line). Structure:
- Header: name + contact line (same as CV).
- Date, and "Dear Hiring Manager," (or a named contact if the JD provides one).
- 2-4 short paragraphs connecting specific, real experience from `generate_cv.py` to the JD's
  stated needs — using the keyword mapping built in step 4. No invented projects, employers,
  or skills.
- Closing + signature.
Output path: `cv/<date>-<company>/Jacob_Tomy_Cover_Letter.pdf`.

### 8. Run and verify
Run both scripts:
```bash
python3 "cv/<date>-<company>/generate_cv_<company_slug>.py"
python3 "cv/<date>-<company>/generate_cover_letter_<company_slug>.py"
```
Then verify the outputs with `pdfplumber` (already installed) rather than assuming success:
```python
import pdfplumber
with pdfplumber.open("cv/<date>-<company>/Jacob_Tomy_CV.pdf") as pdf:
    assert len(pdf.pages) == 1, f"CV is {len(pdf.pages)} pages, must be 1"
    text = pdf.pages[0].extract_text()
with pdfplumber.open("cv/<date>-<company>/Jacob_Tomy_Cover_Letter.pdf") as pdf:
    cl_pages = len(pdf.pages)  # should normally be 1; flag if not
```
- Hard-fail (and fix via the levers in step 6) if the CV is not exactly 1 page.
- Spot-check the extracted CV text contains the reordered/prioritized JD keywords and does
  **not** contain anything absent from `generate_cv.py`.
- Report the final folder path and both PDF paths to the user.

## Notes
- `*.pdf` is gitignored in this repo — generated PDFs stay local; no git action is needed
  unless the user explicitly asks to commit something.
- This skill only ever reads `generate_cv.py`; it never modifies it.
