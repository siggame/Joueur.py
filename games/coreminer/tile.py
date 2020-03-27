# Tile: A Tile in the game that makes up the 2D map grid.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from games.coreminer.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Tile(GameObject):
    """The class representing the Tile in the Coreminer game.

    A Tile in the game that makes up the 2D map grid.
    """

    def __init__(self):
        """Initializes a Tile with basic logic as provided by the Creer code generator."""
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._dirt = 0
        self._is_base = False
        self._is_falling = False
        self._is_hopper = False
        self._is_ladder = False
        self._is_support = False
        self._ore = 0
        self._owner = None
        self._shielding = 0
        self._tile_east = None
        self._tile_north = None
        self._tile_south = None
        self._tile_west = None
        self._units = []
        self._x = 0
        self._y = 0

    @property
    def dirt(self):
        """The amount of dirt on this Tile.

        :rtype: int
        """
        return self._dirt

    @property
    def is_base(self):
        """Whether or not the tile is an indestructible base Tile.

        :rtype: bool
        """
        return self._is_base

    @property
    def is_falling(self):
        """Whether or not this tile is about to fall.

        :rtype: bool
        """
        return self._is_falling

    @property
    def is_hopper(self):
        """Whether or not a hopper is on this Tile.

        :rtype: bool
        """
        return self._is_hopper

    @property
    def is_ladder(self):
        """Whether or not a ladder is built on this Tile.

        :rtype: bool
        """
        return self._is_ladder

    @property
    def is_support(self):
        """Whether or not a support is built on this Tile.

        :rtype: bool
        """
        return self._is_support

    @property
    def ore(self):
        """The amount of ore on this Tile.

        :rtype: int
        """
        return self._ore

    @property
    def owner(self):
        """The owner of this Tile, or undefined if owned by no-one. Only for bases and hoppers.

        :rtype: games.coreminer.player.Player
        """
        return self._owner

    @property
    def shielding(self):
        """The amount of shielding on this Tile.

        :rtype: int
        """
        return self._shielding

    @property
    def tile_east(self):
        """The Tile to the 'East' of this one (x+1, y). None if out of bounds of the map.

        :rtype: games.coreminer.tile.Tile
        """
        return self._tile_east

    @property
    def tile_north(self):
        """The Tile to the 'North' of this one (x, y-1). None if out of bounds of the map.

        :rtype: games.coreminer.tile.Tile
        """
        return self._tile_north

    @property
    def tile_south(self):
        """The Tile to the 'South' of this one (x, y+1). None if out of bounds of the map.

        :rtype: games.coreminer.tile.Tile
        """
        return self._tile_south

    @property
    def tile_west(self):
        """The Tile to the 'West' of this one (x-1, y). None if out of bounds of the map.

        :rtype: games.coreminer.tile.Tile
        """
        return self._tile_west

    @property
    def units(self):
        """An array of the Units on this Tile.

        :rtype: list[games.coreminer.unit.Unit]
        """
        return self._units

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

    def spawn_miner(self):
        """ Spawns a Miner Unit on this Tile - Must be on the surface on their side of the map.

        Returns:
            bool: True if successfully spawned, False otherwise.
        """
        return self._run_on_server('spawnMiner')


    directions = ["North", "East", "South", "West"]
    """int: The valid directions that tiles can be in, "North", "East", "South", or "West"
    """

    def get_neighbors(self):
        """Gets the neighbors of this Tile

        :rtype list[games.coreminer.tile.Tile]
        """
        neighbors = []

        for direction in Tile.directions:
            neighbor = getattr(self, "tile_" + direction.lower())
            if neighbor:
                neighbors.append(neighbor)

        return neighbors

    def is_pathable(self):
        """Checks if a Tile is pathable to units

        Returns:
            bool: True if pathable, False otherwise
        """
        # <<-- Creer-Merge: is_pathable_builtin -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        return false  # DEVELOPER ADD LOGIC HERE
        # <<-- /Creer-Merge: is_pathable_builtin -->>

    def has_neighbor(self, tile):
        """Checks if this Tile has a specific neighboring Tile
        Args:
            tile (games.coreminer.tile.Tile): tile to check against
        Returns:
            bool: True if the tile is a neighbor of this Tile, False otherwise
        """
        return bool(tile and tile in self.get_neighbors())

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
