# User will provide 2 numbers you have to find the HCF of those 2 numbers
# HCF is Highest Common Factor
# HCF is also known as GCD (Greatest Common Divisor)



def find_hcf(num1, num2):
    # Compute the maximum of num1 and num2
    max_num = max(num1, num2)
    
    # Initialize the HCF
    hcf = 1
    
    # Iterate from 1 to the maximum of num1 and num2
    for i in range(1, max_num + 1):
        # Check if i is a factor of both num1 and num2
        if num1 % i == 0 and num2 % i == 0:
            # Update the HCF
            hcf = i
    
    return hcf

# Get the two numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Find and print the HCF
hcf = find_hcf(num1, num2)
print("The HCF of", num1, "and", num2, "is", hcf)