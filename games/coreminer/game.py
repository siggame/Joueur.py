# Game: Mine resources to obtain more value than your opponent.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from joueur.base_game import BaseGame

# import game objects
from games.coreminer.bomb import Bomb
from games.coreminer.game_object import GameObject
from games.coreminer.miner import Miner
from games.coreminer.player import Player
from games.coreminer.tile import Tile
from games.coreminer.upgrade import Upgrade

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Game(BaseGame):
    """The class representing the Game in the Coreminer game.

    Mine resources to obtain more value than your opponent.
    """

    def __init__(self):
        """Initializes a Game with basic logic as provided by the Creer code generator."""
        BaseGame.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._bomb_price = 0
        self._bomb_size = 0
        self._bombs = []
        self._building_material_price = 0
        self._current_player = None
        self._current_turn = 0
        self._dirt_price = 0
        self._fall_damage = 0
        self._fall_weight_damage = 0
        self._game_objects = {}
        self._ladder_cost = 0
        self._ladder_health = 0
        self._large_cargo_size = 0
        self._large_material_size = 0
        self._map_height = 0
        self._map_width = 0
        self._max_shielding = 0
        self._max_turns = 100
        self._max_upgrade_level = 0
        self._miners = []
        self._ore_price = 0
        self._ore_value = 0
        self._players = []
        self._session = ""
        self._shield_cost = 0
        self._shield_health = 0
        self._spawn_price = 0
        self._suffocation_damage = 0
        self._suffocation_weight_damage = 0
        self._support_cost = 0
        self._support_health = 0
        self._tiles = []
        self._time_added_per_turn = 0
        self._upgrade_price = 0
        self._upgrades = []
        self._victory_amount = 0

        self.name = "Coreminer"

        self._game_object_classes = {
            'Bomb': Bomb,
            'GameObject': GameObject,
            'Miner': Miner,
            'Player': Player,
            'Tile': Tile,
            'Upgrade': Upgrade
        }

    @property
    def bomb_price(self):
        """The monetary price of a bomb when bought or sold.

        :rtype: int
        """
        return self._bomb_price

    @property
    def bomb_size(self):
        """The amount of cargo space taken up by a Bomb.

        :rtype: int
        """
        return self._bomb_size

    @property
    def bombs(self):
        """Every Bomb in the game.

        :rtype: list[games.coreminer.bomb.Bomb]
        """
        return self._bombs

    @property
    def building_material_price(self):
        """The monetary price of building materials when bought.

        :rtype: int
        """
        return self._building_material_price

    @property
    def current_player(self):
        """The player whose turn it is currently. That player can send commands. Other players cannot.

        :rtype: games.coreminer.player.Player
        """
        return self._current_player

    @property
    def current_turn(self):
        """The current turn number, starting at 0 for the first player's turn.

        :rtype: int
        """
        return self._current_turn

    @property
    def dirt_price(self):
        """The monetary price of dirt when bought or sold.

        :rtype: int
        """
        return self._dirt_price

    @property
    def fall_damage(self):
        """The amount of damage taken per Tile fallen.

        :rtype: int
        """
        return self._fall_damage

    @property
    def fall_weight_damage(self):
        """The amount of extra damage taken for falling while carrying a large amount of cargo.

        :rtype: int
        """
        return self._fall_weight_damage

    @property
    def game_objects(self):
        """A mapping of every game object's ID to the actual game object. Primarily used by the server and client to easily refer to the game objects via ID.

        :rtype: dict[str, games.coreminer.game_object.GameObject]
        """
        return self._game_objects

    @property
    def ladder_cost(self):
        """The amount of building material required to build a ladder.

        :rtype: int
        """
        return self._ladder_cost

    @property
    def ladder_health(self):
        """The amount of mining power needed to remove a ladder from a Tile.

        :rtype: int
        """
        return self._ladder_health

    @property
    def large_cargo_size(self):
        """The amount deemed as a large amount of cargo.

        :rtype: int
        """
        return self._large_cargo_size

    @property
    def large_material_size(self):
        """The amount deemed as a large amount of material.

        :rtype: int
        """
        return self._large_material_size

    @property
    def map_height(self):
        """The number of Tiles in the map along the y (vertical) axis.

        :rtype: int
        """
        return self._map_height

    @property
    def map_width(self):
        """The number of Tiles in the map along the x (horizontal) axis.

        :rtype: int
        """
        return self._map_width

    @property
    def max_shielding(self):
        """The maximum amount of shielding possible on a Tile.

        :rtype: int
        """
        return self._max_shielding

    @property
    def max_turns(self):
        """The maximum number of turns before the game will automatically end.

        :rtype: int
        """
        return self._max_turns

    @property
    def max_upgrade_level(self):
        """The highest upgrade level allowed on a Miner.

        :rtype: int
        """
        return self._max_upgrade_level

    @property
    def miners(self):
        """Every Miner in the game.

        :rtype: list[games.coreminer.miner.Miner]
        """
        return self._miners

    @property
    def ore_price(self):
        """The amount of money awarded when ore is dumped in the base and sold.

        :rtype: int
        """
        return self._ore_price

    @property
    def ore_value(self):
        """The amount of value awarded when ore is dumped in the base and sold.

        :rtype: int
        """
        return self._ore_value

    @property
    def players(self):
        """List of all the players in the game.

        :rtype: list[games.coreminer.player.Player]
        """
        return self._players

    @property
    def session(self):
        """A unique identifier for the game instance that is being played.

        :rtype: str
        """
        return self._session

    @property
    def shield_cost(self):
        """The amount of building material required to shield a Tile.

        :rtype: int
        """
        return self._shield_cost

    @property
    def shield_health(self):
        """The amount of mining power needed to remove one unit of shielding off a Tile.

        :rtype: int
        """
        return self._shield_health

    @property
    def spawn_price(self):
        """The monetary price of spawning a Miner.

        :rtype: int
        """
        return self._spawn_price

    @property
    def suffocation_damage(self):
        """The amount of damage taken when suffocating inside a filled Tile.

        :rtype: int
        """
        return self._suffocation_damage

    @property
    def suffocation_weight_damage(self):
        """The amount of extra damage taken for suffocating under a large amount of material.

        :rtype: int
        """
        return self._suffocation_weight_damage

    @property
    def support_cost(self):
        """The amount of building material required to build a support.

        :rtype: int
        """
        return self._support_cost

    @property
    def support_health(self):
        """The amount of mining power needed to remove a support from a Tile.

        :rtype: int
        """
        return self._support_health

    @property
    def tiles(self):
        """All the tiles in the map, stored in Row-major order. Use `x + y * mapWidth` to access the correct index.

        :rtype: list[games.coreminer.tile.Tile]
        """
        return self._tiles

    @property
    def time_added_per_turn(self):
        """The amount of time (in nano-seconds) added after each player performs a turn.

        :rtype: int
        """
        return self._time_added_per_turn

    @property
    def upgrade_price(self):
        """The cost to upgrade a Miner.

        :rtype: int
        """
        return self._upgrade_price

    @property
    def upgrades(self):
        """Every Upgrade for a Miner in the game.

        :rtype: list[games.coreminer.upgrade.Upgrade]
        """
        return self._upgrades

    @property
    def victory_amount(self):
        """The amount of victory points (value) required to win.

        :rtype: int
        """
        return self._victory_amount


    def get_tile_at(self, x, y):
        """Gets the Tile at a specified (x, y) position
        Args:
            x (int): integer between 0 and the map_width
            y (int): integer between 0 and the map_height
        Returns:
            games.coreminer.tile.Tile: the Tile at (x, y) or None if out of bounds
        """
        if x < 0 or y < 0 or x >= self.map_width or y >= self.map_height:
            # out of bounds
            return None

        return self.tiles[x + y * self.map_width]

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
