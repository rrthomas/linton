"""Linton development web server

© Reuben Thomas <rrt@sc3d.org> 2024-2025
Released under the GPL version 3, or (at your option) any later version.
"""

import os
import subprocess
import urllib.parse
from http.server import BaseHTTPRequestHandler, HTTPServer

from xdg import Mime


def new_server(port: int, base_url: str, document_root: str) -> HTTPServer:
    class HTTPRequestHandler(BaseHTTPRequestHandler):
        def do_GET(self) -> None:
            """GET handler"""
            filename = None
            expand = False
            url_path = urllib.parse.unquote(
                urllib.parse.urlparse(self.path.removeprefix(base_url)).path
            )
            input_path = os.path.join(document_root, url_path)
            if os.path.isfile(input_path):
                filename = input_path
            elif os.path.basename(input_path) == "index.html":
                # If an 'index.html' is not found but it has a Nancy source file, use it.
                nancy_source = (
                    input_path.removesuffix("index.html") + "index.nancy.html"
                )
                if os.path.exists(nancy_source):
                    filename = nancy_source
                    url_path = url_path.removesuffix("index.html") + "index.nancy.html"
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
                        ["nancy", document_root, "-", f"--path={url_path}"],
                    )
                else:
                    with open(filename, "rb") as fh:
                        output = fh.read()
                self.send_response(200)
                self.send_header("Content-Type", mime_type)
                self.end_headers()
                self.wfile.write(output)

    return HTTPServer(("localhost", port), HTTPRequestHandler)
