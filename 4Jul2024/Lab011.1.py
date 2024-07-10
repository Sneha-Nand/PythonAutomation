# Strings

s = "Durga Goddess"

print(s[0])
print(s[5])
print(s[12])
print(s[-1])
print(s[-7])
print(s[-8])
print(s[-9])

# Methods os string - Length of string
print("Length of a string", len(s))

# find the location of a particular charatcter and it will return the first index value / location of character
a = s.find('s')
print(a)

b = s.find('z')  # If element is not found it will return -1
print(b)

# Join of two strings
c = "Automation" # When and where it is used
d = "Python"
e = "Test".join(d)
print(e)

# strip function - it is used to remove white spaces at the beginning and the end of the sting
t = "  Welcome to the class  "
print(t.strip())
print(t.strip(s))
print(t.strip('a'))

# split method splits a string into list
t = "  Welcome to the class  "
x = t.split()
print(x)

# zfill - The zfill() method adds zeros (0) at the beginning of the string,
# until it reaches the specified length.
# If the value of the len parameter is less than the length of the string, no filling is done.
a ='Hello'
print(a.zfill(10))
print(a.zfill(7))

