"""
The size of a car tire in the United States is represented with
 three numbers like this: 205/60R15. The first number is the 
 width of the tire in millimeters. The second number is the 
 aspect ratio. The third number is the diameter in inches of the
  wheel that the tire fits.
"""
import math

# Get user input
width = input("Enter the width of the tire in mm (ex 205): ")
aspect_ratio = input("Enter the aspect ratio of the tire (ex 60): ")
diameter = input("Enter the diameter of the wheel in inches (ex 15): ")

# Convert string to int in preparation to calculate
w = int(width)
a = int(aspect_ratio)
d = int(diameter)

# Calculate volume
volume = math.pi*w**2*a*(w*a+2540*d)/10000000000

print(f"The approximate volume is {volume:.2f} liters")
