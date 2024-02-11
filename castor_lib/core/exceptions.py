"""Castor core exceptions module."""

from castor_lib.core.logging import get_logger

logger = get_logger(__name__)

class CastorException(Exception):
    """Base class for Castor exceptions."""
    pass
