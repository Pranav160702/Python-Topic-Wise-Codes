# String Concatenation
# Concatenation is the process of joining two strings together.
# In Python, we can concatenate strings using the + operator.
# For example, if we have two strings, "Hello" and "World", we can concatenate
# them using the + operator to get "HelloWorld".
# We can also concatenate strings with other data types, such as integers and floats.
# For example, if we have a string "Hello" and an integer 5, we can

# word1 = "Hello"
# word2 = "World"
# greeting = word1 + " " + word2  # Add a space between words
# print(greeting)                 # Output: Hello World


# word1 = "Hello"
# var1 = 16
# greeting = word1 + var1  
# print(greeting)                 # Output: Hello16


# Multiplication
# We can also multiply strings using the * operator.
# For example, if we have a string "Hello", we can multiply it by 3 to
# get "HelloHelloHello".

# letter = "Hello"
# print(letter,"Pranav"*2)    # Output: Hello PranavPranav


# Logial operators
# =============================================================================================

# # Equal
# text1 = "Hello"
# text2 = "Hello"
# result = text1 == text2
# print(result)           # Output: True

# # Not Equal
# text1 = "Hi"
# text2 = "Hello"   
# result = text1 != text2
# print(result)           # Output: True

# # Less than
# word1 = "Apple"
# word2 = "Banana"
# result = word1 < word2  # "A" in Apple comes before "B" in Banana
# print(result)           # Output: True


# # # Greater than
# color1 = "Green"
# color2 = "Blue"
# result = color1 > color2  # "B" in Blue comes before "G" in Green
# print(result)             # Output: True


# # Less than Equal 
# animal1 = "Cat"
# animal2 = "Cat"
# result = animal1 <= animal2  # Both strings are equal
# print(result)                # Output: True


# # Greater Than Equal to
# fruit1 = "Orange"
# fruit2 = "Apple"
# result = fruit1 >= fruit2  # "O" in Orange comes after "A" in Apple
# print(result)              # Output: True

# Logical Operations
# =============================================================================================
# # And
# username = "Alice"
# password = "secret"

# if username and password:  # Both username and password are non-empty strings (True)
#   print("Login successful!")
# else:
#   print("Invalid username or password.")


# # # Or
# # =======
# is_registered = "yes"
# email = ""  # Empty string

# if is_registered or email:  # "is_registered" is True (non-empty string)
#   print("User record found.")
# else:
#   print("User not found.")

# Not
# =====
# message = "Hello, world!"

# if not message:  # message is a non-empty string (evaluates to False)
#   print("The message is empty.")
# else:
#   print("The message is not empty.")


# Loops
# =============================================================================================
# # # For Loop
# message = "Hello, world!"

# for char in message:
#   print(char)  # Prints each character on a new line


# for index, char in enumerate("Python"):
#   print(f"Index: {index}, Character: {char}")

# # Output
# # Index: 0, Character: P
# # Index: 1, Character: y
# # Index: 2, Character: t
# # Index: 3, Character: h
# # Index: 4, Character: o
# # Index: 5, Character: n


# greeting = "Hi There!"

# for char in greeting:
#   if char.isupper():  # Check if the character is uppercase
#     print(char, end=" ")  # Print only uppercase characters with a space

# # Output: H T


# name = "Alice"

# for char in name[::-1]:
#   print(char, end="")  # Print characters in reverse order

# # Output: ecilA


# Membership Operators
# =============================================================================================
# # # # in Operator
# text = "Welcome to Python programming"
# substring = "Python"

# if substring in text:
#   print("'Python' is present in the text")
# else:
#   print("'Python' is not present in the text")

# # Output: 'Python' is present in the text

# not in 
text = "This is a sample text"
substring = "Java"

if substring not in text:
  print("'Java' is not present in the text")
else:
  print("'Java' is present in the text")

#  Output: 'Java' is not present in the text
