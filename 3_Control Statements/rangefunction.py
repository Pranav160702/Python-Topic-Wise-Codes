# Range function
# The range function generates a sequence of numbers starting from the first argument up to, but not including
# the second argument. The third argument specifies the increment between the numbers in the sequence.
# If the third argument is not provided, the increment defaults to 1.
# The range function returns a range object, which is an iterable.

# # Example:range(stop)
# for i in range(10):
#     print(i, end = " ")


# #Example:range(start,stop)
# for i in range(5,10):
#     print(i, end = " ")


# # Example:range(start,stop,step)
# for i in range(0,10,2):
#     print(i, end = " ")


# # Example of negative step
# for i in range(10,0,-1):
#     print(i, end = " ")
# print()

# for i in range(10,0,-2):
#     print(i, end = " ")


# # range() in list comprehensions to generate lists of numbers.
# numbers = [x for x in range(10)]
# print(numbers)


# Converting range to a List
numbers_list = list(range(10))
print(numbers_list)


