# # Example 1: Function Without Parameters
# def my_function():
#     print("Hello from a function without parameters")

# # Call the function
# my_function()       #Output: Hello from a function without parameters


# # Example 2: Function With Parameters
# def my_function_with_parameters(name, age):
#     print("Hello " + name + ", you are " + str(age) + " years old")

# # Call the function
# my_function_with_parameters("John", 36)  #Output: Hello John, you are 36 years old

# Example 3: Function With a Return Statement 
# def add(a, b):
#     """Returns the sum of two numbers."""
#     return a + b
# # Functi
# result = add(45,65) # result is 110
# print(result)       #Output: 110

# Simple Function Calling Example

# def fun_call():
#     print("This is Function Call")

# # Function Calling
# fun_call()  # Output: This is Function Call




# def greet(name):
#     print(f"Hello, {name}!")

# # Function Calling
# greet("Pranav")


# def modify_value(val_arg):
#     print("ID Inside the Function Before Modification: ",id(val_arg))
    
#     val_arg = 10

#     print("ID Inside the Function After Modification: ",id(val_arg))
#     print(f"Value Inside the function: {val_arg}")


# value = 500
# print("Initial Id of Value: ",id(value))
# modify_value(value)

# print("Id Outside the Function After Function Execution: ",id(value))
# print(f"Value Outside the function After Function Execution: {value}")



# def modify_value(value):
#     print("++++++++++++++ INSIDE THE FUNCTION ++++++++++++++++")
#     print("ID of argument on entry: ", id(value))  # Print the ID of the original value (5)
#     value = 10
#     print("ID inside the function after modification: ", id(value))
#     print(f"Value Inside function: {value}")

# value = 5
# print("Initial ID of value (5): ", id(value))
# modify_value(value)
# print("++++++++++++++ OUTSIDE THE FUNCTION ++++++++++++++++")
# print("ID Outside the Function: ", id(value))
# print(f"Value Outside function: {value}")
# print("ID of value 10 outside: ", id(10))


# def testfunction(arg):
#    print ("List Inside function Before Modification:",arg)
#    print ("List ID inside the function Before Modification:", id(arg))

#    arg=arg.append(100)
   
# var=[10, 20, 30, 40]
# print("Initial List:",var)
# print ("List ID before passing:", id(var))

# testfunction(var)
# print ("list after function call", var)
# print("List Id After Function Call:",id(var))


# global Keyword



# def modify():
#     global x
#     x = 5
#     print("Inside function:", x) # Output: Inside Function: 5

# modify()
# x = 10
# print("Outside function:", x)    # Output: Outside Function: 5


# a = 1
# b = 2

# def modify_globals():
#     global a, b
#     a = a + 1
#     b = b + 1
#     print("Inside function -> a :", a, "b :", b)

# modify_globals()
# print("Outside function -> a :", a, "b :", b)



# def greet(name):
#   """This function greets a person with a customizable message"""

#   def get_message():
#     """Creates a personalized greeting message"""
#     message = f"Hello, {name.upper()}!"  # Accessing outer function's parameter
#     return message

#   greeting = get_message()
#   return greeting

# person = "Alice"
# personalized_greeting = greet(person)
# print(personalized_greeting)            # Output: Hello, ALICE!




# def outer_function():
#   """This function demonstrates the local scope of inner functions"""

#   def inner_function():
#     """This function is only accessible within outer_function"""
#     print("Inner function called!")

#   # inner_function()  # This would cause an error because inner_function is local

# outer_function()  # This will execute outer_function, but not inner_function directly


# def outer_function(message):
#     def inner_function():
#         print(message)
#     return inner_function

# my_closure = outer_function("Hello, World!")
# my_closure()  # Output: Hello, World!
print(dir([1, 2, 3])) 