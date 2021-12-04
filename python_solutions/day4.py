from utils import *

def isInBoard(board, inputs):
  currentInput = inputs[-1]
  for row in board:
      if currentInput in row:
        # Check the row
        if listContains(inputs, row):
          return True
        
        # Check the column
        colIdx = row.index(currentInput)
        rotatedBoard = list(zip(*board[::-1]))
        if listContains(inputs, rotatedBoard[colIdx]):
          return True

rawInputs = readFile('../inputs/day4.txt')

# Part 1
# read bingo inputs
bingoInputs = list(map(int, rawInputs[0].split(','))) 

# create bingo boards
bingoBoards = []
tempBoard = []
for input in rawInputs[2:]:
  if len(input) > 0:
    tempBoard.append(list(map(int, input.split())))
  else:
    bingoBoards.append(tempBoard)
    tempBoard = []
bingoBoards.append(tempBoard)

# Find the first winning board
ii = 4
boardId = 0
foundBoardId = -1
searchedInputs = []
while foundBoardId < 0:
  searchedInputs = bingoInputs[0:ii]
  for board in bingoBoards:
    if isInBoard(board, searchedInputs):
      foundBoardId = boardId
      continue
    boardId += 1
  
  boardId = 0
  ii += 1

# calculate the score of the winning board
winningBoard = bingoBoards[foundBoardId]
unmarkedSum = 0;
for row in winningBoard:
  for value in row:
    if value not in searchedInputs:
      unmarkedSum += value
print('Part 1 = {} * {} = {}'.format(unmarkedSum, searchedInputs[-1], unmarkedSum * searchedInputs[-1]))