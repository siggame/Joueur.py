# This is a simple class to represent the Tile object in the game. You can extend it by adding utility functions here in this file.

from games.saloon.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add addtional import(s) here
# <<-- /Creer-Merge: imports -->>

class Tile(GameObject):
    """The class representing the Tile in the Saloon game.

    A Tile in the game that makes up the 2D map grid.
    """

    def __init__(self):
        """Initializes a Tile with basic logic as provided by the Creer code generator."""
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._bottles = []
        self._cowboy = None
        self._furnishing = None
        self._has_hazard = False
        self._is_wall = False
        self._tile_above = None
        self._tile_below = None
        self._tile_left = None
        self._tile_right = None
        self._x = 0
        self._y = 0



    @property
    def bottles(self):
        """All the beer Bottles currently flying over this Tile.

        :rtype: list[Bottle]
        """
        return self._bottles


    @property
    def cowboy(self):
        """The Cowboy that is on this Tile, or null if empty.

        :rtype: Cowboy
        """
        return self._cowboy


    @property
    def furnishing(self):
        """The furnishing that is on this Tile, or null if empty.

        :rtype: Furnishing
        """
        return self._furnishing


    @property
    def has_hazard(self):
        """If this Tile is pathable, but has a hazard that damages Cowboys that path through it.

        :rtype: bool
        """
        return self._has_hazard


    @property
    def is_wall(self):
        """If this Tile is a wall of the Saloon, and can never be pathed through.

        :rtype: bool
        """
        return self._is_wall


    @property
    def tile_above(self):
        """The Tile above this one (x, y-1). Null if out of bounds of the map.

        :rtype: Tile
        """
        return self._tile_above


    @property
    def tile_below(self):
        """The Tile below this one (x, y+1). Null if out of bounds of the map.

        :rtype: Tile
        """
        return self._tile_below


    @property
    def tile_left(self):
        """The Tile to the left of this one (x-1, y). Null if out of bounds of the map.

        :rtype: Tile
        """
        return self._tile_left


    @property
    def tile_right(self):
        """The Tile to the right of this one (x+1, y). Null if out of bounds of the map.

        :rtype: Tile
        """
        return self._tile_right


    @property
    def x(self):
        """The x (horizontal) position of this Tile.

        :rtype: int
        """
        return self._x


    @property
    def y(self):
        """The y (vertical) position of this Tile.

        :rtype: int
        """
        return self._y



    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
