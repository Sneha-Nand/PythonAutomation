
newList = [12, 35, 9, 56, 24]

def swapList(newList):
    newList[0], newList[-1] = newList[-1], newList[0]
    return newList

print(swapList(newList))