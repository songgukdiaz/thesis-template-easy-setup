import json
import os
import sys
import tempfile
import pytest
from io import StringIO
from unittest.mock import patch

# Add hooks directory to path for importing
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '.claude', 'hooks'))


def make_hook_input(tool_name="Edit", tool_input=None):
    return json.dumps({
        "session_id": "test-session",
        "hook_event_name": "PostToolUse",
        "tool_name": tool_name,
        "tool_input": tool_input or {},
        "tool_result": {}
    })


def test_log_action_writes_to_log_file(tmp_path, monkeypatch):
    """log-action.py should append a line to .claude/logs/activity.log"""
    log_dir = tmp_path / ".claude" / "logs"
    log_dir.mkdir(parents=True)
    log_file = log_dir / "activity.log"

    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr("sys.stdin", StringIO(make_hook_input("Read")))

    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "log_action",
        os.path.join(os.path.dirname(__file__), '..', '.claude', 'hooks', 'log-action.py')
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    assert log_file.exists()
    content = log_file.read_text()
    assert "Read" in content


import importlib.util


def load_protect_hook():
    spec = importlib.util.spec_from_file_location(
        "protect_raw_data",
        os.path.join(os.path.dirname(__file__), '..', '.claude', 'hooks', 'protect-raw-data.py')
    )
    mod = importlib.util.module_from_spec(spec)
    return spec, mod


def test_blocks_edit_to_raw_data(monkeypatch):
    """Hook should exit non-zero when Edit targets data/raw/"""
    hook_input = json.dumps({
        "session_id": "test-session",
        "hook_event_name": "PreToolUse",
        "tool_name": "Edit",
        "tool_input": {"file_path": "data/raw/prices.csv"},
    })
    monkeypatch.setattr("sys.stdin", StringIO(hook_input))

    spec, mod = load_protect_hook()
    with pytest.raises(SystemExit) as exc_info:
        spec.loader.exec_module(mod)

    assert exc_info.value.code != 0


def test_allows_edit_to_clean_data(monkeypatch):
    """Hook should exit 0 when Edit targets data/clean/"""
    hook_input = json.dumps({
        "session_id": "test-session",
        "hook_event_name": "PreToolUse",
        "tool_name": "Edit",
        "tool_input": {"file_path": "data/clean/prices.csv"},
    })
    monkeypatch.setattr("sys.stdin", StringIO(hook_input))

    spec, mod = load_protect_hook()
    try:
        spec.loader.exec_module(mod)
    except SystemExit as e:
        assert e.code == 0 or e.code is None


def test_allows_read_of_raw_data(monkeypatch):
    """Hook should not block Read tool on data/raw/"""
    hook_input = json.dumps({
        "session_id": "test-session",
        "hook_event_name": "PreToolUse",
        "tool_name": "Read",
        "tool_input": {"file_path": "data/raw/prices.csv"},
    })
    monkeypatch.setattr("sys.stdin", StringIO(hook_input))

    spec, mod = load_protect_hook()
    try:
        spec.loader.exec_module(mod)
    except SystemExit as e:
        assert e.code == 0 or e.code is None
