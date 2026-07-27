#!/usr/bin/env python3

import os
import sys
from datetime import datetime
from pathlib import Path


# Get command-line arguments
page = Path(sys.argv[1]).parent
realpath = Path(os.environ["NANCY_INPUT"]) / page
file = Path(os.environ["NANCY_INPUT"]) / page / "body.in.md"

time = os.stat(file).st_mtime
dt = datetime.fromtimestamp(time)
print(dt.strftime("%Y/%m/%d"), end="")
