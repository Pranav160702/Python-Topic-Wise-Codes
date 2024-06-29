# # Example 1: Demonstrating Use of Python break Statement
# #Using for loop
# for i in "Pranav":                  #First Example
#     if i == "a":
#         break
#     print("Curent letter: ", i)


# num = 20
# for i in range(1, num + 1):        #Second Example
#     if i > 10:
#         break
#     print("Current value: ", i)


# # Using while loop
# var = 20
# while var > 0:
#     if var < 10:
#         break
#     print("Current Variable value: ", var)
#     var -= 1


# # Example 2: Checking for a Number in List
# num = int(input("Enter the Number: "))
# numbers=[11,33,55,39,55,75,37,21,23,41,13]
# for i in numbers:
#     if i == num:
#         print("Number found in the list")
#         break
# else:
#     print("Number not found in the list")


# Example 3: Checking for Prime Number
num = int(input("Enter the Number: "))
for i in range(2, num):
    if num % i == 0:
        print("Number is not prime")
        break
    else:
        print("Number is prime")
        break
    