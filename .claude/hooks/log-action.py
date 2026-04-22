#!/usr/bin/env python3
"""
PostToolUse hook: appends a log entry to .claude/logs/activity.log
Receives JSON on stdin with hook event data.
"""
import json
import os
import sys
from datetime import datetime

def main():
    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, EOFError):
        data = {}

    tool_name = data.get("tool_name", "unknown")
    timestamp = datetime.now().isoformat(timespec="seconds")

    log_dir = os.path.join(".claude", "logs")
    os.makedirs(log_dir, exist_ok=True)
    log_path = os.path.join(log_dir, "activity.log")

    with open(log_path, "a", encoding="utf-8") as f:
        f.write(timestamp + ": " + tool_name + "\n")

main()
