# test_main.py

from typer_template import main


def test_main(capsys):
    main.main("Test")
    captured = capsys.readouterr()
    assert "Hello Test" in captured.out
