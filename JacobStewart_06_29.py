# Jacob L Stewart
# Chapter 06 Assignment 29
# program simply attaches one list to another (modification for user inputted list possible)
# Assignment didn't call for user input so ill reuse my getRandomInts() from assignment 1 CH 6.
import random


def main():
    # generates 2 random lists of 5 integers
    randList1 = getRandomInts()
    randList2 = getRandomInts()
    # displays both lists first
    print("First list:", randList1)
    print("Second list:", randList2)
    # calls function to append list1 to list2
    appendList(randList1, randList2)


def getRandomInts():
    randomIntegerList = []
    # for loop that generates a random #1-30 until 5 numbers are stored
    for i in range(0, 5):
        rndInt = random.randint(1, 30)
        randomIntegerList.append(rndInt)
    return randomIntegerList


# @param appendedList stores value of list A after B is attached then prints output.
def appendList(a, b):
    a.append(b)
    appendedList = a
    return print("List using append:", appendedList)


main()
