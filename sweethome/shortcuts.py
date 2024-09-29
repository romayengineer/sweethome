"""
Shortcuts module.

This module contains shortcuts that can be quickly accessed in the REPL.

The shortcuts are:
    - p: opens the departments all page

"""

from typing import Any, Callable, Dict, List, Tuple

import sweethome.types as types
from sweethome.types import BrowserContext, Page, get_context

from . import base, browser
from .logging import Logger
from .sites import remax
from .sites.remax.get import DepartmentItem, get_departments_all

logger = Logger(__name__)


def print_help() -> None:
    """
    Prints the help message for the shortcuts.
    """
    logger.info("Shortcuts:")
    logger.info("  l: opens the login page")
    logger.info("  h: opens the home page")
    logger.info("  d: opens the departments page")
    logger.info("  n: opens the next department page")
    logger.info("  c: gets the HTML of the current page")
    logger.info("  p: prints this help message")
    logger.info("  g: gets the departments from the current page")


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

    def goto() -> Page:
        return remax.goto.departments_all(context)

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

    def copy() -> str:
        return remax.copy.html(types.current_page)

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
            page=types.current_page,
            overwrite=True,
        )

    return save


def get_departments_from_page() -> Callable[[], List[DepartmentItem]]:
    """
    Returns a shortcut function that gets the departments from the current page.

    Returns:
        Callable[[], List[DepartmentItem]]: A function that gets the departments
        from the current page when called.
    """
    return lambda: get_departments_all(page=types.current_page)


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
    play = get_context().start()
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
        "g": get_departments_from_page(),
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
