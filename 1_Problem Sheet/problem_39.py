# Print all factors of a given number provided by the user.

# Get the number from the user
num = int(input("Enter a number: "))

# Print all factors of the number
print("Factors of", num, "are:")
for i in range(1, num + 1):
    if num % i == 0:
        print(i)