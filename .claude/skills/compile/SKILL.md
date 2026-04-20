---
name: compile
description: Compiles all thesis/*.md sections into output/thesis.pdf using Pandoc and XeLaTeX. Checks prerequisites before running.
---

# Compile Skill

Use this skill when the student wants to produce a PDF from their thesis Markdown files.

## Step 1: Check prerequisites

Run the following to check prerequisites:
```bash
pandoc --version
xelatex --version
```

If either command fails:
- For pandoc: tell the student to install it from https://pandoc.org/installing.html (or brew install pandoc on macOS, winget install JohnMacFarlane.Pandoc on Windows, sudo apt install pandoc on Linux).
- For xelatex: tell the student to install TeX Live (Linux/macOS) or MiKTeX (Windows).
Do NOT proceed until both prerequisites pass.

## Step 2: Check required files

Verify these files exist:
- pandoc/thesis.yaml
- pandoc/template.latex
- docs/references.bib

If any is missing, tell the student which file is missing and how to create it.

## Step 3: Run Pandoc

Run this exact command via Bash:

```bash
pandoc   thesis/00_abstract.md   thesis/01_introduction.md   thesis/02_literature_review.md   thesis/03_research_question.md   thesis/04_data.md   thesis/05_methodology.md   thesis/06_results.md   thesis/07_robustness.md   thesis/08_discussion.md   thesis/09_conclusion.md   --metadata-file pandoc/thesis.yaml   --bibliography docs/references.bib   --citeproc   --template pandoc/template.latex   --pdf-engine=xelatex   -o output/thesis.pdf
```

## Step 4: Report result

If successful:
- Tell the student: "PDF compiled successfully → output/thesis.pdf"

If it fails:
- Show the first error line from Pandoc's stderr output.
- Diagnose the most likely cause:
  - "Undefined control sequence" → LaTeX template issue
  - "citation key not found" → key in thesis text but missing from references.bib → run /validate-references
  - "font not found" → the font in template.latex is not installed → suggest changing to a system font
  - "file not found" → one of the thesis/*.md files is missing
- Suggest the fix in plain English.
