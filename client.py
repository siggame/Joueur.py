import socket
import sys
import json
import time
from serializer import serialize
EOT_CHAR = chr(4)

## @class Client: talks to the server recieving game information and sending commands to execute. Clients perform no game logic
class Client():
    def __init__(self, game, ai, server='localhost', port=3000, requested_session="*", player_name=None, print_io=False):
        self.game = game
        self.ai = ai
        self.server = server
        self.port = port
        self._requested_session = requested_session
        self._player_name = player_name
        self._print_io = print_io
        self._got_initial_state = False

        self._isRunning = False
        self._buffer_size = 1024
        self._timeout_time = 1.0

        print("connecting to:", self.server + ":" + str(self.port))

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # stupid Windows
        self.socket.connect((self.server, self.port))


    ## disconnects from the server and ends the program
    def disconnect(self):
        print("Disconnected from server...")
        self._isRunning = False
        self.socket.close()
        sys.exit()

    ## tells the server this player is ready to play a game
    def ready(self):
        self.send('play', {
            'clientType': 'Python',
            'playerName': self._player_name or self.ai.get_name() or "Python Player",
            'gameName': self.game.name,
            'gameSession': self._requested_session
        })

        self.run()

    ## loops to check the socket for incoming data and runs it when it gets.
    def run(self):
        self._isRunning = True

        buffer = ""
        try:
            while self._isRunning:
                self.socket.settimeout(self._timeout_time) # so the blocking on recv doesn't hang forever and other system interupts (e.g. keyboard) can be handled
                sent = ""
                try:
                    sent = self.socket.recv(self._buffer_size).decode("utf-8")
                except socket.timeout:
                    pass

                if not sent:
                    continue
                elif self._print_io:
                    print("FROM SERVER <--", sent)

                split = (buffer + sent).split(EOT_CHAR)
                buffer = split.pop() # the last item will either be "" if the last char was an EOT_CHAR, or a partial data we need to buffer anyways

                for json_str in split:
                    self._sent_data(json.loads(json_str))
        except (KeyboardInterrupt, SystemExit):
            pass
        self.disconnect()

        ## called via the client run loop when data is sent
    def _sent_data(self, data):
        my_function = getattr(self, "_sent_" + data['event'])
        my_function(data['data'] if 'data' in data else None)


    def _send_raw(self, string):
        if self._print_io:
            print("TO SERVER -->", string)
        self.socket.send(string)

     ## sends the server an event via socket
    def send(self, event, data):
        self._send_raw(
            (json.dumps({
                'sentTime': int(time.time()),
                'event': event,
                'data': serialize(data)
            })
            + EOT_CHAR).encode('utf-8')
        )



    #-- Socket sent data functions --#

    def _sent_lobbied(self, data):
        self.game.set_constants(data['constants'])
        print("Connection successful to game '" + data['gameName'] + "' in session '" + str(data['gameSession']) + "'.")

    def _sent_start(self, data):
        self._player_id = data['playerID']

    def _sent_request(self, data):
        response = self.ai.respond_to(data['request'], data['args'])

        if response == None:
            print("no response return to: '" + data['request'] + "', erroring out")
            self.disconnect()
        else:
            self.send("response", {
                'response': data['request'],
                'data': response
            })

    def _sent_delta(self, data):
        self.game.apply_delta_state(data)

        if not self._got_initial_state:
            self._got_initial_state = True

            self.ai.set_player(self.game.get_game_object(self._player_id))
            self.ai.start()

        self.ai.game_updated()

    def _sent_invalid(self, data):
        self.ai.invalid(data)
        print("recieved invalid data", data)
        self.disconnect()

    def _sent_over(self, data):
        won = self.ai.player.won
        reason = self.ai.player.reason_won if self.ai.player.won else self.ai.player.reason_lost

        print("Game is over.", "I Won!" if won else "I Lost :(", "because: " + reason)

        self.ai.end(won, reason)
        self.disconnect()
