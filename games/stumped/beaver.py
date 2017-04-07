# Beaver: A beaver in the game.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from games.stumped.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Beaver(GameObject):
    """The class representing the Beaver in the Stumped game.

    A beaver in the game.
    """

    def __init__(self):
        """Initializes a Beaver with basic logic as provided by the Creer code generator."""
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._actions = 0
        self._branches = 0
        self._food = 0
        self._health = 0
        self._job = None
        self._moves = 0
        self._owner = None
        self._recruited = False
        self._tile = None
        self._turns_distracted = 0

    @property
    def actions(self):
        """The number of actions remaining for the Beaver this turn.

        :rtype: int
        """
        return self._actions

    @property
    def branches(self):
        """The amount of branches this Beaver is holding.

        :rtype: int
        """
        return self._branches

    @property
    def food(self):
        """The amount of food this Beaver is holding.

        :rtype: int
        """
        return self._food

    @property
    def health(self):
        """How much health this Beaver has left.

        :rtype: int
        """
        return self._health

    @property
    def job(self):
        """The Job this Beaver was recruited to do.

        :rtype: Job
        """
        return self._job

    @property
    def moves(self):
        """How many moves this Beaver has left this turn.

        :rtype: int
        """
        return self._moves

    @property
    def owner(self):
        """The Player that owns and can control this Beaver.

        :rtype: Player
        """
        return self._owner

    @property
    def recruited(self):
        """True if the Beaver has finished being recruited and can do things, False otherwise.

        :rtype: bool
        """
        return self._recruited

    @property
    def tile(self):
        """The Tile this Beaver is on.

        :rtype: Tile
        """
        return self._tile

    @property
    def turns_distracted(self):
        """Number of turns this Beaver is distracted for (0 means not distracted).

        :rtype: int
        """
        return self._turns_distracted

    def attack(self, beaver):
        """ Attacks another adjacent beaver.

        Args:
            beaver (Beaver): The Beaver to attack. Must be on an adjacent Tile.

        Returns:
            bool: True if successfully attacked, False otherwise.
        """
        return self._run_on_server('attack', beaver=beaver)

    def build_lodge(self):
        """ Builds a lodge on the Beavers current Tile.

        Returns:
            bool: True if successfully built a lodge, False otherwise.
        """
        return self._run_on_server('buildLodge')

    def drop(self, tile, resource, amount=0):
        """ Drops some of the given resource on the beaver's Tile.

        Args:
            tile (Tile): The Tile to drop branches/food on. Must be the same Tile that the Beaver is on, or an adjacent one.
            resource (str): The type of resource to drop ('branch' or 'food').
            amount (Optional[int]): The amount of the resource to drop, numbers <= 0 will drop all the resource type.

        Returns:
            bool: True if successfully dropped the resource, False otherwise.
        """
        return self._run_on_server('drop', tile=tile, resource=resource, amount=amount)

    def harvest(self, spawner):
        """ Harvests the branches or food from a Spawner on an adjacent Tile.

        Args:
            spawner (Spawner): The Spawner you want to harvest. Must be on an adjacent Tile.

        Returns:
            bool: True if successfully harvested, False otherwise.
        """
        return self._run_on_server('harvest', spawner=spawner)

    def move(self, tile):
        """ Moves this Beaver from its current Tile to an adjacent Tile.

        Args:
            tile (Tile): The Tile this Beaver should move to.

        Returns:
            bool: True if the move worked, False otherwise.
        """
        return self._run_on_server('move', tile=tile)

    def pickup(self, tile, resource, amount=0):
        """ Picks up some branches or food on the beaver's tile.

        Args:
            tile (Tile): The Tile to pickup branches/food from. Must be the same Tile that the Beaver is on, or an adjacent one.
            resource (str): The type of resource to pickup ('branch' or 'food').
            amount (Optional[int]): The amount of the resource to drop, numbers <= 0 will pickup all of the resource type.

        Returns:
            bool: True if successfully picked up a resource, False otherwise.
        """
        return self._run_on_server('pickup', tile=tile, resource=resource, amount=amount)

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
