# Write a program that can multiply 2 numbers provided by the user without using the * operator

def multiply(a, b):
    result = 0
    for _ in range(abs(b)):
        result += a
    if b < 0:
        return -result
    return result

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("The product of the two numbers is", multiply(num1, num2))