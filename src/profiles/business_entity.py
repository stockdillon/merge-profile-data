class BusinessEntity(object):
    def __init__(self, name="BusinessEntity"):
        self.name = name
        self.repositories = []
        self.projects = []
        self.count_repos = 0
        self.count_watchers = 0
        self.count_followers = 0        