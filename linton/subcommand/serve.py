"""Linton 'serve' subcommand

© Reuben Thomas <rrt@sc3d.org> 2024-2025
Released under the GPL version 3, or (at your option) any later version.
"""

import argparse
import os
import subprocess
import urllib.parse
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

from xdg import Mime


def run(args: argparse.Namespace) -> None:
    """'serve' command handler"""

    class HTTPRequestHandler(BaseHTTPRequestHandler):
        def do_GET(self) -> None:
            """GET handler"""
            filename = None
            expand = False
            url_path = urllib.parse.unquote(
                urllib.parse.urlparse(self.path.removeprefix(args.base_url)).path
            )
            input_path = Path(args.document_root) / url_path
            if input_path.is_file():
                filename = input_path
            else:
                # If a file is not found but it has a Nancy source file, use it.
                suffix = input_path.suffix
                nancy_suffix = f".nancy{suffix}"
                nancy_source = input_path.with_suffix(nancy_suffix)
                if os.path.exists(nancy_source):
                    filename = nancy_source
                    url_path = url_path.removesuffix(suffix) + nancy_suffix
                    expand = True
            if filename is None:
                self.send_response(404)
                self.send_header("Content-Type", "text/html")
                self.end_headers()
                self.wfile.write(
                    b"<html><head><title>No such page</title><body>No such page</body></html>"
                )
            else:
                mime_type = str(Mime.get_type2(filename).canonical())
                if expand:
                    output = subprocess.check_output(
                        ["nancy", args.document_root, "-", f"--path={url_path}"],
                    )
                else:
                    with open(filename, "rb") as fh:
                        output = fh.read()
                self.send_response(200)
                self.send_header("Content-Type", mime_type)
                self.end_headers()
                self.wfile.write(output)

    httpd = HTTPServer(("localhost", args.port), HTTPRequestHandler)
    [host, port] = httpd.server_address
    print(f"Connect to server at http://{str(host)}:{port}/index.html")
    httpd.serve_forever()


def add_subparser(subparsers: argparse._SubParsersAction) -> None:
    parser = subparsers.add_parser(
        "serve",
        help="serve a Linton web site locally on your computer, for testing",
    )
    parser.add_argument(
        "--port",
        help="port on which to listen [default: random]",
        type=int,
        default=0,
    )
    parser.add_argument(
        "document_root",
        metavar="DIRECTORY",
        help="directory containing source files [default: current working directory]",
        default=os.getcwd(),
        nargs="?",
    )
    parser.set_defaults(func=run)
