# Write a program to find the sum of first n numbers, where n will be provided by the user. Eg if the user provides n=10 the output should be 55.

def sum_of_first_n_numbers(n):
    return n * (n + 1) // 2

n = int(input("Enter a number: "))
result = sum_of_first_n_numbers(n)
print("The sum of the first", n, "numbers is", result)