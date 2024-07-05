# Find the index position of a particular character in another string. 

def find_char_index(string, char):
    try:
        index = string.index(char)
        return f"The character '{char}' is at index {index} in the string '{string}'."
    except ValueError:
        return f"The character '{char}' is not found in the string '{string}'."


# take input from user
string = input("Enter a string: ")
char = input("Enter a character: ")

print(find_char_index(string, char))  