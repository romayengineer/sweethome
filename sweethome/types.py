from typing import Any

from playwright.sync_api import Browser, BrowserContext, Locator
from playwright.sync_api import Page as _Page
from playwright.sync_api import PlaywrightContextManager as ContextManager
from playwright.sync_api import Response, expect
from playwright.sync_api import sync_playwright as get_context

from sweethome.logging import Logger

logger = Logger(__name__)

__all__ = [
    "Browser",
    "BrowserContext",
    "ContextManager",
    "Page",
    "current_page",
    "expect",
    "get_context",
    "Locator",
]

# stores the last page visited
current_page = None


class Page:
    """
    A wrapper around the playwright Page object.
    """

    def __init__(self, page: _Page):
        """
        Updates the current_page global variable when initialized

        Args:
            page (_Page): the playwright page object
        """
        global current_page
        logger.debug("Setting current page to %s", page.url)
        self.page = page
        current_page = self

    def goto(self, url: str, *args, **kwargs) -> Response:
        logger.info("Navigating to %s", url)
        return self.page.goto(url, *args, **kwargs)

    def __getattribute__(self, item: str) -> Any:
        """
        Custom __getattribute__ method to delegate attribute access to the
        underlying page object.

        This method intercepts attribute access on the Page wrapper class. If
        the requested attribute is 'page', it returns the actual page object
        stored in this instance.

        For all other attributes, it delegates the access to the underlying
        Playwright page object.

        Args:
            item (str): The name of the attribute being accessed.

        Returns:
            Any: The value of the requested attribute, either from this instance or the underlying page object.
        """
        if item == "page":
            return object.__getattribute__(self, item)
        return getattr(self.page, item)
