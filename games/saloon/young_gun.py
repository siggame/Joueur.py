# YoungGun: An eager young person that wants to join your gang, and will call in the veteran Cowboys you need to win the brawl in the saloon.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from games.saloon.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add addtional import(s) here
# <<-- /Creer-Merge: imports -->>

class YoungGun(GameObject):
    """The class representing the YoungGun in the Saloon game.

    An eager young person that wants to join your gang, and will call in the veteran Cowboys you need to win the brawl in the saloon.
    """

    def __init__(self):
        """Initializes a YoungGun with basic logic as provided by the Creer code generator."""
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._can_call_in = False
        self._owner = None
        self._tile = None



    @property
    def can_call_in(self):
        """True if the YoungGun can call in a Cowboy, False otherwise.

        :rtype: bool
        """
        return self._can_call_in


    @property
    def owner(self):
        """The Player that owns and can control this YoungGun.

        :rtype: Player
        """
        return self._owner


    @property
    def tile(self):
        """The Tile this YoungGun is currently on. Cowboys they send in will be on the nearest non-balcony Tile.

        :rtype: Tile
        """
        return self._tile



    def call_in(self, job):
        """ Tells the YoungGun to call in a new Cowbow of the given job to the open Tile nearest to them.

        Args:
            job (str): The job you want the Cowboy being brought to have.

        Returns:
            Cowboy: The new Cowboy that was called in if valid. They will not be added to any `cowboys` lists until the turn ends. None otherwise.
        """
        return self._run_on_server('callIn', job=job)


    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
