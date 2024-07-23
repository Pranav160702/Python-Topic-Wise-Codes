

# def fibonacci(n):
#     # Base cases
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     # Recursive case
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# # Example usage:

# for i in range(10):  # Print first 10 Fibonacci numbers
#     print(f"F({i}) = {fibonacci(i)}")


# using Dictionary for same
def fibonacci(n, d):
    if n in d:
        return d[n]
    else:
        d[n] = fibonacci(n-1,d) + fibonacci(n-2,d) 
        return d[n]

d = {0:1,1:1}
n = int(input("Enter Any number: "))
print(fibonacci(n,d))