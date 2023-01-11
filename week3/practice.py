# def function_name(param1, param2, … paramN):
#     """documentation string"""
#     statement1
#     statement2
#         ⋮
#     statementN
#     return value



from datetime import datetime

#function returns date and time and param of task name
def print_time(task_name):
        print(task_name)
        print(datetime.now())
        print()

print_time('test date funct')

#function returns an inital from name inputs
def get_initial(name, force_uppercase=True):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial

first_name = input('Enter your first name: ')
middle_name = input('Enter your middle name: ')
last_name = input('Enter your last name: ')

##calls get_inital function within print
print (f'Your initials are: {get_initial(first_name)}{get_initial(middle_name)}{get_initial(last_name, False)}')