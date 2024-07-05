# Find the reverse of a number provided by the user(any number of digit) 


# Get the number from the user
num = int(input("Enter a number: "))

# Convert the number to a string to easily reverse it
num_str = str(num)

# Reverse the string using slicing
reversed_num_str = num_str[::-1]

# Convert the reversed string back to an integer
reversed_num = int(reversed_num_str)

# Print the result
print("The reverse of", num, "is:", reversed_num)