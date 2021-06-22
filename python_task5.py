"""
# 1) Write a program in Python to allow the error of syntax to be handled using exception handling.
# HINT: Use SyntaxError
try:
    a = int(input("Enter a number: "))
    while a == 0  # No semi-colon to induce syntax error
    break
except Exception:
    print("Sorry, my fault!")
finally:
    print("This is a final block of code")


# =============================================================================
# 2) Write a program in Python to allow the user to open a file by using the argv module. If the
# entered name is incorrect throw an exception and ask them to enter the name again. Make sure
# to use read only mode.
import sys
arg = sys.argv[1]
try:
    with open(arg, 'r') as infile:
        print(infile.read())
except FileNotFoundError:
    print(f"The file {arg} does not exist, try again")
    raise(SystemExit)

# =============================================================================
# 3) Write a program to handle an error if the user entered a number more than four digits it should
# return “The length is too short/long !!! Please provide only four digits”
try:
    a = input("enter a four digit number: ")
    if len(a) == 4:
        pass
    else:
        raise Exception
except Exception:
    print("The length is too short/long !!! Please provide only four digits")

# =============================================================================
# 4)Create a login page backend to ask users to enter the username and password. Make sure to
# ask for a Re-Type Password and if the password is incorrect give chance to enter it again but it
# should not be more than 3 times.

count = 0
while True:
    try:
        userName = input("Enter as required! \nUsername: ")
        password = input("Password: ")
        retype = input("Retype password: ")
        count += 1
        if count == 3:
            print("you have exceeded the limit. Better luck next time")
            break  # exit
        elif userName == 'elmo' and password == 'blue' and retype == password:
            print("you are in!!")
            break  # they are in, exit loop
        else:
            raise Exception
    except Exception:
        print("Either username or password is entered wrong")

# =============================================================================
# 5)Go through the link provided below to understand finally and raise concept:
# https://www.programiz.com/python-programming/exception-handling
"""
# =============================================================================
# 6)Read doc.txt file using Python File handling concept and return only the even length string from
# the file. Consider the content of doc.txt as given below:
#open("doc.txt", "x")
"""
# ---create a file and write into file: ---
f = open("doc.txt", "w")
f.write("Hello I am a file\nWhere you need to return the data string\nWhich is of even length\nMake sure you return the content in The same link as it is present.")
"""
f = open("doc.txt", "r")
Lines = f.readlines()

# Strips the newline character
for line in Lines:
    if len(line) % 2 == 0:
        print('Length: ', len(line), "\nLine:", line.strip())
