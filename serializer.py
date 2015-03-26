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
