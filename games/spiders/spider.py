# Spider: A Spider in the game. The most basic unit.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from games.spiders.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Spider(GameObject):
    """The class representing the Spider in the Spiders game.

    A Spider in the game. The most basic unit.
    """

    def __init__(self):
        """Initializes a Spider with basic logic as provided by the Creer code generator."""
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._is_dead = False
        self._nest = None
        self._owner = None



    @property
    def is_dead(self):
        """If this Spider is dead and has been removed from the game.

        :rtype: bool
        """
        return self._is_dead


    @property
    def nest(self):
        """The Nest that this Spider is currently on. None when moving on a Web.

        :rtype: Nest
        """
        return self._nest


    @property
    def owner(self):
        """The Player that owns this Spider, and can command it.

        :rtype: Player
        """
        return self._owner



    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
