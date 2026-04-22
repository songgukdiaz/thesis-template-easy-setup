#!/usr/bin/env python3
"""
PreToolUse hook: blocks Edit and Write tool calls targeting data/raw/.
Receives JSON on stdin. Exits non-zero to block; exits 0 to allow.
"""
import json
import os
import sys


WRITE_TOOLS = {"Edit", "Write", "NotebookEdit"}
RAW_DATA_PREFIX = os.path.join("data", "raw")


def is_raw_data_path(file_path: str) -> bool:
    # Normalise separators so forward/back slash both work
    normalised = file_path.replace("\\", "/")
    return normalised.startswith("data/raw/") or normalised == "data/raw"


def main():
    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, EOFError):
        sys.exit(0)

    tool_name = data.get("tool_name", "")
    tool_input = data.get("tool_input", {})

    if tool_name not in WRITE_TOOLS:
        sys.exit(0)

    file_path = tool_input.get("file_path", "")
    if is_raw_data_path(file_path):
        print(
            f"BLOCKED: Claude cannot modify files in data/raw/. "
            f"Raw data is read-only. Copy to data/clean/ before editing.",
            file=sys.stderr
        )
        sys.exit(1)

    sys.exit(0)


main()
