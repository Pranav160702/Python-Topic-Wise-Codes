# Write a program that will give you the in hand salary after deduction of HRA(10%),DA(5%),PF(3%), and tax(if salary is between 5-10 lakh–10%),(11-20lakh–20%),(20< _   – 30%)(0-1lakh print k).


def calculate_in_hand_salary(gross_salary):
    # Calculate HRA, DA, and PF deductions
    hra_deduction = gross_salary * 0.10
    da_deduction = gross_salary * 0.05
    pf_deduction = gross_salary * 0.03

    # Calculate total deductions
    total_deductions = hra_deduction + da_deduction + pf_deduction

    # Calculate taxable income
    taxable_income = gross_salary - total_deductions

    # Calculate tax based on taxable income
    if taxable_income <= 100000:
        tax = 0
    elif 100000 < taxable_income <= 500000:
        tax = taxable_income * 0.10
    elif 500000 < taxable_income <= 1000000:
        tax = taxable_income * 0.20
    else:
        tax = taxable_income * 0.30

    # Calculate in-hand salary
    in_hand_salary = gross_salary - total_deductions - tax

    return in_hand_salary

# Test the function
gross_salary = float(input("Enter your gross salary: "))
in_hand_salary = calculate_in_hand_salary(gross_salary)

if gross_salary <= 100000:
    print("k")
else:
    print("Your in-hand salary is: ", in_hand_salary)