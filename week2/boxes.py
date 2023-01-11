"""
Asks for two integers:
  the number of manufactured items
  the number of items that the user will pack per box

Your program must compute and print the number of boxes necessary 
to hold the items. This must be a whole number. Note that the last 
box may be packed with fewer items than the other boxes.
"""
import math 

# Get user input
item_count = input("Enter the number of items: ")
box_size = input("Enter the number of items per box: ")

# Convert string to int in preparation to calculate
ic = int(item_count)
bs = int(box_size)

# Calculate volume
box_count = math.ceil(ic/bs)

#print results
print()
print(f"For {item_count} items, packing {box_size} items in each box, you will need {box_count:.0f} boxes.")
print()