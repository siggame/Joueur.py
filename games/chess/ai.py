# This is where you build your AI for the Chess game.

from joueur.base_ai import BaseAI

def pretty_fen(fen, us):
    """
    Pretty formats an FEN string to a human readable string.

    For more information on FEN (Forsyth-Edwards Notation) strings see:
    https://wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation
    """

    # split the FEN string up to help parse it
    split = fen.split(' ')
    first = split[0] # the first part is always the board locations

    side_to_move = split[1] # always the second part for side to move
    us_or_them = 'us' if side_to_move == us[0] else 'them'

    fullmove = split[5]; # always the sixth part for the full move

    lines = first.split('/')
    strings = [
        'Move: {}\nSide to move: {} ({})\n   +-----------------+'.format(
            fullmove, side_to_move, us_or_them
        )
    ]

    for i, line in enumerate(lines):
        strings.append('\n {} |'.format(8 - i))
        for char in line:
            try:
                char_as_number = int(char)
                # it is a number, so that many blank lines
                strings.append(' .' * char_as_number)
            except:
                strings.append(' ' + char)

        strings.append(' |')
    strings.append('\n   +-----------------+\n     a b c d e f g h\n')

    return ''.join(strings)

class AI(BaseAI):
    """ The AI you add and improve code inside to play Chess. """

    @property
    def game(self) -> 'games.chess.game.Game':
        """games.chess.game.Game: The reference to the Game instance this AI
        is playing.
        """
        return self._game # don't directly touch this "private" variable pls

    @property
    def player(self) -> 'games.chess.player.Player':
        """games.chess.player.Player: The reference to the Player this AI
        controls in the Game.
        """
        return self._player # don't directly touch this "private" variable pls

    def get_name(self) -> str:
        """This is the name you send to the server so your AI will control
        the player named this string.

        Returns:
            str: The name of your Player.
        """
        return "Chess Python Player" # REPLACE THIS WITH YOUR TEAM NAME

    def start(self) -> None:
        """This is called once the game starts and your AI knows its player
        and game. You can initialize your AI here.
        """
        # replace with your start logic

    def game_updated(self) -> None:
        """This is called every time the game's state updates, so if you are
        tracking anything you can update it here.
        """
        # replace with your game updated logic

    def end(self, won: bool, reason: str) -> None:
        """This is called when the game ends, you can clean up your data and
        dump files here if need be.

        Args:
            won (bool): True means you won, False means you lost.
            reason (str): The human readable string explaining why your AI
            won or lost.
        """
        # replace with your end logic

    def make_move(self) -> str:
        """This is called every time it is this AI.player's turn to make a
        move.

        Returns:
            str: A string in Universal Chess Inferface (UCI) or
            Standard Algebraic Notation (SAN) formatting for the move you
            want to make. If the move is invalid or not properly formatted
            you will lose the game.
        """
        print(pretty_fen(self.game.fen, self.player.color))

        # This will only work if we are black move the pawn at b2 to b3.
        # Otherwise we will lose.
        # Your job is to code SOMETHING to parse the FEN string in some way
        # to determine a valid move, in UCI format.
        return 'b2b3'
