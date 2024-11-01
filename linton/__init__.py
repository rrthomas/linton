#!/usr/bin/env python3
#
# © Reuben Thomas <rrt@sc3d.org> 2023-2024
# Released under the GPL version 3, or (at your option) any later version.

import os
import sys
import shutil
from pathlib import Path
import argparse
import subprocess
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib
import warnings
from warnings import warn
from typing import (
    Optional,
    List,
    Union,
    Type,
    NoReturn,
    TextIO,
)

from xdg import Mime


# Error messages
def simple_warning(  # pylint: disable=too-many-positional-arguments,too-many-arguments
    message: Union[Warning, str],
    category: Type[Warning],  # pylint: disable=unused-argument
    filename: str,  # pylint: disable=unused-argument
    lineno: int,  # pylint: disable=unused-argument
    file: Optional[TextIO] = sys.stderr,
    line: Optional[str] = None,  # pylint: disable=unused-argument
) -> None:
    """Print an error message."""
    print(f"{parser.prog}: {message}", file=file or sys.stderr)


warnings.showwarning = simple_warning


def die(code: int, msg: str) -> NoReturn:
    """Print error message `msg` and exit with error code `code`."""
    warn(msg)
    sys.exit(code)


def set_globals(args: argparse.Namespace) -> None:
    # Set globals.
    global base_url, document_root
    base_url = args.base_url
    document_root = Path(os.path.expanduser(args.document_root)).resolve()

    # Set up environment for executable $include scripts.
    global render_env
    render_env = dict(os.environ)
    render_env["LINTON_BASE_URL"] = base_url
    render_env["LINTON_DOCUMENT_ROOT"] = str(document_root)



# 'publish' command
def publish(args: argparse.Namespace) -> None:
    """'publish' command handler"""
    set_globals(args)

    # Check output directory is not under document_root
    # FIXME: move this functionality to Nancy
    output_path = Path(args.output)
    if output_path.absolute().is_relative_to(document_root):
        die(1, "output directory cannot be a subdirectory of input")

    # Ensure output directory exists and is empty
    # FIXME: move this functionality to Nancy
    os.makedirs(output_path, exist_ok=True)
    if len(os.listdir(output_path)) > 0:
        if not args.force:
            die(1, f"output directory {output_path} is not empty")
        shutil.rmtree(output_path)
        os.mkdir(output_path)

    # Render the project files to the output
    subprocess.check_output(["nancy", document_root, output_path], env=render_env)


# 'serve' command
class HTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:  # pylint: disable=invalid-name
        """GET handler"""
        filename = None
        expand = False
        url_path = urllib.parse.unquote(
            os.path.splitroot(self.path.removeprefix(base_url))[2]
        ).removesuffix("/")
        input_path = os.path.join(document_root, url_path)
        if os.path.isdir(input_path):
            index_path = os.path.join(input_path, "body.in.md")
            if os.path.exists(index_path):
                self.send_response(302)
                self.send_header("Location", os.path.join(url_path, "index.html"))
                self.end_headers()
                return
        elif os.path.isfile(input_path):
            filename = input_path
        elif os.path.basename(input_path) == "index.html":
            # If an 'index.html' is not found but it has a Nancy source file, use it.
            nancy_source = input_path.removesuffix("index.html") + "index.nancy.html"
            if os.path.exists(nancy_source):
                filename = nancy_source
                url_path = url_path.removesuffix("index.html") + "index.nancy.html"
                expand = True
        if filename is None:
            self.send_response(404)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            # FIXME: Use a 'notfound.nancy.html' template for this, as with
            # DarkGlass. Resurrect the docs!
            self.wfile.write(
                b"<html><head><title>No such page</title><body>No such page</body></html>"
            )
        else:
            mime_type = str(Mime.get_type2(filename).canonical())
            if expand:
                output = subprocess.check_output(
                    ["nancy", document_root, "-", f"--path={url_path}"],
                    env=render_env,
                )
            else:
                with open(filename, "rb") as fh:
                    output = fh.read()
            self.send_response(200)
            self.send_header("Content-Type", mime_type)
            self.end_headers()
            self.wfile.write(output)


def serve(args: argparse.Namespace) -> None:
    """'serve' command handler"""
    set_globals(args)
    httpd = HTTPServer(("localhost", 0), HTTPRequestHandler)
    [host, port] = httpd.server_address
    print(f"Connect to server at http://{str(host)}:{port}{base_url}")
    httpd.serve_forever()


# Command-line arguments
parser = argparse.ArgumentParser(
    description="Make a web site from Markdown files and other resources.",
)
parser.add_argument(
    "-V",
    "--version",
    action="version",
    version="%(prog)s 0.7 (22 Oct 2024) by Reuben Thomas <rrt@sc3d.org>",
)

subparsers = parser.add_subparsers(required=True, title="subcommands")


def add_subcommand_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "base_url",
        metavar="URL",
        help="base URL of web site relative to root of server",
    )
    parser.add_argument(
        "document_root", metavar="DIRECTORY", help="directory containing source files"
    )


base_url: str
document_root: Path
render_env: dict[str, str]

publish_parser = subparsers.add_parser(
    "publish",
    help="convert a directory of Markdown files and other resources into a web site.",
    epilog="The output DIRECTORY cannot be a subdirectory of the source directory.",
)
publish_parser.add_argument(
    "--force",
    action="store_true",
    help="overwrite output directory even if it is not empty",
)
add_subcommand_arguments(publish_parser)
publish_parser.add_argument("output", metavar="DIRECTORY", help="output directory")
publish_parser.set_defaults(func=publish)

serve_parser = subparsers.add_parser(
    "serve",
    help="serve a Linton web site locally on your computer, for testing",
)
add_subcommand_arguments(serve_parser)
serve_parser.set_defaults(func=serve)


def main(argv: List[str] = sys.argv[1:]) -> None:
    args = parser.parse_args(argv)
    args.func(args)
