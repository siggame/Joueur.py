# This is where you build your AI for the Saloon game.

from joueur.base_ai import BaseAI



class AI(BaseAI):
    """ The basic AI functions that are the same between games. """


    def get_name(self):
        """ This is the name you send to the server so your AI will control the player named this string.

        Returns
            str: The name of your Player.
        """
        return "Saloon Python Player" # REPLACE THIS WITH YOUR TEAM NAME



    def start(self):
        """ This is called once the game starts and your AI knows its playerID and game. You can initialize your AI here.
        """
        # replace with your start logic



    def game_updated(self):
        """ This is called every time the game's state updates, so if you are tracking anything you can update it here.
        """
        # replace with your game updated logic



    def end(self, won, reason):
        """ This is called when the game ends, you can clean up your data and dump files here if need be.

        Args:
            won (bool): True means you won, False means you lost.
            reason (str): The human readable string explaining why you won or lost.
        """
        # replace with your end logic


    def run_turn(self):
        """ This is called every time it is this AI.player's turn.

        Returns:
            bool: Represents if you want to end your turn. True means end your turn, False means to keep your turn going and re-call this function.
        """
        # Put your game logic here for runTurn
        return True
