<%include file="functions.noCreer" /># ${obj_key}: ${shared['py']['format_description'](obj['description'])}
<%
parent_classes = obj['parentClasses']
builtin_typing_imports = set()
if 'TiledGame' in game['serverParentClasses']:
    if obj_key == 'Game':
        builtin_typing_imports.add('Optional')
    elif obj_key == 'Tile':
        builtin_typing_imports.add('List')

typing_import = shared['py']['get_imports'](
    obj,
    builtin_typing_imports
)
if typing_import:
    typing_import = '\n' + typing_import
%>
# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.
${typing_import}
% if len(parent_classes) > 0:
% for parent_class in parent_classes:
from games.${underscore(game_name)}.${underscore(parent_class)} import ${parent_class}
% endfor
% else:
<% if obj_key == "Game":
    parent_classes = [ 'BaseGame' ]
else:
    parent_classes = [ 'BaseGameObject' ]
%>from joueur.${underscore(parent_classes[0])} import ${parent_classes[0]}
% endif

% if obj_key == "Game":
# import game objects
% for game_obj_key in sort_dict_keys(game_objs):
from games.${underscore(game_name)}.${underscore(game_obj_key)} import ${game_obj_key}
% endfor

% endif
${merge("# ", "imports", "# you can add additional import(s) here", optional=True)}

class ${obj_key}(${", ".join(parent_classes)}):
    """The class representing the ${obj_key} in the ${game_name} game.

    ${shared['py']['format_description'](obj['description'])}
    """

${shared['py']['function_top']('__init__', {
    'description': 'Initializes a ' + obj_key + ' with basic logic as provided by the Creer code generator.'
})}
% for parent_class in reversed(parent_classes):
        ${parent_class}.__init__(self)
% endfor

        # private attributes to hold the properties so they appear read only
% for attr_name in obj['attribute_names']:
<% attr_parms = obj['attributes'][attr_name]
%>        self._${underscore(attr_name)} = ${shared['py']['default'](attr_parms['type'], attr_parms['default'])}
% endfor

% if obj_key == "Game":
        self.name = "${game_name}"

        self._game_object_classes = {<% c = len(game_objs) %>
% for game_obj_key in sort_dict_keys(game_objs):
<% c -= 1
%>            '${game_obj_key}': ${game_obj_key}${',' if c != 0 else ''}
% endfor
        }

% endif
% for attr_name in obj['attribute_names']:
<% attr_parms = obj['attributes'][attr_name]
%>${shared['py']['function_top'](attr_name, attr_parms, is_property=True)}
        return self._${underscore(attr_name)}

% endfor
% for function_name in obj['function_names']:
<% function_parms = obj['functions'][function_name]
%>${shared['py']['function_top'](function_name, function_parms)}
        return self._run_on_server('${function_name}', {
${',\n'.join(map(
    lambda arg_name: "            '{}': {}".format(arg_name, underscore(arg_name)),
    function_parms['argument_names']
))}
        })

% endfor
% if 'Tile' in game_objs:
% if 'TiledGame' in game['serverParentClasses']: #// then we need to add some client side utility functions
% if obj_key == 'Game':
${shared['py']['function_top']('get_tile_at', {
    'description': 'Gets the Tile at a specified (x, y) position.',
    'arguments': [
        {
            'name': 'x',
            'description': 'An integer between 0 and the map_width.',
            'type': { 'name': 'int' }
        },
        {
            'name': 'y',
            'description': 'An integer between 0 and the map_height.',
            'type': { 'name': 'int' }
        }
    ],
    'returns': {
        'description': 'The Tile at (x, y) or None if out of bounds.',
        'type': {
            'name': 'Tile',
            'is_game_object': True,
            'nullable': True
        }
    }
})}
        if x < 0 or y < 0 or x >= self.map_width or y >= self.map_height:
            # out of bounds
            return None

        return self.tiles[x + y * self.map_width]
% elif obj_key == 'Tile':
    directions = ["North", "East", "South", "West"]
    """int: The valid directions that tiles can be in, "North", "East", "South", or "West"
    """

${shared['py']['function_top']('get_neighbors', {
    'description': 'Gets the neighbors of this Tile',
    'returns': {
        'description': 'The list of neighboring Tiles of this Tile.',
        'type': {
            'name': 'list',
            'valueType': {
                'name': 'Tile',
                'is_game_object': True,
            },
        }
    }
})}
        neighbors = []

        for direction in Tile.directions:
            neighbor = getattr(self, "tile_" + direction.lower())
            if neighbor:
                neighbors.append(neighbor)

        return neighbors

${shared['py']['function_top']('is_pathable', {
    'description': 'Checks if a Tile is pathable to units',
    'returns': {
        'description': 'True if pathable, False otherwise.',
        'type': { 'name': 'boolean' }
    }
})}
${merge("        # ", "is_pathable_builtin", "        return False # DEVELOPER ADD LOGIC HERE")}

${shared['py']['function_top']('has_neighbor', {
    'description': 'Checks if this Tile has a specific neighboring Tile.',
    'arguments': [
        {
            'name': 'tile',
            'description': 'The Tile to check against.',
            'type': {
                'name': 'Tile',
                'is_game_object': True
            }
        }
    ],
    'returns': {
        'description': 'True if the tile is a neighbor of this Tile, False otherwise',
        'type': { 'name': 'boolean' }
    }
})}
        return bool(tile and tile in self.get_neighbors())
% endif
% endif

% endif
${merge("    # ", "functions", "    # if you want to add any client side logic (such as state checking functions) this is where you can add them", optional=True)}
