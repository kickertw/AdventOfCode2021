from utils import *

def isLowest(currentVal, adjacentVals):
    for val in adjacentVals:
        if val <= currentVal:
            return False
    return True

def findBasinSize(rowIdx, colIdx, heightMap):
    if heightMap[rowIdx][colIdx] == -1:
        return 0

    # count 1 for size, and then set it to -1
    # -1 = spot has already been marked
    retVal = 1 if heightMap[rowIdx][colIdx] < 9 else 0
    heightMap[rowIdx][colIdx] = -1

    mapHeight = len(heightMap)
    mapWidth = len(heightMap[0])
    left = 9 if colIdx == 0 else heightMap[rowIdx][colIdx - 1] 
    right = 9 if colIdx == mapWidth - 1 else heightMap[rowIdx][colIdx +  1]
    up = 9 if rowIdx == 0 else heightMap[rowIdx - 1][colIdx]
    down = 9 if rowIdx == mapHeight - 1 else heightMap[rowIdx + 1][colIdx]

    retVal += 0 if left in [-1, 9] else findBasinSize(rowIdx, colIdx - 1, heightMap)
    retVal += 0 if right in [-1, 9] else findBasinSize(rowIdx, colIdx + 1, heightMap)
    retVal += 0 if up in [-1, 9] else findBasinSize(rowIdx - 1, colIdx, heightMap)
    retVal += 0 if down in [-1, 9] else findBasinSize(rowIdx + 1, colIdx, heightMap)

    return retVal

rawInputs = readFile('./inputs/day9.txt')

heightMap = []
for rawInput in rawInputs:
    rawInts = [int(i) for i in rawInput]
    heightMap.append(rawInts)

riskLevel = 0
mapHeight = len(heightMap)
mapWidth = len(heightMap[0])
sinkLocation = []
for rowIdx in range(mapHeight):
    for colIdx in range(mapWidth):
        adjacentVals = []
        # left
        adjacentVals.append(9 if colIdx == 0 else heightMap[rowIdx][colIdx - 1])
        
        # right
        adjacentVals.append(9 if colIdx == mapWidth - 1 else heightMap[rowIdx][colIdx +  1])
        
        # up
        adjacentVals.append(9 if rowIdx == 0 else heightMap[rowIdx - 1][colIdx])

        # down
        adjacentVals.append(9 if rowIdx == mapHeight - 1 else heightMap[rowIdx + 1][colIdx])

        if isLowest(heightMap[rowIdx][colIdx], adjacentVals):
            sinkLocation.append([rowIdx, colIdx])
            riskLevel += heightMap[rowIdx][colIdx] + 1

basinSizes = []
for location in sinkLocation:
    size = findBasinSize(location[0], location[1], heightMap)
    print(f"({location[0]},{location[1]}) has size {size}")
    basinSizes.append(size)

basinSizes.sort()
p2Answer = basinSizes[-3] * basinSizes[-2] * basinSizes[-1]


print(f'Part 1 = {riskLevel}')
print(f'Part 2 = {p2Answer}')