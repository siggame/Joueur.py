# Player: A player in this game. Every AI controls one player.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from games.anarchy.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Player(GameObject):
    """The class representing the Player in the Anarchy game.

    A player in this game. Every AI controls one player.
    """

    def __init__(self):
        """Initializes a Player with basic logic as provided by the Creer code generator."""
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._bribes_remaining = 0
        self._buildings = []
        self._client_type = ""
        self._fire_departments = []
        self._headquarters = None
        self._lost = False
        self._name = "Anonymous"
        self._opponent = None
        self._police_departments = []
        self._reason_lost = ""
        self._reason_won = ""
        self._time_remaining = 0
        self._warehouses = []
        self._weather_stations = []
        self._won = False

    @property
    def bribes_remaining(self):
        """How many bribes this player has remaining to use during their turn. Each action a Building does costs 1 bribe. Any unused bribes are lost at the end of the player's turn.

        :rtype: int
        """
        return self._bribes_remaining

    @property
    def buildings(self):
        """All the buildings owned by this player.

        :rtype: list[games.anarchy.building.Building]
        """
        return self._buildings

    @property
    def client_type(self):
        """What type of client this is, e.g. 'Python', 'JavaScript', or some other language. For potential data mining purposes.

        :rtype: str
        """
        return self._client_type

    @property
    def fire_departments(self):
        """All the FireDepartments owned by this player.

        :rtype: list[games.anarchy.fire_department.FireDepartment]
        """
        return self._fire_departments

    @property
    def headquarters(self):
        """The Warehouse that serves as this player's headquarters and has extra health. If this gets destroyed they lose.

        :rtype: games.anarchy.warehouse.Warehouse
        """
        return self._headquarters

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

        :rtype: games.anarchy.player.Player
        """
        return self._opponent

    @property
    def police_departments(self):
        """All the PoliceDepartments owned by this player.

        :rtype: list[games.anarchy.police_department.PoliceDepartment]
        """
        return self._police_departments

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
    def time_remaining(self):
        """The amount of time (in ns) remaining for this AI to send commands.

        :rtype: float
        """
        return self._time_remaining

    @property
    def warehouses(self):
        """All the warehouses owned by this player. Includes the Headquarters.

        :rtype: list[games.anarchy.warehouse.Warehouse]
        """
        return self._warehouses

    @property
    def weather_stations(self):
        """All the WeatherStations owned by this player.

        :rtype: list[games.anarchy.weather_station.WeatherStation]
        """
        return self._weather_stations

    @property
    def won(self):
        """If the player won the game or not.

        :rtype: bool
        """
        return self._won

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
