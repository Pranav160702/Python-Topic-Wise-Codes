# # basic if statement
# x = 10
# if x > 5:
#     print("x is greater than 5")  

# # Output: x is greater than 5



# # if...else statement
# x = 3
# if x > 5:
#     print("x is greater than 5")
# else:
#     print("x is not greater than 5")

# # Output: x is not greater than 5



# # if...elif...else Statement
# x = 7
# if x > 10:
#     print("x is greater than 10")
# elif x > 5:
#     print("x is greater than 5 but less than or equal to 10")
# else:
#     print("x is 5 or less")

# # Output: x is greater than 5 but less than or equal to 10


# Nested if Statements
x = 8
if x > 5:
    print("x is greater than 5")
    if x > 10:
        print("x is also greater than 10")
    else:
        print("x is not greater than 10")
else:
    print("x is not greater than 5")

# Output: 
# x is greater than 5
# x is not greater than 10