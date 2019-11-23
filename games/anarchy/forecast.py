# Forecast: The weather effect that will be applied at the end of a turn, which causes fires to spread.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from games.anarchy.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Forecast(GameObject):
    """The class representing the Forecast in the Anarchy game.

    The weather effect that will be applied at the end of a turn, which causes fires to spread.
    """

    def __init__(self):
        """Initializes a Forecast with basic logic as provided by the Creer code generator.
        """
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._controlling_player = None
        self._direction = ""
        self._intensity = 0

    @property
    def controlling_player(self) -> 'games.anarchy.player.Player':
        """The Player that can use WeatherStations to control this Forecast when its the nextForecast.

        :rtype: games.anarchy.player.Player
        """
        return self._controlling_player

    @property
    def direction(self) -> str:
        """The direction the wind will blow fires in. Can be 'north', 'east', 'south', or 'west'.

        :rtype: 'North', 'East', 'South', or West
        """
        return self._direction

    @property
    def intensity(self) -> int:
        """How much of a Building's fire that can be blown in the direction of this Forecast. Fire is duplicated (copied), not moved (transfered).

        :rtype: int
        """
        return self._intensity

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
