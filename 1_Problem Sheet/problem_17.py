# Write a program that will take three digits from the user and add the square of each digit.

# Code
num = int(input("Enter a number: "))
while len(str(num)) != 3:
    print("Enter a number with 3 digits:")
    num = int(input("Enter a number: "))
sum = 0
for i in str(num):
    sum += int(i) ** 2
print(sum)
