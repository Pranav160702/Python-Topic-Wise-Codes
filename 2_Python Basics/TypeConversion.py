#Implicit Type Conversion
#Python automatically converts one data type to another if it makes sense.

#Example

# first = 10      #Integer
# second = 3.14   #Float

# result = first + second #Implicit type conversion
# print(result)           # Outputs: 13.14
# print(type(result))     # Outputs: <class 'float'> 


#====================================Explicit Conversion======================================================
# # Integer Conversion

# # Converting float to int
# x = 3.14
# int_x = int(x)
# print(int_x)        # Outputs: 3
# print(type(int_x))  # Outputs: <class 'int'>

# # Converting string to int
# y = "100"
# int_y = int(y)
# print(int_y)        # Outputs: 100
# print(type(int_y))  # Outputs: <class 'int'>

# # Converting string to int
# y = "Pranav"
# int_y = int(y)      # ValueError: invalid literal for int() with base 10: 'Pranav'


#***********************************************************************************
#float conversion

# # Converting int to float
# x = 10
# float_x = float(x)
# print(float_x)      # Outputs: 10.0
# print(type(float_x))# Outputs: <class 'float'>

# # Converting string to float
# y = "3.14"
# float_y = float(y)
# print(float_y)      # Outputs: 3.14
# print(type(float_y))# Outputs: <class 'float'>


#***********************************************************************************
#String conversion

# # Converting int to string
# x = 10
# str_x = str(x)
# print(str_x)        # Outputs: '10'
# print(type(str_x))  # Outputs: <class 'str'>

# # Converting float to string
# y = 3.14
# str_y = str(y)
# print(str_y)        # Outputs: '3.14'
# print(type(str_y))  # Outputs: <class 'str'>


#***********************************************************************************
#Boolean conversion
# # Converting int to boolean
# x = 10
# bool_x = bool(x)
# print(bool_x)       # Outputs: 'True'
# print(type(bool_x))  # Outputs: <class 'bool'>

# #Converting float to boolean
# y = 10.23
# bool_y = bool(x)
# print(bool_y)       # Outputs: 'True'
# print(type(bool_y))  # Outputs: <class 'bool'>


#***********************************************************************************
#List conversion

# # Converting string to list
# x = "hello"
# list_x = list(x)
# print(list_x)       # Outputs: ['h', 'e', 'l', 'l', 'o']
# print(type(list_x)) # Outputs: <class 'list'>

# # Converting tuple to list
# y = (1, 2, 3)
# list_y = list(y)
# print(list_y)       # Outputs: [1, 2, 3]
# print(type(list_y)) # Outputs: <class 'list'>

# # Converting set to list
# my_set = {1, 2, 3, 4, 5}
# my_list = list(my_set)
# print(my_list)        #Output: [1, 2, 3, 4, 5]
# print(type(my_list))  #Output: <class 'list'>


#**********************************************************************************************

# # Converting list to tuple
# x = [1, 2, 3]
# tuple_x = tuple(x)
# print(tuple_x)      # Outputs: (1, 2, 3)
# print(type(tuple_x))# Outputs: <class 'tuple'>

# # Converting string to tuple
# y = "hello"
# tuple_y = tuple(y)
# print(tuple_y)      # Outputs: ('h', 'e', 'l', 'l', 'o')
# print(type(tuple_y))# Outputs: <class 'tuple'>

# #Converting set to tuple
# z = {1, 2, 3}
# tuple_z = tuple(z)
# print(tuple_z)      # Outputs: (1, 2, 3)
# print(type(tuple_z))# Outputs: <class 'tuple'>

#**********************************************************************************************

# # Converting string to set
# x = "hello"
# set_x = set(x)
# print(set_x)        # Outputs: {'o', 'l', 'e', 'h'}
# print(type(set_x))  # Outputs: <class 'set'>


# # Converting list to set
# y = [1, 2, 2, 3]
# set_y = set(y)
# print(set_y)        # Outputs: {1, 2, 3}
# print(type(set_y))  # Outputs: <class 'set'>

#Converting tuple to set
# z = (1, 2, 2, 3)
# set_z = set(z)
# print(set_z)        # Outputs: {1, 2, 3}
# print(type(set_z))  # Outputs: <class 'set'>


#************************************************************************

# Scenario 1: List of tuples
list_of_tuples = [("name", "Alice"), ("age", 25), ("city", "New York")]
dict_from_list_of_tuples = dict(list_of_tuples)
print(dict_from_list_of_tuples)     #Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Scenario 2: List with an even number of elements
list_of_elements = ["name", "Alice", "age", 25, "city", "New York"]
dict_from_list_of_elements = {list_of_elements[i]: list_of_elements[i + 1] for i in range(0, len(list_of_elements), 2)}
print(dict_from_list_of_elements) #Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Scenario 3: List of lists
list_of_lists    = [["name", "Alice"], ["age", 25], ["city", "New York"]]
dict_from_list_of_lists = dict(list_of_lists)
print(dict_from_list_of_lists)    #Output: {'name': 'Alice', 'age': 25, 'city': 'New York'} 

# Scenario 4: Two lists (keys and values)
keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]
dict_from_two_lists = dict(zip(keys, values))
print(dict_from_two_lists)        #Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}
