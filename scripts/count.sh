#!/bin/bash
#
# Count lines of Python code in this repository.
#
# Usage:
#
#   ./count.bash
#
# Output:
#
#   The number of lines of Python code in this repository, excluding virtualenv.

find . -type f -name '*.py' -not -path './venv/*' | xargs wc -l
