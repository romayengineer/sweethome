"""
Run the REPL (Read-Eval-Print Loop) for SweetHome.

This script will run the REPL, allowing you to enter Python commands and
execute them in the context of the SweetHome application.

The REPL is useful for testing and debugging code, as well as for running
one-off commands.

The REPL imports the current working directory into the Python path, so
you can import modules and functions from your local codebase.

Example usage:

    $ python -m scripts.repl

Then you can enter Python commands:

    >>> page = browser.new_blank_page()
    >>> page.goto("https://www.google.com")
    >>> page.title()
    'Google'

TODO fix assigment statements in REPL, a = 1 raises SyntaxError

"""

import os
import sys

cwd = os.getcwd()
if cwd not in sys.path:
    sys.path.append(cwd)

from sweethome.repl import run

if __name__ == "__main__":
    run()
