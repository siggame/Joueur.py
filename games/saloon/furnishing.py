# Furnishing: An furnishing in the Saloon that must be pathed around, or destroyed.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from games.saloon.game_object import GameObject



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
        self._is_playing = False
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
    def is_playing(self):
        """If this is a piano and a Cowboy is playing it this turn.

        :rtype: bool
        """
        return self._is_playing


    @property
    def tile(self):
        """The Tile that this Furnishing is located on.

        :rtype: Tile
        """
        return self._tile
