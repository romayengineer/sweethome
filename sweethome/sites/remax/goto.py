from playwright.sync_api import BrowserContext, Page

from sweethome import browser

from . import urls


def home(context: BrowserContext) -> Page:
    page = browser.page(context)
    page.goto(urls.home)
    return page


def departments_all(context: BrowserContext) -> Page:
    page = browser.page(context)
    page.goto(urls.departments_all)
    return page
