"""Tests for `{{ cookiecutter.project_slug }}` package."""

from pathlib import Path

import pytest
from typer.testing import CliRunner
from {{cookiecutter.app_slug}} import logger_util, main

runner = CliRunner()


@pytest.fixture
def tmp_dir(tmp_path: Path):
    d = tmp_path
    print(f"tmp_dir: {d}")
    assert d.is_dir()
    return d


def test_main(capsys: pytest.CaptureFixture[str]):
    main.hello("Test")
    captured = capsys.readouterr()
    assert "Hello Test" in captured.out


def test_logger_init(tmp_dir):
    print(f"tmp_dir: {tmp_dir}")
    assert tmp_dir.is_dir()
    logger_util.setup_logging("DEBUG", log_dest=tmp_dir)
    assert (tmp_dir / "debug.log").exists()


# CLI Tests


def test_cli_help():
    result = runner.invoke(main.app, ["--help"])
    assert result.exit_code == 0
    assert "Typer CLI Template Project" in result.stdout


def test_cli_init():
    result = runner.invoke(main.app, ["init"])
    assert result.exit_code == 0
    assert "Processed 100 things." in result.stdout


def test_cli_hello():
    result = runner.invoke(main.app, ["hello", "Test"])
    assert result.exit_code == 0
    assert "Hello Test" in result.stdout
