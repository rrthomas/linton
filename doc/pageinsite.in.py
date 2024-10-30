#!/usr/bin/env python3

import sys
import os.path

# Get command-line arguments
page = sys.argv[1]

pagename = os.path.dirname(page)
if pagename != ".":
    print(f": {pagename}")
