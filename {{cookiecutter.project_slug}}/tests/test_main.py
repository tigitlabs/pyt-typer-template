"""Tests for `{{ cookiecutter.project_slug }}` package."""


from {{ cookiecutter.app_slug }} import main
from {{ cookiecutter.app_slug }} import _logger


def test_main(capsys):
    main.hello("Test")
    captured = capsys.readouterr()
    assert "Hello Test" in captured.out


def test_logger_init():
    _logger.setup_logging("DEBUG")
