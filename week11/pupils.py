import csv


# Each row in the pupils.csv file contains three elements.
# These are the indexes of the elements in each row.
GIVEN_NAME_INDEX = 0
SURNAME_INDEX = 1
BIRTHDATE_INDEX = 2

def main():
    students_list = read_compound_list('pupils.csv')
    birthdate_func = lambda birthdate: birthdate[BIRTHDATE_INDEX]
    given_name_func = lambda given_name: given_name[GIVEN_NAME_INDEX]
    birthdate_noyear_func = lambda birthdate: birthdate[BIRTHDATE_INDEX][5:]
    birthdate_sorted_list = sorted(students_list, key=birthdate_func)
    given_name_sorted_list = sorted(students_list, key=given_name_func)
    birthdate_noyear_sorted_list = sorted(students_list, key=birthdate_noyear_func)

    print()
    print('Ordered from Oldest to Youngest')
    print_list(birthdate_sorted_list)
    print()

    print()
    print('Ordered by Given Name')
    print_list(given_name_sorted_list)
    print()

    print()
    print('Ordered by Birth Month and Day')
    print_list(birthdate_noyear_sorted_list)
    print()

def read_compound_list(filename):
    """Read the text from a CSV file into a compound list.
    The compound list will contain small lists. Each small
    list will contain the data from one row of the CSV file.

    Parameter
        filename: the name of the CSV file to read.
    Return: the compound list
    """
    # Create an empty list.
    compound_list = []

    # Open the CSV file for reading.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column headings
        # and not a student's I-Number and name, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:

            # Append the current row at the end of the compound list.
            compound_list.append(row)

    return compound_list

def print_list(list):
    for i in list:
        print(i)


# Call main to start this program.
if __name__ == "__main__":
    main()