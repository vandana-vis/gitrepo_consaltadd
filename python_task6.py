
# 1) Write a program in Python to find out the character in a string which is uppercase using list comprehension.
strng = "This is Python List"
# Using list comprehension + isupper()
list1 = [i for i in strng if i.isupper()]

print("The uppercase characters in string are : " + str(list1))

# ======================================================================================
# 2) Write a program to construct a dictionary from the two lists containing the names of students and
# their corresponding subjects. The dictionary should map the students with their respective subjects.
# Let’s see how to do this using for loops and dictionary comprehension.
students = ['Smit', 'Jaya', 'Rayyan']
subjects = ['CSE', 'Networking', 'Operating System']

dict1 = dict(zip(students, subjects))
print(dict1)

# ======================================================================================
# 3) Learn More about Yield, next and Generators
"""
Yield: 
The yield statement suspends function’s execution and sends a value back to the caller, 
but retains enough state to enable function to resume where it is left off. When resumed, 
the function continues execution immediately after the last yield run. 
This allows its code to produce a series of values over time, rather than computing them at once and sending them back like a list.

Next:
The next() function returns the next item in an iterator.
You can add a default return value, to return if the iterable has reached to its end.

Generators:
A generator-function is defined like a normal function, 
but whenever it needs to generate a value, it does so with the yield keyword rather than return. 
If the body of a def contains yield, the function automatically becomes a generator function.

"""
# ======================================================================================
# 4)Write a program in Python using generators to reverse the string.
# Input String = “Consultadd Training”
# generator to reverse a string


def reverse_string(my_str):
    length = len(my_str)
    for i in range(length-1, -1, -1):
        yield my_str[i]


# using for loop to reverse the string
for char in reverse_string("Consultadd Training"):
    print(char)

# ======================================================================================
# 5)Write an example on decorators.


def hello_decorator(func):

    def inner1():
        print("Hello, this is before function execution")
        func()
        print("This is after function execution")
    return inner1


def function_to_be_used():
    print("This is inside the function !!")


function_to_be_used = hello_decorator(function_to_be_used)
# calling the function
function_to_be_used()
