import io
import logging
import traceback
from typing import Any

default_level = logging.DEBUG

# Create a formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")


class Logger:
    """
    A custom logger class that wraps the standard Python logging module.

    This class provides a simplified interface for creating and using loggers,
    with pre-configured formatting and handling. It also includes a custom
    method for printing exception tracebacks.

    Attributes:
        logger (logging.Logger): The underlying Python logger object.

    Methods:
        print_exc(): Prints the current exception traceback using the logger.
        __getattribute__(attr: str): Provides access to the underlying logger's
        attributes.

    The Logger class automatically sets up a StreamHandler for stdout and
    applies a default formatter. It uses the global default_level for both
    the logger and the handler.
    """

    def __init__(self, name: str, *args, **kwargs):
        # Create a logger
        self.logger = logging.getLogger(name, *args, **kwargs)
        self.logger.setLevel(default_level)

        # Create a StreamHandler for stdout
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(default_level)
        stream_handler.setFormatter(formatter)

        # Add the StreamHandler to the logger
        self.logger.addHandler(stream_handler)

        # Loggers don't have a setFormatter method, we need to set it on handlers
        for handler in self.logger.handlers:
            handler.setFormatter(formatter)

    def print_exc(self):
        """
        Print the current exception traceback using the logger.

        This function captures the current exception traceback, writes it to an
        in-memory file, and then logs each line of the traceback as an error
        message. This allows for a more structured and controlled way of logging
        exceptions compared to simply printing them to stdout or stderr.

        Returns:
            None
        """
        self.logger.error("Printing exception with sweethome.logging.print_exc")
        in_memory_file = io.StringIO()
        traceback.print_exc(file=in_memory_file)
        in_memory_file.flush()
        in_memory_file.seek(0)
        for line in in_memory_file.readlines():
            self.logger.error(line.rstrip("\n"))

    def __getattribute__(self, attr: str) -> Any:
        # if attr is not in the logger, return the attribute from the instance
        if attr in ("logger", "print_exc"):
            return object.__getattribute__(self, attr)
        return getattr(self.logger, attr)
