import http.server
import socketserver
import json
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
from profiles.github.organization import Organization
from profiles.bitbucket.team import Team
from profiles.profile import Profile
import urllib

org_pygame = Organization(name='pygame')
org_mailchimp = Organization(name='mailchimp')
orgs = {
    'pygame':org_pygame,
    'mailchimp':org_mailchimp,
}

team_pygame = Team(name='pygame')
team_mailchimp = Team(name='mailchimp')
teams = {
    'pygame':team_pygame,
    'mailchimp':team_mailchimp,
}

class Handler(BaseHTTPRequestHandler):
    def parse_params(self, path=''):
        params = urllib.parse.urlparse(path)
        param_dict = urllib.parse.parse_qs(params.query)
        return param_dict
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        param_dict = self.parse_params(self.path)
        print('param_dict:', param_dict)
        org_name = param_dict.get('github')[0]
        team_name = param_dict.get('bitbucket')[0]
        print('org name:', org_name)
        print('team name:', team_name)
        org = {}
        team = {}
        if org_name in orgs:
            org = orgs[org_name].__dict__
        if team_name in teams:
            team = teams[team_name].__dict__            
        prof = Profile(org, team)
        self.wfile.write(bytes(json.dumps(prof.__dict__), encoding='utf-8'))


PORT = 5000

myserver = HTTPServer(("", 5000), Handler)
myserver.serve_forever()