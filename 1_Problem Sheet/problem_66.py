# Write a program to check if a list is in ascending order or not


def is_ascending(input_list):
    # Check if each element is less than or equal to the next element
    return all(input_list[i] <= input_list[i + 1] for i in range(len(input_list) - 1))

# Get input from the user
input_list = input("Enter the list of numbers separated by space: ").split()
input_list = [int(x) for x in input_list]  # Convert elements to integers

# Check if the list is in ascending order
if is_ascending(input_list):
    print("The list is in ascending order.")
else:
    print("The list is not in ascending order.")
