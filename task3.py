
# 1) Create a list of 10 elements of four different data types like int, string, complex and float.
list1 = [1, 2, "abc", "def", 2+2j, 3+4j, 0.01, 0.8, 3, 4]
print(list1)

# ---------------------------------------------------------------------------
# 2) Create a list of size 5 and execute the slicing structure

list2 = [1, 2, [0, 5], "abc", 9]
print(list2[1:4:1])

# ---------------------------------------------------------------------------
# 3) Write a program to get the sum and multiply of all the items in a given list.

list3 = [1, 2, 3, 4, 5]
result0 = 0
result1 = 1

for i in list3:
    result0 = result0 + i
    result1 = result1 * i

print(result0, result1)

# ---------------------------------------------------------------------------
# 4) Find the largest and smallest number from a given list.
list4 = [1, 2, 3, 4, 5]
largest = max(list4)
smallest = min(list4)
print(largest, smallest)

# ---------------------------------------------------------------------------
# 5) Create a new list which contains the specified numbers after removing the even numbers from a
# predefined list
list5 = list(range(0, 100, 1))
evenlist = []
for i in list5:
    if i % 2 == 0:
        evenlist.append(i)
print(evenlist)

# ---------------------------------------------------------------------------
# 6)Create a list of elements such that it contains the squares of the first and last 5 elements between
# 1 and 30 (both included).
list6 = list(range(1, 31, 1))
sqlist = []
for i in list6:
    sqlist.append(i * i)
sqlist = [sqlist[n] for n in (0, 1, 2, 3, 4, -5, -4, -3, -2, -1)]
print(sqlist)

# -----------------------------------------------------------------------------
# 7)Write a program to replace the last element in a list with another list.
a = [1, 3, 5, 7, 9, 10]
b = [2, 4, 6, 8]
a[-1:] = b
print(a)

# -----------------------------------------------------------------------------
# 8) Create a new dictionary by concatenating the following two dictionaries
a = {1: 10, 2: 20}
b = {3: 30, 4: 40}
c = {}
for i in a, b:
    c.update(i)
print(c)

# -----------------------------------------------------------------------------
# 9)Create a dictionary that contain numbers in the form(x:x*x) where x takes all the values between 1
# and n(both 1 and n included).
n = int(input("Enter a number : "))
a = {}
for i in range(1, n+1):
    a[i] = i*i
print(a)

# -----------------------------------------------------------------------------
# 10)Write a program which accepts a sequence of comma-separated numbers from console and
# generates a list and a tuple which contains every number in the form of string.
n = input("Enter a comma seperated seq of numbers :")

alist = n.split(',')
btuple = tuple(alist)
print(alist, btuple)
