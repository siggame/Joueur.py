# Nest: A location (node) connected to other Nests via Webs (edges) in the game that Spiders can converge on, regardless of owner.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from typing import List, Optional
from games.spiders.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Nest(GameObject):
    """The class representing the Nest in the Spiders game.

    A location (node) connected to other Nests via Webs (edges) in the game that Spiders can converge on, regardless of owner.
    """

    def __init__(self):
        """Initializes a Nest with basic logic as provided by the Creer code generator.
        """
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._controlling_player = None
        self._spiders = []
        self._webs = []
        self._x = 0
        self._y = 0

    @property
    def controlling_player(self) -> Optional['games.spiders.player.Player']:
        """games.spiders.player.Player or None: The Player that 'controls' this Nest as they have the most Spiders on this nest.
        """
        return self._controlling_player

    @property
    def spiders(self) -> List['games.spiders.spider.Spider']:
        """list[games.spiders.spider.Spider]: All the Spiders currently located on this Nest.
        """
        return self._spiders

    @property
    def webs(self) -> List['games.spiders.web.Web']:
        """list[games.spiders.web.Web]: Webs that connect to this Nest.
        """
        return self._webs

    @property
    def x(self) -> int:
        """int: The X coordinate of the Nest. Used for distance calculations.
        """
        return self._x

    @property
    def y(self) -> int:
        """int: The Y coordinate of the Nest. Used for distance calculations.
        """
        return self._y

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
