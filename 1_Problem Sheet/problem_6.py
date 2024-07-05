# Write a program that will tell whether the number entered by the user is odd or even.
# num = int(input("Enter The Number: "))
# if num % 2 == 0:
#     print("The Number is Even")
# else:
#     print("The Number is Odd")


# Lambda function for the same 
even_odd = lambda x: "Even" if x % 2 == 0 else "Odd"
print(even_odd(int(input("Enter The Number: "))))

