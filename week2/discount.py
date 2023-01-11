"""
Work as a team to write a Python program named discount.py that gets a 
customer’s subtotal as input and gets the current day of the week from your 
computer’s operating system. Your program must not ask the user to enter 
the day of the week. Instead, it must get the day of the week from your 
computer’s operating system.

If the subtotal is $50 or greater and today is Tuesday or Wednesday, your 
program must subtract 10% from the subtotal. Your program must then compute
the total amount due by adding sales tax of 6% to the subtotal. Your program
must print the discount amount if applicable, the sales tax amount, and 
the total amount due.
"""
# Get user input
subtotal = input("Please enter the subtotal of your order: ")

# Convert string to int in preparation to calculate
s = float(subtotal)

# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()
day_of_week = 2 
# current_date_and_time.weekday()

# Calculate discount
while True:
    if s > 50 and (day_of_week == 1 or 2):
        discount = s * 0.1
        break
    else:
        discount = 0
        break

subtotal_discount = s - discount
tax = subtotal_discount * 0.06
total = subtotal_discount + tax

print(f"The discount is ${discount:.2f}")
print(f"The tax is ${tax:.2f}")
print(f"The total is ${total:.2f}")



# # additional exceeds requirement for adding price to volumes.txt file
# intent = input("Would you like to purchase tires with these dimensions? (Please enter Y or N): ")
# while True:
#         if w == 185 and a == 50 and d == 14:
#             price = "$172.22"
#             break
#         elif w == 185 and a == 60 and d == 15:
#             price = "$81.80"
#             break
#         elif w == 205 and a == 60 and d == 15:
#             price = "$83.99"
#             break
#         elif w == 215 and a == 60 and d == 15:
#             price = "$96.00"
#             break
#         else:
#             price = "unlisted"
#             break

# # Open a text file named volumes.txt in append mode.
# with open("volumes.txt", "at") as volumes_file:

#     # Print current date, width of the tire, aspect ratio of the tire
#     # diameter of the wheel and volume of the tire as well as the price
#     print(f"{current_date_and_time:%Y-%m-%d}, {w}, {a}, {d}, {volume:.2f}, Tire price: {price}", file=volumes_file)

# # additional exceeds requirement for inquiring of purchase intent and if Y asking for phone number
# while True:
#     if intent == "Y":
#         phone = input("Please enter your phone number for a representative to help (Please format as XXX-XXX-XXXX): ")
#         with open("volumes.txt", "at") as volumes_file:
#             print(f"Phone number for prior dimensions outreach: {phone}", file=volumes_file)
#         break
#     elif intent == "N":
#         print("Please reach out again if you are interested in the future! Goodbye")
#         break

#     else:
#         print("Answered in an invalid format")
#         continue
