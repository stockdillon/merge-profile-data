from ..business_entity import BusinessEntity

class Organization(BusinessEntity):
    def __init__(self, name="Organization"):
        super().__init__(name)
        self.packages = []
        self.people = []
        self.links = {
            'self': {
                'name': name,
                'href': f'https://api.github.com/orgs/{name}'
            }
        }
        self.languages = {
            'count': 2,
            'list': [
                'Typescript',
                'Javascript',
            ]
        }
        self.repos = {
            'original': {
                'count': 3,
                'list': [
                    'GitHub Original Repo 1',
                    'GitHub Original Repo 2',
                    'GitHub Original Repo 3',
                ]
            },
            'forked': {
                'count': 3,
                'list': [
                    'GitHub Forked Repo 1',
                    'GitHub Forked Repo 2',
                    'GitHub Forked Repo 3',                    
                ]
            }            
        }
        self.observers = {
            'count': 1,
            'list': [
                'Dillon'
            ]
        }
        self.topics = {
            'count': 2,
            'list': [
                'GitHub Topic 1',
                'GitHub Topic 2',
            ]
        }  
