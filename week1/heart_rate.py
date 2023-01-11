"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""
#Get user input
age = input("Please enter your age: ")

#Convert string to int and calculate max heart rate
max = 220 - int(age)

#Calculate top and bottom of range
bottom = max * .65
top = max * .85

print(f"When you exercise to strengthen your heart,")
print(f"you should keep your heart rate")
print(f"between {bottom:.0f} and {top:.0f} beats per minute.")