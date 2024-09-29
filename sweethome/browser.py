from playwright.sync_api import (
    Browser,
    BrowserContext,
    Page,
    PlaywrightContextManager,
    sync_playwright,
)

from .config import default_timeout
from .logging import logger


def new(play: PlaywrightContextManager, headless: bool = False) -> Browser:
    logger.debug("Launching browser, headless: %s", headless)
    browser = play.chromium.launch(headless=headless)
    return browser


def context(browser: Browser) -> BrowserContext:
    logger.debug("Creating context")
    return browser.new_context()


def page(context: BrowserContext, timeout: int = default_timeout) -> Page:
    logger.debug("Creating page, timeout: %s", timeout)
    page = context.new_page()
    page.set_default_timeout(timeout)
    return page


def blank_page(play: PlaywrightContextManager, headless: bool = False) -> Page:
    """
    Create a new blank page in a browser.

    This function creates a new browser instance, a new context, and a new page
    in that context, effectively providing a blank page ready for use.

    Args:
        play (PlaywrightContextManager): The Playwright context manager.
        headless (bool, optional): Whether to run the browser in headless mode.
            Defaults to False.

    Returns:
        Page: A new blank Playwright page object.

    Note:
        This function combines the `new`, `context`, and `page` functions
        to create a fully set up page in one step.
    """
    logger.debug("Creating blank page")
    return page(context(new(play, headless=headless)))


def new_blank_page(headless: bool = False) -> Page:
    play = sync_playwright().start()
    return blank_page(play, headless=headless)


if __name__ == "__main__":
    new_blank_page()
