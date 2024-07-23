# Find the length of a given string without using the len() function. 
# Input: "Python"
# Output: 6
def length(s):
    count = 0
    for i in s:
        count += 1
    return count

s = input("Enter a String:")
print("Length of the string is: ", length(s))