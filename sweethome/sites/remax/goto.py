
from playwright.sync_api import Page, BrowserContext
from sweethome import browser
from . import urls

def home(context: BrowserContext) -> Page:
    page = browser.page(context)
    page.goto(urls.home)
    return page