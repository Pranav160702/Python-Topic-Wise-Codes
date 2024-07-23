# Creating a Dictionary
# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Create a Dictionary
# Create a dictionary, and use a variable to store it:
# Create an empty dictionary
# my_dict = {}

# # Create a dictionary with some key-value pairs
# my_dict = {"name": "John", "age": 30, "city": "New York"}
# print(my_dict)

# # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# # Access a value using its key
# print(my_dict["name"])  # Output: John

# # +=======================================================
# # Access a value using the get() method (returns None if key is not found)
# print(my_dict.get("city", "Not found"))  # Output: Not found




# # Updating Values
# # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# # Update a value
# my_dict["age"] = 31
# print(my_dict)  # Output: {"name": "John", "age": 31, "city": "New York"}

# # Add a new key-value pair
# my_dict["country"] = "USA"
# print(my_dict)  # Output: {"name": "John", "age": 31, "city": "New York", "country": "USA"}


# Iterating Over Dictionary
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
my_dict = {"name": "John", "age": 30, "city": "New York"}

# Iterate over the keys
for key in my_dict:
    print(key)

# Iterate over the values
for value in my_dict.values():
    print(value)

# Iterate over the key-value pairs
for key, value in my_dict.items():
    print(f"{key}: {value}")