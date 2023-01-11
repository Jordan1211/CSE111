"""
The size of a car tire in the United States is represented with
 three numbers like this: 205/60R15. The first number is the 
 width of the tire in millimeters. The second number is the 
 aspect ratio. The third number is the diameter in inches of the
  wheel that the tire fits.

  For week 2 we are adding the date and appending the text to a file
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

# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()

# additional exceeds requirement for adding price to volumes.txt file
intent = input("Would you like to purchase tires with these dimensions? (Please enter Y or N): ")
while True:
        if w == 185 and a == 50 and d == 14:
            price = "$172.22"
            break
        elif w == 185 and a == 60 and d == 15:
            price = "$81.80"
            break
        elif w == 205 and a == 60 and d == 15:
            price = "$83.99"
            break
        elif w == 215 and a == 60 and d == 15:
            price = "$96.00"
            break
        else:
            price = "unlisted"
            break

# Open a text file named volumes.txt in append mode.
with open("volumes.txt", "at") as volumes_file:

    # Print current date, width of the tire, aspect ratio of the tire
    # diameter of the wheel and volume of the tire as well as the price
    print(f"{current_date_and_time:%Y-%m-%d}, {w}, {a}, {d}, {volume:.2f}, Tire price: {price}", file=volumes_file)

# additional exceeds requirement for inquiring of purchase intent and if Y asking for phone number
while True:
    if intent == "Y":
        phone = input("Please enter your phone number for a representative to help (Please format as XXX-XXX-XXXX): ")
        with open("volumes.txt", "at") as volumes_file:
            print(f"Phone number for prior dimensions outreach: {phone}", file=volumes_file)
        break
    elif intent == "N":
        print("Please reach out again if you are interested in the future! Goodbye")
        break

    else:
        print("Answered in an invalid format")
        continue
