from ..business_entity import BusinessEntity

class Team(BusinessEntity):
    def __init__(self, name="Team"):
        super().__init__(name)
        self.links = {
            'self': {
                'name': name,
                'href': f'https://api.bitbucket.org/1.0/teams/{name}'
            }
        }        
        self.languages = {
            'count': 1,
            'list': [
                'Python',
            ]
        }
        self.topics = {
            'count': 2,
            'list': [
                'BitBucket Topic 1',
                'BitBucket Topic 2',
            ]
        }
        self.repos = {
            'original': {
                'count': 3,
                'list': [
                    'BitBucket Original Repo 1',
                    'BitBucket Original Repo 2',
                    'BitBucket Original Repo 3',
                ]
            },
            'forked': {
                'count': 2,
                'list': [
                    'BitBucket Forked Repo 1',
                    'BitBucket Forked Repo 2',
                ]
            }            
        }        