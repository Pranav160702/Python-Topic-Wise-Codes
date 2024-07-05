# Write a program to calculate the sum of the following series till the nth term
# 1/1! + 2/2! + 3/3! + 4/4! +…….+ n/n!
# n will be provided by the user

import math

def series_sum(n):
    if n <= 0:
        return "Error: n should be a positive integer."
    sum_series = 0
    for i in range(1, n+1):
        sum_series += i / math.factorial(i)
    return sum_series

# Get input from the user
n = int(input("Enter the value of n: "))
result = series_sum(n)
print(f"The sum of the series up to {n} terms is: {result}")
