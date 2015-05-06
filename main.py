import argparse
import importlib
from client import Client

parser = argparse.ArgumentParser(description='Runs the python client with options. must provide a server and game to connect to')
parser.add_argument('game', action='store', help='the name of the game you want to play on the server')
parser.add_argument('-s, --server', action='store', dest='server', default='localhost', help='the url to the server you want to connect to e.g. locahost:3000')
parser.add_argument('-p, --port', action='store', dest='port', default=3000, help='the port to connect to on the server. Can be defined on the server arg via server:port')
parser.add_argument('-n, --name', action='store', dest='name', help='the name you want to use as your AI\'s player name')
parser.add_argument('-r, --session', action='store', dest='session', default='*', help='the requested game session you want to play on the server')
parser.add_argument('--printIO', action='store_true', dest='print_io', help='(debugging) print IO through the TCP socket to the terminal')

args = parser.parse_args()

split_server = args.server.split(":")
args.server = split_server[0]
args.port = int((len(split_server) == 2 and split[1])) or args.port

module = importlib.import_module(args.game) # should load Game and AI to load based on the game selected in args

game = module.Game({})
ai = module.AI(game)
client = Client(game, ai, args.server, args.port, print_io=args.print_io)

client.send("play", {
    'gameName': game.name,
    'requestedSession': args.session,
    'clientType': "Python",
    'playerName': args.name or ai.get_name() or "Python Player"
})

lobby_data = client.wait_for_event("lobbied")

print("In Lobby for game '" + lobby_data['gameName'] + "' in session '" + lobby_data['gameSession'] + "'")

game.set_client(client)
game.set_constants(lobby_data['constants'])

start_data = client.wait_for_event("start")

print("Game starting")

ai.set_player(game.get_game_object(start_data['playerID']))
ai.start()
ai.game_updated()

while True:
    data = client.wait_for_event("order") # the client will decide when to os.exit

    returned = ai.do_order(data['order'], data['args'])

    client.send("finished", {
        'finished': data['order'],
        'returned': returned
    })

