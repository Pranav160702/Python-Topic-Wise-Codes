# Write a program that can check if you can perform matrix multiplication on 2 matrices 
def can_multiply_matrices(matrix1, matrix2):
    # Number of columns in matrix1
    num_columns_matrix1 = len(matrix1[0]) if matrix1 else 0
    # Number of rows in matrix2
    num_rows_matrix2 = len(matrix2)
    
    # Check if the number of columns in matrix1 equals the number of rows in matrix2
    return num_columns_matrix1 == num_rows_matrix2

# Get input for the first matrix
num_rows_matrix1 = int(input("Enter the number of rows in the first matrix: "))
matrix1 = []

for i in range(num_rows_matrix1):
    row = input(f"Enter row {i + 1} of the first matrix elements separated by space: ").split()
    row = [int(x) for x in row]  # Convert elements to integers
    matrix1.append(row)

# Get input for the second matrix
num_rows_matrix2 = int(input("Enter the number of rows in the second matrix: "))
matrix2 = []

for i in range(num_rows_matrix2):
    row = input(f"Enter row {i + 1} of the second matrix elements separated by space: ").split()
    row = [int(x) for x in row]  # Convert elements to integers
    matrix2.append(row)

# Check if the matrices can be multiplied
if can_multiply_matrices(matrix1, matrix2):
    print("The matrices can be multiplied.")
else:
    print("The matrices cannot be multiplied.")
