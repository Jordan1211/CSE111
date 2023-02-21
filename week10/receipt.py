import csv

from datetime import datetime, time

PRODUCT_NUMBER_INDEX = 0
PRODUCT_NAME_INDEX = 1
PRODUCT_PRICE_INDEX = 2
QUANTITY_INDEX = 1

def main():
    """Print the store name at the top of the receipt.
    Print the list of ordered items.
    Sum and print the number of ordered items.
    Sum and print the subtotal due.
    Compute and print the sales tax amount. Use 6% as the sales tax rate.
    Compute and print the total amount due.
    Print a thank you message.
    Get the current date and time from your computer’s operating system and 
    print the current date and time. Include a try block and except blocks 
    to handle FileNotFoundError, PermissionError, and KeyError."""
    try:
        products_file = "products.csv"
        request_file = "request.csv"
        products_dict = read_dictionary(products_file, PRODUCT_NUMBER_INDEX)
        current_date_and_time = datetime.now()

        print('Inkom Emporium')

        process_requests(products_dict, request_file)

        print(f'Thank you for shopping at Inkom Emporium.')
        print(f'{current_date_and_time:%a %b %d %I:%M:%S %Y}')

    except FileNotFoundError as not_found_err:
        print()
        print('Error: missing file')
        print(not_found_err)
    
    except PermissionError as perm_err:
        print()
        print(perm_err)
    
    except KeyError as key_err:
        print()
        print(f'Error: unknown product ID in the {request_file} file')
        print(key_err)



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

def process_requests(products_dict, request_file):
    now = datetime.now()
    day_of_week = datetime.now().weekday()
    time_of_day = int(f'{now:%H}')

    with open(request_file, mode="rt") as requests_file:
        reader = csv.reader(requests_file)
        next(reader)
        
        print()
        print('Requsted items:')
        total_items = 0
        total_price = 0

        for request in reader:
            product_number = request[PRODUCT_NUMBER_INDEX]
            quantity = int(request[QUANTITY_INDEX])
            product_name = products_dict[product_number][PRODUCT_NAME_INDEX]
            product_price = float(products_dict[product_number][PRODUCT_PRICE_INDEX])
            total_items += quantity
            total_price += product_price*quantity

            print(f'{product_name}: {quantity} @ ${product_price}')
        if day_of_week == 1 or day_of_week == 2 or time_of_day < 11:
            discount = .1 * total_price
        else: discount = 0

        tax = total_price * .06
        final_total = (total_price + tax) - discount
        
        print()
        print(f'Number of Items: {total_items}')
        print(f'Subtotal: ${total_price:.2f}')
        print(f'Sales Tax: ${tax:.2f}')
        print(f'Discount: ${discount:.2f}')
        print(f'Total: ${final_total:.2f}')
        print()
        print(f'*Discounts are provided if orders are placed')
        print(f' before 11am or all day on Tuesday and Wednesday*')
        print()


if __name__ == "__main__":
    main()
