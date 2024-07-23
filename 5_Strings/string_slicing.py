# String Slicing
# Extracting from the beginning: 
# =============================
# print("Hello"[0:2]) # prints "He"
# print("Hello"[0:3]) # prints "Hel"
# print("Hello"[0:4]) # prints "Hell"
# print("Hello"[0:5]) # prints "Hello"

# string = "Hello, World!"
# substring = string[:5]  # "Hello"
# print(substring)


# # Extracting from specific index:
# # =============================

# string = "Hello, World!"
# substring = string[7:]  # "World!"
# print(substring)


# # Extracting a section:
# # ============================
# string = "Hello, World!"
# substring = string[2:7]  # "llo, W"
# print(substring)


# # Steps
# # ============================
# string = "Hello, World!"
# substring = string[::2]  # "Hlo ol!"
# substring_2 = string[2:7:2]  # "l o"

# print(substring)
# print(substring_2)


# # Negative Stepping
# # ============================
# string = "Hello, World!"
# substring = string[ : :-1]  # " !dlroW ,olle
# substring_2 = string[-1:-7:-1]  # " !dlroW ,olle
# print(substring)
# print(substring_2)


