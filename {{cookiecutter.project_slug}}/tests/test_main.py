"""Tests for `{{ cookiecutter.project_slug }}` package."""


from {{cookiecutter.app_slug}} import logger_util, main


def test_main(capsys):
    main.hello("Test")
    captured = capsys.readouterr()
    assert "Hello Test" in captured.out


def test_logger_init():
    logger_util.setup_logging("DEBUG")
