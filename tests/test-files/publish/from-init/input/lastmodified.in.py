#!/usr/bin/env python3

import os
import sys
from datetime import datetime
from pathlib import Path


# Get command-line arguments
basename = sys.argv[1]
file = Path(os.environ["NANCY_INPUT"]) / basename

time = os.stat(file).st_mtime
dt = datetime.fromtimestamp(time)
print(dt.strftime("%Y/%m/%d"), end="")
