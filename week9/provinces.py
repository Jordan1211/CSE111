def main():
    """Code to do the following:
            Open the provinces.txt file for reading.
            Read the contents of the file into a list where each line of text in the file is stored in a separate element in the list.
            Print the entire list.
            Remove the first element from the list.
            Remove the last element from the list.
            Replace all occurrences of "AB" in the list with "Alberta".
            Count the number of elements that are "Alberta" and print that number.
"""
    provinces = read_list('week9/provinces.txt')

    count = clean_list(provinces)

    print(provinces)
    print(f'There are {count} provinces listed as Alberta')

def read_list(filename):
    text_list = []

    with open(filename, 'rt') as text_file:

        for line in text_file:

            clean_line = line.strip()

            text_list.append(clean_line)

    return text_list

def clean_list(provinces):
    """removes first item in list"""
    provinces.pop(0)
    provinces.pop()


    for i in range(len(provinces)):
        if provinces[i] == "AB":
            provinces[i] = "Alberta"

    count = provinces.count('Alberta')


    return count


def count_alberta(list4):
    """counts items in list that are = to Alberta"""

if __name__ == "__main__":
    main()

# Expected output:
# > python provinces.py
# ['Alberta', 'Ontario', 'Prince Edward Island', 'Ontario',
# 'Quebec', 'Saskatchewan', 'AB', 'Nova Scotia', 'Alberta',
# 'Northwest Territories', 'Saskatchewan', 'Nunavut',
# 'Nova Scotia', 'Prince Edward Island', 'Alberta',
# 'Nova Scotia', 'Nova Scotia', 'Prince Edward Island',
# 'British Columbia', 'Ontario', 'Ontario',
# 'Newfoundland and Labrador', 'Ontario', 'Ontario',
# 'Saskatchewan', 'Nova Scotia', 'Prince Edward Island',
# 'Saskatchewan', 'Ontario', 'Newfoundland and Labrador',
# 'Ontario', 'British Columbia', 'Manitoba', 'Ontario',
# 'Alberta', 'Saskatchewan', 'Ontario', 'Yukon', 'Ontario',
# 'New Brunswick', 'British Columbia', 'Manitoba', 'Yukon',
# 'British Columbia', 'Manitoba', 'Yukon',
# 'Newfoundland and Labrador', 'Ontario', 'Yukon', 'Ontario',
# 'AB', 'Nova Scotia', 'Newfoundland and Labrador', 'Yukon',
# 'Nunavut', 'Northwest Territories', 'Nunavut', 'Yukon',
# 'British Columbia', 'Ontario', 'AB', 'Saskatchewan',
# 'Prince Edward Island', 'Saskatchewan',
# 'Prince Edward Island', 'Alberta', 'Ontario', 'Alberta',
# 'Manitoba', 'AB', 'British Columbia', 'Alberta']

# Alberta occurs 9 times in the modified list.