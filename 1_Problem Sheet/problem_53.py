# Count the frequency of a particular character in a provided string. 
# Eg 'hello how are you' is the string, the frequency of h in this string is 2.

def count_char_frequency(string, char):
    return string.lower().count(char.lower())

string = input("Enter a string: ")
char = input("Enter a character: ")

frequency = count_char_frequency(string, char)

print(f"The frequency of '{char}' in '{string}' is {frequency}.")


