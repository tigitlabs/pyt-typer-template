# logger_util.py
import sys
from pathlib import Path
from typing import Optional

from loguru import logger

LOG_LEVEL = "WARNING"
LOG_FORMAT = "<green>{time:YYYY-MM-DD HH:mm:ss.SSS zz}</green> | <level>{level: <8}</level> | <yellow>Line {line: >4} ({file}):</yellow> <b>{message}</b>"


# Configure Loguru
def setup_logging(log_level: str = LOG_LEVEL, log_dest: Optional[Path] = None):
    if log_dest is None:
        log_dest = Path("logs")
    else:
        log_dest = Path(log_dest)
        log_dest.mkdir(parents=True, exist_ok=True)
        assert log_dest.is_dir()
    logger.remove()
    log_file: Path = log_dest / "debug.log"
    # Add logger for stdout for certain levels (e.g., DEBUG and INFO)
    logger.add(log_file, colorize=False, format=LOG_FORMAT, level="DEBUG")
    logger.add(sys.stdout, colorize=True, format=LOG_FORMAT, level=log_level)
    logger.debug("Initialized Logger")
    logger.debug(f"Log destination: {log_dest.absolute()}")
