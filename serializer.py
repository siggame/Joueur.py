# Serializer: functions to serialize and unserialize json communication strings
from baseGameObject import BaseGameObject

def serialize(data):
    serialized = {}
    for key in data:
        value = data[key]
        if isinstance(value, BaseGameObject):
            serialized[key] =  {'id': value.id}
        elif isinstance(value, dict) or isinstance(value, list):
            serialized[key] = serialize(value)
        else:
            serialized[key] = value

    return serialized

def is_game_object_reference(d):
    return (isinstance(d, dict) and len(d) == 1 and 'id' in d)

def is_object(obj):
    return (isinstance(obj, dict) or isinstance(obj, list)) or isinstance(obj, BaseGameObject)
