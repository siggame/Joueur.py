# Game: A 7x9 board game with pieces, to win the game the players must make successful captures of the enemy and reach the opponents den.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from typing import Dict, List
from joueur.base_game import BaseGame

# import game objects
from games.jungle_chess.game_object import GameObject
from games.jungle_chess.player import Player

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Game(BaseGame):
    """The class representing the Game in the JungleChess game.

    A 7x9 board game with pieces, to win the game the players must make successful captures of the enemy and reach the opponents den.
    """

    def __init__(self):
        """Initializes a Game with basic logic as provided by the Creer code generator.
        """
        BaseGame.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._game_objects = {}
        self._history = []
        self._jungle_fen = ""
        self._players = []
        self._session = ""

        self.name = "JungleChess"

        self._game_object_classes = {
            'GameObject': GameObject,
            'Player': Player
        }

    @property
    def game_objects(self) -> Dict[str, 'games.jungle_chess.game_object.GameObject']:
        """dict[str, games.jungle_chess.game_object.GameObject]: A mapping of every game object's ID to the actual game object. Primarily used by the server and client to easily refer to the game objects via ID.
        """
        return self._game_objects

    @property
    def history(self) -> List[str]:
        """list[str]: The list of [known] moves that have occurred in the game, in a format. The first element is the first move, with the last element being the most recent.
        """
        return self._history

    @property
    def jungle_fen(self) -> str:
        """str: The jungleFen is similar to the chess FEN, the order looks like this, board (split into rows by '/'), whose turn it is, half move, and full move.
        """
        return self._jungle_fen

    @property
    def players(self) -> List['games.jungle_chess.player.Player']:
        """list[games.jungle_chess.player.Player]: List of all the players in the game.
        """
        return self._players

    @property
    def session(self) -> str:
        """str: A unique identifier for the game instance that is being played.
        """
        return self._session

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
