# Git Workflow & Advisor Report Design Spec
**Date:** 2026-04-20  
**Status:** Approved by user

---

## Overview

Three coordinated changes to the master thesis template:

1. **`.gitignore` update** — exclude `data/clean/` so no datasets are ever committed
2. **README git workflow section** — plain instructions for setting up a private GitHub remote and committing regularly
3. **`/advisor-report` skill** — generates an email-ready progress report addressed to the advisor, based on git history since a provided date and the current state of thesis sections

---

## Change 1: .gitignore

Replace the current data exclusion block with:

```gitignore
# Data (never commit datasets)
data/raw/
!data/raw/.gitkeep
data/clean/
!data/clean/.gitkeep
```

Both `data/raw/` and `data/clean/` are excluded. The `.gitkeep` markers are preserved so the directories exist after a fresh clone.

---

## Change 2: README git workflow section

Add a new section to `README.md` immediately before the "For the instructor" section:

```markdown
## Git workflow

Your thesis lives in a private GitHub repository. Set it up once:

1. Create a new private repo on GitHub (github.com → New repository)
2. Change the remote in this folder:
   ```bash
   git remote set-url origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
   git push -u origin master
   ```
3. Commit regularly as you write — at least after each work session
4. Push before every advisor meeting so your advisor can see your progress
5. Run /advisor-report to generate a progress email before each meeting

### What to commit

- Everything in `thesis/`, `code/`, `docs/`, `pandoc/`
- Never commit `data/` (already excluded by `.gitignore`)
```

---

## Change 3: /advisor-report skill

### File

Create `.claude/skills/advisor-report/SKILL.md`

### Invocation

The student runs `/advisor-report` and provides the date of their last advisor meeting in the same message.

Example: `/advisor-report 2026-03-15`

If no date is provided, ask for it before proceeding.

### Process

1. **Read student context** — read `docs/student-profile.md` to get: student name, advisor name, thesis topic, research question
2. **Get changed files** — run `git log --since="<date>" --name-only --pretty=format:` to list thesis files modified since the given date
3. **Read all thesis sections** — read `thesis/00_abstract.md` through `thesis/09_conclusion.md`. Classify each as:
   - **Substantive** — contains original prose beyond headings and `[placeholder]` markers
   - **Empty** — contains only headings, `>` comments, or `[placeholder]` markers
4. **Write the report** — compose an email-ready report (see Output Format below)
5. **Save** — write the report to `docs/advisor-report.md`
6. **Tell the student** — confirm the file was written and suggest they review it before sending

### Output Format

```markdown
Subject: Thesis Progress Update — [Student Name]

Dear [Advisor Name],

I am writing to update you on the progress of my master's thesis, "[Working Title]", since our last meeting on [date].

## Progress Since [date]

### [Section Name — only sections changed since date]
[For substantive sections: one progress-framed paragraph beginning with "Since our last meeting I have..."
 describing what is in the section — key arguments, approach, findings — in plain academic English.]

### [Section Name — empty or unchanged]
[One-liner: "The [section name] has not yet been started." OR "The [section name] was not updated since our last meeting."]

## Current Research Question

My research question is: [RQ from student-profile.md]

## Next Steps

[2–3 honest next steps based on which sections are still empty or in progress. Do not invent plans — base this on what is actually missing.]

Best regards,
[Student Name]
```

### Constraints

- Only describe what is actually in the thesis files. Do not invent progress or pad empty sections.
- Do not claim work the student hasn't done.
- Write in first person as the student, addressed to the advisor.
- Use cautious academic language where interpreting content.
- If `docs/student-profile.md` has not been filled in (student hasn't run `/interview`), tell the student to run `/interview` first.

---

## What is NOT in scope

- Automatically emailing the advisor
- Attaching the compiled PDF to the report
- Comparing two reports to show a diff
- Scheduling recurring reports
