def readFile(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]    
    return lines

# Checks if values in list A are contained in values of list B
def listContains(A, B):
    return all(item in A for item in B)