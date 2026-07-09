#!/usr/bin/env python3
# Convert given Markdown file to HTML fragment on stdout

import sys

from markdown_it import MarkdownIt


md = MarkdownIt()
sys.stdout.write(md.render(sys.stdin.read()))
