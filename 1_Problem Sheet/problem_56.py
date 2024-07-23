# Write a program which can remove a particular character from a string. 

def remove_character(string, char_to_remove):
    return string.replace(char_to_remove, '')

# Get input from the user
input_string = input("Enter the string: ")
char_to_remove = input("Enter the character to remove: ")

# Ensure the user enters exactly one character to remove
while len(char_to_remove) != 1:
    char_to_remove = input("Please enter a single character to remove: ")

result_string = remove_character(input_string, char_to_remove)
print(f"The string after removing '{char_to_remove}' is: {result_string}")
