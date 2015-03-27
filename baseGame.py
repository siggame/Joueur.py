from easydict import EasyDict
from utilities import camel_case_converter
from baseGameObject import BaseGameObject

# @class BaseGame: the basics of any game, basically state management. Do not modify
class BaseGame:
    def __init__(self, session):
        self.session = session
        self.client = None
        self.game_objects = {}
        self.players = []
        self.current_players = []

        self._got_initial_state = False
        self._game_object_classes = {}


    def __contains__(self, key):
        return hasattr(self, key)

    def __getitem__(self, key):
        return getattr(self, key)

    def set_client(self, client):
        self.client = client

    def set_ai(self, ai):
        self.ai = ai

    def connected(self, data):
        self._server_constants = EasyDict(data['constants'])
        self.session = str(data["gameSession"])
        self.name = str(data['gameName'])


    def get_game_object(self, id):
        id = str(id)
        if id in self.game_objects:
            return self.game_objects[id]

    def apply_delta_state(self, delta):
        not_got_initial_state = not self._got_initial_state
        self._got_initial_state = True

        if 'gameObjects' in delta:
            self._init_game_objects(delta['gameObjects'])

        self._merge_delta(self, delta)

        if not_got_initial_state:
            self.ai.connect_player()
            self.ai.game_initialized()

        self.ai.game_updated()


    def _init_game_objects(self, game_objects):
        for id, obj in game_objects.items():
            id = str(id)
            if not id in self.game_objects: # then we need to create it
                obj['game'] = self
                obj['ai'] = self.ai
                obj['client'] = self.client
                self.game_objects[id] = self._game_object_classes[obj['gameObjectName']](obj)


    def _merge_delta(self, state, delta):
        delta_length = -1
        if self._server_constants.DELTA_ARRAY_LENGTH in delta:
            delta_length = delta[self._server_constants.DELTA_ARRAY_LENGTH]
            del delta[self._server_constants.DELTA_ARRAY_LENGTH] # we don't want to copy this key/value over to the state, it was just to signify it is an array

        if delta_length > -1: # then this part in the state is an array
            while len(state) > delta_length: # remove elements off the array to make it's size correct.
                state.pop()
            while len(state) < delta_length: # append elements on the array to make it's size correct.
                state.append(None)

        for key in delta: # deltas will always be objects when iterating through, arrays just have keys of numbers
            d = delta[key]
            state_key = key # array's keys are real numbers, not strings e.g. "1"
            key_in_state = False

            if isinstance(state, list):
                state_key = int(key)
                key_in_state = state_key < len(state)
            else:
                state_key = camel_case_converter(state_key)
                key_in_state = state_key in state

            value = d
            if d == self._server_constants.DELTA_REMOVED:
                value = None
                if key_in_state:
                    del state[state_key]
            elif isinstance(d, dict) and len(d) == 1 and 'id' in d: # then this is a shallow reference to a game object
                value = self.get_game_object(d['id'])
            elif (isinstance(d, dict) or isinstance(d, list)) and key_in_state and (isinstance(state[state_key], dict) or isinstance(state[state_key], list) or isinstance(state[state_key], BaseGameObject)):
                value = None
                self._merge_delta(state[state_key], d)

            if value != None:
                if isinstance(state_key, int) or isinstance(state, dict):
                    state[state_key] = value
                else:
                    setattr(state, state_key, value)
