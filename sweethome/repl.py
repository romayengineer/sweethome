from importlib import import_module

from .errors import print_exc


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


def run():
    """
    Runs the REPL (Read-Eval-Print Loop) indefinitely, accepting and executing user commands.

    Args:
        None

    Returns:
        None
    """
    while True:
        command = input(">>> ").strip()
        if command == "":
            continue
        if command == "exit":
            break
        try:
            if command.startswith("import "):
                import_into_globals(command)
                continue
            print(eval(command))
        except Exception:
            print_exc()
