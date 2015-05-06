# @class BaseGameObject: the base class that every game object within a game inherit from for Python manipulation that would be redundant via Creer
class BaseGameObject:
    def __init__(self, data):
        self._client = data['client']

    def _run_on_server(self, function_name, **kwargs):
        return self._client.run_on_server(self, function_name, kwargs)

    def __contains__(self, key):
        return hasattr(self, key)

    def __getitem__(self, key):
        return getattr(self, key)
