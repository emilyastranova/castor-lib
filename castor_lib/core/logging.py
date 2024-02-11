"""Castor core logging module."""
from loguru import logger
from loguru._logger import Logger

def get_logger(name: str) -> Logger:
    """Get logger instance."""
    return logger.bind(name=name)
