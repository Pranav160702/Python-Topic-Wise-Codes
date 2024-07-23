# Write a program that will tell whether the given year is a leap year or not.
# A year is a leap year if it is divisible by 4, but not by 100
# unless it is also divisible by 400.
# For example, 1997 is not a leap year, but 1996 is.

year = int(input("Enter The year: "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")
    