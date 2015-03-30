# @class BaseGameObject: the base class that every game object within a game inherit from for Python manipulation that would be redundant via Creer
class BaseGameObject:
    def __init__(self, data):
        self.game = data['game']
        self.ai = data['ai']
        self.client = data['client']


    def __contains__(self, key):
        return hasattr(self, key)

    def __getitem__(self, key):
        return getattr(self, key)
