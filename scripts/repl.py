import sys
import os

cwd = os.getcwd()
if cwd not in sys.path:
    sys.path.append(cwd)

from sweethome.repl import run

if __name__ == "__main__":
    run()