# This is where you build your AI for the Chess game.

from joueur.base_ai import BaseAI
import random

class AI(BaseAI):
    """ The basic AI functions that are the same between games. """


    def get_name(self):
        """ This is the name you send to the server so your AI will control the player named this string.

        Returns
            str: The name of your Player.
        """

        return "Chess Python Player" # REPLACE THIS WITH YOUR TEAM NAME



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

        # Here is where you'll want to code your AI.

        # We've provided sample code that:
        #    1) prints the board to the console
        #    2) prints the opponent's last move to the console
        #    3) prints how much time remaining this AI has to calculate moves
        #    4) makes a random (and probably invalid) move.

        # 1) print the board to the console
        for r in range(9, -2, -1): # iterate through the range in reverse order
            output = ""
            if r == 9 or r == 0: # then the top or bottom of the board
                output = "   +------------------------+"
            elif r == -1: # then show the ranks
                output = "     a  b  c  d  e  f  g  h"
            else: # board
                output = " " + str(r) + " |"
                # fill in all the ranks with pieces at the current file
                for file_offset in range(0, 8):
                    f = chr(ord("a") + file_offset) # start at a, with with file offset increasing the char
                    current_piece = None
                    for piece in self.game.pieces:
                        if piece.file == f and piece.rank == r: # then we found the piece at (file, rank)
                            current_piece = piece
                            break

                    code = "." # default "no piece"
                    if current_piece:
                        code = current_piece.type[0] # the code will be the first character of their type, e.g. 'Q' for "Queen"

                        if current_piece.type == "Knight": # 'K' is for "King", we use 'N' for "Knights"
                            code = "N"

                        if current_piece.owner.id == "1": # the second player (black) is lower case. Otherwise it's upppercase already
                            code = code.lower()

                    output += " " + code + " "

                output += "|"

            print(output)

        # 2) print the opponent's last move to the console
        if len(self.game.moves) > 0:
            print("Opponent's Last Move: '" + self.game.moves[-1].san + "'")

        # 3) print how much time remaining this AI has to calculate moves
        print("Time Remaining: " + str(self.player.time_remaining) + " ns")

        # 4) make a random (and probably invalid) move.
        random_piece = random.choice(self.player.pieces)
        random_file = chr(ord("a") + random.randrange(8))
        random_rank = random.randrange(8) + 1
        random_piece.move(random_file, random_rank)

        return True # to signify we are done with our turn.
