# Write a program to print the first 25 odd numbers
# Initialize a counter for the number of odd numbers printed
count = 0

# Initialize a variable to keep track of the current number
num = 1

while count < 25:
    # Check if the number is odd
    if num % 2!= 0:
        print(num)
        count += 1
    num += 1