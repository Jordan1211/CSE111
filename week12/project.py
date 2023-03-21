import csv

from datetime import datetime, time

def main():
    """ """
    try:
        length = float(input('Please provide the LENGTH of the area in feet: '))
        width = float(input('Please provide the WIDTH of the area in feet: '))
        depth = float(input('Please provide the DEPTH of the area in feet: '))
        cost = float(input('Please give the current price: '))

        cubic_yards = calculate_cubic_yards(length, width, depth) 
        total_price = calculate_price(cubic_yards, cost)

        current_date_and_time = datetime.now()

        print()
        print(f'Your Price is ${total_price:.2f}.')
        print(f'Quote Date: {current_date_and_time:%a %b %d %I:%M:%S %Y}')

    except FileNotFoundError as not_found_err:
        print()
        print('Error: missing file')
        print(not_found_err)
    
    except PermissionError as perm_err:
        print()
        print(perm_err)
    
    # except KeyError as key_err:
    #     print()
    #     print(f'Error: unknown product ID in the {request_file} file')
    #     print(key_err)




def calculate_cubic_yards(l, w, d):
    """Calculates area"""
    area = l*w*d
    area_by_foot = area / 12
    cubic_yards = area_by_foot / 27

    return cubic_yards

def calculate_price(cubic_yards, cost):
    """Calculates price"""
    total_price = cubic_yards * cost

    return total_price

if __name__ == "__main__":
    main()
