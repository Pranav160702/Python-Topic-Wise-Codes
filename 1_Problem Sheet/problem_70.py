# Write a program that can convert a 2D list to 1D list Write a program that can print 

def flatten_2d_list(two_d_list):
    # Use a list comprehension to flatten the 2D list
    return [item for sublist in two_d_list for item in sublist]

# Example 2D list
two_d_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Convert the 2D list to a 1D list
one_d_list = flatten_2d_list(two_d_list)
print(f"The 1D list is: {one_d_list}")

