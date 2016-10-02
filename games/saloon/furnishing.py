# This is a simple class to represent the Furnishing object in the game. You can extend it by adding utility functions here in this file.

from games.saloon.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add addtional import(s) here
# <<-- /Creer-Merge: imports -->>

class Furnishing(GameObject):
    """The class representing the Furnishing in the Saloon game.

    An furnishing in the Saloon that must be pathed around, or destroyed.
    """

    def __init__(self):
        """Initializes a Furnishing with basic logic as provided by the Creer code generator."""
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._health = 0
        self._is_destroyed = False
        self._is_piano = False
        self._tile = None



    @property
    def health(self):
        """How much health this Furnishing currently has.

        :rtype: int
        """
        return self._health


    @property
    def is_destroyed(self):
        """If this Furnishing has been destroyed, and has been removed from the game.

        :rtype: bool
        """
        return self._is_destroyed


    @property
    def is_piano(self):
        """True if this Furnishing is a piano and can be played, False otherwise.

        :rtype: bool
        """
        return self._is_piano


    @property
    def tile(self):
        """The Tile that this Furnishing is located on.

        :rtype: Tile
        """
        return self._tile



    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
