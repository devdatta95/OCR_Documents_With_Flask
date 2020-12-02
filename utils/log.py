import logging
from logging.handlers import TimedRotatingFileHandler


def log_setup(logname, file):
    logger = logging.getLogger(logname)
    logger.setLevel(logging.DEBUG)
    handler = TimedRotatingFileHandler(file, "midnight", interval=1, encoding="utf-8")
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    handler.suffix = "%Y%m%d"
    logger.addHandler(handler)
    return logger
