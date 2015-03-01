from dotDict import DotDict

# @class BaseGame: the basics of any game, basically state management. Do not modify
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

    def _connected(self, data):
        self.name = data['gameName']
        self.session = data['gameSession']
