# 1)
x = input("Enter a number :")
if int(x) % 3 == 0 and int(x) % 5 == 0:
    print("Consultadd - Python Training")
elif int(x) % 3 == 0:
    print("Consultadd")
elif int(x) % 5 == 0:
    print("Python Training")

print('-' * 50)

# ---------------------------------------------------------------------------------
# 2)
y = int(input("Enter a number between 1 and 5\n 1 : Addition\n 2 : Subtraction\n 3 : Division\n 4 : Multiplication\n 5 : Average \n"))
if y == 1 or y == 2 or y == 3 or y == 4:
    num1 = int(input("Enter num 1: "))
    num2 = int(input("Enter num 2: "))
    if y == 1:
        z = (num1 + num2)
        print(z)
    elif y == 2:
        z = (num1 - num2)
        print(z)
    elif y == 3:
        z = (num1 / num2)
        print(z)
    elif y == 4:
        z = (num1 * num2)
        print(z)
if y == 5:
    first = int(input("Enter first number : "))
    second = int(input("Enter second number : "))
    z = (first + second)/2
    print(z)
if z < 0:
    print("NEGETIVE")

print('-' * 50)

# ---------------------------------------------------------------------------------
# 3)
a = 10
b = 20
c = 30

avg = (a + b + c)/3
print("avg =", avg)

if avg > a and avg > b and avg > c:
    print("avg is higher than a, b, c")
elif avg > a and avg > b:
    print("average is higher than a and b")
elif avg > a and avg > c:
    print("average is higher than a and c")
elif avg > b and avg > c:
    print("average is higher than b and c")
else:
    if avg > a:
        print("avg is just higher than a")
    elif avg > b:
        print("avg is just higher than b")
    elif avg > c:
        print("avg is just higher than c")

print('-' * 50)

# --------------------------------------------------------------------------------
# 4)
while True:
    x = int(input("Enter a number: "))
    if x < 0:
        print("It's over")
        break
    else:
        print("Good Going")
        continue
print('-' * 50)

# --------------------------------------------------------------------------------
# 5)
for i in range(2000, 3201):
    if i % 7 == 0 and not(i % 5 == 0):
        print(i)
print('-' * 50)


# --------------------------------------------------------------------------------
# 6)
x = 123
for i in x:
    print(i)

# Output: TypeError: 'int' object is not iterable

i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
    else:
        print("error")

# output :
# 0
# error
# 1
# error
# 2

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Output:
# 0
# 1
# 2
# 3
# 4

# --------------------------------------------------------------------------------
# 7)
for i in range(7):
    if i == 3 or i == 6:
        continue
    else:
        print(i)

# --------------------------------------------------------------------------------
# 8)
Letters = 0
Digits = 0

str = input("Enter a string with letters and digits: ")
for i in str:
    if i.isdigit():
        Digits += 1
    elif i.isalpha():
        Letters += 1
print("Letters  ", Letters)
print("Digits  ", Digits)


# --------------------------------------------------------------------------------
# 9)
number = int(input("Guess the lucky number :"))
while number != 5:
    print("That is not the lucky number")
    number = int(input("Guess the lucky number "))

# (or)

number = 0
again = "yes"
while number != 5 and again != "no":
    number = int(input("Guess the lucky number: "))
    if number != 5:
        print("That is not the lucky number")
        again = input("Would you like to guess again? (yes or no) :")


# --------------------------------------------------------------------------------
# 10)
counter = 1
while counter <= 5:
    x = int(input("Type in the " + str(counter) + " number :"))
    counter += 1
    if counter <= 5 and x == 5:
        print("Good Guess!")
    elif counter <= 5 and x != 5:
        print("Try Again!")
    else:
        print("Game Over!")

# --------------------------------------------------------------------------------
# 11)
counter = 1
hits = 1
while counter <= 5:
    number = int(input("Guess the " + str(counter) + ". time :"))
    if number != 5:
        print("Try again.")
    else:
        print("Good guess!")
        break
    hits = hits + 1
    counter = counter + 1
else:
    print("Sorry but that was not very successful")
