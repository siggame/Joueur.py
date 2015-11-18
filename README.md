# Anarchy Python 3 Client

This is the root of you AI. Stay out of the joueur/ folder, it does most of the heavy lifting to play on our game servers. Your AI, and the game objects it manipulates are all in `games/anarchy/`, with your very own AI living in `games/anarchy/ai.py` for you to make smarter.

## How to Run

This client has been tested and confirmed to work on the Campus rc##xcs213 Linux machines, but it can work on your own Windows/Linux/Mac machines if you desire.

### Linux

```
./testRun MyOwnGameSession
```

For Linux a recent version of python3 should work. It has been tested on 3.4.3 extensively, but would work with <= 3.2. The normal 'python' usually refers to Python 2.7.X, so make sure you have the python**3** installed.

### Windows

On Windows you'll need some version of Python 3. As of this version [3.4.3](https://www.python.org/downloads/release/python-343/) worked fine. Install that and ensure that python us set up in your Environmental Variables as 'python', then

```
python main.py Anarchy -s r99acm.device.mst.edu -r MyOwnGameSession
```

#### Make

There is a make file provided, but it is empty as python is an intepreted language. If you want to add make steps feel free to, but you may want to check with an Arena dev to make sure the Arena has the packages you need to use in make.
