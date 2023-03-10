import random

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
    numbers = [16.2, 75.1, 52.3]
    print(f'Original numbers list: {numbers}')

    append_random_numbers(numbers)
    print(f'Numbers, one appended: {numbers}')

    append_random_numbers(numbers,3)
    print(f'Numbers, three appended: {numbers}')
  
    words = []
    
    append_random_words(words)
    print(f'words: {words}')

    append_random_words(words,5)
    print(f'words five appended: {words}')


def append_random_numbers(numbers_list, quantity=1):
    """adds random numbers"""
    for i in range(quantity):
        random_number = random.uniform(0, 100)
        rounded_random_number = round(random_number, 1)
        numbers_list.append(rounded_random_number)


def append_random_words(words_list, quantity = 1):
    """adds random words"""
    word_bank = ["worker","grace","hotdog","claim","divide","hard",
                    "aware","disagree","bleed","fairy","heavy",
                    "biography","throat","ratio","thanks","how","now"
                    "brown","cow","dog","hit","me","one","more","time"]
    
    for i in range(quantity):
        random_word = random.choice(word_bank)
        words_list.append(random_word)

if __name__ == "__main__":
    main()
