from .github.organization import Organization
from .bitbucket.team import Team

class Profile(object):
    def __init__(self, org: Organization=Organization(), team: Team=Team()):
        self.test = 'success'
        self.org = org
        self.team = team
        self.count_repos = org.count_repos + team.count_repos
        self.count_watchers = org.count_watchers + team.count_watchers
        self.count_followers = org.count_followers + team.count_followers