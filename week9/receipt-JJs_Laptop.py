import csv

PRODUCT_NUMBER_INDEX = 0
PRODUCT_NAME_INDEX = 1
PRODUCT_PRICE_INDEX = 2
QUANTITY_INDEX = 1

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
    
    products_dict = read_dictionary("week9/products.csv", PRODUCT_NUMBER_INDEX)
    print("All Products")
    print(products_dict)
    print()

    read_requests(products_dict)

     

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

def read_requests(products_dict):
    with open("week9/request.csv", mode="rt") as requests_file:
        reader = csv.reader(requests_file)
        next(reader)

        print('Requsted items')

        for request in reader:
            product_number = request[PRODUCT_NUMBER_INDEX]
            quantity = request[QUANTITY_INDEX]

            print(f'{products_dict[product_number][PRODUCT_NAME_INDEX]}: {quantity} @ ${products_dict[product_number][PRODUCT_PRICE_INDEX]}')

# Expected Output:
# All Products
# {'D150': ['D150', '1 gallon milk', '2.85'], 'D083': ['D083',
# '1 cup yogurt', '0.75'], 'D215': ['D215', '1 lb cheddar
# cheese', '3.35'], 'P019': ['P019', 'iceberg lettuce',
# '1.15'], 'P020': ['P020', 'green leaf lettuce', '1.79'],
# 'P021': ['P021', 'butterhead lettuce', '1.83'], 'P025':
# ['P025', '8 oz arugula', '2.19'], 'P143': ['P143', '1 lb
# baby carrots', '1.39'], 'W231': ['W231', '32 oz granola',
# '3.21'], 'W112': ['W112', 'wheat bread', '2.55'], 'C013':
# ['C013', 'twix candy bar', '0.85'], 'H001': ['H001', '8
# rolls toilet tissue', '6.45'], 'H014': ['H014', 'facial
# tissue', '2.49'], 'H020': ['H020', 'aluminum foil', '2.39'],
# 'H021': ['H021', '12 oz dish soap', '3.19'], 'H025':
# ['H025', 'toilet cleaner', '4.50']}

# Requested Items
# wheat bread: 2 @ 2.55
# 1 cup yogurt: 4 @ 0.75
# 32 oz granola: 1 @ 3.21
# twix candy bar: 2 @ 0.85
# 1 cup yogurt: 3 @ 0.75
if __name__ == "__main__":
    main()