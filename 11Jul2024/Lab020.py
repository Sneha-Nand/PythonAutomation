# List - List is a dataype in python
# It is a collection of items which can be of different types
# The items are enclosed within brackets [] and separated by commas.
# It allows us to store elements of different data types in one container.
# A list is a collection of items that are ordered and changeable (mutable). It allows duplicate members.

#Creation: Lists are created by placing a comma-separated sequence of items inside square brackets [].
fruits = ['apple', 'banana', 'cherry']

fruits.insert(3, "Apple1")
print(fruits)

# List Functions

# length - len()
a =[10,20,30,40,40,50,40]
print(len(a))

# count - Return the number of items a specified item
print(a.count(40))

#index - It returns the idex of the first occurance of a specified item
print(a.index(30))

a1 =[1,2,3,4,4,5,4,5]
print(a1.index(4))

#print(a1.index(8)) # ValueError: 8 is not in list

#append - Add item at the end of the list
a1 =[1,2,3,4,4,5,4,5]
a1.append(30)
print(a1)
#print(a1.append(30))

#insert - Inserting a value at specified index
a1.insert(3,"70")
print(a1)

#extend - It add list
s1 = [1,2,3]
s2 = [4,5,6]
s1.extend(s1)
print(s1)
s1.extend(s2)
print(s1)

# Remove - remove element from particular index
a1 =[1,2,3,4,7,4,5,4,5]
a1.remove(7)
print(a1)
# a6 =[1,2,3,4,7,4,5,4,5]
# a6.remove(8)
# print(a6) #ValueError: list.remove(x): x not in list

# pop ()- Removes the item at a specific location or the last item if no index is specified

a1 =[1,2,3,4,7,4,5,4,5]
a1.pop()
print(a1)
a1.pop(1)
print(a1)

# reverse - Reverse the order of the items in the list
a1 = [34,35,36]
a1.reverse()
print(a1)

# sort - sort the items in the list in the ascending order - numbers and alphabets
a1 = [34,35,36,3,4]
a1.sort()
print(a1)

a2 = ['a','e','b','c']
a2.sort()
print(a2)

# copy - return the copy of the list
a3 = [55,56,57]
a4 = a3.copy()
print(a4)

# clear

a1 = [4,5,6]
a1.clear()
print(a1)