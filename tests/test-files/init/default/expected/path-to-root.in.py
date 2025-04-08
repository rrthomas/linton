#!/usr/bin/env python3
# Output the path from the first argument to the root of the directory

# /// script
# requires-python = ">=3.9"
# ///

import sys
from pathlib import Path


# Read command-line arguments
page = Path(sys.argv[1])
directory = page.parent

path_to_root = Path(".")
while directory != Path("."):
    directory = directory.parent
    path_to_root /= ".."

print(str(path_to_root), end="")
