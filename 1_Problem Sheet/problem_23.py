# Write a program that will swap numbers

def swap_numbers(a, b):
    # Create a temporary variable to hold the value of a
    temp = a
    
    # Assign the value of b to a
    a = b
    
    # Assign the value of temp (which is the original value of a) to b
    b = temp
    
    return a, b

# Get user input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("Before swapping: ")
print("Number 1 =", num1)
print("Number 2 =", num2)

num1, num2 = swap_numbers(num1, num2)

print("After swapping: ")
print("Number 1 =", num1)
print("Number 2 =", num2)