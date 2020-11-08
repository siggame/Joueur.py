from typing import List
from enum import Enum

class STATE(Enum):
  IDLE = 0
  MOVE = 1
  MINE = 2

class Robot:

  def __init__(self, miner):
    self.miner = miner
    self.goalPos = None
    self.state = STATE.IDLE
  
  def moveToward(self, goal):
    path = self.getPath(self.miner.tile, goal)
    while path and self.miner.moves > 0:

      # get next path tile
      nextPos = path.pop(0)

      # Place ladder/support if needed
      if nextPos == self.miner.tile.tile_north or nextPos == self.miner.tile.tile_south:
        self.miner.build(self.miner.tile, 'ladder')
      elif nextPos == self.miner.tile.tile_east or nextPos == self.miner.tile.tile_east:
        self.miner.build(self.miner.tile, 'support')

      # Mine if needed
      if nextPos.ore + nextPos.dirt > 0:
        self.miner.mine(nextPos, -1)
      
      

      self.miner.move(nextPos)
    self.miner.build(self.miner.tile, 'ladder')
  
  def getPath(self, start:'games.coreminer.tile.Tile', end:'games.coreminer.tile.Tile') -> List:
    
    if start == end: return [] # No need to path if we're already there!

    path = [start]

    xdiff = end.x - start.x
    ydiff = start.y - end.y

    while xdiff > 0:
      path.append(path[-1].tile_east)
      print("Tile East")
      xdiff -= 1
    while xdiff < 0:
      path.append(path[-1].tile_west)
      xdiff += 1
    
    while ydiff > 0:
      path.append(path[-1].tile_north)
      print("Tile North")
      print(ydiff)
      ydiff -= 1
    while ydiff < 0:
      path.append(path[-1].tile_south)
      ydiff += 1
    
    return path[1:]