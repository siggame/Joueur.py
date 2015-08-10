import client

# @class DeltaMergeable: a game or game object that needs to be delta merged
class DeltaMergeable():
    def __init__(self):
        pass

    def _run_on_server(self, function_name, **kwargs):
        return client.run_on_server(self, function_name, kwargs)

    def __contains__(self, key):
        return hasattr(self, key)

    def __getitem__(self, key):
        return getattr(self, key)
