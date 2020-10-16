from processing import *
from fonctions import *


dx = 125
dy = 400
mX = 1
mY = 1

def draw():
  global dx
  global dy
  global mX
  global mY
  setup()
  raquette()
  
  balleMovement(dx, dy)
  
  brique(90, 30)
  brique(90, 130)
  brique(90, 230)
  
  dx += mX
  dy += mY
  
  if rebondirX(dx) == 1:
    mX = 1
  elif rebondirX(dx) == 2:
    mX = -1
    
  if rebondirY(dy) == 1:
    mY = 1
  elif rebondirY(dy) == 2:
    mY = -1

run()
