# Checker: A checker on the game board.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from games.checkers.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Checker(GameObject):
    """The class representing the Checker in the Checkers game.

    A checker on the game board.
    """

    def __init__(self):
        """Initializes a Checker with basic logic as provided by the Creer code generator."""
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._kinged = False
        self._owner = None
        self._x = 0
        self._y = 0

    @property
    def kinged(self):
        """If the checker has been kinged and can move backwards.

        :rtype: bool
        """
        return self._kinged

    @property
    def owner(self):
        """The player that controls this Checker.

        :rtype: games.checkers.player.Player
        """
        return self._owner

    @property
    def x(self):
        """The x coordinate of the checker.

        :rtype: int
        """
        return self._x

    @property
    def y(self):
        """The y coordinate of the checker.

        :rtype: int
        """
        return self._y

    def is_mine(self):
        """ Returns if the checker is owned by your player or not.

        Returns:
            bool: True if it is yours, False if it is not yours.
        """
        return self._run_on_server('isMine')

    def move(self, x, y):
        """ Moves the checker from its current location to the given (x, y).

        Args:
            x (int): The x coordinate to move to.
            y (int): The y coordinate to move to.

        Returns:
            games.checkers.checker.Checker: Returns the same checker that moved if the move was successful. None otherwise.
        """
        return self._run_on_server('move', x=x, y=y)

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
