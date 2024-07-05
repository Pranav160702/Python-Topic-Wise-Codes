# Write a program that accepts 2 numbers from the user a numerator and a denominator 
# and then simplifies it
# Eg if the num = 5, den = 15 the answer should be ⅓
# Eg if the num = 6, den = 9 the answer should be ⅔


import math

def simplify_fraction(numerator, denominator):
    gcd = math.gcd(numerator, denominator)
    # print(gcd)
    simplified_numerator = numerator // gcd
    simplified_denominator = denominator // gcd
    return simplified_numerator, simplified_denominator

def print_fraction(numerator, denominator):
    if denominator == 1:
        return str(numerator)
    else:
        return f"{numerator}/{denominator}"

numerator = int(input("Enter the numerator: "))
denominator = int(input("Enter the denominator: "))

simplified_numerator, simplified_denominator = simplify_fraction(numerator, denominator)

print(f"The simplified fraction is: {print_fraction(simplified_numerator, simplified_denominator)}")