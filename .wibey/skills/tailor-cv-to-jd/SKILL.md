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
  version: 1.1
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

## Never assume — ask

Do not silently decide anything that isn't explicitly known from the JD, the base CV, or a
prior answer from the user. This includes (non-exhaustive):
- **The job title / tagline** to display in the CV header. Never invent or reword the
  tagline (e.g. "AI-Driven Engineering Productivity...") on your own judgment — propose it
  and ask the user to confirm or correct it before it goes in the script.
- Which team/org/hiring-manager name to use in the cover letter greeting, if not stated in
  the JD (default to "Dear Hiring Manager," only after confirming no name is available/needed).
- Anything else materially uncertain (e.g. which of two plausible company names is correct,
  whether a JD requirement is a hard must-have or a nice-to-have).
When in doubt, ask a short, direct question rather than guessing.

## Workflow

### 1. Get the job description
If the user's prompt doesn't already contain the JD text, ask them directly to paste it
(plain question — this is free-form text, not a multiple-choice decision).

### 2. Identify the company
Read the JD and extract the hiring company name. If it's ambiguous or missing, ask the user
to confirm the company name before proceeding (needed for folder naming).

### 3. Clarify before drafting
Before writing any content, ask the user (one batch of short questions, not one-by-one):
- What job title/tagline should headline this CV? Show the JD's title and the base CV's
  current tagline as reference points, but let the user decide — do not pick for them.
- Anything else you're unsure about from step 2 (company name) or the JD (e.g. who to address
  the cover letter to, if a name/title is mentioned but ambiguous).
Wait for answers before proceeding to keyword extraction.

### 4. Create the output folder
Path: `cv/<DD-MM-YY>-<CompanyName>/` at the repo root, where:
- `DD-MM-YY` is **today's date** in day-month-2digit-year format (e.g. `05-09-26`).
- `CompanyName` is the company, sanitized to filesystem-safe characters (spaces →
  underscores, strip anything outside `[A-Za-z0-9_-]`).

Example: `cv/05-09-26-Acme_Corp/`

### 5. Extract JD keywords + gap check
Pull the key skills/technologies/keywords the JD emphasizes (e.g. specific languages,
frameworks, cloud platforms, architecture terms, seniority signals). Cross-reference these
against what's actually present in `generate_cv.py`. Build a short internal mapping of
"JD keyword → matching existing bullet/skill in generate_cv.py".

**Gap check (hard stop):** if the JD requires anything with no match in `generate_cv.py`
(e.g. a specific language, cloud provider, certification, methodology), do NOT silently
omit it. Stop and ask the user directly, listing each gap, e.g.:
> "The JD asks for Go and GCP — I don't see either in your base CV. Do you have relevant
> experience with these that should be included?"
- If the user confirms real experience and gives you the details, incorporate it faithfully
  (it's no longer fabrication — it's user-supplied fact).
- If the user says no / doesn't respond with real experience, only then omit that item from
  the tailored CV and cover letter.
Never fill a gap with an assumption or a plausible-sounding guess.

### 6. Generate the tailored CV script
Copy the full content of `generate_cv.py` into a new, **self-contained** script inside the
output folder (e.g. `generate_cv_<company_slug>.py`) — do not `import` from the original, so
this application's CV stays reproducible even if the base script changes later.

**Formatting must match the original exactly.** Copy the style constants, `ParagraphStyle`
definitions, colors (`DARK`/`BLUE`/`GREY`), margins (`ML`/`MR`/`MT`/`MB`), and layout helpers
(`S`, `sec`, `role_block`, `b`) byte-for-byte from `generate_cv.py`. Do not introduce new
styles, change font sizes/leading/margins, or restructure the layout functions. The only
allowed changes are:
- Bullet/skills-row **order** (which JD-relevant items come first).
- The header tagline — but only the value confirmed with the user in step 3.
- Light rewording of the summary paragraph to mirror JD terminology, using only facts
  already present (e.g. if the JD says "cloud-native" and the base mentions Azure/
  Kubernetes, "cloud-native" is a fair rephrasing — never claim a technology never
  mentioned, and never smuggle in unconfirmed gap-fills from step 5).
- Keep all real numbers/metrics exactly as-is (5×, 40%, 60% MTTR, etc.) — never alter facts.
- Set the output path inside `build()` (or via the `out` argument) to write into this same
  folder, e.g. `cv/<date>-<company>/Jacob_Tomy_CV.pdf`.

### 7. Single-page enforcement
The base script is already tuned to fit one A4 page. Because you are not changing margins,
fonts, or layout helpers (step 6), reordering alone should not change the page count. If
content still grows past one page (e.g. because the user asked to add a gap-fill bullet in
step 5), use these levers in order — never touch margins/fonts:
1. Trim a reworded/added bullet back down in length.
2. Reduce `Spacer` gaps between sections (small increments).
3. Reduce bullet `spaceAfter`.
4. As a last resort, drop the least JD-relevant bullet (never drop a bullet that supports a
   metric/skill also asked for in the JD, and never drop a bullet the user just confirmed
   in step 5).

### 8. Generate the cover letter script
Create a second self-contained script in the same folder (e.g.
`generate_cover_letter_<company_slug>.py`) that produces a PDF cover letter, reusing the same
visual language as the CV (`reportlab`, same `DARK`/`BLUE`/`GREY` colors, same margins, same
header block: name / contact line). Structure:
- Header: name + contact line (same as CV).
- Date, and the greeting confirmed in step 3 ("Dear Hiring Manager," or a named contact).
- 2-4 short paragraphs connecting specific, real experience from `generate_cv.py` (plus any
  user-confirmed gap-fills from step 5) to the JD's stated needs. No invented projects,
  employers, or skills.
- Closing + signature.
Output path: `cv/<date>-<company>/Jacob_Tomy_Cover_Letter.pdf`.

**Write it to sound like a person wrote it, not an AI:**
- Vary sentence and paragraph length; don't give every paragraph the same "topic sentence +
  three examples" shape.
- Avoid AI-cliché phrasing: "I'm particularly drawn to...", "I understand that...", "I'd
  welcome the opportunity to...", "thrive in a dynamic, fast-paced environment", "hands-on
  delivery", "seamlessly", "leverage", stacked triplets ("X, Y, and Z"), and closing lines
  that just restate the opening.
- Get to the point in the opening line instead of a windup; use "I" and contractions
  naturally; let one paragraph be short.
- No em-dash-heavy rhythm throughout — mix in periods and commas the way people actually
  write.
- Keep it concrete: name the actual project/number/outcome instead of vague enthusiasm.
- Read it back once and cut anything that sounds like a template.

### 9. Run and verify
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
- Hard-fail (and fix via the levers in step 7) if the CV is not exactly 1 page.
- Spot-check the extracted CV text contains the reordered/prioritized JD keywords and does
  **not** contain anything absent from `generate_cv.py` and unconfirmed by the user.
- Report the final folder path and both PDF paths to the user.

## Notes
- `*.pdf` is gitignored in this repo — generated PDFs stay local; no git action is needed
  unless the user explicitly asks to commit something.
- This skill only ever reads `generate_cv.py`; it never modifies it.
