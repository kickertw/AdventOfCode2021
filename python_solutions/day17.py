import math
from utils import *

def findMinimumHorizontalVelocity(minX):
  ii = 1
  retVal = 1
  while True:
    ii += 1
    retVal += ii
    if retVal > minX:
      return ii


def shoot(velX = 0, velY = 0, forPart2 = False):
  global minX, minY, maxX, maxY, debugOn

  maxHeight = -100
  pX, pY = 0, 0

  enteredTargetArea = False
  exitedTargetArea = False
  while not exitedTargetArea:
    pX += velX
    pY += velY
    maxHeight = pY if pY > maxHeight else maxHeight

    velX += 0 if velX == 0 else -1 if velX > 0 else 1
    velY -= 1

    if enteredTargetArea and (pX > maxX or pY < minY):
      debugPrint(debugOn, f'Got Out ({pX},{pY})')
      exitedTargetArea = True
      return maxHeight

    if not enteredTargetArea and minX <= pX <= maxX and minY <= pY <= maxY:
      debugPrint(debugOn, f'Got In ({pX},{pY})')
      enteredTargetArea = True
      if forPart2:
        return True

    if velX == 0 and pY < minY:
      debugPrint(debugOn, 'Unable to hit target :(')
      return False if forPart2 else -1

def Part1():
  global minX, maxX, minY, maxY
  velX = findMinimumHorizontalVelocity(minX)
  velY = 0
  maxHeight = -1
  hasHitTargetBefore = False
  #unableToHitTargetAgain = False
  while velY < 100:
    height = shoot(velX, velY)
    if (height > 0):
      debugPrint(debugOn, f'At velX/velY = {velX}/{velY}, height = {height}')

    maxHeight = height if height > maxHeight else maxHeight
    velY += 1

    # if not hasHitTargetBefore and height > 0:
    #   hasHitTargetBefore = True

    # if hasHitTargetBefore and height < 0:
    #   unableToHitTargetAgain = True
  print(f'Max Height = {maxHeight}')

def Part2():
  global minX, maxX, minY, maxY
  allVelocities = []

  # add coords for target area
  for ii in range(minX, maxX + 1):
    for jj in range(minY, maxY + 1):
      allVelocities.append((ii, jj))
  
  minXV = findMinimumHorizontalVelocity(minX)

  for yy in range(minY, 100):
    for xx in range(minXV, minX):
      if (xx, yy) not in allVelocities:
        if shoot(xx, yy, True):
          allVelocities.append((xx, yy))
  
  print(len(allVelocities))

# My real input = target area: x=240..292, y=-90..-57
# 240, 292, -90, -57
minX, maxX, minY, maxY = 240, 292, -90, -57 #20, 30, -10, -5
debugOn = False

Part1()
Part2()