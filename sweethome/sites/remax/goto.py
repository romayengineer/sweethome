from playwright.sync_api import BrowserContext, Page

from sweethome import browser

from . import urls


def home(context: BrowserContext) -> Page:
    page = browser.page(context)
    page.goto(urls.home)
    return page


def login(context: BrowserContext) -> Page:
    page = browser.page(context)
    page.goto(urls.login)
    return page


def departments_all(context: BrowserContext) -> Page:
    page = browser.page(context)
    page.goto(urls.departments_all)
    return page


def department_next(context: BrowserContext) -> Page:
    page = browser.page(context)
    page.goto(urls.next_department())
    return page
