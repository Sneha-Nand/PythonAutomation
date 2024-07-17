my_string = "hello"
list_1 = list(my_string)

print(list_1)
print(list_1[0])

a = list_1[-1]
list_1[-1]=list_1[0]
list_1[0]=a

print(list_1)
