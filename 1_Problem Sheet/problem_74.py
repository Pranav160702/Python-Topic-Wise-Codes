# Write a program to print the shape of a matrix.

def print_matrix_shape(matrix):
    # Get the number of rows
    num_rows = len(matrix)
    
    # Get the number of columns (assuming all rows have the same number of columns)
    num_columns = len(matrix[0]) if num_rows > 0 else 0
    
    return num_rows, num_columns

# Get input from the user
num_rows = int(input("Enter the number of rows in the matrix: "))
matrix = []

for i in range(num_rows):
    row = input(f"Enter row {i + 1} elements separated by space: ").split()
    row = [int(x) for x in row]  # Convert elements to integers
    matrix.append(row)

# Print the shape of the matrix
rows, columns = print_matrix_shape(matrix)
print(f"The shape of the matrix is: {rows}x{columns}")
