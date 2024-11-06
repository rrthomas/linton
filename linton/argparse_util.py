"""
Linton argparse utilities
© Reuben Thomas <rrt@sc3d.org> 2024
Released under the GPL version 3, or (at your option) any later version.
"""

import argparse


def add_subcommand_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "base_url",
        metavar="URL",
        help="base URL of web site relative to root of server",
    )
    parser.add_argument(
        "document_root", metavar="DIRECTORY", help="directory containing source files"
    )
