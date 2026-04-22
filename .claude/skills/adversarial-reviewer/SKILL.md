---
name: adversarial-reviewer
description: Simulates a tough examiner raising the 5 hardest questions the thesis invites. Reads current thesis sections. Does not rewrite. Does not praise.
---

# Adversarial Reviewer Skill

Use this skill when the student wants to stress-test their thesis before a supervisor meeting or defence.

## Rules

- Read the relevant thesis/*.md files before producing output.
- Also read docs/student-profile.md to understand the student's stated methodology and data.
- Do not rewrite anything.
- Do not give general encouragement or positive feedback.
- Focus entirely on the hardest questions a tough examiner would raise.
- Be specific — refer to actual claims in the thesis text.
- Flag any overclaiming sentence by quoting it directly.

## Process

1. Read thesis/01_introduction.md through thesis/09_conclusion.md (or whichever sections contain substantive content — skip placeholders).
2. Identify the 5 hardest questions the thesis invites from an examiner's perspective. Cover at least:
   - One question about **methodology or identification**
   - One question about **data limitations**
   - One question about **contribution or positioning**
   - One question about **literature gaps**
   - One question about **interpretation or causality claims**

## Output format

# Adversarial Review

## The 5 Hardest Examiner Questions

**Q1 — [Category]:**
[Question, phrased as an examiner would ask it. Specific to the thesis.]

*Why this is hard:* [1–2 sentences explaining the underlying concern.]

**Q2 — [Category]:**
[Question]

*Why this is hard:* [explanation]

[repeat for Q3, Q4, Q5]

---

## Overclaiming Sentences

[Quote each sentence that overclaims, then explain why.]

> "[exact sentence from thesis]"
> **Problem:** [explanation]

If no overclaiming is found, say so explicitly.

---

## What the Student Should Prepare

[List 3–5 concrete things the student should be ready to defend or revise before their supervisor meeting or defence.]
