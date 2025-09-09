import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

def setup_logging():
    logs_dir = Path(__file__).parent.parent / "logs"
    logs_dir.mkdir(exist_ok=True)
    fh = RotatingFileHandler(logs_dir / "app.log", maxBytes=5*1024*1024, backupCount=3)
    fh.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    logger = logging.getLogger("customer_api")
    logger.setLevel(logging.INFO)
    # Avoid duplicate handlers if called multiple times
    if not logger.handlers:
        logger.addHandler(ch)
        logger.addHandler(fh)
    return logger
