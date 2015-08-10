from delta_mergeable import DeltaMergeable

# @class BaseGameObject: the base class that every game object within a game inherit from for Python manipulation that would be redundant via Creer
class BaseGameObject(DeltaMergeable):
    def __init__(self):
        DeltaMergeable.__init__(self)
