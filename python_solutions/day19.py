
def rotate(x, y, z):
  retVal = []
  retVal.append((x,y,z))
  retVal.append((x,z,-1*y))
  retVal.append((x,-1*y,-1*z))
  retVal.append((x,-1*z,y))

  return retVal

def findPermutations(tuples):
  retVal = []

  for tuple in tuples:
    origX, origY, origZ = tuple
    
    # face right (x) and rotate
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

    # face back (-z) and rotate
    x = origZ
    z = origX * -1
    points = rotate(x,y,z)
    if len(retVal) < 5:
      retVal = retVal + [[p] for p in points]
    else:
      retVal[4].append(points[0])
      retVal[5].append(points[1])
      retVal[6].append(points[2])
      retVal[7].append(points[3])

    # face left (-x) and rotate
    x = origX * -1
    z = origZ * -1
    points = rotate(x,y,z)
    if len(retVal) < 9:
      retVal = retVal + [[p] for p in points]
    else:
      retVal[8].append(points[0])
      retVal[9].append(points[1])
      retVal[10].append(points[2])
      retVal[11].append(points[3])

    #face front (z) and rotate
    x = origZ * -1
    z = origX
    points = rotate(x,y,z)
    if len(retVal) < 13:
      retVal = retVal + [[p] for p in points]
    else:
      retVal[12].append(points[0])
      retVal[13].append(points[1])
      retVal[14].append(points[2])
      retVal[15].append(points[3])

    #face up (y) and rotate
    x = origY
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

    #face down (-y) and rotate
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

input = [(-1,-1,1), (-2,-2,2), (-3,-3,3), (-2,-3,1), (5,6,-4), (8,0,7)]
allPerms = findPermutations(input)

for perm in allPerms:
  print(perm)