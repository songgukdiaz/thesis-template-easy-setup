---
name: mac-setup
description: One-command macOS setup — installs Homebrew, Python, Git, Pandoc, and MacTeX via brew, then runs project setup. Designed for non-developers using Claude Desktop.
---

# Mac Setup Skill

Use this skill when a macOS student wants to set up the thesis template. This skill replaces the manual installation process with automated Homebrew commands.

## Rules

- Only run this on macOS. If the OS is not macOS, tell the student: "This skill is for macOS. On Windows, run `/windows-setup` instead. On Linux, use your package manager, then run `python setup.py`."
- Ask before installing anything. Show the student what will be installed and get confirmation.
- If a tool is already installed, skip it — do not reinstall.
- If Homebrew is not available, offer to install it first.

## Step 1: Detect platform

Run:
```bash
uname -s
```

If the output is not "Darwin", stop and show the message from Rules above.

## Step 2: Check for Homebrew

Run:
```bash
brew --version
```

If brew is not found, tell the student:

"Homebrew is the standard macOS package manager. I need it to install the other tools. It is safe, widely used, and recommended by Apple developers.

I will run this command to install it:
```
/bin/bash -c \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\"
```

This may ask for your Mac password — that is normal. Shall I go ahead?"

Wait for confirmation. If they say yes, run the install command. After install, check if brew needs to be added to PATH (common on Apple Silicon Macs):
```bash
which brew
```
If not found, run:
```bash
eval "$(/opt/homebrew/bin/brew shellenv)"
```

## Step 3: Check what is already installed

Run each of these and note which ones succeed vs. fail:
```bash
python3 --version
git --version
pandoc --version
xelatex --version
```

Build a list of what is missing. Note: macOS comes with Git via Xcode Command Line Tools, so it is likely already present.

## Step 4: Show the installation plan

Tell the student exactly what will be installed. Example:

"I need to install the following on your Mac:
- **Python 3** — needed for data analysis scripts
- **Pandoc** — converts your thesis from Markdown to PDF
- **MacTeX** — the LaTeX engine that produces the PDF (this is a large download, about 4 GB)

Git is already installed, so I will skip that.

This uses Homebrew, the standard macOS package manager. Shall I go ahead?"

Wait for confirmation before proceeding. Do NOT install anything without the student saying yes.

## Step 5: Install missing prerequisites

For each missing tool, run the corresponding brew command. Run them one at a time so the student can see progress.

**Python:**
```bash
brew install python
```
Verify:
```bash
python3 --version
```

**Git** (usually already present, but if missing):
```bash
brew install git
```

**Pandoc:**
```bash
brew install pandoc
```

**MacTeX (LaTeX):**
```bash
brew install --cask mactex-no-gui
```
Warn the student: "MacTeX is about 4 GB — this download will take a few minutes depending on your internet speed."

After MacTeX installs, the terminal may need a PATH refresh. Check:
```bash
eval "$(/usr/libexec/path_helper)"
xelatex --version
```
If xelatex is still not found, tell the student: "MacTeX installed, but you may need to restart Claude Desktop for it to be detected. The thesis writing tools will work immediately — PDF compilation (/compile) will work after the restart."

## Step 6: Run project setup

Once all prerequisites are confirmed, run:
```bash
python3 setup.py
```

If setup.py reports any issues, help the student resolve them.

## Step 7: Activate the virtual environment

Run:
```bash
source .venv/bin/activate
```

If this fails, the venv may not have been created. Run:
```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

## Step 8: Verify everything works

Run a quick check:
```bash
python3 --version
git --version
pandoc --version
xelatex --version
```

Report the results as a checklist:
- [x] Python 3.x.x
- [x] Git 2.x.x
- [x] Pandoc 3.x.x
- [x] XeLaTeX (MacTeX)
- [x] Python virtual environment

## Step 9: Next steps

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

If any brew install fails with a permissions error:
- Try: `sudo chown -R $(whoami) /usr/local/` (Intel Mac) or check permissions on `/opt/homebrew/` (Apple Silicon).

If Xcode Command Line Tools are needed:
- Run: `xcode-select --install` and wait for the popup to complete the installation.

If brew install hangs or fails on MacTeX:
- Provide the direct download: https://tug.org/mactex/
- Student can download and install the .pkg file manually, then run /mac-setup again — it will skip what is already installed.

If the student has an older macOS version (pre-Catalina):
- Homebrew may not be fully supported. Provide direct download links:
  - Python: https://python.org/downloads/
  - Pandoc: https://pandoc.org/installing.html
  - MacTeX: https://tug.org/mactex/
