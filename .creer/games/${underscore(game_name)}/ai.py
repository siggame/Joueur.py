# This is where you build your AI for the ${game_name} game.
<%include file="functions.noCreer" /><%
typing_import = shared['py']['get_imports'](
    ai,
    { 'List' } if 'TiledGame' in game['serverParentClasses'] else None
)
if typing_import:
    typing_import += '\n'
%>
${typing_import}from joueur.base_ai import BaseAI

${merge("# ", "imports", "# you can add additional import(s) here", optional=True)}

class AI(BaseAI):
    """ The AI you add and improve code inside to play ${game_name}. """

${shared['py']['function_top']('game', {
    'description': 'The reference to the Game instance this AI is playing.',
    'type': {
        'name': 'Game',
        'is_game_object': True
    }
}, is_property=True)}
        return self._game # don't directly touch this "private" variable pls

${shared['py']['function_top']('player', {
    'description': 'The reference to the Player this AI controls in the Game.',
    'type': {
        'name': 'Player',
        'is_game_object': True
    }
}, is_property=True)}
        return self._player # don't directly touch this "private" variable pls

${shared['py']['function_top']('get_name', {
    'description': 'This is the name you send to the server so your AI will control the player named this string.',
    'returns': {
        'description': 'The name of your Player.',
        'type': { 'name': 'string' }
    }
})}
${merge("        # ", "get-name", '        return "' + game_name + ' Python Player" # REPLACE THIS WITH YOUR TEAM NAME')}

${shared['py']['function_top']('start', {
    'description': 'This is called once the game starts and your AI knows its player and game. You can initialize your AI here.',
    'returns': None
})}
${merge("        # ", "start", "        # replace with your start logic")}

${shared['py']['function_top']('game_updated', {
    'description': 'This is called every time the game\'s state updates, so if you are tracking anything you can update it here.',
    'returns': None
})}
${merge("        # ", "game-updated", "        # replace with your game updated logic")}

${shared['py']['function_top']('end', {
    'description': 'This is called when the game ends, you can clean up your data and dump files here if need be.',
    'arguments': [
        {
            'name': 'won',
            'description': 'True means you won, False means you lost.',
            'type': { 'name': 'boolean' }
        },
        {
            'name': 'reason',
            'description': 'The human readable string explaining why your AI won or lost.',
            'type': { 'name': 'string' }
        }
    ],
    'returns': None
})}
${merge("        # ", "end", "        # replace with your end logic")}
% for function_name in ai['function_names']:
<% function_parms = ai['functions'][function_name]
%>${shared['py']['function_top'](function_name, function_parms)}
${merge("        # ", function_name,
"""        # Put your game logic here for {0}
        return {1}
""".format(function_name, shared['py']['default'](function_parms['returns']['type'], function_parms['returns']['default']) if function_parms['returns'] else "")
)}
% endfor

% if 'TiledGame' in game['serverParentClasses']: # then we need to add some client side utility functions
${shared['py']['function_top']('find_path', {
    'description': 'A very basic path finding algorithm (Breadth First Search) that when given a starting Tile, will return a valid path to the goal Tile.',
    'arguments': [
        {
            'name': 'start',
            'description': 'The starting Tile to find a path from.',
            'type': { 'name': 'Tile', 'is_game_object': True }
        },
        {
            'name': 'goal',
            'description': 'The goal (destination) Tile to find a path to.',
            'type': { 'name': 'Tile', 'is_game_object': True }
        }
    ],
    'returns': {
        'description': 'A list of Tiles representing the path, the the first element being a valid adjacent Tile to the start, and the last element being the goal.',
        'type': {
            'name': 'list',
            'valueType': {
                'name': 'Tile',
                'is_game_object': True
            }
        }
    }
})}

        if start == goal:
            # no need to make a path to here...
            return []

        # queue of the tiles that will have their neighbors searched for 'goal'
        fringe = []

        # How we got to each tile that went into the fringe.
        came_from = {}

        # Enqueue start as the first tile to have its neighbors searched.
        fringe.append(start)

        # keep exploring neighbors of neighbors... until there are no more.
        while len(fringe) > 0:
            # the tile we are currently exploring.
            inspect = fringe.pop(0)

            # cycle through the tile's neighbors.
            for neighbor in inspect.get_neighbors():
                # if we found the goal, we have the path!
                if neighbor == goal:
                    # Follow the path backward to the start from the goal and
                    # # return it.
                    path = [goal]

                    # Starting at the tile we are currently at, insert them
                    # retracing our steps till we get to the starting tile
                    while inspect != start:
                        path.insert(0, inspect)
                        inspect = came_from[inspect.id]
                    return path
                # else we did not find the goal, so enqueue this tile's
                # neighbors to be inspected

                # if the tile exists, has not been explored or added to the
                # fringe yet, and it is pathable
                if neighbor and neighbor.id not in came_from and (
                    neighbor.is_pathable()
                ):
                    # add it to the tiles to be explored and add where it came
                    # from for path reconstruction.
                    fringe.append(neighbor)
                    came_from[neighbor.id] = inspect

        # if you're here, that means that there was not a path to get to where
        # you want to go; in that case, we'll just return an empty path.
        return []

% endif
${merge("    # ", "functions", "    # if you need additional functions for your AI you can add them here", optional=True)}
