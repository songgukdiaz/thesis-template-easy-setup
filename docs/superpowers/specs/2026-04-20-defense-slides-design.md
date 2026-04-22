# Defense Slides Design Spec
**Date:** 2026-04-20  
**Status:** Approved by user

---

## Overview

A single skill (`/defense-slides`) that reads the student's thesis sections and `docs/student-profile.md`, generates a populated LaTeX Beamer presentation (`output/defense.tex`), and attempts to compile it to `output/defense.pdf`. Designed for a 20-minute thesis defense (~16 slides). No agent required.

---

## Invocation

```
/defense-slides
```

No arguments. The skill reads all required context from existing project files. If `docs/student-profile.md` has not been filled in, stop and tell the student to run `/interview` first.

---

## Output

| File | Purpose |
|------|---------|
| `output/defense.tex` | Editable Beamer source — student can adjust before defense |
| `output/defense.pdf` | Compiled PDF (if `pdflatex` is available) |

---

## Beamer Configuration

- **Theme:** `Boadilla` — clean, professional, footer with author/title/date, no cluttered navigation bullets
- **PDF engine:** `pdflatex` (Beamer is optimized for it; more universally available than `xelatex` for slide compilation)
- The student can change the theme by editing `\usetheme{Boadilla}` on line 2 of the `.tex` file

---

## Slide Structure

Fixed 16-slide structure for a 20-minute defense:

| Slide # | Title | Source |
|---------|-------|--------|
| 1 | Title slide | `docs/student-profile.md` (student name, thesis title, advisor, university, date) |
| 2 | Outline | Auto-generated from section titles |
| 3 | Motivation | `thesis/01_introduction.md` |
| 4 | Research Question | `thesis/03_research_question.md` |
| 5–6 | Literature & Positioning | `thesis/02_literature_review.md` |
| 7–8 | Data | `thesis/04_data.md` |
| 9–10 | Methodology | `thesis/05_methodology.md` |
| 11–13 | Main Results | `thesis/06_results.md` |
| 14 | Robustness | `thesis/07_robustness.md` |
| 15 | Conclusion & Contribution | `thesis/08_discussion.md` + `thesis/09_conclusion.md` |
| 16 | Thank You / Questions | Static slide |

---

## Content Extraction Rules

When reading each thesis section:

1. Strip `>` comment lines, `[placeholder]` markers, and bare headings
2. Summarize remaining prose into **3–4 concise bullet points** per slide (one line each)
3. Do not copy sentences verbatim — rephrase into presentation language
4. Preserve cautious academic language where relevant: "suggests", "consistent with", "evidence points to"
5. For results slides: prioritize tables, coefficients, or key findings
6. For empty sections: insert a LaTeX comment — `% TODO: [Section name] not yet written — fill in before defense`

Multi-slide sections (Literature, Data, Methodology, Results) split their content across their allocated slides. If a section has very little content, collapse to one slide rather than leaving an empty second slide.

---

## Compilation Process

### Step 1 — Check pdflatex

Run:
```bash
pdflatex --version
```

If not found, print platform-specific install instructions:
- **macOS:** `brew install --cask mactex` or `brew install basictex`
- **Windows:** Install MiKTeX from miktex.org or `winget install MiKTeX.MiKTeX`
- **Linux:** `sudo apt install texlive-latex-base` or `sudo dnf install texlive`

Do not proceed until pdflatex is available.

### Step 2 — Write output/defense.tex

Write the complete Beamer `.tex` file to `output/defense.tex`.

### Step 3 — Compile twice

Run pdflatex twice (required for correct page numbering and outline):
```bash
pdflatex -interaction=nonstopmode -output-directory=output output/defense.tex
pdflatex -interaction=nonstopmode -output-directory=output output/defense.tex
```

### Step 4 — Report result

On success:
> "Slides compiled → `output/defense.pdf` (16 slides). Open `output/defense.tex` to edit before your defense."

On failure:
- Show the first error line from pdflatex stderr
- Diagnose common causes:
  - `Undefined control sequence` → malformed LaTeX generated from thesis content (special characters not escaped)
  - `File not found` → missing package; suggest `tlmgr install <package>` or switching to a more basic theme
  - `LaTeX Error: Environment ... undefined` → Beamer environment issue; suggest checking the `.tex` file
- Suggest the fix in plain English

---

## Beamer .tex Template Structure

```latex
\documentclass{beamer}
\usetheme{Boadilla}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}

\title{[Thesis Title]}
\author{[Student Name]}
\institute{[University] \\ [Program]}
\date{[Date]}

\begin{document}

\begin{frame}
  \titlepage
\end{frame}

\begin{frame}{Outline}
  \tableofcontents
\end{frame}

% --- Motivation ---
\section{Motivation}
\begin{frame}{Motivation}
  \begin{itemize}
    \item [bullet from introduction]
    \item [bullet from introduction]
    \item [bullet from introduction]
  \end{itemize}
\end{frame}

% ... (one \begin{frame}...\end{frame} per slide)

\begin{frame}
  \centering
  \Large Thank you. \\[1em]
  \normalsize Questions welcome.
\end{frame}

\end{document}
```

Special characters in thesis content (`&`, `%`, `$`, `#`, `_`, `^`, `{`, `}`, `~`, `\`) must be escaped before inserting into the `.tex` file.

---

## What Is NOT in Scope

- Automatically adding figures or tables from `output/figures/` or `output/tables/`
- Animating bullet points (`\pause`, `\only`, `\uncover`)
- Multiple theme options or interactive theme selection
- Generating speaker notes
- Sending or uploading the presentation

---

## No Agent Required

The skill is self-contained. Content extraction rules are explicit enough that an agent adds no meaningful quality gate. The student reviews `output/defense.tex` before presenting — that is the quality gate.
