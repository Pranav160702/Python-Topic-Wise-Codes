# Write a program that take a user input of three angles and will find out whether it can form a triangle or not.

def can_form_triangle(angle1, angle2, angle3):
    if angle1 <= 0 or angle2 <= 0 or angle3 <= 0:
        return False
    if angle1 + angle2 + angle3 != 180:
        return False
    return True

angle1 = int(input("Enter the First Angle: "))
angle2 = int(input("Enter the Second Angle: "))
angle3 = int(input("Enter the Third Angle: "))

if can_form_triangle(angle1, angle2, angle3):
    print("The Triangle can be formed")
else:
    print("The Triangle can not be formed")