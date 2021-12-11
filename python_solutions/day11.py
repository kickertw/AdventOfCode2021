from utils import *

def isValidCoordinate(x, y, mapWidth, mapHeight):
  return x >= 0 and y >= 0 and x < mapWidth and y < mapHeight

def countAdjacentFlashes(x, y, mapWidth, mapHeight, octoMap):
  tl = 1 if y > 0 and x > 0 and octoMap[y-1][x-1] == 0 else 0
  t = 1 if y > 0 and octoMap[y-1][x] == 0 else 0
  tr = 1 if y > 0 and x < mapWidth - 1 and octoMap[y-1][x+1] == 0 else 0
  l = 1 if x > 0 and octoMap[y][x-1] == 0 else 0
  r = 1 if x < mapWidth - 1 and octoMap[y][x+1] == 0 else 0
  bl = 1 if y < mapHeight - 1 and x > 0 and octoMap[y+1][x-1] == 0 else 0
  b = 1 if y < mapHeight - 1 and octoMap[y+1][x] == 0 else 0
  br = 1 if y < mapHeight - 1 and x < mapWidth - 1 and octoMap[y+1][x+1] == 0 else 0
  return tl + t + tr + l + r + bl + b + br

def incrementOctopus(x, y, mapWidth, mapHeight, octoMap, newFlashList):
  if isValidCoordinate(x, y, mapWidth, mapHeight) and octoMap[y][x] > 0:
    if octoMap[y][x] < 9:
      octoMap[y][x] += 1
    else:
      octoMap[y][x] = 0
      newFlashList.append((y, x))

def incrementFromFlash(newFlashes, octoMap, mapWidth, mapHeight):
  newFlashList = []
  for flash in newFlashes:
    y, x = flash
    incrementOctopus(x-1, y-1, mapWidth, mapHeight, octoMap, newFlashList)
    incrementOctopus(x, y-1, mapWidth, mapHeight, octoMap, newFlashList)
    incrementOctopus(x+1, y-1, mapWidth, mapHeight, octoMap, newFlashList)
    incrementOctopus(x-1, y, mapWidth, mapHeight, octoMap, newFlashList)
    incrementOctopus(x+1, y, mapWidth, mapHeight, octoMap, newFlashList)
    incrementOctopus(x-1, y+1, mapWidth, mapHeight, octoMap, newFlashList)
    incrementOctopus(x, y+1, mapWidth, mapHeight, octoMap, newFlashList)
    incrementOctopus(x+1, y+1, mapWidth, mapHeight, octoMap, newFlashList)
  return newFlashList

rawInputs = readFile('./inputs/day11.txt')

# Create int grid
octoMap = []
for row in rawInputs:
  octoMap.append([int(x) for x in row])

steps = 1000
flashCount = 0
for ii in range(steps):
  tempMap = []

  # Increase energy lvl by 1
  yy = 0
  newFlashList= []
  for row in octoMap:
    newRow = list(map(lambda x: x+1 if x < 9 else 0, row))
    tempMap.append(newRow)
    if any(x == 0 for x in newRow):
      for xx, octo in enumerate(newRow):
        if octo == 0:
          newFlashList.append((yy, xx))
    yy += 1

  # Increase energy based on adjacent flashes
  mapHeight = len(octoMap)
  mapWidth = len(octoMap[0])
  while len(newFlashList) > 0:
    # for row in tempMap:
    #   print(''.join([str(i) for i in row]))
    # print('')
    newFlashList = incrementFromFlash(newFlashList, tempMap, mapWidth, mapHeight)

  tempSum = sum(map(sum, tempMap))
  flashCount += sum(x.count(0) for x in tempMap)

  if ii == 99:
    print(f'Part 1 = {flashCount}')
  elif tempSum == 0:
    print(f'Part 2 = {ii + 1}')
    break
  octoMap = tempMap