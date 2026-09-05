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
  version: 1.7
---

# Tailor CV + Cover Letter to a Job Description

Generates a job-specific, single-page CV PDF and a matching cover-letter PDF, both derived
from the ground-truth content in `generate_cv.py` at the repo root. Nothing is invented -
tailoring means **reordering, re-weighting, and rewording existing facts**, never adding new
skills, technologies, or achievements that aren't already in `generate_cv.py`.

## Ground truth

- **Only source of truth: `generate_cv.py`** (repo root). It contains the real experience,
  bullets, skills, education, and achievements.
- **Do NOT use `CV_CONTEXT.md`** as a factual source - it is a stale planning note (last
  updated April, references old numbers/awards/margins that don't match the current script).
  It may be skimmed for style history only, never for facts.
- Never edit `generate_cv.py` itself. Always work from a **copy**.

## Character rules

Never use an em dash (`—`) or en dash (`–`) anywhere in generated text - the tailored CV
script/PDF (tagline, summary, bullets, skills) and the cover letter script/PDF. Always use a
plain hyphen (`-`) instead, including when rewording JD phrasing that itself uses an em dash.
This applies to all newly written/reworded text; do not introduce em dashes even if
`generate_cv.py` or the JD contains one elsewhere.

## No comments in generated code

The tailored CV script and the cover letter script must contain **code only** - no `#`
comments, no docstrings, no explanatory text of any kind (saves tokens on every future read).
This overrides anything elsewhere that implies carrying comments over from `generate_cv.py`:
when copying its content into the new script, strip every comment and docstring (e.g. the
module docstring, `# HEADER`, `# SUMMARY`, `# EXPERIENCE`, `# Walmart`, `# Clari`, `# SKILLS`,
`# ACHIEVEMENTS`, `# EDUCATION`, the `# RED/DARK/GREY` placeholders, etc.) - keep the actual
executable code and string content byte-for-byte, just drop every comment line. Any
explanation of what was tailored belongs only in `CHANGES.md` (step 10) and your reply to the
user, never in the script itself.

## Tone - senior, never junior-sounding

This candidate profile is senior/staff-level (see the CV's own tagline and titles). Every
piece of reworded/generated text - CV summary, CV bullets, cover letter - must read as
confident and senior. Concretely:
- **Never** phrase anything as a bare skill-listing/self-assessment: "I know Java", "I'm
  familiar with X", "I have experience in Y", "I'm good at Z". This reads junior and
  defensive, especially for a Principal/Staff-level application.
- Instead, fold the same fact into an ownership/impact statement: what was built, led,
  owned, or delivered, and in what language/stack - e.g. "built and owned large-scale
  backend systems in Java" rather than "I know Java, which is a server-side language."
- This applies even when a gap-check answer (step 5) tells you to call out an existing skill
  in place of a missing one - reframe it as something the candidate did, not something they
  merely "know."
- If a sentence would sound silly or over-explained coming from a Principal/Staff engineer
  (e.g. explaining that Java is "a server-side language"), cut the explanation - assume the
  reader already knows what the technology is.

## Never assume - ask

Do not silently decide anything that isn't explicitly known from the JD, the base CV, or a
prior answer from the user. This includes (non-exhaustive):
- **The job title / tagline** to display in the CV header. Never invent or reword the
  tagline (e.g. "AI-Driven Engineering Productivity...") on your own judgment - propose it
  and ask the user to confirm or correct it before it goes in the script.
- Which team/org/hiring-manager name to use in the cover letter greeting, if not stated in
  the JD (default to "Dear Hiring Manager," only after confirming no name is available/needed).
- Anything else materially uncertain (e.g. which of two plausible company names is correct,
  whether a JD requirement is a hard must-have or a nice-to-have).
When in doubt, ask a short, direct question rather than guessing.

## Workflow

### 1. Get the job description
If the user's prompt doesn't already contain the JD text, ask them directly to paste it
(plain question - this is free-form text, not a multiple-choice decision).

### 2. Identify the company
Read the JD and extract the hiring company name. If it's ambiguous or missing, ask the user
to confirm the company name before proceeding (needed for folder naming).

### 3. Clarify before drafting
Before writing any content, ask the user (one batch of short questions, not one-by-one):
- What job title/tagline should headline the CV itself? Show the JD's title and the base
  CV's current tagline as reference points, but let the user decide - do not pick for them.
- **What exact job title are they applying for** - this is the title used in the cover
  letter's opening line and may differ from the CV tagline (e.g. the CV tagline stays
  unchanged while the applied-for title is the JD's specific posting title). Get this as its
  own explicit answer, don't assume it equals the CV tagline.
- Anything else you're unsure about from step 2 (company name) or the JD (e.g. who to address
  the cover letter to, if a name/title is mentioned but ambiguous).
Wait for answers before proceeding to keyword extraction.

**Double-check before writing anything:** re-read back the confirmed company name and the
confirmed applied-for job title character-for-character against what the user typed. Do not
paraphrase or auto-correct either one. If the JD's team/department name (e.g. "Dev-AI") is
different from the company name (e.g. "Grab"), never conflate the two - the company name and
the applied-for title must both appear, unambiguously, wherever the cover letter states what
role is being applied for (e.g. "the <title> role at <Company>", not "...role on <team>"
alone).

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
> "The JD asks for Go and GCP - I don't see either in your base CV. Do you have relevant
> experience with these that should be included?"
- If the user confirms real experience and gives you the details, incorporate it faithfully
  (it's no longer fabrication - it's user-supplied fact).
- If the user says no / doesn't respond with real experience, only then omit that item from
  the tailored CV and cover letter.
Never fill a gap with an assumption or a plausible-sounding guess.

### 6. Generate the tailored CV script
Copy the full content of `generate_cv.py` into a new, **self-contained** script inside the
output folder (e.g. `generate_cv_<company_slug>.py`) - do not `import` from the original, so
this application's CV stays reproducible even if the base script changes later.

**Formatting must match the original exactly.** Copy the style constants, `ParagraphStyle`
definitions, colors (`DARK`/`BLUE`/`GREY`), margins (`ML`/`MR`/`MT`/`MB`), and layout helpers
(`S`, `sec`, `role_block`, `b`) byte-for-byte from `generate_cv.py`. Do not introduce new
styles, change font sizes/leading/margins, or restructure the layout functions. The only
allowed changes are:
- Bullet/skills-row **order** (which JD-relevant items come first). **If the JD is an
  AI-focused role:** do not let AI-related bullets/skills dominate the ordering just because
  the JD is AI-flavored. Keep roughly an even (50/50) split between AI-related achievements
  (e.g. the on-call agent, NL2SQL/LangGraph work) and core distributed-systems/backend
  achievements (e.g. platform ownership, migrations, Kafka/cost work) in the top few
  positions - the candidate's foundation is distributed systems, and over-indexing on AI
  content misrepresents that. Interleave the two rather than clustering all AI bullets first.
- The header tagline - but only the value confirmed with the user in step 3.
- Light rewording of the summary paragraph to mirror JD terminology, using only facts
  already present (e.g. if the JD says "cloud-native" and the base mentions Azure/
  Kubernetes, "cloud-native" is a fair rephrasing - never claim a technology never
  mentioned, and never smuggle in unconfirmed gap-fills from step 5). Follow the Tone rule
  above - fold facts into ownership/impact statements, never "I know X" style call-outs.
- Keep all real numbers/metrics exactly as-is (5×, 40%, 60% MTTR, etc.) - never alter facts.
- Set the output path inside `build()` (or via the `out` argument) to write into this same
  folder, e.g. `cv/<date>-<company>/Jacob_Tomy_CV.pdf`.

### 7. Single-page enforcement
The base script is already tuned to fit one A4 page. Because you are not changing margins,
fonts, or layout helpers (step 6), reordering alone should not change the page count. If
content still grows past one page (e.g. because the user asked to add a gap-fill bullet in
step 5), use these levers in order - never touch margins/fonts:
1. Trim a reworded/added bullet back down in length.
2. Reduce `Spacer` gaps between sections (small increments).
3. Reduce bullet `spaceAfter`.
4. As a last resort, drop the least JD-relevant bullet (never drop a bullet that supports a
   metric/skill also asked for in the JD, and never drop a bullet the user just confirmed
   in step 5).

### 8. Generate the cover letter script
Create a second self-contained script in the same folder (e.g.
`generate_cover_letter_<company_slug>.py`) that produces a PDF cover letter, reusing the same
color palette/fonts as the CV (`reportlab`, same `DARK`/`BLUE`/`GREY`, same margins) but with
its own **letter-style header, distinct from the CV's centered header**:
- Two-column header row: **name on the left** (bold, left-aligned), **contact info stacked as
  separate lines on the right** (email / linkedin / location each on their own line,
  right-aligned) - a standard business-letter layout, not the CV's centered block. **Do not
  include the GitHub link in the cover letter** (it stays on the CV only).
- Date, and the greeting confirmed in step 3 ("Dear Hiring Manager," or a named contact).
- **Opening line uses this soft, formal template** (fill in the exact confirmed applied-for
  job title from step 3 and the confirmed company name from step 2):
  > "Please accept this letter and the attached resume as an indication of my sincere
  > interest in the open position of `<title>` at `<Company>`."
  If the JD's team/department differs from the company name (e.g. "Dev-AI" at "Grab"),
  work the team in as a qualifier after the company, never as a stand-in for it (e.g.
  "...at Grab, on the Dev-AI team.") - never leave the sentence without the company name.
- 2-4 short paragraphs connecting specific, real experience from `generate_cv.py` (plus any
  user-confirmed gap-fills from step 5) to the JD's stated needs. No invented projects,
  employers, or skills. **For AI-focused roles, apply the same 50/50 balance from step 6** -
  don't fill every paragraph with AI examples; give distributed-systems/platform achievements
  equal space.
- Closing + signature.
Output path: `cv/<date>-<company>/Jacob_Tomy_Cover_Letter.pdf`.

**Write it to sound like a person wrote it, not an AI - and like a senior/staff engineer,
not a junior one (see Tone section above):**
- The opening line is the fixed soft/formal template above - it's intentionally a traditional
  windup, not a "get to the point" hook. Every paragraph *after* it should get straight to
  the substance, no further windup.
- Vary sentence and paragraph length; don't give every paragraph the same "topic sentence +
  three examples" shape.
- Avoid AI-cliché phrasing: "I'm particularly drawn to...", "I understand that...", "I'd
  welcome the opportunity to...", "thrive in a dynamic, fast-paced environment", "hands-on
  delivery", "seamlessly", "leverage", stacked triplets ("X, Y, and Z"), and closing lines
  that just restate the opening.
- Avoid junior-sounding self-assessment ("I know X", "I'm familiar with Y") - see the Tone
  section; state what was built/led/owned instead.
- Use "I" and contractions naturally in the body paragraphs; let one paragraph be short.
- No em-dash-heavy rhythm throughout - mix in periods and commas the way people actually
  write.
- Keep it concrete: name the actual project/number/outcome instead of vague enthusiasm.
- Read it back once and cut anything that sounds like a template or sounds junior.

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

### 10. Document every edit
Track every change made relative to `generate_cv.py` as you go (steps 6-8), then produce a
markdown table with exactly two columns, one row per edit:

| Before | After |
|---|---|
| Senior Software Engineer (SDE 4) · Distributed Systems & Platform Architecture · 8 Years Experience | Senior Software Engineer (SDE 4) · Distributed Systems & Platform Architecture · 8 Years Experience |
| 1. OPD Ownership 2. Cross-Org Architecture 3. Stability ... (original bullet order) | 1. Operational Intelligence 2. End-to-End Initiative 3. Cross-Org Architecture ... (reordered) |
| Languages, Backend, Cloud & Platform, Databases, AI, Architecture & Engineering (original skills order) | AI, Architecture & Engineering, Cloud & Platform, Backend, Languages, Databases (reordered) |
|  | Java called out explicitly as "a server-side language" in the summary |
| Go |  |
| GCP |  |

Rules:
- Only two columns: **Before** and **After**. No extra columns (no "reason", "section",
  "change type") - keep it to the raw diff.
- If content was **added** (e.g. a user-confirmed gap-fill, a new opening line), leave
  **Before** empty.
- If content was **removed/omitted** (e.g. a JD requirement with no match that the user chose
  not to add, per step 5), leave **After** empty.
- If content was reordered or reworded, put the original in **Before** and the new version in
  **After**.
- If something was deliberately kept unchanged (e.g. the tagline, per user confirmation),
  still include a row with the same value in both columns, so it's clear it was reviewed and
  intentionally left alone.
- One row per discrete edit - don't collapse multiple bullets/rows into one entry.

Save this table as `cv/<date>-<company>/CHANGES.md` and also paste it directly in your reply
to the user alongside the folder/PDF paths from step 9.

## Notes
- `*.pdf` is gitignored in this repo - generated PDFs stay local; no git action is needed
  unless the user explicitly asks to commit something.
- This skill only ever reads `generate_cv.py`; it never modifies it.
