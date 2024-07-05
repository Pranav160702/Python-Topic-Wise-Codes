# Write a program that will give you the sum of the digits of 3 digit Number
def sum_digits(num):
    sum = 0
    if(100 <= num <= 999):
        while num > 0:
            sum += num % 10
            num //= 10
        return sum
    else:
        return("Invalid Number, please Enter Valid Number")
    

num = int(input("Enter The Number to Colculate Digit Sum:"))
print("The Sum of Digit is: ",sum_digits(num))