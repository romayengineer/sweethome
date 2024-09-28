import logging
import traceback

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def print_exc():
    traceback.print_exc(file=logger_file)


class MockLoggerFile:
    def __init__(self, logger: logging.Logger = logger) -> None:
        self.logger = logger

    def write(self, s):
        for line in s.splitlines():
            print("DEBUG: ", line)
        logger.debug(s)


logger_file = MockLoggerFile()
