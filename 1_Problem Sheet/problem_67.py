# Create 2 lists from a given list where 1st list will contain all the odd numbers 
# from the original list and the 2nd one will contain all the even numbers 

def separate_odd_even(input_list):
    odd_numbers = [num for num in input_list if num % 2 != 0]
    even_numbers = [num for num in input_list if num % 2 == 0]
    return odd_numbers, even_numbers

# Get input from the user
input_list = input("Enter the list of numbers separated by space: ").split()
input_list = [int(x) for x in input_list]  # Convert elements to integers

# Separate the numbers into odd and even lists
odd_list, even_list = separate_odd_even(input_list)

print(f"List of odd numbers: {odd_list}")
print(f"List of even numbers: {even_list}")

