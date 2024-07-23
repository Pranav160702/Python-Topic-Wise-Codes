# Write a program to print all the unique combinations of 1,2,3 and 4

import itertools

def print_unique_combinations(numbers):
    # Generate all permutations of the given numbers
    permutations = list(itertools.permutations(numbers))
    
    # Print each permutation
    for perm in permutations:
        print(perm)

# List of numbers
numbers = [1, 2, 3, 4]

# Print all unique combinations
print_unique_combinations(numbers)
