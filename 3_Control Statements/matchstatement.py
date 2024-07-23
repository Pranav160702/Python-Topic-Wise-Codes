# Literal Patterns
# ================
#
# A literal pattern is a pattern that matches a specific value.
#
# For example, the pattern `1` matches the value `1`, and the pattern `"hello
# world"` matches the string `"hello world"`
#
# Here's an example of using a literal pattern in a `match` expression:
#
# def identify_literal(value):
#     match value:
#         case 1:
#             return "One"
#         case "hello":
#             return "Greeting"
#         case True:
#             return "Truth"
#         case (1, 2):
#             return "Tuple"
#         case _:
#             return "Unknown"

# print(identify_literal(1))       # Output: One
# print(identify_literal("hello")) # Output: Greeting
# print(identify_literal(True))    # Output: Truth
# print(identify_literal((1, 2)))  # Output: Tuple
# print(identify_literal(3))       # Output: Unknown



# Variable Patterns
# ================
#
# A variable pattern is a pattern that matches any value and binds it to a
# variable.
#
# For example, the pattern `x` matches any value and binds it to the variable
# `x`
#
# def identify_variable(value):
#     match value:
#         case 0:
#             return "Zero"
#         case x:
#             return f"Value: {x}"

# print(identify_variable(0))    # Output: Zero
# print(identify_variable(10))   # Output: Value: 10
# print(identify_variable("abc")) # Output: Value: abc



# Sequence Patterns
# =================
#
# A sequence pattern is a pattern that matches a sequence (such as a list or
# tuple) and binds its elements to variables.
#
# For example, the pattern `(x, y)` matches a sequence of two elements and binds
# them to the variables `x` and `y`
#
# def identify_sequence(seq):
#     match seq:
#         case [1, 2, 3]:
#             return "Exact List"
#         case [1, 2, *rest]:
#             return f"Starts with 1, 2 and the rest is {rest}"
#         case (1, 2, 3):
#             return "Exact Tuple"
#         case (1, 2, *rest):
#             return f"Starts with 1, 2 and the rest is {rest}"
#         case _:
#             return "Unknown Sequence"

# print(identify_sequence([1, 2, 3]))       # Output: Exact List
# print(identify_sequence([1, 2, 4, 5]))    # Output: Starts with 1, 2 and the rest is [4, 5]
# print(identify_sequence((1, 2, 3)))       # Output: Exact Tuple
# print(identify_sequence((1, 2, 4, 5)))    # Output: Starts with 1, 2 and the rest is (4, 5)
# print(identify_sequence([4, 5, 6]))       # Output: Unknown Sequence


# Mapping Patterns
# =================
#
# A mapping pattern is a pattern that matches a mapping (such as a dictionary) and
# binds its keys and values to variables.
#
# For example, the pattern `{x: 1, y: 2}` matches a mapping
# with keys `x` and `y` and values `1` and `2`, respectively
#
# def identify_mapping(mapping):
#     match mapping:
#         case {"type": "click", "position": (x, y)}:
#             return f"Click at ({x}, {y})"
#         case {"type": "keypress", "key": k}:
#             return f"Keypress: {k}"
#         case _:
#             return "Unknown mapping"

# print(identify_mapping({"type": "click", "position": (10, 20)}))  # Output: Click at (10, 20)
# print(identify_mapping({"type": "keypress", "key": "Enter"}))     # Output: Keypress: Enter
# print(identify_mapping({"type": "scroll"}))                       # Output: Unknown mapping


# Class patterns
# =============
#
# A class pattern is a pattern that matches an instance of a class and binds its
# attributes to variables.
#
# For example, the pattern `Point(x, y)` matches an instance of the `Point`
# class with attributes `x` and `y`
#
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# def identify_class(obj):
#     match obj:
#         case Point(x=0, y=0):
#             return "Origin"
#         case Point(x, y):
#             return f"Point at ({x}, {y})"
#         case _:
#             return "Not a point"

# p1 = Point(0, 0)
# p2 = Point(3, 4)

# print(identify_class(p1))  # Output: Origin
# print(identify_class(p2))  # Output: Point at (3, 4)


# Gaurds
# =======
#
# A guard is a conditional expression that is evaluated after the pattern has
# matched. If the guard is true, the pattern is considered to have matched.
#
# For example, the pattern `Point(x, y) if x == y` matches an instance
# of the `Point` class with attributes `x` and `y` only if `x
# equals `y`
#
# def identify_guard(value):
#     match value:
#         case x if x > 0:
#             return "Positive"
#         case x if x < 0:
#             return "Negative"
#         case _:
#             return "Zero"

# print(identify_guard(10))  # Output: Positive
# print(identify_guard(-5))  # Output: Negative
# print(identify_guard(0))   # Output: Zero


# Combining Patterns
# =================
#
# You can combine multiple patterns using the `|` operator.
#
# For example, the pattern `Point(0, 0) | Point(0, y
# )` matches an instance of the `Point` class with attributes `x` and `y
# only if `x` is 0 and `y` is any value.
#
def identify_combined(value):
    match value:
        case "red" | "blue" | "green":
            return "Primary color"
        case "yellow" | "cyan" | "magenta":
            return "Secondary color"
        case _:
            return "Unknown color"

print(identify_combined("red"))      # Output: Primary color
print(identify_combined("yellow"))   # Output: Secondary color
print(identify_combined("black"))    # Output: Unknown color


