#!/usr/bin/env python3
# Convert given Markdown file to HTML fragment on stdout

import sys

from markdown_it import MarkdownIt


md = MarkdownIt("commonmark", {"typographer": True}).enable("table").enable("smartquotes")
sys.stdout.write(md.render(sys.stdin.read()))
