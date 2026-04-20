---
name: interview
description: One-time onboarding interview that creates student-profile.md, proposal.md, and rewrites CLAUDE.md with the student's context.
---

# Interview Skill

Use this skill when the student runs /interview for the first time (or wants to update their profile).

## Rules

- Ask questions one at a time. Wait for the student's answer before moving on.
- Never skip a question or batch multiple questions together.
- Accept vague or uncertain answers — the student may not know their methodology yet.
- At the end, write three files. Do not write any files until all questions are answered.

## Questions (ask in this order)

1. "What is your full name and what program are you in? (e.g. Jane Smith, MSc Finance)"
2. "What is the name of your university and department?"
3. "Who is your thesis supervisor? (You can skip this if you don't have one yet — just say 'skip'.)"
4. "What is your thesis topic or working title? It's fine if this is rough — we can refine it."
5. "What is the core research question you want to answer? Try to phrase it as a question."
6. "What data do you have or plan to use? (e.g. Compustat, Bloomberg, hand-collected data, survey data)"
7. "What methodology do you expect to use? (e.g. OLS regression, event study, difference-in-differences, qualitative analysis — anything is fine)"
8. "How would you describe your Python experience? Choose one: beginner / intermediate / advanced"
9. "Do you plan to use any programming language other than Python? (e.g. R, Stata, Julia — or say 'no')"

## After all questions are answered

Write the following three files using the student's answers.

### File 1: docs/student-profile.md

```markdown
# Student Profile

## Personal
- **Name:** [answer to Q1 — name only]
- **Program:** [answer to Q1 — program]
- **University:** [answer to Q2 — university]
- **Department:** [answer to Q2 — department]
- **Supervisor:** [answer to Q3, or "TBD"]

## Thesis
- **Topic:** [answer to Q4]
- **Research Question:** [answer to Q5]
- **Data:** [answer to Q6]
- **Methodology:** [answer to Q7]

## Technical
- **Python Level:** [answer to Q8]
- **Additional Languages:** [answer to Q9, or "None"]

## Derived Profile
- **Thesis Type:** [infer from Q7: empirical / theoretical / mixed / literature survey]
- **Coding Guidance:** [based on Q8: if beginner — explain code in detail; if intermediate — explain key choices; if advanced — minimal explanation]
```

### File 2: docs/proposal.md

```markdown
# Thesis Concept Note

## Working Title
[answer to Q4]

## Research Question
[answer to Q5]

## Motivation
[Write 2–3 sentences explaining why this question matters, based on the student's topic and RQ. Do not invent facts — keep this general and prompt-based.]

## Data Needed
[answer to Q6]

## Methodology
[answer to Q7]

## Expected Contribution
[Write 1–2 sentences about what the thesis could contribute, phrased cautiously.]

## Main Risks
[Identify 2–3 honest risks based on the student's data and methodology choices.]

## Next Steps
1. Run /literature-review to map the relevant literature.
2. Run /empirical-design (if empirical) to design the regression strategy.
3. Run /citation-search to find candidate papers.
4. Begin drafting thesis/02_literature_review.md.

## Supervisor Pitch
[Write 3–4 sentences the student could send to a supervisor introducing their thesis idea. Cautious, professional tone.]
```

### File 3: CLAUDE.md (full rewrite)

```markdown
# Thesis Copilot — [Student Name]

You are helping [Student Name] write their master's thesis.

## Student Context

- **Name:** [name]
- **Program:** [program] at [university]
- **Supervisor:** [supervisor or "TBD"]
- **Topic:** [topic]
- **Research Question:** [RQ]
- **Data:** [data]
- **Methodology:** [methodology]
- **Python Level:** [level]
- **Additional Languages:** [languages or "None"]

## Coding guidance

[If beginner: "Explain every code block in plain English. Define all variable names. Do not assume familiarity with pandas or statistical packages."]
[If intermediate: "Explain key design choices. You can assume familiarity with pandas and basic statistics."]
[If advanced: "Minimal explanation. Focus on correctness and efficiency."]

## Core principles

1. Do not invent citations, papers, datasets, regression results, or institutional facts.
2. Always separate what is known from project files, what is an assumption, and what needs verification.
3. Encourage reproducibility: every empirical claim should be traceable to data, code, or a cited source.
4. Keep outputs concise unless the student asks for a full draft.
5. Use cautious language: "This suggests...", "The evidence is consistent with...", "A possible interpretation is..."
6. Never use: "This proves...", "Clearly...", "Undoubtedly..."

## Thesis structure

1. Abstract — thesis/00_abstract.md
2. Introduction — thesis/01_introduction.md
3. Literature Review — thesis/02_literature_review.md
4. Research Question — thesis/03_research_question.md
5. Data — thesis/04_data.md
6. Methodology — thesis/05_methodology.md
7. Results — thesis/06_results.md
8. Robustness Tests — thesis/07_robustness.md
9. Discussion — thesis/08_discussion.md
10. Conclusion — thesis/09_conclusion.md

## Writing surface

- Write in thesis/*.md using Pandoc Markdown
- Cite with [@key] referencing docs/references.bib
- Run /compile to produce output/thesis.pdf
- Run /progress-check to see thesis health

## Workflow rule

Before creating or editing large thesis sections, produce a short plan first.
```

## After writing all three files

Tell the student:
"Setup complete. Here is your thesis concept note:

[paste the proposal.md content]

Suggested next steps:
1. Review docs/proposal.md and let me know if anything needs changing.
2. Run /literature-review to start mapping the literature.
3. Run /progress-check to see the current state of your thesis sections."
```
