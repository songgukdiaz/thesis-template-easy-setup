# Thesis Template Design Spec
**Date:** 2026-04-20  
**Project:** Master Thesis Copilot Template  
**Status:** Approved by user

---

## Overview

A GitHub template repository distributed to a cohort of master's students. Each student clones it once and customizes it via a guided interview. The template provides a complete AI-assisted thesis environment: structured writing surface, Python analysis pipeline, document compilation, and a suite of Claude Code skills and agents covering the full thesis lifecycle.

The template is purpose-built for students — not a research tool with corners sanded off. Every design decision prioritizes a student opening the repo on day one with zero prior context.

---

## Folder Structure

```
thesis-template/
├── CLAUDE.md                    ← rewritten by /interview per student
├── CLAUDE.md.template           ← original default, copied to CLAUDE.md by setup.py
├── README.md                    ← human setup instructions
├── setup.py                     ← cross-platform bootstrap script
├── requirements.txt             ← Python dependencies
├── .gitignore
├── pandoc/
│   ├── template.latex           ← Pandoc LaTeX thesis template
│   └── thesis.yaml              ← Pandoc metadata (populated by /interview)
├── thesis/
│   ├── 00_abstract.md
│   ├── 01_introduction.md
│   ├── 02_literature_review.md
│   ├── 03_research_question.md
│   ├── 04_data.md
│   ├── 05_methodology.md
│   ├── 06_results.md
│   ├── 07_robustness.md
│   ├── 08_discussion.md
│   └── 09_conclusion.md
├── code/
│   ├── 01_load_data.py
│   ├── 02_clean_data.py
│   ├── 03_analysis.py
│   └── 04_tables_figures.py
├── data/
│   ├── raw/                     ← read-only (Claude cannot edit)
│   └── clean/
├── output/
│   ├── tables/
│   ├── figures/
│   └── thesis.pdf               ← compiled output
└── docs/
    ├── student-profile.md       ← created by /interview
    ├── proposal.md              ← created by /interview
    ├── references.bib
    ├── thesis-health.md         ← created by /progress-check
    └── reference-validation.md  ← created by /validate-references
```

---

## Setup Flow

### Step 1 — `setup.py` (run once, cross-platform)

A plain Python script using stdlib only. No pip install required to run it.

**Actions:**
1. Detect OS (Windows / macOS / Linux)
2. Check prerequisites: Python 3.8+, `pandoc`, `git`, Claude Code CLI (`claude`)
3. For each missing prerequisite, print platform-specific install instructions:
   - macOS: Homebrew commands
   - Windows: winget or manual download links
   - Linux: apt/dnf commands
4. Create `.venv/` and install `requirements.txt` (pandas, matplotlib, jupyter, requests, plyer)
5. Copy `CLAUDE.md.template` → `CLAUDE.md` if `CLAUDE.md` does not already exist
6. Print: "Setup complete. Open Claude Code in this folder and run /interview to get started."

**Constraints:** No network calls beyond pip. No external APIs. Works anywhere Python 3 is installed.

### Step 2 — `/interview` skill (run once inside Claude Code)

A guided conversation (9 questions, one at a time) that bootstraps the student's environment.

**Questions:**
1. Full name and program (e.g. MSc Finance)
2. University and department
3. Supervisor name (optional — can be skipped)
4. Thesis topic or working title (open text)
5. Core research question in their own words
6. Data they have or plan to use
7. Methodology they expect to apply (open text — no forced type)
8. Programming experience level: beginner / intermediate / advanced
9. Any programming language beyond Python they want set up

**Outputs (written atomically at the end):**

- `docs/student-profile.md` — raw interview answers plus a derived profile section (thesis type inferred from methodology description, coding level, languages)
- `docs/proposal.md` — structured concept note with: working title, research question, motivation, data needed, methodology, expected contribution, main risks, supervisor pitch paragraph
- `CLAUDE.md` — full rewrite of the project instructions, baking in: student's field, topic, methodology, coding level, institutional context, and any language additions. This replaces the generic Finance-only default.

From this point forward, every Claude Code session in the project loads the student's full context automatically.

---

## Skills

All skills live in `.claude/skills/<name>/SKILL.md`.

### `/interview`
Bootstraps student profile, proposal, and CLAUDE.md. Run once. Described in Setup Flow above.

### `/literature-review`
Organizes literature streams, suggests search queries for Google Scholar / SSRN / NBER / Semantic Scholar, and positions the thesis contribution. Never invents papers, authors, journals, or years. If papers are provided, synthesizes them. If not, produces a literature map with search queries only.

**Output structure:**
- Core research area
- Key mechanism
- Literature streams table (stream / main question / typical data / what to look for)
- Missing papers: search queries only
- How to position the thesis

### `/citation-search`
Given a claim or topic from the student, returns structured search queries for major academic databases. Does not invent papers. Produces a list of search strategies the student can execute themselves, organized by database.

### `/validate-references`
Validates all citations in `thesis/*.md` against `docs/references.bib`, then attempts web verification.

**Logic:**
1. Extract all `[@key]` citation keys from thesis Markdown files
2. Cross-check against `references.bib` — flag keys present in text but missing from bib
3. For each key in bib, query Semantic Scholar public API (`api.semanticscholar.org/graph/v1/paper/search`) using title + first author — no API key required
4. Classify each reference:
   - **Confirmed** — API returned a matching result (title, author, year consistent)
   - **Unverified** — API returned no match (may still be real; student should check manually)
   - **Suspicious** — impossible year, no matching author found, title too generic to verify
5. Write a validation report to `docs/reference-validation.md`

### `/empirical-design`
Guides the student through designing an empirical strategy. Defines the dependent variable, main independent variable, controls, baseline regression specification (in text and LaTeX), identification concerns, robustness checks, and expected tables and figures. Ends with an interpretation guide explaining how to read coefficients cautiously.

### `/write-section`
Drafts a thesis section from the student's outline and notes. The student invokes the skill and provides in the same message: (1) the target section name and (2) their bullet-point notes or outline. Produces Markdown text in academic English with cautious language enforced. Does not add citations not already present in the notes.

### `/adversarial-reviewer`
Simulates a tough examiner reading the current draft. Reads the relevant `thesis/*.md` files and raises the 5 hardest questions the thesis invites — questions about methodology, data limitations, identification, contribution, and literature gaps. Does not rewrite. Does not praise. Flags overclaiming sentences specifically.

### `/data-explorer`
The student invokes the skill and provides the file path (relative to the project root, within `data/clean/`) in the same message. Reads the file and produces:
- Schema: column names, types, missing value counts
- Summary statistics for numeric columns
- Data quality flags: duplicates, outliers, implausible values
- Suggested analyses given the student's research question (read from `docs/student-profile.md`)

### `/progress-check`
Scans all `thesis/*.md` files. Reports which sections contain substantive content vs. placeholder text. Writes `docs/thesis-health.md` with: overall status, section-by-section assessment, what to work on next, and estimated completeness.

### `/compile`
Produces `output/thesis.pdf` via Pandoc.

**Logic:**
1. Verify `pandoc` and `xelatex` are on PATH; if not, print platform-specific install instructions and exit
2. Verify `pandoc/thesis.yaml` and `docs/references.bib` exist
3. Construct and run the Pandoc command via Python `subprocess`, listing all `thesis/0*.md` files in alphabetical order (so numbered filenames guarantee correct chapter sequence):
```bash
pandoc thesis/00_abstract.md thesis/01_introduction.md thesis/02_literature_review.md \
  thesis/03_research_question.md thesis/04_data.md thesis/05_methodology.md \
  thesis/06_results.md thesis/07_robustness.md thesis/08_discussion.md \
  thesis/09_conclusion.md \
  --metadata-file pandoc/thesis.yaml \
  --bibliography docs/references.bib \
  --citeproc \
  --template pandoc/template.latex \
  --pdf-engine=xelatex \
  -o output/thesis.pdf
```
4. On success: report path to PDF
5. On failure: surface first Pandoc error in plain English with a suggested fix

### `/reproducibility-check`
Checks whether the project can be reproduced by someone else. Verifies: raw data folder exists, clean data folder exists, scripts are numbered and present, output folder has content, README explains how to run, requirements.txt or environment file exists, data dictionary exists, raw vs. generated files are clearly separated. Produces a reproducibility report with missing elements and immediate fixes.

---

## Agents

Agents live in `.claude/agents/<name>.md`. They are persistent reviewers with restricted tool access.

### `literature-reviewer`
Reviews lit review sections for: idea-based organization (not paper-by-paper summary), mechanism explanation, citation support, realistic positioning for a master's thesis, and invented or unsupported citations. Returns: strengths, weaknesses, missing literature categories, revision suggestions, overclaiming sentences.

### `methods-reviewer`
Reviews methodology sections for: clear variable definitions, justified controls, appropriate fixed effects and standard errors, identification claims that are not too strong, and meaningful robustness tests. Returns: main assessment, econometric concerns, identification concerns, missing elements, suggested rewrites only if needed.

### `thesis-editor`
Edits any section for clarity, structure, concision, academic tone, and cautious language. Preserves the student's meaning and voice. Does not add citations not already present.

---

## Document Pipeline

**Writing surface:** Standard Markdown in `thesis/*.md`. Citations use `[@key]` referencing `docs/references.bib`. No LaTeX knowledge required.

**`pandoc/thesis.yaml`:** Pre-filled by `/interview` with student name, supervisor, university, date, and title. Students can edit for formatting preferences (font size, citation style, line spacing).

**`pandoc/template.latex`:** A clean thesis template providing:
- Title page (all fields from `thesis.yaml`)
- Abstract page
- Table of contents
- Chapter-level headings from `## ` Markdown headings
- Bibliography at end
- Reasonable margins and font via XeLaTeX using a widely available system font (no special package install)

---

## Settings & Permissions

**`.claude/settings.json`:**

```json
{
  "permissions": {
    "allow": [
      "Read(*)",
      "Grep(*)",
      "Glob(*)",
      "Edit(thesis/**)",
      "Edit(docs/**)",
      "Edit(output/**)",
      "Edit(code/**)",
      "Edit(pandoc/**)",
      "Edit(CLAUDE.md)",
      "Bash(python:*)",
      "Bash(pandoc:*)",
      "Bash(pip:*)",
      "Bash(git:*)",
      "Bash(ls:*)",
      "Bash(find:*)"
    ],
    "deny": [
      "Bash(rm:*)",
      "Bash(del:*)",
      "Bash(rmdir:*)",
      "Edit(data/raw/**)",
      "Edit(setup.py)",
      "Edit(.claude/**)"
    ]
  }
}
```

**Principle:** Claude can read anything. Claude can write only to student-owned zones. Raw data and the `.claude/` configuration layer are read-only.

---

## Hooks

All hooks are Python scripts (not bash) so they work identically on Windows, macOS, and Linux.

| Hook | Trigger | File | What it does |
|---|---|---|---|
| `log-action.py` | Every tool call | `.claude/hooks/log-action.py` | Appends timestamp + tool name to `.claude/logs/activity.log` |
| `protect-raw-data.py` | Pre-tool | `.claude/hooks/protect-raw-data.py` | Blocks any Edit/Write to `data/raw/**`, prints a clear warning |
| `notify.py` | Post-tool | `.claude/hooks/notify.py` | Desktop notification when `/compile` or `/validate-references` finishes, via `plyer` |

---

## Cross-Platform Considerations

- All hooks are Python, not shell scripts
- `setup.py` uses `sys.platform` to branch install instructions
- `/compile` constructs the Pandoc command via Python's `subprocess` rather than a shell script so path quoting works on Windows
- `.gitignore` includes `.venv/`, `data/raw/`, `output/thesis.pdf`, `.claude/logs/`
- `requirements.txt` pins versions for reproducibility across student machines

---

## What Is NOT in Scope

- Journal submission workflow (no cover letter, response-to-reviewers, or replication package for journals)
- R or Stata setup (Python only; student can extend manually)
- Enforced stage gates (skills are always available; no programmatic unlocking)
- Adversarial agent as a persistent reviewer (stateless skill only)
- Automated grading or supervisor-facing dashboards
