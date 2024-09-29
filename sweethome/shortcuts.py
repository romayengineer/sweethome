"""
Shortcuts module.

This module contains shortcuts that can be quickly accessed in the REPL.

The shortcuts are:
    - p: opens the departments all page

"""

from typing import Any, Callable, Dict, Tuple

from playwright.sync_api import BrowserContext, Page, sync_playwright

from . import base, browser
from .sites import remax

current_page = None


def print_help() -> None:
    """
    Prints the help message for the shortcuts.
    """
    print("Shortcuts:")
    print("  l: opens the login page")
    print("  h: opens the home page")
    print("  d: opens the departments page")
    print("  n: opens the next department page")
    print("  c: gets the HTML of the current page")
    print("  p: prints this help message")


def goto_home(context: BrowserContext) -> Callable[[], None]:
    """
    Returns a shortcut function that navigates to the home page.

    Args:
        context (BrowserContext): The browser context to use for navigation.

    Returns:
        Callable[[], None]: A function that navigates to the home page when
        called.
    """
    return lambda: remax.goto.home(context)


def goto_login(context: BrowserContext) -> Callable[[], None]:
    """
    Returns a shortcut function that navigates to the login page.

    Args:
        context (BrowserContext): The browser context to use for navigation.

    Returns:
        Callable[[], None]: A function that navigates to the login page when
        called.
    """
    return lambda: remax.goto.login(context)


def goto_departments(context: BrowserContext) -> Callable[[], None]:
    """
    Returns a shortcut function that navigates to the departments all page.

    Args:
        context (BrowserContext): The browser context to use for navigation.

    Returns:
        Callable[[], None]: A function that navigates to the departments all
        page when called.
    """
    _globals = globals()

    def goto() -> Page:
        current_page = remax.goto.departments_all(context)
        _globals.update({"current_page": current_page})
        return current_page

    return goto


def goto_next_department(context: BrowserContext) -> Callable[[], None]:
    return lambda: remax.goto.department_next(context)


def get_html() -> Callable[[], str]:
    """
    Returns a shortcut function that gets the HTML of the current page.

    Returns:
        Callable[[], str]: A function that gets the HTML of the current page
        when called.
    """
    _globals = globals()

    def copy() -> str:
        return remax.copy.html(_globals.get("current_page"))

    return copy


def save_html() -> Callable[[], str]:
    """
    Returns a shortcut function that saves the HTML of the current page.

    Returns:
        Callable[[], str]: A function that saves the HTML of the current page
        and returns the path to the saved file when called.
    """

    def save() -> str:
        return base.pages.save_html(
            page=current_page,
            overwrite=True,
        )

    return save


def set() -> Dict[str, Callable[[], None]]:
    """
    Sets shortcuts.

    Assigns shortcuts to the global namespace, allowing the user to quickly
    access them in the REPL.

    The shortcuts are:

        - p: opens the departments all page

    Args:
        None

    Returns:
        A dict containing the shortcuts.
    """
    play = sync_playwright().start()
    new_browser = browser.new(play, headless=False)
    context = browser.context(new_browser)
    shortcuts = {
        "l": goto_login(context),
        "h": goto_home(context),
        "d": goto_departments(context),
        "n": goto_next_department(context),
        "c": get_html(),
        "p": print_help,
        "s": save_html(),
    }
    globals().update(shortcuts)
    return shortcuts


def run(command: str, shortcuts: Dict[str, Callable[[], None]]) -> Tuple[bool, Any]:
    """
    Runs a shortcut command.

    Checks if the command is a shortcut, and if so, runs the associated
    function.

    Args:
        command (str): The command to check.
        shortcuts (Dict[str, Callable[[], None]]): A dict containing the
        shortcuts.

    Returns:
        bool: True if the command was a shortcut, False otherwise.
    """
    if command in shortcuts:
        out = shortcuts[command]()
        return True, out
    return False, None
