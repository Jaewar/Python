# Jacob L Stewart
# Chapter 2 Assignment 04
# Prompts user for 2 integers and displays mathematical functions using
# both inputs.


def assignment2_4():
    # continuous loop that verifies that the input is an integer.
    while True:
        try:
            num1 = int(input("Input a number: "))
            # catches error and prompts user to reenter
        except ValueError:
            print("Error! Please enter a number. Try again.")
            # breaks out of current loop to retrieve second number
        else:
            break
    # loop that verifies the input is an integer then displays required results
    while True:
        try:
            num2 = int(input("Input a second number: "))
            # catches error and prompts user to reenter
        except ValueError:
            print("Error! Please enter a number. Try again.")
            # displays required equations after 2 integers are input.
        else:
            print("Sum:", num1 + num2)
            print("Difference:", num1 - num2)
            print("Product:", num1 * num2)
            print("Average:", (num1+num2)/2)
            print("Distance:", abs(num1-num2))
            print("Maximum:", max(num1, num2))
            print("Minimum:", min(num1, num2))
            break


assignment2_4()
