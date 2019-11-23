# Tile: A Tile in the game that makes up the 2D map grid.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from typing import List, Optional
from games.catastrophe.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Tile(GameObject):
    """The class representing the Tile in the Catastrophe game.

    A Tile in the game that makes up the 2D map grid.
    """

    def __init__(self):
        """Initializes a Tile with basic logic as provided by the Creer code generator.
        """
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._food = 0
        self._harvest_rate = 0
        self._materials = 0
        self._structure = None
        self._tile_east = None
        self._tile_north = None
        self._tile_south = None
        self._tile_west = None
        self._turns_to_harvest = 0
        self._unit = None
        self._x = 0
        self._y = 0

    @property
    def food(self) -> int:
        """int: The number of food dropped on this Tile.
        """
        return self._food

    @property
    def harvest_rate(self) -> int:
        """int: The amount of food that can be harvested from this Tile per turn.
        """
        return self._harvest_rate

    @property
    def materials(self) -> int:
        """int: The number of materials dropped on this Tile.
        """
        return self._materials

    @property
    def structure(self) -> Optional['games.catastrophe.structure.Structure']:
        """games.catastrophe.structure.Structure or None: The Structure on this Tile if present, otherwise None.
        """
        return self._structure

    @property
    def tile_east(self) -> Optional['games.catastrophe.tile.Tile']:
        """games.catastrophe.tile.Tile or None: The Tile to the 'East' of this one (x+1, y). None if out of bounds of the map.
        """
        return self._tile_east

    @property
    def tile_north(self) -> Optional['games.catastrophe.tile.Tile']:
        """games.catastrophe.tile.Tile or None: The Tile to the 'North' of this one (x, y-1). None if out of bounds of the map.
        """
        return self._tile_north

    @property
    def tile_south(self) -> Optional['games.catastrophe.tile.Tile']:
        """games.catastrophe.tile.Tile or None: The Tile to the 'South' of this one (x, y+1). None if out of bounds of the map.
        """
        return self._tile_south

    @property
    def tile_west(self) -> Optional['games.catastrophe.tile.Tile']:
        """games.catastrophe.tile.Tile or None: The Tile to the 'West' of this one (x-1, y). None if out of bounds of the map.
        """
        return self._tile_west

    @property
    def turns_to_harvest(self) -> int:
        """int: The amount of turns before this resource can be harvested.
        """
        return self._turns_to_harvest

    @property
    def unit(self) -> Optional['games.catastrophe.unit.Unit']:
        """games.catastrophe.unit.Unit or None: The Unit on this Tile if present, otherwise None.
        """
        return self._unit

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

    def get_neighbors(self) -> List['games.catastrophe.tile.Tile']:
        """Gets the neighbors of this Tile

        Returns:
            list[games.catastrophe.tile.Tile]: The list of neighboring Tiles of this Tile.
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

    def has_neighbor(self, tile: 'games.catastrophe.tile.Tile') -> bool:
        """Checks if this Tile has a specific neighboring Tile.

        Args:
            tile (games.catastrophe.tile.Tile): The Tile to check against.

        Returns:
            bool: True if the tile is a neighbor of this Tile, False otherwise
        """
        return bool(tile and tile in self.get_neighbors())

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
