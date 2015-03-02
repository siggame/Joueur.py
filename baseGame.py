from easydict import EasyDict

# @class BaseGame: the basics of any game, basically state management. Do not modify
class BaseGame:
    def __init__(self):
        self.state = False
        self.ai = False


    def _connected(self, data):
        self.name = data['gameName']
        self.session = data['gameSession']
        self._serverConstants = EasyDict(data['constants'])

    # the main socket handler should call this once, when the inital state is sent
    def setState(self, newState):
        originalState = self.state
        self.state = EasyDict(newState)

        if not originalState:
            self.ai.init()

        self.ai.gameUpdated()


    def applyDeltaState(self, deltaState):
        self._mergeDelta(self.state, deltaState)

        self.ai.gameUpdated()

    def _mergeDelta(self, state, delta):
        deltaLength = -1
        if self._serverConstants.DELTA_ARRAY_LENGTH in delta:
            deltaLength = delta[self._serverConstants.DELTA_ARRAY_LENGTH]
            del delta[self._serverConstants.DELTA_ARRAY_LENGTH] # we don't want to copy this key/value over to the state, it was just to signify it is an array

        if deltaLength > -1: # then this part in the state is an array
            while len(state) > deltaLength: # remove elements off the array to make it's size correct.
                state.pop()
            while len(state) < deltaLength: # append elements on the array to make it's size correct.
                state.append(None)

        for key in delta: # deltas will always be objects when iterating through, arrays just have keys of numbers
            stateKey = key # array's keys are real numbers, not strings e.g. "1"
            keyInState = key in state

            if isinstance(state, list):
                stateKey = int(key)
                keyInState = stateKey < len(state)

            if delta[key] == self._serverConstants.DELTA_REMOVED:
                if keyInState:
                    del state[stateKey]
            elif isinstance(delta[key], dict) and keyInState and (isinstance(state[stateKey], dict) or isinstance(state[stateKey], list)):
                self._mergeDelta(state[stateKey], delta[key])
            else:
                state[stateKey] = delta[key]


    def setAI(self, ai):
        self.ai = ai
