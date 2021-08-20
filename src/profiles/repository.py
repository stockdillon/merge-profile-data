from repo_type import RepoType

class Repository(object):
    def __init__(self, name="Repository", repo_type: RepoType=None):
        self.name = name
        self.type = repo_type