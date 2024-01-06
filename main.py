# main.py

import sys
import typer
from loguru import logger

LOG_LEVEL = "WARNING"
LOG_FORMAT = "<green>{time:YYYY-MM-DD HH:mm:ss.SSS zz}</green> | <level>{level: <8}</level> | <yellow>Line {line: >4} ({file}):</yellow> <b>{message}</b>"

# Configure Loguru
def setup_logging():
    # Remove default logger to stdout
    logger.remove()
    # Add logger for stdout for certain levels (e.g., DEBUG and INFO)
    logger.add("debug.log", colorize=False, format=LOG_FORMAT , level="DEBUG")
    logger.add(sys.stdout, colorize=True, format=LOG_FORMAT, level=LOG_LEVEL)

def main(name: str):
  print(f"Hello {name}")
  logger.debug("That's it, beautiful and simple logging, debug!")
  logger.info("That's it, beautiful and simple logging, info!")
  logger.warning("That's it, beautiful and simple logging, warning!")
  logger.error("That's it, beautiful and simple logging, error!")


if __name__ == "__main__":
  setup_logging()
  typer.run(main)
