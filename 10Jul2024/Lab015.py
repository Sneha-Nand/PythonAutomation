#string functions

# count - It count the ocurances in a strig and return the count
text = "Hello my friends"
count = text.count("l")
print(count)

# lower - Returns all characters in lower case
text_lower = text.lower()
print(text_lower)

# upper - Returns all characters in upper case
text_upper = text.upper()
print(text_upper)

# endswith - This method return True if the specified value is found at end
a = text.endswith("s")
print(a)
b = text.endswith("d")
print(b)

# statswith - This method return True if the specified value is found at start
a = text.startswith("s")
print(a)
b = text.startswith("H")
print(b)

# capitalize - Makes first character Caps and rest all in small
text1 = "hEllo My FRiends and welcome"
cap1 = text1.capitalize()
print(cap1)


#center - It will center allign the string using a specied character (space) as the fill character

txt ='Python'
s=txt.center(10,"#")
print(s)

# replaces - It replcases old character with new value. It will require 2 args
text2 = "Heloo my friends"
s = text2.replace("H","D")
print(s)

#format():-The format() method formats the specified value(s) and insert them inside the string's placeholder.
#the placeholder is defined using curly brackets: {}.

#named Index
txt1 = "My name is {name},I am {age}".format(name="sneha",age=10)
print(txt1)

# Number index
txt2 = "My name is {0} , Iam {1}".format("Sneha",20)
print(txt2)

# Empty placeholder
txt3 = "My name is {}, I am {}".format("Sne",21)
print(txt3)

#isalnum():--returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
str = "Python123"
b=str.isalnum()
print(b)

str1 = "Python123##"
c=str1.isalnum()
print(c)

str2 = "Python 123"
d = str2.isalnum()
print(d)

#istitle - :-- returns True if all words in a text start with a upper case letter,
# AND the rest of the word are lower case letters, otherwise False

str3 = "Python"
a1 =str3.istitle()
print(a1)

str4 = "Python@123"
a2 = str4.istitle()
print(a2)

str5 = "python@123"
a3 = str4.istitle()
print(a3)