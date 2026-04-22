---
name: defense-slides
description: Generates a populated LaTeX Beamer presentation for the thesis defense from thesis sections and student profile. Compiles to output/defense.pdf.
---

# /defense-slides

Generates a 16-slide Beamer presentation for your thesis defense, populated from your thesis sections. Outputs `output/defense.tex` (editable) and attempts to compile `output/defense.pdf`.

## Prerequisites

Run `/interview` first if you have not already — this skill reads `docs/student-profile.md` for your name, advisor, university, and thesis title.

## Process

### Step 1 — Check student profile

Read `docs/student-profile.md`. Extract:
- Student full name
- Advisor name
- University and program
- Thesis working title
- Research question

If the file does not exist or contains only placeholder text, stop and tell the student: "Please run `/interview` first to set up your student profile."

### Step 2 — Read thesis sections

Read each of the following files:

| File | Used for |
|------|---------|
| `thesis/01_introduction.md` | Motivation slide |
| `thesis/02_literature_review.md` | Literature slides (2) |
| `thesis/03_research_question.md` | Research Question slide |
| `thesis/04_data.md` | Data slides (2) |
| `thesis/05_methodology.md` | Methodology slides (2) |
| `thesis/06_results.md` | Results slides (3) |
| `thesis/07_robustness.md` | Robustness slide |
| `thesis/08_discussion.md` | Conclusion slide (combined with 09) |
| `thesis/09_conclusion.md` | Conclusion slide (combined with 08) |

### Step 3 — Check pdflatex

Run:
```bash
pdflatex --version
```

If not found, print install instructions and stop:
- **macOS:** `brew install --cask mactex` or `brew install basictex`
- **Windows:** Install MiKTeX from miktex.org or `winget install MiKTeX.MiKTeX`
- **Linux:** `sudo apt install texlive-latex-base` or `sudo dnf install texlive`

### Step 4 — Generate output/defense.tex

Apply these content extraction rules to each thesis section before inserting into the .tex file:

1. Strip lines starting with `>`, lines containing `[placeholder]`, and bare headings
2. Summarize remaining prose into **3–4 concise bullet points** per slide (one line each)
3. Do not copy sentences verbatim — rephrase into presentation language
4. Preserve cautious language where relevant: "suggests", "consistent with", "evidence points to"
5. For results slides: prioritize coefficients, key findings, and tables
6. For empty sections: insert `% TODO: [Section name] not yet written — fill in before defense`
7. Multi-slide sections: split content evenly across allocated slides; collapse to one slide if content is thin
8. **Escape these characters** before inserting into LaTeX:
   - `&` → `\&`
   - `%` → `\%`
   - `$` → `\$`
   - `#` → `\#`
   - `_` → `\_`
   - `^` → `\^{}`
   - `~` → `\textasciitilde{}`
   - `{` → `\{`
   - `}` → `\}`
   - `\` → `\textbackslash{}`

Generate `output/defense.tex` using this exact structure, substituting bullet points from the thesis:

```latex
\documentclass{beamer}
\usetheme{Boadilla}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}

\title{[Thesis Title]}
\subtitle{Master's Thesis Defense}
\author{[Student Name]}
\institute{[University] \\ [Program]}
\date{\today}

\begin{document}

\begin{frame}
  \titlepage
\end{frame}

\begin{frame}{Outline}
  \tableofcontents
\end{frame}

% -------------------------------------------------------
\section{Motivation}
\begin{frame}{Motivation}
  \begin{itemize}
    \item [bullet 1 from introduction]
    \item [bullet 2 from introduction]
    \item [bullet 3 from introduction]
  \end{itemize}
\end{frame}

% -------------------------------------------------------
\section{Research Question}
\begin{frame}{Research Question}
  \begin{itemize}
    \item \textbf{Research question:} [RQ from student-profile.md]
    \item [bullet 2 from research question section]
    \item [bullet 3 from research question section]
  \end{itemize}
\end{frame}

% -------------------------------------------------------
\section{Literature \& Positioning}
\begin{frame}{Literature \& Positioning (1/2)}
  \begin{itemize}
    \item [bullet 1]
    \item [bullet 2]
    \item [bullet 3]
  \end{itemize}
\end{frame}

\begin{frame}{Literature \& Positioning (2/2)}
  \begin{itemize}
    \item [bullet 1]
    \item [bullet 2]
    \item [bullet 3]
  \end{itemize}
\end{frame}

% -------------------------------------------------------
\section{Data}
\begin{frame}{Data (1/2)}
  \begin{itemize}
    \item [bullet 1]
    \item [bullet 2]
    \item [bullet 3]
  \end{itemize}
\end{frame}

\begin{frame}{Data (2/2)}
  \begin{itemize}
    \item [bullet 1]
    \item [bullet 2]
    \item [bullet 3]
  \end{itemize}
\end{frame}

% -------------------------------------------------------
\section{Methodology}
\begin{frame}{Methodology (1/2)}
  \begin{itemize}
    \item [bullet 1]
    \item [bullet 2]
    \item [bullet 3]
  \end{itemize}
\end{frame}

\begin{frame}{Methodology (2/2)}
  \begin{itemize}
    \item [bullet 1]
    \item [bullet 2]
    \item [bullet 3]
  \end{itemize}
\end{frame}

% -------------------------------------------------------
\section{Results}
\begin{frame}{Main Results (1/3)}
  \begin{itemize}
    \item [bullet 1]
    \item [bullet 2]
    \item [bullet 3]
  \end{itemize}
\end{frame}

\begin{frame}{Main Results (2/3)}
  \begin{itemize}
    \item [bullet 1]
    \item [bullet 2]
    \item [bullet 3]
  \end{itemize}
\end{frame}

\begin{frame}{Main Results (3/3)}
  \begin{itemize}
    \item [bullet 1]
    \item [bullet 2]
    \item [bullet 3]
  \end{itemize}
\end{frame}

% -------------------------------------------------------
\section{Robustness}
\begin{frame}{Robustness Checks}
  \begin{itemize}
    \item [bullet 1]
    \item [bullet 2]
    \item [bullet 3]
  \end{itemize}
\end{frame}

% -------------------------------------------------------
\section{Conclusion}
\begin{frame}{Conclusion \& Contribution}
  \begin{itemize}
    \item [bullet 1 from discussion/conclusion]
    \item [bullet 2 from discussion/conclusion]
    \item [bullet 3 from discussion/conclusion]
  \end{itemize}
\end{frame}

% -------------------------------------------------------
\begin{frame}
  \centering
  \Large Thank you. \\[1em]
  \normalsize Questions welcome.
\end{frame}

\end{document}
```

### Step 5 — Compile

Run pdflatex twice from the project root (required for correct page numbering and outline):

```bash
pdflatex -interaction=nonstopmode -output-directory=output output/defense.tex
pdflatex -interaction=nonstopmode -output-directory=output output/defense.tex
```

### Step 6 — Report result

On success:
> "Slides compiled → `output/defense.pdf` (16 slides). Open `output/defense.tex` to customise the theme or adjust content before your defense. To change the theme, edit `\usetheme{Boadilla}` on line 2."

On failure, show the first error line from pdflatex output and diagnose:
- `Undefined control sequence` → a special character in your thesis was not escaped — open `output/defense.tex` and look for unescaped `&`, `%`, `$`, `#`, or `_`
- `File ... not found` → missing LaTeX package; run `tlmgr install <package>` (macOS/Linux) or use MiKTeX Package Manager (Windows)
- `LaTeX Error: Environment itemize undefined` → Beamer package not installed; reinstall your LaTeX distribution
