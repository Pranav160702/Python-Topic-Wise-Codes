# Write a python program to convert a string to title case without using the title()

def to_title_case(string):
    words = string.split()
    title_cased_words = [word.capitalize() for word in words]
    return ' '.join(title_cased_words)

# Get input from the user
input_string = input("Enter the string to convert to title case: ")
title_cased_string = to_title_case(input_string)
print(f"The title cased string is: {title_cased_string}")
