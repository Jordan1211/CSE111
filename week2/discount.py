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
day_of_week = current_date_and_time.weekday()

# Calculate discount
if s > 50 and (day_of_week == 1 or day_of_week == 2):
    discount = s * 0.1
else:
    discount = 0

subtotal_discount = s - discount
tax = subtotal_discount * 0.06
total = subtotal_discount + tax
discount_diff = 50 - s

if discount > 0:
    print(f"The discount is ${discount:.2f}")
else:
    print(f"You need to purchase ${discount_diff:.2f} more in merchandise to receive a 10% discount")
print(f"The tax is ${tax:.2f}")
print(f"The total is ${total:.2f}")

