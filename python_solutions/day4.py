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

def playBingo(boards, inputs, boardIdsToSkip = [], ii = 4):
  boardId = 0
  newWinningBoardIds = []
  searchedInputs = []
  while len(newWinningBoardIds) == 0:
    searchedInputs = inputs[0:ii]
    for board in boards:      
      if boardId not in boardIdsToSkip and isInBoard(board, searchedInputs):
        if boardId not in newWinningBoardIds:
          newWinningBoardIds.append(boardId)
          boardIdsToSkip.append(boardId)
          print(f"BoardID {boardId} got BINGO on number {searchedInputs[-1]}")
        if len(boardIdsToSkip) == 0:
          continue
      boardId += 1
    
    boardId = 0
    ii += 1
  
  return newWinningBoardIds, searchedInputs

def calcUnmarkedSum(winningBoard, searchedInputs):
  unmarkedSum = 0
  print(winningBoard)
  print(searchedInputs)
  for row in winningBoard:
    unmarkedSum += sum([val for val in row if val not in searchedInputs])
  return unmarkedSum

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
winningBoardIds, searchedInputs = playBingo(bingoBoards, bingoInputs)

# calculate the score of the winning board
winningBoard = bingoBoards[winningBoardIds[0]]
unmarkedSum = calcUnmarkedSum(winningBoard, searchedInputs)
print('Part 1 = {} * {} = {}'.format(unmarkedSum, searchedInputs[-1], unmarkedSum * searchedInputs[-1]))

# Part 2
while len(winningBoardIds) < len(bingoBoards):
  justWonIds, searchedInputs = playBingo(bingoBoards, bingoInputs, winningBoardIds, len(searchedInputs)-1)
  winningBoardIds.extend(justWonIds)
  # can't quite figure out where I'm duplicating effort, so this strips out dupes
  tempList = []
  [tempList.append(x) for x in winningBoardIds if x not in tempList]
  winningBoardIds = tempList

print(winningBoardIds)
unmarkedSum = calcUnmarkedSum(bingoBoards[winningBoardIds[-1]], searchedInputs)
print('Part 2 = {} * {} = {}'.format(unmarkedSum, searchedInputs[-1], unmarkedSum * searchedInputs[-1]))