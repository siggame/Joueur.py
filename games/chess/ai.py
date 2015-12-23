# This is where you build your AI for the Chess game.

from joueur.base_ai import BaseAI
import random

class AI(BaseAI):
    """ the basic AI functions that are the same between games
    """


    def get_name(self):
        """ this is the name you send to the server to play as.

        Returns
            str: the name you want your player to have
        """

        return "Chess Python Player" # REPLACE THIS WITH YOUR TEAM NAME



    def start(self):
        """ this is called once the game starts and your AI knows its player.id and game. You can initialize your AI here.
        """

        # replace with your start logic




    def game_updated(self):
        """ this is called every time the game's state updates, so if you are tracking anything you can update it here.
        """

        # replace with your game updated logic




    def end(self, won, reason):
        """ this is called when the game ends, you can clean up your data and dump files here if need be

        Args:
            won (bool): won == true means you won, won == false means you lost
            reason (str): the reason why you won or lost
        """

        # replace with your end logic



    def run_turn(self):
        """ This is called every time the AI is asked to respond with a command during their turn

        Returns:
            bool: represents if you want to end your turn. true means end the turn, false means to keep your turn going and re-call runTurn()
        """

        # Here is where you'll want to code your AI.

        # We've provided sample code that:
        #    1) prints the board to the console
        #    2) prints the opponent's last move to the console
        #    3) prints how much time remaining this AI has to calculate moves
        #    4) makes a random (and probably invalid) move.

        # 1) print the board to the console
        for f in range(9, -2, -1): # iterate through the file in reverse order
            output = ""
            if f == 9 or f == 0: # then the top or bottom of the board
                output = "   +------------------------+"
            elif f == -1: # then show the ranks
                output = "     a  b  c  d  e  f  g  h"
            else: # board
                output = " " + str(f) + " |"
                # fill in all the ranks with pieces at the current rank
                for rankOffset in range(0, 8):
                    r = chr(ord("a") + rankOffset) # start at a, with with rank offset increasing the char
                    currentPiece = None
                    for piece in self.game.pieces:
                        if piece.rank == r and piece.file == f: # then we found the piece at (rank, file)
                            currentPiece = piece
                            break

                    code = "." # default "no piece"
                    if currentPiece:
                        code = currentPiece.type[0] # the code will be the first character of their type, e.g. 'Q' for "Queen"

                        if currentPiece.type == "Knight": # 'K' is for "King", we use 'N' for "Knights"
                            code = "N"

                        if currentPiece.owner.id == "1": # the second player (black) is lower case. Otherwise it's upppercase already
                            code = code.lower()

                    output += " " + code + " "

                output += "|"

            print(output)

        # 2) print the opponent's last move to the console
        if len(self.game.moves) > 0:
            print("Opponent's Last Move: '" + self.game.moves[-1] + "'")

        # 3) print how much time remaining this AI has to calculate moves
        print("Time Remaining: " + str(self.player.time_remaining) + " ns")

        # 4) make a random (and probably invalid) move.
        randomPiece = random.choice(self.player.pieces)
        randomRank = chr(ord("a") + random.randrange(8))
        randomFile = random.randrange(8) + 1
        randomPiece.move(randomRank, randomFile)

        return True # to signify we are done with our turn.
