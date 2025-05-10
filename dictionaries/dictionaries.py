# In Python 3.12, dictionaries (dict) are one of the most
# fundamental and powerful built-in data types. They allow you to store key-value pairs.
# Here('s a clear and structured explanation, covering what dictionaries are, how to use them, '
#     'common methods, and the philosophy behind their design.)

# What is a Dictionary in Python?

# A dictionary is a mutable, unordered (as of Python <3.6), key-value data structure. In Python 3.7+,
# dictionaries maintain insertion order as an implementation detail (officially guaranteed from 3.7+).

person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

#Here:

#    Keys: "name", "age", "city"

#    Values: "Alice", 30, "New York"

# Creating a Dictionary

# Using curly braces
my_dict = {"a": 1, "b": 2}

# Using the dict() constructor
my_dict_constructor = dict(a=1, b=2)

# From a list of tuples
my_dict_list_of_tuples = dict([("a", 1), ("b", 2)])

# Accessing and Modifying Values

# Accessing
print(my_dict["a"])        # Output: 1

# Safe access
print(my_dict.get("z", 0)) # Output: 0 (default if key not found)

# Modifying
my_dict["a"] = 100

# Dictionary Comprehension

squares = {x: x**2 for x in range(5)}
# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}


