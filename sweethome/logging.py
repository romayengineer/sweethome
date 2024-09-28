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
        logging_level = logging.getLevelName(logger.getEffectiveLevel()).upper()
        for line in s.splitlines():
            print(f"{logging_level}: ", line)
        logger.debug(s)


logger_file = MockLoggerFile()
