"""Linton 'init' subcommand

© Reuben Thomas <rrt@sc3d.org> 2024
Released under the GPL version 3, or (at your option) any later version.
"""

import argparse
import os
import shutil

import importlib_resources

from linton.warnings_util import die


def run(args: argparse.Namespace, _render_env: dict[str, str]) -> None:
    """'init' command handler"""
    # Check directory does not exist.
    if os.path.exists(args.directory):
        die(f"output {args.directory} already exists")

    # Copy the demo files to the new project
    with importlib_resources.as_file(importlib_resources.files()) as fspath:
        shutil.copytree(
            os.path.join(fspath, "..", "init-pages"),
            args.directory,
            # See https://github.com/rrthomas/linton/issues/7
            ignore=shutil.ignore_patterns("__pycache__"),
        )


def add_subparser(subparsers: argparse._SubParsersAction) -> None:  # type: ignore[type-arg]
    parser = subparsers.add_parser(
        "init",
        help="create a new Linton project",
    )
    parser.add_argument("directory", metavar="DIRECTORY", help="output directory")
    parser.set_defaults(func=run)
