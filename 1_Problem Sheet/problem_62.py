# Write a python program to search a given number from a list


def search_number(input_list, number):
    # Check if the number is in the list
    if number in input_list:
        return True
    else:
        return False

# Get input from the user
input_list = input("Enter the list of numbers separated by space: ").split()
input_list = [int(x) for x in input_list]  # Convert elements to integers
number_to_search = int(input("Enter the number to search: "))

# Search for the number in the list
if search_number(input_list, number_to_search):
    print(f"The number {number_to_search} is in the list.")
else:
    print(f"The number {number_to_search} is not in the list.")
