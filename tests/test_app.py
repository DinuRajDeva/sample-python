"""Tests for sample_python_app.app."""

import pytest

from sample_python_app.app import greet, run


def test_greet_default() -> None:
    assert greet() == "Hello, world!"


def test_greet_custom() -> None:
    assert greet("Alice") == "Hello, Alice!"


def test_run_returns_zero(capsys: pytest.CaptureFixture[str]) -> None:
    assert run() == 0
    captured = capsys.readouterr()
    assert "Hello, world!" in captured.out
