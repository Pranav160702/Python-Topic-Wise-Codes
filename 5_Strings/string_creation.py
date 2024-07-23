# # String Creation Using Single Quotes
# # ===================================
# single_quote_string = 'Hello, World!'
# single_quote_with_double = 'He said, "Hello!"'

# print(single_quote_string)      # Output: Hello, World!
# print(single_quote_with_double) # Output: He said, "Hello!"



# # String Creation Using Double Quotes
# # ====================================
# double_quote_string = "Hello, World!"
# double_quote_with_single = "He said, 'Hello!'"

# print(double_quote_string)      # Output: Hello, World!
# print(double_quote_with_single) # Output: He said, 'Hello!'


# # String Creation Using Triple Quotes
# # ===================================
# triple_quote_string = '''Hello, World!'''
# triple_quote_with_single = """He said, 'Hello!' """
# triple_quote_with_double = '''He said, "Hello!"'''

# print(triple_quote_string)      # Output: Hello, World!
# print(triple_quote_with_single) # Output: He said, 'Hello!'
# print(triple_quote_with_double) # Output: He said, "Hello!"

# # Multiline String
# # =================
# triple_quote_string = '''Hello, World!
# This is a multiline string!'''
# print(triple_quote_string)  # Output: Hello, World! 
#                             #         This is a multiline string!



# # String Creating Using Escape Character
# # ======================================
# escape_single_quote = 'It\'s a beautiful day!'
# print(escape_single_quote)  # Output: It's a beautiful day!

# escape_double_quote = "He said, \"Hello, World!\""
# print(escape_double_quote)  # Output: He said, "Hello, World!"


# # # String Creatio  n Using Raw String
# # # ================================
# raw_string = r'C:\Users\Public'
# print(raw_string)  # Output: C:\Users\Public


# # String Creation Using str() Constructor
# # ======================================
# # str() constructor takes an object and returns a string object
# str_object = str('Hello, World!')
# print(str_object)  # Output: Hello, World!

# number = 123
# number_string = str(number)
# print(number_string)  # Output: 123

# boolean = True
# boolean_string = str(boolean)
# print(boolean_string)  # Output: True


text = "This text will be deleted"
del text
print(text)
# Now you cannot access the variable 'text'
