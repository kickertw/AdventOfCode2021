from utils import *
from collections import defaultdict

def getChildren(riskMap, visited, currentX, currentY):
  children = []
  #up
  if currentY - 1 >= 0:
    children.append((currentX, currentY-1, riskMap[currentY-1][currentX]))
  #down
  if currentY + 1 < len(riskMap):
    children.append((currentX, currentY+1, riskMap[currentY+1][currentX]))
  #left
  if currentX - 1 >= 0:
    children.append((currentX-1, currentY, riskMap[currentY][currentX-1]))
  #right
  if currentX + 1 < len(riskMap[0]):
    children.append((currentX+1, currentY, riskMap[currentY][currentX+1]))

  return [c for c in children if f'{c[0]},{c[1]}' not in visited]

def getNextUnvisited(touched, visited):
  allKeys = sorted(touched.keys())
  return touched[allKeys[0]][0]

# def getNextUnvisited(spTree, unvisited):
#   retVal = ''
#   minWeight = 1000001
#   for node in unvisited:
#     if spTree[node][0] < minWeight:
#       minWeight = spTree[node][0]
#       retVal = node

#   return retVal

def trackTouched(touched, node, oldWeight, newWeight):
  touched[oldWeight] = [x for x in touched[oldWeight] if x != node]
  if len(touched[oldWeight]) == 0:
    del touched[oldWeight]
  
  if newWeight in touched:
    touched[newWeight].append(node)
  else:
    touched[newWeight] = [node]

def removeFromTouched(touched, node, weight):
    # remove anything we don't care to track (i.e. - already visited)
    touched[weight].remove(node)
    
    if len(touched[weight]) == 0:
      del touched[weight]  

def runDijkstras(riskMap):
  visited = set()
  unvisited = {'0,0'}
  touched = defaultdict(list)

  # Creating 2 things
  # - list of all unvisited nodes
  # - creating a shortest path tree (the node and the shortest path to that node)
  #   - spTree key = coordinate / value = (distance/weight, previous node)
  spTree = {'0,0': (0, '')}
  for yy in range(len(riskMap)):
    for xx in range(len(riskMap[0])):
      if xx != 0 or yy != 0:
        coord = f"{xx},{yy}"
        unvisited.add(coord)
        spTree[coord] = (1000000, '')        

  currentNode = '0,0'
  while len(unvisited) > 0:
    nodeXY = currentNode.split(',')
    children = getChildren(riskMap, visited, int(nodeXY[0]), int(nodeXY[1]))    

    for node in children:
      (cnodeX, cnodeY, weight) = node
      weight += spTree[currentNode][0]
      key = f'{cnodeX},{cnodeY}'

      oldWeight = spTree[key][0]
      if weight < oldWeight:          
          spTree[key] = (weight, currentNode)
          trackTouched(touched, key, oldWeight, weight)
      
    visited.add(currentNode)
    unvisited.remove(currentNode)
   
    if len(unvisited) > 0:
      if currentNode != '0,0':
        removeFromTouched(touched, currentNode, spTree[currentNode][0])
      currentNode = getNextUnvisited(touched, visited) #getNextUnvisited(spTree, unvisited)
  
  return spTree

rawInputs = readFile('./inputs/day15.txt')

riskMap = []
for input in rawInputs:
  riskMap.append([int(i) for i in input])

spTree = runDijkstras(riskMap)
bottomRight = f'{len(riskMap)-1},{len(riskMap[0])-1}'

print(f'Part 1 = {spTree[bottomRight][0]}')