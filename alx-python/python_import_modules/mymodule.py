# def print_max(x, y):
    
#     x = int(x)
#     y = int(y)

#     if x > y:
#         print(x, 'is maximum')
#     else:
#         print(y, 'is maximum')

# print_max(3, 5)
# print_max()


# def total(a=5, *numbers, **phonebook):
#     print('a', a)

#     #iterate through all the items in tuple
#     for single_item in numbers:
#         print('single_item', single_item)

#     #iterate through all the items in dictionary    
#     for first_part, second_part in phonebook.items():
#         print(first_part,second_part)

# total(10,1,7,3,Jack=1123,John=2231,Inge=1560)

# def maximum(x, y):
#     if x > y:
#         return x
#     elif x == y:
#         return 'The numbers are equal'
#     else:
#         return y

# print(maximum(2, 2))

# def some_function():
#     pass

# import sys

# print('The command line arguments are:')
# for i in sys.argv:
#     print(i)

# print('\n\nThe PYTHONPATH is', sys.path, '\n')

# import os; print(os.getcwd())

# from math import sqrt
# print("Square root of 16 is", sqrt(16))

# if __name__ == '__main__':
#     print('This program is being run by itself')
# else:
#     print('I am being imported from another module')
    
# def say_hi():
#     print('Hi, this is mymodule speaking.')

# __version__ = '0.1'

# import mymodule

# mymodule.say_hi()
# print('Version', mymodule.__version__)

import sys
dir(sys)
['__displayhook__', '__doc__',
'argv', 'builtin_module_names',
'version', 'version_info']

dir()
['__builtins__', '__doc__',
'__name__', '__package__', 'sys']

a = 5
dir()
['__builtins__', '__doc__', '__name__', '__package__', 'sys', 'a']

del a