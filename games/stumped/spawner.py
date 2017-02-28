# Spawner: A resource spawner that generates branches or fish.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from games.stumped.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Spawner(GameObject):
    """The class representing the Spawner in the Stumped game.

    A resource spawner that generates branches or fish.
    """

    def __init__(self):
        """Initializes a Spawner with basic logic as provided by the Creer code generator."""
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._health = 0
        self._tile = None
        self._type = ""

    @property
    def health(self):
        """How much of the resource is left.

        :rtype: int
        """
        return self._health

    @property
    def tile(self):
        """The tile this resource is on.

        :rtype: Tile
        """
        return self._tile

    @property
    def type(self):
        """What type of resource this is ('Fish' or 'Branch').

        :rtype: str
        """
        return self._type

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
