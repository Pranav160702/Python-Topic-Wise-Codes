# Write a program that can reverse words of a given string.
# Eg if the input is Hello how are you
# Output should be you are how Hello


def reverse_words(string):
    # Split the string into words
    words = string.split()
    # Reverse the list of words
    reversed_words = words[::-1]
    # Join the reversed list of words back into a string
    return ' '.join(reversed_words)

# Get input from the user
input_string = input("Enter the string: ")
reversed_string = reverse_words(input_string)
print(f"The string with reversed words is: {reversed_string}")

