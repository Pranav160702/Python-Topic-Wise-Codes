# Write a program to replace an item with a different item if found in the list 

def replace_item(input_list, old_item, new_item):
    # Replace old_item with new_item in the list
    return [new_item if item == old_item else item for item in input_list]

# Get input from the user
input_list = input("Enter the list of elements separated by space: ").split()
old_item = input("Enter the item to replace: ")
new_item = input("Enter the new item: ")

# Convert elements to integers if needed
# Here we handle items as strings; if you need to handle integers, uncomment the next lines
# input_list = [int(x) for x in input_list]
# old_item = int(old_item)
# new_item = int(new_item)

# Replace the item in the list
result_list = replace_item(input_list, old_item, new_item)
print(f"The list after replacement is: {result_list}")
