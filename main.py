import argparse
import importlib
import client
from error_code import ErrorCode, handle_error
from game_manager import GameManager
from utilities import camel_case_converter

parser = argparse.ArgumentParser(description='Runs the python client with options. Must provide a game name to play on the server.')
parser.add_argument('game', action='store', help='the name of the game you want to play on the server')
parser.add_argument('-s, --server', action='store', dest='server', default='localhost', help='the url to the server you want to connect to e.g. locahost:3000')
parser.add_argument('-p, --port', action='store', dest='port', default=3000, help='the port to connect to on the server. Can be defined on the server arg via server:port')
parser.add_argument('-n, --name', action='store', dest='name', help='the name you want to use as your AI\'s player name. This over-rides the name you set in your code')
parser.add_argument('-r, --session', action='store', dest='session', default='*', help='the requested game session you want to play on the server')
parser.add_argument('--printIO', action='store_true', dest='print_io', help='(debugging) print IO through the TCP socket to the terminal')

args = parser.parse_args()

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

client.setup(game, ai, manager, args.server, int(args.port), print_io=args.print_io)

client.send("play", {
    'gameName': game.name,
    'requestedSession': args.session,
    'clientType': "Python",
    'playerName': args.name or ai.get_name() or "Python Player"
})

lobby_data = client.wait_for_event("lobbied")

print("In Lobby for game '" + lobby_data['gameName'] + "' in session '" + lobby_data['gameSession'] + "'")

manager.set_constants(lobby_data['constants'])

start_data = client.wait_for_event("start")

print("Game starting")

ai.set_player(game.get_game_object(start_data['playerID']))
try:
    ai.start()
    ai.game_updated()
except:
    client.handle_error(ErrorCode.ai_errored, sys.exc_info()[0], "AI errored during game initialization")

client.play()
