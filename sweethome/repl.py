from .errors import print_exc

def run():
    while True:
        command = input(">>> ").strip()
        if command == "":
            continue
        if command == "exit":
            break
        try:
            print(eval(command))
        except SyntaxError:
            print_exc()
