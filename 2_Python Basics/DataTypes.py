#=====================INTEGER==============================
# x = 16          #integer
# print(x)        #Output: 16
# print(type(x))  #Ouput: <class 'int'>

# y= 0x16         #Hexadecimal Integer
# print(y)        #Output: 22
# print(type(y))  #Output: <class 'int'>

# z = 0o23        #Ocatal Integer
# print(z)        #Output:
# print(type(z))  #Output: <class 'int'>

# w = 0b10101     #Binary Integer
# print(w)        #Output: 21
# print(type(w))  #Output: <class 'int'>

# print(1e308)
# print(1e309) 

#=====================FLOAT==========================

# x = 3.14  # float
# print(x)
# print(type(x))  # Output: <class 'float'>

# y = -0.5        # negative float
# print(y)        # Output: -0.5
# print(type(y))  # Output: <class 'float'>

# z = 1e2  # scientific notation
# print(z)  # Output: 100.0

# Large float within the range
# large_float = 1.7e308
# print(large_float)  # Outputs: 1.7e+308

# # Trying to exceed the maximum float value results in infinity
# too_large_float = 1.8e308
# print(too_large_float)  # Outputs: inf

# # Small float within the range
# small_float = 1.7e-308
# print(small_float)  # Outputs: 1.7e-308

# # Trying to go below the minimum float value results in underflow to 0.0
# too_small_float = 1e-324
# print(too_small_float)  # Outputs: 0.0

#=================================Boolean=========================================

# x = True  # assign True to x
# print(x)
# y = False  # assign False to y
# print(y)


#=================================Complex=========================================

# x = 3 + 4j  # complex number
# print(x)
# print(type(x))  # Output: <class 'complex'>

# y = -2 - 3j  # complex number
# print(y)  # Output: (-2-3j)

# z = x + y  # complex number addition
# print(z)  # Output: (1+1j)


#======================================String======================================


# my_string = 'Hello, World!'     #Single quotes
# print(my_string)

# my_string = "Hello, World!"     #Double Quotes
# print(my_string)

# my_string = """Hello, 
#     World
#         String!""" #Triple quotes(used for multiline strings)
# print(my_string)


#===================================List(Mutable)=============================================

# print([1,3,5,65,98,54])         #List with integer values

# print(["India","Nepal","Japan","Srilanka"]) #List with string values

# print([2.3,45.6,7.8,4.5,98.7])  #List with float values

# print([23,"India",6.5,34,"Japan"])


#====================================Tuples(Imutable)===========================================
# x = (1, 2, 3)  # tuple
# print(type(x))  # Output: <class 'tuple'>

# y = ("a", "b", "c")  # tuple of strings
# print(y)  # Output: ('a', 'b', 'c')

# z = (1, "a", 2.5)  # tuple of mixed types
# print(z)  # Output: (1, 'a', 2.5)

# w = x + y  # tuple concatenation
# print(w)  # Output: (1, 2, 3, 'a', 'b', 'c')


#====================================SET===============================================

# x = {1, 2, 3}  # set
# print(type(x))  # Output: <class 'set'>

# y = {"a", "b", "c"}  # set of strings
# print(y)  # Output: {'a', 'b', 'c'}

# z = x | y  # set union
# print(z)  # Output: {1, 2, 3, 'a', 'b', 'c'}

# w = x & y  # set intersection
# print(w)  # Output: set()

#===============================DICTIONARY==========================================
x = {"name": "John", "age": 30}  # dictionary
print(type(x))  # Output: <class 'dict'>

y = {"a": 1, "b": 2, "c": 3}  # dictionary of integers
print(y)  # Output: {'a': 1, 'b': 2, 'c': 3}

z = x["name"]  # accessing a dictionary value
print(z)  # Output: John

w = x.get(" occupation", "Unknown")  # accessing a dictionary value with default
print(w)  # Output: Unknown
