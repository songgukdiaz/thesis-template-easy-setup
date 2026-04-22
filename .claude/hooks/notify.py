#!/usr/bin/env python3
import json, sys

NOTIFY_KEYWORDS = ["pandoc", "validate-references", "validate_references"]

def should_notify(data):
    if data.get("tool_name") != "Bash":
        return False
    command = data.get("tool_input", {}).get("command", "")
    return any(kw in command for kw in NOTIFY_KEYWORDS)

def main():
    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, EOFError):
        sys.exit(0)
    if not should_notify(data):
        sys.exit(0)
    try:
        from plyer import notification
        command = data.get("tool_input", {}).get("command", "command")
        notification.notify(title="Thesis Copilot", message=f"Done: {command[:60]}", timeout=5)
    except Exception:
        pass
    sys.exit(0)

main()
