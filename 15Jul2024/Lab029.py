# find the greateest number from 3 numbers

a = int(input(("Enter number1")))
b = int(input("Enter number 2"))
c = int(input("Enter number 3"))

if a > b > c:
    print(a ," is greater")
elif b > a > c:
    print(b,"is greater")
else:
    print(c,"is greater")