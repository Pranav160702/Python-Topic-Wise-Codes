# Calculate the angle between the hour hand and minute hand.
import math

def calculate_angle(hour, minute):
    if hour < 0 or hour > 12 or minute < 0 or minute > 60:
        return "Invalid time."

    if hour == 12:
        hour = 0
    if minute == 60:
        minute = 0

    # Calculate the angles moved by hour and minute hands
    minute_angle = 6 * minute
    hour_angle = 30 * hour + 0.5 * minute

    # Calculate the difference between the two angles
    angle = abs(hour_angle - minute_angle)

    # Get the smaller angle
    angle = min(360 - angle, angle)

    # Floor the result
    return math.floor(angle)

# Taking input for the hour and minute
hour = int(input("Enter the hour: "))
minute = int(input("Enter the minute: "))

# Calculate and print the result
result = calculate_angle(hour, minute)
print(f"The angle between the hour hand and the minute hand is: {result} degrees")
