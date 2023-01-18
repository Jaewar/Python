# Jacob L Stewart
# Chapter 4 Assignment 05
# Asks user to input values and then calculates the
# average, smallest, largest and difference from smallest and largest
from statistics import mean


def assignment4_05():
    # counter to track number of integers entered
    minNumberCount = 0
    # list to hold user inputted numbers
    providedNumbers = []

    # Asks user how many numbers they want to use and then value checks for whole numbers.
    invalid = True
    while invalid:
        try:
            totalNumbersExpected = int(input("How many numbers would you like to input? "))
            invalid = False
        except ValueError:
            print("Please enter a whole number.")

    # gets user input until the above amount of floating-point integers are collected
    while minNumberCount < totalNumbersExpected:
        try:
            userInputtedNumbers = [float(input("Enter a number with a decimal value: "))]
            minNumberCount += 1
            # adds user input to list of numbers
            providedNumbers += userInputtedNumbers
        except ValueError:
            print("Value error, numbers expected. Letters detected, please re-enter your digit.")

    # prints provided numbers then the average, smallest, largest and difference.
    print("Values Given:", providedNumbers, "\n ======================" )
    # print("Average of numbers provided:", round(sum(providedNumbers)/len(providedNumbers), 2))
    print("Average of numbers provided:", round(mean(providedNumbers), 2))
    print("Smallest number provided:", min(providedNumbers))
    print("Largest number provided:", max(providedNumbers))
    print("Difference between largest and smallest number:",
          round(max(providedNumbers) - min(providedNumbers), 2))


assignment4_05()


