# the max item of each row of a matrix. 

def max_in_rows(matrix):
    # Find the maximum item in each row of the matrix
    return [max(row) for row in matrix]

# Get input from the user
num_rows = int(input("Enter the number of rows in the matrix: "))
matrix = []

for i in range(num_rows):
    row = input(f"Enter row {i + 1} elements separated by space: ").split()
    row = [int(x) for x in row]  # Convert elements to integers
    matrix.append(row)

# Find the maximum item in each row
max_items = max_in_rows(matrix)
print(f"The maximum item in each row is: {max_items}")

