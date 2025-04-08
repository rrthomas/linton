#!/usr/bin/env python3

# /// script
# requires-python = ">=3.9"
# ///

import sys
from pathlib import Path


# Get command-line arguments
page = Path(sys.argv[1])

pagename = page.parent
if pagename != Path("."):
    print(f": {str(pagename)}", end="")
