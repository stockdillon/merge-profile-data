import http.server
import socketserver
import json
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer

class Profile():
    def __init__(self):
        self.test = 'success'
    

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        # self.wfile.write(bytes(json.dumps({'hello': 'world', 'received': 'ok'}), "utf-8"))
        # self.wfile.write(json.dumps({'hello': 'world', 'received': 'ok'}))
        self.wfile.write(bytes(json.dumps({'hello': 'world', 'received': 'ok'}), encoding='utf-8'))


PORT = 5000

myserver = HTTPServer(("", 5000), Handler)
myserver.serve_forever()