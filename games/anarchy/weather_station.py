# WeatherStation: Can be bribed to change the next Forecast in some way.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from games.anarchy.building import Building

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class WeatherStation(Building):
    """The class representing the WeatherStation in the Anarchy game.

    Can be bribed to change the next Forecast in some way.
    """

    def __init__(self):
        """Initializes a WeatherStation with basic logic as provided by the Creer code generator.
        """
        Building.__init__(self)

        # private attributes to hold the properties so they appear read only

    def intensify(self, negative: bool = False) -> bool:
        """Bribe the weathermen to intensity the next Forecast by 1 or -1.

        Args:
            negative (bool): By default the intensity will be increased by 1, setting this to True decreases the intensity by 1.

        Returns:
            bool: True if the intensity was changed, False otherwise.
        """
        return self._run_on_server('intensify', {
            'negative': negative
        })

    def rotate(self, counterclockwise: bool = False) -> bool:
        """Bribe the weathermen to change the direction of the next Forecast by rotating it clockwise or counterclockwise.

        Args:
            counterclockwise (bool): By default the direction will be rotated clockwise. If you set this to True we will rotate the forecast counterclockwise instead.

        Returns:
            bool: True if the rotation worked, False otherwise.
        """
        return self._run_on_server('rotate', {
            'counterclockwise': counterclockwise
        })

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
