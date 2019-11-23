# Game: There's an infestation of enemy spiders challenging your queen broodmother spider! Protect her and attack the other broodmother in this turn based, node based, game.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from typing import Dict, List
from joueur.base_game import BaseGame

# import game objects
from games.spiders.brood_mother import BroodMother
from games.spiders.cutter import Cutter
from games.spiders.game_object import GameObject
from games.spiders.nest import Nest
from games.spiders.player import Player
from games.spiders.spider import Spider
from games.spiders.spiderling import Spiderling
from games.spiders.spitter import Spitter
from games.spiders.weaver import Weaver
from games.spiders.web import Web

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Game(BaseGame):
    """The class representing the Game in the Spiders game.

    There's an infestation of enemy spiders challenging your queen broodmother spider! Protect her and attack the other broodmother in this turn based, node based, game.
    """

    def __init__(self):
        """Initializes a Game with basic logic as provided by the Creer code generator.
        """
        BaseGame.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._current_player = None
        self._current_turn = 0
        self._cut_speed = 0
        self._eggs_scalar = 0
        self._game_objects = {}
        self._initial_web_strength = 0
        self._max_turns = 100
        self._max_web_strength = 0
        self._movement_speed = 0
        self._nests = []
        self._players = []
        self._session = ""
        self._spit_speed = 0
        self._time_added_per_turn = 0
        self._weave_power = 0
        self._weave_speed = 0
        self._webs = []

        self.name = "Spiders"

        self._game_object_classes = {
            'BroodMother': BroodMother,
            'Cutter': Cutter,
            'GameObject': GameObject,
            'Nest': Nest,
            'Player': Player,
            'Spider': Spider,
            'Spiderling': Spiderling,
            'Spitter': Spitter,
            'Weaver': Weaver,
            'Web': Web
        }

    @property
    def current_player(self) -> 'games.spiders.player.Player':
        """The player whose turn it is currently. That player can send commands. Other players cannot.

        :rtype: games.spiders.player.Player
        """
        return self._current_player

    @property
    def current_turn(self) -> int:
        """The current turn number, starting at 0 for the first player's turn.

        :rtype: int
        """
        return self._current_turn

    @property
    def cut_speed(self) -> int:
        """The speed at which Cutters work to do cut Webs.

        :rtype: int
        """
        return self._cut_speed

    @property
    def eggs_scalar(self) -> float:
        """Constant used to calculate how many eggs BroodMothers get on their owner's turns.

        :rtype: float
        """
        return self._eggs_scalar

    @property
    def game_objects(self) -> Dict[str, 'games.spiders.game_object.GameObject']:
        """A mapping of every game object's ID to the actual game object. Primarily used by the server and client to easily refer to the game objects via ID.

        :rtype: dict[str, games.spiders.game_object.GameObject]
        """
        return self._game_objects

    @property
    def initial_web_strength(self) -> int:
        """The starting strength for Webs.

        :rtype: int
        """
        return self._initial_web_strength

    @property
    def max_turns(self) -> int:
        """The maximum number of turns before the game will automatically end.

        :rtype: int
        """
        return self._max_turns

    @property
    def max_web_strength(self) -> int:
        """The maximum strength a web can be strengthened to.

        :rtype: int
        """
        return self._max_web_strength

    @property
    def movement_speed(self) -> int:
        """The speed at which Spiderlings move on Webs.

        :rtype: int
        """
        return self._movement_speed

    @property
    def nests(self) -> List['games.spiders.nest.Nest']:
        """Every Nest in the game.

        :rtype: list[games.spiders.nest.Nest]
        """
        return self._nests

    @property
    def players(self) -> List['games.spiders.player.Player']:
        """List of all the players in the game.

        :rtype: list[games.spiders.player.Player]
        """
        return self._players

    @property
    def session(self) -> str:
        """A unique identifier for the game instance that is being played.

        :rtype: str
        """
        return self._session

    @property
    def spit_speed(self) -> int:
        """The speed at which Spitters work to spit new Webs.

        :rtype: int
        """
        return self._spit_speed

    @property
    def time_added_per_turn(self) -> int:
        """The amount of time (in nano-seconds) added after each player performs a turn.

        :rtype: int
        """
        return self._time_added_per_turn

    @property
    def weave_power(self) -> int:
        """How much web strength is added or removed from Webs when they are weaved.

        :rtype: int
        """
        return self._weave_power

    @property
    def weave_speed(self) -> int:
        """The speed at which Weavers work to do strengthens and weakens on Webs.

        :rtype: int
        """
        return self._weave_speed

    @property
    def webs(self) -> List['games.spiders.web.Web']:
        """Every Web in the game.

        :rtype: list[games.spiders.web.Web]
        """
        return self._webs

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
