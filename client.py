import socket, errno
import sys
import json
import time
from serializer import serialize, deserialize
from error_code import ErrorCode
from error_code import handle_error as handle_error_exit
from game_manager import GameManager
EOT_CHAR = chr(4)

class _Client:
    pass

_client = _Client()

## Client: A singlton module that talks to the server receiving game information and sending commands to execute. Clients perform no game logic
def setup(game, ai, manager, server='localhost', port=3000, print_io=False):
    _client.game = game
    _client.ai = ai
    _client.server = server
    _client.port = port
    _client.manager = manager

    _client._print_io = print_io
    _client._received_buffer = ""
    _client._events_stack = []
    _client._buffer_size = 1024
    _client._timeout_time = 1.0

    print("connecting to:", _client.server + ":" + str(_client.port))

    try:
        _client.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        _client.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # stupid Windows
        _client.socket.settimeout(_client._timeout_time) # so the blocking on recv doesn't hang forever and other system interupts (e.g. keyboard) can be handled
        _client.socket.connect((_client.server, _client.port))
    except socket.error as e:
        handle_error_exit(ErrorCode.could_not_connect, e, "Could not connect to " + _client.server + ":" + _client.port)


def _send_raw(string):
    if _client._print_io:
        print("TO SERVER -->", string)
    _client.socket.send(string)

 ## sends the server an event via socket
def send(event, data):
    _send_raw(
        (json.dumps({
            'sentTime': int(time.time()),
            'event': event,
            'data': serialize(data)
        })
        + EOT_CHAR).encode('utf-8')
    )

def handle_error(code, e=None, message=None):
    disconnect()
    handle_error_exit(code, e, message)

def disconnect(exit_code=None):
    _client.socket.close()
    if exit_code != None:
        sys.exit(exit_code)

def run_on_server(caller, function_name, args=None):
    send("run", {
        'caller': caller,
        'functionName': function_name,
        'args': args
    })

    ran_data = wait_for_event("ran")
    return deserialize(ran_data, _client.game)

def play():
    wait_for_event(None)

def wait_for_event(event):
    while True:
        wait_for_events()

        while len(_client._events_stack) > 0:
            sent = _client._events_stack.pop()
            if event != None and sent['event'] == event:
                return sent['data']
            else:
                _auto_handle(sent['event'], sent['data'] if 'data' in sent else None)

## loops to check the socket for incoming data and ends once some events get found
def wait_for_events():
    if len(_client._events_stack) > 0:
        return # as we already have events to handle, no need to wait for more

    try:
        while True:
            sent = None
            try:
                sent = _client.socket.recv(_client._buffer_size).decode("utf-8")
            except socket.timeout:
                pass # timed out so keyboard/system interupts can be handled, hence the while true loop above
            except socket.error as e:
                handle_error(ErrorCode.cannot_read_socket, e, "Error reading socket while waiting for events")

            if not sent:
                continue
            elif _client._print_io:
                print("FROM SERVER <--", sent)

            split = (_client._received_buffer + sent).split(EOT_CHAR)
            _client._received_buffer = split.pop() # the last item will either be "" if the last char was an EOT_CHAR, or a partial data we need to buffer anyways

            for json_str in reversed(split):
                try:
                    parsed = json.loads(json_str)
                except ValueError as e:
                    handle_error(ErrorCode.malformed_json, e, "Could not parse json '" + json_str + "'")

                _client._events_stack.append(parsed)

            if len(_client._events_stack) > 0:
                return
    except (KeyboardInterrupt, SystemExit):
        disconnect(1)

    ## called via the client run loop when data is sent
def _auto_handle(event, data=None):
    g = globals() # the current module, e.g. the Client module that acts as a singleton
    auto_handle_function = g["_auto_handle_" + event]

    if auto_handle_function:
        return auto_handle_function(data)
    else:
        handle_error(ErrorCode.unknown_event_from_server, message=("Could not auto handle event '" + event + "'."))

def _auto_handle_delta(data):
    try:
        _client.manager.apply_delta_state(data)
    except:
        handle_error(ErrorCode.delta_merge_failure, sys.exc_info()[0], "Error merging delta")

    if _client.ai.player: # then the AI is ready for updates
        _client.ai.game_updated()

def _auto_handle_order(data):
    try:
        returned = _client.ai._do_order(data['order'], data['args'])
    except:
        handle_error(ErrorCode.ai_errored, sys.exc_info()[0], "AI errored executing order '" + data['order'] + "'.")

    send("finished", {
        'finished': data['order'],
        'returned': returned
    })

def _auto_handle_invalid(data):
    _client.ai.invalid(data)
    handle_error(ErrorCode.invalid_event, message="Got invalid data: '" + data + "'")

def _auto_handle_over(data):
    won = _client.ai.player.won
    reason = _client.ai.player.reason_won if _client.ai.player.won else _client.ai.player.reason_lost

    print("Game is over.", "I Won!" if won else "I Lost :(", "because: " + reason)

    _client.ai.end(won, reason)
    disconnect(0)

