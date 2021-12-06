import sys
sys.path.append("./classes")

from utils import *
from classes.geometry import *
from collections import defaultdict

rawInputs = readFile('../inputs/day5.txt')

# Part 1
allVents = []
maxSize = 0
for input in rawInputs:
  si = input.split()
  p1 = [int(x) for x in si[0].split(',')]
  p2 = [int(x) for x in si[2].split(',')]  
  newLine = Line(Point(p1[0], p1[1]), Point(p2[0], p2[1]))
  maxNewLineSize = newLine.getHighestVal()
  maxSize = maxNewLineSize if maxNewLineSize > maxSize else maxSize
  allVents.append(newLine)

p1Answer = 0
p2Answer = 0

grid = defaultdict(int)
diagonals = []
for vent in allVents:
  if (vent.notDiagonal):
    for point in vent.getLine():
      grid[(point[0], point[1])] += 1
  else:
    diagonals.append(vent)

part1 = sum([1 if v > 1 else 0 for v in grid.values()])

# for vent in diagonals:
for vent in diagonals:
  for point in vent.getLine():
    grid[(point[0], point[1])] += 1

part2 = sum([1 if v > 1 else 0 for v in grid.values()])

print(f"Part 1 = {part1}")
print(f"Part 2 = {part2}")