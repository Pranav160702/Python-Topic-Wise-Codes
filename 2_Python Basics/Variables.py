# Rules for Naming Variables
# _variable = 5  # Valid
# 1variable = 5  # Invalid

# variable_1 = 10  # Valid
# var2 = 20  # Valid

# Variable = 100
# variable = 200
# print(variable)  # Outputs: 200
# print(Variable)  # Outputs: 100

# import keyword
# print(keyword.kwlist)  # Lists all keywords


# Python variable naming conventions
# 1. Single underscore prefix: _var (private variable)
# 2. Double underscore prefix: __var (name mangling)
# 3. Double underscore suffix: var__ (magic method)
# 4. Uppercase letters with underscores: TOTAL_COST (constants)


# ********************************************************************************************
# Integer variable
# age = 25
# print("Age:", age)

# # Float variable
# height = 5.9
# print("Height:", height)

# # String variable
# greeting = "Hello, World!"
# print(greeting)

# # Boolean variable
# is_student = True
# print("Is Student:", is_student)

# # List variable
# fruits = ["apple", "banana", "cherry"]
# print(fruits)

# # Dictionary variable
# person = {"name": "Alice", "age": 30}
# print(person)



# ********************************************************************************************
# Multiple Variables
# x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)


# ********************************************************************************************
# One Value to Multiple Variables
# x = y = z = "Orange"
# print(x)
# print(y)
# print(z)


# ********************************************************************************************
# Assign Values using Conditional Operators:
# x = 16 if 43 > 45 else 20
# y, z = (10, 20) if 5 < 10 else (20 , 10)
# print(x)
# print(y, z)


# ********************************************************************************************
# Dynamic Typing
# x = 10         # x is an integer
# print(x)

# x = "Hello"    # Now x is a string
# print(x)

# x = 3.14       # Now x is a float
# print(x)


# ********************************************************************************************
# Variable Assignment and Reassignment
# value = 100      # Integer
# print(type(value))  # <class 'int'>

# value = "Python"  # String
# print(type(value))  # <class 'str'>

# value = [1, 2, 3]  # List
# print(type(value))  # <class 'list'>

# ********************************************************************************************
# Unpack a Collection
# fruits = ["apple", "banana", "cherry"]
# x, y,z = fruits
# print(x)
# print(y)
# print(z)



# ********************************************************************************************
# The Local Variables
# def my_function():
#     local_variable = 5
#     print(local_variable)

# my_function()
# # print(local_variable)  # This would raise an error


# ********************************************************************************************
# Global Variables
# global_variable = 10

# def my_function():
#     print(global_variable)

# my_function()
# print(global_variable)


# ====================================== Unpack a Collection ======================================================

# LIST
# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits
# print(x)
# print(y)
# print(z)

# TUPLE
# fruits = ("apple", "banana", "cherry")
# x, y, z = fruits
# print(x)
# print(y)
# print(z)

# SET
# fruits = {"apple", "banana", "cherry"}
# x, y, z = fruits
# print(x)
# print(y)
# print(z)

# String
# fruits = "abc"
# x, y, z = fruits
# print(x)
# print(y)
# print(z)

# Unpacking with More Variables than Elements
# fruits = ["apple", "banana"]
# x, y, z = fruits  # ValueError: not enough values to unpack (expected 3, got 2)

# Unpacking with Fewer Variables than Elements
fruits = ["apple", "banana", "cherry", "date"]
x, y = fruits
print(x)
print(y)