# main.py

import sys

from loguru import logger

LOG_LEVEL = "WARNING"
LOG_FORMAT = "<green>{time:YYYY-MM-DD HH:mm:ss.SSS zz}</green> | <level>{level: <8}</level> | <yellow>Line {line: >4} ({file}):</yellow> <b>{message}</b>"


# Configure Loguru
def setup_logging(log_level: str = LOG_LEVEL):
    # Remove default logger to stdout
    logger.remove()
    # Add logger for stdout for certain levels (e.g., DEBUG and INFO)
    logger.add("debug.log", colorize=False, format=LOG_FORMAT, level="DEBUG")
    logger.add(sys.stdout, colorize=True, format=LOG_FORMAT, level=log_level)
    logger.debug("Initialized Logger")
