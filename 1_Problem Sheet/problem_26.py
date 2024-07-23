# Write a program that can find the factorial of a given number provided by the user.
# The factorial of a number is the product of all the integers from 1 to that number.
# For example, the factorial of 5 is 1*2*3*4*5

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))
result = factorial(num)
print("The factorial of", num, "is", result)