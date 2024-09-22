import logging
import traceback

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class MockLoggerFile:
    def write(self, s):
        for line in s.splitlines():
            print("DEBUG: ", line)
        logger.debug(s)

logger_file = MockLoggerFile()

def print_exc():
    return traceback.print_exc(file=logger_file)
