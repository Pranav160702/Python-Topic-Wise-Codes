# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.


def compute_n_plus_nn_plus_nnn(n):
    nn = int(str(n) + str(n))
    nnn = int(str(n) + str(n) + str(n))
    return n + nn + nnn

n = int(input("Enter an integer: "))
print(compute_n_plus_nn_plus_nnn(n))

