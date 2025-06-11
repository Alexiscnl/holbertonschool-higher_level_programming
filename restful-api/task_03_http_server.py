#!/usr/bin/python3
"""Simple API using http.server"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import socketserver

PORT = 8000


class MyHandler(BaseHTTPRequestHandler):
    """Custom handler to manage GET requests"""

    def do_GET(self):
        """Handle GET requests"""
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!".encode())

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            dic = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(dic).encode())

        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            dic2 = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(dic2).encode())

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            dic_status = {"status": "OK"}
            self.wfile.write(json.dumps(dic_status).encode())

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"404 - Not Found")

with socketserver.TCPServer(("", PORT), MyHandler) as http:
    print(f"Serving at port {PORT}")
    http.serve_forever()
