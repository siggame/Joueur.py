# Game: Collect of the most of the rarest mineral orbiting aroung the sun and outcompete your competetor.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from typing import Dict, List
from joueur.base_game import BaseGame

# import game objects
from games.stardash.body import Body
from games.stardash.game_object import GameObject
from games.stardash.job import Job
from games.stardash.player import Player
from games.stardash.projectile import Projectile
from games.stardash.unit import Unit

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Game(BaseGame):
    """The class representing the Game in the Stardash game.

    Collect of the most of the rarest mineral orbiting aroung the sun and outcompete your competetor.
    """

    def __init__(self):
        """Initializes a Game with basic logic as provided by the Creer code generator.
        """
        BaseGame.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._bodies = []
        self._current_player = None
        self._current_turn = 0
        self._dash_cost = 0
        self._dash_distance = 0
        self._game_objects = {}
        self._genarium_value = 0
        self._jobs = []
        self._legendarium_value = 0
        self._max_asteroid = 0
        self._max_turns = 100
        self._min_asteroid = 0
        self._mining_speed = 0
        self._mythicite_amount = 0
        self._orbits_protected = 0
        self._ore_rarity_genarium = 0
        self._ore_rarity_legendarium = 0
        self._ore_rarity_rarium = 0
        self._planet_energy_cap = 0
        self._planet_recharge_rate = 0
        self._players = []
        self._projectile_radius = 0
        self._projectile_speed = 0
        self._projectiles = []
        self._rarium_value = 0
        self._regenerate_rate = 0
        self._session = ""
        self._ship_radius = 0
        self._size_x = 0
        self._size_y = 0
        self._time_added_per_turn = 0
        self._turns_to_orbit = 0
        self._units = []

        self.name = "Stardash"

        self._game_object_classes = {
            'Body': Body,
            'GameObject': GameObject,
            'Job': Job,
            'Player': Player,
            'Projectile': Projectile,
            'Unit': Unit
        }

    @property
    def bodies(self) -> List['games.stardash.body.Body']:
        """list[games.stardash.body.Body]: All the celestial bodies in the game. The first two are planets and the third is the sun. The fourth is the VP asteroid. Everything else is normal asteroids.
        """
        return self._bodies

    @property
    def current_player(self) -> 'games.stardash.player.Player':
        """games.stardash.player.Player: The player whose turn it is currently. That player can send commands. Other players cannot.
        """
        return self._current_player

    @property
    def current_turn(self) -> int:
        """int: The current turn number, starting at 0 for the first player's turn.
        """
        return self._current_turn

    @property
    def dash_cost(self) -> int:
        """int: The cost of dashing.
        """
        return self._dash_cost

    @property
    def dash_distance(self) -> int:
        """int: The distance traveled each turn by dashing.
        """
        return self._dash_distance

    @property
    def game_objects(self) -> Dict[str, 'games.stardash.game_object.GameObject']:
        """dict[str, games.stardash.game_object.GameObject]: A mapping of every game object's ID to the actual game object. Primarily used by the server and client to easily refer to the game objects via ID.
        """
        return self._game_objects

    @property
    def genarium_value(self) -> float:
        """float: The value of every unit of genarium.
        """
        return self._genarium_value

    @property
    def jobs(self) -> List['games.stardash.job.Job']:
        """list[games.stardash.job.Job]: A list of all jobs. first item is corvette, second is missileboat, third is martyr, fourth is transport, and fifth is miner.
        """
        return self._jobs

    @property
    def legendarium_value(self) -> float:
        """float: The value of every unit of legendarium.
        """
        return self._legendarium_value

    @property
    def max_asteroid(self) -> int:
        """int: The highest amount of material, that can be in a asteroid.
        """
        return self._max_asteroid

    @property
    def max_turns(self) -> int:
        """int: The maximum number of turns before the game will automatically end.
        """
        return self._max_turns

    @property
    def min_asteroid(self) -> int:
        """int: The smallest amount of material, that can be in a asteroid.
        """
        return self._min_asteroid

    @property
    def mining_speed(self) -> int:
        """int: The rate at which miners grab minerals from asteroids.
        """
        return self._mining_speed

    @property
    def mythicite_amount(self) -> float:
        """float: The amount of mythicite that spawns at the start of the game.
        """
        return self._mythicite_amount

    @property
    def orbits_protected(self) -> int:
        """int: The number of orbit updates you cannot mine the mithicite asteroid.
        """
        return self._orbits_protected

    @property
    def ore_rarity_genarium(self) -> float:
        """float: The rarity modifier of the most common ore. This controls how much spawns.
        """
        return self._ore_rarity_genarium

    @property
    def ore_rarity_legendarium(self) -> float:
        """float: The rarity modifier of the rarest ore. This controls how much spawns.
        """
        return self._ore_rarity_legendarium

    @property
    def ore_rarity_rarium(self) -> float:
        """float: The rarity modifier of the second rarest ore. This controls how much spawns.
        """
        return self._ore_rarity_rarium

    @property
    def planet_energy_cap(self) -> int:
        """int: The amount of energy a planet can hold at once.
        """
        return self._planet_energy_cap

    @property
    def planet_recharge_rate(self) -> int:
        """int: The amount of energy the planets restore each round.
        """
        return self._planet_recharge_rate

    @property
    def players(self) -> List['games.stardash.player.Player']:
        """list[games.stardash.player.Player]: List of all the players in the game.
        """
        return self._players

    @property
    def projectile_radius(self) -> int:
        """int: The standard size of ships.
        """
        return self._projectile_radius

    @property
    def projectile_speed(self) -> int:
        """int: The amount of distance missiles travel through space.
        """
        return self._projectile_speed

    @property
    def projectiles(self) -> List['games.stardash.projectile.Projectile']:
        """list[games.stardash.projectile.Projectile]: Every projectile in the game.
        """
        return self._projectiles

    @property
    def rarium_value(self) -> float:
        """float: The value of every unit of rarium.
        """
        return self._rarium_value

    @property
    def regenerate_rate(self) -> float:
        """float: The regeneration rate of asteroids.
        """
        return self._regenerate_rate

    @property
    def session(self) -> str:
        """str: A unique identifier for the game instance that is being played.
        """
        return self._session

    @property
    def ship_radius(self) -> int:
        """int: The standard size of ships.
        """
        return self._ship_radius

    @property
    def size_x(self) -> int:
        """int: The size of the map in the X direction.
        """
        return self._size_x

    @property
    def size_y(self) -> int:
        """int: The size of the map in the Y direction.
        """
        return self._size_y

    @property
    def time_added_per_turn(self) -> int:
        """int: The amount of time (in nano-seconds) added after each player performs a turn.
        """
        return self._time_added_per_turn

    @property
    def turns_to_orbit(self) -> int:
        """int: The number of turns it takes for a asteroid to orbit the sun. (Asteroids move after each players turn).
        """
        return self._turns_to_orbit

    @property
    def units(self) -> List['games.stardash.unit.Unit']:
        """list[games.stardash.unit.Unit]: Every Unit in the game.
        """
        return self._units

    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
