def readFile(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]    
    return lines

# Checks if values in list A are contained in values of list B
def listContains(A, B):
    set1 = set(A)
    set2 = set(B)
    return set1.issubset(set2)


# Returns the values not contained in either list
def listDiff(li1, li2):
    return list(set(li1) - set(li2)) + list(set(li2) - set(li1))

def init2DList(size):
  return [[0] * (size) for _ in range(size)]

def getIndexByVal(list, val):
    try:
        return list.index(val)
    except ValueError:
        return -1

def convertHexToBin(input):
  h_size = len(input) * 4
  return (bin(int(input, 16))[2:]).zfill(h_size)

def convertBinToDec(input):
  return int(input,2)

def debugPrint(debugOn = False, printVal = ''):
  if debugOn:
    print(printVal)