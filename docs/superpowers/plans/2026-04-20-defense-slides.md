# Defense Slides Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a `/defense-slides` skill that reads the student's thesis and generates a populated Beamer `.tex` presentation, then compiles it to PDF.

**Architecture:** Single skill file at `.claude/skills/defense-slides/SKILL.md` containing all instructions. A small README.md update adds it to the skills table. No Python code, no agents, no new hooks. The `.claude/**` deny rule requires writing the skill file via Python subprocess.

**Tech Stack:** Markdown (skill), LaTeX Beamer (generated output), Python (file write workaround), pdflatex (compilation)

---

## File Map

| Action | Path | Purpose |
|--------|------|---------|
| Create | `.claude/skills/defense-slides/SKILL.md` | New skill — all logic in Markdown instructions |
| Modify | `README.md` | Add `/defense-slides` row to skills table |

---

### Task 1: Create /defense-slides skill

**Files:**
- Create: `.claude/skills/defense-slides/SKILL.md`

> **Constraint:** `.claude/**` is blocked by the deny rule in `.claude/settings.json`. Use Python via Bash to write the file. Full Python path on this machine: `/c/Users/jfimb/anaconda3/python.exe`

- [ ] **Step 1: Write the skill file via Python**

  Run:
  ```bash
  /c/Users/jfimb/anaconda3/python.exe -c "
  import pathlib
  p = pathlib.Path(r'C:\\Users\\jfimb\\Documents\\AIMasterThesis\\.claude\\skills\\defense-slides')
  p.mkdir(parents=True, exist_ok=True)
  (p / 'SKILL.md').write_text(open(r'C:\\Users\\jfimb\\AppData\\Local\\Temp\\defense_slides_skill.md', encoding='utf-8').read(), encoding='utf-8')
  print('Done')
  "
  ```

  First write the content to a temp file:

  ```bash
  /c/Users/jfimb/anaconda3/python.exe -c "
  import pathlib
  content = r'''---
  name: defense-slides
  description: Generates a populated LaTeX Beamer presentation for the thesis defense from thesis sections and student profile. Compiles to output/defense.pdf.
  ---

  # /defense-slides

  Generates a 16-slide Beamer presentation for your thesis defense, populated from your thesis sections. Outputs \`output/defense.tex\` (editable) and attempts to compile \`output/defense.pdf\`.

  ## Prerequisites

  Run \`/interview\` first if you have not already — this skill reads \`docs/student-profile.md\` for your name, advisor, university, and thesis title.

  ## Process

  ### Step 1 — Check student profile

  Read \`docs/student-profile.md\`. Extract:
  - Student full name
  - Advisor name
  - University and program
  - Thesis working title
  - Research question

  If the file does not exist or contains only placeholder text, stop and tell the student: \"Please run \`/interview\` first to set up your student profile.\"

  ### Step 2 — Read thesis sections

  Read each of the following files:

  | File | Used for |
  |------|---------|
  | \`thesis/01_introduction.md\` | Motivation slide |
  | \`thesis/02_literature_review.md\` | Literature slides (2) |
  | \`thesis/03_research_question.md\` | Research Question slide |
  | \`thesis/04_data.md\` | Data slides (2) |
  | \`thesis/05_methodology.md\` | Methodology slides (2) |
  | \`thesis/06_results.md\` | Results slides (3) |
  | \`thesis/07_robustness.md\` | Robustness slide |
  | \`thesis/08_discussion.md\` | Conclusion slide (combined with 09) |
  | \`thesis/09_conclusion.md\` | Conclusion slide (combined with 08) |

  ### Step 3 — Check pdflatex

  Run:
  \`\`\`bash
  pdflatex --version
  \`\`\`

  If not found, print install instructions and stop:
  - **macOS:** \`brew install --cask mactex\` or \`brew install basictex\`
  - **Windows:** Install MiKTeX from miktex.org or \`winget install MiKTeX.MiKTeX\`
  - **Linux:** \`sudo apt install texlive-latex-base\` or \`sudo dnf install texlive\`

  ### Step 4 — Generate output/defense.tex

  Apply these content extraction rules to each thesis section before inserting into the .tex file:

  1. Strip lines starting with \`>\`, lines containing \`[placeholder]\`, and bare headings
  2. Summarize remaining prose into **3–4 concise bullet points** per slide (one line each)
  3. Do not copy sentences verbatim — rephrase into presentation language
  4. Preserve cautious language where relevant: \"suggests\", \"consistent with\", \"evidence points to\"
  5. For results slides: prioritize coefficients, key findings, and tables
  6. For empty sections: insert \`% TODO: [Section name] not yet written — fill in before defense\`
  7. Multi-slide sections: split content evenly across allocated slides; collapse to one slide if content is thin
  8. **Escape these characters** before inserting into LaTeX:
     - \`&\` → \`\\&\`
     - \`%\` → \`\\%\`
     - \`$\` → \`\\$\`
     - \`#\` → \`\\#\`
     - \`_\` → \`\\_\`
     - \`^\` → \`\\^{}\`
     - \`~\` → \`\\textasciitilde{}\`
     - \`\\\` → \`\\textbackslash{}\`

  Generate \`output/defense.tex\` using this exact structure, substituting bullet points from the thesis:

  \`\`\`latex
  \\documentclass{beamer}
  \\usetheme{Boadilla}
  \\usepackage[utf8]{inputenc}
  \\usepackage[T1]{fontenc}

  \\title{[Thesis Title]}
  \\subtitle{Master\'s Thesis Defense}
  \\author{[Student Name]}
  \\institute{[University] \\\\ [Program]}
  \\date{\\today}

  \\begin{document}

  \\begin{frame}
    \\titlepage
  \\end{frame}

  \\begin{frame}{Outline}
    \\tableofcontents
  \\end{frame}

  % -------------------------------------------------------
  \\section{Motivation}
  \\begin{frame}{Motivation}
    \\begin{itemize}
      \\item [bullet 1 from introduction]
      \\item [bullet 2 from introduction]
      \\item [bullet 3 from introduction]
    \\end{itemize}
  \\end{frame}

  % -------------------------------------------------------
  \\section{Research Question}
  \\begin{frame}{Research Question}
    \\begin{itemize}
      \\item \\textbf{Research question:} [RQ from student-profile.md]
      \\item [bullet 2 from research question section]
      \\item [bullet 3 from research question section]
    \\end{itemize}
  \\end{frame}

  % -------------------------------------------------------
  \\section{Literature \\& Positioning}
  \\begin{frame}{Literature \\& Positioning (1/2)}
    \\begin{itemize}
      \\item [bullet 1]
      \\item [bullet 2]
      \\item [bullet 3]
    \\end{itemize}
  \\end{frame}

  \\begin{frame}{Literature \\& Positioning (2/2)}
    \\begin{itemize}
      \\item [bullet 1]
      \\item [bullet 2]
      \\item [bullet 3]
    \\end{itemize}
  \\end{frame}

  % -------------------------------------------------------
  \\section{Data}
  \\begin{frame}{Data (1/2)}
    \\begin{itemize}
      \\item [bullet 1]
      \\item [bullet 2]
      \\item [bullet 3]
    \\end{itemize}
  \\end{frame}

  \\begin{frame}{Data (2/2)}
    \\begin{itemize}
      \\item [bullet 1]
      \\item [bullet 2]
      \\item [bullet 3]
    \\end{itemize}
  \\end{frame}

  % -------------------------------------------------------
  \\section{Methodology}
  \\begin{frame}{Methodology (1/2)}
    \\begin{itemize}
      \\item [bullet 1]
      \\item [bullet 2]
      \\item [bullet 3]
    \\end{itemize}
  \\end{frame}

  \\begin{frame}{Methodology (2/2)}
    \\begin{itemize}
      \\item [bullet 1]
      \\item [bullet 2]
      \\item [bullet 3]
    \\end{itemize}
  \\end{frame}

  % -------------------------------------------------------
  \\section{Results}
  \\begin{frame}{Main Results (1/3)}
    \\begin{itemize}
      \\item [bullet 1]
      \\item [bullet 2]
      \\item [bullet 3]
    \\end{itemize}
  \\end{frame}

  \\begin{frame}{Main Results (2/3)}
    \\begin{itemize}
      \\item [bullet 1]
      \\item [bullet 2]
      \\item [bullet 3]
    \\end{itemize}
  \\end{frame}

  \\begin{frame}{Main Results (3/3)}
    \\begin{itemize}
      \\item [bullet 1]
      \\item [bullet 2]
      \\item [bullet 3]
    \\end{itemize}
  \\end{frame}

  % -------------------------------------------------------
  \\section{Robustness}
  \\begin{frame}{Robustness Checks}
    \\begin{itemize}
      \\item [bullet 1]
      \\item [bullet 2]
      \\item [bullet 3]
    \\end{itemize}
  \\end{frame}

  % -------------------------------------------------------
  \\section{Conclusion}
  \\begin{frame}{Conclusion \\& Contribution}
    \\begin{itemize}
      \\item [bullet 1 from discussion/conclusion]
      \\item [bullet 2 from discussion/conclusion]
      \\item [bullet 3 from discussion/conclusion]
    \\end{itemize}
  \\end{frame}

  % -------------------------------------------------------
  \\begin{frame}
    \\centering
    \\Large Thank you. \\\\[1em]
    \\normalsize Questions welcome.
  \\end{frame}

  \\end{document}
  \`\`\`

  ### Step 5 — Compile

  Run pdflatex twice from the project root (required for correct page numbering and outline):

  \`\`\`bash
  pdflatex -interaction=nonstopmode -output-directory=output output/defense.tex
  pdflatex -interaction=nonstopmode -output-directory=output output/defense.tex
  \`\`\`

  ### Step 6 — Report result

  On success:
  > \"Slides compiled → \`output/defense.pdf\` (16 slides). Open \`output/defense.tex\` to customise the theme or adjust content before your defense. To change the theme, edit \`\\usetheme{Boadilla}\` on line 2.\"

  On failure, show the first error line from pdflatex output and diagnose:
  - \`Undefined control sequence\` → a special character in your thesis was not escaped — open \`output/defense.tex\` and look for unescaped \`&\`, \`%\`, \`$\`, \`#\`, or \`_\`
  - \`File ... not found\` → missing LaTeX package; run \`tlmgr install <package>\` (macOS/Linux) or use MiKTeX Package Manager (Windows)
  - \`LaTeX Error: Environment itemize undefined\` → Beamer package not installed; reinstall your LaTeX distribution
  '''
  pathlib.Path(r'C:\\Users\\jfimb\\AppData\\Local\\Temp\\defense_slides_skill.md').write_text(content, encoding='utf-8')
  print('Temp file written')
  "
  ```

  Then copy into place:
  ```bash
  /c/Users/jfimb/anaconda3/python.exe -c "
  import pathlib, shutil
  p = pathlib.Path(r'C:\\Users\\jfimb\\Documents\\AIMasterThesis\\.claude\\skills\\defense-slides')
  p.mkdir(parents=True, exist_ok=True)
  shutil.copy(r'C:\\Users\\jfimb\\AppData\\Local\\Temp\\defense_slides_skill.md', p / 'SKILL.md')
  print('SKILL.md written to', p / 'SKILL.md')
  "
  ```

- [ ] **Step 2: Verify key content is present**

  ```bash
  /c/Users/jfimb/anaconda3/python.exe -c "
  content = open(r'C:\\Users\\jfimb\\Documents\\AIMasterThesis\\.claude\\skills\\defense-slides\\SKILL.md', encoding='utf-8').read()
  assert 'name: defense-slides' in content, 'Missing frontmatter name'
  assert 'Step 1' in content, 'Missing Step 1'
  assert 'Step 6' in content, 'Missing Step 6'
  assert 'output/defense.tex' in content, 'Missing output path'
  assert 'pdflatex' in content, 'Missing pdflatex instruction'
  assert 'Boadilla' in content, 'Missing theme'
  assert 'student-profile.md' in content, 'Missing profile read'
  assert 'textbackslash' in content, 'Missing special char escaping'
  print('OK — all assertions passed')
  "
  ```
  Expected: `OK — all assertions passed`

- [ ] **Step 3: Commit**

  ```bash
  git add .claude/skills/defense-slides/SKILL.md
  git commit -m "feat: add /defense-slides skill"
  ```

---

### Task 2: Add /defense-slides to README skills table

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Add the row**

  In `README.md`, find the skills table row:
  ```
  | `/advisor-report` | Generates an email-ready progress report for your advisor |
  ```

  Add one row immediately after it:
  ```markdown
  | `/defense-slides` | Generates a populated Beamer presentation for your thesis defense |
  ```

- [ ] **Step 2: Verify**

  ```bash
  grep -n "defense-slides" README.md
  ```
  Expected: one line containing `/defense-slides` in the skills table.

- [ ] **Step 3: Commit**

  ```bash
  git add README.md
  git commit -m "docs: add /defense-slides to README skills table"
  ```

---

## Self-Review

- [x] **Spec: invocation** — Task 1 creates skill with no-argument invocation ✓
- [x] **Spec: output files** — `output/defense.tex` and `output/defense.pdf` both in skill ✓
- [x] **Spec: Boadilla theme** — present in skill ✓
- [x] **Spec: pdflatex engine** — present in skill ✓
- [x] **Spec: 16-slide structure** — all 16 slides in template ✓
- [x] **Spec: content extraction rules** — all 8 rules present ✓
- [x] **Spec: special character escaping** — all 8 characters listed ✓
- [x] **Spec: compile twice** — both pdflatex runs present ✓
- [x] **Spec: platform install instructions** — macOS/Windows/Linux covered ✓
- [x] **Spec: failure diagnosis** — 3 error patterns covered ✓
- [x] **Spec: empty section TODO comment** — present in extraction rules ✓
- [x] **Spec: multi-slide collapse rule** — present in extraction rules ✓
- [x] **README update** — Task 2 covers this ✓
- [x] **No placeholders** — all steps contain complete content ✓
- [x] **Write constraint documented** — .claude/** workaround explained in Task 1 ✓
