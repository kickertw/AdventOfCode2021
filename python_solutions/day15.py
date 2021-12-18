import sys
from utils import *
from collections import defaultdict

def getChildren(riskMap, currentX, currentY):
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

  return children

def getNextUnvisited(spTree, unvisited):
  retVal = ''
  minWeight = 1000001
  for node in unvisited:
    if spTree[node][0] < minWeight:
      minWeight = spTree[node][0]
      retVal = node

  return retVal

def runDijkstras(riskMap):
  visited = set()
  unvisited = {'0,0'}

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
    children = getChildren(riskMap, int(nodeXY[0]), int(nodeXY[1]))    

    for node in children:
      (cnodeX, cnodeY, weight) = node
      weight += spTree[currentNode][0]
      key = f'{cnodeX},{cnodeY}'

      if key not in visited:
        spTree[key] = (weight, currentNode) if weight < spTree[key][0] else spTree[key]
      
    visited.add(currentNode)
    unvisited.remove(currentNode)
    if len(unvisited) > 0:
      currentNode = getNextUnvisited(spTree, unvisited)
  
  return spTree

rawInputs = readFile('./inputs/day15.txt')

riskMap = []
for input in rawInputs:
  riskMap.append([int(i) for i in input])

spTree = runDijkstras(riskMap)
print(spTree['99,99'])