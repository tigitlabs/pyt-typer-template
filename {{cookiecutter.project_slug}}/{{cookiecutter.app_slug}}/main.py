# main.py

import time

import typer
from loguru import logger
from rich.progress import track
from {{cookiecutter.app_slug}} import _logger

app = typer.Typer()


# Configure Loguru
@app.callback()
def init_logging(verbose: bool = False):
    """
    Typer CLI Template Project
    """
    log_level = "ERROR"
    if verbose:
        log_level = "DEBUG"
    _logger.setup_logging(log_level)


@app.command()
def init():
    """Initialize the application"""
    print("Initializing...")
    total = 0
    for value in track(range(100), description="Processing..."):
        # Fake processing time
        time.sleep(0.01)
        total += 1
    print(f"Processed {total} things.")


@app.command()
def hello(name: str):
    print(f"Hello {name}")
    logger.debug("That's it, beautiful and simple logging, debug!")
    logger.info("That's it, beautiful and simple logging, info!")
    logger.warning("That's it, beautiful and simple logging, warning!")
    logger.error("That's it, beautiful and simple logging, error!")


if __name__ == "__main__":
    app()
