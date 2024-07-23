# Write a program that can check whether a given string is palindrome or not.


def is_palindrome(string):
    # Remove any spaces and convert the string to lowercase for accurate comparison
    cleaned_string = string.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    return cleaned_string == cleaned_string[::-1]

# Get input from the user
input_string = input("Enter the string to check: ")

# Check if the input string is a palindrome
if is_palindrome(input_string):
    print(f"The string '{input_string}' is a palindrome.")
else:
    print(f"The string '{input_string}' is not a palindrome.")
