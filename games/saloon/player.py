# This is a simple class to represent the Player object in the game. You can extend it by adding utility functions here in this file.

from games.saloon.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add addtional import(s) here
# <<-- /Creer-Merge: imports -->>

class Player(GameObject):
    """The class representing the Player in the Saloon game.

    A player in this game. Every AI controls one player.
    """

    def __init__(self):
        """Initializes a Player with basic logic as provided by the Creer code generator."""
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._client_type = ""
        self._cowboys = []
        self._kills = 0
        self._lost = False
        self._name = "Anonymous"
        self._opponent = None
        self._reason_lost = ""
        self._reason_won = ""
        self._rowdyness = 0
        self._score = 0
        self._siesta = 0
        self._time_remaining = 0
        self._won = False
        self._young_gun = None



    @property
    def client_type(self):
        """What type of client this is, e.g. 'Python', 'JavaScript', or some other language. For potential data mining purposes.

        :rtype: str
        """
        return self._client_type


    @property
    def cowboys(self):
        """Every Cowboy owned by this Player.

        :rtype: list[Cowboy]
        """
        return self._cowboys


    @property
    def kills(self):
        """How many enemy Cowboys this player's team has killed.

        :rtype: int
        """
        return self._kills


    @property
    def lost(self):
        """If the player lost the game or not.

        :rtype: bool
        """
        return self._lost


    @property
    def name(self):
        """The name of the player.

        :rtype: str
        """
        return self._name


    @property
    def opponent(self):
        """This player's opponent in the game.

        :rtype: Player
        """
        return self._opponent


    @property
    def reason_lost(self):
        """The reason why the player lost the game.

        :rtype: str
        """
        return self._reason_lost


    @property
    def reason_won(self):
        """The reason why the player won the game.

        :rtype: str
        """
        return self._reason_won


    @property
    def rowdyness(self):
        """How rowdy their team is. When it gets too high their team takes a collective siesta.

        :rtype: int
        """
        return self._rowdyness


    @property
    def score(self):
        """How many times their team has played a piano.

        :rtype: int
        """
        return self._score


    @property
    def siesta(self):
        """0 when not having a team siesta. When greater than 0 represents how many turns left for the team siesta to complete.

        :rtype: int
        """
        return self._siesta


    @property
    def time_remaining(self):
        """The amount of time (in ns) remaining for this AI to send commands.

        :rtype: float
        """
        return self._time_remaining


    @property
    def won(self):
        """If the player won the game or not.

        :rtype: bool
        """
        return self._won


    @property
    def young_gun(self):
        """The only 'Yong Gun' Cowboy this player owns, or null if they called in their young gun during their turn.

        :rtype: Cowboy
        """
        return self._young_gun



    def send_in(self, job):
        """ Sends in the Young Gun to the nearest Tile into the Saloon, and promotes them to a new job.

        Args:
            job (str): The job you want the Young Gun being brought in to be called in to do, changing their job to it.

        Returns:
            Cowboy: The Cowboy that was previously a 'Young Gun', and has now been promoted to a different job if successful, null otherwise.
        """
        return self._run_on_server('sendIn', job=job)


    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
