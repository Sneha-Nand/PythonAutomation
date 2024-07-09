#Add Two Integers with User Input
# 0 will take up 24 bytes whereas 1 would occupy 28 bytes

#Add Two Numbers with User Input
#In Python, the input() function is used to take user input. By default, the input() function returns data as a string.
#To get a numerical input from a user, you should convert it to an integer or float using the int() or float() function, respectively.

# Arithmetic operations
# Sum of two numbers

# # odd and even
# a = int(input("Enter number:"))
#
# if(a%2==0):
#     print("A is even")
# else:
#     print("A is odd")

# Take input from user
x = int(input("Enter number1:"))
y = int(input("Enter number2:"))

#sum = int(x) +int(y) # without using inbuilt function

#b = sum((x, y)) # tuple sum using inbuilt funtion
c = sum([x, y]) #list
print("Sum is ", c)



