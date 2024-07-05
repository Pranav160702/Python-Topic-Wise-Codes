# Write a program to find the compound interest 

def calculate_compound_interest(principal, rate, time, n):
    """
    Calculate the compound interest.

    Args:
        principal (float): The initial amount of money.
        rate (float): The interest rate (in %).
        time (float): The time the money is invested for (in years).
        n (int): The number of times the interest is compounded per year.

    Returns:
        float: The compound interest.
    """
    amount = principal * (1 + rate / 100 / n) ** (n * time)
    ci = amount - principal
    return ci

# Get user input
principal = float(input("Enter the initial amount: "))
rate = float(input("Enter the interest rate (%): "))
time = float(input("Enter the time (in years): "))
n = int(input("Enter the number of times the interest is compounded per year: "))

# Calculate and print the compound interest
ci = calculate_compound_interest(principal, rate, time, n)
print(f"The compound interest is: {ci:.2f}")