# Strings
# Strings are sequences of characters
#In Python, you can define strings using either single quotes (''), double quotes ("") or triple quotes (''' or """) for multiline strings

s = 'Hello world'
s1 = "Hello Python"
s2 = "Hello Sneha"

print(s)
print(s1)
print(s2)

# specify path or raw strings
print(r'C:\Users\sneha.nandvadekar\Downloads\Doc')

# length of a string
str = "I am Batman"
print(len(str))

# length of string
str1 = "IamBatman"
print(len(str1))

# Indexing and Reverse Indexing
# A string in Python is indexed from 0 to n-1 where n is its length.

string1 = "Bruce Wayne" # 0 - 10 -- n=length=11

# Accessing the first character in the string
first_char = string1[0]
print(first_char)

# Accessing the empty space in the string
empty_space = string1[5]
print(empty_space)

# Accessing the last char in the string
last_char = string1[10]
print(last_char)

# length of a string

# # if we try to use length =10 - it wiil be string out of index
# len_char_err = string1(10)
# print(len_char_err)  # TypeError: 'str' object is not callable

len = len(string1)
print(len)

batman = "Bruce Wayne"
print(batman[-1])  # Corresponds to batman[10]
print(batman[-5])  # Corresponds to batman[6]