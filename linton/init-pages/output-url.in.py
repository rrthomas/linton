#!/usr/bin/env python3
# Output the path from the root to `$path` as it will appear in the output.

# /// script
# requires-python = ">=3.9"
# ///

import re, sys
from pathlib import Path


# Read command-line arguments
path = Path(sys.argv[1])

type_ = path.suffix
path = path.with_suffix('')

nancy = path.suffix
path = path.with_suffix('')
assert nancy == '.nancy', nancy

path = path.with_suffix(type_)

print(str(path), end="")
