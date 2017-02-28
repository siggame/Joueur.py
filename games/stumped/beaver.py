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
        self._distracted = 0
        self._fish = 0
        self._health = 0
        self._job = None
        self._moves = 0
        self._owner = None
        self._tile = None

    @property
    def actions(self):
        """The number of actions remaining for the beaver this turn.

        :rtype: int
        """
        return self._actions

    @property
    def branches(self):
        """The number of branches this beaver is holding.

        :rtype: int
        """
        return self._branches

    @property
    def distracted(self):
        """Number of turns this beaver is distracted for (0 means not distracted).

        :rtype: int
        """
        return self._distracted

    @property
    def fish(self):
        """The number of fish this beaver is holding.

        :rtype: int
        """
        return self._fish

    @property
    def health(self):
        """How much health this beaver has left.

        :rtype: int
        """
        return self._health

    @property
    def job(self):
        """The Job this beaver was recruited to do.

        :rtype: Job
        """
        return self._job

    @property
    def moves(self):
        """How many moves this beaver has left this turn.

        :rtype: int
        """
        return self._moves

    @property
    def owner(self):
        """The Player that owns and can control this beaver.

        :rtype: Player
        """
        return self._owner

    @property
    def tile(self):
        """The tile this beaver is on.

        :rtype: Tile
        """
        return self._tile

    def attack(self, tile):
        """ Attacks another adjacent beaver.

        Args:
            tile (Tile): The tile of the beaver you want to attack.

        Returns:
            bool: True if successfully attacked, False otherwise.
        """
        return self._run_on_server('attack', tile=tile)

    def build_lodge(self):
        """ Builds a lodge on the Beavers current tile.

        Returns:
            bool: True if successfully built a lodge, False otherwise.
        """
        return self._run_on_server('buildLodge')

    def drop(self, resource, amount=0):
        """ Drops some of the given resource on the beaver's tile. Fish dropped in water disappear instantly, and fish dropped on land die one per tile per turn.

        Args:
            resource (str): The type of resource to drop ('branch' or 'fish').
            amount (Optional[int]): The amount of the resource to drop, numbers <= 0 will drop all of that type.

        Returns:
            bool: True if successfully dropped the resource, False otherwise.
        """
        return self._run_on_server('drop', resource=resource, amount=amount)

    def harvest(self, tile):
        """ Harvests the branches or fish from a Spawner on an adjacent tile.

        Args:
            tile (Tile): The tile you want to harvest.

        Returns:
            bool: True if successfully harvested, False otherwise.
        """
        return self._run_on_server('harvest', tile=tile)

    def move(self, tile):
        """ Moves this beaver from its current tile to an adjacent tile.

        Args:
            tile (Tile): The tile this beaver should move to. Costs 2 moves normally, 3 if moving upstream, and 1 if moving downstream.

        Returns:
            bool: True if the move worked, False otherwise.
        """
        return self._run_on_server('move', tile=tile)

    def pickup(self, resource, amount=0):
        """ Picks up some branches or fish on the beaver's tile.

        Args:
            resource (str): The type of resource to pickup ('branch' or 'fish').
            amount (Optional[int]): The amount of the resource to drop, numbers <= 0 will pickup all of that type.

        Returns:
            bool: True if successfully picked up a resource, False otherwise.
        """
        return self._run_on_server('pickup', resource=resource, amount=amount)

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
