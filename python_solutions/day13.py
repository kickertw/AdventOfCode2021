from utils import *

def drawDots(coords):
  maxX, maxY = getMaxXY(coords)
  paper = [['.']*(maxX+1) for _ in range(maxY+1)]  
  for coord in coords:
    paper[coord[1]][coord[0]] = '#'

  return paper

def getMaxXY(coords):
  maxX = 0
  maxY = 0
  for coord in coords:
    maxX = coord[0] if coord[0] > maxX else maxX
    maxY = coord[1] if coord[1] > maxY else maxY
  return maxX, maxY

def foldPaper(currentFold, coords):
  foldDir = currentFold[0]
  foldVal = int(currentFold[1])

  for ii in range(len(coords)):
    if foldDir == 'y':
      if coords[ii][1] > foldVal:
        coords[ii][1] -= (coords[ii][1] - foldVal) * 2
    else:
      if coords[ii][0] > foldVal:
        coords[ii][0] -= (coords[ii][0] - foldVal) * 2  

rawInputs = readFile('../inputs/day13.txt')

coords = []
folds = []
firstFoldDir = ''
maxX = 0
maxY = 0
for input in rawInputs:
  if len(input) > 0:
    if input.startswith('fold'):
      fold = input.split()
      foldVal = fold[2].split('=')
      folds.append([foldVal[0], foldVal[1]])
    else:
      coord = input.split(',')
      xVal = int(coord[0])
      yVal = int(coord[1])
      maxX = xVal if xVal > maxX else maxX
      maxY = yVal if yVal > maxY else maxY
      coords.append([xVal, yVal])

# First Fold
foldPaper(folds[0], coords)

# Draw everything
paper = drawDots(coords)

# P1 Count
p1Count = 0
for row in paper:
  p1Count += len([x for x in row if x == '#'])
  # print(''.join(row))

# P2 Do the rest of the folds
for ii in range(1,len(folds)):
  currentFold = folds[ii]
  foldPaper(currentFold, coords)

print(f"Part 1 = {p1Count}")

print(f"Part 2...")
paper = drawDots(coords)
for row in paper:
  print(''.join(row))