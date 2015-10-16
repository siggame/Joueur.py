# Joueur.py
A simple python game client for the Cadre framework to connect to [Cerveau](https://github.com/JacobFischer/Cerveau) servers.

![{Cadre}](http://i.imgur.com/17wwI3f.png)

All inspiration taken from [MST's SIG-GAME framework](https://github.com/siggame), and most of the terminology is assuming some familiarity with it as this is a spiritual successor to it.

## Features

* Multi-Game:
  * One client can have multiple AIs to play different games.
* Easy generation of new game AIs using the [Creer](https://github.com/JacobFischer/Creer) codegen
* No game specific logic. All logic is done server side. Here on clients we just merge deltas into the game state.
* Generated game classes are slim and can be extended by coders without breaking client server communication.
* PEP-8: although the server is written using `camelCase`, PEP-8 reccomends using `variables_with_underscores` instead. The client will automatically convert camel case to underscores to appease Python purists.
* Args to game objects can be kwargs if that's your thing.
* Networking via basic TCP sockets
  * Communication via json strings with support for cycles within game references
  * Only deltas in states are send over the network

## How to Run

You just need python 3.

### Windows

On Windows you'll need some version of Python 3. As of this version [3.4.3](https://www.python.org/downloads/release/python-343/) worked fine. Install that and ensure that python us set up in your Environmental Variables as 'python', then

```
python main.py GAME_NAME -s SERVER -p PORT
```

### Linux

For Linux and recent version of python3 should work. The normal 'python' usually refers to Python 2.7.X, so make sure you have the python**3** installed, then:

```
./run GAME_GAME -s SERVER -p PORT
```

or `python main.py --help` for help on how to run.
