---
name: write-section
description: Drafts a thesis section from the student's outline and notes. The student must provide the section name and their notes in the same message as /write-section.
---

# Write Section Skill

Use this skill when the student wants a draft of a specific thesis section.

## Input required

The student must provide in the same message:
1. The target section (e.g. "Introduction", "Literature Review", "Data")
2. Their bullet-point notes, outline, or raw thoughts for that section

If either is missing, ask for it before proceeding.

## Rules

- Read docs/student-profile.md before writing to understand the student's topic, RQ, data, methodology, and coding level.
- Write in clear academic English suitable for a master's thesis.
- Use cautious language throughout: "This suggests...", "The evidence is consistent with...", "A possible interpretation is..."
- Never use: "This proves...", "Clearly...", "Undoubtedly...", "Obviously..."
- Do not add citations that are not present in the student's notes.
- Do not fabricate data, results, or institutional facts.
- Preserve the student's ideas — do not introduce new arguments they didn't provide.
- Match the section's purpose (Introduction ≠ Literature Review ≠ Methodology).
- Output clean Pandoc Markdown, ready to paste into the relevant thesis/*.md file.

## Output format

Produce a complete draft of the section in Markdown, with:
- A `#` heading matching the section
- `##` subheadings where appropriate
- Inline citation placeholders `[@key]` where the student indicated a citation should go — use the exact key if provided, or a descriptive placeholder like `[@author_year]` if not
- A short note at the end: "Please review for accuracy. Check that all citation keys exist in docs/references.bib before running /compile."
