import http.server
import socketserver
import json
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
from github import organization

org = organization.Organization()

class Profile(object):
    def __init__(self):
        self.test = 'success'
        self.org = org.__dict__

prof = Profile()

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(bytes(json.dumps(prof.__dict__), encoding='utf-8'))


PORT = 5000

myserver = HTTPServer(("", 5000), Handler)
myserver.serve_forever()