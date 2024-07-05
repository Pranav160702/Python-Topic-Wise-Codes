# Print all the armstrong numbers in the range of 100 to 1000
# Armstrong number is a number that is equal to the sum of the cubes of its digits.
# For example, 371 is an Armstrong number since 3**3 + 7**3 + 1**3 = 371.

def find_armstrong():
    armstrong_numbers = []
    for num in range(100, 1001):
        num_str = str(num)
        num_len = len(num_str)
        sum_cubes = sum(int(digit) ** num_len for digit in num_str)
        if sum_cubes == num:
            armstrong_numbers.append(num)
    return armstrong_numbers

print(find_armstrong())


