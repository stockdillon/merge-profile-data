class BusinessEntity(object):
    def __init__(self, name="BusinessEntity"):
        self.name = name
        self.repositories = {
            'count': 0,
            'list': []
        }
        self.projects = []
        self.count_repos = 1
        self.count_watchers = 1
        self.count_followers = 1