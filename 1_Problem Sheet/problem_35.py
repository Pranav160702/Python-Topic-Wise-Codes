# Print the first 20 numbers of a Fibonacci series
# 0, 1, 1, 2, 3, 5,
# 8, 13, 21, 34, 55, 89,
# 144, 233, 377, 610, 987, 1597,
# 2584, 4181


def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series

print("The first 20 numbers of a Fibonacci series are:", fibonacci(20))