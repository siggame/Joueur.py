# Chess Python 3 Client

This is the root of you AI. Stay out of the joueur/ folder, it does most of the heavy lifting to play on our game servers. Your AI, and the game objects it manipulates are all in `games/chess/`, with your very own AI living in `games/chess/ai.py` for you to make smarter.

## How to Run

This client has been tested and confirmed to work on the Campus rc##xcs213 Linux machines, but it can work on your own Windows/Linux/Mac machines if you desire.

### Linux

```
./testRun MyOwnGameSession
```

For Linux a recent version of `python3` should work. It has been tested on 3.4.3 extensively, but should work with >= 3.2. The normal 'python' usually refers to Python 2.7.X, so make sure you have the python**3** installed.

### Windows

On Windows you'll need some version of Python 3. As of this version [3.4.3](https://www.python.org/downloads/release/python-343/) worked fine. Install that and ensure that python is set up in your Environmental Variables as 'python3', then

```
python main.py Chess -s r99acm.device.mst.edu -r MyOwnGameSession
```

## Make

There is a `Makefile` provided, but it is empty as python is an intepreted language. If you want to add `make` steps feel free to, but you may want to check with an Arena dev to ensure the Arena has the packages you need to use in `make`.

## Other Notes

It is possible that on your Missouri S&T S-Drive this client will not run properly. This is not a fault with the client, but rather the school's S-Drive implimentation changing some file permissions during run time. We cannot control this. Instead, we recommend cloning your repo outside the S-Drive and use an SCP program like [WinSCP](https://winscp.net/eng/download.php) to edit the files in Windows using whatever IDE you want if you want to code in Windows, but compile in Linux.
