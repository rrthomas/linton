#!/usr/bin/env python3

import sys
import os.path

# Get globals from environment variables
BaseUrl = os.environ["LINTON_BASE_URL"]

# Get command-line arguments
page = sys.argv[1]

# Extract page name and normalize path
path = os.path.dirname(page)
if path == ".":
    path = ""
parents = path.removesuffix("$")

# Generate and print breadcrumb
desc = os.path.basename(parents)
tree = ""
classes = "breadcrumb-item breadcrumb-active"
while parents not in ("", ".", "/"):
    tree = f'<li class="{classes}"><a href="{BaseUrl}{parents}">{desc}</a></li>{tree}'
    classes = "breadcrumb-item"
    parents = os.path.dirname(parents)
    desc = os.path.basename(parents)
print(f'<li class="breadcrumb-item"><a href="{BaseUrl}">$include{{Title.in.txt}}</a></li>{tree}')
