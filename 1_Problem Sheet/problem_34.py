# Print first 25 prime numbers

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n**0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True

count = 0
num = 2
prime_numbers = []

while count < 25:
    if is_prime(num):
        prime_numbers.append(num)
        count += 1
    num += 1

print("The first 25 prime numbers are:", prime_numbers)