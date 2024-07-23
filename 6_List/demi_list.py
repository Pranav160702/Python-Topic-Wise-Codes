# # Creating List
# # =========================================
# # Create an empty list
# my_list = []

# # Create a list with some elements
# my_list = [1, 2, 3, 4, 5]


# # Indexing and Slicing
# # =========================================
# my_list = [1, 2, 3, 4, 5]

# # Access an element using its index
# print(my_list[0])  # Output: 1

# # Access a slice of elements
# print(my_list[1:3])  # Output: [2, 3]

# # Access a slice of elements from the start
# print(my_list[:3])  # Output: [1, 2, 3]

# # Access a slice of elements to the end
# print(my_list[2:])  # Output: [3, 4, 5]


# # updating Elements
# # =========================================
# my_list = [1, 2, 3, 4, 5]

# # Update an element
# my_list[0] = 10
# print(my_list)  # Output: [10, 2, 3, 4, 5]

# # Update a slice of elements
# my_list[1:3] = [20, 30]
# print(my_list)  # Output: [10, 20, 30, 4, 5]


# # Deleting Elements
# # =========================================
# my_list = [1, 2, 3, 4, 5]

# # Delete an element using the del statement
# del my_list[0]
# print(my_list)  # Output: [2, 3, 4, 5]

# # Delete a slice of elements
# del my_list[1:3]
# print(my_list)  # Output: [2, 5]

# # Delete an element using the remove() method
# my_list.remove(2)
# print(my_list)  # Output: [5]

# # Delete an element using the pop() method
# my_list.pop(0)
# print(my_list)  # Output: []


# # Inserting Elements
# # =========================================
# my_list = [1, 2, 3, 4, 5]

# # Insert an element at a specific position
# my_list.insert(0, 10)
# print(my_list)  # Output: [10, 1, 2, 3, 4, 5]

# # Insert multiple elements at a specific position
# my_list[1:1] = [20, 30]
# print(my_list)  # Output: [10, 20, 30, 1, 2, 3, 4, 5]


# # Sorting and Reversing
# # =========================================
# my_list = [5, 2, 8, 3, 1]

# # Sort the list in ascending order
# my_list.sort()
# print(my_list)  # Output: [1, 2, 3, 5, 8]

# # Sort the list in descending order
# my_list.sort(reverse=True)
# print(my_list)  # Output: [8, 5, 3, 2, 1]

# # Reverse the list
# my_list.reverse()
# print(my_list)  # Output: [1, 2, 3, 5, 8]



# #Appending  Elements
# # =========================================
# my_list = [1, 2, 3, 4, 5]

# # Append an element to the end of the list
# my_list.append(6)
# print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

# # Append multiple elements to the end of the list
# my_list.extend([7, 8, 9])
# print(my_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]



# # Check if an element exists in the list
# # =========================================

# my_list = [1, 2, 3, 4, 5]

# # Check if an element exists in the list
# print(2 in my_list)  # Output: True
# print(6 in my_list)  # Output: False


# List Comprehensions
# =========================================
# Create a new list with squares of numbers from 1 to 5
squares = [x**2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]

# Create a new list with even numbers from 1 to 10
even_numbers = [x for x in range(1, 11) if x % 2 == 0] 
print(even_numbers)  