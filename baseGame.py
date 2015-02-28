# @class BaseGame: the basics of any game, basically state management. Do not modify
import pprint

class DotDict(dict):
    """
    Creates objects that behave much like a dictionaries, but allow nested
    key access using object '.' (dot) lookups.
    from: http://code.activestate.com/recipes/576586-dot-style-nested-lookups-over-dictionary-based-dat/
    """
    def __init__(self, d):
        for k in d:
            if isinstance(d[k], dict):
                self.__dict__[k] = DotDict(d[k])
            elif isinstance(d[k], (list, tuple)):
                l = []
                for v in d[k]:
                    if isinstance(v, dict):
                        l.append(DotDict(v))
                    else:
                        l.append(v)
                self.__dict__[k] = l
            else:
                self.__dict__[k] = d[k]

    def __getitem__(self, name):
        if name in self.__dict__:
            return self.__dict__[name]

    def __iter__(self):
        return iter(self.__dict__.keys())

    def __repr__(self):
        return pprint.pformat(self.__dict__)

class BaseGame:
    def __init__(self):
        self.state = False
        self.ai = False

    def updateState(self, newState):
        self.originalState = self.state
        self.state = DotDict(newState)

        if not self.originalState:
            self.ai.init()

        self.ai.gameUpdated()

    def setAI(self, ai):
        self.ai = ai
