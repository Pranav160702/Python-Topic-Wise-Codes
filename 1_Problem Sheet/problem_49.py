# Write a program that keeps on accepting a number from the user until the user enters Zero. 
# Display the sum and average of all the numbers.

def calculate_sum_and_average():
    total = 0
    count = 0
    while True:
        num = float(input("Enter a number (0 to quit): "))
        if num == 0:
            break
        total += num
        count += 1
    if count == 0:
        print("You didn't enter any numbers.")
    else:
        average = total / count
        print(f"Sum: {total:.2f}")
        print(f"Average: {average:.2f}")


calculate_sum_and_average()