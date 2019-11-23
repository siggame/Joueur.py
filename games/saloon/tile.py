# Tile: A Tile in the game that makes up the 2D map grid.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from typing import List, Optional
from games.saloon.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Tile(GameObject):
    """The class representing the Tile in the Saloon game.

    A Tile in the game that makes up the 2D map grid.
    """

    def __init__(self):
        """Initializes a Tile with basic logic as provided by the Creer code generator.
        """
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._bottle = None
        self._cowboy = None
        self._furnishing = None
        self._has_hazard = False
        self._is_balcony = False
        self._tile_east = None
        self._tile_north = None
        self._tile_south = None
        self._tile_west = None
        self._x = 0
        self._y = 0
        self._young_gun = None

    @property
    def bottle(self) -> Optional['games.saloon.bottle.Bottle']:
        """The beer Bottle currently flying over this Tile, None otherwise.

        :rtype: games.saloon.bottle.Bottle or None
        """
        return self._bottle

    @property
    def cowboy(self) -> Optional['games.saloon.cowboy.Cowboy']:
        """The Cowboy that is on this Tile, None otherwise.

        :rtype: games.saloon.cowboy.Cowboy or None
        """
        return self._cowboy

    @property
    def furnishing(self) -> Optional['games.saloon.furnishing.Furnishing']:
        """The furnishing that is on this Tile, None otherwise.

        :rtype: games.saloon.furnishing.Furnishing or None
        """
        return self._furnishing

    @property
    def has_hazard(self) -> bool:
        """If this Tile is pathable, but has a hazard that damages Cowboys that path through it.

        :rtype: bool
        """
        return self._has_hazard

    @property
    def is_balcony(self) -> bool:
        """If this Tile is a balcony of the Saloon that YoungGuns walk around on, and can never be pathed through by Cowboys.

        :rtype: bool
        """
        return self._is_balcony

    @property
    def tile_east(self) -> Optional['games.saloon.tile.Tile']:
        """The Tile to the 'East' of this one (x+1, y). None if out of bounds of the map.

        :rtype: games.saloon.tile.Tile or None
        """
        return self._tile_east

    @property
    def tile_north(self) -> Optional['games.saloon.tile.Tile']:
        """The Tile to the 'North' of this one (x, y-1). None if out of bounds of the map.

        :rtype: games.saloon.tile.Tile or None
        """
        return self._tile_north

    @property
    def tile_south(self) -> Optional['games.saloon.tile.Tile']:
        """The Tile to the 'South' of this one (x, y+1). None if out of bounds of the map.

        :rtype: games.saloon.tile.Tile or None
        """
        return self._tile_south

    @property
    def tile_west(self) -> Optional['games.saloon.tile.Tile']:
        """The Tile to the 'West' of this one (x-1, y). None if out of bounds of the map.

        :rtype: games.saloon.tile.Tile or None
        """
        return self._tile_west

    @property
    def x(self) -> int:
        """The x (horizontal) position of this Tile.

        :rtype: int
        """
        return self._x

    @property
    def y(self) -> int:
        """The y (vertical) position of this Tile.

        :rtype: int
        """
        return self._y

    @property
    def young_gun(self) -> Optional['games.saloon.young_gun.YoungGun']:
        """The YoungGun on this tile, None otherwise.

        :rtype: games.saloon.young_gun.YoungGun or None
        """
        return self._young_gun

    directions = ["North", "East", "South", "West"]
    """int: The valid directions that tiles can be in, "North", "East", "South", or "West"
    """

    def get_neighbors(self) -> List['games.saloon.tile.Tile']:
        """Gets the neighbors of this Tile

        Returns:
            list[games.saloon.tile.Tile]: The list of neighboring Tiles of this Tile.
        """
        neighbors = []

        for direction in Tile.directions:
            neighbor = getattr(self, "tile_" + direction.lower())
            if neighbor:
                neighbors.append(neighbor)

        return neighbors

    def is_pathable(self) -> bool:
        """Checks if a Tile is pathable to units

        Returns:
            bool: True if pathable, False otherwise.
        """
        # <<-- Creer-Merge: is_pathable_builtin -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        return False # DEVELOPER ADD LOGIC HERE
        # <<-- /Creer-Merge: is_pathable_builtin -->>

    def has_neighbor(self, tile: 'games.saloon.tile.Tile') -> bool:
        """Checks if this Tile has a specific neighboring Tile.

        Args:
            tile (games.saloon.tile.Tile): The Tile to check against.

        Returns:
            bool: True if the tile is a neighbor of this Tile, False otherwise
        """
        return bool(tile and tile in self.get_neighbors())

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
