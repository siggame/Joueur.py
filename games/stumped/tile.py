# Tile: A Tile in the game that makes up the 2D map grid.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from typing import List, Optional
from games.stumped.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Tile(GameObject):
    """The class representing the Tile in the Stumped game.

    A Tile in the game that makes up the 2D map grid.
    """

    def __init__(self):
        """Initializes a Tile with basic logic as provided by the Creer code generator.
        """
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._beaver = None
        self._branches = 0
        self._flow_direction = ""
        self._food = 0
        self._lodge_owner = None
        self._spawner = None
        self._tile_east = None
        self._tile_north = None
        self._tile_south = None
        self._tile_west = None
        self._type = ""
        self._x = 0
        self._y = 0

    @property
    def beaver(self) -> Optional['games.stumped.beaver.Beaver']:
        """The Beaver on this Tile if present, otherwise None.

        :rtype: games.stumped.beaver.Beaver or None
        """
        return self._beaver

    @property
    def branches(self) -> int:
        """The number of branches dropped on this Tile.

        :rtype: int
        """
        return self._branches

    @property
    def flow_direction(self) -> str:
        """The cardinal direction water is flowing on this Tile ('North', 'East', 'South', 'West').

        :rtype: 'North', 'East', 'South', 'West', or ''
        """
        return self._flow_direction

    @property
    def food(self) -> int:
        """The number of food dropped on this Tile.

        :rtype: int
        """
        return self._food

    @property
    def lodge_owner(self) -> Optional['games.stumped.player.Player']:
        """The owner of the Beaver lodge on this Tile, if present, otherwise None.

        :rtype: games.stumped.player.Player or None
        """
        return self._lodge_owner

    @property
    def spawner(self) -> Optional['games.stumped.spawner.Spawner']:
        """The resource Spawner on this Tile if present, otherwise None.

        :rtype: games.stumped.spawner.Spawner or None
        """
        return self._spawner

    @property
    def tile_east(self) -> Optional['games.stumped.tile.Tile']:
        """The Tile to the 'East' of this one (x+1, y). None if out of bounds of the map.

        :rtype: games.stumped.tile.Tile or None
        """
        return self._tile_east

    @property
    def tile_north(self) -> Optional['games.stumped.tile.Tile']:
        """The Tile to the 'North' of this one (x, y-1). None if out of bounds of the map.

        :rtype: games.stumped.tile.Tile or None
        """
        return self._tile_north

    @property
    def tile_south(self) -> Optional['games.stumped.tile.Tile']:
        """The Tile to the 'South' of this one (x, y+1). None if out of bounds of the map.

        :rtype: games.stumped.tile.Tile or None
        """
        return self._tile_south

    @property
    def tile_west(self) -> Optional['games.stumped.tile.Tile']:
        """The Tile to the 'West' of this one (x-1, y). None if out of bounds of the map.

        :rtype: games.stumped.tile.Tile or None
        """
        return self._tile_west

    @property
    def type(self) -> str:
        """What type of Tile this is, either 'water' or 'land'.

        :rtype: 'land' or 'water'
        """
        return self._type

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

    directions = ["North", "East", "South", "West"]
    """int: The valid directions that tiles can be in, "North", "East", "South", or "West"
    """

    def get_neighbors(self) -> List['games.stumped.tile.Tile']:
        """Gets the neighbors of this Tile

        Returns:
            list[games.stumped.tile.Tile]: The list of neighboring Tiles of this Tile.
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

    def has_neighbor(self, tile: 'games.stumped.tile.Tile') -> bool:
        """Checks if this Tile has a specific neighboring Tile.

        Args:
            tile (games.stumped.tile.Tile): The Tile to check against.

        Returns:
            bool: True if the tile is a neighbor of this Tile, False otherwise
        """
        return bool(tile and tile in self.get_neighbors())

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
