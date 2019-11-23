# Game: Two player grid based game where each player tries to burn down the other player's buildings. Let it burn.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from typing import Dict, List, Optional
from joueur.base_game import BaseGame

# import game objects
from games.anarchy.building import Building
from games.anarchy.fire_department import FireDepartment
from games.anarchy.forecast import Forecast
from games.anarchy.game_object import GameObject
from games.anarchy.player import Player
from games.anarchy.police_department import PoliceDepartment
from games.anarchy.warehouse import Warehouse
from games.anarchy.weather_station import WeatherStation

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Game(BaseGame):
    """The class representing the Game in the Anarchy game.

    Two player grid based game where each player tries to burn down the other player's buildings. Let it burn.
    """

    def __init__(self):
        """Initializes a Game with basic logic as provided by the Creer code generator.
        """
        BaseGame.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._base_bribes_per_turn = 0
        self._buildings = []
        self._current_forecast = None
        self._current_player = None
        self._current_turn = 0
        self._forecasts = []
        self._game_objects = {}
        self._map_height = 0
        self._map_width = 0
        self._max_fire = 0
        self._max_forecast_intensity = 0
        self._max_turns = 100
        self._next_forecast = None
        self._players = []
        self._session = ""
        self._time_added_per_turn = 0

        self.name = "Anarchy"

        self._game_object_classes = {
            'Building': Building,
            'FireDepartment': FireDepartment,
            'Forecast': Forecast,
            'GameObject': GameObject,
            'Player': Player,
            'PoliceDepartment': PoliceDepartment,
            'Warehouse': Warehouse,
            'WeatherStation': WeatherStation
        }

    @property
    def base_bribes_per_turn(self) -> int:
        """How many bribes players get at the beginning of their turn, not counting their burned down Buildings.

        :rtype: int
        """
        return self._base_bribes_per_turn

    @property
    def buildings(self) -> List['games.anarchy.building.Building']:
        """All the buildings in the game.

        :rtype: list[games.anarchy.building.Building]
        """
        return self._buildings

    @property
    def current_forecast(self) -> 'games.anarchy.forecast.Forecast':
        """The current Forecast, which will be applied at the end of the turn.

        :rtype: games.anarchy.forecast.Forecast
        """
        return self._current_forecast

    @property
    def current_player(self) -> 'games.anarchy.player.Player':
        """The player whose turn it is currently. That player can send commands. Other players cannot.

        :rtype: games.anarchy.player.Player
        """
        return self._current_player

    @property
    def current_turn(self) -> int:
        """The current turn number, starting at 0 for the first player's turn.

        :rtype: int
        """
        return self._current_turn

    @property
    def forecasts(self) -> List['games.anarchy.forecast.Forecast']:
        """All the forecasts in the game, indexed by turn number.

        :rtype: list[games.anarchy.forecast.Forecast]
        """
        return self._forecasts

    @property
    def game_objects(self) -> Dict[str, 'games.anarchy.game_object.GameObject']:
        """A mapping of every game object's ID to the actual game object. Primarily used by the server and client to easily refer to the game objects via ID.

        :rtype: dict[str, games.anarchy.game_object.GameObject]
        """
        return self._game_objects

    @property
    def map_height(self) -> int:
        """The width of the entire map along the vertical (y) axis.

        :rtype: int
        """
        return self._map_height

    @property
    def map_width(self) -> int:
        """The width of the entire map along the horizontal (x) axis.

        :rtype: int
        """
        return self._map_width

    @property
    def max_fire(self) -> int:
        """The maximum amount of fire value for any Building.

        :rtype: int
        """
        return self._max_fire

    @property
    def max_forecast_intensity(self) -> int:
        """The maximum amount of intensity value for any Forecast.

        :rtype: int
        """
        return self._max_forecast_intensity

    @property
    def max_turns(self) -> int:
        """The maximum number of turns before the game will automatically end.

        :rtype: int
        """
        return self._max_turns

    @property
    def next_forecast(self) -> Optional['games.anarchy.forecast.Forecast']:
        """The next Forecast, which will be applied at the end of your opponent's turn. This is also the Forecast WeatherStations can control this turn.

        :rtype: games.anarchy.forecast.Forecast or None
        """
        return self._next_forecast

    @property
    def players(self) -> List['games.anarchy.player.Player']:
        """List of all the players in the game.

        :rtype: list[games.anarchy.player.Player]
        """
        return self._players

    @property
    def session(self) -> str:
        """A unique identifier for the game instance that is being played.

        :rtype: str
        """
        return self._session

    @property
    def time_added_per_turn(self) -> int:
        """The amount of time (in nano-seconds) added after each player performs a turn.

        :rtype: int
        """
        return self._time_added_per_turn

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
