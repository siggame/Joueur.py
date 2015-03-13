# @class GameObject: the base class that every game class within a game inherit from. The core idea is that game objects are tracked via ID.
class GameObject:
    def __init__(self, data):
        self.id = int(data['id'])
        self._game = data['game']
        self._ai = data['ai']
        self.log = []


    def __contains__(self, key):
        return hasattr(self, key)

    def __getitem__(self, key):
        return getattr(self, key)
