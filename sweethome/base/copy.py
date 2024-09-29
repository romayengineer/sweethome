from sweethome.logging import Logger
from sweethome.types import Page

logger = Logger(__name__)


def html(page: Page) -> str:
    if page == None or page.is_closed():
        logger.error("Page is closed or does not exist")
        logger.error("set current_page by for example running shortcut 'd'")
        return None
    return page.content()
