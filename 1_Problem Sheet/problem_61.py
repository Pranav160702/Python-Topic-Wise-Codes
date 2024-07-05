# Write a python program to reverse a list
def reverse_list(input_list):
    return input_list[::-1]

# Get input from the user
input_list = input("Enter the list of elements separated by space: ").split()
# Convert elements to integers if needed, otherwise keep them as strings
# input_list = [int(x) for x in input_list]

reversed_list = reverse_list(input_list)
print(f"The reversed list is: {reversed_list}")
