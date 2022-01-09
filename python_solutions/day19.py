
def rotate(x, y, z):
  retVal = []
  retVal.append((x,y,z))
  retVal.append((x,-1*z,y))
  retVal.append((x,-1*y,-1*z))
  retVal.append((x,z,-1*y))

  return retVal

def findPermutations(tuples):
  retVal = []

  for tuple in tuples:
    origX, origY, origZ = tuple
    
    # face front and rotate
    x = origX
    y = origY
    z = origZ
    points = rotate(x,y,z)
    if len(retVal) == 0:
      retVal = [[p] for p in points]
    else:
      retVal[0].append(points[0])
      retVal[1].append(points[1])
      retVal[2].append(points[2])
      retVal[3].append(points[3])

    # face back and rotate
    x = origX * -1
    z = origZ * -1
    points = rotate(x,y,z)
    if len(retVal) < 5:
      retVal = retVal + [[p] for p in points]
    else:
      retVal[4].append(points[0])
      retVal[5].append(points[1])
      retVal[6].append(points[2])
      retVal[7].append(points[3])

    # face right and rotate
    x = origZ * -1
    z = origX
    points = rotate(x,y,z)
    if len(retVal) < 9:
      retVal = retVal + [[p] for p in points]
    else:
      retVal[8].append(points[0])
      retVal[9].append(points[1])
      retVal[10].append(points[2])
      retVal[11].append(points[3])

    #face left and rotate
    x = origZ
    z = origX * -1
    points = rotate(x,y,z)
    if len(retVal) < 13:
      retVal = retVal + [[p] for p in points]
    else:
      retVal[12].append(points[0])
      retVal[13].append(points[1])
      retVal[14].append(points[2])
      retVal[15].append(points[3])

    #face up and rotate
    x = origY * -1
    y = origX
    z = origZ
    points = rotate(x,y,z)
    if len(retVal) < 17:
      retVal = retVal + [[p] for p in points]
    else:
      retVal[16].append(points[0])
      retVal[17].append(points[1])
      retVal[18].append(points[2])
      retVal[19].append(points[3])

    #face down and rotate
    x = origY
    y = origX * -1
    points = rotate(x,y,z)
    if len(retVal) < 21:
      retVal = retVal + [[p] for p in points]
    else:
      retVal[20].append(points[0])
      retVal[21].append(points[1])
      retVal[22].append(points[2])
      retVal[23].append(points[3])

  return retVal

def orderScanners(scanners):
# Sorting the list of tuples using second item 
  Len = len(scanners)
  for i in range(Len):
      for j in range(0, (Len - i - 1)):
          if(scanners[j][0] > scanners[j+1][0] or 
             (scanners[j][0] == scanners[j+1][0] and scanners[j][1] > scanners[j+1][1]) or
             (scanners[j][0] == scanners[j+1][0] and scanners[j][1] == scanners[j+1][1] and scanners[j][2] > scanners[j+1][2])):
              temp = scanners[j]
              scanners[j] = scanners[j+1]
              scanners[j+1] = temp
  return scanners

def isNeighbor(scannerAList, scannerBList, minScannerOverlap = 12):
  scannerAList = orderScanners(scannerAList)
  for scanners in scannerBList:
    scanners = orderScanners(scanners)
    diffs = []
    for ii in range(len(scanners)):
      diff = (scannerAList[ii][0] - scanners[ii][0], scannerAList[ii][1] - scanners[ii][1], scannerAList[ii][2] - scanners[ii][2])
      diffs.append(diff)
    
    diffs = orderScanners(diffs)
    counter = 1
    for ii in range(len(diffs)-1):
      if (diffs[ii] == diffs[ii+1]):
        counter += 1

    if (counter >= minScannerOverlap):
      return True
  
  return False

input = [(0,2,0), (4,1,0), (3,3,0)]
input2 = [(0,-5,0), (-1,-1,0), (1,-2,0)]
scannerB = findPermutations(input2)

FoundNeighbor = isNeighbor(input, scannerB, 3)
print(FoundNeighbor)