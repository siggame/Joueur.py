# This is where you build your AI for the Stardash game.

from joueur.base_ai import BaseAI

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>


class AI(BaseAI):
    """ The AI you add and improve code inside to play Stardash. """

    @property
    def game(self):
        """The reference to the Game instance this AI is playing.

        :rtype: games.stardash.game.Game
        """
        return self._game  # don't directly touch this "private" variable pls

    @property
    def player(self):
        """The reference to the Player this AI controls in the Game.

        :rtype: games.stardash.player.Player
        """
        return self._player  # don't directly touch this "private" variable pls

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

        # Gets the coordinates of your home base (planet).
        home_x = self.player.home_base.x
        home_y = self.player.home_base.y

        # Checks if we have any units.
        if len(self.player.units) == 0:
            # If we don't have any units, spawn a miner.
            self.player.home_base.spawn(home_x, home_y, "miner")
        elif self.player.units[0].energy < 0.5 * self.player.units[0].job.energy:
            # If the miner is below 50% energy, goes back to its home base to heal.
            unit = self.player.units[0]

            while unit.moves > 0:
                if unit.y >= self.game.bodies[2].y:
                    unit.move(unit.x, unit.y + 1)
                else:
                    unit.move(unit.x, unit.y - 1)
            if unit.dash():
                break
        elif self.player.units[0].genarium < self.player.units[0].job.carry_limit:
            # If there is space in our inventory, go mine an asteroid for genarium (the worst mineral btw).
        else:
            # Otherwise return to home base and drop off any mined genarium and restoring energy in the process.
            self.player.units[0].dash

        return True
        # <<-- /Creer-Merge: runTurn -->>

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you need additional functions for your AI you can add them here
    # <<-- /Creer-Merge: functions -->>
