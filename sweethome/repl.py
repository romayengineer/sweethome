from importlib import import_module
from typing import Callable, Dict

from playwright.sync_api import sync_playwright

from . import browser
from .errors import print_exc
from .sites import remax

eval_imports = [browser, remax]


def import_into_globals(command: str) -> None:
    """
    Imports a module into the global namespace.

    Args:
        command (str): A string containing the module name to import, prefixed with 'import '.

    Returns:
        None
    """
    module_name = command.split()[1]
    module = import_module(module_name)
    globals().update({module_name: module})


def set_shortcuts() -> Dict[str, Callable[[], None]]:
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


def run_shortcut(command: str, shortcuts: Dict[str, Callable[[], None]]) -> bool:
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


def run():
    """
    Runs the REPL (Read-Eval-Print Loop) indefinitely, accepting and executing user commands.

    Args:
        None

    Returns:
        None
    """
    eval_imports
    shortcuts = set_shortcuts()
    while True:
        command = input(">>> ").strip()
        if command == "":
            continue
        if command == "exit":
            break
        try:
            if run_shortcut(command, shortcuts):
                continue
            if command.startswith("import "):
                import_into_globals(command)
                continue
            print(eval(command))
        except Exception:
            print_exc()
