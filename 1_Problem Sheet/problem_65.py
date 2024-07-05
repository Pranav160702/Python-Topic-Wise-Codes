# Write a program that can count the number of words in a given string

def count_words(string):
    # Split the string into words
    words = string.split()
    # Count the number of words
    return len(words)

# Get input from the user
input_string = input("Enter the string: ")
word_count = count_words(input_string)
print(f"The number of words in the string is: {word_count}")
