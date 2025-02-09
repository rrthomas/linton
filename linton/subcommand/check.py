"""Linton 'check' subcommand

© Reuben Thomas <rrt@sc3d.org> 2025
Released under the GPL version 3, or (at your option) any later version.
"""

import argparse
import os
import subprocess
from multiprocessing import Process

from ..server import new_server


def run(args: argparse.Namespace) -> None:
    """'check' command handler"""
    with new_server(0, args.base_url, args.document_root) as httpd:
        def run_server():
            httpd.serve_forever()
        p = Process(target=run_server)
        p.start()
        [host, port] = httpd.server_address
        subprocess.check_call(["linkchecker", f"http://{host}:{port}/index.html"])
        p.terminate()


def add_subparser(subparsers: argparse._SubParsersAction) -> None:
    parser = subparsers.add_parser(
        "check",
        help="check the internal hyperlinks of a Linton web site",
    )
    parser.add_argument(
        "document_root",
        metavar="DIRECTORY",
        help="directory containing source files [default: current working directory]",
        default=os.getcwd(),
        nargs="?",
    )
    parser.set_defaults(func=run)
