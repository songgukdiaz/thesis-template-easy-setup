---
name: windows-setup
description: One-command Windows setup — installs Python, Git, Pandoc, and MiKTeX via winget, then runs project setup. Designed for non-developers using Claude Desktop.
---

# Windows Setup Skill

Use this skill when a Windows student wants to set up the thesis template. This skill replaces the manual installation process with automated winget commands.

## Rules

- Only run this on Windows. If the OS is not Windows, tell the student: "This skill is for Windows. On macOS, run `brew install pandoc git` and install MacTeX. On Linux, use your package manager. Then run `python setup.py`."
- Ask before installing anything. Show the student what will be installed and get confirmation.
- If a tool is already installed, skip it — do not reinstall.
- If winget is not available, fall back to download links.

## Step 1: Detect platform and check winget

Run:
```powershell
[System.Environment]::OSVersion.Platform
winget --version
```

If the platform is not Windows (not "Win32NT"), stop and show the message from Rules above.

If winget is not found, tell the student:
"winget is not available on your system. It comes with Windows 10 (1709+) and Windows 11. You can install it from the Microsoft Store (search for 'App Installer'). Once installed, run /windows-setup again."

## Step 2: Check what is already installed

Run each of these and note which ones succeed vs. fail:
```powershell
python --version
git --version
pandoc --version
xelatex --version
```

Build a list of what is missing.

## Step 3: Show the installation plan

Tell the student exactly what will be installed. Example:

"I need to install the following on your computer:
- **Python 3.12** — needed for data analysis scripts
- **Pandoc** — converts your thesis from Markdown to PDF
- **MiKTeX** — the LaTeX engine that produces the PDF

Git is already installed, so I will skip that.

This uses `winget`, the built-in Windows package manager. Shall I go ahead?"

Wait for confirmation before proceeding. Do NOT install anything without the student saying yes.

## Step 4: Install missing prerequisites

For each missing tool, run the corresponding winget command. Run them one at a time so the student can see progress.

**Python:**
```powershell
winget install Python.Python.3.12 --accept-package-agreements --accept-source-agreements
```
After installing Python, the terminal may need to be restarted for `python` to be in PATH. Check:
```powershell
python --version
```
If it still fails, tell the student: "Python was installed but the terminal needs to be restarted to pick it up. Please close and reopen Claude Desktop, then run /windows-setup again — it will skip what is already installed."

**Git:**
```powershell
winget install Git.Git --accept-package-agreements --accept-source-agreements
```

**Pandoc:**
```powershell
winget install JohnMacFarlane.Pandoc --accept-package-agreements --accept-source-agreements
```

**MiKTeX (LaTeX):**
```powershell
winget install MiKTeX.MiKTeX --accept-package-agreements --accept-source-agreements
```
Note: MiKTeX is a large download (~200 MB). Warn the student it may take a few minutes.

After MiKTeX installs, it may need a PATH refresh. Check:
```powershell
xelatex --version
```
If xelatex is not found after install, tell the student: "MiKTeX installed, but you may need to restart Claude Desktop for it to be detected. The thesis writing tools will work immediately — PDF compilation (/compile) will work after the restart."

## Step 5: Run project setup

Once all prerequisites are confirmed, run:
```powershell
python setup.py
```

If setup.py reports any issues, help the student resolve them.

## Step 6: Activate the virtual environment

Run:
```powershell
.venv\Scripts\activate
```

If this fails, the venv may not have been created. Run:
```powershell
python -m venv .venv
.venv\Scripts\pip install -r requirements.txt
```

## Step 7: Verify everything works

Run a quick check:
```powershell
python --version
git --version
pandoc --version
xelatex --version
```

Report the results as a checklist:
- [x] Python 3.12.x
- [x] Git 2.x.x
- [x] Pandoc 3.x.x
- [x] XeLaTeX (MiKTeX)
- [x] Python virtual environment

## Step 8: Next steps

Tell the student:

"Your thesis workspace is ready! Here is what to do next:

1. **Run /interview** — this sets up your student profile and thesis topic (takes about 5 minutes)
2. After the interview, your thesis sections are in the `thesis/` folder
3. **Run /compile** any time to produce a PDF of your thesis

You do not need to touch the terminal again — everything works through this chat.

Some helpful commands:
- `/write-section` — drafts a thesis section from your notes
- `/progress-check` — shows how much of your thesis is done
- `/literature-review` — helps you find and organize papers
- `/compile` — creates your thesis PDF"

## Error handling

If any winget install fails with an access error:
- Tell the student to right-click Claude Desktop and select "Run as administrator", then try /windows-setup again.

If winget install fails with "no applicable installer":
- Provide the direct download URL:
  - Python: https://python.org/downloads/
  - Git: https://git-scm.com/downloads/win
  - Pandoc: https://pandoc.org/installing.html
  - MiKTeX: https://miktex.org/download

If the student is on Windows 10 older than version 1709:
- winget is not available. Provide all direct download URLs and walk them through manual installation step by step.
