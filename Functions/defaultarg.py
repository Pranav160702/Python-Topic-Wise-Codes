
# def greet(name = "World"):
#     print(f"Hello, {name}!")

# greet()         # Output: Hello, world!
# greet("Pranav") # Output: Hello, Pranav!


# Order Matters in Default Argumrnts
# Correct Way
def my_function(name, age = 0):
    print(f"Hello, {name}. Your age is {age}")

my_function("Pranav", 22)   # Output: Hello, Pranav. Your age is 22

# Incorrect Way
def my_function(age = 0, name):
    print(f"Hello, {name}. Your age is {age}")

