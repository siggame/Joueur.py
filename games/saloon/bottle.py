# This is a simple class to represent the Bottle object in the game. You can extend it by adding utility functions here in this file.

from games.saloon.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add addtional import(s) here
# <<-- /Creer-Merge: imports -->>

class Bottle(GameObject):
    """The class representing the Bottle in the Saloon game.

    A bottle thrown by a bartender at a Tile.
    """

    def __init__(self):
        """Initializes a Bottle with basic logic as provided by the Creer code generator."""
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._drunk_direction = ""
        self._is_destroyed = False
        self._location = None
        self._next_location = None



    @property
    def drunk_direction(self):
        """The direction any Cowboys hit by this will move, can be 'North', 'East', 'South', or 'West'.

        :rtype: str
        """
        return self._drunk_direction


    @property
    def is_destroyed(self):
        """True if this Bottle has impacted and has been destroyed (removed from the Game). False if still in the game flying through the saloon.

        :rtype: bool
        """
        return self._is_destroyed


    @property
    def location(self):
        """The Tile this bottle is currently flying over.

        :rtype: Tile
        """
        return self._location


    @property
    def next_location(self):
        """The Tile this Bottle will fly to next turn, if it does not impact anything on its path between the two.

        :rtype: Tile
        """
        return self._next_location



    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
