# Accessing Characters by Positive Index Number
# We can access characters by using positive index numbers. The first character of the string is at index
# 0, the second character is at index 1, and so on. The index number
#  of the last character is the length of the string minus one. For example, the string
#  "banana" has six characters, so the last character is at index 5. The
#  following code prints the last character of the string "banana":
#
# print(banana[5])

# string_1 = " Hello Pranav"

# print(string_1[0])
# print(string_1[1])
# print(string_1[2])
# print(string_1[3])
# print(string_1[4])
# print(string_1[5])


# string_2 = "Python String"
# for i in string_2:
#     print(i)








# Accessing Characters by Negative Index Number
# We can also access characters by using negative index numbers. The last character of the string is at
# index -1, the second-to-last character is at index -2, and so on.
# The first character is at index -6, the second character is at index -5, and
# so on. The following code prints the last character of the string "banana":
#


# string_1 = "Hello Pranav"
# print(string_1[-1])
# print(string_1[-4])
# print(string_1[-9])

# Example Using for Loop
string_2 = "Python String"
for i in range(-1, -len(string_2), -1):
    print(string_2[i])
