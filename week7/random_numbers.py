def main():
    """
    As a team, write a Python program named random_numbers.py that creates a 
    list of numbers, appends more numbers onto the list, and prints the list. 
    The program must have two functions named main and 
    append_random_numbers as follows:

    main
        Has no parameters
        Creates a list named numbers like this:
        numbers = [16.2, 75.1, 52.3]
        Prints the numbers list
        Calls the append_random_numbers function with only one argument to add one number to numbers
        Prints the numbers list
        Calls the append_random_numbers function again with two arguments to add three numbers to numbers
        Prints the numbers list
    append_random_numbers
        Has two parameters: a list named numbers_list and an integer named quantity. The parameter quantity has a default value of 1
        Computes quantity pseudo random numbers by calling the random.uniform function.
        Rounds the quantity pseudo random numbers to one digit after the decimal.
        Appends the quantity pseudo random numbers onto the end of the numbers_list
        
    expected ouput:
    > python random_numbers.py
    numbers [16.2, 75.1, 52.3]
    numbers [16.2, 75.1, 52.3, 84.2]
    numbers [16.2, 75.1, 52.3, 84.2, 99.5, 20.4, 25.3]
    words ['join', 'love', 'smile', 'love', 'cloud', 'head']
    """
    numbers1 = append_random_numbers()
    numbers2 = append_random_numbers()
    words = append_random_words()

    print(f'numbers {numbers1}')
    print(f'numbers {numbers2}')
    print(f'words {words}')


def append_random_numbers(numbers_list, quantity = 1):
    """adds random numbers"""

def append_random_words(words_list, quantity = 1):
    """adds random words"""

if __name__ == "__main__":
    main()
