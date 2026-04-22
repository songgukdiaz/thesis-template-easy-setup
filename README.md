# Master Thesis Template

A Claude Code template for master's thesis students. Provides AI-assisted writing, reference validation, empirical design guidance, and PDF compilation.

## Quick Start

### 1. Prerequisites

You need:
- [Claude Code](https://claude.ai/code) — AI assistant (available as CLI, desktop app, or web app)
- [Python 3.8+](https://python.org) — for analysis scripts
- [Pandoc](https://pandoc.org/installing.html) — for PDF compilation
- [A LaTeX distribution](https://tug.org/texlive/) (TeX Live or MiKTeX) — for PDF compilation
- [Git](https://git-scm.com)

> **Don't want to install these manually?** If you have [Claude Desktop](https://claude.ai/download), the setup skills below will install everything for you automatically.

### Easy setup with Claude Desktop (Windows or macOS)

#### Dependencies

You need [Claude Desktop](https://claude.ai/download) installed on your computer. Everything else will be installed automatically.

#### Steps

1. Download this template from GitHub (green "Code" button → "Download ZIP")
2. Extract the ZIP file to a folder on your computer
3. Inside the extracted folder, find and double-click the starter script for your system:
   - **Mac:** `start-mac.command`
   - **Windows:** `start-windows.bat`
4. Open Claude Desktop and go to the **Code** section
5. Open this project folder
6. Type **`/mac-setup`** or **`/windows-setup`** — this installs all remaining prerequisites automatically
7. When setup finishes, type **`/interview`** to configure your thesis

That's it. No terminal knowledge required.

### Manual setup (all platforms)

### 2. Clone and set up

```bash
git clone <your-repo-url>
cd <repo-name>
python setup.py
```

`setup.py` will check your prerequisites, create a Python virtual environment, and tell you what to install if anything is missing.

### 3. Open in Claude Code

```bash
claude .
```

Or open the folder in Claude Desktop or the Claude web app.

### 4. Run the interview

Inside Claude Code, type:

```
/interview
```

This sets up your student profile, thesis proposal, and configures the AI assistant for your specific topic.

## Available Skills

| Skill | What it does |
|---|---|
| `/windows-setup` | **Windows only:** installs all prerequisites automatically via winget |
| `/mac-setup` | **macOS only:** installs all prerequisites automatically via Homebrew |
| `/interview` | One-time setup: creates your student profile and proposal |
| `/literature-review` | Maps literature streams and suggests search queries |
| `/citation-search` | Returns search queries for a claim or topic |
| `/validate-references` | Checks all citations against your .bib file and the web |
| `/empirical-design` | Designs variables, regressions, and robustness checks |
| `/write-section` | Drafts a thesis section from your notes |
| `/adversarial-reviewer` | Simulates a tough examiner raising hard questions |
| `/data-explorer` | Describes a dataset and flags data quality issues |
| `/progress-check` | Reports which sections are done vs. placeholder |
| `/compile` | Produces output/thesis.pdf from your Markdown files |
| `/reproducibility-check` | Checks your project can be reproduced |
| `/advisor-report` | Generates an email-ready progress report for your advisor |
| `/defense-slides` | Generates a populated Beamer presentation for your thesis defense |

## Writing your thesis

Write in `thesis/*.md` files using standard Markdown. Cite with `[@key]` where `key` is a BibTeX key in `docs/references.bib`.

Run `/compile` to produce a PDF.

## Project structure

```
thesis/          ← write here (Markdown sections)
code/            ← Python analysis scripts
data/raw/        ← your raw data (never modified by Claude)
data/clean/      ← processed data
output/          ← tables, figures, compiled PDF
docs/            ← generated docs (proposal, references, health report)
```

## Activating the Python environment

```bash
# macOS / Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

---

## Git workflow

Your thesis lives in a private GitHub repository. Set it up once:

1. Create a new private repo on GitHub (github.com → New repository)
2. Change the remote in this folder:
   ```bash
   git remote set-url origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
   git push -u origin main
   ```
3. Commit regularly as you write — at least after each work session
4. Push before every advisor meeting so your advisor can see your progress
5. Run `/advisor-report` to generate a progress email before each meeting

### What to commit

- Everything in `thesis/`, `code/`, `docs/`, `pandoc/`
- Never commit `data/` (already excluded by `.gitignore`)

---

## For the instructor

This template is distributed as-is. Students clone it and run `python setup.py` followed by `/interview`.

### Files to remove before distributing to students

The following files are from the development phase and should be removed before distributing the template to students:

- `thesis/proposal.md` — superseded by `docs/proposal.md` (created by `/interview`)
- `thesis/literature_review.md` — superseded by `thesis/02_literature_review.md`
- `thesis/methodology.md` — superseded by `thesis/05_methodology.md`
- `thesis/data_dictionary.md` — moved to `docs/data_dictionary.md`
- `.claude/hooks/log-action.sh` — replaced by `.claude/hooks/log-action.py`

Delete these manually before pushing to GitHub as a template:

```bash
git rm thesis/proposal.md thesis/literature_review.md thesis/methodology.md thesis/data_dictionary.md
git rm .claude/hooks/log-action.sh
git commit -m "chore: remove superseded files before template distribution"
```

### Distributing the template

1. Push to GitHub
2. On GitHub: Settings → Template repository ✓
3. Students use "Use this template" to create their own repo
4. Each student then runs `python setup.py` and `/interview`
```
