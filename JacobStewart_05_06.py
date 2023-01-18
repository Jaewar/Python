# Jacob L Stewart
# Chapter 5 Assignment 6
# Asks the user for a string and displays the number of vowels in the string regardless of case.

def assignment05_06():
    # prompts user for input and prints input followed by amount of vowels.
    userString = input("Please input a sentence or word: ")
    print(userString, "\nNumber of vowels found:", countVowels(userString))


# Finds the number of vowels in a string
# @param string : the input given by the user
# @return the number of vowels in given string
def countVowels(string):
    vowels = 0
    for char in string:
        # converts string to lower to account for possible UPPERCASE
        if char.lower() in "aeiou":
            vowels = vowels + 1
    return vowels


assignment05_06()
