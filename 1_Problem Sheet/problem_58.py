# Write a python program to remove all the duplicates from a list


def remove_duplicates(input_list):
    # Use a set to remove duplicates and convert it back to a list
    return list(set(input_list))

# Get input from the user
input_list = input("Enter the list of elements separated by space: ").split()

# Convert input elements to the appropriate type (e.g., integers) if needed
# For now, the program assumes the list contains strings
result_list = remove_duplicates(input_list)
print(f"The list after removing duplicates is: {result_list}")
