---
name: progress-check
description: Scans all thesis/*.md sections, reports substantive content vs. placeholders, and writes docs/thesis-health.md.
---

# Progress Check Skill

Use this skill when the student wants to see the current state of their thesis.

## Process

1. Read each of the 10 thesis section files (thesis/00_abstract.md through thesis/09_conclusion.md).
2. For each file, determine:
   - **Done:** contains substantive content (more than just headings and placeholders)
   - **In progress:** has some content but significant placeholder text remains
   - **Empty:** contains only headings and placeholder text
3. Estimate word count per section (count non-placeholder words).
4. Identify which section to work on next based on logical thesis order and what is currently missing.
5. Write the report to docs/thesis-health.md.

## How to detect placeholder text

A section is "empty" if it contains only:
- Lines starting with `>`
- Lines containing `[placeholder]`
- Headings only (lines starting with `#`)
- The default stub text from the template

A section is "in progress" if it has at least one paragraph of original prose but also has placeholder sections.

## Output format for docs/thesis-health.md

```markdown
# Thesis Health Report

Generated: [date]

## Overall Status

[N]/10 sections have substantive content. Estimated total words: [N].

## Section Status

| Section | Status | Est. Words | Notes |
|---|---|---|---|
| 00 Abstract | [Done/In Progress/Empty] | [N] | |
| 01 Introduction | [Done/In Progress/Empty] | [N] | |
| 02 Literature Review | [Done/In Progress/Empty] | [N] | |
| 03 Research Question | [Done/In Progress/Empty] | [N] | |
| 04 Data | [Done/In Progress/Empty] | [N] | |
| 05 Methodology | [Done/In Progress/Empty] | [N] | |
| 06 Results | [Done/In Progress/Empty] | [N] | |
| 07 Robustness | [Done/In Progress/Empty] | [N] | |
| 08 Discussion | [Done/In Progress/Empty] | [N] | |
| 09 Conclusion | [Done/In Progress/Empty] | [N] | |

## What to Work on Next

[Identify the highest-priority section to work on.]

## Suggested Next Skills

[Based on what's missing, suggest 1–2 skills to run next.]
```

## Also tell the student

After writing the file, summarise the report in the conversation: overall status, the top section to work on, and the next skill to run.
