# Tile: A Tile in the game that makes up the 2D map grid.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from games.necrowar.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Tile(GameObject):
    """The class representing the Tile in the Necrowar game.

    A Tile in the game that makes up the 2D map grid.
    """

    def __init__(self):
        """Initializes a Tile with basic logic as provided by the Creer code generator."""
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._corpses = 0
        self._is_castle = False
        self._is_gold_mine = False
        self._is_grass = False
        self._is_island_gold_mine = False
        self._is_path = False
        self._is_river = False
        self._is_tower = False
        self._is_unit_spawn = False
        self._is_wall = False
        self._is_worker_spawn = False
        self._num_ghouls = 0
        self._num_hounds = 0
        self._num_zombies = 0
        self._tile_east = None
        self._tile_north = None
        self._tile_south = None
        self._tile_west = None
        self._tower = None
        self._type = ""
        self._unit = None
        self._x = 0
        self._y = 0

    @property
    def corpses(self):
        """The amount of corpses on this tile.

        :rtype: int
        """
        return self._corpses

    @property
    def is_castle(self):
        """Whether or not the tile is a castle tile.

        :rtype: bool
        """
        return self._is_castle

    @property
    def is_gold_mine(self):
        """Whether or not the tile is considered to be a gold mine or not.

        :rtype: bool
        """
        return self._is_gold_mine

    @property
    def is_grass(self):
        """Whether or not the tile is considered grass or not (Workers can walk on grass).

        :rtype: bool
        """
        return self._is_grass

    @property
    def is_island_gold_mine(self):
        """Whether or not the tile is considered to be the island gold mine or not.

        :rtype: bool
        """
        return self._is_island_gold_mine

    @property
    def is_path(self):
        """Whether or not the tile is considered a path or not (Units can walk on paths).

        :rtype: bool
        """
        return self._is_path

    @property
    def is_river(self):
        """Whether or not the tile is considered a river or not.

        :rtype: bool
        """
        return self._is_river

    @property
    def is_tower(self):
        """Whether or not the tile is considered a tower or not.

        :rtype: bool
        """
        return self._is_tower

    @property
    def is_unit_spawn(self):
        """Whether or not the tile is the unit spawn.

        :rtype: bool
        """
        return self._is_unit_spawn

    @property
    def is_wall(self):
        """Whether or not the tile can be moved on by workers.

        :rtype: bool
        """
        return self._is_wall

    @property
    def is_worker_spawn(self):
        """Whether or not the tile is the worker spawn.

        :rtype: bool
        """
        return self._is_worker_spawn

    @property
    def num_ghouls(self):
        """The amount of Ghouls on this tile.

        :rtype: int
        """
        return self._num_ghouls

    @property
    def num_hounds(self):
        """The amount of Hounds on this tile.

        :rtype: int
        """
        return self._num_hounds

    @property
    def num_zombies(self):
        """The amount of Zombies on this tile.

        :rtype: int
        """
        return self._num_zombies

    @property
    def tile_east(self):
        """The Tile to the 'East' of this one (x+1, y). None if out of bounds of the map.

        :rtype: games.necrowar.tile.Tile
        """
        return self._tile_east

    @property
    def tile_north(self):
        """The Tile to the 'North' of this one (x, y-1). None if out of bounds of the map.

        :rtype: games.necrowar.tile.Tile
        """
        return self._tile_north

    @property
    def tile_south(self):
        """The Tile to the 'South' of this one (x, y+1). None if out of bounds of the map.

        :rtype: games.necrowar.tile.Tile
        """
        return self._tile_south

    @property
    def tile_west(self):
        """The Tile to the 'West' of this one (x-1, y). None if out of bounds of the map.

        :rtype: games.necrowar.tile.Tile
        """
        return self._tile_west

    @property
    def tower(self):
        """The Tower on this Tile if present, otherwise None.

        :rtype: games.necrowar.tower.Tower
        """
        return self._tower

    @property
    def type(self):
        """The type of Tile this is ('normal', 'path', 'river', or 'spawn').

        :rtype: str
        """
        return self._type

    @property
    def unit(self):
        """The Unit on this Tile if present, otherwise None.

        :rtype: games.necrowar.unit.Unit
        """
        return self._unit

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

    def res(self, num):
        """ Resurrect the corpses on this tile into Zombies.

        Args:
            num (int): Number of zombies to resurrect.

        Returns:
            bool: True if successful res, False otherwise.
        """
        return self._run_on_server('res', num=num)

    def spawn_unit(self, title):
        """ Spawns a fighting unit on the correct tile.

        Args:
            title (str): The title of the desired unit type.

        Returns:
            bool: True if successfully spawned, False otherwise.
        """
        return self._run_on_server('spawnUnit', title=title)

    def spawn_worker(self):
        """ Spawns a worker on the correct tile.

        Returns:
            bool: True if successfully spawned, False otherwise.
        """
        return self._run_on_server('spawnWorker')


    directions = ["North", "East", "South", "West"]
    """int: The valid directions that tiles can be in, "North", "East", "South", or "West"
    """

    def get_neighbors(self):
        """Gets the neighbors of this Tile

        :rtype list[games.necrowar.tile.Tile]
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
            tile (games.necrowar.tile.Tile): tile to check against
        Returns:
            bool: True if the tile is a neighbor of this Tile, False otherwise
        """
        return bool(tile and tile in self.get_neighbors())

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
