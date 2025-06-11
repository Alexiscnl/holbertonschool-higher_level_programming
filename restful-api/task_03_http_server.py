#!/usr/bin/python3
"""Python web server that handles different HTTP endpoints"""
import http.server
import socketserver
import json


PORT = 8000


class MyHandler(http.server.BaseHTTPRequestHandler):
    """Custom HTTP request handler class"""

    def do_GET(self):
        """Handle GET requests to different endpoints"""

        # Root endpoint
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!".encode())

        # Data endpoint
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode())

        # Info endpoint
        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(info).encode())

        # Status endpoint
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("OK".encode())

        # 404 Handler
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("Endpoint not found".encode())


with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
