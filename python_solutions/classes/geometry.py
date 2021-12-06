class Point:
  x = 0
  y = 0

  def __init__(self, x = 0, y = 0):
      self.x = x
      self.y = y

class Line:
  p1 = Point()
  p2 = Point()
  notDiagonal = True

  def __init__(self, p1, p2):
      self.p1 = p1
      self.p2 = p2
      self.notDiagonal = p1.x == p2.x or p1.y == p2.y
    
  def getHighestVal(self):
    allVals = [self.p1.x, self.p1.y, self.p2.x, self.p2.y]
    return max(allVals)

  def getLine(self):
    retVal = []

    if self.p1.x == self.p2.x:
      minYVal = min([self.p1.y, self.p2.y])
      maxYVal = max([self.p1.y, self.p2.y])      
      for y in range(minYVal, maxYVal+1):
        retVal.append([self.p1.x, y])
    elif self.p1.y == self.p2.y:
      minXVal = min([self.p1.x, self.p2.x])
      maxXVal = max([self.p1.x, self.p2.x])
      for x in range(minXVal, maxXVal+1):
        retVal.append([x, self.p1.y])
    else:
      #For Diagonals
      xFactor = 1 if self.p1.x < self.p2.x else -1
      yFactor = 1 if self.p1.y < self.p2.y else -1

      for i in range(abs(self.p1.x - self.p2.x) + 1):
        retVal.append([self.p1.x + (i * xFactor), self.p1.y + (i * yFactor)])
    return retVal

  def prettyPrint(self):
    print(f"(Line) {self.p1.x},{self.p1.y} => {self.p2.x},{self.p2.y}")