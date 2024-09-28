"""
Shortcuts module.

This module contains shortcuts that can be quickly accessed in the REPL.

The shortcuts are:
    - p: opens the departments all page

"""

from typing import Callable, Dict

from playwright.sync_api import sync_playwright

from . import browser
from .sites import remax


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
    shortcuts = {"p": lambda: remax.goto.departments_all(context)}
    globals().update(shortcuts)
    return shortcuts


def run(command: str, shortcuts: Dict[str, Callable[[], None]]) -> bool:
    """
    Runs a shortcut command.

    Checks if the command is a shortcut, and if so, runs the associated function.

    Args:
        command (str): The command to check.
        shortcuts (Dict[str, Callable[[], None]]): A dict containing the shortcuts.

    Returns:
        bool: True if the command was a shortcut, False otherwise.
    """
    if command in shortcuts:
        shortcuts[command]()
        return True
    return False
