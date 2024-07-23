# User will provide 2 numbers you have to find the by LCM of those 2 numbers
# LCM = Lowest Common Multiple

def find_lcm(num1, num2):
    # Compute the maximum of num1 and num2
    max_num = max(num1, num2)
    
    while True:
        if max_num % num1 == 0 and max_num % num2 == 0:
            return max_num
        max_num += 1

# Get user input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Find and print the LCM
lcm = find_lcm(num1, num2)
print("The LCM of", num1, "and", num2, "is", lcm)