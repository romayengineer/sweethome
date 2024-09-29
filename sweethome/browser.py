from sweethome.types import Browser, BrowserContext, ContextManager, Page, get_context

from .config import default_timeout
from .logging import Logger

logger = Logger(__name__)


def new(play: ContextManager, headless: bool = False) -> Browser:
    logger.debug("Launching browser, headless: %s", headless)
    browser = play.chromium.launch(headless=headless)
    return browser


def context(browser: Browser) -> BrowserContext:
    logger.debug("Creating context")
    return browser.new_context()


def page(context: BrowserContext, timeout: int = default_timeout) -> Page:
    """
    Create a new page in the given browser context with a specified timeout.

    This function creates a new page within the provided browser context and
    setsits default timeout. It also wraps the page in a custom Page object.

    Args:
        context (BrowserContext): The browser context in which to create the
        page.
        timeout (int, optional): The default timeout for the page in
        milliseconds. Defaults to the value of default_timeout.

    Returns:
        Page: A new Page object with the specified timeout.

    Note:
        The created page is logged with its timeout value for debugging
        purposes.
    """
    logger.debug("Creating page, timeout: %s", timeout)
    page = Page(context.new_page())
    page.set_default_timeout(timeout)
    return page


def blank_page(play: ContextManager, headless: bool = False) -> Page:
    """
    Create a new blank page in a browser.

    This function creates a new browser instance, a new context, and a new page
    in that context, effectively providing a blank page ready for use.

    Args:
        play (ContextManager): The context manager.
        headless (bool, optional): Whether to run the browser in headless mode.
            Defaults to False.

    Returns:
        Page: A new blank page object.

    Note:
        This function combines the `new`, `context`, and `page` functions
        to create a fully set up page in one step.
    """
    logger.debug("Creating blank page")
    return page(context(new(play, headless=headless)))


def new_blank_page(headless: bool = False) -> Page:
    play = get_context().start()
    return blank_page(play, headless=headless)


if __name__ == "__main__":
    new_blank_page()
