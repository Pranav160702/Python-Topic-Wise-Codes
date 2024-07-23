# User will input (2numbers).Write a program to swap the numbers
# 
# =================================================================


num1 = int(input("Enter the First Number: "))
num2 = int(input("Enter the Second Number:"))
print(f"Before Swapping --> num1 = {num1}, num2 = {num2}")

num1 , num2 = num2, num1
print(f"After Swapping  --> num1 = {num1}, num2 = {num2}")


# # =================================================================
# # Using Three Variable
# # =================================================================
# # 
# # Advantages: 
# # 1. Easy to understand and implement
# # 2. Works for all data types (not just numbers)
# # Disadvantages:
# # Requires an extra variable, which can be a minor memory overhead
# # *****************************************************************
# # 
# temp = num1
# num1 = num2
# num2 = temp
# print(f"After Swapping  --> num1 = {num1}, num2 = {num2}")


# # 
# # =================================================================
# # Without using Third Variable
# # =================================================================
# #
# # Advantages:
# # No extra variable is needed, which can be beneficial in certain situations (e.g., when working with large datasets)
# # Disadvantages:
# # 1. Only works for numbers (not for other data types)
# # 2. Can cause overflow errors if the sum of num1 and num2 exceeds the maximum value for the data type
# # *****************************************************************
# num1 = num1 + num2
# num2 = num1 - num2
# num1 = num1 - num2
# print(f"After Swapping  --> num1 = {num1}, num2 = {num2}")