# # Example 1: Iterating Over a List
# fruits = ['apple', 'banana', 'cherry']
# for fruit in fruits:
#     print(fruit)


# # Example 2: Iterating Over a String
# word = 'hello'
# for char in word:
#     print(char)



# # Using 'range()' with 'for' Loop
# # Example 1: Printing Numbers from 1 to 10 with 2 step.
# for i in range(1, 11, 2):
#     print(i, end=" ")



# Iterating Over Dictionary
# # Example 1: Iterating Over Dictionary Keys
# person = {'name': 'John', 'age': 30, 'city': 'New York'}
# for key in person.keys():
#     print(key)


# # Example 2: Iterating Over Dictionary Values
# person = {'name': 'John', 'age': 30, 'city': 'New York'}
# for value in person.values():
#     print(value)


# # Example 3: Iterating Over Dictionary Both(Keys & Values)
# person = {'name': 'John', 'age': 30, 'city': 'NewYork'}
# for key, value in person.items():
#     print(f"{key}: {value}")



# Using else with for Loop
# # Example 1: Using else with for Loop
# fruits = ['apple', 'banana', 'cherry']
# for fruit in fruits:
#     print(fruit)
# else:
#     print("No more fruits!")


# # Example with break statement
# fruits = ['apple', 'banana', 'cherry']
# for fruit in fruits:
#     if fruit == 'banana':
#         break
#     print(fruit)
# else:
#     print("No more fruits!")  # This will not be executed 
#                               # because of break statement



# # Nested for Loop Example
# months = ["jan", "feb", "mar"]
# days = ["sun", "mon", "tue"]

# for x in months:
#   for y in days:
#     print(x, y)

# # Another stromg example
# for i in range(1, 11):
#   for j in range(1, 11):
#     if i*j < 10 :
#       print(i*j, end = "  ")
#     else:
#       print(i*j, end = " ")
#   print()

# Provide same for nested while loop
i = 1
while i < 11:
  j = 1
  while j < 11 :
    if i*j < 10 :
      print(i*j, end = "  ")
    else:
      print(i*j, end = " ") 
    j += 1
  print()
  i += 1

    # Note: The break statement will only break the inner loop, not the outer loop.
    # If you want to break the outer loop, you can use a flag variable.
    # For example:
    # flag = False
    # for i in range(1, 6):
    #   for j in range(1, 6):
    #     print(i*j)
    #     if i*j > 10 :
    #       flag = True
    #       break
    #   if flag:
    #     break



