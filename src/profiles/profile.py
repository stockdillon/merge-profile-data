from .github.organization import Organization
from .bitbucket.team import Team

class Profile(object):
    def __init__(self, org: Organization=Organization(), team: Team=Team()):
        self.org: Organization = org
        self.team = team
        self.count_repos = org.count_repos + team.count_repos
        self.count_watchers = org.count_watchers + team.count_watchers
        self.count_followers = org.count_followers + team.count_followers
        self.topics = self.aggregate_topics()     
        self.languages = self.aggregate_languages()
        self.repos = self.aggregate_repos()
        self.observers = {
            'original': {
                'count': 3,
                'list': [

                ]
            },
            'forked': {
                'count': 3,
                'list': [
                    
                ]
            }            
        }
    def aggregate_topics(self):
        """
        TODO: Create base `Aggregate` class
        Make `Topics` it's own class that extends `Aggregate`
        Create new class responsible for executing aggregator functionality
        `Profile` class contains child `Aggregator` (composition)
        """
        return {
            'count': self.org.topics['count'] + self.team.topics['count'],
            'list': self.org.topics['list'] + self.team.topics['list']
        }
    def aggregate_languages(self):
        """
        Aggregates the languages from each source (e.g. GitHub and BitBucket)
        """
        return {
            'count': self.org.languages['count'] + self.team.languages['count'],
            'list': self.org.languages['list'] + self.team.languages['list']
        }
    def aggregate_repos(self):
        """
        Aggregates the repos from each source (e.g. GitHub and BitBucket)
        """
        return {
            'original': self.get_aggregate(self.org.repos['original'], self.team.repos['original']),
            'forked': self.get_aggregate(self.org.repos['forked'], self.team.repos['forked']),            
        }
    def get_aggregate(self, a1, a2):
        return {
            'count': a1['count'] + a2['count'],
            'list': a1['list'] + a2['list']
        }        