# TASK-1 : Numbers and Variables:
# 1. Create three variables in a single line and assign values to them in such a manner that each one of them belongs to a different data type.

a, b, c = 1, 'abc', 0.21
print(a, b, c)

print('-' * 50)
# ------------------------------------------------------------------------------------
# 2. Create a variable of type complex and swap it with another variable of type integer.
a = 1+2j
b = 2

print(a, "is complex number?", isinstance(a, complex))

temp = a
a = b
b = temp


print('The value of a after swapping: {}'.format(a))
print('The value of b after swapping: {}'.format(b))

print('-' * 50)

# -------------------------------------------------------------------------------------
# 3.Swap two numbers using a third variable and do the same task without using any third variable.
x = 8
y = 5

x, y = y, x

"""temp = x
x = y
y = temp"""

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))
print('-' * 50)

# -------------------------------------------------------------------------------------
# 4. Write a program that takes input from the user and prints it using both Python 2.x and Python 3.x Version.
a = input("Enter a letter: ")
print("The letter you entered is: {}".format(a))
print('-' * 50)
# -------------------------------------------------------------------------------------
""" 5. Write a program to complete the task given below:
Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum in
another variable called z. Add 30 to z and store the output in variable result and print result as the
final output."""

x, y = input("enter two numbers between 1 to 10 : ").split()

z = int(x) + int(y)
result = int(z) + 30

print("your final output is : {}".format(result))
print('-' * 50)


# -------------------------------------------------------------------------------------
# 6. Write a program to check the data type of the entered values.
# HINT: Printed output should say - The data type of the input value is : int/float/string/etc

# anything given to input function will be considered as string
x = input("Enter anything : ")
print(type(x))

x = 2
print(type(x))

y = "abc"
print(type(y))

z = 0.01
print(type(z))

print('-' * 50)

# -------------------------------------------------------------------------------------
# 7.Create Variables using formats such as Upper CamelCase, Lower CamelCase, SnakeCase and UPPERCASE.

# upper camelcase :
VariableDeclarationInPython = 1
# lower camelcase :
variableDeclarationInPython = 2
# snake case      :
variable_declaration_in_python = 3
# UPPERCASE       :
VARIABLEDECLARATIONINPYTHON = 4
print('-' * 50)

# -------------------------------------------------------------------------------------
# If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’ again.
# Will it change the value? If Yes then Why?
""" Yes, the value of a changes to the last assigned value in the sequence of code. Python executes the code one line at a time(line by line).
Hence, whichever value is assigned and executed by the end of the program will be value for variable a. """
