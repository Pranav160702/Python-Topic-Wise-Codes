# a = 10
# b = 0
# result = a / b  # ZeroDivisionError: division by zero
# print(result)


# # Creating Object
# ex = ValueError("Write Any Message Here!")
# raise ex


# Raising an Exception
# name = input("Enter Name Here (Must be More than 5 Characters): ")

# if(len(name) < 5):
#     raise ValueError("Name Must be More than 5 Characters")

# print(f"Hello {name}!")


# # Subclasses of Exception class.
# print(issubclass(KeyError, LookupError))

# print(issubclass(KeyError, Exception))


# Exception Hierarchy
ex = KeyError("Some Message...")
print(ex)

print(isinstance(ex, KeyError))

print(isinstance(ex, LookupError))

print(isinstance(ex, Exception))

print(isinstance(ex, InterruptedError))


