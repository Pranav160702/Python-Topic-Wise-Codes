# Write a program that will take user input of (4 digits number) and check whether the number is narcissist number or not.

# Narcissistic number is a number that is the sum of its own digits each raised to the power of the number of digits.
# For example, take 153 (3 digits): 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153. So
# Code


num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** len(str(num))
    temp //= 10
if num == sum:
    print(num, "is a narcissistic number")
else:
    print(num, "is not a narcissistic number")

