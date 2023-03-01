import csv

I_NUMBER_INDEX = 0
NAME_INDEX = 1

def main():
    """During this milestone, you will write half of a Python program
    named receipt.py that prints to the terminal window a receipt for
    a customer’s grocery order. Specifically, by the end of this milestone,
    your program must contain at least these two functions: 
        - main
        - read_dictionary
    
    and must read and process these two CSV files:
        - The products.csv file is a catalog of all the products 
          that the grocery store sells.
        - The request.csv file contains the items ordered by a customer."""
    student_dict = read_dictionary("week9/students.csv", I_NUMBER_INDEX)

    student_id = input('Please enter an I-Number (xxxxxxxxx): ')

    if len(student_id) < 9:
        print('Please enter a valid 9 digit ID')
    elif not student_id.isdigit():
        print('Please enter only digits')
    elif student_id not in student_dict:
        print('No such student')
    else:
        response = student_dict[student_id]
        print(response[NAME_INDEX])
     

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """

    dictionary = {}

    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
                       
        next(reader)

        for row_list in reader:
            if len(row_list) != 0:
                key = row_list[key_column_index]
                dictionary[key] = row_list

    return dictionary

# Expected Output:
# > python students.py
# Please enter an I-Number (xxxxxxxxx): 551234151
# No such student

# > python students.py
# Please enter an I-Number (xxxxxxxxx): 751766201
# James Smith
if __name__ == "__main__":
    main()