# # Program to print table of given number
# num = int(input("Enter the Number: "))
# i = 1
# while(i <= 10):
#     print(f"{num} x {i} = {num * i}")
#     i += 1

# # while loop example
# i = 1
# while(i <= 10):
#     print(i)
#     i += 1


# Infinite While loop example

# i = 1           #Example 1
# while True:
#     print(i)
#     i += 1
#     if i > 10:
#         break

# var = 1         #Example 2
# while var == 1:  # This constructs an infinite loop
#     num = int(input("Enter a number: "))
#     print("You entered: ", num)


# Python while-else Loop
i = 1
while i <= 5:
    print(i)
    i += 1
else:
 print("Loop Finished")


#  Prime number code using while-else loop
num = int(input("Enter a number: "))
i = 2
while i * i <= num:
   if num % i == 0:
      print(f"{num} is not a prime number")
      break
   i += 1
else:
    print(f"{num} is a prime number")
