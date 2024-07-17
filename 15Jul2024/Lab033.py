# Python program to interchange first and last elements in a list

list_1 = [3,6.1,89,32,"t","y"]

a = list_1[0]
list_1[0]=list_1[-1]
list_1[-1]=a

print(list_1)
