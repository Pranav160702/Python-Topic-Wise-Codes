# Write a program that will check whether the number is armstrong number or not.
# Armstrong number is a number that is equal to the sum of cubes of its digits.


def is_armstrong(n):
    # Convert integer to string to easily get the number of digits
    num_str = str(n)
    num_digits = len(num_str)
    
    # Calculate the sum of cubes of its digits
    sum_cubes = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the number is equal to the sum of cubes of its digits
    return n == sum_cubes

# Test the function
num = int(input("Enter a number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
