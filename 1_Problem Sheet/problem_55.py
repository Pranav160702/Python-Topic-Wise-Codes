# Count the number of vowels in a string provided by the user.
# Vowels are the characters a, e, i, o, u.


def count_vowels():
    user_input = input("Please enter a string: ")
    vowels = "aeiou"
    count = 0
    for char in user_input.lower():
        if char in vowels:
            count += 1
    print(f"The string contains {count} vowels.")

count_vowels()