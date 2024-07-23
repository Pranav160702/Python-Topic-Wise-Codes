# Write a Python Program to Find the Sum of the Series till the nth term: 
# 1 + x^2/2 + x^3/3 + … x^n/n
# n will be provided by the user
# Code
def series_sum(x, n):
    sum_series = 1  # Start with the first term which is 1
    for i in range(2, n+1):
        sum_series += (x ** i) / i
    return sum_series

# Get input from the user
x = float(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))
result = series_sum(x, n)
print(f"The sum of the series up to {n} terms is: {result}")

