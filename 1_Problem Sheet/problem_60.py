# Write a python program to find the max item from a list without using the max function


def find_max(input_list):
    # Initialize the maximum element with the first element of the list
    max_item = input_list[0]
    
    # Iterate through the list to find the maximum element
    for item in input_list:
        if item > max_item:
            max_item = item
    
    return max_item

# Get input from the user
input_list = input("Enter the list of elements separated by space: ").split()
input_list = [int(x) for x in input_list]  # Convert elements to integers

max_item = find_max(input_list)
print(f"The maximum item in the list is: {max_item}")
