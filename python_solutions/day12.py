from utils import *

def getPermutations(startList, caveSystem, usedList = [], mulligan = False):
  retVal = []
  start = startList[-1]

  if ((start not in caveSystem or start in usedList) and not mulligan) or start == 'end':
    return [startList]

  newUsedList = usedList.copy()

  # If it's lowercase, we can't go there anymore
  if start.islower():
    if start in newUsedList:
      mulligan = False
    
    if start not in newUsedList:
      newUsedList.append(start)

  children = caveSystem[start]
  for child in children:
    newList = startList.copy()    
    newCaveSystem = caveSystem.copy()    
    newList.append(child)

    perms = getPermutations(newList, newCaveSystem, newUsedList, mulligan)
    for perm in perms:
      retVal.append(perm)
    
  return retVal

rawInputs = readFile('./inputs/day12.txt')

caveSystem = {'start': []}

for input in rawInputs:
  conn = input.split('-')
  
  if conn[1] != 'start':
    if conn[0] not in caveSystem:
      caveSystem[conn[0]] = [conn[1]]
    else:
      caveSystem[conn[0]].append(conn[1])

  if conn[0] != 'start':
    if conn[1] not in caveSystem:
      caveSystem[conn[1]] = [conn[0]]
    else:
      caveSystem[conn[1]].append(conn[0])

allRoutes = getPermutations(['start'], caveSystem)
allValidRoutes = [route for route in allRoutes if 'end' in route ]
print(f"Part 1 = {len(allValidRoutes)}")

allRoutes = getPermutations(['start'], caveSystem, mulligan=True)
allValidRoutes = [route for route in allRoutes if 'end' in route ]
print(f"Part 2 = {len(allValidRoutes)}")