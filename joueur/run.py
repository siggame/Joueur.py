import importlib
import joueur.client
from joueur.error_code import ErrorCode, handle_error
from joueur.game_manager import GameManager
from joueur.utilities import camel_case_converter

def run(args):
    split_server = args.server.split(":")
    args.server = split_server[0]
    args.port = int((len(split_server) == 2 and split[1])) or args.port

    module_str = "games." + camel_case_converter(args.game)
    try:
        module = importlib.import_module(module_str) # should load Game and AI to load based on the game selected in args
    except ImportError as e:
        handle_error(ErrorCode.game_not_found, e, "Could not find game module: '" + module_str + "'")

    game = module.Game()
    ai = module.AI(game)
    manager = GameManager(game)

    joueur.client.setup(game, ai, manager, args.server, int(args.port), print_io=args.print_io)

    joueur.client.send("play", {
        'gameName': game.name,
        'password': args.password,
        'requestedSession': args.session,
        'clientType': "Python",
        'playerName': args.name or ai.get_name() or "Python Player",
        'gameSettings': args.game_settings
    })

    lobby_data = joueur.client.wait_for_event("lobbied")

    print("In Lobby for game '" + lobby_data['gameName'] + "' in session '" + lobby_data['gameSession'] + "'")

    manager.set_constants(lobby_data['constants'])

    start_data = joueur.client.wait_for_event("start")

    print("Game starting")

    ai.set_player(game.get_game_object(start_data['playerID']))
    try:
        ai.start()
        ai.game_updated()
    except:
        handle_error(ErrorCode.ai_errored, sys.exc_info()[0], "AI errored during game initialization")

    joueur.client.play()
