# Write a program that can create a new list from a given list 
# where each item in the new list is square of the item of the old list

def square_items(input_list):
    # Create a new list with squared values of each item in the input list
    return [item ** 2 for item in input_list]

# Get input from the user
input_list = input("Enter the list of numbers separated by space: ").split()
input_list = [int(x) for x in input_list]  # Convert elements to integers

squared_list = square_items(input_list)
print(f"The new list with squared items is: {squared_list}")

