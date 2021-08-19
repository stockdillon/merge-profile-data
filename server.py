import http.server
import socketserver
import json
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
from github import organization
import urllib

org_pygame = organization.Organization(name='pygame')
org_mailchimp = organization.Organization(name='mailchimp')
orgs = {
    'pygame':org_pygame,
    'mailchimp':org_mailchimp,
}

class Profile(object):
    def __init__(self, org={}, team={}):
        self.test = 'success'
        # self.org = org.__dict__

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        print(self.path)
        params = urllib.parse.urlparse(self.path)
        param_dict = urllib.parse.parse_qs(params.query)
        print('param_dict:', param_dict)
        org_name = param_dict.get('github')[0]
        team_name = param_dict.get('bitbucket')[0]
        print('org name:', org_name)
        print('team name:', team_name)
        prof = Profile()
        if org_name in orgs:
            prof.org = orgs[org_name].__dict__
        self.wfile.write(bytes(json.dumps(prof.__dict__), encoding='utf-8'))


PORT = 5000

myserver = HTTPServer(("", 5000), Handler)
myserver.serve_forever()