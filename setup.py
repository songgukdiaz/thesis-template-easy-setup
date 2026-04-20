#!/usr/bin/env python3
"""
Cross-platform setup script for the Master Thesis Template.
Uses stdlib only — no pip install required to run this script.

Usage:
    python setup.py
"""
import os
import platform
import shutil
import subprocess
import sys


REQUIRED_TOOLS = ["pandoc", "git", "claude"]
MIN_PYTHON = (3, 8)
VENV_DIR = ".venv"


def detect_os() -> str:
    system = platform.system().lower()
    if system == "windows":
        return "windows"
    if system == "darwin":
        return "macos"
    return "linux"


def check_python_version() -> bool:
    return sys.version_info >= MIN_PYTHON


def check_tool(name: str) -> bool:
    return shutil.which(name) is not None


def install_instructions(tool: str) -> dict:
    instructions = {
        "python": {
            "windows": "Download from https://python.org/downloads/ (check 'Add to PATH')",
            "macos": "brew install python  OR  download from https://python.org/downloads/",
            "linux": "sudo apt install python3  OR  sudo dnf install python3",
        },
        "pandoc": {
            "windows": "winget install JohnMacFarlane.Pandoc  OR  https://pandoc.org/installing.html",
            "macos": "brew install pandoc",
            "linux": "sudo apt install pandoc  OR  sudo dnf install pandoc",
        },
        "git": {
            "windows": "winget install Git.Git  OR  https://git-scm.com/downloads",
            "macos": "brew install git  OR  xcode-select --install",
            "linux": "sudo apt install git  OR  sudo dnf install git",
        },
        "claude": {
            "windows": "npm install -g @anthropic-ai/claude-code  (requires Node.js from nodejs.org)",
            "macos": "npm install -g @anthropic-ai/claude-code  (requires Node.js: brew install node)",
            "linux": "npm install -g @anthropic-ai/claude-code  (requires Node.js from nodejs.org)",
        },
        "xelatex": {
            "windows": "Install MiKTeX from https://miktex.org/download  OR  TeX Live from https://tug.org/texlive/",
            "macos": "brew install --cask mactex-no-gui  OR  https://tug.org/mactex/",
            "linux": "sudo apt install texlive-xetex  OR  sudo dnf install texlive-xetex",
        },
    }
    return instructions.get(tool, {
        "windows": f"Install {tool} manually.",
        "macos": f"brew install {tool}",
        "linux": f"sudo apt install {tool}",
    })


def create_venv():
    if os.path.exists(VENV_DIR):
        print(f"  [OK] Virtual environment already exists at {VENV_DIR}/")
        return
    print(f"  Creating virtual environment at {VENV_DIR}/...")
    subprocess.run([sys.executable, "-m", "venv", VENV_DIR], check=True)
    print(f"  [OK] Virtual environment created.")


def install_requirements():
    os_name = detect_os()
    if os_name == "windows":
        pip = os.path.join(VENV_DIR, "Scripts", "pip")
    else:
        pip = os.path.join(VENV_DIR, "bin", "pip")

    if not os.path.exists(pip):
        print("  [SKIP] Could not find pip in venv — skipping requirements install.")
        return

    print("  Installing Python requirements...")
    subprocess.run([pip, "install", "-r", "requirements.txt", "-q"], check=True)
    print("  [OK] Requirements installed.")


def copy_claude_template():
    template = "CLAUDE.md.template"
    target = "CLAUDE.md"
    if not os.path.exists(template):
        print(f"  [SKIP] {template} not found — skipping.")
        return
    if os.path.exists(target):
        print(f"  [OK] {target} already exists — skipping copy.")
        return
    import shutil as _shutil
    _shutil.copy(template, target)
    print(f"  [OK] Copied {template} -> {target}")


def main():
    os_name = detect_os()
    print(f"\nMaster Thesis Template Setup")
    print(f"Detected OS: {os_name}")
    print("=" * 40)

    print("\n[1/4] Checking Python version...")
    if check_python_version():
        print(f"  [OK] Python {sys.version.split()[0]}")
    else:
        major, minor = MIN_PYTHON
        print(f"  [ERROR] Python {major}.{minor}+ required. Current: {sys.version.split()[0]}")
        print(f"  Install: {install_instructions('python')[os_name]}")
        sys.exit(1)

    print("\n[2/4] Checking required tools...")
    missing = []
    for tool in REQUIRED_TOOLS:
        if check_tool(tool):
            print(f"  [OK] {tool}")
        else:
            print(f"  [MISSING] {tool}")
            print(f"    Install: {install_instructions(tool)[os_name]}")
            missing.append(tool)

    if check_tool("xelatex"):
        print(f"  [OK] xelatex (PDF compilation available)")
    else:
        print(f"  [NOTE] xelatex not found — /compile will not work until installed.")
        print(f"    Install: {install_instructions('xelatex')[os_name]}")

    if missing:
        print(f"\n  Install the missing tools above, then re-run: python setup.py")
        sys.exit(1)

    print("\n[3/4] Setting up Python environment...")
    create_venv()
    install_requirements()

    print("\n[4/4] Preparing Claude configuration...")
    copy_claude_template()

    print("\n" + "=" * 40)
    print("Setup complete!")
    print("\nNext steps:")
    print("  1. Open Claude Code in this folder:  claude .")
    print("  2. Run the interview:                /interview")
    print("=" * 40 + "\n")


if __name__ == "__main__":
    main()
