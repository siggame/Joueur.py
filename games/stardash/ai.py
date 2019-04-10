# This is where you build your AI for the Stardash game.

from joueur.base_ai import BaseAI

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
import math
# <<-- /Creer-Merge: imports -->>

class AI(BaseAI):
    """ The AI you add and improve code inside to play Stardash. """

    @property
    def game(self):
        """The reference to the Game instance this AI is playing.

        :rtype: games.stardash.game.Game
        """
        return self._game # don't directly touch this "private" variable pls

    @property
    def player(self):
        """The reference to the Player this AI controls in the Game.

        :rtype: games.stardash.player.Player
        """
        return self._player # don't directly touch this "private" variable pls

    def get_name(self):
        """ This is the name you send to the server so your AI will control the
            player named this string.

        Returns
            str: The name of your Player.
        """
        # <<-- Creer-Merge: get-name -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        return "Stardash Python Player"  # REPLACE THIS WITH YOUR TEAM NAME
        # <<-- /Creer-Merge: get-name -->>

    def start(self):
        """ This is called once the game starts and your AI knows its player and
            game. You can initialize your AI here.
        """
        # <<-- Creer-Merge: start -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        # replace with your start logic
        # <<-- /Creer-Merge: start -->>

    def game_updated(self):
        """ This is called every time the game's state updates, so if you are
        tracking anything you can update it here.
        """
        # <<-- Creer-Merge: game-updated -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        # replace with your game updated logic
        # <<-- /Creer-Merge: game-updated -->>

    def end(self, won, reason):
        """ This is called when the game ends, you can clean up your data and
            dump files here if need be.

        Args:
            won (bool): True means you won, False means you lost.
            reason (str): The human readable string explaining why your AI won
            or lost.
        """
        # <<-- Creer-Merge: end -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        # replace with your end logic
        # <<-- /Creer-Merge: end -->>
    def run_turn(self):
        """ This is called every time it is this AI.player's turn.

        Returns:
            bool: Represents if you want to end your turn. True means end your turn, False means to keep your turn going and re-call this function.
        """
        # <<-- Creer-Merge: runTurn -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
        # Put your game logic here for runTurn

        # Note that this code is not efficient whatsoever, you should make improvements to almost every aspect of it.
        # This code is only to demonstrate the use of some of the game's functions.
        # For more information about these and other game mechanics, refer to the documentation here: TODO: ADD LINK
        # Feel free to look at all the functions in the other files in this directory, but do not edit anything other than this file.

        # Gets the coordinates of your home base (planet).
        home_x = self.player.home_base.x
        home_y = self.player.home_base.y

        # Checks if we have any units.
        if len(self.player.units) == 0:
            # If we don't have any units, spawn a miner.
            self.player.home_base.spawn(home_x, home_y, "miner")

        # Gets the first unit in our list of units.
        unit = self.player.units[0]

        if unit.energy < 0.5 * unit.job.energy:
            # If the miner is below 50% energy, goes back to its home base to heal.
            self.find_dash(unit, home_x, home_y)
        elif unit.genarium < unit.job.carry_limit:
            # If there is space in our inventory, go mine an asteroid for genarium (the worst mineral btw).
            target = None
            best_dist = 9999

            # Finds the closest asteroid that contains genarium to target.
            for body in self.game.bodies:
                # Only looks at asteroids that contain genarium.
                if body.material_type == "genarium":
                    # Gets the distance from the unit to the body
                    distance = self.distance(unit.x, unit.y, body.x, body.y)

                    # Updates the target if the new asteroid is closer to our unit.
                    if distance < best_dist:
                        target = body
                        best_dist = distance

            if target is not None:
                # Tries to move to the asteroid.
                self.find_dash(unit, target.x, target.y)

                # Checks if the miner is within mining range of the target asteroid.
                if self.distance(unit.x, unit.y, target.x, target.y) < unit.job.range:
                    unit.mine(target)
        else:
            # Otherwise return to home base and drop off any mined genarium and restoring energy in the process.
            self.find_dash(unit, home_x, home_y)

        return True
        # <<-- /Creer-Merge: runTurn -->>

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you need additional functions for your AI you can add them here
    def distance(self, x1, y1, x2, y2):
        """ Returns the Euclidian distance between two points.

            Args:
                x1 (int): The x coordinate of the first point.
                y1 (int): The y coordinate of the first point.
                x2 (int): The x coordinate of the second point.
                y2 (int): The y coordinate of the second point.

            Returns:
                float: The distance between the two points.
        """
        return math.sqrt((x1 - x2) ** 2.0 + (y1 - y2) ** 2.0)

    def find_dash(self, unit, x, y):
        """ This is an EXTREMELY basic pathfinding function to move your ship until it can dash to your target.
            You REALLY should improve this functionality or make your own new one, since this is VERY basic and inefficient.
            Like, for real.

            Args:
                unit (unit): The unit that will be moving.
                x (int): The x coordinate of the destination.
                y (int): The y coordinate of the destination.
        """
        # Gets the sun from the list of bodies.
        sun = self.game.bodies[2]

        while unit.moves > 0:
            if unit.safe(x, y) and unit.energy >= math.ceil((self.distance(unit.x, unit.y, x, y) / self.game.dash_distance) * self.game.dash_cost):
                # Dashes if it is safe to dash to the point and we have enough energy to dash there.
                unit.dash(x, y)

                # Breaks out of the loop since we can't do anything else now.
                break
            else:
                # Otherwise tries moving towards the target.

                # The x and y modifiers for movement.
                x_mod = 0
                y_mod = 0

                if unit.x < x or (y < sun.y and unit.y > sun.y or y > sun.y and unit.y < sun.y) and x > sun.x:
                        # Move to the right if the destination is to the right or on the other side of the sun on the right side.
                    x_mod = 1
                elif unit.x > x or (y < sun.y and unit.y > sun.y or y > sun.y and unit.y < sun.y) and x < sun.x:
                    # Move to the left if the destination is to the left or on the other side of the sun on the left side.
                    x_mod = -1

                if unit.y < y or (x < sun.x and unit.x > sun.x or x > sun.x and unit.x < sun.x) and y > sun.y:
                    # Move down if the destination is down or on the other side of the sun on the lower side.
                    y_mod = 1
                elif unit.y > y or (x < sun.x and unit.x > sun.x or x > sun.x and unit.x < sun.x) and y < sun.y:
                    # Move up if the destination is up or on the other side of the sun on the upper side.
                    y_mod = -1

                if x_mod != 0 and y_mod != 0 and not unit.safe(unit.x + x_mod, unit.y + y_mod):
                    # Special case if we cannot safely move diagonally.
                    if unit.safe(unit.x + x_mod, unit.y):
                            # Only move horizontally if it is safe.
                        y_mod = 0
                    elif unit.safe(unit.x, unit.y + y_mod):
                        # Only move vertically if it is safe.
                        x_mod = 0

                if unit.moves == 1 and x_mod != 0 and y_mod != 0:
                    # Special case if we only have 1 move left and are trying to move 2.
                    if unit.safe(unit.x + x_mod, unit.y):
                        y_mod = 0
                    elif unit.safe(unit.x, unit.y + y_mod):
                        x_mod = 0
                    else:
                        break

                if (x_mod != 0 or y_mod != 0) and (math.sqrt(math.pow(x_mod, 2) + math.pow(y_mod, 2)) >= unit.moves):
                    # Tries to move if either of the modifiers is not zero (we are actually moving somewhere).
                    unit.move(unit.x + x_mod, unit.y + y_mod)
                else:
                    # Breaks otherwise, since something probably went wrong.
                    break

    # <<-- /Creer-Merge: functions -->>
