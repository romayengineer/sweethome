from .errors import print_exc
from importlib import import_module

def run():
    while True:
        command = input(">>> ").strip()
        if command == "":
            continue
        if command == "exit":
            break
        try:
            if command.startswith("import "):
                module_name = command[7:]
                module = import_module(module_name)
                globals()[module_name] = module
                continue
            print(eval(command))
        except Exception:
            print_exc()
