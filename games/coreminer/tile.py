# Tile: A Tile in the game that makes up the 2D map grid.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from typing import List, Optional
from games.coreminer.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Tile(GameObject):
    """The class representing the Tile in the Coreminer game.

    A Tile in the game that makes up the 2D map grid.
    """

    def __init__(self):
        """Initializes a Tile with basic logic as provided by the Creer code generator.
        """
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._bombs = []
        self._dirt = 0
        self._is_base = False
        self._is_falling = False
        self._is_hopper = False
        self._is_ladder = False
        self._is_support = False
        self._miners = []
        self._ore = 0
        self._owner = None
        self._shielding = 0
        self._tile_east = None
        self._tile_north = None
        self._tile_south = None
        self._tile_west = None
        self._x = 0
        self._y = 0

    @property
    def bombs(self) -> List['games.coreminer.bomb.Bomb']:
        """list[games.coreminer.bomb.Bomb]: An array of Bombs on this Tile.
        """
        return self._bombs

    @property
    def dirt(self) -> int:
        """int: The amount of dirt on this Tile.
        """
        return self._dirt

    @property
    def is_base(self) -> bool:
        """bool: Whether or not the Tile is a base Tile.
        """
        return self._is_base

    @property
    def is_falling(self) -> bool:
        """bool: Whether or not this Tile is about to fall after this turn.
        """
        return self._is_falling

    @property
    def is_hopper(self) -> bool:
        """bool: Whether or not a hopper is on this Tile.
        """
        return self._is_hopper

    @property
    def is_ladder(self) -> bool:
        """bool: Whether or not a ladder is built on this Tile.
        """
        return self._is_ladder

    @property
    def is_support(self) -> bool:
        """bool: Whether or not a support is built on this Tile.
        """
        return self._is_support

    @property
    def miners(self) -> List['games.coreminer.miner.Miner']:
        """list[games.coreminer.miner.Miner]: An array of the Miners on this Tile.
        """
        return self._miners

    @property
    def ore(self) -> int:
        """int: The amount of ore on this Tile.
        """
        return self._ore

    @property
    def owner(self) -> Optional['games.coreminer.player.Player']:
        """games.coreminer.player.Player or None: The owner of this Tile, or undefined if owned by no-one.
        """
        return self._owner

    @property
    def shielding(self) -> int:
        """int: The amount of shielding on this Tile.
        """
        return self._shielding

    @property
    def tile_east(self) -> Optional['games.coreminer.tile.Tile']:
        """games.coreminer.tile.Tile or None: The Tile to the 'East' of this one (x+1, y). None if out of bounds of the map.
        """
        return self._tile_east

    @property
    def tile_north(self) -> Optional['games.coreminer.tile.Tile']:
        """games.coreminer.tile.Tile or None: The Tile to the 'North' of this one (x, y-1). None if out of bounds of the map.
        """
        return self._tile_north

    @property
    def tile_south(self) -> Optional['games.coreminer.tile.Tile']:
        """games.coreminer.tile.Tile or None: The Tile to the 'South' of this one (x, y+1). None if out of bounds of the map.
        """
        return self._tile_south

    @property
    def tile_west(self) -> Optional['games.coreminer.tile.Tile']:
        """games.coreminer.tile.Tile or None: The Tile to the 'West' of this one (x-1, y). None if out of bounds of the map.
        """
        return self._tile_west

    @property
    def x(self) -> int:
        """int: The x (horizontal) position of this Tile.
        """
        return self._x

    @property
    def y(self) -> int:
        """int: The y (vertical) position of this Tile.
        """
        return self._y

    directions = ["North", "East", "South", "West"]
    """int: The valid directions that tiles can be in, "North", "East", "South", or "West"
    """

    def get_neighbors(self) -> List['games.coreminer.tile.Tile']:
        """Gets the neighbors of this Tile

        Returns:
            list[games.coreminer.tile.Tile]: The list of neighboring Tiles of this Tile.
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
        return false  # DEVELOPER ADD LOGIC HERE
        # <<-- /Creer-Merge: is_pathable_builtin -->>

    def has_neighbor(self, tile: 'games.coreminer.tile.Tile') -> bool:
        """Checks if this Tile has a specific neighboring Tile.

        Args:
            tile (games.coreminer.tile.Tile): The Tile to check against.

        Returns:
            bool: True if the tile is a neighbor of this Tile, False otherwise
        """
        return bool(tile and tile in self.get_neighbors())

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
