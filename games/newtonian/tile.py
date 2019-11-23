# Tile: A Tile in the game that makes up the 2D map grid.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from typing import List, Optional
from games.newtonian.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Tile(GameObject):
    """The class representing the Tile in the Newtonian game.

    A Tile in the game that makes up the 2D map grid.
    """

    def __init__(self):
        """Initializes a Tile with basic logic as provided by the Creer code generator.
        """
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._blueium = 0
        self._blueium_ore = 0
        self._decoration = 0
        self._direction = ""
        self._is_wall = False
        self._machine = None
        self._owner = None
        self._redium = 0
        self._redium_ore = 0
        self._tile_east = None
        self._tile_north = None
        self._tile_south = None
        self._tile_west = None
        self._type = ""
        self._unit = None
        self._x = 0
        self._y = 0

    @property
    def blueium(self) -> int:
        """int: The amount of blueium on this tile.
        """
        return self._blueium

    @property
    def blueium_ore(self) -> int:
        """int: The amount of blueium ore on this tile.
        """
        return self._blueium_ore

    @property
    def decoration(self) -> int:
        """int: (Visualizer only) Different tile types, cracked, slightly dirty, etc. This has no effect on gameplay, but feel free to use it if you want.
        """
        return self._decoration

    @property
    def direction(self) -> str:
        """'blank', 'north', 'east', 'south', or 'west': The direction of a conveyor belt ('blank', 'north', 'east', 'south', or 'west'). blank means conveyor doesn't move.
        """
        return self._direction

    @property
    def is_wall(self) -> bool:
        """bool: Whether or not the tile is a wall.
        """
        return self._is_wall

    @property
    def machine(self) -> Optional['games.newtonian.machine.Machine']:
        """games.newtonian.machine.Machine or None: The Machine on this Tile if present, otherwise None.
        """
        return self._machine

    @property
    def owner(self) -> Optional['games.newtonian.player.Player']:
        """games.newtonian.player.Player or None: The owner of this Tile, or None if owned by no-one. Only for generators and spawn areas.
        """
        return self._owner

    @property
    def redium(self) -> int:
        """int: The amount of redium on this tile.
        """
        return self._redium

    @property
    def redium_ore(self) -> int:
        """int: The amount of redium ore on this tile.
        """
        return self._redium_ore

    @property
    def tile_east(self) -> Optional['games.newtonian.tile.Tile']:
        """games.newtonian.tile.Tile or None: The Tile to the 'East' of this one (x+1, y). None if out of bounds of the map.
        """
        return self._tile_east

    @property
    def tile_north(self) -> Optional['games.newtonian.tile.Tile']:
        """games.newtonian.tile.Tile or None: The Tile to the 'North' of this one (x, y-1). None if out of bounds of the map.
        """
        return self._tile_north

    @property
    def tile_south(self) -> Optional['games.newtonian.tile.Tile']:
        """games.newtonian.tile.Tile or None: The Tile to the 'South' of this one (x, y+1). None if out of bounds of the map.
        """
        return self._tile_south

    @property
    def tile_west(self) -> Optional['games.newtonian.tile.Tile']:
        """games.newtonian.tile.Tile or None: The Tile to the 'West' of this one (x-1, y). None if out of bounds of the map.
        """
        return self._tile_west

    @property
    def type(self) -> str:
        """'normal', 'generator', 'conveyor', or 'spawn': The type of Tile this is ('normal', 'generator', 'conveyor', or 'spawn').
        """
        return self._type

    @property
    def unit(self) -> Optional['games.newtonian.unit.Unit']:
        """games.newtonian.unit.Unit or None: The Unit on this Tile if present, otherwise None.
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

    def get_neighbors(self) -> List['games.newtonian.tile.Tile']:
        """Gets the neighbors of this Tile

        Returns:
            list[games.newtonian.tile.Tile]: The list of neighboring Tiles of this Tile.
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

    def has_neighbor(self, tile: 'games.newtonian.tile.Tile') -> bool:
        """Checks if this Tile has a specific neighboring Tile.

        Args:
            tile (games.newtonian.tile.Tile): The Tile to check against.

        Returns:
            bool: True if the tile is a neighbor of this Tile, False otherwise
        """
        return bool(tile and tile in self.get_neighbors())

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
