

# Driver code
newList = [12, 35, 9, 56, 24]

first = newList.pop(0)
last = newList.pop(-1)

newList.insert(0, last)
newList.append(first)


print((newList))