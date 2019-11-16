# Tower: A tower in the game. Used to combat enemy waves.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from games.necrowar.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Tower(GameObject):
    """The class representing the Tower in the Necrowar game.

    A tower in the game. Used to combat enemy waves.
    """

    def __init__(self):
        """Initializes a Tower with basic logic as provided by the Creer code generator."""
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._attacked = False
        self._cooldown = 0
        self._health = 0
        self._job = None
        self._owner = None
        self._tile = None

    @property
    def attacked(self):
        """Whether this tower has attacked this turn or not.

        :rtype: bool
        """
        return self._attacked

    @property
    def cooldown(self):
        """How many turns are left before it can fire again.

        :rtype: int
        """
        return self._cooldown

    @property
    def health(self):
        """How much remaining health this tower has.

        :rtype: int
        """
        return self._health

    @property
    def job(self):
        """What type of tower this is (it's job).

        :rtype: games.necrowar.tower_job.TowerJob
        """
        return self._job

    @property
    def owner(self):
        """The player that built / owns this tower.

        :rtype: games.necrowar.player.Player
        """
        return self._owner

    @property
    def tile(self):
        """The Tile this Tower is on.

        :rtype: games.necrowar.tile.Tile
        """
        return self._tile

    def attack(self, tile):
        """ Attacks an enemy unit on an tile within it's range.

        Args:
            tile (games.necrowar.tile.Tile): The Tile to attack.

        Returns:
            bool: True if successfully attacked, False otherwise.
        """
        return self._run_on_server('attack', tile=tile)



    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
