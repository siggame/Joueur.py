import socket
import sys
import json
import time
from serializer import serialize, deserialize 
EOT_CHAR = chr(4)

## @class Client: talks to the server receiving game information and sending commands to execute. Clients perform no game logic
class Client():
    def __init__(self, game, ai, server='localhost', port=3000, print_io=False):
        self.game = game
        self.ai = ai
        self.server = server
        self.port = port

        self._print_io = print_io
        self._received_buffer = ""
        self._events_stack = []
        self._buffer_size = 1024
        self._timeout_time = 1.0

        print("connecting to:", self.server + ":" + str(self.port))

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # stupid Windows
        self.socket.settimeout(self._timeout_time) # so the blocking on recv doesn't hang forever and other system interupts (e.g. keyboard) can be handled
        self.socket.connect((self.server, self.port))


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

    ## disconnects from the server and ends the program
    def disconnect(self):
        print("Disconnected from server...")
        self.socket.close()
        sys.exit()



    def run_on_server(self, caller, function_name, args=None):
        self.send("run", {
            'caller': caller,
            'functionName': function_name,
            'args': args
        })

        ran_data = self.wait_for_event("ran")
        return deserialize(ran_data, self.game)

    def wait_for_event(self, event):
        while True:
            self.wait_for_events()

            while len(self._events_stack) > 0:
                sent = self._events_stack.pop()
                if sent['event'] == event:
                    return sent['data']
                else:
                    self._auto_handle(sent['event'], sent['data'] if 'data' in sent else None)

    ## loops to check the socket for incoming data and ends once some events get found
    def wait_for_events(self):
        if len(self._events_stack) > 0:
            return # as we already have events to handle, no need to wait for more

        try:
            while True:
                sent = ""
                try:
                    sent = self.socket.recv(self._buffer_size).decode("utf-8")
                except socket.timeout:
                    pass

                if not sent:
                    continue
                elif self._print_io:
                    print("FROM SERVER <--", sent)

                split = (self._received_buffer + sent).split(EOT_CHAR)
                self._received_buffer = split.pop() # the last item will either be "" if the last char was an EOT_CHAR, or a partial data we need to buffer anyways

                for json_str in reversed(split):
                    self._events_stack.append(json.loads(json_str))

                if len(self._events_stack) > 0:
                    return
        except (KeyboardInterrupt, SystemExit):
            self.disconnect()



        ## called via the client run loop when data is sent
    def _auto_handle(self, event, data=None):
        my_function = getattr(self, "_auto_handle_" + event)
        return my_function(data)

    def _auto_handle_delta(self, data):
        self.game.apply_delta_state(data)

        if self.ai.player: # then the AI is ready for updates
            self.ai.game_updated()

    def _auto_handle_invalid(self, data):
        self.ai.invalid(data)
        print("received invalid data", data)
        self.disconnect()

    def _auto_handle_over(self, data):
        won = self.ai.player.won
        reason = self.ai.player.reason_won if self.ai.player.won else self.ai.player.reason_lost

        print("Game is over.", "I Won!" if won else "I Lost :(", "because: " + reason)

        self.ai.end(won, reason)
        self.disconnect()
