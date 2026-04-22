import sys
import os
import importlib.util
from unittest.mock import patch

# Load setup module without executing main()
_setup_path = os.path.join(os.path.dirname(__file__), '..', 'setup.py')


def load_setup():
    spec = importlib.util.spec_from_file_location("setup", _setup_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_detect_os_returns_valid_platform():
    mod = load_setup()
    result = mod.detect_os()
    assert result in ("windows", "macos", "linux")


def test_check_tool_returns_true_when_found():
    mod = load_setup()
    with patch("shutil.which", return_value="/usr/bin/git"):
        assert mod.check_tool("git") is True


def test_check_tool_returns_false_when_missing():
    mod = load_setup()
    with patch("shutil.which", return_value=None):
        assert mod.check_tool("pandoc") is False


def test_check_python_version_passes_current():
    mod = load_setup()
    assert mod.check_python_version() is True


def test_install_instructions_keys():
    mod = load_setup()
    for tool in ("python", "pandoc", "git", "claude"):
        instructions = mod.install_instructions(tool)
        assert "windows" in instructions
        assert "macos" in instructions
        assert "linux" in instructions
