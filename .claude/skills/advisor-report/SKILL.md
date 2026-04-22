---
name: advisor-report
description: Generate an email-ready progress report addressed to the student's advisor, based on git history since a provided date and the current state of thesis sections
---

# /advisor-report

Generates an email-ready thesis progress report addressed to your advisor, summarising what has changed since your last meeting.

## Invocation

Run `/advisor-report <date>` where `<date>` is the date of your last advisor meeting in YYYY-MM-DD format.

Example: `/advisor-report 2026-03-15`

If no date is provided, ask: "Please provide the date of your last advisor meeting (YYYY-MM-DD format)." Wait for the answer before proceeding.

## Process

### Step 1 — Read student context

Read `docs/student-profile.md`. Extract:
- Student full name
- Advisor name
- Thesis working title
- Research question

If `docs/student-profile.md` does not exist or contains only placeholder text (e.g., still reads "TBD" or has no filled-in answers), stop and tell the student:

> "Please run `/interview` first to set up your student profile before generating an advisor report."

### Step 2 — Get changed files

Run:
```bash
git log --since="<date>" --name-only --pretty=format:
```

Collect the list of file paths that appear in the output. A thesis file is any path matching `thesis/0*.md`.

If the command fails with "not a git repository", tell the student: "This folder is not a git repository. Please follow the git workflow instructions in README.md to set up git before generating an advisor report."

If the command returns no output (no commits since `<date>`), treat all sections as not changed — use the one-liner format for all substantive sections.

### Step 3 — Read all thesis sections

Read each of the following files in order:

| File | Section name |
|------|-------------|
| `thesis/00_abstract.md` | Abstract |
| `thesis/01_introduction.md` | Introduction |
| `thesis/02_literature_review.md` | Literature Review |
| `thesis/03_research_question.md` | Research Question |
| `thesis/04_data.md` | Data |
| `thesis/05_methodology.md` | Methodology |
| `thesis/06_results.md` | Results |
| `thesis/07_robustness.md` | Robustness Tests |
| `thesis/08_discussion.md` | Discussion |
| `thesis/09_conclusion.md` | Conclusion |

A thesis section is considered **changed since `<date>`** if its file path (e.g., `thesis/03_research_question.md`) appears anywhere in the git log output from Step 2.

For each section, classify as:
- **Substantive** — contains original prose beyond headings and `[placeholder]` markers. A single sentence of real text is sufficient to classify a section as Substantive. Sections with only citations and no surrounding prose, or only data tables with no narrative, count as Empty.
- **Empty** — contains only headings, `>` comment lines, or `[placeholder]` markers

### Step 4 — Write the report

Compose the report using the template below. Apply these rules strictly:

- Only describe what is actually in the thesis files. Do not invent progress or pad empty sections.
- For **substantive sections changed since `<date>`**: write one progress-framed paragraph beginning with "Since our last meeting I have..." describing the key arguments, approach, or findings in plain academic English.
- For **substantive sections NOT changed since `<date>`**: write a single line — "The [section name] was not updated since our last meeting."
- For **empty sections**: write a single line — "The [section name] has not yet been started."
- Write in first person as the student, addressed to the advisor.
- Use cautious academic language when interpreting content: "This suggests...", "The evidence is consistent with...", "A possible interpretation is..."
- Never use: "This proves...", "Clearly...", "Undoubtedly..."
- Do not claim work the student has not done.

**Report template:**

```
Subject: Thesis Progress Update — [Student Name]

Dear [Advisor Name],

I am writing to update you on the progress of my master's thesis, "[Working Title]", since our last meeting on [date].

## Progress Since [date]

### Abstract
[One paragraph or one-liner per rules above]

### Introduction
[One paragraph or one-liner per rules above]

### Literature Review
[One paragraph or one-liner per rules above]

### Research Question
[One paragraph or one-liner per rules above]

### Data
[One paragraph or one-liner per rules above]

### Methodology
[One paragraph or one-liner per rules above]

### Results
[One paragraph or one-liner per rules above]

### Robustness Tests
[One paragraph or one-liner per rules above]

### Discussion
[One paragraph or one-liner per rules above]

### Conclusion
[One paragraph or one-liner per rules above]

## Current Research Question

My research question is: [RQ from student-profile.md]

## Next Steps

[2--3 honest next steps based on which sections are still empty or in progress. Base this only on what is actually missing in the thesis files -- do not invent plans.]

Best regards,
[Student Name]
```

### Step 5 — Save

Write the completed report to `docs/advisor-report.md`.

### Step 6 — Confirm

Tell the student:

> "Your advisor report has been saved to `docs/advisor-report.md`. Please review it before sending — it reflects only what is currently written in your thesis files."
