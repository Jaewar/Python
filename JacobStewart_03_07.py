# Jacob L Stewart
# Chapter 3 Assignment 07
# Write a program that reads in three integers and prints “in order” if they are sorted
# in ascending or descending order, or “not in order” otherwise

def assignment3_07():
    # gets user inputs
    num1 = input("Please enter first number: ")
    num2 = input("Please second first number: ")
    num3 = input("Please third first number: ")

    # checks user input for ascending or descending order (also works with letters and strings) and prints result
    if num1 < num2 < num3 or num1 > num2 > num3:
        print("In order")
    else:
        print("Not in order")


assignment3_07()

