# test_main.py

from typer_template import main
from typer_template import _logger


def test_main(capsys):
    main.hello("Test")
    captured = capsys.readouterr()
    assert "Hello Test" in captured.out


def test_logger_init():
    _logger.setup_logging("DEBUG")
