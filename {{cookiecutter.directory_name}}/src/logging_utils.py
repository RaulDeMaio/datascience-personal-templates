import logging
import os
import io
import sys
from datetime import datetime

def setup_logger(
    name: str = "project_logger",
    level: int = logging.INFO,
    log_to_file: bool = True,
    log_dir: str = "logs",
    encoding: str = "utf-8"
) -> logging.Logger:
    """Create and return a standardized logger with UTF-8 support."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if logger.handlers:
        return logger  # prevent duplicate handlers when re-running

    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Console handler with explicit UTF-8 handling
    if hasattr(sys.stdout, "buffer"):
        stream = io.TextIOWrapper(
            sys.stdout.buffer,
            encoding=encoding,
            line_buffering=True
        )
    else:
        # Jupyter notebooks use OutStream without buffer
        try:
            sys.stdout.reconfigure(encoding=encoding)
        except Exception:
            pass
        stream = sys.stdout
    ch = logging.StreamHandler(stream=stream)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # File handler (optional)
    if log_to_file:
        os.makedirs(log_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = os.path.join(log_dir, f"log_{timestamp}.log")
        fh = logging.FileHandler(log_file, encoding=encoding)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger
