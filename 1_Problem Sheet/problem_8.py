# Write a program to find the euclidean distance between two coordinates.
# d = √(x2 − x1)2 + (y2 − y1)

import math
def euclidean_distance(cord1, cord2):
    x1, y1 = cord1
    x2, y2 = cord2
    return math.sqrt(((x2 - x1)**2 + (y2 - y1)**2))


# Taking input for the first coordinates
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))

# Taking input for the second coordinates
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

distance = euclidean_distance((x1,y1),(x2,y2))
print("The euclidean distance between the two coordinates is",distance)

