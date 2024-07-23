# Write a program that can perform union and intersection on 2 given list.

def list_union(list1, list2):
    # Convert lists to sets to perform union operation
    return list(set(list1) | set(list2))

def list_intersection(list1, list2):
    # Convert lists to sets to perform intersection operation
    return list(set(list1) & set(list2))

# Get input from the user
input_list1 = input("Enter the first list of elements separated by space: ").split()
input_list2 = input("Enter the second list of elements separated by space: ").split()

# Convert elements to integers if needed
input_list1 = [int(x) for x in input_list1]
input_list2 = [int(x) for x in input_list2]

# Perform union and intersection operations
union_list = list_union(input_list1, input_list2)
intersection_list = list_intersection(input_list1, input_list2)

print(f"The union of the lists is: {union_list}")
print(f"The intersection of the lists is: {intersection_list}")
