from importlib import import_module

from . import shortcuts
from .logging import Logger

logger = Logger(__name__)


def import_into_globals(command: str) -> None:
    """
    Imports a module into the global namespace.

    Args:
        command (str): A string containing the module name to import, prefixed
        with 'import '.

    Returns:
        None
    """
    module_name = command.split()[1]
    module = import_module(module_name)
    globals().update({module_name: module})


def run():
    """
    Runs the REPL (Read-Eval-Print Loop) indefinitely, accepting and executing
    user commands.

    Args:
        None

    Returns:
        None
    """
    shortcut_functions = shortcuts.set()
    while True:
        command = input(">>> ").strip()
        logger.info(f">>> {command}")
        if command == "":
            continue
        if command == "exit":
            break
        try:
            called, out = shortcuts.run(command, shortcut_functions)
            if called:
                logger.info("OUT: %s", out)
                continue
            if command.startswith("import "):
                import_into_globals(command)
                continue
            out = eval(command)
            logger.info("OUT: %s", out)
        except Exception:
            logger.print_exc()
