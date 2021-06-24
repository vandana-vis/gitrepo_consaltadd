"""
# 1) Write a program that calculates and prints the value according to the given formula:
# Q= Square root of [(2*C*D)/H]
# Following are the fixed values of C and H:
# C is 50.
# H is 30.
# D is a variable whose values should be input to your program in a comma-separated sequence.

import math
C = 50
H = 30
D = int(input("Enter D value : "))
Q = math.sqrt((2*C*D)/H)
print(Q)

# ==============================================================================================
# 2) Define a class named Shape and its subclass Square. The Square class has an init function which
# takes length as argument. Both classes have an area function which can print the area of the shape
# where Shape’s area is 0 by default.


class Shape():
    def __init__(self):
        pass

    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length=0):
        Shape.__init__(self)
        self.length = length

    def area(self):
        return self.length*self.length


Asqr = Square(5)
print(Asqr.area())      # prints 25
print(Square().area())  # prints à

# ==============================================================================================
# 3) Create a class to find three elements that sum to zero from a set of n real numbers
# Input array: [-25,-10,-7,-3,2,4,8,10]
# Expected output: [[-10,2,8],[-7,-3,10]]


class sumZero:
    def __init__(self, realNumberArray):
        self.realNumberArray = realNumberArray
        self.n = len(self.realNumberArray)

    def findSumZero(self):
        foundList = []
        for i in range(0, self.n - 2):
            for j in range(i + 1, self.n-1):
                for k in range(j + 1, self.n):
                    if(self.realNumberArray[i] + self.realNumberArray[j] + self.realNumberArray[k] == 0):
                        foundList.append(
                            [self.realNumberArray[i], self.realNumberArray[j], self.realNumberArray[k]])
        return foundList


sumObj = sumZero([-25, -10, -7, -3, 2, 4, 8, 10])
foundList = sumObj.findSumZero()
print(foundList)

# ==============================================================================================
# 4) Create a Time class and initialize it with hours and minutes.
# Create a method addTime which should take two Time objects and add them.
# E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
# Create another method displayTime which should print the time.
# Also create a method displayMinute which should display the total minutes in the Time.
# E.g.- (1 hr 2 min) should display 62 minute.


class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def addTime(self, other):
        temp = (((self.hours + other.hours) * 60) +
                (self.minutes + other.minutes))
        self.totalHours = temp // 60
        self.totalMinutes = temp % 60

    def displayTime(self):
        print(self.totalHours, " hr and ", self.totalMinutes, " min")

    def displayMinute(self):
        print(self.hours * 60 + self.minutes, " minutes")

timeObj1 = Time(2, 50)
timeObj1.displayMinute()
timeObj2 = Time(1, 20)
timeObj2.displayMinute()

timeObj1.addTime(timeObj2)

timeObj1.displayTime()

"""
# ==============================================================================================
# 5) Write a Person class with an instance variable “age” and a constructor that takes an integer as a
# parameter. The constructor must assign the integer value to the age variable after confirming the
# argument passed is not negative; if a negative argument is passed then the constructor should set
# age to 0 and print “Age is not valid, setting age to 0”. In addition, you must write the following instance
# methods:


class Person:
    age = 0

    def __init__(self, initialAge):
        # Add some more code to run some checks on initialAge
        if initialAge < 0:
            print("Age is not valid, setting age to 0.")
        else:
            self.age = initialAge

    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.age < 13:
            print("You are young.")
        elif self.age >= 13 and self.age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")

    def yearPasses(self, addYears):
        # Increment the age of the person in here
        self.age += addYears
        print("Age after incrementing", addYears, "years is ", self.age)


personObj = Person(64)
personObj.amIOld()
personObj.yearPasses(30)
