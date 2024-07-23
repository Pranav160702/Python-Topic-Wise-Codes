# Write a program to find the volume of the cylinder. Also find the cost when ,when the cost of 1 litre milk is 40Rs.
# Volume of cylinder = πr^2h
# Cost of 1 litre milk = 40Rs
# Code
import math

def calculate_cylinder_valume(radius,height):
    return math.pi * radius * radius * height
    

def calculate_cost(volume):
    return volume * 40


radius = float(input("Enter the Radius of the Cylinder: "))
height = float(input("Enter the Height of the Cylinder: "))

volume = calculate_cylinder_valume(radius,height)
print("Volume of the Cylinder is: ",volume)

cost = calculate_cost(volume)
print("Cost of the Cylinder is: ",cost)

