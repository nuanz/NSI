from processing import * 

def setup():
  background(255,248,220)
  size(250, 600)
  
def raquette():
  fill(255, 255, 255)
  rect(mouseX-27.5, 500, 55, 25, 7)
  
def balleMovement(dx, dy):
  balle(dx, dy)

def rebondirX(val):
  if val == 0:
    return 1
  elif val == 250:
    return 2
  else:
    return 0
    
def rebondirY(val):
  if val == 0:
    return 1
  elif val == 600:
    return 2
  else:
    return 0
    
def balle(x, y):
  fill(128,0,0)
  ellipse(x, y, 10, 10)
  
def brique(x, y):
  fill(210,105,30)
  rect(x, y, 70, 70, 7)
  
