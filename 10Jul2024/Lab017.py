str1 = "Sneha"
print(id(str1))

str1 = "Sneha"
print(id(str1))

print("Both are mutable")

# Mutable objects:
# Can be modified after creation.
# Operations on the object can change its state or content without creating a new object.
# Examples: lists, dictionaries, sets.

# Immutable objects:
# Cannot be modified after creation.
# Any operation that appears to modify the object actually creates a new object with the modified value.
# Examples: integers, floats, strings, tuples.

# Mutable object - Changable (list)
my_list = [1, 2, 3]
my_list[0] = 10
print(my_list)  # Output: [10, 2, 3]

# Immutable object (string)
my_string = "hello"
my_string[0] = "H"  # This will raise an error