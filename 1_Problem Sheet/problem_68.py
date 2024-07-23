# Write a program to merge 2 list without using the + operator


def merge_lists(list1, list2):
    # Create a copy of list1
    merged_list = list1[:]
    # Extend the copied list with list2
    merged_list.extend(list2)
    return merged_list

# Get input from the user
input_list1 = input("Enter the first list of elements separated by space: ").split()
input_list2 = input("Enter the second list of elements separated by space: ").split()

# Convert elements to integers if needed
input_list1 = [int(x) for x in input_list1]
input_list2 = [int(x) for x in input_list2]

# Merge the two lists
result_list = merge_lists(input_list1, input_list2)
print(f"The merged list is: {result_list}")
