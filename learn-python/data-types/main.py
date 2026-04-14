

# Numeric Data Types
print("Numeric Data Types:")
print("int", 10)
print("float", 3.1415926)
print("complex", 1+2j)

# String Data Type
print("String Data Type:")
print("str", "Hello, World!")

print('It\'s a beautiful day')
print("It's a beautiful day") # Use double quote if there is an apostrophe in the string

print("He said", "\"Halo!\"")
print('He said,' '"Halo!"') # Use single quote if there is a double quote in the string

with_new_line = """
Hello, World!
It's a beautiful day.
"""
print(with_new_line)

# Boolean Data Type
print("Boolean Data Type:")
print("is_true", True)
print("is_false", False)

# None Data Type
print("None Data Type:")
none = None
print("none", none)

# List Data Type
# Mutable Data Type
print("List Data Type:")
example_list = [1, "iqbal", True]
print("example_list", example_list)

# Tuple Data Type
# Immutable Data Type
print("Tuple Data Type:")
example_tuple = (1, "iqbal", True)
print("example_tuple", example_tuple)

# Set Data Type
# Mutable Data Type
# Unordered
# No Duplicate
print("Set Data Type:")
example_set = {1, 2, 3, 4, 5, 5} # Duplicate will be removed
print("example_set", example_set)

# Dictionary Data Type
# Mutable Data Type
print("Dictionary Data Type:")
example_dict = {
    'name': 'Iqbal', 
    'score': 90, 
    'is_pass': True,
    'classes': ['Math', 'English'],
}
print("example_dict", example_dict)