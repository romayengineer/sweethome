import logging
from playwright.sync_api import sync_playwright
from playwright.sync_api import Browser, BrowserContext, Page
from playwright.sync_api import PlaywrightContextManager

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
default_timeout = 5000

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

if __name__ == "__main__":
    with sync_playwright() as play:
        blank_page(play)