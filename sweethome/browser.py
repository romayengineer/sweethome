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


def blank_page(play: PlaywrightContextManager) -> Page:
    """
    Creates a blank page.

    Args:
        play (PlaywrightContextManager): The Playwright context manager.

    Returns:
        Page: The blank page.
    """
    logger.debug("Creating blank page")
    return page(context(new(play)))


def new_blank_page() -> Page:
    play = sync_playwright().start()
    return blank_page(play)


if __name__ == "__main__":
    new_blank_page()
