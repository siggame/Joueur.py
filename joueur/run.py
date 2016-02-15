import importlib.util
import joueur.client
import sys
import joueur.error_code as error_code
from joueur.game_manager import GameManager
from joueur.utilities import camel_case_converter
import joueur.ansi_color_coder as color

def run(args):
    split_server = args.server.split(":")
    args.server = split_server[0]
    args.port = int((len(split_server) == 2 and split[1])) or args.port

    module_str = "games." + camel_case_converter(args.game)

    spec = importlib.util.find_spec(module_str)
    if spec is None:
        error_code.handle_error(error_code.GAME_NOT_FOUND, None, "Could not find the module for game '{}'.".format(args.game))

    try:
        module = importlib.import_module(module_str) # should load Game and AI to load based on the game selected in args
    except ImportError as e:
        error_code.handle_error(error_code.REFLECTION_FAILED, e, "Could not import game module: '{}'.".format(module_str))

    game = module.Game()
    try:
        ai = module.AI(game)
    except:
        error_code.handle_error(error_code.AI_ERRORED, sys.exc_info()[0], "Could not initialize AI class. Probably a syntax error in your AI.")
    manager = GameManager(game)

    joueur.client.setup(game, ai, manager, args.server, int(args.port), print_io=args.print_io)

    joueur.client.send("play", {
        'gameName': game.name,
        'password': args.password,
        'requestedSession': args.session,
        'clientType': "Python",
        'playerName': args.name or ai.get_name() or "Python Player",
        'playerIndex': args.index,
        'gameSettings': args.game_settings
    })

    lobby_data = joueur.client.wait_for_event("lobbied")

    print(color.text("cyan") + "In lobby for game '" + lobby_data['gameName'] + "' in session '" + lobby_data['gameSession'] + "'." + color.reset())

    manager.set_constants(lobby_data['constants'])

    start_data = joueur.client.wait_for_event("start")

    print(color.text("green") + "Game is starting." + color.reset())

    ai.set_player(game.get_game_object(start_data['playerID']))
    try:
        ai.start()
        ai.game_updated()
    except:
        error_code.handle_error(error_code.AI_ERRORED, sys.exc_info()[0], "AI errored during game initialization")

    joueur.client.play()
