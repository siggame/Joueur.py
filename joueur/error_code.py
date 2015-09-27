from enum import Enum
import traceback
import sys
import joueur.client
import os

class ErrorCode(Enum):
    none = 0
    invalid_args = 20
    could_not_connect = 21
    disconnected_unexpectedly = 22
    cannot_read_socket = 23
    delta_merge_failure = 24
    reflection_failed = 25
    unknown_event_from_server = 26
    server_timeout = 27
    fatal_event = 28
    game_not_found = 29
    malformed_json = 30
    unauthenticated = 31
    ai_errored = 42

def handle_error(code, e=None, message=None):
    if isinstance(e, SystemExit) or isinstance(e, KeyboardInterrupt): # we accidentally caught an exit exception, just re-throw it till it gets to the end of the runtime stack
        sys.exit(e.code)

    joueur.client.disconnect()

    sys.stderr.write("Error: " + code.name + "\n---\n")

    if message:
        sys.stderr.write(message + "\n---\n")

    if e:
        sys.stderr.write(str(e) + "\n---\n")

    traceback.print_stack()
    print("---")
    os._exit(code.value)
