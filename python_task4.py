
# 1) Write a program to reverse a string.
from functools import reduce


def reverse(string):
    string = string[::-1]
    return string


print(reverse("1234abcd"))
# -------


def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str


print(reverse("1234abcd"))

# ===========================================================
# 2) Write a function that accepts a string and prints the number of uppercase letters and lowercase
# letters.


def up_low(string):
    uppers = 0
    lowers = 0
    for char in string:
        if char.islower():
            lowers += 1
        elif char.isupper():
            uppers += 1
    return(uppers, lowers)


u, l = up_low("abcSdefPghijQkl")
print("No.of upper case characters: {},\nNo of Lower case characters : {}".format(u, l))

# ===========================================================
# 3) Create a function that takes a list and returns a new list with unique elements of the first list.


def newlist(list):
    list1 = []
    for i in list:
        if i not in list1:
            list1.append(i)
    return list1


inputList = [1, 1, 2, 2, 3, 3, 4, 4, 5, 6]
print(newlist(inputList))

# ===========================================================
# 4) Write a program that accepts a hyphen-separated sequence of words as input and prints the words
# in a hyphen-separated sequence after sorting them alphabetically.
s = input("Enter a hypen seperated words: ")


def hyphen(s):
    s = s.split("-")
    s.sort()
    print('-'.join(s))

# ===========================================================
# 5) Write a program that accepts a sequence of lines as input and prints the lines after making all
# characters in the sentence capitalized.


lines = []
while True:
    l = input("Enter words: (Press enter to break) : ")
    if l:
        lines.append(l.upper())
    else:
        break
for l in lines:
    print(l)

# ===========================================================
# 6) Define a function that can receive two integral numbers in string form and compute their sum and
# print it in the console.
a = int(input("Enter first integer: "))
b = int(input("Enter second integer:"))


def addition(a, b):
    add = a + b
    return add


print(addition(a, b))

# ===========================================================
# 7)Define a function that can accept two strings as input and print the string with the maximum length
# in the console. If two strings have the same length, then the function should print both the strings line
# by line.

a = input("Enter str 1:")
b = input("Enter Str 2:")


def samelen(a, b):
    if len(a) > len(b):
        return a
    elif len(a) < len(b):
        return b
    else:
        return a, b


print("The longest str is : ", samelen(a, b))

# ===========================================================
# 8) Define a function which can generate and print a tuple where the values are square of numbers
# between 1 and 20 (both 1 and 20 included).


def tup():
    list1 = []
    for i in range(1, 21):
        list1.append(i**2)
    print(tuple(list1))


tup()

# ===========================================================
# 9)Write a function called showNumbers that takes a parameter called limit. It should print all the
# numbers between 0 and limit with a label to identify the even and odd numbers.


def shownumber(limit):

    for i in range(0, limit+1):
        if i == 0:
            print(i, end=" ")
            print("EVEN")
        elif i % 2 == 0:
            print(i, end=" ")
            print("EVEN")
        else:
            print(i, end=" ")
            print("ODD")


print(shownumber(5))

# ===========================================================
# 10)Write a program which uses filter() to make a list whose elements are even numbers between 1
# and 20 (both included)
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def is_even(x):
    return x % 2 == 0


list2 = list(filter(is_even, list1))
print(list2)

# ===========================================================
# 11)Write a program which uses map() and filter() to make a list whose elements are squares of even
# numbers in [1,2,3,4,5,6,7,8,9,10].
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result1 = filter(lambda x: x % 2 == 0, list1)

result = map(lambda x: x**2, result1)
print(list(result))

# ===========================================================
# 12)Write a function to compute 5/0 and use try/except to catch the exceptions


def div(x, y):
    try:
        result = x//y
        return result
    except ZeroDivisionError:
        return "not divisible by zero"


print(div(5, 0))

# ===========================================================
# 13)Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce().
list_of_nums = [1, 2, 3, 4, 5, 6, 7]
final_str = reduce(lambda a, b: str(a) + str(b), list_of_nums)
print(final_str)

# ===========================================================
# 14)Write a program in Python to find the values which are not divisible by 3 but are a multiple of 7.
# Make sure to use only higher order functions.
integers = range(0, 101)
print(list(filter(lambda x: x % 3 != 0 and x % 7 == 0, integers)))

# ===========================================================
# 15)Write a program in Python to multiply the elements of a list by itself using a traditional function
# and pass the function to map() to complete the operation.


def square(x):
    return x * x


nums = [1, 2, 3, 4, 5]
nums_squared = map(square, nums)
print(list(nums_squared))

# ===========================================================
# 16)What is the output of the following codes:
# (i)


def foo():
    try:
        return 1
    finally:
        return 2


k = foo()
print(k)
#Output : 2

# (ii)


def a():
    try:
        f(x, 4)
    finally:
        print('after f')
        print('after f?')


a()
# Output: NameError: name 'f' is not defined
